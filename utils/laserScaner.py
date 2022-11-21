import cv2
import numpy as np
import open3d as o3d


class ProfileMeter:
    def __init__(self):
        self.cloud_points = []
        self.cloud_points_current = None
        self.z = 0
        self.step = 25
        self.xyz = []
        self.angle = 45

    def laser_detetctor(self, img, thresh=60):
        _, laser_mask = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
        # laser_mask = cv2.erode( laser_mask, (25,25), iterations=10 )
        return laser_mask

    def extract_points_mean(self, mask):
        ys, xs = np.nonzero(mask)
        ys_sum_per_xs = np.bincount(xs, ys)
        ys_count_per_xs = np.bincount(xs, np.ones(ys.shape, dtype=np.int16))
        exist_points = ys_count_per_xs > 0
        # exist_points[exist_points==False] = True

        mean_y = ys_sum_per_xs[exist_points] / ys_count_per_xs[exist_points]
        xs = np.argwhere(exist_points)

        mean_y = np.expand_dims(mean_y, axis=-1)
        mean_pts = np.hstack((xs, mean_y)).astype(np.int32)

        # mean_pts[:,1][mean_pts[:,1]<0] = 0

        return mean_pts

    def pts2img(self, pts, shape):
        pts = pts.astype(np.int32)
        mask = np.zeros(shape, dtype=np.uint8)
        mask[pts[:, 1], pts[:, 0]] = 255
        return mask

    def img2pts(self, mask):
        y, x = np.nonzero(mask)
        pts = np.array(list(zip(x, y)))
        return pts

    def save_points(self, pts):
        temp_xyz = np.zeros((len(pts), 3), dtype=np.int32)
        temp_xyz[:, 0] = pts[:, 0]
        temp_xyz[:, 2] = pts[:, 1]
        temp_xyz[:, 1] = self.z
        self.z += self.step
        self.cloud_points.append(temp_xyz)
        self.cloud_points_current = temp_xyz

    def get_cloudPoints_current(self):

        self.xyz_current = self.cloud_points_current
        self.xyz_current[:, 2] = self.xyz_current[:, 2] / np.cos(np.deg2rad(self.angle))
        # normals = np.zeros_like( self.xyz_current )
        # normals[:,2]=-1
        # pcd = o3d.geometry.PointCloud()
        # pcd.points = o3d.utility.Vector3dVector(self.xyz_current)
        # pcd.normals = o3d.utility.Vector3dVector( normals )

        # np.save('xyzs/xyz_current_%s.npy' % itr, self.xyz_current)

        return self.xyz_current

    def get_cloudPoints(self):

        self.xyz = np.concatenate(self.cloud_points)
        self.xyz[:, 2] = self.xyz[:, 2] / np.cos(np.deg2rad(self.angle))
        normals = np.zeros_like(self.xyz)
        normals[:, 2] = -1
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(self.xyz)
        pcd.normals = o3d.utility.Vector3dVector(normals)

        np.save("xyzs/xyz.npy", self.xyz)

        return pcd

    def show3D(self, pcd):
        vectors = o3d.geometry.TriangleMesh.create_coordinate_frame()
        print("vectors:", vectors)

        o3d.visualization.draw_geometries([pcd, vectors])

    def bbox_creator(self):

        pts = np.array(self.xyz)
        np.save("xyz.npy", self.xyz)
        minx = pts[:, 0].min() - 5
        maxx = pts[:, 0].max() + 5

        miny = pts[:, 1].min() - 5
        maxy = pts[:, 1].max() + 5

        minz = pts[:, 2].min() - 5
        maxz = pts[:, 2].max() + 5

        bbox = [
            [minx, miny, maxz],
            [minx, miny, minz],
            [minx, maxy, minz],
            [minx, maxy, maxz],
            [maxx, miny, maxz],
            [maxx, miny, minz],
            [maxx, maxy, minz],
            [maxx, maxy, maxz],
        ]
        bbox = np.array(bbox)
        bbox = o3d.utility.Vector3dVector(bbox)
        bbox_mesh = o3d.geometry.OrientedBoundingBox.create_from_points(bbox)
        return bbox_mesh

    def meshPoissonBuilder(
        self, pcd, bbox, smooth=0, depth=9, width=10, scale=2, linear_fit=False
    ):
        poisson_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
            pcd, depth=depth, width=width, scale=scale, linear_fit=linear_fit
        )[0]
        # bbox = pcd.get_axis_aligned_bounding_box()
        if bbox is False:
            pass
        else:
            poisson_mesh = poisson_mesh.crop(self.bbox_creator())
        poisson_mesh.paint_uniform_color([0.7, 0.7, 0.7])  # [0.7, 0.4, 0.5] صورتي
        if smooth > 0:
            mesh_lod = poisson_mesh.filter_smooth_simple(number_of_iterations=smooth)

        else:
            mesh_lod = poisson_mesh

        mesh_lod.remove_degenerate_triangles()
        mesh_lod.remove_duplicated_triangles()
        mesh_lod.remove_duplicated_vertices()
        mesh_lod.remove_non_manifold_edges()
        mesh_lod.compute_vertex_normals()
        mesh_lod.compute_triangle_normals()

        # o3d.io.write_triangle_mesh( MESH_PATH, mesh_lod )
        self.show3D(mesh_lod)
        return mesh_lod

    def meshBallPivotBuilder(self, pcd, smooth=0):

        distances = pcd.compute_nearest_neighbor_distance()
        avg_dist = np.mean(distances)
        factor = 3
        radius = factor * avg_dist
        radi = o3d.utility.DoubleVector([radius, radius * 2])
        bpa_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
            pcd, radi
        )

        # ARG = 10000
        # p_mesh_crop = p_mesh_crop.simplify_quadric_decimation(ARG)
        bpa_mesh.paint_uniform_color([0.7, 0.4, 0])
        if smooth > 0:
            mesh_lod = bpa_mesh.filter_smooth_simple(number_of_iterations=smooth)
        else:
            mesh_lod = bpa_mesh

        return mesh_lod

    def out_window(img, mask, output_size=None):

        LINE = 10
        if output_size == None:
            img = cv2.resize(img, None, fx=0.25, fy=0.25)
            mask = cv2.resize(mask, None, fx=0.25, fy=0.25)

        h, w, _ = img.shape
        result = np.zeros((h, w * 2 + LINE, 3), dtype=np.uint8)
        result[:, :w] = img
        result[:, w : w + LINE, 0] = 255
        result[:, w + LINE :, 2] = mask

        return result
