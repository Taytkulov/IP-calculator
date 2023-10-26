import tkinter as tk
import tkinter.messagebox as mb
from tkinter import ttk

win = tk.Tk()

win.title('IP калькулятор')
win.geometry(f"800x350+50+50")
photo = tk.PhotoImage(file='ip.png')

pref = []
mask = []

for i in range(0, 32 + 1):
    pref.append(str(f'/{i}'))
    mask_bin = int(i) * '1' + int(32 - i) * '0'
    mask_bin_append = mask_bin[0:8] + '.' + mask_bin[8:16] + '.' + mask_bin[16:24] + '.' + mask_bin[24:32]
    mask_append = str(int(mask_bin_append[0:8], 2)) + '.' + str(int(mask_bin_append[9:17], 2)) + '.' + str(
        int(mask_bin_append[18:26], 2)) + '.' + str(int(mask_bin_append[27:36], 2))
    mask.append(str(f' ({mask_append})'))

mask_box = []
for q in range(0, 32 + 1):
    mask_box.append(str(pref[q]) + str(mask[q]))


def get_entry():

    checker = True

    ip = entry_ip_entry.get()

    cmb_value = combobox_mask.get()

    ch = '.'


    if str(ip.replace('.', '')).isdigit() is False:
        checker = False
        mb.showerror(
            "Ошибка!",
            "Должно быть введено число! Вы отличный тестировщик!")
        entry_ip.delete(0, tk.END)
        entry_mask.delete(0, tk.END)
        entry_wildcard.delete(0, tk.END)
        entry_ip_entry.delete(0, tk.END)
        entry_net_ip.delete(0, tk.END)
        entry_net_ip_bin.delete(0, tk.END)
        entry_ip_bin.delete(0, tk.END)
        entry_wildcard_bin.delete(0, tk.END)
        entry_mask_bin.delete(0, tk.END)
        entry_prefix.delete(0, tk.END)
        entry_last_ip_bin.delete(0, tk.END)
        entry_last_ip.delete(0, tk.END)
        entry_broadcast.delete(0, tk.END)
        entry_broadcast_bin.delete(0, tk.END)
        entry_host_address.delete(0, tk.END)
        entry_address_available.delete(0, tk.END)
        entry_first_ip.delete(0, tk.END)
        entry_first_ip_bin.delete(0, tk.END)

    indexes = [i for i, c in enumerate(ip) if c == ch]

    if str(ip).count(ch) != 3:
        checker = False
        mb.showerror(
            "Ошибка!",
            "Необходимо ввести четыре октета!!!")

    oct_1 = bin(int(ip[0:indexes[0]])).replace('0b', '')
    oct_2 = bin(int(ip[indexes[0] + 1:indexes[1]])).replace('0b', '')
    oct_3 = bin(int(ip[indexes[1] + 1:indexes[2]])).replace('0b', '')
    oct_4 = bin(int(ip[indexes[2] + 1::])).replace('0b', '')

    a = [int(oct_1), int(oct_2), int(oct_3), int(oct_4)]

    for i in a:
        if int(str(i), 2) > 255:
            checker = False
            mb.showerror(
                "Ошибка!",
                "Ошибка! Введено значение превышающее 255:" + str(int(str(i), 2)))
            entry_ip.delete(0, tk.END)
            entry_mask.delete(0, tk.END)
            entry_wildcard.delete(0, tk.END)
            entry_ip_entry.delete(0, tk.END)
            entry_net_ip.delete(0, tk.END)
            entry_net_ip_bin.delete(0, tk.END)
            entry_ip_bin.delete(0, tk.END)
            entry_wildcard_bin.delete(0, tk.END)
            entry_mask_bin.delete(0, tk.END)
            entry_prefix.delete(0, tk.END)
            entry_last_ip_bin.delete(0, tk.END)
            entry_last_ip.delete(0, tk.END)
            entry_broadcast.delete(0, tk.END)
            entry_broadcast_bin.delete(0, tk.END)
            entry_host_address.delete(0, tk.END)
            entry_address_available.delete(0, tk.END)
            entry_first_ip.delete(0, tk.END)
            entry_first_ip_bin.delete(0, tk.END)

    if str(ip).replace('.', '').isdigit() and checker is True:

        n = []

        for i in a:
            if len(str(i)) < 8:
                n.append('0' * (8 - len(str(i))) + str(i))
            else:
                n.append(str(i))

        bin_address = str(n[0]) + '.' + str(n[1]) + '.' + str(n[2]) + '.' + str(n[3])

        bin_address_calc = '1' + bin_address.replace('.', '')

        prefix = int(cmb_value[1:3])

        host_address = 2 ** (32 - prefix)

        address_available = 2 ** (32 - prefix) - 2

        prefix_bin = int(prefix + 1) * '1' + int(32 - prefix) * '0'
        mask_bin_print = prefix_bin[1:9] + '.' + prefix_bin[9:17] + '.' + prefix_bin[17:25] + '.' + prefix_bin[25:33]
        mask = str(int(prefix_bin[1:9], 2)) + '.' + str(int(prefix_bin[9:17], 2)) + '.' + str(
            int(prefix_bin[17:25], 2)) + '.' + str(int(prefix_bin[25:33], 2))

        wildcard = int(prefix + 1) * '0' + int(32 - prefix) * '1'
        wildcard_print = str(int(wildcard[1:9], 2)) + '.' + str(int(wildcard[9:17], 2)) + '.' + str(
            int(wildcard[17:25], 2)) + '.' + str(int(wildcard[25:33], 2))
        wildcard_bin = wildcard[1:9] + '.' + wildcard[9:17] + '.' + wildcard[17:25] + '.' + wildcard[25:33]

        bin_net_ip = bin(int(bin_address_calc, 2) & int(prefix_bin, 2)).replace('0b1', '')

        bin_net_ip_print = bin_net_ip[0:8] + '.' + bin_net_ip[8:16] + '.' + bin_net_ip[16:24] + '.' + bin_net_ip[24:32]

        net_ip = str(int(bin_net_ip[0:8], 2)) + '.' + str(int(bin_net_ip[8:16], 2)) + '.' + str(
            int(bin_net_ip[16:24], 2)) + '.' + str(int(bin_net_ip[24:32], 2))

        first_ip_bin = str(bin_net_ip).removesuffix('0') + '1'

        first_ip_bin_print = first_ip_bin[0:8] + '.' + first_ip_bin[8:16] + '.' + first_ip_bin[16:24] + '.' + \
            first_ip_bin[24:32]

        first_ip = str(int('1' + first_ip_bin[0:8], 2) - 256) + '.' + str(int(first_ip_bin[8:16], 2)) + '.' + str(
            int(first_ip_bin[16:24], 2)) + '.' + str(int(first_ip_bin[24:32], 2))

        bin_broadcast = bin(int(bin_address_calc, 2) | int(wildcard, 2)).replace('0b1', '')

        bin_broadcast_print = bin_broadcast[0:8] + '.' + bin_broadcast[8:16] + '.' + bin_broadcast[16:24] + '.' + \
            bin_broadcast[24:32]

        broadcast = str(int(bin_broadcast[0:8], 2)) + '.' + str(int(bin_broadcast[8:16], 2)) + '.' + str(
            int(bin_broadcast[16:24], 2)) + '.' + str(int(bin_broadcast[24:32], 2))

        last_ip_bin = bin_broadcast.removesuffix('1') + '0'

        last_ip_bin_print = last_ip_bin[0:8] + '.' + last_ip_bin[8:16] + '.' + last_ip_bin[16:24] + '.' + last_ip_bin[24:32]

        last_ip = str(int(last_ip_bin[0:8], 2)) + '.' + str(int(last_ip_bin[8:16], 2)) + '.' + str(
            int(last_ip_bin[16:24], 2)) + '.' + str(int(last_ip_bin[24:32], 2))

        if prefix == 32:
            host_address = 0
            address_available = 0
            first_ip = 'В сети нет адресов для рабочих хостов'
            last_ip = 'В сети нет адресов для рабочих хостов'
            first_ip_bin_print = 'Двоичное представление невозможно'
            last_ip_bin_print = 'Двоичное представление невозможно'

        entry_ip.delete(0, tk.END)
        entry_ip.insert(0, ip)

        entry_ip_bin.delete(0, tk.END)
        entry_ip_bin.insert(0, bin_address)

        entry_prefix.delete(0, tk.END)
        entry_prefix.insert(0, str(prefix))

        entry_mask.delete(0, tk.END)
        entry_mask.insert(0, mask)
        entry_mask_bin.delete(0, tk.END)
        entry_mask_bin.insert(0, mask_bin_print)

        entry_wildcard.delete(0, tk.END)
        entry_wildcard.insert(0, wildcard_print)
        entry_wildcard_bin.delete(0, tk.END)
        entry_wildcard_bin.insert(0, wildcard_bin)

        entry_net_ip.delete(0, tk.END)
        entry_net_ip.insert(0, net_ip)
        entry_net_ip_bin.delete(0, tk.END)
        entry_net_ip_bin.insert(0, bin_net_ip_print)

        entry_broadcast.delete(0, tk.END)
        entry_broadcast.insert(0, broadcast)
        entry_broadcast_bin.delete(0, tk.END)
        entry_broadcast_bin.insert(0, bin_broadcast_print)

        entry_address_available.delete(0, tk.END)
        entry_address_available.insert(0, address_available)

        entry_first_ip.delete(0, tk.END)
        entry_first_ip.insert(0, first_ip)
        entry_first_ip_bin.delete(0, tk.END)
        entry_first_ip_bin.insert(0, first_ip_bin_print)

        entry_host_address.delete(0, tk.END)
        entry_host_address.insert(0, host_address)

        entry_last_ip.delete(0, tk.END)
        entry_last_ip.insert(0, last_ip)
        entry_last_ip_bin.delete(0, tk.END)
        entry_last_ip_bin.insert(0, last_ip_bin_print)

# 192.168.25.15


label_ip_entry = tk.Label(win, text='IP адрес:')
entry_ip_entry = tk.Entry(win)

label_mask_entry = tk.Label(win, text='Сетевая маска:')
combobox_mask = ttk.Combobox(win, values=mask_box)

button_calc_button = tk.Button(win, text='Вычислить', command=get_entry)

label_ip = tk.Label(win, text='IP адрес:')
entry_ip = tk.Entry(win, fg='purple')
entry_ip_bin = tk.Entry(win,  fg='green')

label_prefix = tk.Label(win, text='Префикс маски сети: ')
entry_prefix = tk.Entry(win, fg='purple', justify='center')

label_wildcard_bin = tk.Label(win, text='Инверсная маска подсети: ')
entry_wildcard = tk.Entry(win, fg='purple')
entry_wildcard_bin = tk.Entry(win, fg='green')

label_entry_prefix_bin = tk.Label(win, text='Маска подсети: ')
entry_mask = tk.Entry(win, fg='purple')
entry_mask_bin = tk.Entry(win, fg='green')

label_net_ip = tk.Label(win, text='Адрес сети: ')
entry_net_ip = tk.Entry(win, fg='purple')
entry_net_ip_bin = tk.Entry(win, fg='green')

label_broadcast = tk.Label(win, text='Широковещательный адрес: ')
entry_broadcast = tk.Entry(win, fg='purple')
entry_broadcast_bin = tk.Entry(win, fg='green')

label_host_address = tk.Label(win, text='Адресов в подсети: ')
entry_host_address = tk.Entry(win, justify='center', fg='purple')

label_address_available = tk.Label(win, text='Доступно адресов: ')
entry_address_available = tk.Entry(win, justify='center', fg='purple')

label_first_ip = tk.Label(win, text='IP адрес первого хоста: ')
entry_first_ip = tk.Entry(win, fg='purple')
entry_first_ip_bin = tk.Entry(win, fg='green')

label_last_ip = tk.Label(win, text='IP адрес последнего хоста: ')
entry_last_ip = tk.Entry(win, fg='purple')
entry_last_ip_bin = tk.Entry(win, fg='green')

label_instruction = tk.Label(win, text='Введите IP адрес в формате "123.456.789.0"',  justify='center')

label_ip_entry.grid(row=0, column=0, stick='we', padx=5, pady=3)
entry_ip_entry.grid(row=1, column=0, stick='we', padx=5, pady=3)

label_mask_entry.grid(row=0, column=1, stick='we', padx=5, pady=3)
combobox_mask.grid(row=1, column=1, stick='we', padx=5, pady=3)

button_calc_button.grid(row=1, column=2, stick='we', padx=5, pady=3, rowspan=1)

label_ip.grid(row=2, column=0, stick='w', padx=5, pady=3)
entry_ip.grid(row=2, column=1, stick='we', padx=5, pady=3)
entry_ip_bin.grid(row=2, column=2, stick='we', padx=5, pady=3)

label_prefix.grid(row=3, column=0, stick='w', padx=5, pady=3)
entry_prefix.grid(row=3, column=1, stick='we', padx=5, pady=3, columnspan=2)

label_entry_prefix_bin.grid(row=4, column=0, stick='w', padx=5, pady=3)
entry_mask.grid(row=4, column=1, stick='we', padx=5, pady=3)
entry_mask_bin.grid(row=4, column=2, stick='we', padx=5, pady=3)

label_wildcard_bin.grid(row=5, column=0, stick='w', padx=5, pady=3)
entry_wildcard.grid(row=5, column=1, stick='we', padx=5, pady=3)
entry_wildcard_bin.grid(row=5, column=2, stick='we', padx=5, pady=3)


label_net_ip.grid(row=6, column=0, stick='w', padx=5, pady=3)
entry_net_ip.grid(row=6, column=1, stick='we', padx=5, pady=3)
entry_net_ip_bin.grid(row=6, column=2, stick='we', padx=5, pady=3)

label_broadcast.grid(row=7, column=0, stick='w', padx=5, pady=3)
entry_broadcast.grid(row=7, column=1, stick='we', padx=5, pady=3)
entry_broadcast_bin.grid(row=7, column=2, stick='we', padx=5, pady=3)

label_host_address.grid(row=8, column=0, stick='w', padx=5, pady=3)
entry_host_address.grid(row=8, column=1, stick='we', padx=5, pady=3, columnspan=2)

label_address_available.grid(row=9, column=0, stick='w', padx=5, pady=3)
entry_address_available.grid(row=9, column=1, stick='we', padx=5, pady=3, columnspan=2)

label_first_ip.grid(row=10, column=0, stick='w', padx=5, pady=3)
entry_first_ip.grid(row=10, column=1, stick='we', padx=5, pady=3)
entry_first_ip_bin.grid(row=10, column=2, stick='we', padx=5, pady=3)

label_last_ip.grid(row=11, column=0, stick='w', padx=5, pady=3)
entry_last_ip.grid(row=11, column=1, stick='we', padx=5, pady=3)
entry_last_ip_bin.grid(row=11, column=2, stick='we', padx=5, pady=3)

label_instruction.grid(row=0, column=2, stick = 'we', padx=5, pady=10)

win.grid_columnconfigure(1, minsize=240)
win.grid_columnconfigure(2, minsize=240)

win.iconphoto(False, photo)
win.mainloop()

