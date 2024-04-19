# File: speedlimitGUI_Adrienne.py
# Project: CSIS 2101 Assignment 13
# Author: Adrienne Pallett
# History: Version 13.1 [DATE]

# Speed Limit from Assignment 3 using GUI


import tkinter

class SpeedGUI:
    def __init__(self):

        # Windows
        self.main_window = tkinter.Tk()
        self.main_window.title("Speed Limit Fines")

        # Frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.middle2_frame = tkinter.Frame(self.main_window)
        self.middle3_frame = tkinter.Frame(self.main_window)
        self.middle4_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.bottom2_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack(padx = 15, pady = 15)
        self.middle_frame.pack(padx = 10, pady = 5)
        self.middle2_frame.pack(padx = 10, pady = 5)
        self.middle3_frame.pack(padx = 10, pady = 5)
        self.middle4_frame.pack(padx = 10, pady = 5)
        self.bottom_frame.pack(padx = 10,pady = 5)
        self.bottom2_frame.pack(pady = 20)

        # Top Frame
        self.intro = tkinter.Label(self.top_frame,
                                    text = "This program will calculate your speeding fines"
                                    +"\n and whether court is mandatory in Florida")
        
        self.intro.pack()

        # Speed Limit - Middle Frame
        self.speedlimit_label = tkinter.Label(self.middle_frame,
                                               text = "Speed Limit")
        self.speedlimit_entry = tkinter.Entry(self.middle_frame,
                                              width = 5)
        
        self.speedlimit_label.pack(side = "left")
        self.speedlimit_entry.pack(side = "right")

        # Speed - Middle2 Frame
        self.speed_label = tkinter.Label(self.middle2_frame,
                                         text = "Your Speed")
        self.speed_entry = tkinter.Entry(self.middle2_frame,
                                         width = 5)
        
        self.speed_label.pack(side = "left")
        self.speed_entry.pack(side = "right")

        # Teen - Middle3/Middle4 Frames
        self.teen_label = tkinter.Label(self.middle3_frame,
                                        text = "Teen Driver")
        self.teen_entry = tkinter.Entry(self.middle3_frame,
                                        width = 5)
        self.teen_desc_label = tkinter.Label(self.middle4_frame,
                                        text = "Enter T or Teen for Teen Driver\nN or No for Adult Driver")
        
        self.teen_label.pack(side = "left")
        self.teen_entry.pack(side = "left")
        self.teen_desc_label.pack()

        # Results - Bottom Frame
        self.descr_label = tkinter.Label(self.bottom_frame,
                                         text = "Total Fine Calculated:")
        self.fine = tkinter.StringVar()
        self.fine_label = tkinter.Label(self.bottom_frame,
                                        textvariable = self.fine,
                                        fg = "red")
        
        self.descr_label.pack(side = "top")
        self.fine_label.pack(side = "bottom")
        
        
        # Button - Bottom2 Frame
        self.calc_button = tkinter.Button(self.bottom2_frame,
                                          text = "Calculate",
                                          fg = "green",
                                          command = self.calc_fine)
        self.quit_button = tkinter.Button(self.bottom2_frame,
                                          text = "Quit",
                                          fg = "red",
                                          command = self.main_window.destroy)

        self.calc_button.pack(side = "left")
        self.quit_button.pack(side = "right")
        

        tkinter.mainloop()

        
    # Speed Calculations
    def calc_fine(self):

        speedlimit = int(self.speedlimit_entry.get())
        speed = int(self.speed_entry.get())
        teen = str(self.teen_entry.get())
        miles_over = speed - speedlimit

        if miles_over < 0:
            fine = "No Fine"
        elif miles_over > 0 and miles_over <= 5:
            fine = 39.50
        elif miles_over > 5 and miles_over <= 15:
            fine = 89.00
        elif miles_over > 15 and miles_over <= 25:
            fine = 109.50
        elif miles_over > 25 and miles_over <= 35:
            fine = 149.99
        else:
            if miles_over > 35:
                fine = "Court is mandatory. \nYour fine will be decided in court"

        if teen == "t" or teen == "teen" or teen == "T" or teen == "Teen":
            if miles_over < 0:
                pass
            elif miles_over > 35:
                fine = fine
            else:
                fine = fine * 3
                
        if type(fine) == str:
            self.fine.set(fine)
        else:
            self.fine.set(f"${fine:.02f}")
 

if __name__ == "__main__":
    my_gui = SpeedGUI()
