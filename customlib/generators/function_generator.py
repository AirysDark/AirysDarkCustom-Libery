void motor_start(int speed) {
    FunctionRegistry::invoke("motor.start", speed);
}