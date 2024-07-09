import cv2
import mediapipe as mp
import numpy as np
from impostazioni_volume import imposta_volume
from calcoli import calcola_lunghezza

# Inizializzazione di MediaPipe per il rilevamento delle mani
mp_mani = mp.solutions.hands
mani = mp_mani.Hands()
mp_disegno = mp.solutions.drawing_utils

def processa_frame(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    risultati = mani.process(img_rgb)

    if risultati.multi_hand_landmarks:
        for punti_mano in risultati.multi_hand_landmarks:
            mp_disegno.draw_landmarks(img, punti_mano, mp_mani.HAND_CONNECTIONS)
            lista_punti = [(id, int(punto.x * img.shape[1]), int(punto.y * img.shape[0])) for id, punto in enumerate(punti_mano.landmark)]

            if lista_punti:
                x1, y1 = lista_punti[4][1], lista_punti[4][2]  # Pollice
                x2, y2 = lista_punti[8][1], lista_punti[8][2]  # Indice

                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

                lunghezza = calcola_lunghezza(x1, y1, x2, y2)

                volume = np.interp(lunghezza, [50, 300], [0, 1])
                imposta_volume(volume)

                cv2.putText(img, f'Volume: {int(volume*100)}%', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

    return img
