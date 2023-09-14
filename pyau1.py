import pyautogui
import time

# Set the speed of mouse movement (you can adjust this value)
movement_speed = 100  # Adjust as needed

# Get the screen width and height
screen_width, screen_height = pyautogui.size()

try:
    while True:
        # Move right
        pyautogui.moveTo(screen_width - 1, pyautogui.position().y, duration=movement_speed / 1000.0)
        time.sleep(1)

        # Move down
        pyautogui.moveTo(pyautogui.position().x, screen_height - 1, duration=movement_speed / 1000.0)
        time.sleep(1)

        # Move left
        pyautogui.moveTo(1, pyautogui.position().y, duration=movement_speed / 1000.0)
        time.sleep(1)

        # Move up
        pyautogui.moveTo(pyautogui.position().x, 1, duration=movement_speed / 1000.0)
        time.sleep(1)

except KeyboardInterrupt:
    print("\nMouse movement script stopped.")

