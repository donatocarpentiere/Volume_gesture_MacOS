# Italian version
# Descrizione progetto "Volume_gesture_MacOS"
Il progetto "Volume_gesture_MacOS" è una soluzione innovativa che utilizza OpenCV e MediaPipe per il rilevamento dei gesti della mano tramite una webcam. Il progetto è stato sviluppato specificamente per macOS e permette di regolare il volume del sistema in base alla distanza rilevata tra il pollice e l'indice della mano. 

## Struttura del Progetto

- `main.py`: Il file principale che avvia la webcam e gestisce il ciclo principale.
- `impostazioni_volume.py`: Contiene la funzione per impostare il volume su macOS.
- `calcoli.py`: Contiene la funzione per calcolare la lunghezza tra due punti.
- `rilevamento_mano.py`: Contiene la logica per il rilevamento delle mani e l'elaborazione dell'immagine.

## Requisiti

- macOS
- Python 3.x
- OpenCV
- MediaPipe
- NumPy

## Installazione

1. Clona questo repository:
   ```sh
   git clone https://github.com/donatocarpentiere/Volume_gesture_MacOS.git

2. Naviga nella directory del progetto:
   ```sh
   cd Volume_gesture_MacOS
   
3. Installa le dipendenze:
   ```sh
   pip install -r requirements.txt

4. Per eseguire il progetto, esegui il seguente comando:
   ```sh
   python main.py

## Note
* Questo script supporta solo macOS.
* Assicurati di avere la webcam collegata e funzionante.

## Contribuire
Se desideri contribuire al progetto, sentiti libero di fare un fork del repository e inviare una pull request. Tutti i suggerimenti e i miglioramenti sono benvenuti.

## Licenza
Questo progetto è concesso in licenza con MIT License.


# English version
# Project description "Volume_gesture_MacOS"
The "Volume Mano" project is an innovative solution that uses OpenCV and MediaPipe for hand gesture detection via a webcam. The project was specifically developed for macOS and allows adjusting the system volume based on the distance detected between the thumb and the index finger.

## Features
- **Hand gesture detection**: Uses the MediaPipe library to detect hand landmarks in real-time via a webcam.
- **Distance calculation**: Calculates the distance between the thumb and the index finger using the NumPy library.
- **Volume adjustment**: Adjusts the macOS system volume based on the detected distance, with a visual interface showing the current volume percentage.

## Requirements

- macOS
- Python 3.x
- OpenCV
- MediaPipe
- NumPy

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/donatocarpentiere/Volume_gesture_MacOS.git

2. Navigate to the project directory:
   ```sh
   cd Volume_gesture_MacOS
   
3. Install the dependencies:
   ```sh
   pip install -r requirements.txt

4. To run the project, execute the following command:
   ```sh
   python main.py

## Notes
* This script only supports macOS.
* Make sure you have a working and connected webcam.

## Contributing
If you want to contribute to the project, feel free to fork the repository and submit a pull request. All suggestions and improvements are welcome.

## License
This project is licensed under the MIT License.


   
   
