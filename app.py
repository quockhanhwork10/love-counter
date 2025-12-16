import streamlit as st
from datetime import datetime, date

st.title("💖 Đếm số ngày yêu nhau 💖")

ten_1 = st.text_input("Tên của bạn")
ten_2 = st.text_input("Tên người yêu")

ngay_bat_dau = st.date_input("Ngày bắt đầu yêu")

if st.button("💘 Tính số ngày yêu"):
    so_ngay_yeu = (date.today() - ngay_bat_dau).days

    st.success(
        f"💞 {ten_1} và {ten_2} đã yêu nhau {so_ngay_yeu} ngày 💞"
    )