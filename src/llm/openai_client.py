# from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# client = OpenAI()


from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)