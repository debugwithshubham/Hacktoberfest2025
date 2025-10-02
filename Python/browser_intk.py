# pip install tkhtmlview requests


import tkinter as tk
from tkinter import ttk
from tkhtmlview import HTMLLabel
import requests

class MiniBrowser(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mini Tkinter Browser")
        self.geometry("800x600")

        # URL bar
        self.url_var = tk.StringVar()
        url_entry = ttk.Entry(self, textvariable=self.url_var, width=80)
        url_entry.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        go_btn = ttk.Button(self, text="Go", command=self.load_page)
        go_btn.pack(side=tk.TOP, padx=5, pady=5)

        # Web page area
        self.html_label = HTMLLabel(self, html="<h3>Welcome to Mini Browser</h3>")
        self.html_label.pack(fill="both", expand=True)

    def load_page(self):
        url = self.url_var.get()
        if not url.startswith("http"):
            url = "http://" + url
        try:
            response = requests.get(url)
            self.html_label.set_html(response.text)
        except Exception as e:
            self.html_label.set_html(f"<h4 style='color:red;'>Error: {e}</h4>")

if __name__ == "__main__":
    app = MiniBrowser()
    app.mainloop()
