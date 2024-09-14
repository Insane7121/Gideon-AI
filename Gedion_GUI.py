import threading
import tkinter as tk
from tkinter import messagebox

import Gedion  # Importing functions from Gedion.py


class GedionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gedion - Personal Assistant")
        self.root.geometry("400x400")
        
        # Create Widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Create Title Label
        title_label = tk.Label(self.root, text="Gedion - Personal Assistant", font=("Arial", 18, "bold"))
        title_label.pack(pady=10)

        # Create Buttons for Each Function
        greet_button = tk.Button(self.root, text="Greet Me", command=self.greet_user, width=20)
        greet_button.pack(pady=10)

        wiki_button = tk.Button(self.root, text="Search Wikipedia", command=self.search_wikipedia, width=20)
        wiki_button.pack(pady=10)

        time_button = tk.Button(self.root, text="Tell Me the Time", command=self.tell_time, width=20)
        time_button.pack(pady=10)

        email_button = tk.Button(self.root, text="Send Email", command=self.send_email, width=20)
        email_button.pack(pady=10)

        open_youtube_button = tk.Button(self.root, text="Open YouTube", command=self.open_youtube, width=20)
        open_youtube_button.pack(pady=10)

    def greet_user(self):
        # Use threading to prevent the GUI from freezing
        threading.Thread(target=Gedion.wishMe).start()

    def search_wikipedia(self):
        # Open a pop-up to enter search query
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Wikipedia")
        search_window.geometry("300x150")
        
        # Label and Entry for Wikipedia Query
        search_label = tk.Label(search_window, text="Enter a search term:")
        search_label.pack(pady=10)
        
        search_entry = tk.Entry(search_window, width=30)
        search_entry.pack(pady=5)
        
        def start_search():
            query = search_entry.get()
            if query:
                threading.Thread(target=self.wikipedia_search_thread, args=(query,)).start()
            search_window.destroy()

        search_button = tk.Button(search_window, text="Search", command=start_search)
        search_button.pack(pady=10)
        
    def wikipedia_search_thread(self, query):
        # Running Wikipedia search from Gedion.py
        Gedion.speak(f"Searching Wikipedia for {query}")
        result = Gedion.wikipedia.summary(query, sentences=2)
        messagebox.showinfo("Wikipedia Result", result)
        Gedion.speak(result)
    
    def tell_time(self):
        threading.Thread(target=Gedion.wishMe).start()

    def send_email(self):
        # Open a pop-up to get email details
        email_window = tk.Toplevel(self.root)
        email_window.title("Send Email")
        email_window.geometry("400x300")
        
        # Labels and Entry for Email Details
        email_label = tk.Label(email_window, text="Recipient's Email:")
        email_label.pack(pady=5)
        
        email_entry = tk.Entry(email_window, width=40)
        email_entry.pack(pady=5)
        
        content_label = tk.Label(email_window, text="Email Content:")
        content_label.pack(pady=5)
        
        content_text = tk.Text(email_window, height=10, width=40)
        content_text.pack(pady=5)
        
        def start_sending_email():
            recipient_email = email_entry.get()
            content = content_text.get("1.0", tk.END)
            if recipient_email and content:
                threading.Thread(target=self.email_thread, args=(recipient_email, content)).start()
            email_window.destroy()

        send_button = tk.Button(email_window, text="Send Email", command=start_sending_email)
        send_button.pack(pady=10)
    
    def email_thread(self, recipient_email, content):
        try:
            Gedion.sendEmail(recipient_email, content)
            messagebox.showinfo("Email", "Email sent successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send email: {e}")
    
    def open_youtube(self):
        threading.Thread(target=Gedion.webbrowser.open, args=("https://www.youtube.com",)).start()

# Running the Tkinter GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = GedionGUI(root)
    root.mainloop()
