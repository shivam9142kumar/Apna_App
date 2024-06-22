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
            previous_page = self.master._history.pop()  
            self.destroy()  
            previous_page.pack()  

# Login Page class, inheriting from PageBase
class LoginPage(PageBase):
    def __init__(self, master):
        super().__init__(master, bg_color='#f0f0f0')  
        self.username_entry = None
        self.password_entry = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self._PageBase__frame, text="Username:", font=("Helvetica", 14), bg='#f0f0f0').pack()  
        self.username_entry = tk.Entry(self._PageBase__frame, font=("Helvetica", 12))  
        self.username_entry.pack(pady=5)

        tk.Label(self._PageBase__frame, text="Password:", font=("Helvetica", 14), bg='#f0f0f0').pack()  
        self.password_entry = tk.Entry(self._PageBase__frame, show='*', font=("Helvetica", 12))  
        self.password_entry.pack(pady=5)

        tk.Button(self._PageBase__frame, text="Login", command=self.login, font=("Helvetica", 12), bg='#007bff', fg='#ffffff').pack(pady=10, padx=10)  
        tk.Button(self._PageBase__frame, text="Sign Up", command=self.sign_up, font=("Helvetica", 12), bg='#28a745', fg='#ffffff').pack(pady=5, padx=10)  

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

        tk.Button(self._PageBase__frame, text="Submit", command=self.submit, font=("Helvetica", 12), bg='#007bff', fg='#ffffff').pack(pady=10, padx=10)  
        tk.Button(self._PageBase__frame, text="Cancel", command=self.cancel, font=("Helvetica", 12), bg='#dc3545', fg='#ffffff').pack(pady=5, padx=10)  

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
        self.phone_number = "9898989898"  
        self.degree = "Btech CSE with specialization in Machine Learning"  
        self.skills = "PYTHON, JAVA, R, SQL"  
        self.languages = "English, Hindi"  
        self.interests = "Machine Learning, Data Science"  
        self.certifications = "Certification in Python, Certification in Data Science"  
        self.experience = "2 years"  
        self.current_role = "Software Engineer"  
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self._PageBase__frame, text=f"Welcome, {self.username}!", font=("Helvetica", 16, "bold"), bg='#f0f0f0').pack(pady=10)
        
        tk.Label(self._PageBase__frame, text="User Information", font=("Helvetica", 14, "bold"), bg='#f0f0f0').pack(pady=10)
        tk.Label(self._PageBase__frame, text=f"Name: Shubh Agrawal", font=("Helvetica", 12), bg='#f0f0f0').pack(anchor=tk.W)
        tk.Label(self._PageBase__frame, text=f"Email: shubh@gmail.com", font=("Helvetica", 12), bg='#f0f0f0').pack(anchor=tk.W)
        tk.Label(self._PageBase__frame, text=f"Phone Number: {self.phone_number}", font=("Helvetica", 12), bg='#f0f0f0').pack(anchor=tk.W)
        tk.Label(self._PageBase__frame, text=f"Degree: {self.degree}", font=("Helvetica", 12), bg='#f0f0f0').pack(anchor=tk.W)
        tk.Label(self._PageBase__frame, text=f"Skills: {self.skills}", font=("Helvetica", 12), bg='#f0f0f0').pack(anchor=tk.W)
        tk.Label(self._PageBase__frame, text=f"Languages: {self.languages}", font=("Helvetica", 12), bg='#f0f0f0').pack(anchor=tk.W)
        tk.Label(self._PageBase__frame, text=f"Interests: {self.interests}", font=("Helvetica", 12), bg='#f0f0f0').pack(anchor=tk.W)
        tk.Label(self._PageBase__frame, text=f"Certifications: {self.certifications}", font=("Helvetica", 12), bg='#f0f0f0').pack(anchor=tk.W)
        tk.Label(self._PageBase__frame, text=f"Experience: {self.experience}", font=("Helvetica", 12), bg='#f0f0f0').pack(anchor=tk.W)
        tk.Label(self._PageBase__frame, text=f"Current Role: {self.current_role}", font=("Helvetica", 12), bg='#f0f0f0').pack(anchor=tk.W)
        
        tk.Button(self._PageBase__frame, text="Job Seeking Preferences", command=self.job_seeking, font=("Helvetica", 12), bg='#007bff', fg='#ffffff').pack(pady=10, padx=10)
        tk.Button(self._PageBase__frame, text="Give Feedback", command=self.feedback, font=("Helvetica", 12), bg='#28a745', fg='#ffffff').pack(pady=5, padx=10)
        tk.Button(self._PageBase__frame, text="Logout", command=self.logout, font=("Helvetica", 12), bg='#dc3545', fg='#ffffff').pack(pady=5, padx=10)

    def job_seeking(self):
        self.master._history.append(self)  
        self.destroy()  
        JobSeekingPage(self.master, self.username).pack()  

    def feedback(self):
        self.master._history.append(self)  
        self.destroy()  
        FeedbackPage(self.master, self.username).pack()  

    def logout(self):
        self.master._history.clear()  
        self.destroy()  
        LoginPage(self.master).pack()  

# Job Seeking Page class, inheriting from PageBase
class JobSeekingPage(PageBase):
    def __init__(self, master, username):
        super().__init__(master, bg_color='#f0f0f0')  
        self.username = username  
        self.desired_roles_entry = None
        self.desired_locations_entry = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self._PageBase__frame, text=f"Job Seeking Page for {self.username}", font=("Helvetica", 16, "bold"), bg='#f0f0f0').pack(pady=10)

        tk.Label(self._PageBase__frame, text="Desired Roles:", font=("Helvetica", 14), bg='#f0f0f0').pack()
        self.desired_roles_entry = tk.Entry(self._PageBase__frame, font=("Helvetica", 12))  
        self.desired_roles_entry.pack(pady=5)

        tk.Label(self._PageBase__frame, text="Desired Locations:", font=("Helvetica", 14), bg='#f0f0f0').pack()
        self.desired_locations_entry = tk.Entry(self._PageBase__frame, font=("Helvetica", 12))  
        self.desired_locations_entry.pack(pady=5)

        tk.Button(self._PageBase__frame, text="Save Preferences", command=self.save_preferences, font=("Helvetica", 12), bg='#007bff', fg='#ffffff').pack(pady=10)
        tk.Button(self._PageBase__frame, text="Go Back", command=self.go_back, font=("Helvetica", 12), bg='#343a40', fg='#ffffff').pack()

    def save_preferences(self):
        desired_roles = self.desired_roles_entry.get().strip()
        desired_locations = self.desired_locations_entry.get().strip()

        if desired_roles and desired_locations:
            messagebox.showinfo("Preferences Saved", "Your job preferences have been saved successfully!")
        else:
            messagebox.showerror("Error", "Please fill out all fields before saving preferences.")

    def go_back(self):
        if self.master._history:
            previous_page = self.master._history.pop()  
            self.destroy()  
            previous_page.pack()  

# Feedback Page class, inheriting from PageBase
class FeedbackPage(PageBase):
    def __init__(self, master, username):
        super().__init__(master, bg_color='#f0f0f0')  
        self.username = username  
        self.feedback_text = None
        self.feedback_category = None
        self.feedback_rating = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self._PageBase__frame, text=f"Feedback Page for {self.username}", font=("Helvetica", 16, "bold"), bg='#f0f0f0').pack(pady=10)

        tk.Label(self._PageBase__frame, text="Feedback Category:", font=("Helvetica", 14), bg='#f0f0f0').pack()
        self.feedback_category = tk.Entry(self._PageBase__frame, font=("Helvetica", 12))  
        self.feedback_category.pack(pady=5)

        tk.Label(self._PageBase__frame, text="Your feedback:", font=("Helvetica", 14), bg='#f0f0f0').pack()
        self.feedback_text = tk.Text(self._PageBase__frame, width=40, height=5, font=("Helvetica", 12))
        self.feedback_text.pack(pady=10)

        tk.Label(self._PageBase__frame, text="Rating (1-5):", font=("Helvetica", 14), bg='#f0f0f0').pack()
        self.feedback_rating = tk.Entry(self._PageBase__frame, font=("Helvetica", 12))  
        self.feedback_rating.pack(pady=5)

        tk.Button(self._PageBase__frame, text="Submit Feedback", command=self.submit_feedback, font=("Helvetica", 12), bg='#007bff', fg='#ffffff').pack()
        tk.Button(self._PageBase__frame, text="Go Back", command=self.go_back, font=("Helvetica", 12), bg='#343a40', fg='#ffffff').pack()

    def submit_feedback(self):
        category = self.feedback_category.get().strip()
        feedback = self.feedback_text.get("1.0", tk.END).strip()
        rating = self.feedback_rating.get().strip()

        if category and feedback and rating.isdigit() and 1 <= int(rating) <= 5:
            messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")
        else:
            messagebox.showerror("Error", "Please fill out all fields correctly before submitting.")

    def go_back(self):
        if self.master._history:
            previous_page = self.master._history.pop()  
            self.destroy()  
            previous_page.pack()  

# Main application class
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Job Portal Application")
        self.geometry("600x400")
        self._history = []  
        LoginPage(self).pack()  


if __name__ == "__main__":
    app = Application()
    app.mainloop()
