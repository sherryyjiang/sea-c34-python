def safe_input():
    try:
        hello = raw_input("hello")
    except EOFError:
        return "None"
    except KeyboardInterrupt:
        return "None"
    return hello
while True:
    data = safe_input()
    if data == "Q":
        break
        