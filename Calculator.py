import tkinter as tk

# Create main window
window = tk.Tk()
window.title("Digital Calculator")
window.geometry("500x500")
window.resizable(False, False)
window.configure(bg="#0f0f0f")  # Dark background

# Entry (Display)
display = tk.Entry(window, font=("Courier New", 26, "bold"),
                   bd=0, bg="#1a1a1a", fg="#00ffff", justify='right',
                   insertbackground="#00ffff")  # Neon cyan
display.place(x=0, y=0, width=500, height=300)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Command for button clicks
def on_click(btn):
    if btn == "C":
        display.delete(0, tk.END)
    elif btn == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, btn)

# Define button colors
btn_bg = "#2e2e2e"
btn_fg = "#ffffff"
special_bg = "#007acc"  # Function button
equal_bg = "#00cc99"    # Equals button
hover_bg = "#3a3a3a"

# Create buttons
btn_font = ("Segoe UI", 18, "bold")
for i, row in enumerate(buttons):
    for j, char in enumerate(row):
        bg_color = btn_bg
        if char in ['+', '-', '*', '/']:
            bg_color = special_bg
        elif char == "=":
            bg_color = equal_bg
        elif char == "C":
            bg_color = "#cc3333"

        btn = tk.Button(window, text=char, font=btn_font,
                        bg=bg_color, fg=btn_fg, bd=0,
                        activebackground=hover_bg,
                        activeforeground="#00ffff",
                        command=lambda c=char: on_click(c))
        btn.place(x=125*j, y=60 + 110*i, width=125, height=110)

window.mainloop()
