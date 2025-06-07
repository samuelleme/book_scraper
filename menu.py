def display_menu():
    print("""
    +==================================+
    |             Welcome!             |
    +==================================+
    """)
    print("1 - List books")
    print("2 - List users")
    print("3 - List active loans")
    print("4 - List closed loans")
    print("5 - Register user")
    print("6 - Delete user")
    print("7 - Create loan")
    print("8 - Create return")
    print("0 - Exit")
    option = input("\nEnter the desired option: ").strip()
    return option