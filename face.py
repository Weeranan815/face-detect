
import cv2  
img = cv2.imread('img.jpg')#เเปลงจาก ImagePath ให้ใส่ในตัวเเปล img
face_cascade = cv2.CascadeClassifier('front_face.xml')#เเปลงตรวจจับใบหน้าให้อยู่ใน face_cascade
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#แปลงรูปเป็นขาวดำ

faces = face_cascade.detectMultiScale(gray, 1.3)   #ใช้ Haar Cascades ในการตรวจจับใบหน้า
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(222,255,0), 2)   #วาดกรอบใบหน้าสีฟ้า
    
cv2.imshow('img.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()