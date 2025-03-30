import streamlit as st
import random
import string

# Set page config
st.set_page_config(
    page_title="Password Generator",
    page_icon="🔒",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        margin-top: 10px;
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .main {
        padding: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🔒 Password Generator")
st.markdown("Generate strong and secure passwords with ease!")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    # Password length slider
    length = st.slider("Password Length", 8, 32, 16, 1)
    
    # Password options
    st.subheader("Password Options")
    use_uppercase = st.checkbox("Uppercase Letters (A-Z)", value=True)
    use_lowercase = st.checkbox("Lowercase Letters (a-z)", value=True)
    use_numbers = st.checkbox("Numbers (0-9)", value=True)
    use_symbols = st.checkbox("Special Symbols (!@#$%^&*)", value=True)

with col2:
    # Generate password button
    if st.button("Generate Password", key="generate"):
        # Character sets
        chars = ""
        if use_uppercase:
            chars += string.ascii_uppercase
        if use_lowercase:
            chars += string.ascii_lowercase
        if use_numbers:
            chars += string.digits
        if use_symbols:
            chars += string.punctuation
        
        if not chars:
            st.error("Please select at least one character type!")
        else:
            # Generate password
            password = ''.join(random.choice(chars) for _ in range(length))
            
            # Display password in a nice box with copy button
            st.markdown("### Your Generated Password")
            st.code(password, language="text")
            st.markdown(f'<button onclick="navigator.clipboard.writeText(\'{password}\')">Copy to Clipboard</button>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit") 