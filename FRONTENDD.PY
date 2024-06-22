import tkinter as tk
from tkinter import messagebox

# Base class for all pages in the application
class PageBase:
    def __init__(self, master, bg_color='#ffffff'): 
        self.master = master
        self.__frame = tk.Frame(master, bg=bg_color)
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

# Login Page class, inheriting from PageBase
class LoginPage(PageBase):
    def __init__(self, master):
        super().__init__(master, bg_color='#f0f0f0')  # Light gray background
        self.username_entry = None
        self.password_entry = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self._PageBase__frame, text="Username:", font=("Helvetica", 14), bg='#f0f0f0').pack()  # Light gray background, blue text
        self.username_entry = tk.Entry(self._PageBase__frame, font=("Helvetica", 12))  
        self.username_entry.pack(pady=5)

        tk.Label(self._PageBase__frame, text="Password:", font=("Helvetica", 14), bg='#f0f0f0').pack()  
        self.password_entry = tk.Entry(self._PageBase__frame, show='*', font=("Helvetica", 12))  
        self.password_entry.pack(pady=5)

        tk.Button(self._PageBase__frame, text="Login", command=self.login, font=("Helvetica", 12), bg='#007bff', fg='#ffffff').pack(pady=10, padx=10)  # Blue button with white text
        tk.Button(self._PageBase__frame, text="Sign Up", command=self.sign_up, font=("Helvetica", 12), bg='#28a745', fg='#ffffff').pack(pady=5, padx=10)  # Green button with white text

    def login(self):
        username = self.username_entry.get()  
        password = self.password_entry.get()  

        if username == "shubh" and password == "0000":  
            self.destroy()  
            ProfilePage(self.master, username).pack()  
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")  

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
        tk.Label(self._PageBase__frame, text="Sign Up", font=("Helvetica", 16, "bold"), bg='#f0f0f0').pack(pady=10)

        tk.Label(self._PageBase__frame, text="Username:", font=("Helvetica", 14), bg='#f0f0f0').pack()  
        self.username_entry = tk.Entry(self._PageBase__frame, font=("Helvetica", 12))  
        self.username_entry.pack(pady=5)

        tk.Label(self._PageBase__frame, text="Email ID:", font=("Helvetica", 14), bg='#f0f0f0').pack()  
        self.email_entry = tk.Entry(self._PageBase__frame, font=("Helvetica", 12))  
        self.email_entry.pack(pady=5)

        tk.Label(self._PageBase__frame, text="Skills:", font=("Helvetica", 14), bg='#f0f0f0').pack()  
        self.skills_entry = tk.Entry(self._PageBase__frame, font=("Helvetica", 12))  
        self.skills_entry.pack(pady=5)

        tk.Label(self._PageBase__frame, text="Phone Number:", font=("Helvetica", 14), bg='#f0f0f0').pack()  
        self.phone_entry = tk.Entry(self._PageBase__frame, font=("Helvetica", 12))  
        self.phone_entry.pack(pady=5)

        tk.Label(self._PageBase__frame, text="Degree:", font=("Helvetica", 14), bg='#f0f0f0').pack()  
        self.degree_entry = tk.Entry(self._PageBase__frame, font=("Helvetica", 12))  
        self.degree_entry.pack(pady=5)

        tk.Label(self._PageBase__frame, text="Password:", font=("Helvetica", 14), bg='#f0f0f0').pack()  
        self.password_entry = tk.Entry(self._PageBase__frame, show='*', font=("Helvetica", 12))  
        self.password_entry.pack(pady=5)

        tk.Label(self._PageBase__frame, text="Confirm Password:", font=("Helvetica", 14), bg='#f0f0f0').pack()  
        self.confirm_password_entry = tk.Entry(self._PageBase__frame, show='*', font=("Helvetica", 12))  
        self.confirm_password_entry.pack(pady=5)

        tk.Button(self._PageBase__frame, text="Submit", command=self.submit, font=("Helvetica", 12), bg='#007bff', fg='#ffffff').pack(pady=10, padx=10)  # Blue button with white text
        tk.Button(self._PageBase__frame, text="Cancel", command=self.cancel, font=("Helvetica", 12), bg='#dc3545', fg='#ffffff').pack(pady=5, padx=10)  # Red button with white text

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

        messagebox.showinfo("Success", "User registered successfully!")  
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
        tk.Label(self._PageBase__frame, text=f"Welcome, {self.username}!", font=("Helvetica", 16, "bold"), bg='#f0f0f0').pack(pady=10)
        
        tk.Label(self._PageBase__frame, text="User Information", font=("Helvetica", 14, "bold"), bg='#f0f0f0').pack(pady=10)
        tk.Label(self._PageBase__frame, text="Name: Shubh Agrawal", font=("Helvetica", 12), bg='#f0f0f0').pack(anchor=tk.W)
        tk.Label(self._PageBase__frame, text="Email: shubh@gmail.com", font=("Helvetica", 12), bg='#f0f0f0').pack(anchor=tk.W)
        tk.Label(self._PageBase__frame, text="Location: Bangalore, INDIA", font=("Helvetica", 12), bg='#f0f0f0').pack(anchor=tk.W)

        tk.Button(self._PageBase__frame, text="View Profile", command=self.view_profile, font=("Helvetica", 12), bg='#28a745', fg='#ffffff').pack()
        tk.Button(self._PageBase__frame, text="Job Seeking", command=self.show_job_seeking_page, font=("Helvetica", 12), bg='#007bff', fg='#ffffff').pack()
        tk.Button(self._PageBase__frame, text="Feedback", command=self.show_feedback_page, font=("Helvetica", 12), bg='#ffc107', fg='#000000').pack()
        tk.Button(self._PageBase__frame, text="Settings", command=self.show_settings, font=("Helvetica", 12), bg='#17a2b8', fg='#ffffff').pack()

        tk.Button(self._PageBase__frame, text="Logout", command=self.logout, font=("Helvetica", 12), bg='#dc3545', fg='#ffffff').pack()
        if self.master._history:
            tk.Button(self._PageBase__frame, text="Go Back", command=self.go_back, font=("Helvetica", 12), bg='#343a40', fg='#ffffff').pack()

    def view_profile(self):
        messagebox.showinfo("Profile", "Username: shubh\nEmail: shubh@gmail.com\nSkills: Python, JavaScript\nPhone Number: +91 9876543210\nDegree: Bachelor of Engineering")  

    def show_job_seeking_page(self):
        messagebox.showinfo("Job Seeking", "Job seeking page not implemented yet.")  

    def show_feedback_page(self):
        messagebox.showinfo("Feedback", "Feedback page not implemented yet.")  

    def show_settings(self):
        messagebox.showinfo("Settings", "Settings page not implemented yet.")  

    def logout(self):
        self.destroy()  
        LoginPage(self.master).pack()  

# Main Application class
class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Application")
        self.geometry("600x400")
        self._history = []  # To store page history

        self._initialize()

    def _initialize(self):
        LoginPage(self).pack()

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
