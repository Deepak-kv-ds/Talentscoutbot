SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are TalentScout, an AI hiring assistant. "
        "Your task is to generate technical interview questions "
        "based strictly on the candidate's declared tech stack. "
        "Do not answer unrelated questions."
    )
}

def tech_question_prompt(tech_stack):
    return {
        "role": "user",
        "content": (
            f"Candidate tech stack: {tech_stack}\n\n"
            "Generate 3 to 5 technical interview questions per technology. "
            "Questions should start from basics and go to intermediate/advanced. "
            "Focus on practical, real-world understanding. "
            "Return the questions as clear bullet points grouped by technology."
        )
    }
