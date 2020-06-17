/* I2C LCD with Arduino example code. More info: https://www.makerguides.com */

// Include the libraries:
// LiquidCrystal_I2C.h: https://github.com/johnrickman/LiquidCrystal_I2C
#include <Arduino.h> 
#include <Wire.h> // Library for I2C communication
#include <LiquidCrystal_I2C.h> // Library for LCD
#include <SoftwareSerial.h> // Library for Serial communication


// Wiring: SDA pin is connected to A4 and SCL pin to A5.
// Connect to LCD via I2C, default address 0x27 (A0-A2 not jumpered)
LiquidCrystal_I2C lcd = LiquidCrystal_I2C(0x27, 16, 2); // Change to (0x27,16,2) for 16x2 LCD.

void setup() {
  // Initiate the LCD:
  lcd.init();
  lcd.backlight();
  Serial.begin(4800);
  Serial.print("Arduino ON");
  lcd.print("Arduino ON");
  delay(500);
  lcd.clear();
  Serial.print("Entering loop...");
  lcd.print("Entering loop...");
  delay(500);
  lcd.clear();
}

void loop() {
// Print 'Hello there' on the first line of the LCD:
    lcd.setCursor(0, 0); // Set the cursor on the first column and first row.
    lcd.print("Hello there"); // Print the string "Hello there!"
    Serial.print("Hello there");
    lcd.setCursor(0, 1); //Set the cursor on the third column and the second row (counting starts at 0!).
    lcd.print("Would you like a MUSHROOM?");
    Serial.print("Would you like a MUSHROOM?");
}