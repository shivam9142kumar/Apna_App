import tkinter as tk
from tkinter import messagebox

# Base class for pages
class PageBase(tk.Frame):
    def __init__(self, master, bg_color='#ffffff'):
        super().__init__(master)
        self.config(bg=bg_color)
        self._create_frame()

    def _create_frame(self):
        self._frame = tk.Frame(self, bg=self.cget('bg'))  # Private frame
        self._frame.pack(expand=True, fill='both')

    def go_back(self):
        if self.master._history:
            while True:
                previous_page = self.master._history.pop()
                if isinstance(previous_page, ProfilePage):
                    break
                previous_page.destroy()
            self.destroy()
            previous_page.pack()

# Login Page class, inheriting from PageBase
class LoginPage(PageBase):
    def __init__(self, master):
        super().__init__(master, bg_color='#f0f0f0')  # Light gray background
        self.username_entry = None
        self.password_entry = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self._frame, text="Username:", font=("Helvetica", 14), bg='#f0f0f0').pack()
        self.username_entry = tk.Entry(self._frame, font=("Helvetica", 12))
        self.username_entry.pack(pady=5)

        tk.Label(self._frame, text="Password:", font=("Helvetica", 14), bg='#f0f0f0').pack()
        self.password_entry = tk.Entry(self._frame, show='*', font=("Helvetica", 12))
        self.password_entry.pack(pady=5)

        tk.Button(self._frame, text="Login", command=self.login, font=("Helvetica", 12), bg='#007bff', fg='#ffffff').pack(pady=10, padx=10)
        tk.Button(self._frame, text="Sign Up", command=self.sign_up, font=("Helvetica", 12), bg='#28a745', fg='#ffffff').pack(pady=5, padx=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "gautam" and password == "gautam":
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
        tk.Label(self._frame, text="Sign Up", font=("Helvetica", 16, "bold"), bg='#f0f0f0').pack(pady=10)

        tk.Label(self._frame, text="Username:", font=("Helvetica", 14), bg='#f0f0f0').pack()
        self.username_entry = tk.Entry(self._frame, font=("Helvetica", 12))
        self.username_entry.pack(pady=5)

        tk.Label(self._frame, text="Email:", font=("Helvetica", 14), bg='#f0f0f0').pack()
        self.email_entry = tk.Entry(self._frame, font=("Helvetica", 12))
        self.email_entry.pack(pady=5)

        tk.Label(self._frame, text="Skills:", font=("Helvetica", 14), bg='#f0f0f0').pack()
        self.skills_entry = tk.Entry(self._frame, font=("Helvetica", 12))
        self.skills_entry.pack(pady=5)

        tk.Label(self._frame, text="Phone Number:", font=("Helvetica", 14), bg='#f0f0f0').pack()
        self.phone_entry = tk.Entry(self._frame, font=("Helvetica", 12))
        self.phone_entry.pack(pady=5)

        tk.Label(self._frame, text="Degree:", font=("Helvetica", 14), bg='#f0f0f0').pack()
        self.degree_entry = tk.Entry(self._frame, font=("Helvetica", 12))
        self.degree_entry.pack(pady=5)

        tk.Label(self._frame, text="Password:", font=("Helvetica", 14), bg='#f0f0f0').pack()
        self.password_entry = tk.Entry(self._frame, show='*', font=("Helvetica", 12))
        self.password_entry.pack(pady=5)

        tk.Label(self._frame, text="Confirm Password:", font=("Helvetica", 14), bg='#f0f0f0').pack()
        self.confirm_password_entry = tk.Entry(self._frame, show='*', font=("Helvetica", 12))
        self.confirm_password_entry.pack(pady=5)

        tk.Button(self._frame, text="Submit", command=self.submit, font=("Helvetica", 12), bg='#007bff', fg='#ffffff').pack(pady=10, padx=10)
        tk.Button(self._frame, text="Cancel", command=self.cancel, font=("Helvetica", 12), bg='#dc3545', fg='#ffffff').pack(pady=5, padx=10)

    def submit(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        confirm_password = self.confirm_password_entry.get().strip()
        email = self.email_entry.get().strip()
        skills = self.skills_entry.get().strip()
        phone = self.phone_entry.get().strip()
        degree = self.degree_entry.get().strip()

        if not username or not password or not confirm_password or not email or not skills or not phone or not degree:
            messagebox.showerror("Error", "All fields are required.")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        messagebox.showinfo("Success", "User registered successfully!")
        self.master._history.pop()  # Remove SignUpPage from history
        self.destroy()
        LoginPage(self.master).pack()

    def cancel(self):
        self.master._history.pop()  # Remove SignUpPage from history
        self.destroy()
        LoginPage(self.master).pack()

# Profile Page class, inheriting from PageBase
class ProfilePage(PageBase):
    def __init__(self, master, username):
        super().__init__(master, bg_color='#f0f0f0')
        self.username = username
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self._frame, text=f"Welcome, {self.username}!", font=("Helvetica", 16, "bold"), bg='#f0f0f0').pack(pady=10)

        tk.Label(self._frame, text="User Information", font=("Helvetica", 14, "bold"), bg='#f0f0f0').pack(pady=10)
        user_info_frame = tk.Frame(self._frame, bg='#f0f0f0')
        user_info_frame.pack(pady=10, padx=10, fill='both', expand=True)

        user_info_labels = [
            ("Name:", "Shubh Agrawal"),
            ("Email:", "shubh@gmail.com"),
            ("Location:", "Bangalore, INDIA"),
            ("Skills:", "Python, JavaScript"),
            ("Phone Number:", "9898989898"),
            ("Degree:", "BTech CSE with specialization in Machine Learning"),
            ("Experience:", "3 years"),
            ("Current Role:", "Software Engineer"),
            ("Interests:", "Machine Learning, Web Development"),
            ("Languages:", "English, Hindi"),
            ("Certifications:", "Python Certification, Web Development Certification"),
        ]

        for label, value in user_info_labels:
            tk.Label(user_info_frame, text=label, font=("Helvetica", 12), bg='#f0f0f0', width=15, anchor=tk.W).grid(sticky=tk.W)
            tk.Label(user_info_frame, text=value, font=("Helvetica", 12), bg='#f0f0f0', anchor=tk.W).grid(row=user_info_labels.index((label, value)), column=1, sticky=tk.W)

        tk.Button(self._frame, text="Edit Profile", command=self.edit_profile, font=("Helvetica", 12), bg='#28a745', fg='#ffffff').pack()
        tk.Button(self._frame, text="Job Seeking", command=self.show_job_seeking_page, font=("Helvetica", 12), bg='#007bff', fg='#ffffff').pack()
        tk.Button(self._frame, text="Feedback", command=self.show_feedback_page, font=("Helvetica", 12), bg='#ffc107', fg='#000000').pack()
        tk.Button(self._frame, text="Settings", command=self.show_settings, font=("Helvetica", 12), bg='#17a2b8', fg='#ffffff').pack()
        tk.Button(self._frame, text="Logout", command=self.logout, font=("Helvetica", 12), bg='#dc3545', fg='#ffffff').pack()

        if self.master._history:
            tk.Button(self._frame, text="Go Back", command=self.go_back, font=("Helvetica", 12), bg='#343a40', fg='#ffffff').pack()

    def edit_profile(self):
        self.navigate_to(EditProfilePage)

    def show_job_seeking_page(self):
        self.navigate_to(JobSeekingPage)

    def show_feedback_page(self):
        self.navigate_to(FeedbackPage)

    def show_settings(self):
        messagebox.showinfo("Settings", "No settings available in this demo.")

    def logout(self):
        self.master._history.clear()
        self.destroy()
        LoginPage(self.master).pack()

    def go_back(self):
        if self.master._history:
            previous_page = self.master._history.pop()
            self.destroy()
            previous_page.pack()

    def navigate_to(self, page_class):
        self.master._history.append(self)
        self.destroy()
        page_class(self.master, self.username).pack()

# Edit Profile Page class, inheriting from PageBase
class EditProfilePage(PageBase):
    def __init__(self, master, username):
        super().__init__(master, bg_color='#f0f0f0')
        self.username = username
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self._frame, text=f"Edit Profile - {self.username}", font=("Helvetica", 16, "bold"), bg='#f0f0f0').pack(pady=10)

        tk.Label(self._frame, text="User Information", font=("Helvetica", 14, "bold"), bg='#f0f0f0').pack(pady=10)

        editable_fields = [
            ("Name:", "Shubh Agrawal"),
            ("Email:", "shubh@gmail.com"),
            ("Location:", "Bangalore, INDIA"),
            ("Skills:", "Python, JavaScript"),
            ("Phone Number:", "9898989898"),
            ("Degree:", "BTech CSE with specialization in Machine Learning")
        ]

        for label, value in editable_fields:
            tk.Label(self._frame, text=label, font=("Helvetica", 12), bg='#f0f0f0', width=15, anchor=tk.W).pack(pady=3)
            tk.Entry(self._frame, font=("Helvetica", 12), bg='#ffffff', relief=tk.SOLID, bd=1).insert(0, value).pack(pady=3)

        tk.Button(self._frame, text="Save Changes", command=self.save_changes, font=("Helvetica", 12), bg='#007bff', fg='#ffffff').pack(pady=10)
        tk.Button(self._frame, text="Cancel", command=self.go_back, font=("Helvetica", 12), bg='#dc3545', fg='#ffffff').pack(pady=5)

    def save_changes(self):
        messagebox.showinfo("Changes Saved", "Profile changes saved successfully!")
        self.go_back()

    def go_back(self):
        previous_page = self.master._history.pop()
        self.destroy()
        previous_page.pack()

# Job Seeking Page class, inheriting from PageBase
class JobSeekingPage(PageBase):
    def __init__(self, master, username):
        super().__init__(master, bg_color='#f0f0f0')
        self.username = username
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self._frame, text=f"Job Seeking - {self.username}", font=("Helvetica", 16, "bold"), bg='#f0f0f0').pack(pady=10)

        tk.Label(self._frame, text="Job Preferences", font=("Helvetica", 14, "bold"), bg='#f0f0f0').pack(pady=10)
        job_preferences = [
            "Looking for opportunities in Python development.",
            "Experience in web development and machine learning.",
            "Open to remote and freelance work."
        ]
        for pref in job_preferences:
            tk.Label(self._frame, text=pref, font=("Helvetica", 12), bg='#f0f0f0').pack(anchor=tk.W, padx=10)

        tk.Button(self._frame, text="Go Back", command=self.go_back, font=("Helvetica", 12), bg='#343a40', fg='#ffffff').pack(pady=10)

    def go_back(self):
        previous_page = self.master._history.pop()
        self.destroy()
        previous_page.pack()

# Feedback Page class, inheriting from PageBase
class FeedbackPage(PageBase):
    def __init__(self, master, username):
        super().__init__(master, bg_color='#f0f0f0')
        self.username = username
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self._frame, text=f"Feedback - {self.username}", font=("Helvetica", 16, "bold"), bg='#f0f0f0').pack(pady=10)

        tk.Label(self._frame, text="Provide your feedback below:", font=("Helvetica", 14, "bold"), bg='#f0f0f0').pack(pady=10)

        feedback_entry = tk.Text(self._frame, height=5, width=50)
        feedback_entry.pack(pady=10)

        submit_button = tk.Button(self._frame, text="Submit Feedback", command=self.submit_feedback, font=("Helvetica", 12), bg='#007bff', fg='#ffffff')
        submit_button.pack(pady=10)

        tk.Button(self._frame, text="Go Back", command=self.go_back, font=("Helvetica", 12), bg='#343a40', fg='#ffffff').pack(pady=10)

    def submit_feedback(self):
        messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")

    def go_back(self):
        previous_page = self.master._history.pop()
        self.destroy()
        previous_page.pack()

# Main Application class, inheriting from tk.Tk
class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("User Authentication System")
        self._history = []  # Stack to keep track of navigation history

        # Start with the login page
        LoginPage(self).pack()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
