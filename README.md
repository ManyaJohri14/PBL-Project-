# PBL-Project-Campus Mindspace 

**Team Name:** Pop The Stress
**Project Name:** Campus Mindspace (Anonymous Student Support Portal)
**Project Type:** Hybrid System (Python Tkinter UI + C Data Structure Backend)


## Project Team & Roles
** Manya Johri (Team Leader & UI Designer)**
	• My Role: Project Manager and Interface Designer.
	• What I Did: Coded the main desktop application windows, the navigation buttons, text layout spaces, and the 
                      color themes using Python Tkinter.
** Aditi Pandey (Backend Programmer)**
	• Her Role: Data Structures and Logic Developer.
	• What She Did: Wrote the C code framework, defined the struct Node templates, and programmed the push() and pop() 
                        memory methods.
 **Anushka Saboo (Integration & Safety Tester)**
	• Her Role: Code Linker and Quality Assurance Inspector.
	• What She Did: Built the transfer.txt file bridge between Python and C, and verified that data deletes safely    
                        from RAM.

## How Our Project Works

Our software framework does not use permanent hard drive storage like SQL. Instead, everything runs purely inside the laptop's volatile RAM memory to keep students 100% anonymous:

1. **Student Vent Box:** A student opens the Python screen and types their stress note without entering names or college IDs.
2. **File Pipeline Bridge:** Python saves the text into a temporary file (transfer.txt) and tells the computer to run our compiled C code in the background.
3. **C Stack Allocation:** The C program (BACKEND.exe) reads the text into a dynamic memory node using malloc() and immediately executes remove("transfer.txt") to delete the bridge file completely.
4. **Counselor Clearance:** A counselor logs in using mindspace123 to view the top message (LIFO queue rules). Clicking resolve fires the C free(temp) command, completely clearing the text from the laptop's RAM slots permanently.
