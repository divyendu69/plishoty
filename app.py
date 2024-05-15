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
            height: 80vh;
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
        .image-side {
            max-width: 15%;
            height: auto;
            margin: 10px;
        }
        .popup-image {
            display: none;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 10;
            border: 5px solid #ff69b4;
            border-radius: 10px;
        }
        .popup-image img {
            max-width: 100%;
            height: auto;
            border-radius: 10px;
        }
        .overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            z-index: 9;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display side images
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <img src="left_image.jpg" class="image-side">
            <img src="right_image.jpg" class="image-side">
        </div>
        """,
        unsafe_allow_html=True
    )

    # Center the button and add JavaScript for the animation
    st.markdown(
        """
        <div class="centered-button">
            <button id="changeTextButton" class="button">kinda what cuh</button>
        </div>
        <div id="popupImage" class="popup-image">
            <img src="cute_image.jpg" alt="kinda precious, adorable, and cute typpa 🥰">
            <figcaption style="text-align: center; color: #ff69b4;">kinda precious, adorable, and cute typpa 🥰</figcaption>
        </div>
        <div id="overlay" class="overlay"></div>
        <script>
        document.getElementById('changeTextButton').onclick = function() {
            var button = document.getElementById('changeTextButton');
            button.innerHTML = 'kinda what babe 💕';
            button.style.backgroundColor = '#ff1493';
            document.getElementById('popupImage').style.display = 'block';
            document.getElementById('overlay').style.display = 'block';
        };
        document.getElementById('overlay').onclick = function() {
            document.getElementById('popupImage').style.display = 'none';
            document.getElementById('overlay').style.display = 'none';
        };
        </script>
        """,
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    main()
