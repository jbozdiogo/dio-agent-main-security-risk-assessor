Fundamentos de Segurança da Informação
Objetivo
Este documento fornece conceitos fundamentais para análise de vulnerabilidades, avaliação de riscos e recomendação de controles defensivos.

Ativos
Um ativo é qualquer recurso que possua valor para a organização.

Exemplos:

Aplicações web
Servidores
Bancos de dados
Credenciais
Equipamentos de rede
Informações corporativas
Antes de analisar uma vulnerabilidade, identifique qual ativo está sendo protegido.

Vulnerabilidade
Uma vulnerabilidade é uma fraqueza técnica, operacional ou processual que pode ser explorada.

Exemplos:

SQL Injection
Senhas fracas
Software desatualizado
Configuração inadequada de firewall
Permissões excessivas
Perguntas importantes:

O atacante consegue explorar a falha remotamente?
A exploração exige autenticação?
Existe correção disponível?
Ameaças
Ameaças representam agentes ou eventos capazes de explorar vulnerabilidades.

Exemplos:

Cibercriminosos
Malware
Insider malicioso
Erro humano
Falhas de infraestrutura
Nem toda vulnerabilidade possui o mesmo nível de ameaça.

Avaliação de Risco
O risco deve considerar:

Impacto
Probabilidade
Impacto
Avalia as consequências para o negócio.

Baixo:

Pouca interrupção operacional.
Médio:

Afeta usuários ou sistemas não críticos.
Alto:

Afeta operações críticas ou expõe dados sensíveis.
Crítico:

Prejuízo financeiro significativo, indisponibilidade severa ou vazamento de informações estratégicas.
Probabilidade
Avalia a chance de exploração.

Baixa:

Necessita condições específicas.
Média:

Possui barreiras moderadas.
Alta:

Pode ser explorada facilmente.
Tríade CIA
Confidencialidade
Protege informações contra acesso não autorizado.

Exemplos de impacto:

Vazamento de credenciais.
Exposição de dados pessoais.
Integridade
Protege a precisão e consistência dos dados.

Exemplos:

Alteração não autorizada de registros.
Modificação de configurações críticas.
Disponibilidade
Garante acesso aos recursos quando necessário.

Exemplos:

Ataques de negação de serviço.
Indisponibilidade causada por ransomware.
MITRE ATT&CK
Quando possível, associe a análise a técnicas conhecidas do framework MITRE ATT&CK.

O objetivo não é decorar códigos, mas compreender o comportamento do atacante.

OWASP Top 10
Para aplicações web, considere especialmente:

Broken Access Control
Cryptographic Failures
Injection
Security Misconfiguration
Vulnerable and Outdated Components
Identification and Authentication Failures
Controles de Mitigação
Sempre priorize controles defensivos.

Exemplos:

Identidade
MFA
Senhas fortes
Privilégio mínimo
Infraestrutura
Firewall
Segmentação de rede
Hardening
Monitoramento
Logs
SIEM
EDR
Proteção de Dados
Criptografia
Backup
Controle de acesso
Formato de Resposta Esperado
Ao analisar uma vulnerabilidade, apresentar:

Resumo Executivo
Vulnerabilidade Identificada
Impacto
Probabilidade
Severidade
CIA Afetada
Possíveis Técnicas MITRE ATT&CK
Recomendações de Mitigação
Risco Residual