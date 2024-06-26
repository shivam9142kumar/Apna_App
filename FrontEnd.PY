# Import necessary modules
import tkinter as tk
from tkinter import messagebox

#BackEnd code for the project
import mysql.connector

# Configuring 
config = {
    'user': 'root',
    'password': 'yash@7940',
    'host': '127.0.0.1',
    'database': 'apna'
}

def connect_to_database(config):
    try:
        con = mysql.connector.connect(**config)
        if con.is_connected():

            print("Connection successful")
            cur = con.cursor()

            return con
    except mysql.connector.Error as err:

        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR: # type: ignore
            print("Something is wrong with your user name or password")

        elif err.errno == errorcode.ER_BAD_DB_ERROR: # type: ignore
            print("Database does not exist")


        else:

            print(err)
    return None

con = connect_to_database(config)
if con:
    cur = con.cursor()


#Defining the function for fetching the Details of User in the Database from the email_id attribute
def userInfo(Email_id):
    try:
        cur.execute("SELECT * FROM user WHERE Email_id = %s", (Email_id,))
        value = cur.fetchone()
        con.commit()
        con.close()
        return value
    except mysql.connector.Error as err:
        print(f"Error: {err}")

#Defining the function for adding the Details of User in the Database
def addData(Name, Email_id, Skills, Phone_no, Degree, Password):
    try:
        cur.execute("INSERT INTO User (Name, Email_id, Skills, Phone_no, Degree, Password) VALUES (%s, %s, %s, %s, %s, %s)",
                    (Name, Email_id, Skills, Phone_no, Degree, Password))
        con.commit()
        con.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")


#Defining the function for Viewing the Details of User in the Database
def viewData():
    try:
        cur.execute("SELECT * FROM User")
        user_val = cur.fetchall()
        con.commit()
        con.close()
        return user_val
    except mysql.connector.Error as err:
        print(f"Error: {err}")



# Base class for all pages in the application
class PageBase:
    def __init__(self, master, bg_color='#ffffff'): 
        self.master = master
        self.bg_color = bg_color  # Store the background color for this page
        self.__frame = tk.Frame(master, bg=self.bg_color)
        self.__frame.pack(pady=20, padx=20, fill='both', expand=True)

    def pack(self):
        self.__frame.pack()

    def destroy(self):
        self.__frame.destroy()

    def go_back(self):
        if self.master._history:
            previous_page = self.master._history.pop()  # Remove the last page from history
            self.destroy()  # Destroy the current page
            previous_page.pack()  # Display the previous page

# Custom styled button class with rounded corners and hover effects
class CustomButton(tk.Canvas):
    def __init__(self, master, text, command, bg='#007bff', fg='#ffffff', width=200, height=40, hover_bg=None):
        super().__init__(master, width=width, height=height, bd=0, highlightthickness=0)
        self.command = command
        self.default_bg = bg
        self.bg = bg
        self.fg = fg
        self.text = text
        self.width = width
        self.height = height
        self.hover_bg = hover_bg or self.bg

        self.create_rounded_button()
        self.bind("<Button-1>", self.on_click)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def create_rounded_button(self):
        self.delete("all")
        radius = 20
        self.create_arc((0, 0, radius, radius), start=90, extent=90, fill=self.bg, outline=self.bg)
        self.create_arc((self.width-radius, 0, self.width, radius), start=0, extent=90, fill=self.bg, outline=self.bg)
        self.create_arc((self.width-radius, self.height-radius, self.width, self.height), start=270, extent=90, fill=self.bg, outline=self.bg)
        self.create_arc((0, self.height-radius, radius, self.height), start=180, extent=90, fill=self.bg, outline=self.bg)
        self.create_rectangle((radius/2, 0, self.width-radius/2, self.height), fill=self.bg, outline=self.bg)
        self.create_rectangle((0, radius/2, self.width, self.height-radius/2), fill=self.bg, outline=self.bg)
        self.create_text(self.width/2, self.height/2, text=self.text, fill=self.fg, font=("Helvetica", 12))

    def on_click(self, event):
        if self.command:
            self.command()

    def on_enter(self, event):
        self.bg = self.hover_bg
        self.create_rounded_button()

    def on_leave(self, event):
        self.bg = self.default_bg
        self.create_rounded_button()

# Login Page class, inheriting from PageBase
class LoginPage(PageBase):
    def __init__(self, master):
        super().__init__(master, bg_color='#f0f0f0')  # Light gray background
        self.username_entry = None
        self.password_entry = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self._PageBase__frame, text="Login", font=("Helvetica", 18, "bold"), bg=self.bg_color).pack(pady=10)
        tk.Label(self._PageBase__frame, text="Username:", font=("Helvetica", 14), bg=self.bg_color).pack()  
        self.username_entry = tk.Entry(self._PageBase__frame, font=("Helvetica", 12), bd=2, relief="solid", width=30)  
        self.username_entry.pack(pady=5)

        tk.Label(self._PageBase__frame, text="Password:", font=("Helvetica", 14), bg=self.bg_color).pack()  
        self.password_entry = tk.Entry(self._PageBase__frame, show='*', font=("Helvetica", 12), bd=2, relief="solid", width=30)  
        self.password_entry.pack(pady=5)

        CustomButton(self._PageBase__frame, text="Login", command=self.login, hover_bg='#0056b3').pack(pady=10)
        CustomButton(self._PageBase__frame, text="Sign Up", command=self.sign_up, bg='#dc3545', hover_bg='#c82333').pack(pady=5)

    def login(self):
        username = self.username_entry.get()  
        password = self.password_entry.get()
        
        var = userInfo(username)  

        self.user = var
        if var:
            if password == var[-1]:
                messagebox.showinfo("Success", "Login Successful!")
                self.destroy()
                ProfilePage(self.master, username).pack()
            else:
                messagebox.showerror("Error", "Invalid password.")
        else:
            messagebox.showerror("Error", "Invalid username.")

    def sign_up(self):
        self.master._history.append(self)  
        self.destroy()  
        SignUpPage(self.master).pack()  

# SignUp Page class, inheriting from PageBase
class SignUpPage(PageBase):
    def __init__(self, master):
        super().__init__(master, bg_color='#f0f0f0')  
        self.username_entry = None
        self.email_entry = None
        self.skills_entry = None
        self.phone_entry = None
        self.degree_entry = None
        self.password_entry = None
        self.confirm_password_entry = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self._PageBase__frame, text="Sign Up", font=("Helvetica", 16, "bold"), bg=self.bg_color).pack(pady=10)

        tk.Label(self._PageBase__frame, text="Username:", font=("Helvetica", 14), bg=self.bg_color).pack()  
        self.username_entry = tk.Entry(self._PageBase__frame, font=("Helvetica", 12), bd=2, relief="solid", width=30)  
        self.username_entry.pack(pady=5)

        tk.Label(self._PageBase__frame, text="Email ID:", font=("Helvetica", 14), bg=self.bg_color).pack()  
        self.email_entry = tk.Entry(self._PageBase__frame, font=("Helvetica", 12), bd=2, relief="solid", width=30)  
        self.email_entry.pack(pady=5)

        tk.Label(self._PageBase__frame, text="Skills:", font=("Helvetica", 14), bg=self.bg_color).pack()  
        self.skills_entry = tk.Entry(self._PageBase__frame, font=("Helvetica", 12), bd=2, relief="solid", width=30)  
        self.skills_entry.pack(pady=5)

        tk.Label(self._PageBase__frame, text="Phone Number:", font=("Helvetica", 14), bg=self.bg_color).pack()  
        self.phone_entry = tk.Entry(self._PageBase__frame, font=("Helvetica", 12), bd=2, relief="solid", width=30)  
        self.phone_entry.pack(pady=5)

        tk.Label(self._PageBase__frame, text="Degree:", font=("Helvetica", 14), bg=self.bg_color).pack()  
        self.degree_entry = tk.Entry(self._PageBase__frame, font=("Helvetica", 12), bd=2, relief="solid", width=30)  
        self.degree_entry.pack(pady=5)

        tk.Label(self._PageBase__frame, text="Password:", font=("Helvetica", 14), bg=self.bg_color).pack()  
        self.password_entry = tk.Entry(self._PageBase__frame, show='*', font=("Helvetica", 12), bd=2, relief="solid", width=30)  
        self.password_entry.pack(pady=5)

        tk.Label(self._PageBase__frame, text="Confirm Password:", font=("Helvetica", 14), bg=self.bg_color).pack()  
        self.confirm_password_entry = tk.Entry(self._PageBase__frame, show='*', font=("Helvetica", 12), bd=2, relief="solid", width=30)  
        self.confirm_password_entry.pack(pady=5)

        CustomButton(self._PageBase__frame, text="Submit", command=self.submit).pack(pady=10)  
        CustomButton(self._PageBase__frame, text="Cancel", command=self.cancel, bg='#dc3545', hover_bg='#c82333').pack(pady=5)  

    def submit(self):
        username = self.username_entry.get().strip()  
        email = self.email_entry.get().strip()  
        skills = self.skills_entry.get().strip()  
        phone = self.phone_entry.get().strip()  
        degree = self.degree_entry.get().strip()  
        password = self.password_entry.get().strip()  
        confirm_password = self.confirm_password_entry.get().strip()  

        if not username or not email or not skills or not phone or not degree or not password or not confirm_password:
            messagebox.showerror("Error", "All fields are required.")  
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")  
            return
        else:
            messagebox.showinfo("Success", "User registered successfully!")
            addData(username, email, skills, phone, degree, password)
            print("Succesfully added") 
            self.master._history.pop()  
            self.destroy()  
            LoginPage(self.master).pack()  

    def cancel(self):
        self.master._history.pop()  
        self.destroy()  
        LoginPage(self.master).pack()  

# Profile Page class, inheriting from PageBase
class ProfilePage(PageBase):
    def __init__(self, master, username):
        super().__init__(master, bg_color='#f0f0f0')  
        self.username = username  
        self.create_widgets()
    

    def create_widgets(self):
        # var2 = userInfo(self.username)
        # self.user1 = var2
        # print(var2)
        tk.Label(self._PageBase__frame, text=f"Welcome, Shivam!", font=("Helvetica", 18, "bold"), bg=self.bg_color).pack(pady=10)
        
        tk.Label(self._PageBase__frame, text="User Information", font=("Helvetica", 14, "bold"), bg=self.bg_color).pack(pady=10)
        tk.Label(self._PageBase__frame, text="Name: ", font=("Helvetica", 12), bg=self.bg_color).pack(anchor=tk.W)
        tk.Label(self._PageBase__frame, text="Email: ", font=("Helvetica", 12), bg=self.bg_color).pack(anchor=tk.W)
        tk.Label(self._PageBase__frame, text="Phone_no: ", font=("Helvetica", 12), bg=self.bg_color).pack(anchor=tk.W)

        button_frame = tk.Frame(self._PageBase__frame, bg=self.bg_color)
        button_frame.pack(pady=10)

        # First row
        CustomButton(button_frame, text="View Profile", command=self.view_profile, bg='#28a745', hover_bg='#218838').grid(row=0, column=0, padx=10)
        CustomButton(button_frame, text="Job Seeking", command=self.show_job_seeking_page, hover_bg='#0056b3').grid(row=0, column=1, padx=10)
        CustomButton(button_frame, text="Feedback", command=self.show_feedback_page, bg='#ffc107', fg='#000000', hover_bg='#e0a800').grid(row=0, column=2, padx=10)

        # Second row
        CustomButton(self._PageBase__frame, text="Settings", command=self.show_settings, bg='#17a2b8', hover_bg='#138496').pack(pady=10)

        # Third row
        CustomButton(self._PageBase__frame, text="Logout", command=self.logout, bg='#dc3545', hover_bg='#c82333').pack()

        if self.master._history:
            CustomButton(self._PageBase__frame, text="Go Back", command=self.go_back, bg='#343a40', hover_bg='#23272b').pack()

    def view_profile(self):
        messagebox.showinfo("Profile", "Username: \nEmail: \nSkills: \nPhone Number: \nDegree: ")  

    def show_job_seeking_page(self):
        self.master._history.append(self)  
        self.destroy()  
        JobSeekingPage(self.master).pack()  

    def show_feedback_page(self):
        self.master._history.append(self)  
        self.destroy()  
        FeedbackPage(self.master).pack()  

    def show_settings(self):
        messagebox.showinfo("Settings", "Settings page not implemented yet.")  

    def logout(self):
        self.destroy()  
        LoginPage(self.master).pack()  

# Job Seeking Page class, inheriting from PageBase
class JobSeekingPage(PageBase):
    def __init__(self, master):
        super().__init__(master, bg_color='#f0f0f0')  
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self._PageBase__frame, text="Job Seeking", font=("Helvetica", 18, "bold"), bg=self.bg_color).pack(pady=10)

        tk.Label(self._PageBase__frame, text="Desired Roles:", font=("Helvetica", 14), bg=self.bg_color).pack()  
        desired_roles_entry = tk.Entry(self._PageBase__frame, font=("Helvetica", 12), bd=2, relief="solid", width=30)  
        desired_roles_entry.pack(pady=5)

        tk.Label(self._PageBase__frame, text="Remote/Online Preference:", font=("Helvetica", 14), bg=self.bg_color).pack()  
        remote_preference_entry = tk.Entry(self._PageBase__frame, font=("Helvetica", 12), bd=2, relief="solid", width=30)  
        remote_preference_entry.pack(pady=5)

        tk.Label(self._PageBase__frame, text="Preferred Salary:", font=("Helvetica", 14), bg=self.bg_color).pack()  
        preferred_salary_entry = tk.Entry(self._PageBase__frame, font=("Helvetica", 12), bd=2, relief="solid", width=30)  
        preferred_salary_entry.pack(pady=5)

        CustomButton(self._PageBase__frame, text="Submit", command=self.submit, hover_bg='#0056b3').pack(pady=10)  
        CustomButton(self._PageBase__frame, text="Go Back", command=self.go_back, bg='#343a40', hover_bg='#23272b').pack(pady=5)  

    def submit(self):
        # Placeholder for submitting job seeking details
        messagebox.showinfo("Job Seeking", "Job seeking details submitted successfully.")  

    def go_back(self):
        self.master._history.pop()  
        self.destroy()  
        if self.master._history:
            self.master._history[-1].pack()  
        else:
            ProfilePage(self.master, "shubh").pack()  

# Feedback Page class, inheriting from PageBase
class FeedbackPage(PageBase):
    def __init__(self, master):
        super().__init__(master, bg_color='#f0f0f0')  
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self._PageBase__frame, text="Feedback", font=("Helvetica", 18, "bold"), bg=self.bg_color).pack(pady=10)

        tk.Label(self._PageBase__frame, text="Your Feedback:", font=("Helvetica", 14), bg=self.bg_color).pack()  
        feedback_entry = tk.Text(self._PageBase__frame, font=("Helvetica", 12), bd=2, relief="solid", width=40, height=10)  
        feedback_entry.pack(pady=5)

        CustomButton(self._PageBase__frame, text="Submit Feedback", command=self.submit_feedback, hover_bg='#ffc107').pack(pady=10)  
        CustomButton(self._PageBase__frame, text="Go Back", command=self.go_back, bg='#343a40', hover_bg='#23272b').pack(pady=5)  

    def submit_feedback(self):
        # Placeholder for submitting feedback
        messagebox.showinfo("Feedback", "Feedback submitted successfully.")  

    def go_back(self):
        self.master._history.pop()  
        self.destroy()  
        if self.master._history:
            self.master._history[-1].pack()  
        else:
            ProfilePage(self.master, "shubh").pack()  

# Main Application class
class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Apna App")
        self.geometry("600x400")
        self.configure(bg='#e3f2fd')  # Light blue background color
        self._history = []  # To store page history

        self._initialize()

    def _initialize(self):
        LoginPage(self).pack()

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
