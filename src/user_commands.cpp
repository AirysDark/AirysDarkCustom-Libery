#include <Arduino.h>
#include "registry.h"

// --------------------------------------------------
// User-defined command logic
// --------------------------------------------------

static void alarm_arm_logic() {
    Serial.println("[USER] Alarm armed");
}

static void alarm_disarm_logic() {
    Serial.println("[USER] Alarm disarmed");
}

// --------------------------------------------------
// User-defined function logic
// --------------------------------------------------

static void motor_start_logic(int speed) {
    Serial.print("[USER] Motor starting at speed: ");
    Serial.println(speed);
}

static void motor_stop_logic() {
    Serial.println("[USER] Motor stopped");
}

// --------------------------------------------------
// Registration (runs before use)
// --------------------------------------------------

__attribute__((constructor))
static void register_user_logic() {
    CommandRegistry::register_cmd("alarm.arm", alarm_arm_logic);
    CommandRegistry::register_cmd("alarm.disarm", alarm_disarm_logic);

    FunctionRegistry::register_fn("motor.start", motor_start_logic);
    FunctionRegistry::register_fn("motor.stop", motor_stop_logic);
}