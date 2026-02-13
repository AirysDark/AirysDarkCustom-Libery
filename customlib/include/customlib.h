#pragma once

#define COMMAND(name) \
    static const char* __cmd_##__LINE__ = name;

#define FUNCTION(name, signature) \
    static const char* __fn_##__LINE__ = name;