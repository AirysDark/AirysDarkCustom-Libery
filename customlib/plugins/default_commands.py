"""
Default command and function handlers for CustomLib.

This plugin is used by the build-time generator to:
- Provide safe stub implementations
- Prevent linker/runtime failures
- Give visible placeholders for missing logic
"""

# --------------------------------------------------
# Command defaults
# --------------------------------------------------

def default_command_stub(command_name):
    """
    Generate a default C++ stub for a missing command.
    """
    fn_name = command_name.replace(".", "_")

    return f"""
static void __stub_{fn_name}() {{
    // Auto-generated default command stub
    // Command: {command_name}
}}

__attribute__((constructor))
static void __register_stub_{fn_name}() {{
    CommandRegistry::register_cmd("{command_name}", __stub_{fn_name});
}}
"""


# --------------------------------------------------
# Function defaults
# --------------------------------------------------

def default_function_stub(function_name, signature):
    """
    Generate a default C++ stub for a missing function.
    Signature is a string, e.g. "void(int speed)"
    """
    fn_name = function_name.replace(".", "_")

    # Extract return type and arguments
    ret_type = signature.split("(")[0].strip()
    args = signature.split("(")[1].split(")")[0].strip()

    args_decl = args if args else ""
    args_call = ", ".join(
        arg.strip().split(" ")[-1] for arg in args.split(",") if arg.strip()
    )

    return_stmt = ""
    if ret_type != "void":
        return_stmt = f"    return {ret_type}();"

    return f"""
static {ret_type} __stub_{fn_name}({args_decl}) {{
    // Auto-generated default function stub
    // Function: {function_name}
{return_stmt}
}}

__attribute__((constructor))
static void __register_stub_{fn_name}() {{
    FunctionRegistry::register_fn("{function_name}", __stub_{fn_name});
}}
"""


# --------------------------------------------------
# Plugin API (called by generator)
# --------------------------------------------------

def on_missing_command(command_name):
    """
    Called by the generator if a command has no user logic.
    """
    return default_command_stub(command_name)


def on_missing_function(function_name, signature):
    """
    Called by the generator if a function has no user logic.
    """
    return default_function_stub(function_name, signature)