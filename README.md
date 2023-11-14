# Hello-RAG: Run RAG using FAISS and langchain in 2 simple steps! 🚀
RAG = retrieval augmented generation
![hello-rag](./assets/dunk.png)

### Step 1: Download Chat LLM
Download chat LLM model(zephyr-7b-beta.Q4_K_M.gguf) from huggingface. The GGUF format is suitable for CPU usage.
The model at point of writing is one of the best performing LLM model with 7B parameters.

[![Huggingface](./assets/huggingface_logo.svg)](https://huggingface.co/TheBloke/zephyr-7B-beta-GGUF/tree/main)
https://huggingface.co/TheBloke/zephyr-7B-beta-GGUF/tree/main

### Step 2: Install requirements and run the code
```
pip install -r requirements.txt
python3 hello-rag.py
```

