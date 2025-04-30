import tkinter as tk
from tkinter import ttk
import pickle

# Load the saved model
with open(r'C:\Users\Elbostan\Desktop\diabeaes/diabetes_model.pkl', 'rb') as f:
    diabetes_model = pickle.load(f)

# Function to predict diabetes
def predict_diabetes():
    try:
        preg = int(entry_preg.get())
        glu = int(entry_glu.get())
        bp = int(entry_bp.get())
        skin = int(entry_skin.get())
        insulin = int(entry_insulin.get())
        bmi = float(entry_bmi.get())
        dpf = float(entry_dpf.get())
        age = int(entry_age.get())
        
        input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]
        prediction = diabetes_model.predict([input_list])
        
        if prediction[0] == 0:
            result_label.config(text="The person is not diabetic", foreground="green")
        else:
            result_label.config(text="The person is diabetic", foreground="red")
    except Exception as e:
        result_label.config(text=f"Error: {e}", foreground="orange")

# Create the main window
root = tk.Tk()
root.title("Diabetes Prediction")
root.geometry("450x500")
root.configure(bg="#e8f4f8")

# Use ttk for a modern look
style = ttk.Style(root)
style.theme_use("clam")

# Create the main frame
main_frame = ttk.Frame(root, padding="15 15 15 15", style="TFrame")
main_frame.pack(fill=tk.BOTH, expand=True)

# Helper function to create entry fields
def create_entry(parent, label_text, row):
    label = ttk.Label(parent, text=label_text, font=("Helvetica", 10, "bold"))
    label.grid(row=row, column=0, sticky=tk.W, pady=5)
    entry = ttk.Entry(parent, width=30, font=("Helvetica", 10))
    entry.grid(row=row, column=1, pady=5)
    return entry

# Create input fields
entry_preg = create_entry(main_frame, "Number of Pregnancies:", 0)
entry_glu = create_entry(main_frame, "Glucose Level:", 1)
entry_bp = create_entry(main_frame, "Blood Pressure:", 2)
entry_skin = create_entry(main_frame, "Skin Thickness:", 3)
entry_insulin = create_entry(main_frame, "Insulin Level:", 4)
entry_bmi = create_entry(main_frame, "BMI:", 5)
entry_dpf = create_entry(main_frame, "Diabetes Pedigree Function:", 6)
entry_age = create_entry(main_frame, "Age:", 7)

# Create Predict button
predict_button = ttk.Button(main_frame, text="Predict", command=predict_diabetes, style="TButton")
predict_button.grid(row=8, column=0, columnspan=2, pady=15)

# Create result label
result_label = ttk.Label(main_frame, text="Result will be displayed here", font=("Helvetica", 12, "bold"))
result_label.grid(row=9, column=0, columnspan=2, pady=10)

# Add padding and spacing for better aesthetics
style.configure("TFrame", background="#e8f4f8")
style.configure("TButton", font=("Helvetica", 10, "bold"), padding=5)
style.configure("TLabel", background="#e8f4f8", font=("Helvetica", 10))

root.mainloop()
