# inzend84a_drone.py
"""
An IDLE-shell session
-----------------------------------------------------------------
>>> qc1 = QuadCopter()
>>> qc1.move([(0,0,1000)])
...flying...
'flown: 10.0 meter, 253.0625 seconds left'
>>> qc1.move([(0,0,1000),(1000,0,0),(200,200,-200),(77,0,0),(0,0,-500)])
...flying...
...flying...
...flying...
...flying...
...flying...
'flown: 39.23410161513776 meter, 188.3125 seconds left'
>>> qc1.move([(0,0,1000)])
...flying...
'flown: 49.23410161513776 meter, 100.296875 seconds left'
>>> print(qc1)
      distance: 49.23410161513776   
      dt_start: 2015-06-11 17:15:31.468750
      maxspeed: 0.5                 
       maxtime: 300                 
      position: (1277, 200, 2300)   
   secondsleft: 96.859375           
     spaceunit: 0.01                

>>> qc1.move([(0,0,1000),(1000,0,0),(200,200,-200),(77,0,0),(0,0,500)])
...flying...
...flying...
...flying...
...flying...
...flying...
'flown: 78.4682032302755 meter, 24.703125 seconds left'
>>> qc1.move([(0,0,1000)])
...flying...
'Battery empty: crash!!'
-----------------------------------------------------------------
"""

import datetime as dt
import time
import math

class Drone(object):
    """Generalisation of a flying machine"""
    # resolution of our 3d model in meters
    spaceunit = 0.01  # 1 cm
        

class QuadCopter(Drone):
    """Remote controlled helicopter with four roters"""
    # constructor
    def __init__(self, start_position_xyz=(0, 0, 0), max_meter_per_sec=0.5, battery_life_secs=100):
        self.position = start_position_xyz
        self.maxspeed = max_meter_per_sec
        self.maxtime  = battery_life_secs
        self.dt_start  = dt.datetime.utcnow()
        self.distance  = 0   # total distance flown in meters

    @property
    def secondsleft(self):
        """remaining battery life"""
        return self.maxtime - (dt.datetime.utcnow() - self.dt_start).total_seconds()

    # printer
    def __str__(self):
        """print (instance)"""
        toprint = dict([(attr, getattr(self,attr)) for attr in dir(self) \
                        if not attr.startswith('__') and not 'method' in str(getattr(self,attr))])
        result =''
        for key in sorted(toprint):
            result += "{:>14}: {:<30}\n".format(key, str(toprint[key]))
        return result    

# --------- 
# OPLOSSING
# ---------

    def move(self, command_list=[(0,0,0)]):
        """ Moves the quadcopter.
        - A command is a tuple(backward_forward, left_right, down_up).
        - Example:  (0,0,100) moves the QC 100 units (1 meter)  up.
        - Example:  (-10,0,0) moves the QC 10 units backwards.
        - Example:  (0,100,-10) moves the QC 100 units to the right and 10 units down.
        Before and after every move/command the battery life (secondsleft) is checked.
        A move calculates the distance covered, the new position, and the time it takes
        to fly the distance at max speed. When the QC is flying no new commands will
        be processed (time.sleep(seconds_flying)).
        Resources:
        - http://math.stackexchange.com/questions/42640/calculate-distance-in-3d-space
        """
        

        self.command = command_list
        secondsflown = 0
        startpositie = list(self.position)
              
        for directie in self.command:
            for i in directie:            
                voor_achter = directie[0]
                links_rechts = directie[1]
                boven_beneden = directie[2]
                formule = (math.sqrt((voor_achter**2 + links_rechts**2 + boven_beneden**2)))/100
                seconds_flying = formule/self.maxspeed
            startpositie[0] += voor_achter
            startpositie[1] += links_rechts
            startpositie[2] += boven_beneden
                
            if seconds_flying < self.secondsleft:
                print('...flying...')
                time.sleep(seconds_flying)
                self.distance += formule
                secondsflown += seconds_flying
                self.position = tuple(startpositie)
            elif seconds_flying >= self.secondsleft and self.secondsleft > 0:
                print('...flying...')
                self.distance += formule *(self.secondsleft/seconds_flying)
                time.sleep(self.secondsleft)
                print('Battery empty: crash!')
                
                secondsflown += seconds_flying
                self.position = tuple(startpositie)
            elif self.secondsleft <= 0:
                print('Battery empty')
                
        if seconds_flying < self.secondsleft:
            print('flown ', self.distance, 'meter', self.secondsleft, 'seconds left')
        

    

qc1 = QuadCopter()
qc1.move([(0,0,1000)])
qc1.move([(0,0,1000),(1000,0,0),(200,200,-200),(77,0,0),(0,0,-500)])
qc1.move([(0,0,1000)])

print(qc1)

qc1.move([(0,0,1000),(1000,0,0),(200,200,-200),(77,0,0),(0,0,500)])
qc1.move([(0,0,1000)])



    
                                

    
    

    
        
