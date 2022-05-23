#  Copyright (c) 2022.
#  __author__ = 'Virgil Hoover
#  __version__ = '1.0.0'
""" A Host Naming Generator for network devices. """
import sys
import tkinter as tk
from os import getcwd
from re import sub


def name_check(name: str) -> str:
    """ Check if the current name is already in use.
    :param name: The device name to compare.
    :returns the next available name. """
    names = []
    possibities = []
    file = getcwd() + r'\names.txt'
    suffix = 0
    if name.find(' ') != -1:
        prefix = name.replace(' ', '')
    else:
        prefix = name
    with open(file) as file_reader:
        names = file_reader.readlines()
    for item in names:
        if item[:-3].lower().find(prefix) != -1:
            possibities.append(item)
            suffix = str(sub(r'[0-9]+$',
            lambda x: f'{str(int(x.group()) +  1).zfill(len(x.group()))}',
                             item))
            new_name = str(suffix)
        else:
            suffix = '01'
            new_name = prefix + str(suffix)
    with open(file, 'a') as file_writer:
        file_writer.write(new_name + '\n')
    possibities.clear()
    names.clear()
    return new_name


def configure_name(*args) -> None:
    """ This utility method gathers data from various fields and combines
        parts to make a string representaion of a device name minus the counter
        indicator.
    """
    device_name = str(location_entry.get())[0:3] + '-' \
                  + str(os_choices.get())[0] + '-' \
                  + str(owner_entry.get())[0:1] + '-' \
                  + str(purpose_choices.get())[0:4]
    result = name_check(device_name.lower())
    new_device_name = device_name_result_lbl.configure(text=result)


if __name__ == '__main__':
    window_root = tk.Tk()
    window_root.title(__name__)
    window_root.geometry('250x290+250+250')
    window_root.resizable(False, False)
    window_root.overrideredirect(1)
    night_bg = '#000000'
    night_fg = '#66FFFF'
    window_root.option_add('*Background', night_bg)
    window_root.option_add('*Foreground', night_fg)
    window_root.configure(background=night_bg,
                          highlightbackground=night_bg, highlightcolor=night_fg)

    entry_frame = tk.Frame(window_root).grid(row=0, column=0)
    display_frame = tk.Frame(window_root).grid(row=5, column=0)

    location_lbl = tk.Label(entry_frame, text='Location:', justify='left')
    location_entry = tk.Entry(entry_frame, justify='left')
    os_lbl = tk.Label(entry_frame, text='Operating System:', justify='left')
    os_choices = tk.Variable(window_root)
    os = {'Linux', 'Windows', 'Mac OSX'}
    os_choices.set('OS')
    os_choice = tk.OptionMenu(entry_frame, os_choices, *sorted(os))
    os_choice['highlightthickness'] = 0
    owner_lbl = tk.Label(entry_frame, text='Owner:', justify='left')
    owner_entry = tk.Entry(entry_frame, justify='left')
    purpose_lbl = tk.Label(entry_frame, text='Device Purpose:', justify='left')
    purpose_choices = tk.Variable(window_root)
    purposes = {'Web_Server',
                'Print_Server',
                'Database_Server',
                'Multipurpose',
                'Network_Storgae',
                'Printer',
                'Phone',
                'Tablet',
                'Gaming_System',
                'Development',
                'Programming'}
    purpose_choices.set('Purpose')
    purpose_choice = tk.OptionMenu(entry_frame, purpose_choices,
                                   *sorted(purposes))
    purpose_choice['highlightthickness'] = 0
    generate_brn = tk.Button(entry_frame, text='Generate',
                             command=lambda: configure_name())

    location_lbl.grid(row=0, column=0, sticky='ensw', padx=5, pady=5)
    location_entry.grid(row=0, column=1, sticky='ensw', padx=5, pady=5)
    os_lbl.grid(row=1, column=0, sticky='ensw', padx=5, pady=5)
    os_choice.grid(row=1, column=1, sticky='ensw', padx=5, pady=5)
    owner_lbl.grid(row=2, column=0, sticky='ensw', padx=5, pady=5)
    owner_entry.grid(row=2, column=1, sticky='ensw', padx=5, pady=5)
    purpose_lbl.grid(row=3, column=0, sticky='ensw', padx=5, pady=5)
    purpose_choice.grid(row=3, column=1, sticky='ensw', padx=5, pady=5)
    generate_brn.grid(row=4, column=0, columnspan=2, sticky='ensw', padx=5,
                      pady=5)

    device_name_lbl = tk.Label(display_frame, text='Device Name:')
    device_name_result_lbl = tk.Label(display_frame)
    close_btn = tk.Button(display_frame, text='Close', command=sys.exit)

    device_name_lbl.grid(row=5, column=0, columnspan=2, sticky='ensw', padx=5,
                         pady=10)
    device_name_result_lbl.grid(row=6, column=0, columnspan=2, sticky='ensw',
                                padx=5, pady=10)
    close_btn.grid(row=7, column=0, columnspan=2, sticky='ensw', padx=5, pady=5)

    window_root.mainloop()
