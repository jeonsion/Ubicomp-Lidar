import open3d as o3d 
import time
import numpy as np

pcd = o3d.io.read_point_cloud("000012.pcd")

t1 = time.time()
plane_model, inliers = pcd.segment_plane(distance_threshold=0.3, ransac_n=3, num_iterations=100)
inlier_cloud = pcd.select_by_index(inliers)
outlier_cloud = pcd.select_by_index(inliers, invert=True)
inlier_cloud.paint_uniform_color([0.5, 0.5, 0.5])
outlier_cloud.paint_uniform_color([1, 0, 0])
t2 = time.time()
print(f"Time to segment points using RANSAC {t2 - t1}")
o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])