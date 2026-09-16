"""Demo baseline. Replace with a trained model after evaluating held-out dates."""
import math


def predict_demand(employees: int, attendance_rate: float, extra_people: int = 0) -> dict:
    if employees < 0 or extra_people < 0 or not 0 <= attendance_rate <= 1:
        raise ValueError("인원은 0 이상, 참석률은 0~1이어야 합니다.")
    return {"prediction": math.ceil(employees * attendance_rate) + extra_people,
            "method": "demo_rule", "is_trained_model": False}


def calculate_cooking_quantity(prediction: int, safety_rate: float = 0.05) -> int:
    if prediction < 0 or not 0 <= safety_rate <= 1:
        raise ValueError("예측 인원과 안전여유를 확인하세요.")
    return math.ceil(prediction * (1 + safety_rate))
