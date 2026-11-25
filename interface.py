import streamlit as st
from app import responder
st.set_page_config(page_title='StudyAI',page_icon='📚')
st.title('StudyAI | Assistente acadêmico')
st.caption('Base: guia da Aula 28 • respostas com fontes')
chave=st.sidebar.text_input('Chave Gemini (opcional)',type='password')
q=st.text_input('Sua pergunta',placeholder='Qual o prazo de entrega do relatório?')
if st.button('Consultar') and q.strip():
    try: resposta, fontes=responder(q,chave)
    except Exception as e:
        st.warning('API indisponível. Exibindo consulta local.'); resposta,fontes=responder(q)
    st.write(resposta)
    for d,s in fontes:
        with st.expander(f"Fonte {d['id']} • similaridade {s:.2f}"): st.write(d['texto'])
