import cv2
import dlib
import numpy as np

# Inicializando o detector de rosto do dlib
detector = dlib.get_frontal_face_detector()

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("/dev/video0")

# Tente usar o codec MJPEG
# cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

# Definindo a resolução e taxa de quadros
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

if not cap.isOpened():
    print("Erro ao abrir a webcam.")
else:
    print("Webcam aberta com sucesso.")

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    cv2.imshow("Detecção Facial", frame)
    k = cv2.waitKey(30)
    if k == 27:
        break

    # print(faces)
    i = 0
    for face in faces:
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
        i += 1
        cv2.putText(
            frame,
            "Qtd face " + str(i),
            (x - 10, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2,
        )
        print(face, i)

    cv2.imshow("Detecção Facial", frame)
    k = cv2.waitKey(30)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
