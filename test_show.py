import open3d as o3d
pcd = o3d.io.read_point_cloud("000012.pcd")

# visualization with open3d
o3d.visualization.draw_geometries([pcd])
