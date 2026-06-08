from app.storage import load_resources, save_resources
from tkinter import ttk
import tkinter as tk

def refresh_treeview(tree):
    for item in tree.get_children():
        tree.delete(item)
    resources = load_resources()
    for resource in resources:
        tree.insert('', tk.END, values=(resource.get('title', 'N/A'), resource.get('subject', 'N/A'), resource.get('original_path', 'N/A')),iid=resource['id'])

def show_context_menu(event,tree,menu):
    row_id=tree.identify_row(event.y)
    if row_id:
        tree.selection_set(row_id)
        menu.post(event.x_root,event.y_root)