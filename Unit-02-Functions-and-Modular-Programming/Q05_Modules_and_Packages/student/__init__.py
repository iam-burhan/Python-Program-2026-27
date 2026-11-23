# This file marks 'student' as a package and exposes selected functions.
from .details import display_student
from .results import calculate_result

__all__ = ["display_student", "calculate_result"]
