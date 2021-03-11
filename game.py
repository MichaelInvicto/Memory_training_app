from tkinter import *
from tkinter import messagebox
import random

'''
The following are for the buttons for the start page buttons on da button factory
horizontal padding = 15
vertical padding = 8
color = 

'''


class MemoryApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        Tk.wm_title(self, 'Memory app')
        container = Frame(self)

        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, FlashingDigits, RandomImages):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def set_screen(self, which_one):
        if which_one == 'RandomImages':
            self.wm_title('Random Images')
            self.config(bg='#d9dab0', padx=200, pady=40)
            self.show_frame(cont=RandomImages)

        elif which_one == 'StartPage':
            self.wm_title('Memory Training App')
            self.config(bg='#d9dab0', padx=200, pady=40)
            self.show_frame(cont=StartPage)

        elif which_one == 'GameOne':
            self.wm_title('Flashing Digits')
            self.config(bg='#d9dab0', padx=200, pady=40)
            self.show_frame(cont=FlashingDigits)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Frame.config(self, bg='#d9dab0')
        label = Label(self, text='Select A Game Below')
        label.pack(padx=10, pady=10)

        button1 = Button(self, text='Flashing Digits', command=lambda: controller.set_screen('GameOne'))
        button1.pack()

        button2 = Button(self, text='Random Images', command=lambda: controller.set_screen('RandomImages'))
        button2.pack()


class FlashingDigits(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        Frame.config(self, bg='#d9dab0')

        self.MIN_CYCLE = 3
        self.MAX_CYCLE = 45
        self.CYCLES = 3
        self.FLASH_TIME = 500
        self.BG = '#d9dab0'

        self.real_numbers = []
        self.suggested_numbers = []

        self.frame1 = Frame(self)
        self.frame1.config(bg=self.BG)
        self.frame1.pack()

        self.current_number = Label(self.frame1, text='Start', font=('Georgia', 15), fg='black', bg=self.BG)
        self.current_number.grid(row=0, column=1)

        self.view_part = Label(self.frame1, text='', font=('Georgia', 20), fg='black', bg=self.BG)
        self.view_part.grid(row=1, column=1, pady=(10, 10))

        self.frame2 = Frame(self)
        self.frame2.config(bg=self.BG)
        self.frame2.pack()

        self.button1_image = PhotoImage(file='images/flashing text/1.png')
        self.button2_image = PhotoImage(file='images/flashing text/2.png')
        self.button3_image = PhotoImage(file='images/flashing text/3.png')
        self.button4_image = PhotoImage(file='images/flashing text/4.png')
        self.button5_image = PhotoImage(file='images/flashing text/5.png')
        self.button6_image = PhotoImage(file='images/flashing text/6.png')
        self.button7_image = PhotoImage(file='images/flashing text/7.png')
        self.button8_image = PhotoImage(file='images/flashing text/8.png')
        self.button9_image = PhotoImage(file='images/flashing text/9.png')

        self.start_button_image = PhotoImage(file='images/flashing text/start.png')
        self.clear_button_image = PhotoImage(file='images/flashing text/clear.png')
        self.settings_button = PhotoImage(file='images/flashing text/settings.png')
        self.back_button_image = PhotoImage(file='images/flashing text/back.png')
        self.check_answer_button = PhotoImage(file='images/flashing text/check answer.png')
        self.save_button_image = PhotoImage(file='images/flashing text/save.png')
        self.home_button = PhotoImage(file='images/flashing text/home.png')

        self.button1 = Button(self.frame2, image=self.button1_image, command=lambda: self.display_function(1),
                              borderwidth=0, bg=self.BG, activebackground=self.BG)
        self.button1.grid(row=1, column=1, padx=(0, 5), pady=(0, 20))

        self.button2 = Button(self.frame2, image=self.button2_image, command=lambda: self.display_function(2),
                              borderwidth=0, bg=self.BG, activebackground=self.BG)
        self.button2.grid(row=1, column=2, padx=(0, 5), pady=(0, 20))

        self.button3 = Button(self.frame2, image=self.button3_image, command=lambda: self.display_function(3),
                              borderwidth=0, bg=self.BG, activebackground=self.BG)
        self.button3.grid(row=1, column=3, pady=(0, 20))

        self.button4 = Button(self.frame2, image=self.button4_image, command=lambda: self.display_function(4),
                              borderwidth=0, bg=self.BG, activebackground=self.BG)
        self.button4.grid(row=2, column=1, padx=(0, 5), pady=(0, 20))

        self.button5 = Button(self.frame2, image=self.button5_image, command=lambda: self.display_function(5),
                              borderwidth=0, bg=self.BG, activebackground=self.BG)
        self.button5.grid(row=2, column=2, padx=(0, 5), pady=(0, 20))

        self.button6 = Button(self.frame2, image=self.button6_image, command=lambda: self.display_function(6),
                              borderwidth=0, bg=self.BG, activebackground=self.BG)
        self.button6.grid(row=2, column=3, pady=(0, 20))

        self.button7 = Button(self.frame2, image=self.button7_image, command=lambda: self.display_function(7),
                              borderwidth=0, bg=self.BG, activebackground=self.BG)
        self.button7.grid(row=3, column=1, padx=(0, 5), pady=(0, 20))

        self.button8 = Button(self.frame2, image=self.button8_image, command=lambda: self.display_function(8),
                              borderwidth=0, bg=self.BG, activebackground=self.BG)
        self.button8.grid(row=3, column=2, padx=(0, 5), pady=(0, 20))

        self.button9 = Button(self.frame2, image=self.button9_image, command=lambda: self.display_function(9),
                              borderwidth=0, bg=self.BG, activebackground=self.BG, fg=self.BG)
        self.button9.grid(row=3, column=3, pady=(0, 20))

        self.frame3 = Frame(self)
        self.frame3.config(bg=self.BG)
        self.frame3.pack()

        self.back_button = Button(self.frame3, image=self.back_button_image, command=self.back_one_step, fg=self.BG,
                                  activebackground=self.BG, borderwidth=0, bg=self.BG, height=50, width=100)
        self.back_button.grid(row=0, column=1, padx=(0, 50))

        self.clear_button = Button(self.frame3, image=self.clear_button_image, command=self.clear_field,
                                   activebackground=self.BG, borderwidth=0, fg=self.BG, bg=self.BG)
        self.clear_button.grid(row=0, column=2)

        self.check_answer = Button(self.frame3, image=self.check_answer_button, command=self.check_answer_function,
                                   height=50, width=220, fg=self.BG, bg=self.BG, borderwidth=0,
                                   activebackground=self.BG)
        self.check_answer.grid(row=2, column=1, columnspan=2)

        self.frame4 = Frame(self)
        self.frame4.config(bg=self.BG)
        self.frame4.pack()

        self.start = Button(self.frame4, image=self.start_button_image, height=50, width=150, activebackground=self.BG,
                            fg=self.BG, bg=self.BG, borderwidth=0, command=lambda: self.clear_and_start(2))
        self.start.grid(row=0, column=1)

        self.settings = Button(self.frame4, image=self.settings_button, height=50, width=150, activebackground=self.BG,
                               fg=self.BG, bg=self.BG, borderwidth=0, command=self.settings_function)
        self.settings.grid(row=1, column=1, columnspan=3)

        self.home = Button(self.frame4, image=self.home_button, height=40, width=150, activebackground=self.BG,
                           fg=self.BG, bg=self.BG, borderwidth=0, command=lambda: self.ask_quit('StartPage'))
        self.home.grid(row=2, column=1)

    def display_function(self, guess):
        if len(self.real_numbers) == 0:
            messagebox.showinfo('Input Error', 'You must start the game first!')
        else:
            if len(self.suggested_numbers) >= self.CYCLES:
                messagebox.showinfo('Limit Reached', 'You have reached the limit')
            else:
                self.suggested_numbers.append(guess)
                self.view_part.config(text=self.suggested_numbers)

    def settings_function(self):

        def new_settings():

            if (flash_entry.get()).isnumeric() and (cycles_entry.get()).isnumeric():
                if int(flash_entry.get()) < 50 or int(flash_entry.get()) > 2000:
                    messagebox.showinfo('Value Error', 'Your flash time is either too high or too low')
                elif int(cycles_entry.get()) < self.MIN_CYCLE or int(cycles_entry.get()) > self.MAX_CYCLE:
                    messagebox.showinfo('Value Error', 'Your number of digits to flash is either too high or too low')
                else:
                    self.CYCLES = int(cycles_entry.get())
                    self.FLASH_TIME = int(flash_entry.get())
                    messagebox.showinfo('Saving', 'Your settings have been saved!')
                    settings_window.destroy()

            else:
                messagebox.showinfo('Value Error', 'Please make sure you enter only digits')

        settings_bg = '#008891'

        settings_window = Toplevel()
        settings_window.config(padx=100, pady=100, bg=settings_bg)
        settings_window.title('Settings')

        configure_label = Label(settings_window, text='Configure Your Settings', font=('Georgia', 15, 'bold'),
                                bg=settings_bg, fg='white')
        configure_label.grid(row=0, column=1)

        Label(settings_window, text='Flash time in milliseconds (min: 50, max: 2000): ',
              font=('Georgia', 15), bg=settings_bg, fg='white') \
            .grid(row=1, column=1)

        flash_entry = Entry(settings_window, width=5, font=('Georgia', 13))
        flash_entry.insert(0, f'{self.FLASH_TIME}')
        flash_entry.grid(row=1, column=2)

        Label(settings_window, text='Number of digits to flash (min: 3, max: 50): ',
              font=('Georgia', 15), bg=settings_bg, fg='white') \
            .grid(row=2, column=1)

        cycles_entry = Entry(settings_window, width=5, font=('Georgia', 13))
        cycles_entry.insert(0, f'{self.CYCLES}')
        cycles_entry.grid(row=2, column=2)

        save_button = Button(settings_window, image=self.save_button_image, borderwidth=0, fg=settings_bg,
                             bg=settings_bg, activebackground=settings_bg, command=new_settings)

        save_button.grid(row=3, column=1, pady=(30, 0))

        settings_window.mainloop()

    def clear_and_start(self, timer):
        del self.real_numbers[:]
        self.view_part.config(text='')
        self.current_number.config(text='Ready', fg="black")
        if timer > 0:
            self.after(1000, self.clear_and_start, timer - 1)
        else:
            self.start_function((self.CYCLES - 1) * 2)

    def start_function(self, cycle):
        self.check_answer['state'] = 'disable'
        self.button1['state'] = 'disable'
        self.button2['state'] = 'disable'
        self.button3['state'] = 'disable'
        self.button4['state'] = 'disable'
        self.button5['state'] = 'disable'
        self.button6['state'] = 'disable'
        self.button7['state'] = 'disable'
        self.button8['state'] = 'disable'
        self.button9['state'] = 'disable'
        self.start['state'] = 'disable'
        self.back_button['state'] = 'disable'
        self.clear_button['state'] = 'disable'

        num = random.randint(1, 9)
        if cycle % 2 == 0:
            self.current_number.config(text=num, fg="black")
            self.real_numbers.append(num)
        else:
            self.current_number.config(text='')
        if cycle >= 0:
            self.after(self.FLASH_TIME, self.start_function, cycle - 1)

        else:
            self.current_number.config(text='Done')
            self.view_part.config(text='Type Input')
            self.check_answer['state'] = 'normal'
            self.button1['state'] = 'normal'
            self.button2['state'] = 'normal'
            self.button3['state'] = 'normal'
            self.button4['state'] = 'normal'
            self.button5['state'] = 'normal'
            self.button6['state'] = 'normal'
            self.button7['state'] = 'normal'
            self.button8['state'] = 'normal'
            self.button9['state'] = 'normal'
            self.start['state'] = 'normal'
            self.back_button['state'] = 'normal'
            self.clear_button['state'] = 'normal'

    def check_answer_function(self):
        correct_numbers = ''
        i = 0
        while i < len(self.real_numbers):
            if i != len(self.real_numbers) - 1:

                correct_numbers += f'{self.real_numbers[i]}, '
            else:
                correct_numbers += f'{self.real_numbers[i]}'
            i += 1

        if len(self.real_numbers) == 0:
            messagebox.showinfo('Start Error', 'You must start the game first')
        elif self.suggested_numbers == self.real_numbers:
            self.current_number.config(text='Correct!', fg='green')
        else:

            if len(self.real_numbers) <= 10:

                self.current_number.config(text=f'Wrong!\nCorrect sequence was \n{correct_numbers}', fg='red')

            elif len(self.real_numbers) <= 40:
                self.current_number.config(text=f'Wrong!\nCorrect sequence was \n{correct_numbers[:72]}\n'
                                           f'{correct_numbers[74:142]}', fg='red')
            elif len(self.real_numbers) <= 60:
                self.current_number.config(text=f'Wrong!\nCorrect sequence was \n{correct_numbers[:72]}\n'
                                           f'{correct_numbers[74:143]}'
                                           f'\n{correct_numbers[144:152]}', fg='red')

        del self.real_numbers[:]
        del self.suggested_numbers[:]

    def back_one_step(self):
        if len(self.suggested_numbers) == 0:
            messagebox.showinfo('Delete Error', 'Nothing to delete!')
        else:
            del self.suggested_numbers[-1]
            self.view_part.config(text=self.suggested_numbers)

    def clear_field(self):
        del self.suggested_numbers[:]
        self.view_part.config(text=self.suggested_numbers)

    def ask_quit(self, desired_page):
        if messagebox.askokcancel('Quit', 'Are you sure you want to leave game?'):
            self.controller.set_screen(desired_page)


class RandomImages(Frame):

    # This project is under development
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        label = Label(self, text='Random Images')
        label.pack(padx=10, pady=10)

        button2 = Button(self, text='Back to Home', command=lambda: self.ask_quit('StartPage'))
        button2.pack()

    def ask_quit(self, desired_page):
        if messagebox.askokcancel('Quit', 'Are you sure you want to leave game?'):
            self.controller.set_screen(desired_page)


app = MemoryApp()
app.mainloop()
