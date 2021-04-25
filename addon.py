import random
import math

def neighbor(point, centroids):
    dist_list = list(map(lambda centroid : dist(point, centroid), centroids))
    group_index = np.argmin(dist_list)
    return group_index
    
def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def get_random_xy(min_val, max_val, limit=None):
    if limit:
        x_min, x_max, y_min, y_max = limit
        return random.randint(x_min, x_max), random.randint(y_min, y_max)
    else:
        return random.randint(min_val, max_val), random.randint(min_val, max_val)
    
def get_x_list(xy_list):
    return list(map(lambda point: point[0], xy_list))
         
def get_y_list(xy_list):
    return list(map(lambda point: point[1], xy_list))

def get_colors(n):
    color_x = np.arange(n)
    color_y = [i+color_x+(i*color_x)**2 for i in range(n)]
    colors = cm.rainbow(np.linspace(0, 1, len(color_y)))
    return colors

def get_centroid_from_group(group):
    x_sum = 0
    y_sum = 0
    for (x,y) in group:
       x_sum += x
       y_sum += y
    return x_sum/len(group), y_sum/len(group)