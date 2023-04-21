from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas


# Create a new PDF file
pdf_file = canvas.Canvas("labels.pdf", pagesize=A4)


# Fetch the addresses from a data source
addresses = [
    {"enrollment": "A22BC242001     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
    {"enrollment": "A22BC242002     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
    {"enrollment": "A22BC242003     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
    {"enrollment": "A22BC242004     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
    {"enrollment": "A22BC242005     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
    {"enrollment": "A22BC242006     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
    {"enrollment": "A22BC242007     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
    {"enrollment": "A22BC242008     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
    {"enrollment": "A22BC242009     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
    {"enrollment": "A22BC242010     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
    {"enrollment": "A22BC242011     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
    {"enrollment": "A22BC242012     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
    {"enrollment": "A22BC242013     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
    {"enrollment": "A22BC242014     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
    {"enrollment": "A22BC242015     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
    {"enrollment": "A22BC242016     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
    {"enrollment": "A22BC242017     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
    {"enrollment": "A22BC242018     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
    {"enrollment": "A22BC242019     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
    {"enrollment": "A22BC242020     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
    {"enrollment": "A22BC242021     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
    {"enrollment": "A22BC242022     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
   {"enrollment": "A22BC242021     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
    {"enrollment": "A22BC242022     B.COM(G)", "name": "BOLISETTI DURGA BHAVANI", "father":'S/O:D/O: BOLISETTI SRINIVASA RAO',"dno":'1-148 MAGATAPALLI',"village":'MAGATAPALLI - MAMIDIKUDURU (Mandal)',"dist":"East Godavari - 533248","ph":'9963775986'},
   
]

for page_index in range((len(addresses) - 1) // 12 + 1):
    # Add a new page to the PDF file
    pdf_file.showPage()
    pdf_file.setFont("Helvetica",9)
    # Define the size of each cell
    cell_width = 95 * mm        # worked value 100
    cell_height = 27 * mm


    # Iterate over the addresses on this page and add them to each cell
    for index in range(page_index * 12, min((page_index + 1) * 12, len(addresses))):
        address = addresses[index]

        # Calculate the coordinates of the current cell
        row = (index - page_index * 12) // 2
        col = (index - page_index * 12) % 2
        x = 5 * mm + col * (cell_width + 10 * mm)
        y = 250 * mm - row * (cell_height + 20 * mm)

        # Add the address to the current cell
        pdf_file.drawString(x + 5 * mm, y + 31 * mm, address["enrollment"])
        pdf_file.drawString(x + 5 * mm, y + 26 * mm, address["name"])
        pdf_file.drawString(x + 5 * mm, y + 21 * mm, address["father"])
        pdf_file.drawString(x + 5 * mm, y + 16 * mm, address["dno"])
        pdf_file.drawString(x + 5 * mm, y + 11 * mm, address["village"])
        pdf_file.drawString(x + 5 * mm, y + 6 * mm, address["dist"])
        pdf_file.drawString(x + 5 * mm, y + 1 * mm, address["ph"])

# Save the PDF file
pdf_file.save()

# # Iterate over the addresses and add them to each cell
# for index, address in enumerate(addresses):
#     # Calculate the coordinates of the current cell
#     row = index // 2
#     col = index % 2
#     x = 5 * mm + col * (cell_width + 10 * mm)
#     y = 250 * mm - row * (cell_height + 20 * mm)
#     # Add the address to the current cell
#     pdf_file.drawString(x + 5 * mm, y + 31 * mm, address["enrollment"])
#     pdf_file.drawString(x + 5 * mm, y + 26 * mm, address["name"])
#     pdf_file.drawString(x + 5 * mm, y + 21 * mm, address["father"])
#     pdf_file.drawString(x + 5 * mm, y + 16 * mm, address["dno"])
#     pdf_file.drawString(x + 5 * mm, y + 11 * mm, address["village"])
#     pdf_file.drawString(x + 5 * mm, y + 6 * mm, address["dist"])
#     pdf_file.drawString(x + 5 * mm, y + 1 * mm, address["ph"])

# # Save the PDF file
# pdf_file.save()