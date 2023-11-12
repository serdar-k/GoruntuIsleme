import cv2
import numpy as np

# BILGISAYARDAKI WEBCAM'I KULLANMAK
capture = cv2.VideoCapture(0)

while True:
    _, frame = capture.read()
    # ALINAN GORUNTUNUN RENK FORMATI BGR'DEN HSV'YE CEVRILDI
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # cv2.imshow("Frame", frame)

    # TESPIT EDILECEK RENKLER ICIN ALT VE UST LIMITLER TANIMLANIR
    # KIRMIZI ICIN HSV SINIRLARI
    lower_red = np.array([160, 150, 80])
    upper_red = np.array([180, 255, 255])

    # SADECE KIRMIZI RENKLI NESNELERIN GORUNMESI ICIN MASKE UYGULANIR
    red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)

    # BITWISE_AND KULLANILARAK KIRMIZI RENGE AIT DEGERLER ILE EKRANDA GOSTERILECEK OLAN DEGERLER AND
    # ISLEMINE SOKULUR VE BOYLECE SADECE KIRMIZI RENKLI NESNELER EKRANDA GORUNUR
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

    cv2.imshow("Red Mask", red)

    quitKey = cv2.waitKey(1)
    # ESC ILE FRAME KAPATILIR
    if quitKey == 27:
        break
