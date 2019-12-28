from tkinter import *
from tkinter import messagebox
from fpdf import FPDF
import webbrowser
from fpdf import FPDF, HTMLMixin


class HTML2PDF(FPDF, HTMLMixin):
    pass


root = Tk()
root.title("GUI на Pythonn")


def get_pdf(spacing=1):
    html = '''<h1 align="center">PDF CV</h1>
    <p>This is regular text</p>
    <p>You can also <b>bold</b>, <i>italicize</i> or <u>underline</u><br><br>
    '''
    pdf = HTML2PDF()
    pdf.add_page()
    pdf.write_html(html)

    data = [['First Name', 'Last Name', 'email', 'zip'],
            [name.get(), surname.get(), 'mike@somewhere.com', '55555']
            ]

    col_width = pdf.w / 4.5
    row_height = pdf.font_size
    for row in data:
        for item in row:
            pdf.cell(col_width, row_height * spacing,
                     txt=item, border=1)
        pdf.ln(row_height * spacing)

    pdf.output('simple_table.pdf')
    webbrowser.open('simple_table.pdf')


name = StringVar()
surname = StringVar()

name_label = Label(text="Name:")
surname_label = Label(text="Surname:")

name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")

name_entry = Entry(textvariable=name)
surname_entry = Entry(textvariable=surname)

name_entry.grid(row=0, column=1, padx=5, pady=5)
surname_entry.grid(row=1, column=1, padx=5, pady=5)

message_button = Button(text="Get pdf", command=get_pdf)
message_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

root.mainloop()
