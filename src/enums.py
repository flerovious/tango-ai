from enum import Enum


class Expertise(Enum):
    INTRODUCTORY_CHEMISTRY = "chemistry"


class InputField(Enum):
    QUESTION = "question"
    OPTIONS = "option"
    ANSWER = "answer"


class OutputField(Enum):
    GUIDE = "guide"
    CITATIONS = "citations"
