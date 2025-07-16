import tkinter as tk
from tkinter import ttk
import sys
import os

if getattr(sys, "frozen", False):
    base_path = sys._MEIPASS

else:
    base_path = os.path.dirname(os.path.abspath(__file__))

readme_path = os.path.join(base_path, "README.txt")

from app.logic import generate_xlsx
from app.errors import (
    UnequalLengthError,
    InvalidDeleteFlagError,
    UnknownDepartmentError,
    EmptyInputListError,
)
from app.utils import clear_fields, show_readme_popup


def main():

    # --- Color Theme ---
    BG_COLOR = "#f9f9fb"
    LABEL_COLOR = "#2c3e50"
    ENTRY_BG = "white"
    ENTRY_FG = "#2c3e50"
    HEADER_FONT = ("Helvetica", 16, "bold")
    LABEL_FONT = ("Helvetica", 12)

    # --- Root Window ---
    root = tk.Tk()
    root.title("3rd Element Generator")
    root.geometry("520x700")
    root.configure(bg=BG_COLOR)
    root.resizable(False, False)

    # --- ttk Style for Combobox ---
    style = ttk.Style()
    style.theme_use("default")  # use default theme for more styling flexibility
    style.configure(
        "TCombobox", fieldbackground=ENTRY_BG, background=ENTRY_BG, foreground=ENTRY_FG
    )

    # --- Header ---
    tk.Label(
        root,
        text="3rd Element Generator",
        font=HEADER_FONT,
        fg=LABEL_COLOR,
        bg=BG_COLOR,
    ).pack(pady=(10, 20))

    # --- Form Frame ---
    form_frame = tk.Frame(root, bg=BG_COLOR)
    form_frame.pack(padx=20, pady=10)

    # --- Department Field ---
    tk.Label(
        form_frame, text="Department(s):", font=LABEL_FONT, bg=BG_COLOR, fg=LABEL_COLOR
    ).grid(row=0, column=0, sticky="ne", pady=2)

    dept_info = """0 - Moonbase Ops
    1 - Galactic Wellness & Training"
    2 - Command Deck
    3 - Habitat Systems
    4 - Data Processing Core
    5 - Supply Bay
    6 - Quantum Prime
    7 - Repair Division
    8 - Ledger & Council"""

    tk.Label(
        form_frame,
        text=dept_info,
        justify="left",
        anchor="w",
        font=("Helvetica", 9),
        bg=BG_COLOR,
        fg="#555",
    ).grid(row=0, column=1, sticky="w", pady=2)

    dept_entry = tk.Entry(
        form_frame, width=40, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=ENTRY_FG
    )
    dept_entry.grid(row=1, column=1, sticky="w", pady=(0, 8))

    # --- Store Numbers ---
    tk.Label(
        form_frame, text="Sector #'s:", font=LABEL_FONT, bg=BG_COLOR, fg=LABEL_COLOR
    ).grid(row=2, column=0, sticky="e", pady=2)
    store_entry = tk.Entry(
        form_frame, width=40, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=ENTRY_FG
    )
    store_entry.grid(row=2, column=1, sticky="w", pady=2)

    # --- First Name ---
    tk.Label(
        form_frame, text="First Name(s):", font=LABEL_FONT, bg=BG_COLOR, fg=LABEL_COLOR
    ).grid(row=3, column=0, sticky="e", pady=2)
    fname_entry = tk.Entry(
        form_frame, width=40, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=ENTRY_FG
    )
    fname_entry.grid(row=3, column=1, sticky="w", pady=2)

    # --- Require Middle Initial? ---
    minit_required_var = tk.StringVar()
    tk.Label(
        form_frame,
        text="Require middle initial?",
        font=LABEL_FONT,
        bg=BG_COLOR,
        fg=LABEL_COLOR,
    ).grid(row=4, column=0, sticky="e", pady=2)
    minit_dropdown = ttk.Combobox(
        form_frame,
        textvariable=minit_required_var,
        values=["Y", "N"],
        state="readonly",
        width=5,
    )
    minit_dropdown.grid(row=4, column=1, sticky="w", pady=2)
    minit_dropdown.set("N")

    # --- Middle Initial(s) ---
    tk.Label(
        form_frame,
        text="Middle Initial(s):",
        font=LABEL_FONT,
        bg=BG_COLOR,
        fg=LABEL_COLOR,
    ).grid(row=5, column=0, sticky="e", pady=2)
    minit_entry = tk.Entry(
        form_frame,
        width=40,
        bg=ENTRY_BG,
        fg=ENTRY_FG,
        insertbackground=ENTRY_FG,
        state="disabled",
    )
    minit_entry.grid(row=5, column=1, sticky="w", pady=2)

    def toggle_minit_field(*args):
        if minit_required_var.get().strip().upper() == "Y":
            minit_entry.config(state="normal")
        else:
            minit_entry.delete(0, tk.END)
            minit_entry.config(state="disabled")

    minit_required_var.trace_add("write", toggle_minit_field)

    # --- Last Name ---
    tk.Label(
        form_frame, text="Last Name(s):", font=LABEL_FONT, bg=BG_COLOR, fg=LABEL_COLOR
    ).grid(row=6, column=0, sticky="e", pady=2)
    lname_entry = tk.Entry(
        form_frame, width=40, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=ENTRY_FG
    )
    lname_entry.grid(row=6, column=1, sticky="w", pady=2)

    # --- Third Element ---
    tk.Label(
        form_frame,
        text="Third Element(s ):",
        font=LABEL_FONT,
        bg=BG_COLOR,
        fg=LABEL_COLOR,
    ).grid(row=7, column=0, sticky="e", pady=2)
    thirdE_entry = tk.Entry(
        form_frame, width=40, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=ENTRY_FG
    )
    thirdE_entry.grid(row=7, column=1, sticky="w", pady=2)

    # --- Delete Flag ---
    tk.Label(
        form_frame,
        text="Delete Flag(s) (Y/N):",
        font=LABEL_FONT,
        bg=BG_COLOR,
        fg=LABEL_COLOR,
    ).grid(row=8, column=0, sticky="e", pady=2)
    delete_entry = tk.Entry(
        form_frame, width=40, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=ENTRY_FG
    )
    delete_entry.grid(row=8, column=1, sticky="w", pady=2)

    # --- Error Label ---
    error_label = tk.Message(
        root,
        text="",
        width=500,  # width in pixels for wrapping
        fg="red",
        bg=BG_COLOR,
        font=("Helvetica", 10, "bold"),
    )
    error_label.pack(pady=(5, 5), anchor="w")

    # --- Generate Button Logic---
    def generate():
        error_label.config(text="")

        dept_input_str = dept_entry.get()
        store_str = store_entry.get()
        fname_str = fname_entry.get()
        minit_required = minit_required_var.get()
        minit_str = minit_entry.get()
        lname_str = lname_entry.get()
        thirdE_str = thirdE_entry.get()
        delete_str = delete_entry.get()

        # Show preview in output box
        values = {
            "Department(s)": dept_input_str,
            "Sector #'s": store_str,
            "First Name(s)": fname_str,
            "Last Name(s)": lname_str,
            "Require Middle Initial": minit_required,
            "Middle Initials": minit_str,
            "Third Elements": thirdE_str,
            "Delete Flags": delete_str,
        }
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "--- Generated Values ---\n")
        for key, val in values.items():
            output_box.insert(tk.END, f"{key}: {val}\n")

        try:
            # Check if input is valid
            generate_xlsx(
                dept_input_str,
                store_str,
                fname_str,
                minit_required,
                minit_str,
                lname_str,
                thirdE_str,
                delete_str,
            )
            error_label.config(text=f"✓ File generated successfully!", fg="green")
            root.after(3000, lambda: error_label.config(text=""))
        except (
            UnequalLengthError,
            ValueError,
            UnknownDepartmentError,
            InvalidDeleteFlagError,
            EmptyInputListError,
        ) as e:
            error_label.config(text=f"❌ Error: {str(e)}", fg="red")

        except Exception as e:
            error_label.config(text=f"❌ Unexpected error: {str(e)}", fg="red")

    # --- Buttons Frame ---
    button_frame = tk.Frame(root, bg=BG_COLOR)
    button_frame.pack(pady=(0, 10))

    # --- Help Button ---
    ttk.Button(
        button_frame, text="Help", command=lambda: show_readme_popup(readme_path, root)
    ).grid(row=0, column=2, padx=10)

    ttk.Button(button_frame, text="Generate", command=generate).grid(
        row=0, column=0, padx=10
    )

    # --- Output Box ---
    output_box = tk.Text(root, height=10, width=65, bg="white", fg="#2c3e50")
    output_box.pack(pady=(0, 20))

    # --- Clear Button ---
    ttk.Button(
        button_frame,
        text="Clear",
        command=lambda: clear_fields(
            [
                dept_entry,
                store_entry,
                fname_entry,
                lname_entry,
                minit_entry,
                thirdE_entry,
                delete_entry,
            ],
            output_box,
            minit_required_var,
            minit_entry,
        ),
    ).grid(row=0, column=1, padx=10)

    # --- Mainloop ---
    root.mainloop()


if __name__ == "__main__":
    main()
