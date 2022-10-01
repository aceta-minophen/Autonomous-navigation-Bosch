from kalmanfilter import KalmanFilter
from shapes import Paper, Triangle, Rectangle, Oval

# Kalman Filter
kf = KalmanFilter()


ball_positions = [(50, 100), (100, 100), (150, 100), (200, 100),
                  (250, 100), (300, 100), (350, 100), (400, 100), (450, 100), (500, 200), (550, 300), (600, 300)]


paper = Paper()

obj = Oval()

pred = Oval()


for pt in ball_positions:
    obj.set_param(20, 20, pt[0], pt[1], "red")
    predicted = kf.predict(pt[0], pt[1])

    #pred.set_param(20, 20, predicted[0], predicted[1], "green")

    # pred.draw()

    obj.draw()


for i in range(10):
    predicted = kf.predict(predicted[0], predicted[1])

    pred.set_param(20, 20, predicted[0], predicted[1], "green")
    pred.draw()


paper.display()
