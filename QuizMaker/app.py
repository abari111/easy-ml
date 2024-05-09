from datetime import datetime
import io
import streamlit as st
import json
from utils import generate_text

st.markdown("""
    <style>
    .ans {
        font-weight: bold;
        color: green
    }
    .q {
        color: blue;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Simple Quiz App")
topic = st.text_area('Your prompt')
gen_btn = st.button('Generate')

output_format = """" {"Q1": {"label": question, "options": [opt1, opt2, opt3, opt3], 
                          "Correct": correct response}, "Q2": ...........}"""
prompt = f" create a quizz on {topic}n the answers." \
                f" Follow the following format {output_format}"

user_answers = []
with st.spinner('Generating image...'):
    if gen_btn:
        quiz = generate_text(prompt)
        quiz = json.loads(quiz)
        st.session_state.quiz = quiz
    
# # Display questions and checkboxes
if 'ans' not in st.session_state:
    st.session_state.ans = []
if 'user_ans' not in st.session_state:
    st.session_state.user_ans = []

i = 0

if 'quiz' in st.session_state:
    quiz = st.session_state.quiz
    for key in quiz.keys():
        # st.subheader(quiz[key]['label'])
        st.markdown(f"<p class='q'>{quiz[key]['label']}</p>", unsafe_allow_html=True)
        for option in quiz[key]['options']:
            opt_box = st.checkbox(option, key=i)
            i+=1
        if st.button('Show response', key='r'+str(i)):
            # st.text(quiz[key]['Correct'])
            st.markdown(f"<p class='ans'>{quiz[key]['Correct']}</p>", unsafe_allow_html=True)
        # st.session_state.ans.append((ans, quiz[key]['Correct']))
        user_answers.append(opt_box)

col1, col2 = st.columns(2)

def save_quiz(quiz):
    data = ""
    for key in quiz.keys():
        data += quiz[key]['label']
        data += quiz[key]['Correct'] 
    
    buffer = io.StringIO(data) 
    data = buffer.getvalue().encode('utf-8')
    return data

with col1:
    submit_btn = st.button('Submit')

with col2:
    if 'quiz' in st.session_state:
        data = save_quiz(st.session_state.quiz)
        st.download_button(
        label="Download",
        data=data,
        file_name=f'Quiz_{datetime.now()}.txt',
        mime="text" )

