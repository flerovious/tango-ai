from dataclasses import dataclass


@dataclass
class Citation:
    reference_index: int
    page_label: int
    file_name: str
    url: str
