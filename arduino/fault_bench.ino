// Samples A0 at 100 Hz and streams ms,volts,label over serial. Button on D2 (to GND) flags a fault.

const int ANALOG_PIN = A0;
const int FAULT_BUTTON_PIN = 2;
const float VREF = 5.0;
const unsigned long SAMPLE_INTERVAL_US = 10000;

unsigned long next_sample_us;

void setup() {
  pinMode(FAULT_BUTTON_PIN, INPUT_PULLUP);
  Serial.begin(115200);
  next_sample_us = micros();
}

void loop() {
  unsigned long now_us = micros();
  if ((long)(now_us - next_sample_us) < 0) return;

  // a slow Serial write can blow a slot, resync instead of bursting to catch up
  next_sample_us += SAMPLE_INTERVAL_US;
  if ((long)(now_us - next_sample_us) >= 0) next_sample_us = now_us + SAMPLE_INTERVAL_US;

  int adc = analogRead(ANALOG_PIN);
  float v = adc * VREF / 1023.0;
  bool fault = digitalRead(FAULT_BUTTON_PIN) == LOW;

  Serial.print(millis());
  Serial.print(',');
  Serial.print(v, 3);
  Serial.print(',');
  Serial.println(fault ? "fault" : "normal");
}
