import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import PhotoImage

class AudioApp:
    def __init__(self):
        self.root = None
        self.is_on = False
        self.volume_entry = None
        self.volume = None
        self.bold_font = None 
        self.processor = None
        
        
    def create_window(self):
        self.root = tk.Tk()
        self.root.title("EQLZR")
        self.setup()
        return self.root
    

    def setup(self):
        self.root.geometry("800x600") # bigger size
        self.root.configure(bg="#202f6e") # hexadecimal value for royal blue background
        
        self.bold_font = font.Font(family="Courier New", size=34, weight="bold")
        # Title label design
        highlightFont = font.Font(family="Courier New", size=60, weight="bold")
        # Text and title 
       
        # Top border
        top_frame = tk.Frame(self.root, bg="#7b84a8", height = 50)
        top_frame.pack(fill="x")
        #======================================
        title = tk.Label(self.root, text="EQLZR", font=highlightFont,fg="#00BFFF", bg="#202f6e")
        title.pack(pady=(25,15)) #use pack here
        
        self.volume_label()
        self.on_off_switch()
        
    
    def volume_label(self):
        # Input to take in
        volume_label = tk.Label(self.root, text="Enter Volume (1-100):", bg="#202f6e", foreground="#7b84a8", font=self.bold_font) # label for input
        volume_label.pack()
        
        vcmd = (self.root.register(self.validate_volume_input), '%P')
        self.volume_entry = tk.Entry(self.root, justify="center", font=("Courier New", 36)) # input label
        self.volume_entry.insert(0, "50") # default set to 50%
        self.volume_entry.pack(pady=(25,15))
    
    def validate_volume_input(self, new_text):
        if new_text == "":  # Allow empty field temporarily
            return True
        try:
            return 1 <= int(new_text) <= 100
        except ValueError:
            return False

    def set_processor(self, processor):
        self.processor = processor 
    
    # On/Off Switch
    def on_off_switch(self):
    # Add Title
        self.root.title('EQLZR')
 
    # Add Geometry
        self.root.geometry("150x100")
 
    # Create Label
        my_label = tk.Label(self.root, 
        text = "EQLZR Is Off", 
        fg = "#252b57", bg = "#d1dfff",
        font=self.bold_font)
 
        my_label.pack(pady = 20)
     
    # Define our switch function
        def switch():
    # Determine is on or off
            if self.is_on:
                my_label.config(text = "EQLZR is Off", fg = "#252b57", bg = "#d1dfff")
                on_button.config(text="OFF", font=self.bold_font) 
                self.is_on = False
            else:
                my_label.config(text = "EQLZR is On!", fg = "green", bg = "#d1dfff")
                on_button.config(text="ON", font=self.bold_font) 
                self.is_on = True
            
            if self.processor:
                self.processor.process_audio()
    
# Create A Button
        on_button = tk.Button(self.root, text='OFF', bg='#00BFFF', font=self.bold_font, fg='#000080', command = switch)
        on_button.pack(pady = 80)
        return self.is_on
    
    def get_is_on(self):
        return self.is_on
    
    def get_volume(self):
        try:
            vol = int(self.volume_entry.get())
            vol = max(1, min(100, vol))
            if vol == 1:
                return -30
            else:
                return (0.25 * vol) - 30
        except:
            return -30
    
    
    
   
    
    
    
    
    


