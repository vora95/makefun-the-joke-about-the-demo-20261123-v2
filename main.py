import os

JOKE = "I asked my agent why the demo crashed and it said, with total confidence, 'The bug is in the part of the code I didn't write.'"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
