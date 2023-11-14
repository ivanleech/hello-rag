# hello-rag

![Alt text](./assets/dunk.png.jpg)

Run RAG(retrieval augmented generation) using FAISS and langchain in 2 simple steps


### Step1: Download Chat LLM
Download chat LLM model(zephyr-7b-beta.Q4_K_M.gguf) from huggingface. The GGUF format is suitable for CPU usage.
The model at point of writing is one of the best performing LLM model with 7B parameters.
https://huggingface.co/TheBloke/zephyr-7B-beta-GGUF/tree/main


### Step2: Install requirements and run the code
```
pip install -r requirements.txt
python3 hello-rag.py
```

