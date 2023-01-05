import open3d as o3d 
import time
import numpy as np
import matplotlib.pyplot as plt
import hdbscan

pcd = o3d.io.read_point_cloud("000012.pcd")

t1 = time.time()
plane_model, inliers = pcd.segment_plane(distance_threshold=0.3, ransac_n=3, num_iterations=100)
inlier_cloud = pcd.select_by_index(inliers)
outlier_cloud = pcd.select_by_index(inliers, invert=True)
inlier_cloud.paint_uniform_color([0.5, 0.5, 0.5])
outlier_cloud.paint_uniform_color([1, 0, 0])
t2 = time.time()

# CLUSTERING WITH HDBSCAN
t3 = time.time()
clusterer = hdbscan.HDBSCAN(min_cluster_size=50, gen_min_span_tree=True)
clusterer.fit(np.array(outlier_cloud.points))
labels = clusterer.labels_

max_label = labels.max()
print(f'point cloud has {max_label + 1} clusters')
colors = plt.get_cmap("tab20")(labels / max_label if max_label > 0 else 1)
colors[labels < 0] = 0
outlier_cloud.colors = o3d.utility.Vector3dVector(colors[:, :3])
t4 = time.time()
print(f'Time to cluster outliers using HDBSCAN {t4 - t3}')
o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])