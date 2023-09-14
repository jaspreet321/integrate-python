import subprocess
import pyautogui
import time

# Open Notepad
notepad_process = subprocess.Popen(['notepad.exe'])

try:
    while True:
        # Give Notepad some time to open
        time.sleep(1)

        # Type 'x' in Notepad
        pyautogui.typewrite('x')

        # Wait for 1 second before typing 'x' again
        time.sleep(1)

except KeyboardInterrupt:
    # Close Notepad when the script is terminated
    notepad_process.terminate()

