#include <Countimer.h>
#include <LiquidCrystal.h>


const int buttonPin = 2;  // the number of the pushbutton pin
const int ledPin = 3;    // the number of the LED pin
const int d4 = 4;
const int d5 = 5;
const int d6 = 6;
const int d7 = 7;
String incomingString = "";
String tophalf = "";
String bottomhalf = "";
String timestring = "";

Countimer timer;
LiquidCrystal lcd(8, 10, 9, d4, d5, d6, d7);
unsigned int starthours;
unsigned int endhours;
unsigned int startminutes;
unsigned int endminutes;
unsigned int hourdur;
unsigned int mindur;
 
int needhelp = 0;  // variable for reading the pushbutton status

void setup()
{
  Serial.begin(115200);
  Serial.setTimeout(1);
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  lcd.begin(16,2);
  while(!Serial);
  while(Serial.available() < 24);
  incomingString = Serial.readString();
  tophalf = incomingString.substring(0,16);
  lcd.print(tophalf);
  lcd.setCursor(1,1);
  timestring = incomingString.substring(17);
  starthours = timestring.substring(0,2).toInt();
  startminutes = timestring.substring(2,4).toInt();
  endhours = timestring.substring(4,6).toInt();
  endminutes = timestring.substring(6,8).toInt();

  hourdur = endhours - starthours;
  if (hourdur > 0 && endminutes < startminutes)
  {
    mindur = 60 - (startminutes-endminutes);
    hourdur--;
  }
  else 
  {
    mindur = endminutes - startminutes;
  }
  timer.setCounter(hourdur, mindur, 0, timer.COUNT_DOWN, onComplete);

  timer.setInterval(refreshClock, 1000);
}

void refreshClock() {
  lcd.setCursor(0,1);
  lcd.print(timer.getCurrentTime());
}
void onComplete() {
  lcd.println("TimesUp!!!");
}

void loop()
{
  // Run timer
  timer.run();

    // Now timer is running and listening for actions.
    // If you want to start the timer, you have to call start() method.
    if(!timer.isCounterCompleted()) {
      timer.start();
    }
  if (digitalRead(buttonPin)==HIGH)
  { // if button is pressed
    if (needhelp==0) 
    {             // and the status flag is LOW
      needhelp=1;                  // make status flag HIGH
      digitalWrite(ledPin,HIGH);     // and turn on the LED
      }
      else {                        // otherwise...
      needhelp=0;                  // make status flag LOW
      digitalWrite(ledPin,LOW);      // and turn off the LED
    }  
  }
}
