import os

# One fixed joke string: the program is fully deterministic (no random,
# time, or network input), so every run writes the same bytes.
JOKE = "I asked my agent why the demo crashed and it said, with total confidence, 'The bug is in the part of the code I didn't write.'"


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


def main():
    write_entry()


if __name__ == "__main__":
    main()
