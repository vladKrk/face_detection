# import cv2


# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
# #smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

# cap = cv2.VideoCapture(0)
# while 1:
# 	ret, img = cap.read()
# 	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# 	for (x, y, w, h) in faces:
# 		cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
# 		roi_gray = gray[y:y + h, x:x + w]
# 		roi_color = img[y:y + h, x:x + w]

# 		eyes = eye_cascade.detectMultiScale(roi_gray)
# 		#smile = smile_cascade.detectMultiScale(roi_gray)
# 		for (ex, ey, ew, eh) in eyes:
# 			cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 255), 2)
# 		#for (sx,sy,sw,sh) in smile:
# 		#	cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (255, 0, 255), 2)

# 	cv2.imshow('img', img)
# 	if cv2.waitKey(1) & 0xFF == 27:
# 		break

# cap.release()
# cv2.destroyAllWindows()

import cv2

def useCascadeAnalyze(file_path):
    # Load the cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # Read the input image
    img = cv2.imread(file_path)
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display the output
    height, width, _ = img.shape
    width_new=int(width/2)
    height_new=int(height/2)
    img = cv2.resize(img, (width_new, height_new))
    cv2.imshow('img', img)
    cv2.waitKey()