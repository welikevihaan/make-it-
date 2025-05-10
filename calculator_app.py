import streamlit as st

st.title("🧮 Simple Calculator")

expression = st.text_input("Enter a math expression (e.g., 2 + 3 * 4)")

if st.button("Calculate"):
    try:
        result = eval(expression)
        st.success(f"Result: {result}")
    except:
        st.error("Invalid expression. Please try again.")
