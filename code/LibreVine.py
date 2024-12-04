import webbrowser
import time
from pynput import keyboard
import random
import os
import sys

class WebsiteOpener:
    def __init__(self):
        self.is_paused = False
        self.selected_browser = None
        self.listener = None
        self.intervals = []

    def toggle_pause(self):
        """Toggles the paused state when spacebar is pressed."""
        self.is_paused = not self.is_paused
        if self.is_paused:
            print("Paused. Press SPACE to resume.")
        else:
            print("Resuming...")

    def on_press(self, key):
        """Handles key press events."""
        if key == keyboard.Key.space:
            self.toggle_pause()
        elif key == keyboard.Key.esc:
            print("Exiting program...")
            return False  # Stops the listener

    def load_intervals(self):
        """Loads delay intervals from randominterval.txt (in seconds)."""
        try:
            with open(os.path.join('input', 'randominterval.txt'), 'r') as file:
                lines = file.readlines()
                self.intervals = [int(line.strip()) for line in lines[:10]]  # Read as full seconds
            if not self.intervals:
                print("No valid intervals found in randominterval.txt. Defaulting to 5-10 seconds delays.")
                self.intervals = [5, 10]  # Default intervals
        except FileNotFoundError:
            print("randominterval.txt not found. Defaulting to 5-10 seconds delays.")
            self.intervals = [5, 10]  # Default intervals
        except ValueError:
            print("Error reading intervals from randominterval.txt. Defaulting to 5-10 seconds delays.")
            self.intervals = [5, 10]  # Default intervals

    def open_chrome_browser(self):
        """Sets up Chrome as the browser to open websites."""
        try:
            # Read the browser path from browser.txt
            with open(os.path.join('input', 'browser.txt'), 'r') as file:
                chrome_path = file.read().strip()

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            print("Chrome browser registered successfully.")
            self.selected_browser = webbrowser.get('chrome')
        except FileNotFoundError:
            print("Error: Browser.txt file not found in input folder.")
        except Exception as e:
            print(f"Error registering Chrome: {str(e)}")

    def open_websites_from_file(self):
        """Reads websites from a file and opens them with specified delays."""
        if not self.selected_browser:
            print("Error: No browser selected.")
            return

        try:
            with open(os.path.join('input', 'websites.txt'), 'r') as file:
                websites = [line.strip().replace("\n", "") for line in file]

            for website in websites:
                while self.is_paused:
                    time.sleep(1)  # Wait while paused
                
                print(f"Opening: {website}")
                try:
                    self.selected_browser.open(f"https://{website}")
                    
                    # Delay between opening websites: randomly chosen from the loaded intervals
                    delay = random.choice(self.intervals) if self.intervals else random.randint(5, 10)
                    print(f"Waiting for {delay} seconds before opening next website...")
                    time.sleep(delay)
                except Exception as e:
                    print(f"Error opening {website}: {str(e)}")
        except FileNotFoundError:
            print("Websites file 'websites.txt' not found in input folder.")
        except Exception as e:
            print(f"An error occurred while reading the websites file: {str(e)}")

    def start_key_listener(self):
        """Starts the keyboard listener in a separate thread."""
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def stop_key_listener(self):
        """Stops the keyboard listener."""
        if self.listener:
            self.listener.stop()

    def start_program(self):
        """Wait for the user to type START or Q."""
        while True:
            user_input = input("Type 'START' to begin or 'Q' to quit: ").strip().upper()
            if user_input == 'START':
                print("Program starting...")
                break
            elif user_input == 'Q':
                print("Exiting program. Goodbye!")
                sys.exit(0)

    def countdown(self):
        """Countdown before starting the main program."""
        print("Starting in...")
        for i in range(10, 0, -1):
            print(i)
            time.sleep(1)

    def main(self):
        """Main program logic."""
        opener = self
        opener.start_program()
        opener.countdown()

        print("Press SPACE to pause/resume. Press ESC to exit.")
        
        try:
            opener.load_intervals()  # Load the intervals before opening websites
            opener.open_chrome_browser()
            opener.start_key_listener()
            opener.open_websites_from_file()
        finally:
            opener.stop_key_listener()

def keep_window_open():
    print("\nAll websites have been opened successfully!")
    print("Press R to restart the script from the beginning")
    print("or C to close the window")
    
    while True:
        key = input().lower()
        if key == 'r':
            opener.main()  # Restart the main method without launching a new process
            break
        elif key == 'c':
            sys.exit(0)

if __name__ == "__main__":
    opener = WebsiteOpener()
    try:
        opener.main()
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
    
    # Keep the window open after execution
    keep_window_open()
