import tkinter as tk
import random
import time


def add_banner(frame):
    banner_str = """
    ██╗      ██████╗ ████████╗████████╗ ██████╗ 
    ██║     ██╔═══██╗╚══██╔══╝╚══██╔══╝██╔═══██╗ v.2.0
    ██║     ██║   ██║   ██║      ██║   ██║   ██║
    ██║     ██║   ██║   ██║      ██║   ██║   ██║
    ███████╗╚██████╔╝   ██║      ██║   ╚██████╔╝ 
    ╚══════╝ ╚═════╝    ╚═╝      ╚═╝    ╚═════╝ by Mateusz Meksuła  
    """

    banner_frame = tk.Frame(frame, bd=3, bg='black')
    banner_frame.place(relx=0.025, rely=0.025, relwidth=0.45, relheight=0.2, anchor='nw')

    banner_label = tk.Label(banner_frame, text=banner_str, font=('Consolas', 11, 'bold'))
    banner_label.config(background='#5D6D7E', fg='#F1C40F', justify='left')
    banner_label.pack(fill='both', expand=True)

    add_start_btn(banner_frame)
    add_play_again_btn(banner_frame)


def add_numbers(frame, num_list, var_list):
    numbers_frame = tk.Frame(frame, bd=3, bg='black')
    numbers_frame.place(relx=0.025, rely=0.25, relwidth=0.45, relheight=0.4, anchor='nw')

    num = 1

    for row in range(1, 6):
        for column in range(1, 11):
            var_list.append(tk.IntVar())

            num_list.append(tk.Checkbutton(numbers_frame, text=num, indicatoron=False))
            num_list[num-1].config(font=('Consolas', 12, 'bold'), selectcolor='yellow')
            num_list[num-1].config(variable=var_list[num-1], onvalue=num, offvalue=None)
            num_list[num-1].config(command=get_user_numbers)
            num_list[num-1].grid(row=row, column=column, sticky='nsew')

            tk.Grid.rowconfigure(numbers_frame, row, weight=1)
            tk.Grid.columnconfigure(numbers_frame, column, weight=1)

            num += 1
            if num == 50:
                break

    add_check_mark_btn(numbers_frame)


def get_user_numbers():

    numbers_count = 0
    for variable in variables_list:
        if variable.get():
            numbers_count += 1

    if numbers_count < 6:
        buttons_dict['check_mark'].config(state='disabled')
        for index in range(0, 49):
            if variables_list[index].get() == 0:
                checkbuttons_list[index].config(state='active')

    if numbers_count == 6:
        buttons_dict['check_mark'].config(state='active')
        buttons_dict['check_mark'].config(activebackground='light green')
        buttons_dict['check_mark'].config(background='light green')
        for index in range(0, 49):
            if variables_list[index].get() == 0:
                checkbuttons_list[index].config(state='disabled')


def add_drawing_machine(frame):
    machine_frame = tk.Frame(frame, bd=3, bg='black')
    machine_frame.place(relx=0.5025, rely=0.025, relwidth=0.45, relheight=0.625, anchor='nw')

    machine_label = tk.Label(machine_frame, text=animation_frames[-1], bg='light yellow')
    machine_label.config(font=('Consolas', 7), justify='left')
    machine_label.pack(fill='both', expand=True)
    global animation_label
    animation_label = machine_label


def add_results_board(frame):
    results_border = tk.Frame(frame, bd=3, bg='black')
    results_border.place(relx=0.5, rely=0.7, relwidth=0.7, relheight=0.2, anchor='n')

    results_frame = tk.Frame(results_border, bd=3, bg='#D4AC0D')
    results_frame.pack(fill='both', expand=True)

    for index in range(0, 6):
        results_labels.append(tk.Label(results_frame, bd=3, relief='solid'))
        results_labels[index].config(font=('Consolas', 25, 'bold'))
        results_labels[index].place(relx=(0.1 + index*0.16), rely=0.1, relwidth=0.10, relheight=0.8, anchor='n')


def add_start_btn(frame):
    start_btn = tk.Button(frame, text='START', font=('Consolas', 14, 'bold'))
    start_btn.config(command=stage_02)
    start_btn.place(relx=1, rely=0, anchor='ne')

    buttons_dict['start'] = start_btn


def add_play_again_btn(frame):
    play_again_btn = tk.Button(frame, text='PLAY AGAIN', font=('Consolas', 14, 'bold'))
    play_again_btn.config(command=play_again)
    play_again_btn.place(relx=1, rely=0.4, anchor='ne')

    buttons_dict['play_again'] = play_again_btn


def add_check_mark_btn(frame):
    check_mark_btn = tk.Button(frame, text=u'\N{check mark}', font=('Consolas', 10, 'bold'))
    check_mark_btn.config(command=stage_03)
    check_mark_btn.grid(row=5, column=10, sticky='nsew')

    tk.Grid.rowconfigure(frame, 5, weight=1)
    tk.Grid.columnconfigure(frame, 10, weight=1)

    buttons_dict['check_mark'] = check_mark_btn


def checkbuttons_state(btn_list, state):
    for checkbutton in btn_list:
        checkbutton.config(state=state)


def add_frames_to_list():
    for frame in range(1, 5):
        with open(f'frames/{frame}.txt') as frame_file:
            animation_frames.append(frame_file.read())


def machine_animation(label):
    for frame in animation_frames:
        time.sleep(0.5)
        label.config(text=frame)
        app.update()


def stage_01(btn_list):
    checkbuttons_state(btn_list, 'disabled')
    buttons_dict['check_mark'].config(state='disabled')
    buttons_dict['play_again'].config(state='disabled')


def stage_02():
    checkbuttons_state(checkbuttons_list, 'active')
    buttons_dict['start'].config(state='disabled')


def stage_03():
    buttons_dict['check_mark'].config(state='disabled')
    checkbuttons_state(checkbuttons_list, 'disabled')

    for variable in variables_list:
        if variable.get():
            selected_numbers.append(variable.get())

    stage_04()


def stage_04():

    for i in range(0, 6):
        machine_animation(animation_label)
        drawn_number = random.choice(available_numbers)
        drawn_numbers.append(drawn_number)
        available_numbers.remove(drawn_number)

        results_labels[i].config(text=drawn_number)
        if drawn_number in selected_numbers:
            results_labels[i].config(bg='light green')

        app.update()

    buttons_dict['play_again'].config(state='active')


def play_again():
    buttons_dict['play_again'].config(state='disabled')
    buttons_dict['check_mark'].config(activebackground='SystemButtonFace')
    buttons_dict['check_mark'].config(background='SystemButtonFace')

    for index in range(0, 49):
        checkbuttons_list[index].config(state='active')
        variables_list[index].set(0)

    for index in range(0, 6):
        selected_numbers.pop(0)

    for label in results_labels:
        label.config(bg='white', text='')

    global available_numbers
    available_numbers = list(range(1, 50))


checkbuttons_list = []
variables_list = []
buttons_dict = {}
selected_numbers = []
drawn_numbers = []
results_labels = []
available_numbers = list(range(1, 50))
animation_frames = []

app = tk.Tk()
app.geometry("1200x600")
app.config(bg='light blue')
animation_label = tk.Label()
add_banner(app)
add_frames_to_list()
add_drawing_machine(app)
add_results_board(app)
add_numbers(app, checkbuttons_list, variables_list)

stage_01(checkbuttons_list)
app.mainloop()
