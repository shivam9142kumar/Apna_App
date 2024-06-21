import tkinter as tk
from tkinter import messagebox
import BackEnd

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
        var = BackEnd.userInfo(username)  

        self.user = var
        if var:
            if password == var[-1]:
                messagebox.showinfo("Success", "Login Successful!")
                self.show_loading_page()
            else:
                messagebox.showerror("Error", "Invalid password.")
        else:
            messagebox.showerror("Error", "Invalid username.")
    def sign_up(self):
        self.master._history.append(self)  
        self.destroy()  
        SignUpPage(self.master).pack()  

# SignUp Page class, inheriting from PageBase
class SignUpPage(PageBase):
    def __init__(self, master):
        super().__init__(master, bg_color='#f0f0f0')  
        self.username_entry = None
        self.password_entry = None
        self.confirm_password_entry = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self._PageBase__frame, text="Sign Up", font=("Helvetica", 16, "bold"), bg='#f0f0f0').pack(pady=10)

        tk.Label(self._PageBase__frame, text="Username:", font=("Helvetica", 14), bg='#f0f0f0').pack()  
        self.username_entry = tk.Entry(self._PageBase__frame, font=("Helvetica", 12))  
        self.username_entry.pack(pady=5)

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
        password = self.password_entry.get().strip()  
        confirm_password = self.confirm_password_entry.get().strip()  

        if not username or not password or not confirm_password:
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
        tk.Label(self._PageBase__frame, text=f"Welcome, {self.username}!", font=("Helvetica", 16, "bold"), bg='#f0f0f0').pack(pady=20)

        user_info_frame = tk.Frame(self._PageBase__frame, bg='#f0f0f0')
        user_info_frame.pack(pady=10, padx=20, fill='both')

        tk.Label(user_info_frame, text="User Information", font=("Helvetica", 14, "bold"), bg='#f0f0f0').pack(anchor=tk.W, pady=10)
        tk.Label(user_info_frame, text="Name: Shubh Agrawal", font=("Helvetica", 12), bg='#f0f0f0').pack(anchor=tk.W)
        tk.Label(user_info_frame, text="Email: shubh@gmail.com", font=("Helvetica", 12), bg='#f0f0f0').pack(anchor=tk.W)
        tk.Label(user_info_frame, text="Location: Bangalore, INDIA", font=("Helvetica", 12), bg='#f0f0f0').pack(anchor=tk.W)

        navigation_frame = tk.Frame(self._PageBase__frame, bg='#f0f0f0')
        navigation_frame.pack(pady=20)

        tk.Button(navigation_frame, text="View Profile", command=self.view_profile, font=("Helvetica", 12), bg='#007bff', fg='#ffffff').pack(side=tk.LEFT, padx=10)
        tk.Button(navigation_frame, text="Job Seeking", command=self.show_job_seeking_page, font=("Helvetica", 12), bg='#007bff', fg='#ffffff').pack(side=tk.LEFT, padx=10)
        tk.Button(navigation_frame, text="Feedback", command=self.show_feedback_page, font=("Helvetica", 12), bg='#007bff', fg='#ffffff').pack(side=tk.LEFT, padx=10)
        tk.Button(navigation_frame, text="Settings", command=self.show_settings, font=("Helvetica", 12), bg='#007bff', fg='#ffffff').pack(side=tk.LEFT, padx=10)
        tk.Button(navigation_frame, text="Logout", command=self.logout, font=("Helvetica", 12), bg='#dc3545', fg='#ffffff').pack(side=tk.RIGHT, padx=10)

        if self.master._history:
            tk.Button(navigation_frame, text="Go Back", command=self.go_back, font=("Helvetica", 12), bg='#343a40', fg='#ffffff').pack(side=tk.RIGHT, padx=10)

    def view_profile(self):
        self.navigate_to(ViewProfilePage, self.username)

    def show_job_seeking_page(self):
        self.navigate_to(JobSeekingPage)

    def show_feedback_page(self):
        self.navigate_to(FeedbackPage)

    def navigate_to(self, page_class, *args):
        self.master._history.append(self)
        self.destroy()
        page_class(self.master, *args).pack()

    def logout(self):
        self.destroy()
        LoginPage(self.master).pack()

    def show_settings(self):
        messagebox.showinfo("Settings", "No settings available in this demo")

# View Profile Page class, inheriting from PageBase
class ViewProfilePage(PageBase):
    def __init__(self, master, username):
        super().__init__(master, bg_color='#f0f0f0')  
        self.username = username  
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self._PageBase__frame, text=f"Profile of {self.username}", font=("Helvetica", 16, "bold"), bg='#f0f0f0').pack(pady=10)
        tk.Label(self._PageBase__frame, text="User Information", font=("Helvetica", 14, "bold"), bg='#f0f0f0').pack(pady=10)

        tk.Label(self._PageBase__frame, text="Name: Shubh Agrawal", font=("Helvetica", 12), bg='#f0f0f0').pack(anchor=tk.W)
        tk.Label(self._PageBase__frame, text="Email: shubh@gmail.com", font=("Helvetica", 12), bg='#f0f0f0').pack(anchor=tk.W)
        tk.Label(self._PageBase__frame, text="Location: Bangalore, INDIA", font=("Helvetica", 12), bg='#f0f0f0').pack(anchor=tk.W)

        tk.Button(self._PageBase__frame, text="Edit Profile", command=self.edit_profile, font=("Helvetica", 12), bg='#007bff', fg='#ffffff').pack(pady=10)

    def edit_profile(self):
        messagebox.showinfo("Edit Profile", "Edit profile functionality will be implemented here.")  

# JobSeekingPage class, inheriting from PageBase
class JobSeekingPage(PageBase):
    def __init__(self, master):
        super().__init__(master, bg_color='#f0f0f0')  
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self._PageBase__frame, text="Job Seeking Page", font=("Helvetica", 16, "bold"), bg='#f0f0f0').pack(pady=10)

        job_list = [
            {"title": "Software Engineer", "company": "Tech Solutions Inc."},
            {"title": "Data Analyst", "company": "Data Insights Co."},
            {"title": "Marketing Manager", "company": "Global Marketing Group"},
        ]

        for job in job_list:
            job_frame = tk.Frame(self._PageBase__frame, bd=1, relief=tk.RIDGE, bg='#ffffff')  
            job_frame.pack(pady=5, fill=tk.X)

            tk.Label(job_frame, text=f"{job['title']} at {job['company']}", font=("Helvetica", 12), bg='#ffffff').pack(side=tk.LEFT, padx=10)
            tk.Button(job_frame, text="Apply", command=lambda title=job['title']: self.apply_job(title), font=("Helvetica", 10), bg='#28a745', fg='#ffffff').pack(side=tk.RIGHT, padx=10)

        tk.Label(self._PageBase__frame, text="Filter by Company:", font=("Helvetica", 14, "bold"), bg='#f0f0f0').pack(pady=10)
        company_filter = tk.StringVar()
        company_filter.set("All")
        company_options = ["All"] + list(set(job['company'] for job in job_list))
        tk.OptionMenu(self._PageBase__frame, company_filter, *company_options, command=self.filter_jobs).pack()

    def apply_job(self, job_title):
        messagebox.showinfo("Job Application", f"You have applied for {job_title}.")  

    def filter_jobs(self, selected_company):
        print(f"Filtering jobs by company: {selected_company}")  

# FeedbackPage class, inheriting from PageBase
class FeedbackPage(PageBase):
    def __init__(self, master):
        super().__init__(master, bg_color='#f0f0f0')  
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self._PageBase__frame, text="Feedback Page", font=("Helvetica", 16, "bold"), bg='#f0f0f0').pack(pady=10)

        tk.Label(self._PageBase__frame, text="Type of Feedback:", font=("Helvetica", 14), bg='#f0f0f0').pack()
        feedback_type = tk.StringVar()
        feedback_type.set("General")
        tk.OptionMenu(self._PageBase__frame, feedback_type, "General", "Bug Report", "Feature Request").pack()

        tk.Label(self._PageBase__frame, text="Your Feedback:", font=("Helvetica", 14), bg='#f0f0f0').pack()
        feedback_entry = tk.Text(self._PageBase__frame, height=5, width=50, font=("Helvetica", 12))
        feedback_entry.pack()

        tk.Button(self._PageBase__frame, text="Submit Feedback", command=lambda: self.submit_feedback(feedback_type.get(), feedback_entry), font=("Helvetica", 12), bg='#007bff', fg='#ffffff').pack(pady=10)

        tk.Label(self._PageBase__frame, text="Additional Options", font=("Helvetica", 14, "bold"), bg='#f0f0f0').pack(pady=10)
        satisfaction_label = tk.Label(self._PageBase__frame, text="Satisfaction Level:", font=("Helvetica", 12), bg='#f0f0f0')
        satisfaction_label.pack()
        satisfaction_scale = tk.Scale(self._PageBase__frame, from_=1, to=5, orient=tk.HORIZONTAL, font=("Helvetica", 12))
        satisfaction_scale.pack()

    def submit_feedback(self, feedback_type, feedback_entry):
        feedback_text = feedback_entry.get("1.0", tk.END).strip()
        if feedback_type and feedback_text:
            messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")  
        else:
            messagebox.showerror("Error", "Please select feedback type and provide feedback text.")  

# Main application entry point
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Apna IT Application")
    root.geometry("600x500")

    root._history = []

    LoginPage(root).pack()

    root.mainloop()
