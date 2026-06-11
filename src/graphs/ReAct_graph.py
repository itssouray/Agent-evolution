from langgraph.graph import (
    StateGraph,
    START
)

from langgraph.prebuilt import (
    ToolNode,
    tools_condition
)

from src.graphs.state import State
from src.graphs.nodes import (
    chatbot,
    search
)

builder = StateGraph(State)

builder.add_node(
    "chatbot",
    chatbot
)

builder.add_node(
    "tools",
    ToolNode([search])
)

builder.add_edge(
    START,
    "chatbot"
)

builder.add_conditional_edges(
    "chatbot",
    tools_condition
)

builder.add_edge(
    "tools",
    "chatbot"
)

graph = builder.compile()