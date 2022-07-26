import tkinter as tk


def add_banner():
    banner_str = """
    ██╗      ██████╗ ████████╗████████╗ ██████╗ 
    ██║     ██╔═══██╗╚══██╔══╝╚══██╔══╝██╔═══██╗ v.2.0
    ██║     ██║   ██║   ██║      ██║   ██║   ██║
    ██║     ██║   ██║   ██║      ██║   ██║   ██║
    ███████╗╚██████╔╝   ██║      ██║   ╚██████╔╝ 
    ╚══════╝ ╚═════╝    ╚═╝      ╚═╝    ╚═════╝ by Mateusz Meksuła  
    """

    banner_frame = tk.Frame(app, bd=3, bg='black')
    banner_frame.place(relx=0.025, rely=0.025, relwidth=0.45, relheight=0.2, anchor='nw')

    banner_label = tk.Label(banner_frame, text=banner_str, font=('Consolas', 11), justify='left')
    banner_label.pack(fill='both', expand=True)

    add_start_btn(banner_frame)


def add_numbers():
    numbers_frame = tk.Frame(app, bd=3, bg='black')
    numbers_frame.place(relx=0.025, rely=0.25, relwidth=0.45, relheight=0.4, anchor='nw')

    num = 1
    num_dict = {}

    for row in range(1, 6):
        for column in range(1, 11):
            num_dict[f"{num}"] = \
                tk.Checkbutton(numbers_frame, text=num, indicatoron=False, font=('Consolas', 13))
            num_dict[f"{num}"].grid(row=row, column=column, sticky='nsew')

            tk.Grid.rowconfigure(numbers_frame, row, weight=1)
            tk.Grid.columnconfigure(numbers_frame, column, weight=1)

            num += 1
            if num == 50:
                break


def add_drawing_machine():
    machine_frame = tk.Frame(app, bg='black')
    machine_frame.place(relx=0.5025, rely=0.025, relwidth=0.45, relheight=0.625, anchor='nw')


def add_results_board():
    results_frame = tk.Frame(app, bg='black')
    results_frame.place(relx=0.5, rely=0.7, relwidth=0.7, relheight=0.2, anchor='n')


def add_start_btn(frame):
    start_btn = tk.Button(frame, text='START', font=('Consolas', 14))
    start_btn.place(relx=1, rely=0, anchor='ne')


app = tk.Tk()
app.geometry("1200x800")
add_banner()
add_numbers()
add_drawing_machine()
add_results_board()

app.mainloop()
