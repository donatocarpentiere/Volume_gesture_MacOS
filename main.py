import cv2
import platform
from rilevamento_mano import processa_frame

def main():
    if platform.system() != "Darwin":
        raise RuntimeError("Questo script supporta solo macOS")

    videocamera = cv2.VideoCapture(0)

    while videocamera.isOpened():
        successo, img = videocamera.read()
        if not successo:
            break

        img = processa_frame(img)

        cv2.imshow('Immagine', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    videocamera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
