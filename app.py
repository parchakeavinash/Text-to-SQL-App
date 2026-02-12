# the Logic code
# we wil connect Langchain with local Llama 3 model to the database

import streamlit as st
from langchain_community.utilities import SQLDatabase	
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#Page Setup

st.set_page_config(page_title = "Text_to_SQL-APP", layout = "centered")
st.title("Talk to Your Database")
st.write("Ask questions about the student grades database in plan English.")

# Database connection
db =SQLDatabase.from_uri("sqlite:///student_grades.db")

# Local LLM (Ollama)
llm = ChatOllama(
	model = "llama3.2:latest",
	temperature = 0	
)

# prompt (LCEl Style )
prompt = ChatPromptTemplate.from_template("""
	Your are a senior data analyst and sql expert.
	
	Given the database schema below, Write a correct sql query 
	that answers the user's question.

	Rules:
	- Use only the tables and columns in the schema
	- Do NOT explain anything
	- Return ONLY  the SQL query

	Schema:
	{schema}
	
	Question:
	{question}

""")
parser = StrOutputParser()

# LCEL Runnable Pipeline
sql_chain = (
	prompt
	| llm
	| parser
)

Schema = db.get_table_info()


# UI Input

question = st.text_input(
	'Enter your question: ',
	placeholder = 'e.g,, Who scored the highest in Math?')

# Execution

if question:
	try:
		sql_query=  sql_chain.invoke(
			{'schema': Schema, 'question': question}
		).strip()

		st.subheader("🧠 Generated SQL")
		st.code(sql_query, language="sql")

		st.subheader("✅ Result")
		result = db.run(sql_query)
		st.write(result)

	except Exception as e:
		st.error(f'❌ Error', e)
	

# footer
st.markdown("---")
st.caption("Powered by  Langchain | Ollama |  LLama3  | Streamlit")

