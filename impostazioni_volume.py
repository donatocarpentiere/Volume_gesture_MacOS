import subprocess

def imposta_volume(volume):
    volume = max(0, min(volume, 1))  # Assicura che il volume sia compreso tra 0 e 1
    script = f"set volume output volume {(volume * 100)}"
    subprocess.run(["osascript", "-e", script])
