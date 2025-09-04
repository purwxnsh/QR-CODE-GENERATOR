import streamlit as s
import qrcode

st.markdown("<h1 style='color: red;'>⚡ QR Code Generator ⚡</h1>", unsafe_allow_html=True)
orcode = s.text_input("Enter the URL or Link : ")  


app_name = s.text_input("Enter File Name : ( give your QR Code a name ) : ")

if s.button('GENERATE'):
    makeqr = qrcode.make(orcode)
    makeqr.save(f"{app_name}.png")

    s.success("QR code GENERATED SUCESSFULLY ✅")
    s.image(f"{app_name}.png")



    







