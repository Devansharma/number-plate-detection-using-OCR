import cv2
import easyocr

classifier = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
reader = easyocr.Reader(['en'])

img = cv2.imread("images.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
numberplate = classifier.detectMultiScale(img_gray,
                            scaleFactor=1.025, minNeighbors=5)
if len(numberplate) > 0:
    for (x, y, w, h) in numberplate:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,255), 2)
        cropped = img[y:y+w, x:x+w]
        bounds = reader.readtext(cropped)
        cv2.putText(img, bounds[0][1], (x, y-5), 
                       cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2)
        cv2.imshow("Number Plate", img)
        cv2.waitKey()
        cv2.destroyAllWindows()
        