import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re

def connect_to_db():
    return mysql.connector.connect(
        host="localhost", 
        user="root", 
        password="headache", 
        database="tkinter"
    )

def is_valid_email(email):
    email_pattern = r"[^@]+@[^@]+\.[^@]+"
    return re.match(email_pattern, email) is not None

def is_valid_phone(phone):
    phone_pattern = r"^\d{10}$"
    return re.match(phone_pattern, phone) is not None

def send_confirmation_email(first_name, recipient_email):
    sender_email = "forbsubramani@gmail.com"
    sender_password = "wzel lytc qrxf kstj"
    subject = "Registration Confirmation"
    body = f"Thank you {first_name} for registering with us!"
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print(f"Confirmation email sent to {recipient_email}")
    except Exception as e:
        messagebox.showerror("Email Error", f"Failed to send confirmation email: {str(e)}")

def submit_data():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    gender = gender_var.get()
    dob = f"{dob_year_var.get()}-{dob_month_var.get()}-{dob_day_var.get()}"
    phone = entry_phone.get()
    email = entry_email.get()
    course = entry_course.get()

    if not first_name or not last_name or not phone or gender == "" or not email or not course:
        messagebox.showerror("Input Error", "Please fill all required fields!")
        return
    
    if not is_valid_email(email):
        messagebox.showerror("Input Error", "Please enter a valid email address!")
        return

    if not is_valid_phone(phone):
        messagebox.showerror("Input Error", "Phone number must be 10 digits!")
        return

    try:
        db = connect_to_db()
        cursor = db.cursor()
        
        insert_query = "INSERT INTO students (first_name, last_name, gender, dob, phone, email, course) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (first_name, last_name, gender, dob, phone, email, course))
        
        db.commit()
        messagebox.showinfo("Success", "Student data has been added successfully!")
        send_confirmation_email(first_name, email)
        clear_form()
    except Exception as e:
        messagebox.showerror("Database Error", f"An error occurred: {str(e)}")
    finally:
        db.close()

def clear_form():
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    gender_var.set(None)
    dob_day_var.set("")
    dob_month_var.set("")
    dob_year_var.set("")
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_course.delete(0, tk.END)

def cancel():
    root.quit()  

root = tk.Tk()
root.title("Student Registration")
root.state('zoomed')

#placeholder function
def set_placeholder(entry, placeholder_text):
    entry.insert(0, placeholder_text)
    entry.config(fg="grey")
    entry.bind("<FocusIn>", lambda event: clear_placeholder(event, placeholder_text))
    entry.bind("<FocusOut>", lambda event: restore_placeholder(event, placeholder_text))

def clear_placeholder(event, placeholder_text):
    entry = event.widget
    if entry.get() == placeholder_text:
        entry.delete(0, tk.END)
        entry.config(fg="black")

def restore_placeholder(event, placeholder_text):
    entry = event.widget
    if entry.get() == "":
        entry.insert(0, placeholder_text)
        entry.config(fg="#f6f6f6")

# Background image
background_image = Image.open("bg.png")
background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
bg_img = ImageTk.PhotoImage(background_image)

# Canvas to hold the background image
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack(fill="both", expand=True)

# Background img
canvas.create_image(0, 0, image=bg_img, anchor="nw")

# Title label
canvas.create_text(root.winfo_screenwidth() // 2, 50, text="Student Registration", font=("Arial", 24, "bold"), fill="#828080")

# Coordinates for the underline
underline_y = 80  
line_length = 200  
line_x_start = (root.winfo_screenwidth() - line_length) // 2
line_x_end = line_x_start + line_length
line_thickness = 2  

# Creating a straight underline line
canvas.create_line(line_x_start, underline_y, line_x_end, underline_y, fill="#828080", width=line_thickness)

# Creating small ovals at each end to simulate rounded corners
oval_radius = line_thickness * 2
canvas.create_oval(line_x_start - oval_radius, underline_y - oval_radius, line_x_start + oval_radius, underline_y + oval_radius, fill="black", outline="black")
canvas.create_oval(line_x_end - oval_radius, underline_y - oval_radius, line_x_end + oval_radius, underline_y + oval_radius, fill="black", outline="black")


# Frame for the form
form_frame = tk.Frame(root, bg="#d9f9d9", bd=5,highlightbackground="black", highlightthickness=2)
form_frame.pack_propagate(False)
form_frame_width = 500
form_frame_height = 350
form_frame.place(x=(root.winfo_screenwidth() - form_frame_width) // 2,
                 y=(root.winfo_screenheight() - form_frame_height) // 2, 
                 width=form_frame_width, height=form_frame_height)

spacer_label = tk.Label(form_frame, bg="#d9f9d9")  
spacer_label.grid(row=0, column=0, columnspan=4, pady=(10, 5))  




label_first_name = tk.Label(form_frame, text="First Name:", bg="#d9f9d9", font=("Arial", 10, "bold"))
label_first_name.grid(row=1, column=0, padx=10, pady=(15, 5), sticky="W")
entry_first_name = tk.Entry(form_frame)
entry_first_name.grid(row=1, column=1, padx=10, pady=(15, 5), sticky="W")

set_placeholder(entry_first_name, "Enter First Name")



label_last_name = tk.Label(form_frame, text="Last Name:", bg="#d9f9d9", font=("Arial", 10, "bold"))
label_last_name.grid(row=1, column=2, padx=10, pady=(15, 5), sticky="W")
entry_last_name = tk.Entry(form_frame)
entry_last_name.grid(row=1, column=3, padx=10, pady=(15, 5), sticky="W")

set_placeholder(entry_last_name, "Enter Last Name")




label_gender = tk.Label(form_frame, text="Gender:", bg="#d9f9d9", font=("Arial", 10, "bold"))
label_gender.grid(row=2, column=0, padx=10, pady=(5, 5), sticky="W")  
gender_var = tk.StringVar()
gender_frame = tk.Frame(form_frame, bg="#d9f9d9")
gender_frame.grid(row=2, column=1, columnspan=3, padx=10, pady=(5, 5), sticky="W")
tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", bg="#d9f9d9").pack(side=tk.LEFT)
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", bg="#d9f9d9").pack(side=tk.LEFT)
tk.Radiobutton(gender_frame, text="Trans", variable=gender_var, value="Trans", bg="#d9f9d9").pack(side=tk.LEFT)

label_dob = tk.Label(form_frame, text="Date of Birth:", bg="#d9f9d9", font=("Arial", 10, "bold"))
label_dob.grid(row=3, column=0, padx=10, pady=(5, 5), sticky="W")

dob_frame = tk.Frame(form_frame, bg="#d9f9d9")
dob_frame.grid(row=3, column=1, columnspan=3, padx=10, pady=(5, 5), sticky="W")

dob_day_var = tk.StringVar()
dob_month_var = tk.StringVar()
dob_year_var = tk.StringVar()

dob_day = ttk.Combobox(dob_frame, textvariable=dob_day_var, width=5, values=[str(i) for i in range(1, 32)])
dob_day.pack(side=tk.LEFT)  
dob_month = ttk.Combobox(dob_frame, textvariable=dob_month_var, width=5, values=[str(i) for i in range(1, 13)])
dob_month.pack(side=tk.LEFT)  
dob_year = ttk.Combobox(dob_frame, textvariable=dob_year_var, width=7, values=[str(i) for i in range(1950, 2024)])
dob_year.pack(side=tk.LEFT)  



label_phone = tk.Label(form_frame, text="Phone:", bg="#d9f9d9", font=("Arial", 10, "bold"))
label_phone.grid(row=4, column=0, padx=10, pady=(5, 5), sticky="W")
entry_phone = tk.Entry(form_frame)
entry_phone.grid(row=4, column=1, padx=10, pady=(5, 5), columnspan=3, sticky="W")

set_placeholder(entry_phone, "Enter Phone Number")




label_email = tk.Label(form_frame, text="Email:", bg="#d9f9d9", font=("Arial", 10, "bold"))
label_email.grid(row=5, column=0, padx=10, pady=(5, 5), sticky="W")
entry_email = tk.Entry(form_frame)
entry_email.grid(row=5, column=1, padx=10, pady=(5, 5), columnspan=3, sticky="W")

set_placeholder(entry_email, "Enter Email Address")



label_course = tk.Label(form_frame, text="Course:", bg="#d9f9d9", font=("Arial", 10, "bold"))
label_course.grid(row=6, column=0, padx=10, pady=(5, 5), sticky="W")
entry_course = tk.Entry(form_frame)
entry_course.grid(row=6, column=1, padx=10, pady=(5, 5), columnspan=3, sticky="W")

set_placeholder(entry_course, "Enter Course Name")

# Submit, Clear, and Cancel buttons
button_frame = tk.Frame(form_frame, bg="#d9f9d9")
button_frame.grid(row=7, column=0, columnspan=4, pady=(50, 10))

submit_button = tk.Button(button_frame, text="Submit", command=submit_data, bg="green", fg="white")
submit_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_form, bg="orange", fg="black")
clear_button.pack(side=tk.LEFT, padx=10)

cancel_button = tk.Button(button_frame, text="Cancel", command=cancel, bg="red", fg="white")
cancel_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
