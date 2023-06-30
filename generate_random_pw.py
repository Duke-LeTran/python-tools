def generate_pw(length):
    """https://stackoverflow.com/a/23012224/9335288"""
    if not isinstance(length, int) or length < 8:
        raise ValueError("temp password must have positive length")
    chars = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    return "".join(chars[c % len(chars)] for c in os.urandom(length))