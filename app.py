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
        .centered-button {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .button {
            background-color: #ff69b4;
            color: white;
            border: none;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;
            transition: background-color 0.3s ease;
        }
        .button:hover {
            background-color: #ff1493;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Center the button and add JavaScript for the animation
    st.markdown(
        """
        <div class="centered-button">
            <button id="changeTextButton" class="button">kinda what cuh</button>
        </div>
        <script>
        document.getElementById('changeTextButton').onclick = function() {
            var button = document.getElementById('changeTextButton');
            button.innerHTML = 'kinda what babe 💕';
            button.style.backgroundColor = '#ff1493';
            document.getElementById('imageContainer').style.display = 'block';
        };
        </script>
        """,
        unsafe_allow_html=True
    )

    # Placeholder for the image
    st.markdown(
        """
        <div id="imageContainer" style="display: none; text-align: center;">
            <img src="cute_image.jpg" alt="kinda precious, adorable, and cute typpa 🥰" style="max-width: 100%; height: auto;">
            <figcaption>kinda precious, adorable, and cute typpa 🥰</figcaption>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    main()
