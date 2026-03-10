import streamlit as st

# Ρύθμιση Σελίδας
st.set_page_config(page_title="R-V-I-P Calculator", layout="wide")

st.title("⚡ Ηλεκτρολογικός Υπολογιστής R-V-I-P (Python Edition)")
st.write("Εισάγετε τις τιμές στα αντίστοιχα πεδία για να εκτελεστούν οι υπολογισμοί.")

# Χωρισμός σε 2 στήλες (όπως το UI που είχες)
col1, col2 = st.columns(2)

with col1:
    # Υπολογισμός R
    st.subheader("🔍 Υπολογισμός Αντίστασης (R)")
    v_r = st.number_input("Τάση V (Volt):", key="v_r", min_value=0.0)
    i_r = st.number_input("Ένταση I (Ampere):", key="i_r", min_value=0.0)
    if st.button("Υπολόγισε R"):
        if i_r > 0:
            st.success(f"R = {v_r / i_r:.4f} Ω")
        else:
            st.error("Η ένταση πρέπει να είναι > 0")

    # Υπολογισμός I
    st.subheader("🔍 Υπολογισμός Έντασης (I)")
    v_i = st.number_input("Τάση V (Volt):", key="v_i", min_value=0.0)
    r_i = st.number_input("Αντίσταση R (Ohm):", key="r_i", min_value=0.0)
    if st.button("Υπολόγισε I"):
        if r_i > 0:
            st.success(f"I = {v_i / r_i:.4f} A")
        else:
            st.error("Η αντίσταση πρέπει να είναι > 0")

with col2:
    # Υπολογισμός V
    st.subheader("🔍 Υπολογισμός Τάσης (V)")
    i_v = st.number_input("Ένταση I (Ampere):", key="i_v", min_value=0.0)
    r_v = st.number_input("Αντίσταση R (Ohm):", key="r_v", min_value=0.0)
    if st.button("Υπολόγισε V"):
        st.success(f"V = {i_v * r_v:.4f} V")

    # Υπολογισμός P (V*I)
    st.subheader("🔍 Υπολογισμός Ισχύος (P = V * I)")
    v_p = st.number_input("Τάση V (Volt):", key="v_p", min_value=0.0)
    i_p = st.number_input("Ένταση I (Ampere):", key="i_p", min_value=0.0)
    if st.button("Υπολόγισε P"):
        st.success(f"P = {v_p * i_p:.4f} W")

    # Υπολογισμός P (I²*R)
    st.subheader("🔍 Υπολογισμός Ισχύος (P = I² * R)")
    i_p2 = st.number_input("Ένταση I (Ampere):", key="i_p2", min_value=0.0)
    r_p2 = st.number_input("Αντίσταση R (Ohm):", key="r_p2", min_value=0.0)
    if st.button("Υπολόγισε P (I²*R)"):
        st.success(f"P = {(i_p2**2) * r_p2:.4f} W")

st.divider()
st.info("💡 Για να βγει online: Σύνδεσε το GitHub σου με το share.streamlit.io")
