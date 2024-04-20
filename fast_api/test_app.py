from dotenv import load_dotenv

load_dotenv() ## load all the environment variables 

import streamlit as st
import os
import sqlite3
import io

import google.generativeai as genai

## Configure our API key
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

def get_database_schema(uploaded_file):
    if uploaded_file is not None:
        with uploaded_file:

            conn = sqlite3.connect(':memory:')  # Use in-memory SQLite database
            # You can also connect to a file: conn = sqlite3.connect(uploaded_file.name)
            cursor = conn.cursor()

            # Read and execute SQL commands from the uploaded file
            script = uploaded_file.read().decode('iso-8859-1')
            cursor.executescript(script)

            # Fetch and return the tables from the database
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = cursor.fetchall()
            
            ## Store in a List
            schema = []
            for table in tables:
                temp = ''
                temp += f"Table Name: {table[0]}"
                temp += f"\nSchema: \n{table[1]}"
                temp+='\n'
                schema.append(temp)

            # Close the cursor and connection
            cursor.close()
            conn.close()
        
        return schema


## Function to Load Google Gemini MODel and provide sql query as responce

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt,question])
    return response.text

## Function to retrieve query from the sql database

def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()

    for row in rows:
        print(row)

    return rows


# Define Your Prompt
if __name__ == "__main__":
    ## Streamlit APP

    st.set_page_config(page_title = 'I can Retr-ieve Any SQL query')
    st.header("Upload Your Database")
    uploaded_file = st.file_uploader('Upload the database file',type=['db'] )
    schema = get_database_schema(uploaded_file)
    print(schema)

    prompt = [
        f"""
        You are an expert in converting English question to SQL query!
        The Following is the schema {schema}\n\n
        For Example, \nExample 1 - How many entries of records are present? the SQL command will be something this
        SELECT COUNT(*) FROM STUDENT ;
        \nExample 2 - Tell me all the students studying  in Data Science class?,
        the SQL command will be something like this SELECT * FROM STUDENT where CLASS = "DATA Science";
        also the sql code should not have this ``` in beginning or end and sql word in output 
    """
    ]
    
    st.header("Gemini App to Retrieve SQL Data")

    question = st.text_input('Input: ',key = 'input')

    submit = st.button("Ask the Question")

    # If submit is clicked 
    if submit:
        response = get_gemini_response(question,prompt[0])

        st.subheader('The Query is')
        print((response))

        data = read_sql_query(response, "test.db")

        st.subheader('The Response is')

        for row in data:
            print(row)
            st.header(row)
