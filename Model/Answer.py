from dataclasses import dataclass


@dataclass
class Answer:
    x: float
    y: float
    iteration_amount: int
    can_converge: bool
    error_message: str
