def shift_letter(ch: str, shift: int) -> str: #Shift a single alphabet letter by `shift`. Preserves case.
    base = ord('A') if ch.isupper() else ord('a')
    return chr((ord(ch) - base + shift) % 26 + base)

def main():
    message = input("Enter the message: ").strip()
    if not message:
        print("Message cannot be empty.")
        return
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Shift must be an integer.")
        return

    mode = input("encrypt or decrypt? ").strip().lower()
    if mode not in ("encrypt", "decrypt"):
        print("Mode must be 'encrypt' or 'decrypt'.")
        return

    if mode == "decrypt":
        shift = -shift

    result = "".join(shift_letter(ch, shift) if ch.isalpha() else ch for ch in message)
    print("Result:", result)
if __name__ == "__main__":
    main()
