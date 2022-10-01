import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import erdantic as erd

from src.models import (Root, Metadata, Info, Participant, Trait, Unit, Companion)


diagram = erd.create(Root)
diagram.draw("./doc/ER.svg")

