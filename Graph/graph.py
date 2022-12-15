# Mark john M. Raymundo CoE 2-2 Data Structure and Algorithms
# graph.py
# Source: https://realpython.com/queue-in-python/#implementing-queues-in-python

from typing import NamedTuple

class City(NamedTuple):
    name: str
    country: str
    year: int or None
    latitude: float
    longitude: float

    @classmethod
    def from_dict(cls, attrs):
        return cls(
            name=attrs["xlabel"],
            country=attrs["country"],
            year=int(attrs["year"] or None),
            latitude=float(attrs["latitude"]),
            longitude=float(attrs["longitude"]),
        )