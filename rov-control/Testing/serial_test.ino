String inputString = "";
boolean stringComplete = false;

void setup(){
  Serial.begin(9600);
  inputString.reserve(200);
}

void loop (){
  if(stringComplete){
    Serial.println(inputString);
    inputString = "";
    stringComplete = false;
  }
}

void serialEvent(){
  while(Serial.available()>0){
    char inChar= (char) Serial.read();
    if (inChar == '\r' || inChar == '\n'){
      stringComplete = true; 
    }
    else{
      inputString += inChar;
    }
//    if(inChar ==  '\n'){
//       stringComplete = true;
//    }
  }
}
