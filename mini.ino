// include the library code:
#include <SoftwareSerial.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#define BACKLIGHT_PIN     13
LiquidCrystal_I2C lcd( 0x27, 2 , 1 , 0 , 4 , 5 , 6 , 7 , 3 , POSITIVE );

String inData; // buffer for the incoming serial data
String lcdEvent ="0"; // buffer for LCD text
int lcdOn; //defines the "is the LCD on?" variable
void setup()
{
  Serial.begin(9600);// initializes the serial comunication
  Serial.println("Serial conection started, waiting for instructions...");
// initialile values for the variables
  lcdOn =1;
  lcdEvent = inData;

lcd.begin(16,2); // set up the LCD's number of columns and rows

 if (lcdOn == 1) {
  lcd.display(); // turns on the lcd
  lcd.setBacklight(HIGH); // turns the backlight on
 }
else if (lcdOn == 0) {
  lcd.noDisplay(); // turns off the lcd
  lcd.setBacklight(LOW); // turns the backlight off
}

}


void loop()
{
   while (Serial.available() > 0)
      {
          char recieved = Serial.read();
          inData += recieved;

  //if (lcdEvent !="0") {

    // Process message when new line character is recieved
    if (recieved == '\n'){
        lcdEvent = inData;
        lcdEvent.trim();
        Serial.print("Arduino Received: ");
        Serial.print(inData);

        if (lcdEvent.length() < 16 ) {
          lcd.clear();
          lcd.setCursor(0,0);
          lcd.print(lcdEvent);
        }

         if (lcdEvent.length() > 16) {
          if (lcdEvent.length() < 32 ) {
            lcd.clear();
            lcd.setCursor(0,0);
            lcd.print(lcdEvent);
            lcd.setCursor(0,1);
            lcd.print("Cat");
          }
          lcd.clear();
          lcd.setCursor(0,0);
          lcd.print(lcdEvent);
          lcd.setCursor(0,1);
          lcd.print("...");
        }
      }
  //}
  inData = ""; // Clear recieved buffer
  delay(5000);
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Hello there");
   }
}
