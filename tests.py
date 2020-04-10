from zonk import CalcZonkCombo
from unittest import TestCase


class ZonkTestCase(TestCase):

    def setUp(self):
        self.zonk_calculator = CalcZonkCombo()
        self.zonk_test_data =[
            [[1, 1, 1, 2, 4, 3], 1000], [[1, 2, 1, 2, 4, 3], 200], [[2, 2, 1, 1, 4, 4], 750],
            [[5, 1, 1, 1, 4, 5], 1100], [[5, 5, 5, 5, 4, 4], 1000], [[3, 3, 3, 3, 4, 4], 600],
            [[2, 3, 1, 5, 4, 6], 1500], [[2, 3, 3, 6, 4, 4], 0], [[2, 3, 6, 6, 6, 1], 700],
            [[6, 6, 4, 4, 4, 4], 800], [[6, 6, 4, 4, 1, 5], 150], [[6, 2, 3, 2, 4, 4], 0],
            [[6, 4, 4, 4, 1, 1], 600], [[4, 1, 5, 5, 6, 5], 600], [[6, 2, 3, 6, 5, 6], 650],
            [[4, 5, 1, 5, 1, 1], 1100], [[1, 5, 1, 6, 5, 3], 300], [[4, 4, 2, 4, 5, 4], 850],
            [[1, 5, 2, 5, 5, 5], 1100], [[2, 2, 2, 1, 5, 5], 400]]

    def test_zonk_test_data(self):
        for dice_combination, expected_sum in self.zonk_test_data:
            actual_sum = self.zonk_calculator.count_total_points(dice_combination)
            self.assertEqual(actual_sum, expected_sum)

