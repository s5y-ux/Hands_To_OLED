/*
This is the C++ program that must be uploaded to the MicroController.
Included in this program are, "Functions, Input / Output readings, and Memory
allocation." This program utilizes specialized functions for MicroController
programming like setup and loop. It also uses advanced IO through utf-8
conversion in the serial monitor and output data through the analog pins.
*/

#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

//Sets up constants for the OLED deminsions
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

//Shortening Adafruit_SSD1306 library into display driver
typedef Adafruit_SSD1306 Display_Driver;

//instantiates Adafruit_SSD1306 object with respective parameters
Display_Driver display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

//Used as a varible in which the OLED will reference and display
String msg;

//Initalization on power-up
void setup() {

  //Opens up the serial monitor for transfers of up to 9600 bits per second
   Serial.begin(9600);

   //Logic check to see if the OLED was detected (address 0x3D for 128x64)
   if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {

     //If it fails, let the serial monitor know
    Serial.println(F("SSD1306 allocation failed"));

  }

  //wait 2 seconds
  delay(2000);

  //clear the data
  display.clearDisplay();
}

//After instantiation and OLED detection
void loop() {

  //Reads the data in the serial port and stores the data as "msg"
  readSerialPort();

  //Sees if the message isent blank
  if (msg != "") {

    //if its not then we will send the data to the OLED
      sendData();
  }

  //then we wait a half second before reciving more data
  delay(500);
}


//referenced in loop() function for interpreting data in serial monitor
void readSerialPort() {

  //allocates global string, "msg" and sets its value to an empty string
  msg = "";

  //Logic check on if data is avaliable on the searial monitor
  if (Serial.available()) {

    //if its so we will delay for 1/100th of a second
      delay(10);

      //and while the data is avaliable
      while (Serial.available() > 0) {

        //we will concatinate the character to the string
          msg += (char)Serial.read();
      }

      //and flush the data
      Serial.flush();
  }
}

//function used to actually display the message on the OLED
void sendData() {
  /*

  Clears OLED
  |
  v
  Sets Text Size
  |
  v
  Sets Text Color
  |
  v
  Sets Cursor Point
  |
  v
  Prints OLED_String
  |
  v
  Displays

  */
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.setCursor(0, 0);
  display.println(msg);
  display.display();
}
