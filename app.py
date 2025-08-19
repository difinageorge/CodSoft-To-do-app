import tkinter as tk
from tkinter import messagebox

# --- Theme Colors ---
day_theme = {
    "bg": "#f4f6f7",
    "fg": "#2c3e50",
    "entry_bg": "#ffffff",
    "task_done": "#27ae60",
    "task_not_done": "#c0392b",
    "button_colors": {
        "add": "#27ae60",
        "delete": "#e74c3c",
        "toggle": "#2980b9"
    }
}

night_theme = {
    "bg": "#2c3e50",
    "fg": "#ecf0f1",
    "entry_bg": "#34495e",
    "task_done": "#2ecc71",
    "task_not_done": "#e74c3c",
    "button_colors": {
        "add": "#2ecc71",
        "delete": "#e74c3c",
        "toggle": "#3498db"
    }
}

current_theme = day_theme

# --- Functions ---
def apply_theme():
    root.config(bg=current_theme["bg"])
    title.config(bg=current_theme["bg"], fg=current_theme["fg"])
    entry.config(bg=current_theme["entry_bg"], fg=current_theme["fg"], insertbackground=current_theme["fg"])
    button_frame.config(bg=current_theme["bg"])
    footer.config(bg=current_theme["bg"], fg=current_theme["fg"])
    theme_btn.config(bg=current_theme["button_colors"]["toggle"], fg="white")

    # Buttons
    add_btn.config(bg=current_theme["button_colors"]["add"])
    delete_btn.config(bg=current_theme["button_colors"]["delete"])
    toggle_btn.config(bg=current_theme["button_colors"]["toggle"])

    # Listbox
    listbox.config(bg=current_theme["entry_bg"], fg=current_theme["task_not_done"])

def toggle_theme():
    global current_theme
    current_theme = night_theme if current_theme == day_theme else day_theme
    theme_btn.config(text="🌞" if current_theme == day_theme else "🌙")
    apply_theme()

def add_task():
    task = entry.get().strip()
    if task != "":
        listbox.insert(tk.END, f"❌ {task}")
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("⚠️ Warning", "Task cannot be empty!")

def delete_task():
    try:
        index = listbox.curselection()[0]
        task = listbox.get(index)
        listbox.delete(index)
        messagebox.showinfo("🗑️ Deleted", f"Task removed: {task}")
    except:
        messagebox.showwarning("⚠️ Warning", "Please select a task to delete!")

def toggle_task(event=None):
    try:
        index = listbox.curselection()[0]
        task = listbox.get(index)
        
        if task.startswith("❌"):
            task_text = task[2:]
            listbox.delete(index)
            listbox.insert(index, f"✔️ {task_text}")
            listbox.itemconfig(index, fg=current_theme["task_done"])
        elif task.startswith("✔️"):
            task_text = task[2:]
            listbox.delete(index)
            listbox.insert(index, f"❌ {task_text}")
            listbox.itemconfig(index, fg=current_theme["task_not_done"])
    except:
        pass

# --- GUI Setup ---
root = tk.Tk()
root.title("✨ To-Do List")
root.geometry("450x550")

# Title
title = tk.Label(root, text="📌 My To-Do List", font=("Segoe UI", 18, "bold"))
title.pack(pady=15)

# Entry
entry = tk.Entry(root, width=28, font=("Segoe UI", 14), bd=2, relief="solid")
entry.pack(pady=10, ipady=6)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

style = {"font": ("Segoe UI", 10, "bold"), "relief": "flat", "width": 12, "height": 2, "bd": 0}

add_btn = tk.Button(button_frame, text="➕ Add", fg="white", **style, command=add_task)
delete_btn = tk.Button(button_frame, text="🗑️ Delete", fg="white", **style, command=delete_task)
toggle_btn = tk.Button(button_frame, text="🔄 Toggle", fg="white", **style, command=toggle_task)

add_btn.grid(row=0, column=0, padx=5)
delete_btn.grid(row=0, column=1, padx=5)
toggle_btn.grid(row=0, column=2, padx=5)

# Task List
listbox = tk.Listbox(root, width=40, height=15, font=("Segoe UI", 12), bd=0, highlightthickness=0, selectmode=tk.SINGLE, activestyle="none")
listbox.pack(pady=15)
listbox.bind("<Double-1>", toggle_task)

# Footer + Theme Toggle
footer_frame = tk.Frame(root)
footer_frame.pack(pady=10)

footer = tk.Label(footer_frame, text="💡 Tip: Double-click a task to toggle status", font=("Segoe UI", 9))
footer.grid(row=0, column=0, padx=10)

theme_btn = tk.Button(footer_frame, text="🌙", font=("Segoe UI", 12), width=4, command=toggle_theme)
theme_btn.grid(row=0, column=1)

# Apply initial theme
apply_theme()

root.mainloop()
