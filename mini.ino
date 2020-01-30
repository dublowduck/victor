#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#define BACKLIGHT_PIN     13
LiquidCrystal_I2C lcd( 0x27, 2 , 1 , 0 , 4 , 5 , 6 , 7 , 3 , POSITIVE );

String event = "0"; // sets the event variable to the default 0

void setup()
{
  lcd.begin(16,2); // initialize the lcd
  lcd.setBacklight(HIGH); // turns the backlight on
  lcd.setCursor(1,0);
  lcd.print("Good afternoon");
  lcd.setCursor(1,1);
  lcd.print("I`m Victor");
}


void loop()
{
  if (event !="0") {
    lcd.print(event);
  }
}
