import streamlit as st
from PIL import Image
import user_codes.user_defined_functions as udf

def main():

    logo = Image.open("MediumBrief.png")
    resized_logo = logo.resize((500, 500))
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(resized_logo)

    st.sidebar.markdown("""
        # About MediumBrief

        Welcome to **MediumBrief** – your go-to app for quick, no-fuss summaries of Medium articles! Just paste the link to any Medium post, and let MediumBrief do the heavy lifting. Our advanced parsing and language model technology distills articles into concise, impactful summaries, so you get the main points without wading through lengthy content.

        ### How It Works
        **MediumBrief** is designed exclusively for Medium. Once you enter a Medium URL, MediumBrief retrieves and parses the article’s content with precision, then generates a smart summary using cutting-edge language models. Whether you're following trending topics, exploring new ideas, or catching up on thought-provoking reads, MediumBrief brings the highlights to you, fast and easy.

       """)

    website_url = st.text_input(label = "Enter the Medium Article URL for Summarization:")   
    submit = st.button("Submit")

    if submit:
        web_content = udf.Website(website_url)
        llm = udf.llm_model()
        response = udf.llm_chain(llm, web_content)

        st.markdown(response)

if __name__ == "__main__":
    main()