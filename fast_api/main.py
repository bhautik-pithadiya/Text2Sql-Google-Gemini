from fastapi import FastAPI,File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import google.generativeai as genai
from pydantic import BaseModel
from dotenv import load_dotenv
import streamlit as st
import sqlite3
import shutil
import os
import io



load_dotenv() ## load all the environment variables

## Configure our API key
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

app = FastAPI()
app.mount("/files", StaticFiles(directory="static"), name="static")


class PromptRequest(BaseModel):
    text:str

class QueryResponse(BaseModel):
    text:str

def get_model():
    genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

@app.get("/", response_class=HTMLResponse)
async def read_index():
    # Return the HTML page with the form
    return open("static/index.html", "r").read()
# async def root():
#     return {"message": "Welcome to Text to SQL using GEMINI Model."}

@app.get('/text2sql',response_class = HTMLResponse)
async def read_index():
    return open('static/text2sql.html','r').read()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Save the uploaded file to a folder (you may want to validate the file)
        with open(f"uploads/{file.filename}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Process the file as needed
        
        return {"filename": file.filename, "message": "File uploaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post('/text2sql')
async def process_text(text: str):
    # Process the submitted text here (e.g., text-to-SQL conversion)
    # Replace this with your actual text-to-SQL processing logic
    
    # For demonstration purposes, I'm just returning the processed text
    processed_text = f"Processed text: {text}"
    
    return {"processed_text": processed_text}   
# async def get_text(request = PromptRequest):
    
#     try:
#         question = request.text


#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))