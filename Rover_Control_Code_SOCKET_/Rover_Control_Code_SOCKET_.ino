
// Starting of Program

int m1a = 26;
int m1b= 28;
int m2a = 30;
int m2b = 32;
int acc1_f=10;
int acc1_b=11;
int acc2_f=8;
int acc2_b=9;
int acc3_f=6;
int acc3_b=7;
int claw_f=3;
int claw_b=2;
int wrist_f=4;
int wrist_b=5;
int ext_f=12;
int ext_b=13;
int fpv1=23;
int fpv2=25;
int base_f=12;
int base_b=13;
char val;

void setup() 
{  
pinMode(m1a, OUTPUT);  // Digital pin 10 set as output Pin
pinMode(m2b, OUTPUT);  // Digital pin 11 set as output Pin
pinMode(m2a, OUTPUT);  // Digital pin 12 set as output Pin
pinMode(m1b, OUTPUT);  // Digital pin 13 set as output Pin
pinMode(acc1_f, OUTPUT);
pinMode(acc1_b, OUTPUT);
pinMode(acc2_f, OUTPUT);
pinMode(acc2_b, OUTPUT);
pinMode(acc3_f, OUTPUT);
pinMode(acc3_b, OUTPUT);
pinMode(claw_f, OUTPUT);
pinMode(claw_b, OUTPUT);
pinMode(wrist_f, OUTPUT);
pinMode(wrist_b, OUTPUT);
pinMode(ext_f, OUTPUT);
pinMode(ext_b, OUTPUT);
pinMode(fpv1, OUTPUT);
pinMode(fpv2, OUTPUT);
pinMode(base_f, OUTPUT);
pinMode(base_b, OUTPUT);
Serial.begin(9600);
}

void loop()
{
  while (Serial.available() > 0)
  {
  val = Serial.read();
  Serial.print(val);

  if( val == 'w') // Forward
    {
      digitalWrite(m1a, HIGH);
      digitalWrite(m1b, LOW);
      digitalWrite(m2a, HIGH);
      digitalWrite(m2b, LOW);  
    }
  else if(val == 's') // Backward
    {
      digitalWrite(m1a, LOW);
      digitalWrite(m1b, HIGH);
      digitalWrite(m2a, LOW);
      digitalWrite(m2b, HIGH); 
    }
  
    else if(val == 'a') //Left
    {
    digitalWrite(m1a, LOW);
    digitalWrite(m1b, HIGH);
    digitalWrite(m2a, HIGH);
    digitalWrite(m2b, LOW);
    }
    else if(val == 'd') //Right
    {
    digitalWrite(m1a, HIGH);
    digitalWrite(m1b, LOW);
    digitalWrite(m2a, LOW);
    digitalWrite(m2b, HIGH); 
    }
    
  else if(val == '-') //Disconnect
    {
    digitalWrite(m1a, LOW);
    digitalWrite(m1b, LOW);
    digitalWrite(m2a, LOW);
    digitalWrite(m2b, LOW); 
    }
  else if(val == 'e') //Forward Right
    {
    digitalWrite(m1a, HIGH);
    digitalWrite(m1b, LOW);
    digitalWrite(m2a, LOW);
    digitalWrite(m2b, LOW);
    }
  else if(val == 'c') //Backward Right
    {
    digitalWrite(m1a, LOW);
    digitalWrite(m1b, HIGH);
    digitalWrite(m2a, LOW);
    digitalWrite(m2b, LOW);
    }
   else if(val == 'q') //Forward Left
    {
    digitalWrite(m1a, LOW);
    digitalWrite(m1b, LOW);
    digitalWrite(m2a, HIGH);     
    digitalWrite(m2b, LOW);
    }
  else if(val == 'z') //Backward Left
    {
    digitalWrite(m1a, LOW);
    digitalWrite(m1b, LOW);
    digitalWrite(m2a, LOW);
    digitalWrite(m2b, HIGH); 
    }
   else if(val=='x')
   {
    digitalWrite(m1a, LOW);
    digitalWrite(m1b, LOW);
    digitalWrite(m2a, LOW);
    digitalWrite(m2b, LOW); 
   }
   else if(val=='r')
   {
      digitalWrite(acc1_f,LOW);
      digitalWrite(acc1_b,HIGH);
   }
   else if(val=='f')
   {
    digitalWrite(acc1_f,HIGH);
    digitalWrite(acc1_b,LOW);
   }
   //acctu2 open
   else if(val=='t')
   {
    digitalWrite(acc2_f,LOW);
    digitalWrite(acc2_b,HIGH);
   }
   //acc2 close
   else if (val=='g')
   {
    digitalWrite(acc2_f,HIGH);
    digitalWrite(acc2_b,LOW);
    
   }
   //acc3 open
   else if(val=='y')
   {

    digitalWrite(acc3_f,LOW);
    digitalWrite(acc3_b,HIGH);
   }
   //acc3 close
   else if(val=='h')
   {
    digitalWrite(acc3_f,HIGH);
    digitalWrite(acc3_b,LOW);
   }
   //wrist clockwise
   else if(val=='u')
   {
    digitalWrite(wrist_f,LOW);
    digitalWrite(wrist_b,HIGH);
    
   }
   else if(val=='j')
   {
    digitalWrite(wrist_f,HIGH);
    digitalWrite(wrist_b,LOW);
   }
   //claw open
   else if(val=='o')
   {
    digitalWrite(claw_f,LOW);
    digitalWrite(claw_b,HIGH);
   }
   //claw close
   else if(val=='p')
   {
    digitalWrite(claw_f,HIGH);
    digitalWrite(claw_b,LOW);
    
   }
   //base clockwise
   else if(val=='i')
   {
    digitalWrite(base_f,LOW);
    digitalWrite(base_b,HIGH);

   }
   //base anticlockwise
   else if(val=='k')
   {
    digitalWrite(base_f,HIGH);
    digitalWrite(base_b,LOW);
   }
   //acc stop
   else if(val=='b')
   {
    digitalWrite(acc1_f,HIGH);
    digitalWrite(acc1_b,HIGH);
  
    digitalWrite(acc2_f,HIGH);
    digitalWrite(acc2_b,HIGH);
  
    digitalWrite(acc3_f,HIGH);
    digitalWrite(acc3_b,HIGH);
    
   }
   //base stop
   else if(val=='n')
   {
    digitalWrite(base_f,HIGH);
    digitalWrite(base_b,HIGH);
    
   }
   //cw stop
   else if(val=='m')
   {
    digitalWrite(claw_f,HIGH);
    digitalWrite(claw_b,HIGH);
    
    digitalWrite(wrist_f,HIGH);
    digitalWrite(wrist_b,HIGH);
    
    digitalWrite(base_f,HIGH);
    digitalWrite(base_b,HIGH);
   }
 
}
}
