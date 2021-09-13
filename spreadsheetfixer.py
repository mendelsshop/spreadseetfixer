import datetime
import tkinter





def output():
    file = e1.get()
    col = int(e2.get())
    output_file_name = e3.get()
    if not e3.get():
        output_file_name = f'{datetime.datetime.now().date().isoformat()}-{datetime.datetime.now().time().strftime("%I-%M-%S-%p")}'
    with open(file,'r') as read_file:
        with open(f'{output_file_name}.csv', 'w') as write_file:
            for line in read_file:
                write_line = [x for x in line.split(',',col)]
                for z in write_line:
                    if write_line.index(z) < col:
                        write_file.write(z) 
                        if write_line.index(z) <col-1:
                            write_file.write(',')
                write_file.write('\n')


def main():
    root = tkinter.Tk()
    global e1,e2,e3
    file_label = tkinter.Label(root,text='upload file:').grid(row=0)
    e1 = tkinter.Entry(root)
    e1.grid(row=1)
    name_label1 = tkinter.Label(root,text = 'how many columns do you want to include from the csv file:').grid(row=2)
    e2 = tkinter.Entry(root)
    e2.grid(row=3)
    name_label = tkinter.Label(root,text = 'what do you want to name the csv:').grid(row=4)
    e3 = tkinter.Entry(root)
    e3.grid(row=5,column=0)
    output_button_1 = tkinter.Button(root,text = 'enter',command = output).grid(row=5,column=1)
    root.mainloop()


if __name__ == '__main__':
    main()
            