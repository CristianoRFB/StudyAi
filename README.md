# StudyAI — Assistente de Estudos com RAG

Projeto AV_FINAL de Inteligência Artificial e Aprendizagem de Máquina.

## Objetivo

Responder perguntas sobre o guia da Aula 28, recuperando trechos verificáveis de 108 entradas. Versão Python com TF-IDF, Streamlit e Gemini opcional; demonstração web em Cloudflare Worker com busca léxica e Gemini via secret.

## Rodar localmente

```bash
pip install -r requirements.txt
streamlit run interface.py
```

Sem chave Gemini funciona apenas a recuperação documental, identificada como modo local. Configure `GEMINI_API_KEY` apenas no ambiente privado. Consulte `AGENTS.md` e `docs/state.md` antes de contribuir.

A equipe deve preencher autoria, validar o provedor Gemini e testar o deploy antes da entrega. Nenhum conteúdo privado de WhatsApp é armazenado.
