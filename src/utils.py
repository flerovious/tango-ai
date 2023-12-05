from enums import Expertise

TANGO_ENGINE_ID = "tango_engine"


def get_expertise_description(expertise: Expertise):
    if expertise == Expertise.INTRODUCTORY_CHEMISTRY:
        return "Introductory Chemistry 🧪"
    else:
        return "Unknown Expertise"
