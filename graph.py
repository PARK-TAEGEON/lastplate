"""Three deterministic LangGraph nodes; no LLM/API call in the initial demo."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from tools.demand import predict_demand, calculate_cooking_quantity
from tools.inventory import recommend_inventory_use
from tools.order import calculate_order


class MealState(TypedDict, total=False):
    employees: int
    attendance_rate: float
    extra_people: int
    safety_rate: float
    service_date: str
    recipes: list[dict]
    lots: list[dict]
    demand: dict
    cooking_quantity: int
    eligible_lots: list[dict]
    orders: list[dict]


def demand_node(state):
    return {"demand": predict_demand(state["employees"], state["attendance_rate"], state["extra_people"])}


def cooking_node(state):
    return {"cooking_quantity": calculate_cooking_quantity(state["demand"]["prediction"], state["safety_rate"])}


def order_node(state):
    lots = recommend_inventory_use(state["lots"], state["service_date"])
    return {"eligible_lots": lots, "orders": calculate_order(state["cooking_quantity"], state["recipes"], lots)}


def build_graph():
    builder = StateGraph(MealState)
    builder.add_node("demand", demand_node)
    builder.add_node("cooking", cooking_node)
    builder.add_node("order", order_node)
    builder.add_edge(START, "demand")
    builder.add_edge("demand", "cooking")
    builder.add_edge("cooking", "order")
    builder.add_edge("order", END)
    return builder.compile()
