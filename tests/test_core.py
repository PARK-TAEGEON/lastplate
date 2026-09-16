import unittest
from tools.demand import predict_demand, calculate_cooking_quantity
from tools.inventory import recommend_inventory_use
from tools.order import calculate_order


class CoreTests(unittest.TestCase):
    def test_extra_people_recalculate(self):
        base = predict_demand(600, 0.8, 0)["prediction"]
        extra = predict_demand(600, 0.8, 35)["prediction"]
        self.assertEqual((base, extra), (480, 515))
        self.assertEqual(calculate_cooking_quantity(extra), 541)

    def test_expiry_and_fefo_allocations(self):
        lots = [{"lot_id": "late", "ingredient": "tofu", "stock_kg": 12, "expiry_date": "2026-09-19"},
                {"lot_id": "expired", "ingredient": "tofu", "stock_kg": 99, "expiry_date": "2026-09-16"},
                {"lot_id": "early", "ingredient": "tofu", "stock_kg": 8, "expiry_date": "2026-09-17"}]
        eligible = recommend_inventory_use(lots, "2026-09-17")
        result = calculate_order(100, [{"ingredient": "tofu", "kg_per_person": .1}], eligible)[0]
        self.assertEqual(result["order_kg"], 0)
        self.assertEqual(result["allocations"], [{"lot_id": "early", "use_kg": 8}, {"lot_id": "late", "use_kg": 2}])
        shortage = calculate_order(300, [{"ingredient": "tofu", "kg_per_person": .1}], eligible)[0]
        self.assertEqual(shortage["order_kg"], 10)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            predict_demand(600, 1.2)
        with self.assertRaises(ValueError):
            predict_demand(600, .8, -35)


if __name__ == "__main__":
    unittest.main()
