import pyshorteners
import customtkinter as ctk
import emoji
import webbrowser
 
#  themes and color for customtkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


app = ctk.CTk()
app.geometry("780x580")
app.title("URL Shortener")




# frame
frame_1 = ctk.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

# label
title = ctk.CTkLabel(
    master=frame_1,
    text="Enter Link to Short",
    font=ctk.CTkFont(size=20, weight="bold"),
)
title.pack(padx=10, pady=(40, 0))

# link input
url_val = ctk.StringVar()
link = ctk.CTkEntry(master=frame_1, width=550, height=35, textvariable=url_val)
link.pack(padx=10, pady=(10, 10))
try:
    link.insert(0, app.clipboard_get())
except:
    link.get()

#TinyURL shortener service
def short():
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(link.get())
    global newurl
    newurl=short_url
    

def clear():
     link.delete("0", "end")

# download button
short_btn = ctk.CTkButton(master=frame_1, text="Short URL", command=short)
short_btn.pack(pady=10, padx=10)

# Shortened URl
open = ctk.CTkButton(master=frame_1, text="Open in Browser", cursor="hand2")
open.pack(pady=10, padx=10)
open.bind(
    "<Button-1>",
    lambda e: webbrowser.open_new_tab(
        newurl
    ),
)
# clear button
clear_btn = ctk.CTkButton(master=frame_1, text="Clear",command=clear)
clear_btn.pack(pady=10, padx=10)

# footer
em = emoji.emojize("Created with :growing_heart:  @Dev")
author = ctk.CTkLabel(master=frame_1, text=em, justify=ctk.LEFT, cursor="hand2")
author.pack(pady=10, padx=10)
author.bind(
    "<Button-1>",
    lambda e: webbrowser.open_new_tab(
        "http://www.linkedin.com/in/devendra-singh-08b613254"
    ),
)



app.mainloop()