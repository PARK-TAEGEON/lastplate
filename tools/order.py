"""All quantities use kilograms; demo recipe and stock are synthetic."""


def calculate_order(cooking_quantity: int, recipes: list[dict], lots: list[dict]) -> list[dict]:
    if cooking_quantity < 0:
        raise ValueError("조리량은 음수일 수 없습니다.")
    orders = []
    for recipe in recipes:
        per_person = float(recipe["kg_per_person"])
        if per_person < 0:
            raise ValueError("레시피 기준량을 확인하세요.")
        required = cooking_quantity * per_person
        remaining = required
        allocations = []
        for lot in lots:
            if lot["ingredient"] == recipe["ingredient"]:
                available = float(lot["stock_kg"])
                if available < 0:
                    raise ValueError("재고량을 확인하세요.")
                used = min(remaining, available)
                if used > 0:
                    allocations.append({"lot_id": lot["lot_id"], "use_kg": round(used, 3)})
                remaining = max(0.0, remaining - used)
        orders.append({"ingredient": recipe["ingredient"], "required_kg": round(required, 3),
                       "order_kg": round(remaining, 3), "allocations": allocations})
    return orders
