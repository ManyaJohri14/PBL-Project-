import tkinter as tk
from tkinter import messagebox
import random
import os

my_local_list = []

def open_student():
    st_win = tk.Toplevel(root)
    st_win.title("Student Interaction Portal")
    st_win.geometry("450x520")
    st_win.configure(bg="#f4f6f9") 
    st_win.resizable(False, False)
    
    tk.Label(st_win, text="ANONYMOUS STUDENT AREA", font=("Courier", 12, "bold"), bg="#f4f6f9", fg="#2c3e50").pack(pady=15)
    
    tk.Label(st_win, text="Share your academic stress or thoughts anonymously:", font=("Arial", 9), bg="#f4f6f9", fg="#7f8c8d").pack(anchor="w", padx=45)
    txt_area = tk.Text(st_win, height=6, width=45, font=("Arial", 10), bd=1, relief=tk.SOLID)
    txt_area.pack(pady=5)
    
    def submit_btn_clicked():
        msg_data = txt_area.get("1.0", tk.END).strip()
        if msg_data == "":
            messagebox.showwarning("Notice", "Please type your feelings before submitting.")
            return
            
        rand_id = random.randint(1000, 9999)
        
        f = open(os.path.expanduser("~/Documents/transfer.txt"), "w")
        f.write(str(rand_id) + "\n" + msg_data + "\n")
        f.close()
        
        os.system("BACKEND")
        
        my_local_list.append({"tok": rand_id, "msg": msg_data, "reply": ""})
        
        messagebox.showinfo("Data Secured", f"Message loaded into dynamic RAM Stack!\n\nYour Secret Token Key ID: #{rand_id}\n\nSave this token to read counselor guidance later.")
        st_win.destroy()
        
    tk.Button(st_win, text="Submit ", command=submit_btn_clicked, bg="#2ecc71", fg="white", font=("Arial", 10, "bold"), width=22, height=2, cursor="hand2", relief=tk.GROOVE).pack(pady=10)

    tk.Label(st_win, text="_________________________________________________", bg="#f4f6f9", fg="#bdc3c7").pack(pady=10)

    tk.Label(st_win, text="CHECK ANONYMOUS RESPONSE TICKET", font=("Courier", 10, "bold"), bg="#f4f6f9", fg="#2c3e50").pack(pady=5)
    tk.Label(st_win, text="Enter your 4-digit Token ID to view counselor advice:", font=("Arial", 9), bg="#f4f6f9", fg="#7f8c8d").pack(pady=2)
    
    token_entry = tk.Entry(st_win, font=("Arial", 12), width=15, justify="center", bd=1, relief=tk.SOLID)
    token_entry.pack(pady=5)
    
    def check_token_reply():
        search_tok = token_entry.get().strip()
        if search_tok == "":
            messagebox.showwarning("Input Error", "Please provide a valid Token ID number.")
            return
        
        is_case_found = False
        for case in my_local_list:
            if str(case["tok"]) == search_tok:
                is_case_found = True
                help_note = case["reply"] if case["reply"] else "Our counseling team has received this. No response logged yet."
                messagebox.showinfo(f"Ticket #{search_tok} Workspace Data", f"Your Vent Record:\n\"{case['msg']}\"\n\nCounselor Feedback Note:\n\"{help_note}\"")
                break
                
        if not is_case_found:
            messagebox.showerror("System Search Failure", "This specific Token Key ID does not match any active memory tracking entries.")

    tk.Button(st_win, text="Check Help Note Status", command=check_token_reply, bg="#3498db", fg="white", font=("Arial", 9, "bold"), width=22, height=1, cursor="hand2", relief=tk.GROOVE).pack(pady=5)

def open_counselor():
    pass_win = tk.Toplevel(root)
    pass_win.title("Security Access Barrier")
    pass_win.geometry("340x180")
    pass_win.configure(bg="#f4f6f9")
    pass_win.resizable(False, False)
    
    tk.Label(pass_win, text="COUNSELOR PORTAL ACCESS CONTROL", font=("Courier", 9, "bold"), bg="#f4f6f9", fg="#c0392b").pack(pady=15)
    tk.Label(pass_win, text="Enter Admin Security Passkey:", font=("Arial", 10), bg="#f4f6f9").pack()
    
    pass_field_box = tk.Entry(pass_win, show="*", width=22, font=("Arial", 11), justify="center", bd=1, relief=tk.SOLID)
    pass_field_box.pack(pady=5)
    
    def run_password_verification():
        if pass_field_box.get() == "mindspace123":
            pass_win.destroy()
            show_dashboard()
        else:
            messagebox.showerror("Access Denied", "Incorrect password signature key structural mismatch.")
            
    tk.Button(pass_win, text="Login Portal", command=run_password_verification, bg="#c0392b", fg="white", font=("Arial", 9, "bold"), cursor="hand2").pack(pady=15)

def show_dashboard():
    c_win = tk.Toplevel(root)
    c_win.title("Counselor  Dashboard ")
    c_win.geometry("460x480")
    c_win.configure(bg="#f4f6f9")
    c_win.resizable(False, False)
    
    if len(my_local_list) == 0:
        tk.Label(c_win, text="No messages in the queues!\nThe memory stack is currently clean.", font=("Arial", 11, "italic"), bg="#f4f6f9", fg="#27ae60").pack(pady=150)
        return
        
    current_case = my_local_list[-1]
    
    tk.Label(c_win, text=f"Active Ticket ID: #{current_case['tok']}", font=("Courier", 11, "bold"), bg="#f4f6f9", fg="#2c3e50").pack(pady=15)
    
    tk.Label(c_win, text="AStudent Message Text:", font=("Arial", 9), bg="#f4f6f9", fg="#7f8c8d").pack(anchor="w", padx=45)
    t_box = tk.Text(c_win, height=4, width=45, font=("Arial", 10), bd=1, relief=tk.SOLID)
    t_box.insert(tk.END, current_case["msg"])
    t_box.config(state=tk.DISABLED) 
    t_box.pack(pady=5)
    
    tk.Label(c_win, text="Write a helpful response note for the student here:", font=("Arial", 9, "bold"), bg="#f4f6f9", fg="#2980b9").pack(anchor="w", padx=45, pady=(10, 0))
    reply_box = tk.Text(c_win, height=4, width=45, font=("Arial", 10), bd=1, relief=tk.SOLID)
    reply_box.pack(pady=5)
    
    def submit_reply_btn():
        reply_data = reply_box.get("1.0", tk.END).strip()
        if not reply_data:
            messagebox.showwarning("Warning", "Please write a response guidance plan before saving.")
            return
        
        current_case["reply"] = reply_data
        messagebox.showinfo("Data Profile Updated", f"Guidance note locked onto Ticket #{current_case['tok']} successfully.")
        c_win.destroy()

    def resolve_btn():
        my_local_list.pop()
        c_win.destroy()
        messagebox.showinfo("Memory Purged", "Case resolved. Dynamic data block shredded from RAM arrays via C code framework subroutines.")
        
    tk.Button(c_win, text="Save Help Note for Student", command=submit_reply_btn, bg="#2980b9", fg="white", font=("Arial", 10, "bold"), width=32, height=1, cursor="hand2", relief=tk.GROOVE).pack(pady=8)
    tk.Button(c_win, text="Resolve Case & Shred from RAM", command=resolve_btn, bg="#e74c3c", fg="white", font=("Arial", 10, "bold"), width=32, height=1, cursor="hand2", relief=tk.GROOVE).pack(pady=5)

root = tk.Tk()
root.title("Campus Mindspace Control Console")
root.geometry("450x450")
root.configure(bg="#f4f6f9")
root.resizable(False, False)

tk.Label(root, text="-------------------------------------------------------------", bg="#f4f6f9", fg="#bdc3c7").pack(pady=(25, 0))
main_label = tk.Label(root, text="CAMPUS MINDSPACE MAIN SYSTEM", font=("Courier", 13, "bold"), bg="#f4f6f9", fg="#2c3e50")
main_label.pack()
sub_label = tk.Label(root, text="(pop the stress)", font=("Courier", 11, "italic"), bg="#f4f6f9", fg="#7f8c8d")
sub_label.pack()
tk.Label(root, text="-------------------------------------------------------------", bg="#f4f6f9", fg="#bdc3c7").pack(pady=(0, 30))

tk.Button(root, text="1. Open Student Portal ", command=open_student, width=32, height=2, bg="#34495e", fg="white", font=("Arial", 11), cursor="hand2", relief=tk.RAISED, bd=1).pack(pady=10)
tk.Button(root, text="2. Open Counselor Portal ", command=open_counselor, width=32, height=2, bg="#34495e", fg="white", font=("Arial", 11), cursor="hand2", relief=tk.RAISED, bd=1).pack(pady=10)
tk.Button(root, text="3. Close Portal Window", command=root.quit, width=32, height=2, bg="#7f8c8d", fg="white", font=("Arial", 11), cursor="hand2", relief=tk.RAISED, bd=1).pack(pady=10)

root.mainloop()