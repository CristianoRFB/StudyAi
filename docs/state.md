# Estado verificável — StudyAI (25/11/2026)

## Implementado
- Acervo do guia da Aula 28 em `guia.html` e `base.json`: 108 trechos.
- Versão Python: recuperação TF-IDF/cosseno, CLI, Streamlit e integração Gemini opcional.
- Versão Cloudflare: interface responsiva integrada ao Worker, recuperação léxica por palavras e endpoint `/api/ask`.
- Worker publicado em https://studyai-rfb.on7.workers.dev/ e ativado no subdomínio on7.
- Oito bindings JSON armazenam os 108 documentos sem credenciais no código.
- CI executa testes Python e smoke remoto Cloudflare; execução #45636053106 foi aprovada.
- Documentação RFB Method em AGENTS.md, docs/ e pastas de protocolos.

## Evidências e limites
- Teste de recuperação Python registrado em testes.json: cinco acertos entre seis consultas, Hit@3 = 83,33% para esse conjunto específico.
- Smoke Cloudflare (interface + fonte recuperada na API): aprovado em 25/11/2026. Não implica precisão semântica de 83,33% no Worker.
- Gemini real: **não testado**; secret GEMINI_API_KEY ainda precisa ser configurado e endpoint protegido de abuso.
- Relatório técnico PDF preparado em arquivo de entrega separado, não está no GitHub.
- Capturas reais, nomes e apresentação da equipe ainda pendentes.

## Próximos passos
1. Validar Gemini com segredo e limite de taxa (issue #2).
2. Finalizar relatório, vídeo e ensaio (issue #3).
3. Revisar qualidade da busca, discrepâncias e testes (issue #4).
4. Atualizar README e capturas somente com provas reais, sem inventar métricas de conclusão.
