# JODHA
## Jodhpur Dataset for Heterogeneous Environment Analysis

- Duration: 30 minutes
- Camera: Sony (1920x1080, 30 fps)
- LiDAR: Velodyne VLP-16 (10 Hz)
- Data Format: Synced `.jpg` and `.pcd` frames
- Sync: Manual, based on frame offset
- Location: Urban roads, Jodhpur, Rajasthan

### Folder Structure
- `images/`: Synchronized camera frames
- `lidar/`: Synchronized and filtered point clouds
- `calib/`: [TBD]
- `sync_config.json`: Camera–LiDAR frame mapping

### Preprocessing
- Video extracted using FFmpeg at 30 FPS
- Point clouds filtered using Open3D (range < 50m)
- Manual synchronization using visual landmarks
