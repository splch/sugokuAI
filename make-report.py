from fpdf import FPDF
from os import remove


name = 'Spence Churchill'
ucinetid = '89986429'
email = 'churchis@uci.edu'

partner_name = 'Emily Doan'
partner_ucinetid = '19169772'
partner_email = 'edoan2@uci.edu'

language = 'Python'

heuristics = ['']


def generate_intro(pdf: FPDF):
    pdf.multi_cell(200, 10, f'My name, ID#, UCInetID: {name}, {ucinetid}, {email}')
    pdf.multi_cell(200, 10, f'Partner name, ID#, UCInetID: {partner_name}, {partner_ucinetid}, {partner_email}')
    pdf.multi_cell(200, 10, f'The programming language(s) you used in your project: {language}')
    pdf.multi_cell(200, 10, f'What, if any, additional heuristics did you use in your Tournament Final AI?\n\t{",".join(heuristics)}')
    pdf.multi_cell(200, 10, 'By turning in this assignment, I/We do affirm that we did not copy any code, text, or data except course material provided to us by the textbook, class website, class gitlab, or teaching staff.')


if __name__ == "__main__":
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=14)

    generate_intro(pdf)

    pdf.output('doc/report.pdf')

