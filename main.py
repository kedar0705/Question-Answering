from fastapi import FastAPI, Form
from transformers import pipeline
from typing import Annotated

app = FastAPI()

model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"
qa_model = pipeline("question-answering", model=model_name, tokenizer=model_name)

@app.post("/answer")
def answer_question(context: Annotated[str, Form()], question: Annotated[str, Form()]):
    result = qa_model(question=question, context=context)
    return {"answer": result["answer"]}

    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)