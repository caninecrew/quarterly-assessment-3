import tkinter as tk
from tkinter import ttk, messagebox, font
from database import Database

class AdminInterface:
    def __init__(self, root):
        self.root = root
        self.db = Database()
