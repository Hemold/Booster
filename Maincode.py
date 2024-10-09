int PWM1 = 5
int DIR1 = 4
int PWM2 = 6
int DIR2 = 7

pinMode(DIR1, OUTPUT)
pinMode(DIR2, OUTPUT)


digitalWrite(DIR1,HIGH)
digitalWrite(DIR2, HIGH)
analogWrite(PWM1, ?)   #PWM Speed Control
analogWrite(PWM2, ?)   #PWM Speed Control