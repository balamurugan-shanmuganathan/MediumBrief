from langchain.prompts import ChatPromptTemplate
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

import os
import requests
from bs4 import BeautifulSoup

class Website:
    """
    A utility class to represent a Website that we have scraped
    """
    url: str
    title: str
    text: str

    def __init__(self, url):
        """
        Create this Website object from the given url using the BeautifulSoup library
        """
        self.url = url
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)

def llm_model():
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
    google_llm = ChatGoogleGenerativeAI(model='gemini-1.0-pro')
    return google_llm

def llm_chain(llm, web_content):
    prompt = ChatPromptTemplate.from_template("""
        You are an assistant that analyzes the contents of a website
        and provides a short summary atleast 500 words, ignoring text that might be navigation related.
        your response should contains header, sub header and in buillet points \
        Respond in markdown.
                                                  
        Use only input website content. Do use your knowledge to provide the answer out of the content.                                            
        If you don't know. Say I can't able to summarize this article.
                                                  
        You are looking at a website titled {website_title}  
        
        The contents of this website is as follows; please provide a short summary of this website in markdown. \
        If it includes news or announcements, then summarize these too.\n\n 
        {website_text}                  """)
        
    llm = llm
    chain = prompt | llm | StrOutputParser()

    response = chain.invoke({"website_title" : web_content.title, "website_text" : web_content.text})
    
    return response

