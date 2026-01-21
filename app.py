import streamlit as st
from llm import generate_questions
from prompt import SYSTEM_PROMPT, tech_question_prompt
EXIT_KEYWORDS = ["exit", "quit", "bye", "stop"]


st.set_page_config(page_title="TalentScout Hiring Assistant")

st.title("TalentScout Hiring Assistant")

if "stage" not in st.session_state:
    st.session_state.stage = "intro"

if "candidate" not in st.session_state:
    st.session_state.candidate = {}

user_input = st.chat_input("Type your response here...")

if st.session_state.stage == "intro":
    st.chat_message("assistant").write(
        "Hi! I’m TalentScout, your AI Hiring Assistant. Let’s start with your full name."
    )
    st.session_state.stage = "name"

elif user_input:
    st.chat_message("user").write(user_input)
    if user_input.lower() in EXIT_KEYWORDS:
        st.chat_message("assistant").write(
            "Thank you for your time! Our recruitment team will reach out to you shortly."
        )
        st.stop()

    if st.session_state.stage == "name":
        st.session_state.candidate["name"] = user_input
        st.chat_message("assistant").write("Thanks! What is your email address?")
        st.session_state.stage = "email"

    elif st.session_state.stage == "email":
        st.session_state.candidate["email"] = user_input
        st.chat_message("assistant").write(
            "Got it. How many years of experience do you have?"
        )
        st.session_state.stage = "experience"

    elif st.session_state.stage == "experience":
        st.session_state.candidate["experience"] = user_input
        st.chat_message("assistant").write(
            "Please list your tech stack (languages, frameworks, tools)."
        )
        st.session_state.stage = "tech_stack"

    elif st.session_state.stage == "tech_stack":
        st.session_state.candidate["tech_stack"] = user_input

        st.chat_message("assistant").write(
            "Great! Generating technical questions based on your tech stack..."
        )

        messages = [
            SYSTEM_PROMPT,
            tech_question_prompt(user_input)
        ]

        questions = generate_questions(messages)

        st.chat_message("assistant").write(questions)

        st.session_state.stage = "end"




    elif "end" == st.session_state.stage:
        st.chat_message("assistant").write(
            "Thanks for your time! Our team will contact you soon."
        )
