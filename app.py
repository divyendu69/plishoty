import streamlit as st
import time

# Set image paths (replace with your image locations)
left_image_path = "left_image.jpg"
right_image_path = "right_image.jpg"
cute_image_path = "cute_gift_image.jpg"  # Consider a more specific image name

# Initial button text
button_text = "Why you kinda..."

def update_text():
  global button_text
  # Animate button text transition
  chars = "Why you kinda..."
  new_text = "Why you kinda babe..."
  for i in range(len(new_text)):
    st.write(chars[:i+1])
    time.sleep(0.05)  # Adjust speed as needed
  button_text = new_text

# Configure theme (adjust colors to your preference)
st.set_page_config(page_title="Why You Kinda...? ",
                   page_icon=":heart:",
                   layout="wide")
st.markdown("""
<style>
body {
  background-color: #ffc0cb;  /* Light pink background */
  font-family: 'Noto Serif KR', serif;
}

.title {
  color: #f08080;  /* Soft pink for title */
  font-size: 48px;
}

.stButton button {
  background-color: #f0e68c;  /* Peachy button color */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 5px;
  transition: 0.3s ease-in-out;
}

.stButton button:hover {
  background-color: #f8b3b3;  /* Darker peach on hover */
}
</style>
""", unsafe_allow_html=True)

# App layout
st.markdown("""<h1 class="title">Why You Kinda...?</h1>""", unsafe_allow_html=True)

# Display images and button
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
  st.image(left_image_path, width=200)
with col2:
  st.write("")  # Center the text
with col3:
  st.image(right_image_path, width=200)

# Button click event
if st.button(button_text):
  update_text()
  st.image(cute_image_path, width=500)

