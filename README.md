# StudyAI — Assistente acadêmico com recuperação de fontes

Projeto AV_FINAL de Inteligência Artificial e Aprendizagem de Máquina. Baseado no guia da Aula 28, com **108 trechos documentados**. O objetivo é responder dúvidas dos estudantes sobre prazos, critérios de avaliação, entregáveis e requisitos, sempre exibindo a origem da informação.

**Demonstração:** https://studyai-rfb.on7.workers.dev/  
**Status:** Worker habilitado e publicado por API. Abertura externa e Gemini ainda precisam de validação manual.

## Projeto Python: versão acadêmica

```bash
python -m venv .venv
# Ative o ambiente virtual no seu sistema
pip install -r requirements.txt
streamlit run interface.py
```

O algoritmo `app.py` utiliza TF-IDF (unigramas e bigramas), similaridade de cosseno e recuperação dos três trechos de maior relevância. Quando uma chave Gemini é fornecida, os trechos entram no prompt como contexto e o modelo gera uma resposta com IDs de fonte. Sem chave, mostra somente os trechos; não simula geração de texto.

- `guia.html`: material de referência (Aula 28);
- `build.py`: reconstrói `base.json` a partir do HTML;
- `base.json`: 108 documentos indexados;
- `testes.json`: seis consultas avaliadas manualmente (5 acertos em 6, **Hit@3 de 83,33%** apenas para o recuperador Python);
- `tests/test_retrieval.py`: testes automatizados;
- `interface.py`: interface Streamlit.

Para testar:

```bash
python -m unittest discover -s tests -v
python -m compileall -q app.py interface.py build.py
```

## Cloudflare: demonstração no navegador

O arquivo `worker.js` contém a interface HTML e a API de consultas. A indexação usa **sobreposição de termos**, não TF-IDF; é uma variante mais leve e não deve receber as mesmas métricas de precisão do Python. Os 108 trechos são divididos em oito bindings JSON (`DOC_0` a `DOC_7`) porque cada binding tem limite de tamanho.

A geração de respostas por Gemini está condicionada ao secret **`GEMINI_API_KEY`** configurado no Worker. Sem esse secret, a interface opera em modo documental. A versão online foi publicada por API; caso faça uma implantação nova, configure os oito bindings, a rota workers.dev e o secret na conta de destino. **Jamais coloque a chave em GitHub ou no JavaScript do navegador.**

O endpoint `/api/ask` não deve ser exposto com chave ativada para uso público irrestrito sem rate limiting e controle de abuso.

## RFB Method

O repositório contém `AGENTS.md`, `docs/state.md`, `docs/smoke.md`, `docs/tests.md`, `docs/design.md`, `docs/negotiation.md` e as pastas `human/`, `antivibecoding/`, `myown/`, `tests/`. Documentar todo teste real antes de declarar uma funcionalidade completa.

## Preparação para entrega — 02/12/2026

- Preencher integrantes e professor no relatório técnico.
- Confirmar com o professor a divergência no guia sobre o número de membros (o resumo cita 2–3 e outra seção, 2–4).
- Testar uma chamada Gemini de verdade com uma chave privada.
- Executar e gravar demonstração, screenshots e apresentação de 15 minutos.
- Conferir a documentação, revisão da PR e GitHub Actions.
- Não enviar ou indexar conversas privadas do WhatsApp.

**Limitações:** respostas sem contexto podem ser recusadas; sobreposição lexical não garante relevância semântica; métricas históricas não avaliam Gemini. O relatório PDF é um artefato de entrega separado do código.