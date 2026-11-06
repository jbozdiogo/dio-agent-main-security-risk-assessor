DIO Agent - Security Risk Assessor
Descrição

Este projeto consiste na especialização do DIO Agent para atuar como um Analista de Riscos em Segurança da Informação, capaz de conduzir análises estruturadas de vulnerabilidades antes de sugerir correções.

Diferentemente de um chatbot tradicional que responde imediatamente, o agente foi configurado para:

Solicitar contexto antes de emitir recomendações;
Identificar ativos e superfície de ataque;
Avaliar impacto potencial;
Avaliar probabilidade de exploração;
Classificar severidade;
Relacionar riscos aos princípios da Segurança da Informação;
Sugerir medidas defensivas e mitigatórias.

O objetivo da especialização foi aproximar o comportamento do agente do fluxo de trabalho utilizado por profissionais de Cyber Security, AppSec e Infraestrutura.

Especialização Implementada

A especialização criada foi chamada de Security Risk Assessor.

Sua função é conduzir análises de segurança de forma estruturada, evitando conclusões precipitadas e incentivando a coleta de informações antes da tomada de decisão.

Principais características
Análise orientada por contexto;
Avaliação de vulnerabilidades;
Classificação de risco;
Aplicação da Tríade CIA;
Referenciamento de MITRE ATT&CK quando aplicável;
Recomendações de mitigação;
Foco em segurança defensiva.
Melhoria implementada

Como melhoria em relação ao agente base, foi adicionada uma regra que impede respostas imediatas para cenários de segurança.

Antes de sugerir qualquer correção, o agente deve:

Identificar o ativo analisado;
Compreender o contexto;
Identificar possíveis vulnerabilidades;
Avaliar impacto;
Avaliar probabilidade;
Classificar severidade;
Apresentar recomendações.

Dessa forma, o agente passa a se comportar mais próximo de um analista de segurança real.

Arquivos Criados e Alterados
Skill

Criada a skill:

Plain Text
skills/vulnerability-analysis/

Arquivos:

Plain Text
SKILL.md
README.md
 

Responsável por definir o fluxo de análise de vulnerabilidades utilizado pelo agente.

Conhecimento

Criado o arquivo:

Plain Text
agent/knowledge/security-basics.md

Conteúdo adicionado:

Vulnerabilidade;
Ameaça;
Risco;
Tríade CIA;
OWASP Top 10;
MITRE ATT&CK;
Boas práticas de segurança;
Controles defensivos.

Este conhecimento serve de base para as análises realizadas pelo agente.

Persona

Arquivo alterado:

Plain Text
agent/persona.md
 

Foi adicionada uma orientação para que o agente:

Faça perguntas antes de sugerir correções;
Priorize segurança defensiva;
Considere impacto, probabilidade e severidade;
Utilize linguagem técnica adequada.
AGENTS.md

Arquivo alterado:

Plain Text
AGENTS.md

Foi adicionada a referência da nova skill para que o agente saiba quando utilizá-la durante as interações.

Testes Realizados
1. Identificação de SQL Injection

Foi criado o arquivo:

app.py

contendo uma vulnerabilidade clássica de SQL Injection através da concatenação direta de parâmetros fornecidos pelo usuário.

O agente foi solicitado a analisar o código como um especialista em segurança de aplicações (AppSec).

Resultado

O agente foi capaz de:

Identificar a vulnerabilidade SQL Injection;
Explicar os riscos da concatenação de entradas do usuário;
Relacionar a falha a práticas inseguras de desenvolvimento;
Explicar o impacto potencial sobre a confidencialidade e integridade dos dados;
Sugerir a utilização de consultas parametrizadas.

2. Correção da Vulnerabilidade

Após a identificação do problema, foi solicitado ao agente que gerasse uma versão corrigida da aplicação.

Como resultado foi criado o arquivo:

appcorr.py
report.txt

contendo uma implementação segura utilizando consultas parametrizadas para mitigar a vulnerabilidade identificada.
e o output do que foi realizado pela IA.

Resultado

O agente foi capaz de:

Reescrever o código vulnerável;
Aplicar boas práticas de desenvolvimento seguro;
Eliminar a concatenação direta de entradas do usuário;
Reduzir significativamente o risco de exploração por SQL Injection.

3. Análise de Cenário de Infraestrutura

Foi apresentado ao agente o seguinte cenário:

"Quero analisar uma vulnerabilidade. Tenho um servidor Ubuntu exposto na internet e não sei por onde começar."

A principal validação deste teste foi verificar se o agente seguiria a metodologia definida na Skill.

Resultado

O agente não forneceu comandos ou correções imediatas.

Em vez disso, solicitou informações adicionais sobre:

Finalidade do servidor;
Versão do Ubuntu;
Ambiente de hospedagem;
Serviços expostos;
Configuração de firewall;
Método de autenticação SSH;
Estado de atualização do sistema;
Presença de dados sensíveis.

Esse comportamento demonstra que a Skill criada está funcionando corretamente e que o agente prioriza a coleta de contexto antes de realizar análises ou recomendações.