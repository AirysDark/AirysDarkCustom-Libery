from generators.command_generator import generate_commands
from generators.function_generator import generate_functions

generate_commands("src/", "src/generated/autogen_commands.cpp")
generate_functions("src/", "src/generated/autogen_functions.cpp")