import tkinter as tk
from tkinter import messagebox
import BackEnd  # Ensure this module is available in your working directory

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
        user = BackEnd.userInfo(username)

        if user:
            if password == user[-1]:
                messagebox.showinfo("Success", "Login Successful!")
                self.show_loading_page()
            else:
                messagebox.showerror("Error", "Invalid password.")
        else:
            messagebox.showerror("Error", "Invalid username.")

    def show_loading_page(self):
        messagebox.showinfo("Loading", "Loading page...")

    def sign_up(self):
        self.master._history.append(self)
        self.destroy()
        SignUpPage(self.master).pack()

class SignUpPage(PageBase):
    def __init__(self, master):
        super().__init__(master, bg_color='#f0f0f0')
        self.username_entry = None
        self.password_entry = None
        self.confirm_password_entry = None
        self.email_entry = None
        self.skills_entry = None
        self.phone_entry = None
        self.degree_entry = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self._PageBase__frame, text="Sign Up", font=("Helvetica", 16, "bold"), bg='#f0f0f0').pack(pady=10)

        tk.Label(self._PageBase__frame, text="Username:", font=("Helvetica", 14), bg='#f0f0f0').pack()
        self.username_entry = tk.Entry(self._PageBase__frame, font=("Helvetica", 12))
        self.username_entry.pack(pady=5)

        tk.Label(self._PageBase__frame, text="Email:", font=("Helvetica", 14), bg='#f0f0f0').pack()
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

        BackEnd.addData(username, email, skills, phone, degree, password)
        messagebox.showinfo("Success", "User registered successfully!")
        self.master._history.pop()
        self.destroy()
        LoginPage(self.master).pack()

    def cancel(self):
        self.go_back()

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Application")
        self.geometry("400x400")
        self.configure(bg='#ffffff')
        self._history = []
        LoginPage(self).pack()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
