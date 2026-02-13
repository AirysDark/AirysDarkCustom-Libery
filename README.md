? AirysDarkCustom-Libery
AirysDarkCustom-Libery is a build-time code-generation library that allows developers to declare commands, functions, and extensions without implementing them upfront ? while still compiling cleanly.
Missing commands and functions are automatically generated at build time, routed through a registry system, and safely resolved at runtime.
This enables modular, extensible, plugin-style development without modifying core application code.
? Key Features
? Build-time code generation (no runtime hacks)
? Automatically generates missing commands & functions
? User-defined logic via registration (no core edits)
? Plugin system for default behavior & extensions
? Safe stubs prevent linker/runtime failures
? Works with PlatformIO, Make, ESP32, Arduino, and native builds
? Clean separation between declaration, generation, and logic
? Core Idea
Instead of writing functions directly, you declare intent:
Cpp
Copy code
COMMAND("alarm.arm")
FUNCTION("motor.start", "void(int speed)")
At build time, the library:
Scans the source tree
Detects declared commands/functions
Generates real C++ code
Routes calls through a registry
Optionally inserts safe default stubs
The compiler never sees missing symbols.
? Project Structure
Text
Copy code
project/
?? src/
?  ?? main.cpp
?  ?? user_commands.cpp
?  ?? generated/
?     ?? autogen_commands.cpp
?     ?? autogen_functions.cpp
?
?? customlib/
?  ?? include/
?  ?  ?? customlib.h
?  ?  ?? macros.h
?  ?  ?? registry.h
?  ?
?  ?? generators/
?  ?  ?? command_generator.py
?  ?  ?? function_generator.py
?  ?
?  ?? plugins/
?     ?? default_commands.py
?
?? platformio.ini
?? Makefile
? Basic Usage
1?? Declare Commands & Functions
Cpp
Copy code
#include "customlib.h"

COMMAND("alarm.arm")
COMMAND("alarm.disarm")

FUNCTION("motor.start", "void(int speed)")
FUNCTION("motor.stop", "void()")
These declarations do not generate code directly ? they are scanned at build time.
2?? Implement User Logic (Optional)
Cpp
Copy code
#include "registry.h"

static void alarm_arm_logic() {
    // user code
}

__attribute__((constructor))
static void register_logic() {
    CommandRegistry::register_cmd("alarm.arm", alarm_arm_logic);
}
If logic is not registered, safe default stubs are generated automatically.
3?? Build Normally
PlatformIO: pio run
Make: make
The generator runs before compilation, and the project always builds.
?? Build-Time Generation
AirysDarkCustom-Libery uses pre-build hooks:
PlatformIO ? extra_scripts = pre:customlib/build.py
Make ? autogen target
Generated files are placed in:
Text
Copy code
src/generated/
?? Do not edit generated files manually.
? Plugin System
The library supports generator plugins.
Example plugin behavior:
Provide default command/function stubs
Enforce strict mode (fail build on missing logic)
Add logging or diagnostics
Generate AI-assisted placeholder logic
Plugins live in:
Text
Copy code
customlib/plugins/
?? Safety Guarantees
No undefined references
No runtime crashes due to missing functions
No compiler hacks or reflection
Deterministic, reproducible builds
Embedded-safe (ESP32 / Arduino friendly)
? Why This Exists
AirysDarkCustom-Libery was built to solve problems such as:
Plugin systems without fragile linking
Modular firmware development
Game-engine-style command routing
Feature flags and optional logic
Large projects with evolving APIs
It enables clean growth without breaking builds.
? What This Is Not
? A runtime reflection system
? A scripting language
? A dynamic linker replacement
? Magic function interception
This is a professional, explicit, build-time solution.
? License
Specify your license here.
?? Roadmap (Optional)
[ ] Return-value support
[ ] Namespaced command generation
[ ] JSON-defined commands
[ ] Strict / debug modes
[ ] AI-generated logic stubs
[ ] Hot-reload for native builds
? Summary
AirysDarkCustom-Libery gives you:
Control
Safety
Extensibility
Clean architecture
Zero linker pain
If your project needs scalable behavior without fragile dependencies, this library is built for it.