from unittest import TestCase

from boxes import get_box_types_and_quantities, Boxes, put_into_boxes


class TestApp(TestCase):
    def test_get_collective_qty_ok(self):
        self.assertEqual(Boxes(small=0, medium=1, big=0).get_collective_qty(), 0)
        self.assertEqual(Boxes(small=0, medium=1, big=2).get_collective_qty(), 1)
        self.assertEqual(Boxes(small=0, medium=1, big=6).get_collective_qty(), 3)

    def test_put_into_boxes_ok(self):
        self.assertEqual(
            put_into_boxes(15), Boxes(small=0, medium=1, big=1, collective=1)
        )
        self.assertEqual(
            put_into_boxes(32), Boxes(small=0, medium=1, big=3, collective=2)
        )

    def test_put_into_boxes_fail(self):
        self.assertRaises(TypeError, put_into_boxes, "string")
        self.assertRaises(TypeError, put_into_boxes, (2, "1"))

    def test_get_box_types_and_quantities_ok(self):
        self.assertEqual(
            get_box_types_and_quantities(1),
            Boxes(small=1, medium=0, big=0, collective=0),
        )
        self.assertEqual(
            get_box_types_and_quantities(19),
            Boxes(small=1, medium=0, big=2, collective=1),
        )
        self.assertEqual(
            get_box_types_and_quantities(24),
            Boxes(small=0, medium=1, big=2, collective=1),
        )
        self.assertEqual(
            get_box_types_and_quantities(36),
            Boxes(small=0, medium=0, big=4, collective=2),
        )
        self.assertEqual(
            get_box_types_and_quantities(99),
            Boxes(small=0, medium=0, big=11, collective=4),
        )

        # corner cases
        self.assertEqual(
            get_box_types_and_quantities(10),
            Boxes(small=0, medium=2, big=0, collective=1),
        )
        self.assertEqual(
            get_box_types_and_quantities(12),
            Boxes(small=0, medium=2, big=0, collective=1),
        )
        self.assertEqual(
            get_box_types_and_quantities(13),
            Boxes(small=0, medium=0, big=2, collective=1),
        )
        self.assertEqual(
            get_box_types_and_quantities(18),
            Boxes(small=0, medium=0, big=2, collective=1),
        )

    def test_box_types_and_quantities_order_quantity_less_than_1_fail(self):
        self.assertRaises(ValueError, get_box_types_and_quantities, 0)
        self.assertRaises(ValueError, get_box_types_and_quantities, -5)

    def test_box_types_and_quantities_order_quantity_over_99_fail(self):
        self.assertRaises(ValueError, get_box_types_and_quantities, 101)
        self.assertRaises(ValueError, get_box_types_and_quantities, 1024)

    def test_box_types_and_quantities_order_quantity_isinstance_of_integer_fail(self):
        self.assertRaises(TypeError, get_box_types_and_quantities, "10")
        self.assertRaises(TypeError, get_box_types_and_quantities, [1, 2])
