
#include<Servo.h>

Servo servoVer; //Vertical Servo
Servo servoHor; //Horizontal Servo

int x;
int y;

float prevX;
float prevY;
void setup()
{
  Serial.begin(9600);
  servoVer.attach(5); //Attach Vertical Servo to Pin 5
  servoHor.attach(6); //Attach Horizontal Servo to Pin 6
  servoVer.write(90);
  servoHor.write(45);
}

void Pos()
{
  if(prevX != x || prevY != y)
  {
    int servoX = map(x, 600, 100, 0,90);
    int servoY = map(y, 450, 0, 90, 45);

    servoX = min(servoX, 90);
    servoX = max(servoX, 0);
    servoY = min(servoY, 90);
    servoY = max(servoY, 45);

    servoHor.write(servoX);
    servoVer.write(servoY);
  }
}

void loop()
{
  if(Serial.available() > 0)
  {
    if(Serial.read() == 'X')
    {
      x = Serial.parseInt();
      if(Serial.read() == 'Y')
      {
        y = Serial.parseInt();
       Pos();
      }
    }
    while(Serial.available() > 0)
    {
      Serial.read();
    }
  }
}
  
