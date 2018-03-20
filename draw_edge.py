import numpy as np  
import cv2  
  
  
def draw_edge(image):  
    heigth=len(image)  
    width=len(image[0])  
    cv2.imshow('原图',image)#显示原图像  
  
    thorg = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)#为方便标记联通域，转为bgr，实际上我不需要用到它    
  
    G=[[(0,0)]]  
    for x in range(0,heigth):  
        print(x)  
        for y in range(0,width):  
            if thorg[x,y][0]==0 and thorg[x,y][1]==0 and thorg[x,y][2]==0:#找黑色的联通域  
                count=[0,0]#统计和之前几个区域相连  
                for index,g in enumerate(G):  
                    for i in g[::-1]:#倒序遍历计算量更少  
                        if abs(i[0]-x)>1:#相隔超过一行的点不需要看了  
                            continue  
                        if (abs(i[0]-x)+abs(i[1]-y))==1:#说明和之前发现的联通域相连  
                            if count[0]!=0:#一个新的像素可能和之前两个联通域相连，那么他们实际上是同一个联通域，合并  
                                G[count[1]]+=G[index]  
                                G.pop(index)#合并两个联通域  
                                break  
                            else:#在此联通域上增加新的像素  
                                G[index].append((x,y))  
                                count[0]=1  
                                count[1]=index  
                                break  
                if count[0]==0:#新的联通域  
                    G.append([(x,y)])  
  
  
    print(len(G))#共有多少个联通域  
  
  
    for i in G:  
        for j in i:  
            x=j[0]  
            y=j[1]  
            thorg[x,y][0]=255#全部联通域设为浅蓝色  
            thorg[x,y][1]=255  
    cv2.imshow('thorg',thorg)#  
  
    cv2.waitKey(0)  
    cv2.destroyAllWindows()  
  
  
if __name__ == "__main__":  
    path="your image's path"  
    imagename=path+'your image.tif'  
    image=cv2.imread(imagename,0)#灰度方式读取  

    draw_edge(image)  