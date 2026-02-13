def generate_commands(src_dir, out_file):
    commands = scan_for("COMMAND(", src_dir)

    with open(out_file, "w") as f:
        f.write("#include \"registry.h\"\n\n")

        for cmd in commands:
            fn = cmd.replace(".", "_")
            f.write(f"""
void {fn}() {{
    CommandRegistry::invoke("{cmd}");
}}
""")