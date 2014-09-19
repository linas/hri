from .person import Person
from .robot import Robot
from .world import World
from hri_api.query import Query

world = World()
zeno = Robot()


def closest_person_changed(results):
    person = results[0]
    zeno.say_to('hello', person)

people = Query(world).select_type(Person)
close_to_robot = people.select_where(lambda p: p.distance_to(zeno) < 1)


closest_to_robot = people.sort_ascending(lambda p: p.distance_to(zeno)).take(1)
closest_to_robot.subscribe(closest_person_changed)




