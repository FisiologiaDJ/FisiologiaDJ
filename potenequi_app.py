import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Potencial de equilibrio iónico", page_icon="⚡")
st.markdown("<h3 style='text-align: center;'>⚡Calculadora del potencial de equilibrio iónico⚡      (Ecuación de Nernst)</h3>", unsafe_allow_html=True)

with st.expander("💡¿Qué tanto sabes de la Ecuación de Nernst?"):
    st.markdown("""
    ¿Sabias que la ecuación de Nernst es de gran utilidad en fisiología para calcular el potencial de equilibrio iónico? Este valor representa la energía eléctrica que compensa a la energía química, esto nos ayuda a entender mejor el potencial de membrana en reposo y el potencial de acción. ⚡Cuando se alcanza el voltaje del potencial de equilibrio iónico el flujo neto del ion es cero.  
    """)
with st.expander("📖 Instrucciones:"):
    st.markdown("""
    1. Elige el ion de tu interés, puedes elegir entre los iones sodio, potasio, cloro y calcio. 
    2. Establece la concentración extra e intracelular. 
    3. Elige la temperatura de tu preferencia desplazando las barras hasta obtener el valor deseado. 
    4. 🤩Observa cómo se actualiza el potencial de equilibrio iónico resultante en la gráfica y en valor numérico en milivolts (mV). Dejamos para ti la ecuación de Nernst al final para que puedas repasarla.
    """)

ion = st.selectbox("Ion", ["Na⁺", "K⁺", "Cl⁻", "Ca²⁺"])

if ion == "Ca²⁺":
    st.markdown("### Concentraciones para calcio")
    conc_out = st.number_input(
        "Concentración extracelular (mM)", 
        value=5.0, 
        min_value=0.001, 
        step=0.1,
        format="%.3f"
    )
    conc_in_nM = st.number_input(
        "Concentración intracelular (nM)", 
        value=500.0, 
        min_value=1.0, 
        step=10.0,
        format="%.1f"
    )
    conc_in = conc_in_nM / 1_000_000
else:
    st.markdown(f"### Concentraciones para {ion} (en mM)")
    conc_out = st.number_input("Concentración extracelular (mM)", value=130.0, min_value=0.1, step=0.1, format="%.2f")
    conc_in = st.number_input("Concentración intracelular (mM)", value=20.0, min_value=0.1, step=0.1, format="%.2f")

temp_c = st.slider("🌡️ Temperatura (°C)", 20, 40, 37)

T = temp_c + 273.15
R = 8.314
F = 96485
z = {"Na⁺": 1, "K⁺": 1, "Cl⁻": -1, "Ca²⁺": 2}[ion]

E_ion = (R * T / (z * F)) * np.log(conc_out / conc_in) * 1000


fig, ax = plt.subplots(figsize=(6, 3.5))
colors = {"Na⁺": "green", "K⁺": "blue", "Cl⁻": "orange", "Ca²⁺": "purple"}
color = colors.get(ion, "blue")

bar = ax.bar([f"E_{{{ion}}}"], [E_ion], color=color, alpha=0.7)

ax.axhline(E_ion, color='red', linestyle='--', linewidth=1)
ax.text(0, E_ion + (5 if E_ion >= 0 else -10), f"{E_ion:.1f} mV",
        ha='center', va='bottom' if E_ion >= 0 else 'top',
        fontweight='bold', fontsize=12, color=color)

ax.set_ylabel("Potencial (mV)")
ax.set_title(f"Potencial de equilibrio para {ion}")
ax.grid(True, linestyle=':', alpha=0.6)
ax.set_ylim(-150, 180) 

st.pyplot(fig)


color = {"Na⁺": "green", "K⁺": "blue", "Cl⁻": "orange", "Ca²⁺": "purple"}[ion]
st.markdown(f'<p style="color:{color}; font-size:28px;">  **Resultado: Potencial de equilibrio para {ion}= {E_ion:.1f} mV**</p>', unsafe_allow_html=True)




st.markdown(r'''
Para calcular el potencial de equilibrio iónico empleamos la ecuación de Nernst, que es la siguiente:
$$
E_{\text{ion}} = \frac{RT}{zF} \ln\left(\frac{[\text{ion}]_{\text{ext}}}{[\text{ion}]_{\text{int}}}\right)
$$
En esta ecuación:
- $R = 8.314\ \text{J/mol·K}$
- $T$ = temperatura en grados Kelvin
- $z$ = valencia del ion
- $F = 96485\ \text{C/mol}$
''')


st.subheader("📚¿Te gastaría calcular la concentración a partir de un potencial de equilibrio iónico deseado?")

st.info("💡Instrucciones: Primero elige que ion deseas emplear, puedes elegir entre los iones sodio, potasio, cloro y calcio.")


ion_inv = st.selectbox("Selecciona el ion", ["Na⁺", "K⁺", "Cl⁻", "Ca²⁺"], key="ion_inverse")
z_inv = {"Na⁺": 1, "K⁺": 1, "Cl⁻": -1, "Ca²⁺": 2}[ion_inv]


st.info("💡Ahora elige qué concentración deseas calcular, la intra o la extracelular.")

calc_option = st.radio(
    "¿Qué concentración deseas calcular?",
    ("Intracelular ([ion]ᵢₙₜ)", "Extracelular ([ion]ₑₓₜ)"),
    key="calc_option"
)



if ion_inv == "Ca²⁺":
    default_ext = 1.0
    default_int = 0.0005  
    min_val = 0.000001    
else:
    default_ext = 100.0 if ion_inv == "Na⁺" else (2.0 if ion_inv == "K⁺" else 100.0)
    default_int = 5.0 if ion_inv == "Na⁺" else (110.0 if ion_inv == "K⁺" else 2.0)
    min_val = 0.001


st.info("💡En esta sección deberás ingresar la concentración de referencia en el compartimiento opuesto, ⚡posteriormente, ingresa el potencial de equilibrio iónico que deseas y 📚finalmente presiona el botón de calcular para que puedas obtener el resultado, además se mostrará una gráfica que te permitirá ver el potencial de membrana con respecto a la concentración.")

if calc_option == "Intracelular ([ion]ᵢₙₜ)":
    conc_ext_ref = st.number_input(
        "Concentración extracelular de referencia (mM)", 
        value=default_ext,
        min_value=min_val, 
        step=0.1 if ion_inv != "Ca²⁺" else 0.0001,
        format="%.4f" if ion_inv == "Ca²⁺" else "%.1f"
    )
    E_desired = st.number_input("Potencial de equilibrio deseado (mV)", value=10.0, step=1.0)
    
    if st.button("Calcular [ion]ᵢₙₜ"):
        ratio = np.exp((E_desired / 1000) * (z_inv * F) / (R * T))
        conc_int_new = conc_ext_ref / ratio
        
        # Validar mínimo para evitar error
        if conc_int_new < min_val:
            st.warning(f"⚠️ La concentración calculada ({conc_int_new:.6f} mM) es muy baja. "
                       f"Valor mínimo permitido: {min_val:.6f} mM.")
        else:
            st.success(f"Para E = {E_desired:.1f} mV y [ion]ₑₓₜ = {conc_ext_ref:.4f} mM, [ion]ᵢₙₜ = **{conc_int_new:.4f} mM**")

        
        conc_range = np.linspace(min_val, conc_ext_ref * 10, 200)
        E_vals = (R * T / (z_inv * F)) * np.log(conc_ext_ref / conc_range) * 1000
        current_conc = conc_int_new if 'conc_int_new' in locals() and conc_int_new >= min_val else min_val
        current_E = E_desired

elif calc_option == "Extracelular ([ion]ₑₓₜ)":
    conc_int_ref = st.number_input(
        "Concentración intracelular de referencia (mM)", 
        value=default_int,
        min_value=min_val, 
        step=0.1 if ion_inv != "Ca²⁺" else 0.0001,
        format="%.4f" if ion_inv == "Ca²⁺" else "%.1f"
    )
    E_desired = st.number_input("Potencial de equilibrio deseado (mV)", value=0.0, step=1.0)
    
    if st.button("Calcular [ion]ₑₓₜ"):
        ratio = np.exp((E_desired / 1000) * (z_inv * F) / (R * T))
        conc_ext_new = conc_int_ref * ratio
        
        if conc_ext_new < min_val:
            st.warning(f"⚠️ La concentración calculada ({conc_ext_new:.6f} mM) es muy baja.")
        else:
            st.success(f"Para E = {E_desired:.1f} mV y [ion]ᵢₙₜ = {conc_int_ref:.4f} mM, [ion]ₑₓₜ = **{conc_ext_new:.4f} mM**")

       
        conc_range = np.linspace(min_val, max(conc_int_ref * 10, 200), 200)
        E_vals = (R * T / (z_inv * F)) * np.log(conc_range / conc_int_ref) * 1000
        current_conc = conc_ext_new if 'conc_ext_new' in locals() and conc_ext_new >= min_val else min_val
        current_E = E_desired


if ('conc_int_new' in locals() or 'conc_ext_new' in locals()):
    colors = {"Na⁺": "green", "K⁺": "blue", "Cl⁻": "orange", "Ca²⁺": "purple"}
    color = colors[ion_inv]
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    ax.scatter([current_conc], [current_E], color=color, s=100, zorder=5)
    ax.axvline(current_conc, color='blue', linestyle='--', alpha=0.6)
    ax.axhline(current_E, color='red', linestyle='--', alpha=0.6)


    ax.text(
        current_conc, current_E + 5, 
        f"[{ion_inv}] = {current_conc:.4f} mM\nE = {current_E:.1f} mV",
        ha='left', va='bottom',
        fontsize=10, fontweight='normal',
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8)
    )
    
    
   
    ax.set_ylabel("Potencial de equilibrio iónico (mV)")
    ax.grid(True, linestyle=':', alpha=0.5)
    
    
    ax.set_ylim(-105, 150)  
    
   
    if ion_inv == "Ca²⁺":
        if calc_option == "Intracelular ([ion]ᵢₙₜ)":
            ax.set_xlim(0, 0.01)  
            ax.set_xlabel("Concentración iónica [ion]ᵢₙₜ (mM)")
        else:
            ax.set_xlim(0, 15)    
            ax.set_xlabel("Concentración iónica [ion]ₑₓₜ (mM)")
    else:
        # Para Na⁺, K⁺, Cl⁻: 0 a 200 mM
        ax.set_xlim(0, 200)
        ax.set_xlabel("Concentración iónica [ion]ᵢₙₜ (mM)" if calc_option == "Intracelular ([ion]ᵢₙₜ)" else "Concentración iónica [ion]ₑₓₜ (mM)")
    
    ax.set_title(f" Potencial de equilibrio iónico E_{{{ion_inv}}} vs Concentración iónica [ion]")
    st.pyplot(fig)


st.info("📚En la gráfica se observa el potencial de equilibrio para la concentración calculada, tomando como referencia el valor establecido en el espacio correspondiente.")


import pandas as pd

st.markdown("### 🩺 Concentraciones iónicas fisiológicas aproximadas (en mM)")

st.info("📊 Puedes emplear estos valores para conocer cuáles son los potenciales de equilibrio aproximados en condiciones normales.")

ion_data = {
    "Ion": ["Sodio (Na⁺)", "Potasio (K⁺)", "Cloro (Cl⁻)", "Calcio (Ca²⁺)"],
    "Intracelular (mM)": ['10 - 12', '140 - 150', '4 - 20', '0.0001 - 0.0002'],  # 0.0001 mM = 100 nM
    "Extracelular (mM)": ['135 - 145', '3.5 - 5', '100 - 110', '2.0 - 2.6']
}

df_ions = pd.DataFrame(ion_data)
st.table(df_ions)

st.caption("💡 Nota: La concentración intracelular de Ca²⁺ es ~100 - 200 nM (0.0001 - 0.0002 mM).")



st.info("🩺Gracias por visitarnos, puedes emplear esta aplicación gratuitamente y compartirla si así lo deseas. En Fisiología DJ podrás encontrar una gran cantidad de videos e información que te será de utilidad para todos tus cursos. 🙏 Agradecemos infinitamente toda la ayuda brindada por Qwen Studio para el desarrollo e implementación de esta aplicación.")
