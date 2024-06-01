from lib import wifi
from lib import lcd
from lib import webserver
import json

def load_credentials():
    with open('cred.json', 'r') as file:
        credentials = json.load(file)
    return credentials['SSID'], credentials['PASSWORD']

def main():
    # Load Wi-Fi credentials
    SSID, PASSWORD = load_credentials()

    # Initialize LCD
    display = lcd.init_lcd()
    lcd.display_text(display, 'Motopya!', 50, 50, display.color565(255, 255, 255))

    # Connect to Wi-Fi
    ip_address = wifi.connect_wifi(SSID, PASSWORD)
    lcd.display_text(display, "IP Address:", 50, 130, display.color565(0, 255, 255))
    lcd.display_text(display, ip_address, 50, 150, display.color565(255, 0, 255))

    # Read the HTML content from the file
    html = webserver.read_html_file('html/index.html')

    # Start the web server
    webserver.start_server(html)

# if __name__ == "__main__":
#     main()
