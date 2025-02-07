import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    AIMessagePromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_ollama import ChatOllama

# Custom CSS styling
st.markdown(
    """
<style>
    /* Existing styles */
    .main {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    .sidebar .sidebar-content {
        background-color: #2d2d2d;
    }
    .stTextInput textarea {
        color: #ffffff !important;
    }

    /* Add these new styles for select box */
    .stSelectbox div[data-baseweb="select"] {
        color: white !important;
        background-color: #3d3d3d !important;
    }

    .stSelectbox svg {
        fill: white !important;
    }

    .stSelectbox option {
        background-color: #2d2d2d !important;
        color: white !important;
    }

    /* For dropdown menu items */
    div[role="listbox"] div {
        background-color: #2d2d2d !important;
        color: white !important;
    }
</style>
""",
    unsafe_allow_html=True,
)
st.title("🧠 DeepSeek Chatbot")
st.caption("🚀 Your AI Pair Programmer with Debugging Superpowers")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    selected_model = st.selectbox(
        "Choose Model",
        [
            "deepseek-r1:1.5b",
            "deepseek-r1:7b",
        ],
        index=0,
    )
    st.divider()
    st.markdown("### Model Capabilities")
    st.markdown("""
    - 🐍 Python Expert
    - 🐞 Debugging Assistant
    - 📝 Code Documentation
    - 💡 Solution Design
    """)
    st.divider()
    st.markdown(
        "Built with [Ollama](https://ollama.ai/) | [LangChain](https://python.langchain.com/)"
    )

# Initialize the Chat Engine with streaming enabled
llm_engine = ChatOllama(
    model=selected_model,
    base_url="http://localhost:11434",
    temperature=0.3,
    stream=True,
)

# System Prompt Configuration
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are an expert AI coding assistant. Provide concise, correct solutions "
    "with strategic print statements for debugging. Always respond in English. "
    "Before giving your final answer, provide a brief thought process inside <think> </think>."
)

# Session state management
if "message_log" not in st.session_state:
    st.session_state.message_log = [
        {
            "role": "ai",
            "content": "Hi! I'm DeepSeek. How can I help you code today? 💻",
        }
    ]

# Chat container
chat_container = st.container()

# Display chat messages
with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.write(message["content"])

# Chat input and processing
user_query = st.chat_input("Type your coding question here...")


def generate_ai_response(prompt_chain):
    """Generate streaming AI responses with thought process inside <think> tags."""
    processing_pipeline = prompt_chain | llm_engine | StrOutputParser()

    # Streaming response
    response_placeholder = st.empty()  # Create placeholder for updating response
    streamed_text = ""

    for chunk in processing_pipeline.stream({}):  # Stream response in real time
        streamed_text += chunk
        response_placeholder.write(streamed_text)  # Update UI with streamed response

    return streamed_text


def build_prompt_chain():
    """Construct the chat history prompt chain."""
    prompt_sequence = [system_prompt]
    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            prompt_sequence.append(
                HumanMessagePromptTemplate.from_template(msg["content"])
            )
        elif msg["role"] == "ai":
            prompt_sequence.append(
                AIMessagePromptTemplate.from_template(msg["content"])
            )
    return ChatPromptTemplate.from_messages(prompt_sequence)


if user_query:
    # Add user message to the log
    st.session_state.message_log.append(
        {
            "role": "user",
            "content": user_query,
        }
    )

    # Generate AI response with streaming
    with st.chat_message("ai"):
        with st.spinner("🧠 Thinking..."):
            prompt_chain = build_prompt_chain()
            ai_response = generate_ai_response(prompt_chain)

    # Add AI response to the log
    st.session_state.message_log.append(
        {
            "role": "ai",
            "content": ai_response,
        }
    )

    # Rerun to update the chat display
    st.rerun()
