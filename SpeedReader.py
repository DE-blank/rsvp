import tkinter as tk
from tkinter import ttk

wpm = 400
current_index = 0
timer_id = None

def run(event=None):
    global wpm, current_index, timer_id
    input_frame.pack_forget()
    control_frame.pack_forget()

    text = text_input.get("1.0", tk.END).strip()
    words = text.split()
    
    style = ttk.Style()
    style.theme_use('clam') # 'clam' erlaubt abgerundete Formen und Farben
    style.configure("white.Horizontal.TProgressbar", 
                    troughcolor='black',    # Hintergrund des Balkens schwarz
                    background='white',     # Fortschritt weiß
                    bordercolor='black',    # Randfarbe schwarz für nahtlosen Übergang
                    lightcolor='white',     # Glanz-Effekt weiß
                    darkcolor='white',      # Schatten-Effekt weiß
                    thickness=15)           # Etwas schlanker für die "Form"
    
    progress = ttk.Progressbar(root, maximum=len(words), mode='determinate', length=400, style="white.Horizontal.TProgressbar")
    progress.pack(pady=10)
    
    display_label = tk.Label(root, text="", font=("Helvetica", 40))
    display_label.pack(expand=True)

    # Container für die Buttons, um grid() nutzen zu können
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    def quit_reading(event=None):
        nonlocal display_label, button_frame, progress
        if timer_id:
            root.after_cancel(timer_id)
        display_label.destroy()
        button_frame.destroy()
        progress.destroy()
        # Tastenkürzel für das Lesen entfernen
        root.unbind('<space>')
        root.unbind('<Left>')
        root.unbind('<Right>')
        root.unbind('<Escape>')
        # Enter-Taste wieder für Start binden
        root.bind('<Return>', run)
        restore_widgets()

    quit_button = tk.Button(button_frame, text="Quit", command=quit_reading, width=10, height=2)
    quit_button.grid(row=0, column=0, padx=10)
    
    def toggle_pause(event=None):
        global current_index, timer_id
        if pp_button.config('text')[-1] == "||":
            pp_button.config(text=">")
            if timer_id:
                root.after_cancel(timer_id)
                timer_id = None
        else:
            pp_button.config(text="||")
            show_word(current_index)

    pp_button = tk.Button(button_frame, text="||", command=toggle_pause, width=10, height=2)
    pp_button.grid(row=0, column=1, padx=10)

    def go_back(event=None):
        global current_index, timer_id
        if timer_id:
            root.after_cancel(timer_id)
        current_index = max(0, current_index - 5)
        if current_index < len(words):
            display_label.config(text=words[current_index])
        if pp_button.config('text')[-1] == "||":
            show_word(current_index)
            
        progress['value'] = current_index

    def go_forward(event=None):
        global current_index, timer_id
        if timer_id:
            root.after_cancel(timer_id)
        current_index = min(len(words) - 1, current_index + 5)
        if current_index < len(words):
            display_label.config(text=words[current_index])
        if pp_button.config('text')[-1] == "||":
            show_word(current_index)
            
        progress['value'] = current_index

    back_button = tk.Button(button_frame, text="<<-", command=go_back, width=10, height=2)
    back_button.grid(row=0, column=2, padx=10)

    forward_button = tk.Button(button_frame, text="->>", command=go_forward, width=10, height=2)
    forward_button.grid(row=0, column=3, padx=10)
    
    # Tastenkürzel während des Lesens
    root.bind('<space>', toggle_pause)
    root.bind('<Left>', go_back)
    root.bind('<Right>', go_forward)
    root.bind('<Escape>', quit_reading)
    # Während des Lesens soll Enter nichts neu starten
    root.unbind('<Return>')

    try:
        current_wpm = int(wpm_entry.get())
        if current_wpm <= 0:
            current_wpm = 300
    except:
        current_wpm = 300
    delay = int(60000 / current_wpm)  
    
    def show_word(index):
        global current_index, timer_id
        current_index = index
        if index < len(words):
            display_label.config(text=words[index])
            timer_id = root.after(delay, lambda: show_word(index + 1))
            progress['value'] = index + 1
        else:
            quit_reading()

    show_word(0)

def clear_text():
    text_input.delete("1.0", tk.END)

def restore_widgets():
    input_frame.pack(pady=10)
    control_frame.pack(pady=10)

# Hauptfenster 
root = tk.Tk()
root.title("Speed Reader")
root.geometry("800x600")  

root.lift()
root.focus_force()

# Enter-Taste für Start binden
root.bind('<Return>', run)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)
text_input = tk.Text(input_frame, height=10, width=60, font=("Helvetica", 14))
text_input.pack()

control_frame = tk.Frame(root)
control_frame.pack(pady=10)

wpm_label = tk.Label(control_frame, text="Wörter pro Minute:", font=("Helvetica", 12))
wpm_label.grid(row=0, column=0, padx=5)
wpm_entry = tk.Entry(control_frame, width=5)
wpm_entry.insert(0, str(wpm))
wpm_entry.grid(row=0, column=1, padx=5)

start_button = tk.Button(control_frame, text="Start", command=run, width=10)
start_button.grid(row=0, column=2, padx=10)

clear_button = tk.Button(control_frame, text="Clear", command=clear_text, width=10)
clear_button.grid(row=0, column=3, padx=10)

root.mainloop()
