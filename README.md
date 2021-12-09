
ICS 32 Final Project:

Members:
Sona Keshishyan
Hassan Hayder Al-Najjar
Xiaofan Lu


* __part4.py__: Use this file as the main module for the program. To close: While in the program, click options on the top and click exit. The requirement of a custom class is stored in this file. The Refresh class uses the threading module and it automatically retrieves new message every few seconds.

* __part1_protocol.py__: This file is used for part 1 of our final project. It's a helper function for communicating with another user on the DSP platform. It was extended from a3 to accept directmessage commands. 

* __ds_messenger.py__: This file is used for part 2 of our final project. It runs independently from the other functions which allows it to be used in other applications if needed. Contains the classes DirectMessage, and Direct Messenger. 

* __part3.py__: This file is used for part 3 of our final project. It stores the data locally on the computer which removes the need of internet connection to display all message history from contacts. Added feature of password security which makes sure the password matches the one of an already made profile of the same username before granting access to log in. 

* __test_ds_messenger.py__: This file is used for part 2 of our final project. It contains unittest cases for the ds_messenger which makes sure it works. 

* __test_protocol.py__: This file is used for part 1 of our final project. It contains unittest cases for the protocol module which makes sure the expected results happen. 

* __custom_class__: This file is used for the required of having at least one custom exception class. It is for password to alert a user making an account that it is either too short or too long of a password. It tells the user to type between 2 and 100 characters. 


Important to know:
- To close the program, go to the options tab and click the exit button. 
- Make sure to click on the contact name in the tree to update the GUI


Sources and References:
Refresh class source https://thispointer.com/create-a-thread-using-class-in-python/
Unittest source https://docs.python.org/3/library/unittest.html
