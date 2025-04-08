###====== IT0011 FINAL PROJECT =======### 
####=== TC24 Feel Good BGYO Store ===####         [!] ATTENTION [!]  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  [!]
#####===============================#####            
###==  Agero, Mikhail Gianmarko G.  ==###            If you want to add new items, just use the provided
####= Flaviano, Angel Gaebrielle N. =####            images in our 'itm_img' folder for image upload.
####======   Gison, Yuan Ira   ======####               
####==   Sanchez, Aaron Joshua D.  ==####         [!]  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  [!] ATTENTION [!]


import tkinter as tk ### - //Used for window and widget configuration.//
import dbs as db ### - //This is referencing our database file, allowing the main program to use the database functions.//
import pygame ### - //Used for mp3 handling.//
import os ### - //Used for pathfinding, specifically handling of image.//
from PIL import Image, ImageTk ### - //Used for image handling.//
from tkinter import ttk, messagebox, simpledialog, filedialog, StringVar, IntVar ### - //tkinter library extensions.//

class App:
##========== [SYSTEM INITIALIZATION & MENU PAGE] ==========##
    def __init__(self, root):
        #===== [Main Menu Window & Sytem Initialization] =====# - //Root Window Constructor.//
        self.root = root
        self.root.title("Main Menu")
        self.root.geometry("350x185")
        self.center_window(self.root)
        icon = tk.PhotoImage(file="assets/logo.png")
        self.root.iconphoto(True, icon)

        ##= SFX Loader =## 
        pygame.mixer.init()
        pygame.mixer.music.load("assets/music.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        self.click_sound = pygame.mixer.Sound("assets/click.wav")
        self.click_sound.set_volume(0.5)

        ##= Widget Style =# 
        self.style = ttk.Style()
        self.parent_bg = '#f0f0f0'
        self.style.theme_use('clam')
        self.style.configure('TLabel', background=self.parent_bg, foreground='black')
        self.style.configure('TRadiobutton', background=self.parent_bg, foreground='black')
        self.style.configure('TButton', background='black', foreground='white')
        
        #= Logo =#
        self.logo = Image.open("assets/logo.png")
        self.logo = self.logo.resize((50, 50)) 
        self.logo = ImageTk.PhotoImage(self.logo)

        self.logo_lb = tk.Label(self.root, image=self.logo)
        self.logo_lb.pack()

        #= Other Components =#    
        ttk.Label(self.root, text="Feel Good BGYO Store", font=("Oswald")).pack(pady=10)
        ttk.Button(self.root, text="Vendor's  Panel", command=self.sound(self.Vndr_pg)).pack(pady=5)
        ttk.Button(self.root, text="Customer Login", command=self.sound(self.Lgn_pg)).pack(pady=5)

    def sound(self, func):
        #===== Sound-Click Function =====# - //This Function embeds a clicking sound to all buttons ensuring feedback to users.//
            return lambda: [self.click_sound.play(), func()][-1]

    def center_window(self, win):
        #===== Center Window Function =====# - //This Function automatically centers a page by solving for half of the
        win.update_idletasks()             #     height and width of the monitor and sets it as the x and y position.//
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x = (screen_width - win.winfo_width()) // 2  
        y = (screen_height - win.winfo_height()) // 2
        win.geometry(f"+{x}+{y}")
    
    def back_menu(self, win):
        #===== Back to Menu Button Function =====# - //This Function closes the current window and restores the root menu.//
        win.withdraw()
        self.root.deiconify()

##========== [LOGIN PAGE] ==========##
    def Lgn_pg(self):
        #===== Login Page Initialization =====# - //Initializes the Login Page.//
        self.root.withdraw() ### hides root window
        self.lgn_wn = tk.Toplevel(self.root)
        self.lgn_wn.title("Login Page")
        self.lgn_wn.geometry("335x235")
        self.center_window(self.lgn_wn)
        
        #= Login Icon =#
        self.log = Image.open("assets/login.png")
        self.log = self.log.resize((50, 50)) 
        self.log = ImageTk.PhotoImage(self.log)

        self.log_lb = tk.Label(self.lgn_wn, image=self.log)
        self.log_lb.grid(row=0, column=0, sticky="we", padx=10, pady=5)

        #= Page Label and Back button =#
        ttk.Label(self.lgn_wn, text="Login", font=("Oswald")).grid(row=0, column=1, sticky="we", padx=10, pady=5)
        ttk.Button(self.lgn_wn, text="Back to Menu", command=self.sound(lambda: self.back_menu(self.lgn_wn))).grid(row=0, column=2, sticky="we", padx=10, pady=5)
        
        #= Username Input =#
        ttk.Label(self.lgn_wn, text="Username: ").grid(row=1, column=0, padx=10, pady=10)
        self.usr_inp = ttk.Entry(self.lgn_wn)
        self.usr_inp.grid(row=1, column=1, columnspan=2, sticky="we", padx=10, pady=10) 

        #= Password Input =#
        ttk.Label(self.lgn_wn, text="Password: ").grid(row=2, column=0, padx=10, pady=10)
        self.psw_inp = ttk.Entry(self.lgn_wn, show="*")
        self.psw_inp.grid(row=2, column=1, columnspan=2, sticky="we", padx=10, pady=10)
        
        #= Login Button =#
        lgn_btn = ttk.Button(self.lgn_wn, text="Login", command=self.sound(self.login)) ### activates 'login' Function once clicked.
        lgn_btn.grid(row=3, column=0, columnspan=3, sticky="we", padx=10, pady=10)
        
        #= Sign-Up Hyperlink =#
        tk.Label(self.lgn_wn, text="Don't have an account?, ").grid(row=4, column=1, sticky="e", padx=(10, 0), pady=10)
        hyper = tk.Label(self.lgn_wn, text="click here", fg="blue", cursor="hand2")
        hyper.grid(row=4, column=2, columnspan=2, sticky="w", padx=(0, 3), pady=10)
        hyper.bind("<Button-1>", lambda e: self.Reg_pg()) ### redirects user to 'Registration page' once clicked.
    
    def login(self):
        #===== Login Page Function =====# - //This Function is in charge of the Functionality of the 'Login Page'.//
        username = self.usr_inp.get()
        password = self.psw_inp.get()

        if username == "" or password == "": ### if either username and password is null. 
            messagebox.showwarning("Incomplete Information", "Please enter both username and password.")
        else: ### if all fields are filled in.
            result = db.verify_user(username, password) ### checks in database if user and password is existing and valid.
            if result: ### if result is true, it means that the user exists and login is valid.
                messagebox.showinfo("Login Successful", f"Welcome, {result[1]}! Successfully logged in as {username}.")
                self.Cstmr_pg() ### once successfully logged in, transports user to 'Customer Page'.
            else: ### if user does not exist (possibly from wrong input)
                messagebox.showerror("Login Failed", "Incorrect username or password.")
    
##========== [REGISTRATION PAGE] ==========##
    def Reg_pg(self):
        #===== Registration Page Initialization =====# - //Initializes the Registration page.//
        self.lgn_wn.withdraw()  ### hides login window
        self.reg_pg = tk.Toplevel(self.root)  
        self.reg_pg.title("Registration Page")
        self.reg_pg.geometry("330x315")
        self.center_window(self.reg_pg)

        #= Registration Icon =#
        self.reg = Image.open("assets/register.png")
        self.reg = self.reg.resize((50, 50)) 
        self.reg = ImageTk.PhotoImage(self.reg)

        self.reg_lb = tk.Label(self.reg_pg, image=self.reg)
        self.reg_lb.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        
        #= Page Label and Back button =#
        ttk.Label(self.reg_pg, text="Register", font=("Oswald")).grid(row=0, column=1, sticky="w", padx=10, pady=5)
        ttk.Button(self.reg_pg, text="Back to Menu", command=self.sound(lambda: self.back_menu(self.reg_pg))).grid(row=0, column=2, sticky="we", padx=10, pady=5)

        #= Name Input =#
        ttk.Label(self.reg_pg, text="Name: ").grid(row=1, column=0, sticky="w",padx=10, pady=10)
        self.name_inp = ttk.Entry(self.reg_pg)
        self.name_inp.grid(row=1, column=1, columnspan=2, sticky="we", padx=10, pady=10) 

        #= Address Input =#
        ttk.Label(self.reg_pg, text="Address: ").grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.add_inp = ttk.Entry(self.reg_pg)
        self.add_inp.grid(row=2, column=1, columnspan=2, sticky="we", padx=10, pady=10)

        #= Username Input =#
        ttk.Label(self.reg_pg, text="Username: ").grid(row=3, column=0, sticky="w", padx=10, pady=10)
        self.usr_inp = ttk.Entry(self.reg_pg)
        self.usr_inp.grid(row=3, column=1, columnspan=2, sticky="we", padx=10, pady=10) 

        #= Password Input =#
        ttk.Label(self.reg_pg, text="Password: ").grid(row=4, column=0, sticky="w", padx=10, pady=10)
        self.psw_inp = ttk.Entry(self.reg_pg, show="*")
        self.psw_inp.grid(row=4, column=1, columnspan=2, sticky="we", padx=10, pady=10)

        #= Confirm Password Input =#
        ttk.Label(self.reg_pg, text="Confirm Password: ").grid(row=5, column=0, sticky="w", padx=10, pady=10)
        self.cpsw_inp = ttk.Entry(self.reg_pg, show="*")
        self.cpsw_inp.grid(row=5, column=1, columnspan=2, sticky="we", padx=10, pady=10)

        #= Registration Button =#
        reg_btn = ttk.Button(self.reg_pg, text="Register now", command=self.sound(self.register))
        reg_btn.grid(row=6, column=0, columnspan=3, sticky="we", padx=10, pady=10) ### activates 'register' function once clicked.

    def register(self):
        #===== Registration Page Function =====# - //This Function is in charge of the Functionality of the 'Registration Page'.//
        usr_nm = self.name_inp.get()
        usr_add = self.add_inp.get()
        usr_inp = self.usr_inp.get()
        usr_pass = self.psw_inp.get()
        usr_confp = self.cpsw_inp.get() ### gets all information from the 'Registration page' inputs.

        if usr_nm == "" or usr_add == "" or usr_inp == "" or usr_pass == "" or usr_confp == "": ### if a null value was detected.
            messagebox.showwarning("Incomplete Information", "Please fill in all fields.")
        else: ### if all fields are filled in.
            if usr_confp != usr_pass: ### if there are no null values, but password and confirm password are not equal.
                messagebox.showwarning("Passwords not matched","Entered passwords are not the same, please try again.")
            else: ### if no errors. 
                result = db.register_user(usr_nm, usr_add, usr_inp, usr_pass) ### transfers data to 'dbs.py' to be checked.
                messagebox.showinfo("System", result) ### shows result of registration (either error or successful). 

##========== [ITEM MANAGEMENT/VENDOR'S PAGE] ==========##
    def Vndr_pg(self):
        #===== Vendor's Page Initialization =====# - //Initializes the 'Vendor's page' which contains the item management panel.//
        self.root.withdraw()
        self.vndr_wn = tk.Toplevel(self.root)
        self.vndr_wn.title("Vendor's Panel")
        self.vndr_wn.geometry("370x700")
        self.center_window(self.vndr_wn)
        
        #= Item Management Icon =#
        self.itm = Image.open("assets/inventory.png")
        self.itm = self.itm.resize((50, 50)) 
        self.itm = ImageTk.PhotoImage(self.itm)

        self.itm_lb = tk.Label(self.vndr_wn, image=self.itm)
        self.itm_lb.grid(row=0, column=0, pady=5)

        #= Page Label and Back button =#
        ttk.Label(self.vndr_wn, text="Item Management", font=("Oswald")).grid(row=0, column=1, columnspan=2, sticky="w", padx=10, pady=5)
        ttk.Button(self.vndr_wn, text="Back to Menu", command=self.sound(lambda: self.back_menu(self.vndr_wn))).grid(row=0, column=3, sticky="we", padx=10, pady=5)

        #= Item ID Input  =#
        ttk.Label(self.vndr_wn, text="Item ID: ").grid(row=1, column=0, sticky="w",padx=10, pady=10)
        self.itm_id = ttk.Entry(self.vndr_wn)
        self.itm_id.grid(row=1, column=1, columnspan=3, sticky="we", padx=10, pady=10)

        #= Item Name Input =#
        ttk.Label(self.vndr_wn, text="Item Name: ").grid(row=2, column=0, sticky="w",padx=10, pady=10)
        self.itm_name = ttk.Entry(self.vndr_wn)
        self.itm_name.grid(row=2, column=1, columnspan=3, sticky="we", padx=10, pady=10)

        #= Item Stock Input =#
        ttk.Label(self.vndr_wn, text="Item Stock: ").grid(row=3, column=0, sticky="w",padx=10, pady=10)
        self.itm_stock = ttk.Entry(self.vndr_wn)
        self.itm_stock.grid(row=3, column=1, columnspan=3, sticky="we", padx=10, pady=10)

        #= Item Price Input =#
        ttk.Label(self.vndr_wn, text="Item Price: ").grid(row=4, column=0, sticky="w",padx=10, pady=10)
        self.itm_price = ttk.Entry(self.vndr_wn)
        self.itm_price.grid(row=4, column=1, columnspan=3, sticky="we", padx=10, pady=10)

        #= Item Image Input =#
        ttk.Label(self.vndr_wn, text="Image Preview: ").grid(row=5, column=0, sticky="w",padx=10, pady=10)
        self.itm_img = ttk.Button(self.vndr_wn, text="Upload Image", command=self.upload_image)
        self.itm_img.grid(row=5, column=1, columnspan=3, sticky="we", padx=10, pady=10)

        #= Category Radio Buttons =#
        self.category = tk.StringVar()
        self.category.set("Merch") ### default selection for radio buttons.

        self.category_lb = ttk.Label(self.vndr_wn, text="Select category:")
        self.category_lb.grid(row=6, column=0, sticky="w",padx=10, pady=10)
        self.merch_radio = ttk.Radiobutton(self.vndr_wn, text="Merch", variable=self.category, value="Merch")
        self.merch_radio.grid(row=6, column=1, pady=10)
        self.albums_radio = ttk.Radiobutton(self.vndr_wn, text="Albums", variable=self.category, value="Album")
        self.albums_radio.grid(row=6, column=2, pady=10)
        self.tickets_radio = ttk.Radiobutton(self.vndr_wn, text="Tickets", variable=self.category, value="Ticket")
        self.tickets_radio.grid(row=6, column=3, pady=10)

        #= Insert Item Button =#
        nsrt_btn = ttk.Button(self.vndr_wn, text="Insert Item", command=self.sound(self.insert_item))
        nsrt_btn.grid(row=7, column=1, columnspan=2, sticky="we", padx=10, pady=10)

        #= Update Item Button =#
        upd_btn = ttk.Button(self.vndr_wn, text="Update Item", command=self.sound(self.update_item))
        upd_btn.grid(row=8, column=1, columnspan=2, sticky="we", padx=10, pady=10)

        #= Delete Item Button =#
        del_btn = ttk.Button(self.vndr_wn, text="Delete Item", command=self.sound(self.delete_item))
        del_btn.grid(row=9, column=1, columnspan=2, sticky="we", padx=10, pady=10)

        #= Show Items Button =#
        shw_btn = ttk.Button(self.vndr_wn, text="Show Items", command=self.sound(self.show_items))
        shw_btn.grid(row=10, column=1, columnspan=2, sticky="we", padx=10, pady=10)

        #= Item Listbox =#
        self.itm_lst = tk.Listbox(self.vndr_wn)
        self.itm_lst.grid(row=11, column=0, columnspan=4, sticky="we", padx=10, pady=10)
        self.itm_lst.bind("<<ListboxSelect>>", self.load_item_to_inputs)

    def clear_inputs(self):
            #===== Clear Entry Function =====# - //Clears the Entries at the 'Vendor's Page' every action/event for easier queries.//
            self.itm_id.delete(0, tk.END)
            self.itm_name.delete(0, tk.END)
            self.itm_stock.delete(0, tk.END)
            self.itm_price.delete(0, tk.END)

    def upload_image(self):
        #===== Upload Image Button Function =====# - //Extracts pathway from user-prompted image.//
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")]) ### checks whether image format
        if file_path: ### if file is existing
            self.image_path = file_path
            messagebox.showinfo("Image Uploaded", "Image successfully selected.")

    def insert_item(self):
        #===== Insert Button Function  =====# - //
        itm_id = self.itm_id.get()
        name = self.itm_name.get()
        stock = self.itm_stock.get()
        price = self.itm_price.get()
        category = self.category.get()

        #= Empty Field Checker =#
        if not (itm_id and name and stock and price):
            messagebox.showwarning("Incomplete Data", "Please fill all item details.")
            return

        #= Stock & Price Validator =#
        try:
            stock = int(stock)
            price = float(price)
        except ValueError:
            messagebox.showwarning("Invalid Data", "Stock must be an integer and Price must be a number.")
            return

        if stock <= 0 or price <= 0:
            messagebox.showwarning("Invalid Values", "Stock and Price must be greater than 0.")
            return

        if not hasattr(self, 'image_path') or not self.image_path:
            messagebox.showwarning("Missing Image", "Please upload an image before inserting the item.")
            return

        #= Database Inserter =#
        result = db.add_item(itm_id, name, stock, price, category, self.image_path)
        messagebox.showinfo("Insert Item", result)

        self.show_items()
        self.clear_inputs()

    def update_item(self):
        #===== Update Item Button Function =====# - // 
        itm_id = self.itm_id.get()
        name = self.itm_name.get()
        stock = self.itm_stock.get()
        price = self.itm_price.get()
        category = self.category.get()

        #= Empty Field Checker =#
        if not (itm_id and name and stock and price):
            messagebox.showwarning("Incomplete Data", "Please fill all item details.")
            return

        #= Price & Stock Validator =#
        try:
            stock = int(stock)
            price = float(price)
        except ValueError:
            messagebox.showwarning("Invalid Data", "Stock must be an integer and Price must be a number.")
            return

        if stock <= 0 or price <= 0:
            messagebox.showwarning("Invalid Values", "Stock and Price must be greater than 0.")
            return

        #= Image Path Validator =#
        if not hasattr(self, 'image_path') or not self.image_path:
            messagebox.showwarning("Missing Image", "Please upload an image before updating the item.")
            return

        #= Database Updater =#
        result = db.update_item(itm_id, name, stock, price, category, self.image_path)
        messagebox.showinfo("Update Item", result)
        self.show_items()
        self.clear_inputs()

    def delete_item(self):
        #===== Delete Item Button Function =====# - //
        itm_id = self.itm_id.get()

        #= Item Existence Checker =#
        if not itm_id:
            messagebox.showwarning("Missing Item ID", "Please enter the Item ID to delete.")
            return
        
        existing_item = db.get_item_by_id(itm_id)
        if not existing_item:
            messagebox.showerror("Delete Item", f"Item with ID '{itm_id}' does not exist.")
            return

        #= Deletion Confirmation =#
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete Item ID: {itm_id}?")
        if not confirm:
            return

        #= Database Deleter =#
        result = db.delete_item(itm_id)
        messagebox.showinfo("Delete Item", result)
        self.show_items()
        self.clear_inputs()

    def show_items(self):
        #===== Show Items Button Function =====# - //
        self.itm_lst.delete(0, tk.END)
        items = db.get_items()
        
        if not items:
            self.itm_lst.insert(tk.END, "No items found.")
        else:
            for itm in items:
                display_text = f"ID: {itm[0]} | Name: {itm[1]} | Stock: {itm[2]} | Price: ₱{itm[3]} | Category: {itm[4]}"
                self.itm_lst.insert(tk.END, display_text)

    def load_item_to_inputs(self, event):
            #===== Item Management Listbox Selection Function =====# - //Loads the selected item in the listbox to be altered using 
                                                                   #     delete or update buttons.//
            selection = self.itm_lst.curselection() ### whichever the user selects on the listbox.
            if not selection: ### if no selection.
                return
            selected_text = self.itm_lst.get(selection[0]) ### Selects the string of listbox choice.
            
            #= Data initialization =# - //Stores each data from the string of listbox choice to their own variable.//
            parts = selected_text.split(" | ")
            itm_id = parts[0].split(": ")[1]
            name = parts[1].split(": ")[1]
            stock = parts[2].split(": ")[1]
            price = parts[3].split(": ")[1].replace("₱", "")
            category = parts[4].split(": ")[1]

            #= Data Insertion =# - //After clearing, it would load all data in entry fields.//
            self.clear_inputs()
            self.itm_id.insert(0, itm_id)
            self.itm_name.insert(0, name)
            self.itm_stock.insert(0, stock)
            self.itm_price.insert(0, price)
            self.category.set(category)

            #= Image Loader =# - //Loads the image path for possible revisions/updates.//
            item_data = db.get_item_by_id(itm_id)
            if item_data: ### if item_data exists 
                self.image_path = item_data[5] if item_data[5] else ""  ### it retains the value if item_data[5] does not
                                                                    #       hold a 'NULL' or 'None' value, otherwise it 
                                                                    #       would be stored as empty string. 
            else: ### if item_data does not exist
                self.image_path = ""  ### automatically sets the image_path as empty string.

##========== [SHOP/CUSTOMER'S PAGE] ==========##
    def Cstmr_pg(self):
        #===== Customer/Shopping Page Initialization =====# - //
        self.lgn_wn.withdraw()
        self.cstmr_wn = tk.Toplevel(self.root)  
        self.cstmr_wn.title("Feel Good BGYO Store")
        self.cstmr_wn.geometry("510x530")
        self.center_window(self.cstmr_wn)

        self.logo_lb = tk.Label(self.cstmr_wn, image=self.logo)
        self.logo_lb.grid(row=0, column=0, pady=10)
        
        #= Page Label and Back button =#
        ttk.Label(self.cstmr_wn, text=f"Hey, {self.usr_inp.get()}! Ready to shine like a star?", font=("Oswald")).grid(row=0, column=1, columnspan=2, sticky="w", pady=5)

        self.banner = Image.open("assets/banner.png")
        self.banner = self.banner.resize((445, 208)) 
        self.banner = ImageTk.PhotoImage(self.banner)

        self.banner_lb = tk.Label(self.cstmr_wn, image=self.banner)
        self.banner_lb.grid(row=2, column=0, columnspan=4, sticky="we", pady=5)

        self.category_var = StringVar()
        self.category_var.set("Merch") 
        self.category_label = ttk.Label(self.cstmr_wn, text="Select Category:")
        self.category_label.grid(row=3, column=1, sticky="e", padx=10, pady=10)
        self.category_options = ["Merch", "Album", "Ticket"]
        self.category_dropdown = ttk.OptionMenu(self.cstmr_wn, self.category_var, self.category_var.get(), *self.category_options)
        self.category_dropdown.grid(row=3, column=2, sticky="w", padx=10, pady=10)

        ttk.Button(self.cstmr_wn, text="Search", command=self.sound(self.show_item_cstm)).grid(row=3, column=3, sticky="we", padx=10, pady=5)

        ttk.Button(self.cstmr_wn, text="Logout", command=self.sound(lambda: self.back_menu(self.cstmr_wn))).grid(row=0, column=3, sticky="we", padx=10, pady=5)

        #= Item Listbox =#
        self.itm_lst = tk.Listbox(self.cstmr_wn)
        self.itm_lst.grid(row=6, column=0, columnspan=4, sticky="we", padx=10, pady=10)
        self.itm_lst.bind("<<ListboxSelect>>", self.load_items)

    def show_item_cstm(self):
        #===== Search Bar Button Function =====# - //
                self.itm_lst.delete(0, tk.END)
                items = db.get_items()  
                category_selected = self.category_var.get()  
                filtered_items = [itm for itm in items if itm[4] == category_selected]  

                if not filtered_items:
                    self.itm_lst.insert(tk.END, "No items found.")
                else:
            
                    for itm in filtered_items:
                        stock = int(itm[2])
                        if stock <= 0:
                            display_text = f"ID: {itm[0]} | Name: {itm[1]} | OUT OF STOCK | Price: ₱{itm[3]} | Category: {itm[4]}"
                        else:
                            display_text = f"ID: {itm[0]} | Name: {itm[1]} | Stock: {stock} | Price: ₱{itm[3]} | Category: {itm[4]}"
                        self.itm_lst.insert(tk.END, display_text)
    
##========== [CHECKOUT WINDOW] ==========##
    def load_items(self, event):
        #===== Store Item Listbox Selection Function =====#
        selection = event.widget.curselection()
        if not selection:
            return

        item_text = event.widget.get(selection[0])
        if item_text == "No items found.":  
            return

        item_id = int(item_text.split("|")[0].split(":")[1].strip())
        itm = db.get_item_by_id(item_id)

        item_win = tk.Toplevel(self.cstmr_wn)
        item_win.title(f"Item Details - {itm[1]}")
        item_win.geometry("400x440")
        self.center_window(item_win)

        image_frame = tk.LabelFrame(item_win, text="Item Photo", padx=10, pady=10)
        image_frame.pack(pady=10)
        img_path = itm[5]

        try: ### attempt to load the image, fall back if not found
            if img_path and os.path.exists(img_path):
                img = Image.open(img_path)
            else:
                img = Image.open("assets/placeholder.png")  ### provide a safe fallback
        except FileNotFoundError:
            img = Image.open("assets/placeholder.png")  ### safe fallback if the image is missing

        img = img.resize((200, 200))
        img = ImageTk.PhotoImage(img)
        
        self.item_img_label = tk.Label(image_frame, image=img, bg="white", width=200, height=200, relief="solid", bd=1)
        self.item_img_label.image = img  ### Prevent garbage collection
        self.item_img_label.pack()

        info_frame = tk.Frame(item_win)
        info_frame.pack(pady=5)

        tk.Label(info_frame, text=f"Name: {itm[1]}").pack()
        tk.Label(info_frame, text=f"Stock: {itm[2]}").pack()
        tk.Label(info_frame, text=f"Price: ₱{itm[3]}").pack()
        tk.Label(info_frame, text=f"Category: {itm[4]}").pack()

        btn_frame = tk.Frame(item_win)
        btn_frame.pack(pady=20)

        ttk.Button(btn_frame, text="Buy Now", command=lambda: self.sound(self.buy_item(itm))).pack(side="left", padx=10)
    
    def buy_item(self, selected_item):
        #===== Buy Now Button Function ======# - // //
        item_id = selected_item[0]
        name = selected_item[1]
        category = selected_item[4]
        price = float(selected_item[3])
        stock = int(selected_item[2])

        if stock <= 0:
            messagebox.showerror("Out of Stock", "This item is currently out of stock.")
            return

        while True:
            qty = simpledialog.askinteger("Quantity", f"Enter quantity to purchase (Available: {stock}):", parent=self.cstmr_wn)
            if qty is None:
                return  ### user cancelled
            if qty <= 0:
                messagebox.showwarning("Invalid Quantity", "Please enter a valid quantity greater than 0.")
                continue  ### retry
            if qty > stock:
                messagebox.showwarning("Stock Exceeded", f"Only {stock} items available.")
                continue  ### retry
            break  

        total = qty * price
        while True:
            payment = simpledialog.askfloat("Payment", f"The total price is ₱{total:.2f}. Please enter payment:", parent=self.cstmr_wn)
            if payment is None:
                return 
            if payment < total:
                messagebox.showerror("Insufficient Payment", "Payment is not enough.")
            else:
                break 

        change = payment - total

        user_info = db.get_user_by_username(self.usr_inp.get())
        if user_info:
            fullname = user_info[1]    
            address = user_info[2]     
            username = user_info[0]    
        else:
            fullname = "N/A"
            address = "N/A"
            username = self.usr_inp.get()

        #= Stock Updater =#
        new_stock = stock - qty
        image_path = selected_item[5]
        db.update_item(item_id, name, new_stock, price, category, image_path)

        messagebox.showinfo("Purchase Successful", f"Checkout successful, please check your receipt.")

        #= Receipt Generator =#
        with open("receipt.txt", "a") as f:
            f.write("\n###============ RECEIPT =============###\n")
            f.write("####===== Feel Good BGYO Store =====####\n")
            f.write("========================================\n")
            f.write(f"Username: {username}\n")
            f.write(f"Full Name: {fullname}\n")
            f.write(f"Address: {address}\n")
            f.write(f"Item Purchased: {name}\n")
            f.write(f"Quantity: {qty}\n")
            f.write(f"Total Price: PHP{total:.2f}\n")
            f.write(f"Payment: PHP{payment:.2f}\n")
            f.write(f"Change: PHP{change:.2f}\n")
            f.write("========================================\n")
            f.write("Thank you for shopping!\n")

        self.show_item_cstm()  ### Refresh items in the listbox

###========== [MAIN CODE] ==========### - //Creates an instance of the Application.//
root = tk.Tk()
app = App(root)
root.mainloop() 
