import open3d as o3d
import numpy as np

# point cloud → numpy
pcd = o3d.io.read_point_cloud("000012.pcd")

#o3d.visualization.draw_geometries([pcd])


print(f"Points before downsampling: {len(pcd.points)} ")
pcd = pcd.voxel_down_sample(voxel_size=0.5)
print(f"Points after downsampling: {len(pcd.points)}")




#pcd, inliers = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
pcd, inliers = pcd.remove_radius_outlier(nb_points=20, radius=0.5)
inlier_cloud = pcd.select_by_index(inliers)
outlier_cloud = pcd.select_by_index(inliers, invert=True)
inlier_cloud.paint_uniform_color([0.5, 0.5, 0.5])
outlier_cloud.paint_uniform_color([1, 0, 0])
o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])

#o3d.visualization.draw_geometries([pcd])
