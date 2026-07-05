constexpr unsigned long SAMPLE_INTERVAL_US = 10000;
constexpr int ANALOG_PIN = A0;
constexpr int FAULT_BUTTON_PIN = 2;
constexpr float VREF = 5.0f;

unsigned long next_sample_us = 0;

void setup() {
  pinMode(FAULT_BUTTON_PIN, INPUT_PULLUP);
  Serial.begin(115200);
  next_sample_us = micros();
}

void loop() {
  const unsigned long now_us = micros();
  if ((long)(now_us - next_sample_us) < 0) {
    return;
  }

  next_sample_us += SAMPLE_INTERVAL_US;
  if ((long)(now_us - next_sample_us) >= 0) {
    next_sample_us = now_us + SAMPLE_INTERVAL_US;
  }

  const int adc_reading = analogRead(ANALOG_PIN);
  const float voltage = (static_cast<float>(adc_reading) * VREF) / 1023.0f;
  const bool fault_active = digitalRead(FAULT_BUTTON_PIN) == LOW;
  const char *fault_label = fault_active ? "fault" : "normal";

  Serial.print(millis());
  Serial.print(',');
  Serial.print(voltage, 3);
  Serial.print(',');
  Serial.println(fault_label);
}
