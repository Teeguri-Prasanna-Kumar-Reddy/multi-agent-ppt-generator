from typing import TypedDict, Dict, Any
from langgraph.graph import StateGraph, END

# Import agents
from agents.router_agent import router_agent
from agents.parser_agent import parser_agent
from agents.rag_agent import rag_agent
from agents.planner_agent import planner_agent
from agents.research_agent import research_agent
from agents.structure_agent import structure_agent
from agents.content_agent import content_agent
from agents.design_agent import design_agent
from agents.ppt_builder_agent import ppt_builder_agent
from agents.reviewer_agent import reviewer_agent


# -------------------------
# State Schema
# -------------------------
class PPTState(TypedDict, total=False):
    topic: str
    documents: list

from typing import TypedDict, List

class PPTState(TypedDict):
    topic: str
    documents: list
    outline: List[str]  
    parsed_docs: list
    context: str
    plan: list
    research: dict
    research_content: dict
    structure: list
    slides: list
    ppt_path: str
    review: dict


# -------------------------
# Graph Builder
# -------------------------
def build_graph():

    graph = StateGraph(PPTState)

    # Add nodes
    graph.add_node("router_node", router_agent)
    graph.add_node("parser_node", parser_agent)
    graph.add_node("rag_node", rag_agent)
    graph.add_node("planner_node", planner_agent)
    graph.add_node("research_node", research_agent)
    graph.add_node("structure_node", structure_agent)
    graph.add_node("content_node", content_agent)
    graph.add_node("design_node", design_agent)
    graph.add_node("ppt_builder_node", ppt_builder_agent)
    graph.add_node("reviewer_node", reviewer_agent)

    # Define Flow
    graph.set_entry_point("router_node")

    graph.add_edge("router_node", "parser_node")
    graph.add_edge("parser_node", "rag_node")
    graph.add_edge("rag_node", "planner_node")
    graph.add_edge("planner_node", "research_node")
    graph.add_edge("research_node", "structure_node")
    graph.add_edge("structure_node", "content_node")
    graph.add_edge("content_node", "design_node")
    graph.add_edge("design_node", "ppt_builder_node")
    graph.add_edge("ppt_builder_node", "reviewer_node")

    graph.add_edge("reviewer_node", END)


    return graph.compile()


# -------------------------
# Runner Function
# -------------------------
def run_ppt_agent(input_data: Dict[str, Any]):

    graph = build_graph()

    result = graph.invoke(input_data)

    return result