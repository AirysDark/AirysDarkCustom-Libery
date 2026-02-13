#pragma once
#include <map>
#include <functional>

class CommandRegistry {
public:
    static void register_cmd(const char* name, std::function<void()> fn);
    static void invoke(const char* name);
};

class FunctionRegistry {
public:
    template<typename Fn>
    static void register_fn(const char* name, Fn fn);
};