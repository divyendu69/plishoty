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
        .center {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 50vh;
            margin-top: -50px;
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

    # Center the button
    st.markdown(
        """
        <div class="center">
            <button class="button" id="changeTextButton">kinda what cuh</button>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Placeholder for the image and script for button action
    st.markdown(
        """
        <div id="imageContainer" style="text-align: center; display: none;">
            <img src="cute_image.jpg" alt="kinda precious, adorable, and cute typpa 🥰" style="max-width: 100%; height: auto;">
            <figcaption style="color: #ff69b4;">kinda precious, adorable, and cute typpa 🥰</figcaption>
        </div>
        <script>
        document.getElementById('changeTextButton').onclick = function() {
            var button = document.getElementById('changeTextButton');
            button.innerHTML = 'kinda what babe 💕';
            document.getElementById('imageContainer').style.display = 'block';
        };
        </script>
        """,
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    main()
