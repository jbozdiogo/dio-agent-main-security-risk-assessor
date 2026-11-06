import sqlite3
import hashlib
import hmac
import os
import time
import threading

# Configurações de segurança
ITERACOES_PBKDF2 = 100000
LIMITE_TENTATIVAS = 5
JANELA_TEMPO_SECONDS = 300  # 5 minutos
DB_PATH = 'usuarios.db'

# Rate limiting (em produção, use Redis ou sistema similar)
_tentativas = {}
_tentativas_lock = threading.Lock()


def gerar_hash_senha(senha):
    """Gera hash PBKDF2 com salt aleatório."""
    salt = os.urandom(32)
    hash_senha = hashlib.pbkdf2_hmac('sha256', senha.encode('utf-8'), salt, ITERACOES_PBKDF2)
    return salt.hex(), hash_senha.hex()


def verificar_senha(senha, salt_hex, hash_hex):
    """Verifica senha com compare_digest para evitar timing attacks."""
    salt = bytes.fromhex(salt_hex)
    hash_senha = bytes.fromhex(hash_hex)
    hash_calc = hashlib.pbkdf2_hmac('sha256', senha.encode('utf-8'), salt, ITERACOES_PBKDF2)
    return hmac.compare_digest(hash_calc, hash_senha)


def verificar_rate_limit(usuario):
    """Verifica e atualiza o rate limiting para o usuário."""
    with _tentativas_lock:
        agora = time.time()
        if usuario in _tentativas:
            ultimo_acerto, contador = _tentativas[usuario]
            if agora - ultimo_acerto >= JANELA_TEMPO_SECONDS:
                _tentativas[usuario] = (agora, 1)
            elif contador >= LIMITE_TENTATIVAS:
                return False
            else:
                _tentativas[usuario] = (agora, contador + 1)
        else:
            _tentativas[usuario] = (agora, 1)
    return True


def fazer_login(usuario, senha):
    """Função de login segura, sem vulnerabilidades críticas."""
    # 1. Rate limiting para prevenir força bruta
    if not verificar_rate_limit(usuario):
        return "Muitas tentativas. Tente novamente mais tarde."

    try:
        conexao = sqlite3.connect(DB_PATH)
        cursor = conexao.cursor()

        # Query parametrizada - prevenção a SQL Injection
        query = "SELECT senha_salt, senha_hash FROM usuarios WHERE usuario = ?"
        cursor.execute(query, (usuario,))
        resultado = cursor.fetchone()
        conexao.close()

        # 2. Resposta consistente para evitar enumeration de usuários por timing
        if resultado is None:
            time.sleep(0.3)
            return "Acesso negado"

        salt_hex, hash_hex = resultado

        # 3. Verifica senha com hash (não compara em texto puro)
        if not verificar_senha(senha, salt_hex, hash_hex):
            return "Acesso negado"

        # 4. Limpa o rate limit no sucesso
        with _tentativas_lock:
            if usuario in _tentativas:
                del _tentativas[usuario]

        return "Acesso concedido"

    except sqlite3.Error:
        # Em produção, registre o erro em log e retorne mensagem genérica
        return "Erro interno. Tente novamente mais tarde."
