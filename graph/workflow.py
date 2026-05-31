
from langgraph.graph import StateGraph, END

from graph.state import ResearchState
from graph.nodes import (
    planner_node,
    researcher_node,
    analyst_node,
    writer_node,
    reviewer_node,
    should_continue,
)


def build_graph():
    workflow = StateGraph(ResearchState)

    # Nodes
    workflow.add_node("planner", planner_node)
    workflow.add_node("researcher", researcher_node)
    workflow.add_node("analyst", analyst_node)
    workflow.add_node("writer", writer_node)
    workflow.add_node("reviewer", reviewer_node)

    # Flow
    # defining flow  (order of steps and how data moves between them)
    workflow.set_entry_point("planner")

    workflow.add_edge("planner", "researcher")
    workflow.add_edge("researcher", "analyst")
    workflow.add_edge("analyst", "writer")
    workflow.add_edge("writer", "reviewer")

    # Conditional loop (reviewer decides)
    workflow.add_conditional_edges(
        "reviewer",
        should_continue,
        {
            "approved": END,
            "revise": "writer",
        },
    )

    return workflow.compile()


# singleton
research_graph = build_graph()