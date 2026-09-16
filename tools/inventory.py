"""FEFO: use eligible lots with the earliest expiry first."""
from datetime import date


def recommend_inventory_use(lots: list[dict], service_date: str) -> list[dict]:
    day = date.fromisoformat(service_date)
    eligible = []
    for lot in lots:
        expiry = date.fromisoformat(lot["expiry_date"])
        if float(lot["stock_kg"]) < 0:
            raise ValueError("재고량은 음수일 수 없습니다.")
        if expiry >= day:
            eligible.append(dict(lot))
    return sorted(eligible, key=lambda lot: lot["expiry_date"])
