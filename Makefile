CC = g++
CFLAGS = -std=c++17 -Icustomlib/include -Isrc/generated
SRC_DIR = src
GEN_DIR = src/generated
CUSTOMLIB = customlib

SRCS = $(wildcard $(SRC_DIR)/*.cpp) \
       $(wildcard $(GEN_DIR)/*.cpp)

OBJS = $(SRCS:.cpp=.o)
TARGET = app

.PHONY: all clean autogen

all: autogen $(TARGET)

# -----------------------------
# Build-time code generation
# -----------------------------
autogen:
	@echo ">>> CustomLib: Generating missing commands/functions"
	@mkdir -p $(GEN_DIR)
	@python $(CUSTOMLIB)/generators/command_generator.py $(SRC_DIR) $(GEN_DIR)
	@python $(CUSTOMLIB)/generators/function_generator.py $(SRC_DIR) $(GEN_DIR)

# -----------------------------
# Build
# -----------------------------
$(TARGET): $(OBJS)
	$(CC) $(OBJS) -o $(TARGET)

%.o: %.cpp
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(TARGET)
	rm -rf $(GEN_DIR)