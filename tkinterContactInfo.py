import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Manager")

        self.contacts = []
        self.selected_contact = None

        self.name_label = tk.Label(master, text="NAME:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(master, text="PHONE:")
        self.phone_label.grid(row=1, column=0)
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=1, column=1)

        self.email_label = tk.Label(master, text="EMAIL:")
        self.email_label.grid(row=2, column=0)
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=2, column=1)

        self.add_button = tk.Button(master, text="ADD CONTACT", command=self.add_contact)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.contacts_listbox = tk.Listbox(master, width=40, height=10)
        self.contacts_listbox.grid(row=4, column=0, columnspan=2)

        self.view_button = tk.Button(master, text="VIEW CONTACT", command=self.view_contact)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=5)

        self.edit_button = tk.Button(master, text="EDIT CONTACT", command=self.edit_contact)
        self.edit_button.grid(row=6, column=0, columnspan=2, pady=5)

        self.delete_button = tk.Button(master, text="DELETE CONTACT", command=self.delete_contact)
        self.delete_button.grid(row=7, column=0, columnspan=2, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if name and phone and email:
            contact = {'Name': name, 'Phone': phone, 'Email': email}
            self.contacts.append(contact)
            self.contacts_listbox.insert(tk.END, name)
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter all contact details.")

    def view_contact(self):
        if self.selected_contact:
            messagebox.showinfo("Contact Details", f"Name: {self.selected_contact['Name']}\nPhone: {self.selected_contact['Phone']}\nEmail: {self.selected_contact['Email']}")
        else:
            messagebox.showerror("Error", "Please select a contact.")

    def edit_contact(self):
        if self.selected_contact:
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()

            if name and phone and email:
                index = self.contacts.index(self.selected_contact)
                self.contacts[index] = {'Name': name, 'Phone': phone, 'Email': email}
                self.contacts_listbox.delete(index)
                self.contacts_listbox.insert(index, name)
                self.clear_entries()
            else:
                messagebox.showerror("Error", "Please enter all contact details.")
        else:
            messagebox.showerror("Error", "Please select a contact.")

    def delete_contact(self):
        if self.selected_contact:
            index = self.contacts.index(self.selected_contact)
            self.contacts.pop(index)
            self.contacts_listbox.delete(index)
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please select a contact.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def select_contact(self, event):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            self.selected_contact = self.contacts[index]
            self.display_selected_contact()

    def display_selected_contact(self):
        self.clear_entries()
        self.name_entry.insert(tk.END, self.selected_contact['Name'])
        self.phone_entry.insert(tk.END, self.selected_contact['Phone'])
        self.email_entry.insert(tk.END, self.selected_contact['Email'])

def main():
    root = tk.Tk()
    contact_manager = ContactManager(root)
    contact_manager.contacts_listbox.bind('<<ListboxSelect>>', contact_manager.select_contact)
    root.mainloop()

if __name__ == "__main__":
    main()
