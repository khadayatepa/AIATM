import streamlit as st
import openai

# Streamlit UI
st.title("🛠️ AI-Powered Middleware Troubleshooting Chatbot")

# API Key Input
api_key = st.text_input("🔑 Enter your OpenAI API key:", type="password")

# Select Middleware Type
middleware_type = st.selectbox("🌐 Select Middleware", ["Apache Tomcat", "WebLogic", "WebSphere", "IIS"])

# Middleware Task Selection
task_type = st.selectbox("⚙️ Select Task", [
    "Server Health Check",
    "Configuration Analysis",
    "Log Analysis & Issue Detection",
    "Performance Optimization Recommendations"
])

# Natural Language Input
task_description = st.text_area("📝 Describe your middleware issue or requirement in plain English:")

if st.button("🚀 Generate Troubleshooting Steps"):
    if not api_key:
        st.error("❌ Please enter your OpenAI API key!")
    elif not task_description:
        st.error("❌ Please describe your middleware request!")
    else:
        try:
            # Create OpenAI client
            client = openai.OpenAI(api_key=api_key)

            # System instruction for AI
            system_prompt = f"You are an expert in {middleware_type} administration. Provide only step-by-step troubleshooting or optimization recommendations for {task_type} without explanation."

            # Full user request
            full_prompt = f"Provide a step-by-step guide for {task_type} in {middleware_type}. {task_description}"

            # Call OpenAI API
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": full_prompt}
                ]
            )

            # Display Generated Response
            st.subheader("✅ Recommended Steps:")
            st.markdown(response.choices[0].message.content)

        except Exception as e:
            st.error(f"🚨 Error: {e}")
