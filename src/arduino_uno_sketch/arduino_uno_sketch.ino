/*
:description:
	Sketch can be used for controlling Digital output of "Arduino UNO R3" using serial communication.
	
	Digital output	:	Digital Pin no 2 to 5. (By default all Digital output will be HIGH. Se below example for controlling Digital output)
	Not used		:	Pin No 1 and 2. Reserved for external serial communication.
	
	example 1:	To Turn ON Relay 1, send below command.
				      11
  example 2:  To Turn OFF Relay 1, send below command.
              10
	example 3:	To Turn ON  Relay 4, send below command string on serial port.
				      41  
  example 4:  To check status of relays (ON/OFF), send below command string on serial port.
              STATUS
	
	*Note:	Please save backup of this sketch before editing.
*/

#include <stdlib.h>

/*Digital outputStrings*/
#define DOUT2 2
#define DOUT3 3
#define DOUT4 4
#define DOUT5 5
  
/*Baudrate and variables used for serial comm*/
#define BAUDRATE 9600
String inputString = "00";
String outputString = "00000";

void setup()
{

  /* statements which will be executed when Board turned on first time*/
  /*Digital outputStrings configuration and default pin mode*/
  pinMode(DOUT2, OUTPUT);
  digitalWrite(DOUT2, HIGH);
  pinMode(DOUT3, OUTPUT);
  digitalWrite(DOUT3, HIGH);
  pinMode(DOUT4, OUTPUT);
  digitalWrite(DOUT4, HIGH);
  pinMode(DOUT5, OUTPUT);
  digitalWrite(DOUT5, HIGH);
  
  /*Begin serial communication with defined BAUDRATE*/
  Serial.begin(BAUDRATE);
  Serial.setTimeout(1);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }  
}

void loop()
{
  if(Serial.available() > 0)
  {
    inputString = Serial.readString();
    if(inputString.length() >= 2)
    {
      if(inputString == "10")
      {
        digitalWrite(DOUT2, HIGH);
      }
      else if(inputString == "11")
      {
        digitalWrite(DOUT2, LOW);
      }
      else if(inputString == "20")
      {
        digitalWrite(DOUT3, HIGH);
      }
      else if(inputString == "21")
      {
        digitalWrite(DOUT3, LOW);
      }
      else if(inputString == "30")
      {
        digitalWrite(DOUT4, HIGH);
      }
      else if(inputString == "31")
      {
        digitalWrite(DOUT4, LOW);
      }
      else if(inputString == "40")
      {
        digitalWrite(DOUT5, HIGH);
      }
      else if(inputString == "41")
      {
        digitalWrite(DOUT5, LOW);
      }
      else if(inputString == "F1")
      {
        digitalWrite(DOUT2, LOW);
        digitalWrite(DOUT3, LOW);
        digitalWrite(DOUT4, LOW);
        digitalWrite(DOUT5, LOW);
      }
      else if(inputString == "F0")
      {
        digitalWrite(DOUT2, HIGH);
        digitalWrite(DOUT3, HIGH);
        digitalWrite(DOUT4, HIGH);
        digitalWrite(DOUT5, HIGH);
      }
      else if(inputString == "STATUS")
      {
        outputString = "";
        outputString = outputString + "R1=" + !digitalRead(DOUT2) + ",R2=" + !digitalRead(DOUT3) + ",R3=" + !digitalRead(DOUT4) + ",R4=" + !digitalRead(DOUT5);
        Serial.println(outputString);
      }
    }
  }
  delay(50);
}
