#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
// constants won't change. They're used here to set pin numbers:
const int startbutton = 6;     // the number of the startbutton pin
const int powerbutton =  7;      // the number of the powerbutton pin

  // variables will change:
int startbuttonState = 0;         // variable for reading the pushbutton status
// set up the LCD's number of columns and rows:

void setup() {
  // initialize the startbutton pin as an input:
  pinMode(startbutton, INPUT);
  // initialize the pushbutton pin as an input:
  pinMode(powerbutton, OUTPUT);

  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("LCD Check [PASS]");
}

void loop() {
  // read the state of the startbutton value:
  startbuttonState = digitalRead(startbutton);
// check if the startbutton is pressed. If it is, the startbuttonState is HIGH:
if (startbuttonState == HIGH) {
  digitalWrite(powerbutton,HIGH);
  delay(500);
  digitalWrite(powerbutton,LOW);
  lcd.print("Powering up");
  }

  if () {
    lcd.print("POST");
  }
  if () {
    lcd.print("Booting");
  }
}
