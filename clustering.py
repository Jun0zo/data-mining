import math
import numpy as np
import random
import matplotlib.pyplot as plt 
import matplotlib.cm as cm
from addon import *

class KMeans():
    def __init__(self):
        self.points = list()
        self.centroids = list()
        self.groups = list()
        
        
    def set_points(self, point_n):  # Set points
        centroid_n = int(math.sqrt(int(point_n)))
        
        for _ in range(point_n):  # add points
            x, y = get_random_xy(1, 100)
            self.points.append((x,y))
            self.groups.append(None)
            
            
        for _ in range(centroid_n):  # add centroid
            x_min = min(get_x_list(self.points))
            x_max = max(get_x_list(self.points))
            y_min = min(get_y_list(self.points))
            y_max = max(get_y_list(self.points))
            x, y = get_random_xy(1, 100, (x_min, x_max, y_min, y_max))
            self.centroids.append((x,y))
        
        
    def set_points_random(self, rand_range=(5, 20)):  # Set points random
        point_n = random.randint(rand_range[0], rand_range[1])
        set_points(point_n)
        
        
    def match_points_and_centroids(self):  # return [ [p1, p3, p8] , [p4, p6, p7], ... ]
        matchs = []
        for centroid_index, centroid in enumerate(self.centroids):
            group_points = list()
            for point_index, group in enumerate(self.groups):
                if group == centroid_index:
                    group_points.append(self.points[point_index])
            matchs.append(group_points)
        return matchs
    
    
    def expactation(self):  # 
        for point_index, point in enumerate(self.points):
            group_index = neighbor(point, self.centroids)
            self.groups[point_index] = group_index
        
        
    def maximization(self):  # move centroids
        matchs = self.match_points_and_centroids()
        
        for group_index, match in enumerate(matchs):
            group_x_list = get_x_list(match)
            group_y_list = get_y_list(match)
            x_mean = np.mean(group_x_list)
            y_mean = np.mean(group_y_list)
            self.centroids[group_index] = (x_mean, y_mean)
        
        
    def train(self, it, is_save=False, lev=-1):  # expactation and maximization
        # self.plot('init')
        for step in range(it):    
            self.expactation()
            self.maximization()
            if is_save == True and step % (it/lev) == 0:
                print(step)
                self.plot(str(step))
            
            
    def plot(self, index):  # save scatter
        plt.clf()
        group_n = len(self.centroids)
        colors = get_colors(group_n)
        
        matchs = self.match_points_and_centroids()
        for group_index , match in enumerate(matchs):
            group_x_list = get_x_list(match)
            group_y_list = get_y_list(match)
            cur_color = colors[group_index]
            cur_centroid = self.centroids[group_index]
            
            plt.scatter(group_x_list, group_y_list, color=cur_color)
            plt.scatter(cur_centroid[0], cur_centroid[1], color=cur_color, marker='*', s=200)
        plt.savefig('./results/res_{}.jpg'.format(index))
            