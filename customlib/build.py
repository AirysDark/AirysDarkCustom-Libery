Import("env")
import os
import shutil

print(">>> AirysDarkCustom-Libery: generator running")

OUT_DIR = ".pio/airysdarkcustomlib/generated"
FINAL_DIR = "src/generated"

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(FINAL_DIR, exist_ok=True)

# example proof file
with open(os.path.join(OUT_DIR, "GENERATOR_OK.txt"), "w") as f:
    f.write("Generator ran successfully\n")

# copy to src AFTER CMake
shutil.copy(
    os.path.join(OUT_DIR, "GENERATOR_OK.txt"),
    os.path.join(FINAL_DIR, "GENERATOR_OK.txt")
)

print(">>> CustomLib: output written and copied")