import streamlit as st

def main():
    # Set a cute background color and text color
    st.markdown(
        """
        <style>
        .reportview-container {
            background-color: #ffe4e1;
            color: #ff69b4;
        }
        .sidebar .sidebar-content {
            background-color: #ffe4e1;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display the initial text with a heart emoji
    st.markdown("<h2 style='text-align: center;'>Why you kinda ❤️</h2>", unsafe_allow_html=True)

    # Define a button and its behavior
    if st.button('kinda what cuh'):
        # Change 'cuh' to 'babe'
        response_text = 'kinda what babe 💕'
        st.markdown(f"<h3 style='text-align: center;'>{response_text}</h3>", unsafe_allow_html=True)

        # Display an image with the text 'kinda precious adorable and cute typpa'
        st.image('cute_image.jpg', caption='kinda precious, adorable, and cute typpa 🥰')

if __name__ == '__main__':
    main()
