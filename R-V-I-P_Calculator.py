import streamlit as st

# Ρύθμιση Σελίδας
st.set_page_config(page_title="R-V-I-P Calculator", page_icon="⚡")

st.title("⚡ Ηλεκτρολογικός Υπολογιστής R-V-I-P")
st.markdown("---")

# Χρήση Columns για να μοιάζει με το Layout του Form σου
col1, col2 = st.columns(2)

# --- ΕΝΟΤΗΤΑ R ---
with col1:
    st.subheader("🔍 Υπολογισμός Αντίστασης (R)")
    v_for_r = st.number_input("Τάση V (Volt):", key="v_r")
    i_for_r = st.number_input("Ένταση I (Ampere):", key="i_r")
    if st.button("Υπολόγισε R", help="R = V / I"):
        if i_for_r != 0:
            st.success(f"Αποτέλεσμα R: {v_for_r / i_for_r:.2f} Ω")
        else:
            st.error("Σφάλμα: Διαίρεση με το μηδέν!")

# --- ΕΝΟΤΗΤΑ V ---
with col2:
    st.subheader("🔍 Υπολογισμός Τάσης (V)")
    i_for_v = st.number_input("Ένταση I (Ampere):", key="i_v")
    r_for_v = st.number_input("Αντίσταση R (Ohm):", key="r_v")
    if st.button("Υπολόγισε V", help="V = I * R"):
        st.success(f"Αποτέλεσμα V: {i_for_v * r_for_v:.2f} V")

st.markdown("---")

col3, col4 = st.columns(2)

# --- ΕΝΟΤΗΤΑ I ---
with col3:
    st.subheader("🔍 Υπολογισμός Έντασης (I)")
    v_for_i = st.number_input("Τάση V (Volt):", key="v_i")
    r_for_i = st.number_input("Αντίσταση R (Ohm):", key="r_i")
    if st.button("Υπολόγισε I", help="I = V / R"):
        if r_for_i != 0:
            st.success(f"Αποτέλεσμα I: {v_for_i / r_for_i:.2f} A")
        else:
            st.error("Σφάλμα: Διαίρεση με το μηδέν!")

# --- ΕΝΟΤΗΤΑ P ---
with col4:
    st.subheader("🔍 Υπολογισμός Ισχύος (P)")
    method = st.radio("Επιλέξτε τύπο:", ["P = V * I", "P = I² * R"])
    
    if method == "P = V * I":
        v_p = st.number_input("Τάση V (Volt):", key="v_p1")
        i_p = st.number_input("Ένταση I (Ampere):", key="i_p1")
        if st.button("Υπολόγισε P (V*I)"):
            st.success(f"Αποτέλεσμα P: {v_p * i_p:.2f} W")
    else:
        i_p2 = st.number_input("Ένταση I (Ampere):", key="i_p2")
        r_p2 = st.number_input("Αντίσταση R (Ohm):", key="r_p2")
        if st.button("Υπολόγισε P (I²*R)"):
            st.success(f"Αποτέλεσμα P: {(i_p2**2) * r_p2:.2f} W")

st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Ohms_law_wheel_W_V_I_R.svg/1024px-Ohms_law_wheel_W_V_I_R.svg.png", use_container_width=True)
st.sidebar.write("© 2026 Dimitrios Kavallieros")
