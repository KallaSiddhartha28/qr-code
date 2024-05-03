import qrcode

def generate_qr_code(name, roll_number, branch, cgpa, filename):
    data = f"Name: {name}\nRoll Number: {roll_number}\nBranch: {branch}\nCGPA: {cgpa}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
    name = input("Enter your name: ")
    roll_number = input("Enter your roll number: ")
    branch = input("Enter your branch: ")
    cgpa = input("Enter your CGPA: ")
    filename = input("Enter filename for the QR code image (with extension, e.g., 'my_qr_code.png'): ")
    generate_qr_code(name, roll_number, branch, cgpa, filename)
    print("QR code generated successfully!")
