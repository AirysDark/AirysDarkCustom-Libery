#pragma once

// --------------------------------------------------
// CustomLib declaration macros
// These macros DO NOT generate code directly.
// They exist only for the build-time generator.
// --------------------------------------------------

// Declare a command (no arguments)
#define COMMAND(name) \
    static const char* __customlib_cmd_##__LINE__ = name;

// Declare a function with a signature string
// Example:
// FUNCTION("motor.start", "void(int speed)")
#define FUNCTION(name, signature) \
    static const char* __customlib_fn_##__LINE__ = name; \
    static const char* __customlib_fn_sig_##__LINE__ = signature;

// Optional metadata (future use)
#define COMMAND_META(name, meta) \
    static const char* __customlib_cmd_meta_##__LINE__ = name "|" meta;

#define FUNCTION_META(name, signature, meta) \
    static const char* __customlib_fn_meta_##__LINE__ = name "|" signature "|" meta;

// --------------------------------------------------
// Safety: prevent accidental macro redefinition
// --------------------------------------------------
#ifdef COMMAND
#undef COMMAND
#endif

#ifdef FUNCTION
#undef FUNCTION
#endif