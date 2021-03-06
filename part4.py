# part 4

# a5.py
# 
# ICS 32 
#
# v0.4
# 
# The following module provides a graphical user interface shell for the DSP journaling program.

# Site source https://thispointer.com/create-a-thread-using-class-in-python/


import tkinter as tk
from tkinter import Button, Entry, Label, Message, StringVar, Text, Toplevel, ttk, filedialog
from tkinter.constants import BOTH, END, RADIOBUTTON, RIGHT, TRUE
import Profile
import sys
from threading import Thread
import time
from ds_messenger import DirectMessenger
import custom_class
#from NaClProfile import NaClProfile

# lucas
# ics 32 final project


"""Class responsible for the Body of the GUI"""
class Body(tk.Frame):
    def __init__(self, root, select_callback=None, night_mode=False):
        tk.Frame.__init__(self, root)
        self.root = root
        self.night_mode = night_mode
        self._select_callback = select_callback
        self.contact_name = None # for send check, if None, message will send to default messgener. 
        self._name = []
        self._body_contact = {}# because the call back doesn't work
        # After all initialization is complete, call the _draw method to pack the widgets
        # into the Body instance
        self._history_text = []
        self._draw()

    """Sets the name for the contact"""
    def set_contact_msg(self,contact:dict): # for final project
        self._body_contact = contact
        for name in contact:
            self._name.append(name)
            self.insert_contact(name)

    """Selects the node in the GUI Tree."""
    def node_select(self, event):
        self._history_text = []# clear the previous text
        index = int(self.posts_tree.selection()[0])
        self.contact_name = self._name[index]
        for key, value in self._body_contact.items():
            if key == self.contact_name:
                for item in value:
                    self._history_text.append(f"{item['from']}: {item['message']}")
        self.set_history_message(self._history_text)

    """Retrieves the text entry from the entry box."""
    def get_text_entry(self) -> str:
        return self.entry_box.get('1.0', 'end').rstrip()

    """Sets all the messages sent by the contact."""
    def set_history_message(self, text: list):
        self.message_widget.configure(state='normal')
        self.message_widget.delete(0.0, 'end')
        self.message_widget.insert(0.0, "\n".join(text))
        self.message_widget.configure(state='disable')

    """Sets the text entry."""
    def set_text_entry(self, text:str):
        self.entry_box.delete(1.0,END)
        self.entry_box.insert("end",text)

    """Inserts contact into the post tree."""
    def insert_contact(self, name):
        id = len(self._name) - 1 #adjust id for 0-base of treeview widget
        self._insert_post_tree(id, name)

    """Resets the GUI."""
    def reset_ui(self):
        self.set_text_entry("")
        self.message_widget.configure(state=tk.NORMAL)
        self._name = []
        for item in self.posts_tree.get_children():
            self.posts_tree.delete(item)

    """Inserts contact name into the post tree"""
    def _insert_post_tree(self, id, name):
        self.posts_tree.insert('', 0,id, text=name)
    
    
    def _draw(self):
        if self.night_mode:
            bg_color = 'black'
            fg_color = 'white'
        else:
            bg_color = 'white'
            fg_color = 'black'
        posts_frame = tk.Frame(master=self, width=250, bg=bg_color)
        posts_frame.pack(fill=tk.BOTH, side=tk.LEFT)

        ttk.Style().configure("Treeview", background = bg_color, 
        foreground=fg_color, fieldbackground=bg_color)

        self.posts_tree = ttk.Treeview(posts_frame)
        self.posts_tree.bind("<<TreeviewSelect>>", self.node_select)
        self.posts_tree.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=5)

        entry_frame = tk.Frame(master=self,height = 120, bg=fg_color)
        entry_frame.pack(fill=tk.BOTH, side=tk.BOTTOM,pady =5,padx = 5)

        msg_post_frame = tk.Frame(master=self, bg="red" )
        msg_post_frame.pack(fill=tk.BOTH, side=tk.TOP,expand = True, pady =5,padx = 5)

        scroll_frame = tk.Frame(master=msg_post_frame, bg="blue", width=10)
        scroll_frame.pack( fill = tk.BOTH, side=tk.RIGHT, expand=False)

        scroll_frame_entry = tk.Frame(master=entry_frame, bg="blue", width=10)
        scroll_frame_entry.pack( fill = tk.BOTH, side=tk.RIGHT, expand=False)

        self.entry_box = tk.Text(entry_frame,height=5, bg= bg_color, fg=fg_color)# where to type in message
        self.entry_box.pack(fill=BOTH, side = tk.BOTTOM, expand = False)

        self.message_widget = tk.Text(msg_post_frame,height = 0, bg= bg_color, fg = fg_color, state = 'disabled')  # where display the message
        self.message_widget.pack(fill = BOTH,side = tk.TOP,expand = True )
    
        entry_scrollbar = tk.Scrollbar(master=scroll_frame, command=self.message_widget.yview)#scrollbar in text widget
        self.message_widget['yscrollcommand'] = entry_scrollbar.set
        entry_scrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=True, padx=0, pady=0)
        
        entry_editor_scrollbar = tk.Scrollbar(master=scroll_frame_entry, command=self.entry_box.yview)#scrollbar in text widget
        self.entry_box['yscrollcommand'] = entry_editor_scrollbar.set
        entry_editor_scrollbar.pack(fill=tk.Y, side=tk.LEFT, expand=False, padx=0, pady=0)
    
#--------------------------------send button ------------------------------------------------------>>


"""
A subclass of tk.Frame that is responsible for drawing all of the widgets
in the footer portion of the root frame.
"""
class Footer(tk.Frame):
    def __init__(self, root, night_mode_callback=None, send_callback=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self.night_mode_callback = night_mode_callback
        self._send_callback = send_callback
        self.is_online = tk.IntVar()
        # IntVar is a variable class that provides access to special variables
        # for Tkinter widgets. is_online is used to hold the state of the chk_button widget.
        # The value assigned to self.is_night when the chk_button widget is changed by the user
        # can be retrieved using the get() function:
        # chk_value = self.is_night.get()
        self.is_night = tk.IntVar()
        # After all initialization is complete, call the _draw method to pack the widgets
        # into the Footer instance 
        self._draw()
    
    """
    Calls the callback function specified in the night_mode_callback class attribute, if
    available, when the chk_button widget has been clicked.
    """
    def night_mode_click(self):
        if self.is_night.get() == 1:  # Night mode enabled
            self.night_mode_callback(True)
        else:  # Night mode disabled
            self.night_mode_callback(False)


    """
    Updates the text that is displayed in the footer_label widget
    """
    def set_status(self, message):
        self.footer_label.configure(text=message)
    

    """Calls the send message call back function."""
    def send_message(self):
        if self._send_callback is not None:
            self._send_callback()
        pass

        
    def _draw(self):
        save_button = tk.Button(master=self, text="Send", width=20)
        save_button.configure(command=self.send_message)
        save_button.pack(fill=tk.BOTH, side=tk.RIGHT, padx=5, pady=5)

        self.chk_button = tk.Checkbutton(master=self, text="Night Mode", variable=self.is_night)
        self.chk_button.configure(command=self.night_mode_click) 
        self.chk_button.pack(fill=tk.BOTH, side=tk.RIGHT)

        self.footer_label = tk.Label(master=self, text="Ready.")
        self.footer_label.pack(fill=tk.BOTH, side=tk.RIGHT, padx=5)


"""Custom class that uses the threading module to create a thread that automatically 
retrieves new messages and updates them to the Profile class."""
class Refresh(Thread):
    def __init__(self, main_app):
        Thread.__init__(self)
        self.main_app = main_app
        self.keep_running = True

    def run(self):
        while self.keep_running:
            time.sleep(2)
            self.main_app.update()
        

"""Main App that is a subclass of tk.Frame. Is the main class of this file."""
class MainApp(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.user_profile = Profile.Profile() # for final project
        self.messgener = DirectMessenger()
        # without any setting
        #self.token = None
        self.root = root
        self.username = ''
        self.password=""
        self.dsu_server=''
        self.is_night_mode = False
        
        self.recipient = None

        self.refresh = Refresh(self)

        self._draw()

    """Is called from the Refresh class every few seconds."""
    def update(self):
        retreived_messages = self.messgener.retrieve_new()
        messages = retreived_messages[1]
        if messages:
            message = messages[0]
            recipient = message['from']
            if recipient in self.user_profile.contacts:
                self.user_profile.contacts[recipient].append(message)
            else:
                self.user_profile.contacts[recipient] = [message]
            self.save_profile()


#----------------------------------------------new profile--------------------------#
    """Checks if the user exists and if so, will create a file path using their username,
    stored in the profiles folder. Then it will load the profile."""
    def user_exist_checker(self,usr):
        self.file_path = f'profiles/{usr}.dsu' #usr = the self.username
        try:
            self.create_path(self.file_path)
            self.create_new_profile()
        except FileExistsError:
            self.load_profile()
        except custom_class.UnExpected_Error:
            print("An unexpected error occurred, please try again")

    """Creates a file in the profiles folder for storing Profile data."""
    def create_path(self,file_path):
        with open(file_path,'x') as f:
            pass

    """Creates a new profile."""
    def create_new_profile(self):
        self.user_profile = Profile.Profile()
        self.user_profile.dsuserver = self.dsu_server
        self.user_profile.username = self.username
        self.user_profile.password = self.password
        self.save_profile()
#----------------------------------------------new profile--------------------------#
    """
    Opens an existing DSU file when the 'Open' menu item is clicked and loads the profile
    data into the UI.
    """
    def load_profile(self):
        self.clear_ui()
        self.clear_profile()  # Clears the current profile so that the new profile could be loaded
        self.user_profile.load_profile(self.file_path)  # Sets all the profile attributes to the self.user_profile object

    """Clears the profile attributes."""
    def clear_profile(self):
        """Clears the previous profile when loading in a new one."""
        self.user_profile = Profile.Profile(dsuserver=None, username=None, password=None)
        self.user_profile.bio = ''
        self.user_profile._posts = []
        self.user_profile.contacts = {}

    """Saves the profile using the given file path attribute."""
    def save_profile(self):
        self.user_profile.save_profile(self.file_path)

    """Sends the message to the server"""
    def send_message_to_server(self): # callback to footer, so when user click send, the msg in entry will send to 
        #message widget
        if self.messgener.token is None: # when the the username is not set up 
            self.messgener = DirectMessenger(dsuserver="168.235.86.101",username=self.username,password=self.password)
            self.messgener.token = self.messgener.join()
        else:
            self.recipient = self.body.contact_name
    

        self.messgener.send(self.body.get_text_entry(),self.recipient)
        Time = str(time.time())
        New_message = {}
        New_message["from"] = self.username
        New_message["timestamp"] = Time
        New_message["message"] = self.body.get_text_entry()
        
        self.user_profile.contacts[f'{self.body.contact_name}'].append(New_message)
        self.save_profile()
        self.body.set_text_entry('')


    """
    Closes the program when the 'Close' menu item is clicked.
    """
    def close(self):
        self.refresh.keep_running = False
        sys.exit()
        self.root.destroy()


#-------------------------------------configure account screen---------------------------------->>

    """Add to contacts attribute."""
    def add_to_contacts(self, messages:list) -> dict:
        contacts = self.user_profile.contacts
        for msg in messages:
            reciepient = msg['from']
            if reciepient not in contacts:
                contacts[reciepient] = [msg]
            else:
                contacts[reciepient].append(msg)
        return contacts

    """Is called when the 'ok' button is pressed."""
    def ok_login(self): #TODO for final project
        self.dsu_server = str(self.DS_Server_Address.get())
        self.username =str(self.Username.get())
        self.password = str(self.Password.get())
        self.messgener = DirectMessenger(dsuserver=self.dsu_server,username=self.username,password=self.password)
        self.messgener.token = self.messgener.join()

        self.user_exist_checker(self.username)

        list_of_messages = self.messgener.retrieve_all()
        self.user_profile.contacts = self.add_to_contacts(list_of_messages)
        self.save_profile()

        self.body.set_contact_msg(self.user_profile.contacts)#<<<<<<<<<<<<<<<<<<<<<<<<<,

        self.refresh.start()


        self.account_screen.destroy()
        
    

    """Is called when the cancel button is called."""
    def cancel(self):
        self.account_screen.destroy()
#-------------------------------------configure account screen---------------------------------->>

#-------------------------------------add friend screen----------------------------------------->>
    """Is called when the 'ok' button is pressed when adding a friend."""
    def ok_add_f(self): #TODO for final project
        New_message = {}
        #self.body.reset_ui()
        Time = time.time()
        New_message={}
        new_list = []
        New_message["from"] = f'{self.username}'
        New_message["timestamp"] = Time
        New_message["message"] = "New friend"
        new_list.append(New_message)
        self.user_profile.contacts[f'{str(self.add_name.get())}'] = new_list
        self.save_profile()
        self.body.set_contact_msg(self.user_profile.contacts)
        self.add_f_screen.destroy()

    """Is called when the 'ok' button is pressed when adding a friend."""
    def cancel_add_f(self):
        self.add_f_screen.destroy()
#-------------------------------------add friend screen----------------------------------------->>

    """for collecting the ip, username, passwords from user"""
    def configure_account(self):
        self.account_screen = Toplevel(self.root)
        self.account_screen.title('Configure Account')
        self.account_screen.geometry("250x180") # width x height
        try:
            self.DS_Server_Address = StringVar()
            self.Username = StringVar()
            self.Password = StringVar()

            Label(self.account_screen,text='DS Server Address').pack()
            Entry(self.account_screen,textvariable=self.DS_Server_Address ).pack()

            Label(self.account_screen,text='Username').pack()
            Entry(self.account_screen,textvariable=self.Username ).pack()

            Label(self.account_screen,text='Password').pack()
            Entry(self.account_screen,textvariable=self.Password ).pack()

            Button(self.account_screen,text = "Ok", width= 15, 
                height=1,
                command= self.ok_login).pack(side=tk.LEFT,pady = 5, padx =5)
            Button(self.account_screen,text = "cancel", width= 15, 
                height=1,
                command = self.cancel).pack(side=tk.RIGHT,pady = 5, padx =5)
            if len(self.Password.get()) < 2:
                raise custom_class.Password_Short
            if len(self.Password.get()) > 100:
                raise custom_class.Password_Too_Long
        except custom_class.Password_Short:
            print("Password is too short, please input more than 5 characters")
        except custom_class.Password_Too_Long:
            print("Password is too long, please input less than 100 characters")
        except custom_class.UnExpected_Error:
            print("An unexpected error occurred, please try again")

    """Add user by username."""
    def add_friends(self):
        self.add_f_screen = Toplevel(self.root)
        self.add_f_screen.title("Add a friend")
        self.add_f_screen.geometry("250x100")

        self.add_name = StringVar()

        Label(self.add_f_screen,text='Please type the username of your new contact').pack()
        Entry(self.add_f_screen,textvariable=self.add_name ).pack()

        Button(self.add_f_screen,text = "Ok", width= 15, 
            height=1,
            command= self.ok_add_f).pack(side=tk.LEFT,pady = 5, padx =5)

        Button(self.add_f_screen,text = "cancel", width= 15, 
            height=1,
            command = self.cancel_add_f).pack(side=tk.RIGHT,pady = 5, padx =5)
    
    
    """
    A callback function for responding to changes to the night mode button.
    """
    def night_mode_changed(self, value:bool):
        if self.is_night_mode == 1:
            self.is_night_mode = 0
        else:
            self.is_night_mode = 1

        self.clear_ui()
        
    """Clears the UI"""
    def clear_ui(self):
        self.body.pack_forget()
        self.footer.pack_forget()
        self._draw()

    def _draw(self):
        # Build a menu and add it to the root frame.
        menu_bar = tk.Menu(self.root)
        self.root['menu'] = menu_bar
        menu_file = tk.Menu(menu_bar)
        menu_bar.add_cascade(menu=menu_file, label='Options')
        menu_file.add_command(label='Exit', command=self.close)
        menu_file.add_separator()
        menu_setting = tk.Menu(menu_bar)
        menu_bar.add_cascade(menu= menu_setting,label = 'Setting')
        menu_setting.add_command(label='Configure Account', command=self.configure_account)
        menu_setting.add_separator()
        menu_setting.add_command(label='Add Friends', command=self.add_friends)

        self.footer = Footer(self.root, night_mode_callback=self.night_mode_changed, send_callback=self.send_message_to_server)
        self.footer.pack(fill=tk.BOTH, side=tk.BOTTOM)

        self.body = Body(self.root, night_mode=self.is_night_mode, select_callback=self.user_profile)
        self.body.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

if __name__ == "__main__":
    # All Tkinter programs start with a root window. We will name ours 'main'.
    main = tk.Tk()

    # 'title' assigns a text value to the Title Bar area of a window.
    main.title("ICS 32 Final Project")

    # This is just an arbitrary starting point. You can change the value around to see how
    # the starting size of the window changes. I just thought this looked good for our UI.
    main.geometry("720x480")

    # adding this option removes some legacy behavior with menus that modern OSes don't support. 
    # If you're curious, feel free to comment out and see how the menu changes.
    main.option_add('*tearOff', False)

    # Initialize the MainApp class, which is the starting point for the widgets used in the program.
    # All of the classes that we use, subclass Tk.Frame, since our root frame is main, we initialize 
    # the class with it.
    MainApp(main)

    # When update is called, we finalize the states of all widgets that have been configured within the root frame.
    # Here, Update ensures that we get an accurate width and height reading based on the types of widgets
    # we have used.
    # minsize prevents the root window from resizing too small. Feel free to comment it out and see how
    # the resizing behavior of the window changes.
    main.update()
    main.minsize(main.winfo_width(), main.winfo_height())
    # And finally, start up the event loop for the program (more on this in lecture).
    main.mainloop()