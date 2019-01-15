import datetime

import Tag
import Event
from GridMap.python.grid_map import GridMap

class EventServer:

    def __init__(
            self,
            bit_depth=32,
            min_x=0,
            min_y=0,
    ):
        self.mask = (1 << bit_depth) - 1
        self.bit_depth = bit_depth
        self.min_x = min_x
        self.min_y = min_y
        self.events = GridMap(
            threshold=2048,
            bit_depth=self.bit_depth,
            min_x=self.min_x,
            min_y=self.min_y
        )

    def hello_world(self, arg1, kwarg1="hello universe"):
        print(str(arg1) + str(kwarg1))

    def _geo_to_rect(self, lon=None, lat=None):
        #resizes to the appropriate length
        x = lon + 90
        y = lat + 90
        x = int((x/180)*(self.mask))
        y = int((y/180)*(self.mask))

    def create_event(
            self=None,
            name=None,
            time=None,
            lon=None,
            lat=None,
            tags=None,
            description=None):
        time = datetime.strptime(time, "%d-%m-%Y %H:%M") #23-01-2018 23:07
        tags = Tag.get_tags(tags)
        e = Event(
            name=name,
            time=time,
            location=(lon, lat),
            tags=tags,
            description=descriptions)
        (x, y) = self._geo_to_rect(lon=lon, lat=lat)
        self.events.add(x, y, e)

    def create_tag(self, name=""):
        Tag.create_tag(name)

    def get_events(self, lon=None, lat=None, tags=[], radius=0):
        (x, y) = self._geo_to_rect(lon=lon, lat=lat)
        x_min = x - radius
        x_max = x + radius
        y_min = y - radius
        y_max = y + radius
        results = self.events.get_nodes(x_min, y_min, x_max, y_max)
        #need to go through tags

    def get_server_functions(self):
        pass




if __name__ == "__main__":
    print("executing main startup")
