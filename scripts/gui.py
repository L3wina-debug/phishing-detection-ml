"""Tkinter interface: enter the 30 website features and get a prediction.

Each feature uses the UCI encoding: 1 = legitimate, 0 = suspicious, -1 = phishing.
"""
import tkinter as tk
from tkinter import messagebox, ttk

from predict_phishing import feature_names, predict_phishing

VALUES = ("1", "0", "-1")


def main() -> None:
    root = tk.Tk()
    root.title("Phishing website detection")

    frame = ttk.Frame(root, padding=12)
    frame.grid()
    ttk.Label(frame, text="1 = legitimate · 0 = suspicious · -1 = phishing").grid(
        row=0, column=0, columnspan=4, pady=(0, 8)
    )

    inputs = {}
    for index, name in enumerate(feature_names()):
        row, col = divmod(index, 2)
        ttk.Label(frame, text=name).grid(row=row + 1, column=col * 2, sticky="w", padx=4, pady=2)
        box = ttk.Combobox(frame, values=VALUES, width=4, state="readonly")
        box.set("1")
        box.grid(row=row + 1, column=col * 2 + 1, padx=4, pady=2)
        inputs[name] = box

    def on_predict() -> None:
        try:
            features = {name: int(box.get()) for name, box in inputs.items()}
            messagebox.showinfo("Prediction", f"This website is: {predict_phishing(features)}")
        except Exception as error:  # show any loading/prediction error to the user
            messagebox.showerror("Error", str(error))

    ttk.Button(frame, text="Predict", command=on_predict).grid(
        row=len(inputs) // 2 + 2, column=0, columnspan=4, pady=10
    )
    root.mainloop()


if __name__ == "__main__":
    main()
