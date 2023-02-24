# Vehicle_counting

What is YOLO?
YOLO stands for You Only Look Once. It is a real-time object recognition algorithm. It can classify and localize multiple objects in a single frame. YOLO is a very fast and accurate algorithm for its simpler network architecture.

How does YOLO work?
YOLO works using mainly these techniques.

1. Residual Blocks – Basically, it divides an image into NxN grids.

2. Bounding Box regression – Each grid cell is sent to the model. Then YOLO determines the probability of the cell contains a certain class and the class with the maximum probability is chosen.

3. Intersection Over Union (IOU) – IOU is a metric that evaluates intersection between the predicted bounding box and the ground truth bounding box. A Non-max suppression technique is applied to eliminate the bounding boxes that are very close by performing the IoU with the one having the highest class probability among them.

Prerequisites for Vehicle Detection and Classification Project using OpenCV:
1. Python – 3.x (We used python 3.8.8 in this project)
2. OpenCV – 4.4.0

It is strongly recommended to run DNN models on GPU.
You can install OpenCV via “pip install opencv-python opencv_contrib-python”.
3. Numpy – 1.20.3
4. YOLOv3 Pre-trained model weights and Config Files.
