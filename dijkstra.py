
from re import I
from tkinter import Y
import matplotlib.pyplot as plt
import math

show_animation = True

class Dijkstra:
    def __init__(self,ox,oy,resolution,robot_radius):
        
        self.min_x=None
        self.min_y=None
        self.max_x=None
        self.max_y=None
        self.x_width=None
        self.y_width=None
        self.obstacle_map=None
        self.resolution=resolution
        self.robot_radius=robot_radius
        self.clac_obstacle_map(ox,oy)
        self.motion=self.get_motion_model()


class Node:
      def __init__(self,x,y,cost,parent_index):
         self.x=x
         self.y=y
         self.cost=cost
         self.parent_index=parent_index
      def __str__(self) -> str:
         return str(self.x) + "," + str(self.y) + "," + str(self.cost)+","+str(self.parent_index)

      def planning(self,sx,sy,gx,gy):
          start_node=self.Node(self.calc_xy_index(sx,self.min_x),self.clac_xy_index(sy,self.min_y),0.0,-1)
          gorl_node=self.Node(self.clac_xy_index(gx,self.min_x),self.clac_xy_index(gy,self.min_y),0.0,-1)
          open_set,closed_set=dict(),dict()
          open_set[self.calc_index(start_node)]=start_node

          while 1:
             c_id=min(open_set,key=lambda o: open_set[o].cost)
             current=open_set[c_id]

             if show_animation:
                plt.plot(self.calc_positon(current.x,self.min_x)),self.calc_positon(current.y,self.min_y),"xc")
                plt.gcf().canvas.mpl_connect(
                   'key_release_event',lambda event: [exit(0) if event.key=='escape']
                )
             
