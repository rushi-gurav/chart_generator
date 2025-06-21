from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from fpdf import FPDF

def generate_chart():
	student_name = name_entry.get().strip()  

	if not student_name:
		messagebox.showerror("Error", "Student name is required!")
		return

	mark1 = mark1_entry.get()
	mark2 = mark2_entry.get()
	mark3 = mark3_entry.get()

	if not mark1 or not mark2 or not mark3:
		messagebox.showerror("Error", "All fields are required!")
		return

	try:
		physics = int(mark1)
		chemistry = int(mark2)
		maths = int(mark3)

		if any(m < 0 or m > 100 for m in [physics, chemistry, maths]):
			messagebox.showerror("Error", "Marks should be between 0-100!")
			return

		
		pdf_filename = f"{student_name}.pdf"

		subjects = ["Physics", "Chemistry", "Mathematics"]
		marks = [physics, chemistry, maths]

		
		plt.figure(figsize=(6, 4))
		plt.bar(subjects, marks, color=['blue', 'green', 'red'])
		plt.xlabel("Subjects")
		plt.ylabel("Marks")
		plt.title(f"Marks of {student_name}")
		plt.ylim(0, 100)
		plt.grid(axis='y', linestyle='', alpha=0.7)

		
		with PdfPages(pdf_filename) as pdf:
			pdf.savefig()  # Save the current figure to PDF
			plt.close()

		messagebox.showinfo("Success", f"Chart saved as '{pdf_filename}'!")

	except ValueError:
		messagebox.showerror("Error", "Please enter valid numeric values for marks!")

chart_window = Tk()
chart_window.title("Student Marks Chart Generator")


window_width = 500
window_height = 400
screen_width = chart_window.winfo_screenwidth()
screen_height = chart_window.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
chart_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

Label(chart_window, text="Student Name:", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10)
name_entry = Entry(chart_window, font=("Arial", 14))
name_entry.grid(row=0, column=1, padx=10, pady=10)

Label(chart_window, text="Physics Marks:", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=10)
mark1_entry = Entry(chart_window, font=("Arial", 14))
mark1_entry.grid(row=1, column=1, padx=10, pady=10)

Label(chart_window, text="Chemistry Marks:", font=("Arial", 14)).grid(row=2, column=0, padx=10, pady=10)
mark2_entry = Entry(chart_window, font=("Arial", 14))
mark2_entry.grid(row=2, column=1, padx=10, pady=10)

Label(chart_window, text="Mathematics Marks:", font=("Arial", 14)).grid(row=3, column=0, padx=10, pady=10)
mark3_entry = Entry(chart_window, font=("Arial", 14))
mark3_entry.grid(row=3, column=1, padx=10, pady=10)

Button(chart_window, text="Generate Chart", font=("Arial", 14), command=generate_chart).grid(row=4, column=0, columnspan=2, pady=20)
Button(chart_window, text="Exit", font=("Arial", 14), command=chart_window.quit).grid(row=5, column=0, columnspan=2, pady=10)

chart_window.mainloop()
