import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Potencial de equilibrio iónico", page_icon="⚡")
st.markdown("<h3 style='text-align: center;'>⚡Calculadora del potencial de equilibrio iónico⚡      (Ecuación de Nernst)</h3>", unsafe_allow_html=True)

st.info("💡¿Sabias que la ecuación de Nernst es de gran utilidad en fisiología para calcular el potencial de equilibrio iónico? Este valor representa la energía eléctrica que compensa a la energía química, esto nos ayuda a entender mejor el potencial de membrana en reposo y el potencial de acción. ⚡Cuando se alcanza el voltaje del potencial de equilibrio iónico el flujo neto del ion es cero.")
st.info("📚Intrucciones: Elige el ion de tu interés, tienes para elegir entre sodio, potasio, cloro y calcio. Después elige la concentración extra e intracelular, así como la temperatura de tu preferencia desplazando las barras hasta obtener el valor deseado. 🤩Observa cómo se actualiza el potencial de equilibrio iónico resultante en la gráfica y en valor numérico en milivolts (mV) en la parte inferior. Dejamos para ti la ecuación de Nernst al final.")

ion = st.selectbox("Ion", ["Na⁺", "K⁺", "Cl⁻", "Ca²⁺"])

if ion == "Ca²⁺":
    st.markdown("### Concentraciones para calcio")
    conc_out = st.number_input(
        "Concentración extracelular (mM)", 
        value=2.0, 
        min_value=0.001, 
        step=0.1,
        format="%.3f"
    )
    conc_in_nM = st.number_input(
        "Concentración intracelular (nM)", 
        value=100.0, 
        min_value=1.0, 
        step=10.0,
        format="%.1f"
    )
    conc_in = conc_in_nM / 1_000_000
else:
    st.markdown(f"### Concentraciones para {ion}")
    conc_out = st.slider(
        "Concentración extracelular (mM)", 
        min_value=1, max_value=200, value=145
    )
    conc_in = st.slider(
        "Concentración intracelular (mM)", 
        min_value=1, max_value=200, value=10
    )

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

# Ecuación
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



st.info("🩺Gracias por visitarnos, puedes emplear esta aplicación gratuitamente y compartirla si así lo deseas. En Fisiología DJ podrás encontrar una gran cantidad de videos e información que te será de utilidad para todos tus cursos. 🙏 Agradecemos infinitamente toda la ayuda brindada por Qwen Studio para el desarrollo e implementación de esta aplicación.")
