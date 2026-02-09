import constant as cst
import numpy as np
from matplotlib.animation import FuncAnimation

class Pyramid:
    def __init__(self, max_h):
        self.max_h = max_h
        self.bricks_count = 0

    def add_bricks(self, count):
        self.brick_count = self.bricks_count + count

    def is_done(self):
            return self.bricks_count >= ((self.max_h *(self.max_h + 1))//2)
    def get_height(self):
              virtual_bricks = self.bricks_count
              current_level = 1
              current_level_bricks_count = self.max_h
              while vurtual_bricks > 0:
                vurtual_bricks = vurtual_bricks - current_level_bricks_count
                current_level_bricks_count = current_level_bricks_count - 1
                current_level = current_level + 1
              return current_level - 1
pyramid = Pyramid(4)    
for i in range(10):
     pyramid.add_bricks(1)
     print(pyramid.get_height())
