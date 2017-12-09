import cv2
import time

# Check fps for video
# cap = cv2.VideoCapture('demo.mp4')

# Check fps from live cam
num_frames = 0
cap = cv2.VideoCapture(0)

start = time.time()

while num_frames <= 120:
	ret, image = cap.read()

	cv2.imshow('video', image)
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break
	num_frames += 1

end = time.time()
seconds = end - start

fps = num_frames / seconds
cap.release()
print(fps)
