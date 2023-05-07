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

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

String msg;
void setup() {
   Serial.begin(9600);
   if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { // Address 0x3D for 128x64
    Serial.println(F("SSD1306 allocation failed"));
    for(;;);
  }
  delay(2000);
  display.clearDisplay();
}
void loop() {
  readSerialPort();
  if (msg != "") {
      sendData();
  }
  delay(500);
}
void readSerialPort() {
  msg = "";
  if (Serial.available()) {
      delay(10);
      while (Serial.available() > 0) {
          msg += (char)Serial.read();
      }
      Serial.flush();
  }
}
void sendData() {
  //write data
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.setCursor(0, 0);
  // Display static text
  display.println(msg);
  display.display();
  //Serial.print(msg);
}
