from langchain.tools import tool
from src.llm.openai_client import llm
from src.tools.tavily_search import tavily_search


@tool
def search(query: str):
    """
    Search the web for current information.
    Use this tool whenever the question requires
    recent or factual information.
    
    """
    return tavily_search(query)




llm_with_tools = llm.bind_tools(
    [search]
)

def chatbot(state):

    return {
        "messages": [
            llm_with_tools.invoke(
                state["messages"]
            )
        ]
    }