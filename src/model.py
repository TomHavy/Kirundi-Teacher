from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain import PromptTemplate
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
# import chainlit as cl
import streamlit as st

DB_FAISS_PATH = 'vectorstore/db_faiss'

custom_prompt_template = """You are an expert of the Kirundi language. 
Using your knowledge and the context below, answer to the following question testing your Kirundi level.\
The context is 3 documents, extracts of Kirundi lessons. ""

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Answer:
"""

def set_custom_prompt():
    """
    Prompt template for QA retrieval for each vectorstore
    """
    prompt = PromptTemplate(template=custom_prompt_template,
                            input_variables=['context', 'question'])
    return prompt

#Loading the model
st.cache_data()
def load_llm():
    # Load the locally downloaded model here
    llm = CTransformers(
        model = "TheBloke/Llama-2-7B-Chat-GGML",
        # model="tomhavy/Llama-2-7b-chat-hf-sharded-bf16-fine-tuned-ENG-KIR",
        model_type="llama",
        max_new_tokens = 512,
        temperature = 0.5
    )
    return llm

st.cache_data()
def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                                       model_kwargs={'device': 'cpu'})
    db = FAISS.load_local(DB_FAISS_PATH, embeddings)
    return db


def main():
    query = st.chat_input()
    if query:
        with st.chat_message(name="user"):
            st.markdown(query)

        with st.spinner("Loading model..."):
            llm = load_llm()
            prompt = set_custom_prompt()
        
        with st.spinner("Finding relevant documents..."):
            db = load_vectorstore()
            docs = db.similarity_search(query, k=3)

        with st.spinner("Generating output..."):
            context=""
            for i, doc in enumerate(docs):
                context += f"Document {i+1}: {doc.page_content}\n\n"
            print(f"Context: \n{context}")
            answer = llm(prompt.format(context=context,question=query))

        with st.chat_message(name="assistant"):
            st.markdown(answer)
      
main()