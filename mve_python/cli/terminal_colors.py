"""
python3 ./terminal_colors.py
"""

def color(num, text):
    """
    fn docstring
    """
    return f"\033[38;5;{num}m{text}\033[0m"

for i in range(16):
    print(color(i, f"number {i:02}"))