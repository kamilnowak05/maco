from dataclasses import dataclass
from enum import Enum
from math import ceil


class BoxCapacity(Enum):
    SMALL: int = 3
    MEDIUM: int = 6
    BIG: int = 9
    COLLECTIVE: int = 3  # Collective box contains max 3 boxes


@dataclass
class Boxes:
    small: int = 0
    medium: int = 0
    big: int = 0
    collective: int = 0

    def get_collective_qty(self) -> int:
        collective = 0
        single_boxes = sum([self.small, self.medium, self.big])
        if single_boxes >= 2:
            collective = ceil(single_boxes / BoxCapacity.COLLECTIVE.value)
        return collective


def put_into_boxes(order_quantity: int) -> Boxes:
    if not isinstance(order_quantity, int):
        raise TypeError("The order_quantity argument must be an integer")

    boxes = Boxes()
    while order_quantity > 0:
        if order_quantity > BoxCapacity.MEDIUM.value:
            order_quantity -= BoxCapacity.BIG.value
            boxes.big += 1
        elif order_quantity > BoxCapacity.SMALL.value:
            order_quantity -= BoxCapacity.MEDIUM.value
            boxes.medium += 1
        else:
            order_quantity -= BoxCapacity.SMALL.value
            boxes.small += 1

    boxes.collective = boxes.get_collective_qty()
    return boxes


def get_box_types_and_quantities(order_quantity: int) -> Boxes:
    # validate order_quantity
    if not isinstance(order_quantity, int):
        raise TypeError("The order_quantity argument must be an integer")
    elif order_quantity < 1:
        raise ValueError("The order_quantity argument must be gt: 0")
    elif order_quantity > 100:
        raise ValueError("The order_quantity argument must be lt 100")

    boxes = put_into_boxes(order_quantity)

    # Corner case for order_quantity between 10 and 18
    if 10 <= order_quantity <= 18:
        if boxes.medium == 1 and boxes.big == 1:
            boxes.big = boxes.medium + boxes.big
            boxes.medium = 0
        if boxes.small == 1 and boxes.big == 1:
            boxes.medium = boxes.small + boxes.big
            boxes.small = 0
            boxes.big = 0

    return boxes
