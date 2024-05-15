import streamlit as st
from time import sleep  # Import for button press delay

# Set image paths (replace with your image locations)
left_image_path = "left_image.jpg"
right_image_path = "right_image.jpg"
cute_image_path = "cute_image.jpg"  # Consider a more specific image name

# Initial button text
button_text = "Why you kinda..."
press_count = 0  # Track button press count

def update_text():
  global button_text, press_count
  press_count += 1
  if press_count == 1:
    button_text = "Why you kinda what cuh?"
  elif press_count == 2:
    button_text = "Why you kinda babe..."
    st.image(cute_image_path, width=500)
  else:
    # Handle additional presses if needed
    pass
  sleep(0.25)  # Delay after each button press (adjust as desired)

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

.title,
.button {  /* Center both title and button */
  text-align: center;
}

.title {
  color: #f08080;  /* Soft pink for title */
  font-size: 48px;
}

.button-container {
  display: flex;
  justify-content: center;  /* Center horizontally */
  margin-top: 20px;  /* Add some space above the button */
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
  st.write("")  # Center the text (optional, title is already centered with CSS)
with col3:
  st.image(right_image_path, width=200)

# Button container and click event
with st.container():
  button_class = "button-container"
  st.write('<div class="' + button_class + '">', unsafe_allow_html=True)
  if st.button(button_text, class_="button"):
    update_text()
  st.write('</div>', unsafe_allow_html=True)

