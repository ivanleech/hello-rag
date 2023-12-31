from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import CTransformers
from langchain.embeddings.huggingface import HuggingFaceEmbeddings

if __name__ == "__main__":
    # Load the PDF, split texts into chunks, and embed chunks using embedding LLM(all-MiniLM-L6-v2)
    pdf_path = "assets/uob.pdf"
    loader = PyPDFLoader(file_path=pdf_path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(
        chunk_size=200, chunk_overlap=30, separator="\n"
    )
    docs = text_splitter.split_documents(documents=documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Save vector embeddings to FAISS(In-memory vectorstore)
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("faiss_index")
    new_vectorstore = FAISS.load_local("faiss_index", embeddings)

    # Retrieve similar vectors from FAISS and generate answer using chat LLM(zephyr-7b-beta.Q4_K_M.gguf)
    llm = CTransformers(
        model="/home/ivanleech/apps/github_new/llm/zephyr-7b-beta.Q4_K_M.gguf",
        model_type="mistral",
        lib="avx2",
    )
    qa = RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=new_vectorstore.as_retriever()
    )

    qn = "What are the eligible cards?"
    res = qa.run(qn)
    print(f'❓Qn: {qn} \n✅ Ans: {res}')
    print()

    qn = "What are the transactions that does not count?"
    res = qa.run(qn)
    print(f'❓Qn: {qn} \n✅ Ans: {res}')
