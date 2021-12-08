# part 4

# a5.py
# 
# ICS 32 
#
# v0.4
# 
# The following module provides a graphical user interface shell for the DSP journaling program.



import tkinter as tk
from tkinter import Button, Entry, Label, StringVar, Text, Toplevel, ttk, filedialog
from tkinter.constants import BOTH, END, RADIOBUTTON, RIGHT, TRUE
import Profile
#from NaClProfile import NaClProfile

# lucas
# ics 32 final project


"""
A subclass of tk.Frame that is responsible for drawing all of the widgets
in the body portion of the root frame.
"""
class Body(tk.Frame):
    def __init__(self, root, select_callback=None, night_mode=False):
        tk.Frame.__init__(self, root)
        self.root = root
        self.night_mode = night_mode
        self._select_callback = select_callback

        # a list of the Post objects available in the active DSU file
        self._posts = [Profile.Post]
        
        # After all initialization is complete, call the _draw method to pack the widgets
        # into the Body instance 
        self._draw()
    
    """
    Update the entry_editor with the full post entry when the corresponding node in the posts_tree
    is selected.
    """
    def node_select(self, event):
        index = int(self.posts_tree.selection()[0])
        entry = self._posts[index].entry
        self.set_text_entry(entry)
    
    """
    Returns the text that is currently displayed in the entry_editor widget.
    """
    def get_text_entry(self) -> str:
        return self.entry_editor.get('1.0', 'end').rstrip()

    """
    Sets the text to be displayed in the entry_editor widget.
    NOTE: This method is useful for clearing the widget, just pass an empty string.
    """
    def set_text_entry(self, text:str):
        self.message_widget.delete(1.0,END)
        self.message_widget.insert("end",text)
        pass
    
    """
    Populates the self._posts attribute with posts from the active DSU file.
    """
    def set_posts(self, posts:list):
        # TODO: Write code to populate self._posts with the post data passed
        # in the posts parameter and repopulate the UI with the new post entries.
        # HINT: You will have to write the delete code yourself, but you can take 
        # advantage of the self.insert_posttree method for updating the posts_tree
        # widget.
        pass

    """
    Inserts a single post to the post_tree widget.
    """
    def insert_post(self, post: Profile.Post):
        self._posts.append(post)
        id = len(self._posts) - 1 #adjust id for 0-base of treeview widget
        self._insert_post_tree(id, post)


    """
    Resets all UI widgets to their default state. Useful for when clearing the UI is neccessary such
    as when a new DSU file is loaded, for example.
    """
    def reset_ui(self):
        self.set_text_entry("")
        self.entry_editor.configure(state=tk.NORMAL)
        self._posts = []
        for item in self.posts_tree.get_children():
            self.posts_tree.delete(item)

    """
    Inserts a post entry into the posts_tree widget.
    """
    def _insert_post_tree(self, id, post: Profile.Post):
        entry = post.entry

        if len(entry) > 25:
            entry = entry[:24] + "..."
        
        self.posts_tree.insert('', id, id, text=entry)
    
    
        #self.message_widget.config(text = "send successfully")
    
    """
    Call only once upon initialization to add widgets to the frame
    """
    def _draw(self):
        print('BODY', self.night_mode)
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

        self.message_widget = tk.Text(msg_post_frame,height = 0,state = 'disabled', bg= bg_color) #where display the message
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
    def __init__(self, root, night_mode_callback=None, save_callback=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self.night_mode_callback = night_mode_callback
        self._save_callback = save_callback
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
    Calls the callback function specified in the online_callback class attribute, if
    available, when the chk_button widget has been clicked.
    """
    def night_mode_click(self):
        print("SELF.IS_NIGHT.GET()", self.is_night.get())
        if self.is_night.get() == 1:  # Night mode enabled
            self.night_mode_callback(True)
        else:  # Night mode disabled
            self.night_mode_callback(False)

    """
    Calls the callback function specified in the save_callback class attribute, if
    available, when the save_button has been clicked.
    """
    def save_click(self):
        if self._save_callback is not None:
            self._save_callback()

    """
    Updates the text that is displayed in the footer_label widget
    """
    def set_status(self, message):
        self.footer_label.configure(text=message)
    
    """
    Call only once upon initialization to add widgets to the frame
    """

    def send_message(self):
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




"""
A subclass of tk.Frame that is responsible for drawing all of the widgets
in the main portion of the root frame. Also manages all method calls for
the NaClProfile class.
"""
class MainApp(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self.username = ''
        self.password=""
        self.dsu_server=''
        self.is_night_mode = False
        self._draw()

    """
    Creates a new DSU file when the 'New' menu item is clicked.
    """
#----------------------------------------------new profile--------------------------#
    """
    After user click the 'ok' in configure account 
    1.go to the user_exist_checker to check whether the usrname is taken
    2.if taken go to open_profile
    3.if not taken, go to new_profile 
    """
    def user_exist_checker(self,usr):
        self.file_path = f'profiles/{usr}.dsu' #usr = the self.username
        try:
            self.create_path(self.file_path)
            self.create_new_profile()
        except FileExistsError:
            self.load_profile()

    def create_path(self,file_path):
        """Creates a file in the profiles folder for storing Profile data."""
        with open(file_path,'x') as f:
            pass

    def create_new_profile(self):
        self.user_profile = Profile.Profile()
        self.user_profile.dsuserver = self.dsu_server
        self.user_profile.username = self.username
        self.user_profile.password = self.password
        self.save_profile()
        print('called')
#----------------------------------------------new profile--------------------------#
    """
    Opens an existing DSU file when the 'Open' menu item is clicked and loads the profile
    data into the UI.
    """
    def load_profile(self):
        self.clear_profile()  # Clears the current profile so that the new profile could be loaded
        self.user_profile.load_profile(self.file_path)  # Sets all the profile attributes to the self.user_profile object
        if self.check_password(self.password):  # Passes in the password the user entered in the tkinter entry widget
            print('ACCESS GRANTED')
            #logged_in = True?
            # Show all the contacts saved in the profile
        else:
            print('ACCESS DENIED')  #  Wrong passwrod


    def clear_profile(self):
        """Clears the previous profile when loading in a new one."""
        self.user_profile = Profile.Profile(dsuserver=None, username=None, password=None)
        self.user_profile.bio = ''
        self.user_profile._posts = []
        self.user_profile.contacts = {}
    

    def check_password(self, password) -> bool:
        """Returns True if the given password is equal to the profile's password.
        """
        return password == self.user_profile.password

    """
    Saves the text currently in the entry_editor widget to the active DSU file.
    """
    def save_profile(self):
        self.user_profile.save_profile(self.file_path)


    """
    Closes the program when the 'Close' menu item is clicked.
    """
    def close(self):
        self.root.destroy()


#-------------------------------------configure account screen---------------------------------->>
    def ok_login(self): #TODO for final project
        self.dsu_server = str(self.DS_Server_Address.get())
        self.username =str(self.Username.get())
        self.password = str(self.Password.get())
        self.user_exist_checker(self.username)
        self.account_screen.destroy()
        

    def cancel(self):
        self.account_screen.destroy()
#-------------------------------------configure account screen---------------------------------->>

#-------------------------------------add friend screen----------------------------------------->>
    def ok_add_f(self): #TODO for final project
        pass

    def cancel_a_f(self):
        self.add_f_screen.destroy()
#-------------------------------------add friend screen----------------------------------------->>

    # for collecting the ip, username, passwords from user
    def configure_account(self):
        self.account_screen = Toplevel(self.root)
        self.account_screen.title('Configure Account')
        self.account_screen.geometry("250x180") # width x height

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


    # add user by username 
    def add_friends(self):
        self.add_f_screen = Toplevel(self.root)
        self.add_f_screen.title("Add a friend")
        self.add_f_screen.geometry("250x100")

        self.cont_name = StringVar()

        Label(self.add_f_screen,text='Please type the username of your new contact').pack()
        Entry(self.add_f_screen,textvariable=self.cont_name ).pack()

        Button(self.add_f_screen,text = "Ok", width= 15, 
            height=1,
            command= self.ok_add_f).pack(side=tk.LEFT,pady = 5, padx =5)

        Button(self.add_f_screen,text = "cancel", width= 15, 
            height=1,
            command = self.cancel_a_f).pack(side=tk.RIGHT,pady = 5, padx =5)
        pass
    
    """
    A callback function for responding to changes to the night mode button.
    """
    def night_mode_changed(self, value:bool):
        if self.is_night_mode == 1:
            self.is_night_mode = 0
        else:
            self.is_night_mode = 1
        #self.is_night_mode = value

        self.body.destroy()
        self.footer.destroy()
        self._draw()


    def _draw(self):
        # Build a menu and add it to the root frame.
        menu_bar = tk.Menu(self.root)
        self.root['menu'] = menu_bar
        menu_file = tk.Menu(menu_bar)
        menu_bar.add_cascade(menu=menu_file, label='File')
        menu_file.add_command(label='New', command=self.create_new_profile)
        menu_file.add_separator()
        menu_file.add_command(label='Open...', command=self.load_profile)
        menu_file.add_separator()
        menu_file.add_command(label='Close', command=self.close)
        menu_setting = tk.Menu(menu_bar)
        menu_bar.add_cascade(menu= menu_setting,label = 'Setting')
        menu_setting.add_command(label='Configure Account', command=self.configure_account)
        menu_setting.add_separator()
        menu_setting.add_command(label='Add Friends', command=self.add_friends)

        self.footer = Footer(self.root, night_mode_callback=self.night_mode_changed, save_callback=self.save_profile)
        self.footer.pack(fill=tk.BOTH, side=tk.BOTTOM)
        self.body = Body(self.root, night_mode=self.is_night_mode)
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