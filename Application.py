import streamlit as s
import qrcode

s.title("QRCode Generator")
orcode = s.text_input("Enter the URL")  


app_name = s.text_input("Enter File Name (any new name) : ")

if s.button('GENERATE'):
    makeqr = qrcode.make(orcode)
    makeqr.save(f"{app_name}.png")

    s.success("QR code genereted SUCESSFULLY")
    s.image(f"{app_name}.png")



    


