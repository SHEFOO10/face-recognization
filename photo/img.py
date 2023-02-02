import cv2
import sys
from PIL import Image
import improve_img as im

imagePath = sys.argv[1]

Image.open(imagePath).transpose(Image.ROTATE_90).save(imagePath, dpi=(300,300))

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=3,
    minSize=(80, 70)
)

print(faces)
print("[INFO] Found {0} Faces.".format(len(faces)))
i = 0

for (x, y, w, h) in faces:
    roi_color = image[y - 55 :y + h + 60, x - 35 : x + w + 35]
    print("[INFO] Object found. Saving locally.")
    filename = str(i) + str(i) + '_faces.jpg'
    print(filename)
    cv2.imwrite(str(i) + str(i) + '_faces.jpg', roi_color)
    
    im.improve(filename)
    i +=1
