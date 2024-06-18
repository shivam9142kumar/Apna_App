import tkinter as tk
from tkinter import messagebox

# Base class for all pages in the application
class PageBase:
    def __init__(self, master): 
        self.master = master
        self.__frame = tk.Frame(master)
        self.__frame.pack(pady=20)

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
        super().__init__(master)
        self.username_entry = None
        self.password_entry = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self._PageBase__frame, text="Username:", font=("Helvetica", 14)).pack()  # Increase font size for username label
        self.username_entry = tk.Entry(self._PageBase__frame, font=("Helvetica", 12))  # Increase font size for username entry
        self.username_entry.pack(pady=5)

        tk.Label(self._PageBase__frame, text="Password:", font=("Helvetica", 14)).pack()  # Increase font size for password label
        self.password_entry = tk.Entry(self._PageBase__frame, show='*', font=("Helvetica", 12))  # Increase font size for password entry
        self.password_entry.pack(pady=5)

        tk.Button(self._PageBase__frame, text="Login", command=self.login, font=("Helvetica", 12)).pack(pady=10)  # Increase font size for login button

    def login(self):
        username = self.username_entry.get()  # Get the username entered by the user
        password = self.password_entry.get()  # Get the password entered by the user

        if username == "shubh" and password == "0000":  # Check if the username and password match
            self.destroy()  # Destroy the login page
            ProfilePage(self.master, username).pack()  # Create and display the ProfilePage with username
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")  # Display an error message if the credentials are incorrect

# Profile Page class, inheriting from PageBase
class ProfilePage(PageBase):
    def __init__(self, master, username):
        super().__init__(master)
        self.username = username  # Store the username
        self.create_widgets()

    def create_widgets(self):
        # Welcome message and user information
        tk.Label(self._PageBase__frame, text=f"Welcome, {self.username}!", font=("Helvetica", 16, "bold")).pack(pady=10)  # Increase font size for welcome message
        tk.Label(self._PageBase__frame, text="User Information", font=("Helvetica", 14, "bold")).pack(pady=10)

        # User details section
        tk.Label(self._PageBase__frame, text="Name: Shubh Agrawal", font=("Helvetica", 12)).pack(anchor=tk.W)
        tk.Label(self._PageBase__frame, text="Email: shubh@gmaill.com", font=("Helvetica", 12)).pack(anchor=tk.W)
        tk.Label(self._PageBase__frame, text="Location: Bangalore, INDIA", font=("Helvetica", 12)).pack(anchor=tk.W)

        # Navigation buttons and settings
        tk.Label(self._PageBase__frame, text="Actions", font=("Helvetica", 14, "bold")).pack(pady=10)
        tk.Button(self._PageBase__frame, text="Job Seeking", command=self.show_job_seeking_page, font=("Helvetica", 12)).pack()
        tk.Button(self._PageBase__frame, text="Feedback", command=self.show_feedback_page, font=("Helvetica", 12)).pack()
        tk.Button(self._PageBase__frame, text="Settings", command=self.show_settings, font=("Helvetica", 12)).pack()

        # Navigation buttons
        tk.Button(self._PageBase__frame, text="Logout", command=self.logout, font=("Helvetica", 12)).pack()
        if self.master._history:  # Add 'Go Back' button only if history exists
            tk.Button(self._PageBase__frame, text="Go Back", command=self.go_back, font=("Helvetica", 12)).pack()

    def show_job_seeking_page(self):
        self.navigate_to(JobSeekingPage)  # Navigate to JobSeekingPage

    def show_feedback_page(self):
        self.navigate_to(FeedbackPage)  # Navigate to FeedbackPage

    def navigate_to(self, page_class):
        self.master._history.append(self)  # Add current page to history
        self.destroy()  # Destroy the current page (ProfilePage)
        page_class(self.master).pack()  # Create and display the specified page

    def logout(self):
        self.destroy()  # Destroy the current page (ProfilePage)
        LoginPage(self.master).pack()  # Create and display the LoginPage for logout

    def show_settings(self):
        messagebox.showinfo("Settings", "No settings available in this demo")  # Placeholder for settings functionality

# JobSeekingPage class, inheriting from PageBase
class JobSeekingPage(PageBase):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self._PageBase__frame, text="Job Seeking Page", font=("Helvetica", 16, "bold")).pack()  # Increase font size for heading

        job_list = [
            {"title": "Software Engineer", "company": "Tech Solutions Inc."},
            {"title": "Data Analyst", "company": "Data Insights Co."},
            {"title": "Marketing Manager", "company": "Global Marketing Group"},
        ]

        # Display job listings
        for job in job_list:
            job_frame = tk.Frame(self._PageBase__frame, bd=1, relief=tk.RIDGE)  # Create a frame for each job listing
            job_frame.pack(pady=5, fill=tk.X)

            tk.Label(job_frame, text=f"{job['title']} at {job['company']}", font=("Helvetica", 12)).pack(side=tk.LEFT, padx=10)  # Increase font size for job title and company
            tk.Button(job_frame, text="Apply", command=lambda title=job['title']: self.apply_job(title), font=("Helvetica", 10)).pack(side=tk.RIGHT, padx=10)  # Increase font size for apply button

        # Filter jobs by company
        tk.Label(self._PageBase__frame, text="Filter by Company:", font=("Helvetica", 14, "bold")).pack(pady=10)
        company_filter = tk.StringVar()
        company_filter.set("All")
        company_options = ["All"] + list(set(job['company'] for job in job_list))  # Get unique company names
        tk.OptionMenu(self._PageBase__frame, company_filter, *company_options, command=self.filter_jobs).pack()

    def apply_job(self, job_title):
        # Implement job application logic here 
        messagebox.showinfo("Job Application", f"You have applied for {job_title}.")  # Show confirmation message for job application

    def filter_jobs(self, selected_company):
        # Implement filtering logic based on selected company
        # For demo purposes, just print the selected company
        print(f"Filtering jobs by company: {selected_company}")

# FeedbackPage class, inheriting from PageBase
class FeedbackPage(PageBase):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self._PageBase__frame, text="Feedback Page", font=("Helvetica", 16, "bold")).pack()  # Increase font size for heading

        # Feedback form
        tk.Label(self._PageBase__frame, text="Type of Feedback:", font=("Helvetica", 14)).pack()  # Increase font size for feedback type label
        feedback_type = tk.StringVar()  # Variable to store the selected feedback type
        feedback_type.set("General")  # Set default value for feedback type
        tk.OptionMenu(self._PageBase__frame, feedback_type, "General", "Bug Report", "Feature Request").pack()  # Dropdown menu for selecting feedback type

        tk.Label(self._PageBase__frame, text="Your Feedback:", font=("Helvetica", 14)).pack()  # Increase font size for feedback label
        feedback_entry = tk.Text(self._PageBase__frame, height=5, width=50, font=("Helvetica", 12))  # Increase font size for feedback entry
        feedback_entry.pack()  # Pack the feedback entry widget into the frame

        tk.Button(self._PageBase__frame, text="Submit Feedback", command=lambda: self.submit_feedback(feedback_type.get(), feedback_entry), font=("Helvetica", 12)).pack()  # Increase font size for submit button

        # Additional feedback options
        tk.Label(self._PageBase__frame, text="Additional Options", font=("Helvetica", 14, "bold")).pack(pady=10)
        satisfaction_label = tk.Label(self._PageBase__frame, text="Satisfaction Level:", font=("Helvetica", 12))
        satisfaction_label.pack()
        satisfaction_scale = tk.Scale(self._PageBase__frame, from_=1, to=5, orient=tk.HORIZONTAL, font=("Helvetica", 12))
        satisfaction_scale.pack()

    def submit_feedback(self, feedback_type, feedback_entry):
        feedback_text = feedback_entry.get("1.0", tk.END).strip()  # Get feedback text from the text widget
        if feedback_type and feedback_text:
            messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")  # Show confirmation message for feedback submission
        else:
            messagebox.showerror("Error", "Please select feedback type and provide feedback text.")  # Show error if feedback type or text is empty

# Main application entry point
if __name__ == "__main__":
    root = tk.Tk()  # Create the main application window
    root.title("Apna IT Application")  # Set the title of the window
    root.geometry("600x500")  # Set the initial size of the window

    # Stack to keep track of page history
    root._history = []

    LoginPage(root).pack()  # Create and display the LoginPage

    root.mainloop()  # Start the Tkinter event loop
