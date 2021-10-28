import streamlit as st
from PIL import Image
import io


def print_welcome(first_name: str, new_image: Image):
    st.write(
        f"""
        # Hello {first_name}!
        we are happy to see you sign up for the best cat facts.
        """
    )
    st.image(new_image, caption="Your photo")


with st.form("person"):
    col1, col2 = st.columns(2)
    first_name = col1.text_input("First name")
    last_name = col2.text_input("Last name")
    date_of_birth = st.date_input("Date of birth")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    uploaded_photo = st.file_uploader("Choose a photo")
    if uploaded_photo is not None:
        new_image = Image.open(io.BytesIO(uploaded_photo.getvalue()))
    checkbox = st.checkbox("I agree to the end user agreement!")
    submitted = st.form_submit_button(
        help="Submits the form",
    )
    password = st.text_input("Password", type="password")
    if submitted:
        if len(phone) != 8:
            st.error("Invalid phone number (8 chars)")
        else:
            print_welcome(first_name, new_image)
