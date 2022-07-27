import tkinter as tk


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

    banner_label = tk.Label(banner_frame, text=banner_str, font=('Consolas', 11), justify='left')
    banner_label.pack(fill='both', expand=True)

    add_start_btn(banner_frame)


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
        for index in range(0, 49):
            if variables_list[index].get() == 0:
                checkbuttons_list[index].config(state='disabled')


def add_drawing_machine(frame):
    machine_frame = tk.Frame(frame, bg='black')
    machine_frame.place(relx=0.5025, rely=0.025, relwidth=0.45, relheight=0.625, anchor='nw')


def add_results_board(frame):
    results_frame = tk.Frame(frame, bg='black')
    results_frame.place(relx=0.5, rely=0.7, relwidth=0.7, relheight=0.2, anchor='n')


def add_start_btn(frame):
    start_btn = tk.Button(frame, text='START', font=('Consolas', 14))
    start_btn.config(command=stage_02)
    start_btn.place(relx=1, rely=0, anchor='ne')

    buttons_dict['start'] = start_btn


def add_check_mark_btn(frame):
    check_mark_btn = tk.Button(frame, text=u'\N{check mark}', font=('Consolas', 14, 'bold'))
    check_mark_btn.config(command=stage_03)
    check_mark_btn.grid(row=5, column=10, sticky='nsew')

    tk.Grid.rowconfigure(frame, 5, weight=1)
    tk.Grid.columnconfigure(frame, 10, weight=1)

    buttons_dict['check_mark'] = check_mark_btn


def checkbuttons_state(btn_list, state):
    for checkbutton in btn_list:
        checkbutton.config(state=state)


def stage_01(btn_list, button):
    checkbuttons_state(btn_list, 'disabled')
    button.config(state='disabled')


def stage_02():
    checkbuttons_state(checkbuttons_list, 'active')
    buttons_dict['start'].config(state='disabled')


def stage_03():
    buttons_dict['check_mark'].config(state='disabled')
    checkbuttons_state(checkbuttons_list, 'disabled')

    for variable in variables_list:
        if variable.get():
            selected_numbers.append(variable.get())

    print(selected_numbers)
    stage_04()


def stage_04():
    pass


checkbuttons_list = []
variables_list = []
buttons_dict = {}
selected_numbers = []
drawn_numbers = []

app = tk.Tk()
app.geometry("1200x800")
add_banner(app)
add_drawing_machine(app)
add_results_board(app)
add_numbers(app, checkbuttons_list, variables_list)

stage_01(checkbuttons_list, buttons_dict['check_mark'])

app.mainloop()

