from data.classes.wall import Wall
from data.classes.sensor import Sensor

walls=[]
walls.append(Wall((0,0),(800,10)))
walls.append(Wall((0,10),(10,580)))
walls.append(Wall((0,590),(800,10)))
walls.append(Wall((790,10),(10,580)))

walls.append(Wall((400,10),(10,300)))
walls.append(Wall((410,200),(200,10)))
walls.append(Wall((400,10),(10,500)))
walls.append(Wall((190,300),(210,10)))
walls.append(Wall((10,200),(320,10)))
walls.append(Wall((410,300),(120,10)))

start_position = ( 30, 100 )
finish_position = (450, 100)

sensors = []
sensors.append(Sensor(0, 0, walls))
sensors.append(Sensor(-45, 1, walls))
sensors.append(Sensor(-90, 2, walls))
sensors.append(Sensor(45, 3, walls))
sensors.append(Sensor(90, 4, walls))