### Welcome to Text to SQL from Google-Gemini-model

<b>Step 1.</b> Clone this repository: https://github.com/bhautik-pithadiya/Text2Sql-Google-Gemini.git
<br/><br/>
<b>Step 2.</b> Create a new virtual environment 
<pre>
python -m venv tfod
</pre> 
<br/>
<b>Step 3.</b> Activate your virtual environment
<pre>
source tfod/bin/activate # Linux
.\tfod\Scripts\activate # Windows 
</pre>

<b>Step 4.</b> Install dependencies

    pip install -r requiements

<b>Step 4.</b> Now create a file named .env and add your api from <a href= 'https://aistudio.google.com/app/apikey'>aistudio</a>

    GOOGLE_API_KEY = 'YOUR API KEY'

<b>Step 5.</b> Now let's startup the streamlit app

    streamlit run app.py

## Demo
![Video Name](images/demo.webm)
