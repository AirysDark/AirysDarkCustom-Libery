#include <Arduino.h>

#include "customlib.h"
#include "registry.h"

// --------------------------------------------------
// Declare commands & functions (build-time scanned)
// --------------------------------------------------

COMMAND("alarm.arm")
COMMAND("alarm.disarm")

FUNCTION("motor.start", "void(int speed)")
FUNCTION("motor.stop", "void()")

// --------------------------------------------------
// Arduino entry points
// --------------------------------------------------

void setup() {
    Serial.begin(115200);
    delay(500);

    Serial.println("System booting...");

    // Call generated commands/functions
    alarm_arm();
    motor_start(120);
}

void loop() {
    delay(1000);
}