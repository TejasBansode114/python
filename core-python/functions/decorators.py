# --------- Decorators -------------
# Decorators --> A decorator is a function that wraps another function. It takes a function as input, adds new features to it, and returns it—all without touching the original code.


# 1. Define the decorator function. 'func' will be the function we wrap.
def my_decorator(func):
    # 2. Define the 'wrapper' function. This is the "envelope" around the original function.
    def wrapper():
        print("Something is happening before the function is called.")

        # 3. This line triggers the original function (say_hello)
        func()

        print("Something is happening after the function is called.")

    # 4. The decorator returns the wrapper, effectively replacing the original function.
    return wrapper


# 5. The '@' symbol tells Python: "Pass say_hello through my_decorator"
@my_decorator
def say_hello():
    print("Hello!")


# 6. When we call say_hello(), we are actually calling 'wrapper()'
say_hello()


# -----------------------LOGIN Decorator---------------------------------------
# 1. The Decorator (The Security Guard)
def login_required(func):
    # 2. The Wrapper (The Checkpoint)
    # It takes 'user' as an argument because the function it wraps (view_profile) needs it.
    def wrapper(user):
        # 3. Logic Check: Does the user have the right 'key'?
        if user.get("is_authenticated"):
            # 4. If True: Let them in! Run the original function.
            return func(user)
        else:
            # 5. If False: Block them and show a message.
            print("Please log in to access this function.")

    return wrapper


# 6. Apply the security check to the profile view
@login_required
def view_profile(user):
    print(f"Welcome to your profile, {user['name']}!")


# --- Execution ---

# Case A: Authenticated User
user1 = {"name": "Alice", "is_authenticated": True}
view_profile(user1)
# Result: "Welcome to your profile, Alice!"

# Case B: Unauthenticated User
user2 = {"name": "Stranger", "is_authenticated": False}
view_profile(user2)
# Result: "Please log in to access this function."
