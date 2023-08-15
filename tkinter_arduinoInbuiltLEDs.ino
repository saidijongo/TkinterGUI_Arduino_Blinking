char command;

void setup() {
  Serial.begin(9600); 
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) { 
    command = Serial.read();
    
    if (command == '1') {                
      digitalWrite(LED_BUILTIN, HIGH); 
    }
    if (command == '0') {
      digitalWrite(LED_BUILTIN, LOW);         
    }
  }
}
