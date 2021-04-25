import clustering


# K-NN
'''

'''

# K-MEANS
'''k_means_model = clustering.KMeans()  # 
k_means_model.set_points(point_n=200)  #  set_points(point_n)  point_n : number of points
k_means_model.train(30, is_save=True, lev=5)  # train(iteration , is_save, lev)  is_save : save fig , lev : number of fig'''


# Hierarchical
hierachical_model = clustering.Hierarchical()
hierachical_model.set_points(point_n=20)
hierachical_model.cluster(cluster_n=3)
