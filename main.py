"""The Wrong Box: an entry for the make.fun bounty "The Most Honest Outage Line".

The program writes the entry text - one line, 94 characters -
to entry.txt (94 characters, inside the 1-160 gate) in the output directory (MAKEFUN_OUTPUT_DIR locally, /output
in the grader). The text is a fixed constant with no trailing newline, so
both of the grader's runs write byte-identical output.
"""
import os

LINE = "We are down because someone typed the wrong thing into the wrong box, and that someone was me."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
