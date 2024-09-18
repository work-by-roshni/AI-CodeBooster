import streamlit as st
import openai

# Create a left column in the Streamlit interface
left_column = st.sidebar

# Add a title and an input box for the OpenAI API key in the left column
left_column.title("OpenAI API key")
api_key = left_column.text_input("Enter your OpenAI API key:", type="password")
openai.api_key = api_key

# Streamlit UI
st.title('AI CodeBooster')

uploaded_file = st.file_uploader('Upload your code file', type=['.py'])


if api_key:
    openai.api_key = api_key
       

    if st.button ("Process"):
        if uploaded_file is not None:
           # Text extraction
         code_text = uploaded_file.read()

        # Code review using ChatGPT
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Review the following Python code such that first tell the 'Good about in the code', secondly tell 'Drawback about the code' and last 'review about the code' in detail and doll points. \n\n{code_text}\n\nReview: ",
            max_tokens=1024 # Adjust as needed
        )

        code_review = response.choices[0].text

        # Display code review
        st.subheader('Code Review:')
        st.write(code_review)


    
        