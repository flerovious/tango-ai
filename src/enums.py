from enum import Enum


class Expertise(Enum):
    INTRODUCTORY_CHEMISTRY = "Introductory Chemistry 🧪"


class InputField(Enum):
    QUESTION = "question"
    OPTIONS = "option"
    ANSWER = "answer"


class OutputField(Enum):
    GUIDE = "guide"
    CITATIONS = "citations"
