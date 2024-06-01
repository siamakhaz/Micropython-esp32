# boot.py

#pin 35 and 0 are related to botons
# pin 34 if for ADC
import machine
# import main
pin13 = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
# Import necessary modules
# import main
# main.main()
# Run the main script

# Create an ADC object on Pin 34 (example for ESP32, the pin number may vary for different boards)
adc = machine.ADC(machine.Pin(36))

# Optionally, you can configure the ADC attenuation to adjust the input voltage range
adc.atten(machine.ADC.ATTN_11DB)  # This sets the range to 0 - 3.6V

# Read the ADC value

while pin13.value():
    adc_value = adc.read()

    print("ADC Value:", adc_value)
    
    # print(pin13.value())
