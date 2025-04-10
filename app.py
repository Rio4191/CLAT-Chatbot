
import streamlit as st
import difflib

st.set_page_config(page_title="CLAT Chatbot", page_icon="🎓")

st.title("🎓 CLAT Exam Chatbot")
st.markdown("Ask me **anything about CLAT 2025**! I'll try my best to answer it.")

#knowledge base
knowledge_base = {
    "syllabus": "CLAT 2025 includes: English Language, Current Affairs & GK, Legal Reasoning, Logical Reasoning, and Quantitative Techniques.",
    "subjects": "CLAT 2025 has the following subjects : English Language, Current Affairs & GK, Legal Reasoning, Logical Reasoning, and Quantitative Techniques.", 
    "english_questions": "The English section usually contains 28–32 multiple-choice questions based on comprehension passages.",
    "logical_reasoning": "Logical Reasoning section tests critical thinking and includes around 28–32 questions.",
    "legal_reasoning": "This section focuses on legal principles and scenarios, with 35–39 questions.",
    "gk": "Current Affairs & GK section has 35–39 questions from national and international news.",
    "maths": "The Quantitative Techniques section has 13–17 questions based on graphs, charts, and basic math.",
    "cutoff_nlsiu": "NLSIU Bangalore cut-off (General, 2024) was around AIR 114.",
    "cutoff_nalsar": "NALSAR Hyderabad cut-off (General, 2024) was around AIR 177.",
    "exam_date": "CLAT 2025 is tentatively scheduled for December 2024.",
    "marks": "The total marks for CLAT is 150, with 1 mark per question and -0.25 for each wrong answer.",
    "application_date": "The application window usually opens in July and closes by November.",
    "career": "CLAT opens paths to careers in corporate law, litigation, judiciary, civil services, academia, and legal consultancy.",
    "strategy": "Focus on reading comprehension and practice mock tests. Prioritize accuracy and time management.",
    "eligibility": "You must have passed Class 12 with at least 45% (General) or 40% (SC/ST). No age limit."
}


def get_answer(query):
    query = query.lower()
    for key in knowledge_base:
        if key in query:
            return knowledge_base[key]
    closest = difflib.get_close_matches(query, knowledge_base.keys(), n=1, cutoff=0.4)
    if closest:
        return f"Here's something close to your question: {knowledge_base[closest[0]]}"
    return "🤔 Sorry, I don't have an answer for that. Try asking in a different way!"

# Chat UI
user_query = st.text_input("Your Question:")
if user_query:
    response = get_answer(user_query)
    st.markdown(f"**Answer:** {response}")
