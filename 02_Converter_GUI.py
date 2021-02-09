from tkinter import *
import random


class converter:
    def __init__(self):
        # Formatting Variables This color is light orange.
        background_color = "#FFE6CC"

        # Converter Frame
        self.converter_frame = Frame(bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Converter Heading (Row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "19", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)
        # User Instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame, text="Type in the amount to be "
                                                                        "converted and then push "
                                                                        "one of the buttons below...",

                                             font=("Arial", "10", "bold"), wrap=290, justify=LEFT,
                                             bg=background_color,
                                             padx=10, pady=10,
                                             )
        self.temp_instructions_label.grid(row=1)
        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20, font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        # Conversion buttons frame (row 3) Light blue for Celsius, light Red for Fahrenheit
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Celsius", font="Arial 10 bold",
                                  bg="#DAE8FC", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  bg="#F8CECC", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))

        self.to_f_button.grid(row=0, column=1)

        # Answer Label (row 4)
        self.converted_label = Label(self.converter_frame, width=10, font="Arial 14 bold", text="Conversion goes here",
                                     bg=background_color,
                                     fg='#765FE8', pady=10, padx=50)

        self.converted_label.grid(row=4)

        # History / Help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame, font='Arial 12 bold', text="Calculation History",
                                       width=15, bg="#E1D5E7")
        self.calc_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help!", width=5,
                                  bg="#E1D5E7")
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, low):
        print(low)

        error = "#FADBD8"

        # Retrieve amount entered into Entry Field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # Check amount is a valid number

            # Convert to F
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9 / 5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = " {} degrees C is {} degrees F".format(to_convert, fahrenheit)


            # Convert to C
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5 / 9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = " {} degrees F is {} degrees C".format(to_convert, celsius)

            # Input is too low
            else:
                answer = "Too Cold!"
                has_errors = "yes"

            # Display the Answer
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")

            else:
                self.converted_label.configure(text="Enter a Number!", fg="red")
                self.to_convert_entry.configure(bg=error)

        except ValueError:
            self.converted_label.configure(text="Enter a Number!", fg="red")
            self.to_convert_entry.configure(bg=error)

    # Rounding!
    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)

        return rounded

        # Add Answer to list for History.


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = converter()
    root.mainloop()
