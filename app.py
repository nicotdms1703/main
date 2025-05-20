import streamlit as st
from PIL import Image

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="NICO_WEBBLOG", page_icon=":heart:", layout="wide")

# Define your background image URL from GitHub repository (use the direct link to the raw image file)
background_image_url = "https://raw.githubusercontent.com/nicotdms1703/My_WebpageNico1/main/mo.png"

# Apply the background image using custom CSS
background_style = f"""
    <style>
        .stApp {{
            background-image: url('{background_image_url}');
            background-size: cover;
            background-repeat: no-repeat;
        }}
        .css-17eq0hr, .css-1v1k8g1, .css-1be9khp {{
            color: black !important;
        }}
        .sidebar, .sidebar-content {{
            background-color: #FFB7C5 !important; /* Cherry Blossom Pink */
        }}
    </style>
"""
st.markdown(background_style, unsafe_allow_html=True)

# Add a title above the sidebar
st.sidebar.title("MY CONTENTS")

# Sidebar navigation
selected_page = st.sidebar.radio("", ["📝 Blog :memo:", "📚 My Project :books:"])

if selected_page == "📝 Blog :memo:":
    # Blog section
    st.title("Hi, I'm Romel Charlz Nico C. Dela Cruz and Welcome To my Blog :wave:, \n where you'll learn more about me")
    st.header("I'm a 2nd Year College Student in BSCPE Course")
    st.write("I'm learning how to code and program, since this is the field that I'm best at")
    st.write("Message me on FaceBook [Click here >](https://www.facebook.com/NICO.TDMS1703)")

    img = Image.open("look.png")
    st.image(img, width=600, channels="RGB")

    st.write("---")
    st.header("Some information About me:")
    st.write("##")
    st.write(
        """
        - I'm a 2nd year irregular student who transferred courses from Bachelor of Science in Electronic Engineering (BSECE) to Bachelor of Science in Computer Engineering (BSCpE).
        - As a second-year irregular student, my academic journey has taken a fascinating turn, marked by a significant transition from my initial pursuit of a Bachelor of Science in Electronic Engineering (BSECE) to a dynamic new path in the field of Bachelor of Science in Computer Engineering (BSCpE).
        - This decision to shift courses reflects not just a change in academic focus but a deliberate choice to explore and align my educational journey with the evolving landscape of technology.
        - As a newcomer to the vast and ever-evolving field of computing, I find myself on an exhilarating exploration eager to unravel the intricacies that span the entire spectrum of this technological landscape.
        - My journey commences with a keen interest in programming, where I am navigating through the diverse languages and frameworks that serve as the building blocks for creating innovative software solutions.
        """
    )

    st.header("\n More Story about me:")
    st.write("##")
    st.write(
        """
        - In the past, my creative endeavors found a unique outlet as I immersed myself in the world of Warcraft 3 World Editor. This engaging platform became the canvas for my imaginative pursuits, where I delved into the intricate art of encoding triggers and crafting meticulously designed maps.
        - My passion for creating immersive gaming experiences reached new heights as I harnessed the tools provided by the World Editor to breathe life into custom scenarios and trigger-based events within the Warcraft 3 universe.
        - Upon completing my masterpieces, the natural next step was to share them with the vibrant community of gaming enthusiasts. HIVEWORKSHOP.COM emerged as the go-to platform for this purpose, providing a collaborative space where creators from around the world converged to showcase their creations.
        - Here are some links for samples of what I do [Click link to know more >](https://www.hiveworkshop.com/threads/hivewe-world-editor-0-6.303110/)
        """
    )

elif selected_page == "📚 My Project :books:":
    # Python Calculator section
    st.title("My Python Projects")

    st.header("Basic Python Calculator")

    # Calculator logic
    num1 = st.number_input("Enter the first number", step=1)
    num2 = st.number_input("Enter the second number", step=1)

    operation = st.radio("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

    result = 0

    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Division by zero is undefined. Please enter a non-zero value for the second number.")

    st.header(f"Result of {num1} {operation} {num2} is: {result}")
