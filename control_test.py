import matplotlib.pyplot as plt
import math


class robot:
    def __init__(self,target_x,target_y,target_z,step_size,path_x,path_y,path_z,now_x,now_y,now_z):
        ## tx,ty,tz ターゲットのポジション
        ## step_size 経路の点の数
        ## px,py,pz 第三の点
        self.x=target_x
        self.y=target_y
        self.z=target_z
        self.step_size=step_size
        self.px=path_x
        self.py=path_y
        self.pz=path_z
        self.nx=now_x
        self.ny=now_y
        self.nz=now_z
    def routegen(self):
        rx=[]
        ry=[]
        for i in range(0,11):
            t:float=i/10
            rx.append(self.nx*pow((1-t),2)+2*self.px*(1-t)*t+self.x*pow(t,2))
            ry.append(self.ny*pow((1-t),2)+2*self.py*(1-t)*t+self.y*pow(t,2))
        
        return rx,ry
         
        
def main():
    print("start")
    tx=4.0
    ty=5.0
    tz=0.0
    step=10
    px=2.5
    py=2.5
    pz=0.0
    nx=0.0
    ny=0.0
    nz=0.0
    robo=robot(tx,ty,tz,step,px,py,pz,nx,ny,nz)
    rx,ry=robot.routegen(robo)
    plt.plot(rx, ry)
    plt.plot(px,py)
    plt.show()

if __name__ == '__main__':
    main()

        