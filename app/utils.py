from app.errors import (
    EmptyInputListError,
    UnequalLengthError,
    UnknownDepartmentError,
    InvalidDeleteFlagError,
)
import tkinter as tk


# --- Helper function to check if input lists have equal lengths ---
def validate_equal_lengths(**lists):
    lengths = {name: len(lst) for name, lst in lists.items()}
    unique_lengths = set(lengths.values())

    if len(unique_lengths) > 1:
        length_info = ", ".join([f"{k}={v}" for k, v in lengths.items()])
        raise UnequalLengthError(f"Length mismatch: {length_info}")


# --- Helper function for required input validation ---
def require_non_empty(parsed_list, label):
    if not parsed_list:
        raise EmptyInputListError(label)
    return parsed_list


# --- Helper function for department validation ---
def validate_departments(raw_list, mapped_list):
    for raw, mapped in zip(raw_list, mapped_list):
        if mapped is None:
            raise UnknownDepartmentError(raw)


# --- Helper function for delete flag validation ---
def validate_delete_flags(delete_list):
    for flag in delete_list:
        if flag not in ("Y", "N"):
            raise InvalidDeleteFlagError(flag)


# --- Helper function for input parsing drop empty entries ---
def parse_input(input_str, to_upper=False):
    raw_entries = [s.strip() for s in input_str.split(",")]
    entries = [s for s in raw_entries if s]
    return [s.upper() if to_upper else s.title() for s in entries]


# --- Helper function for input parsing with empty entries preserved ---
def parse_input_allow_empty(input_str, to_upper=False):
    """Parse input and preserve position (even for empty entries)."""
    entries = [s.strip() for s in input_str.split(",")]
    return [s.upper() if to_upper else s.title() for s in entries]


# --- Helper function for clearing all fields in GUI---
def clear_fields(entries, output_box, minit_required_var, minit_entry):
    for entry in entries:
        entry.delete(0, tk.END)
    output_box.delete("1.0", tk.END)
    minit_required_var.set("N")
    minit_entry.config(state="disabled")


# --- Helper function for displaying README in GUI---
def show_readme_popup(readme_path, root):
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    popup = tk.Toplevel(root)
    popup.title("User Guide")
    popup.geometry("600x700")

    text_area = tk.Text(popup, wrap="word")
    text_area.insert(tk.END, content)
    text_area.config(state="disabled")
    text_area.pack(expand=True, fill=tk.BOTH)

    scrollbar = tk.Scrollbar(popup, command=text_area.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_area.config(yscrollcommand=scrollbar.set)
