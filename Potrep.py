import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Potencial de Membrana", page_icon="⚡")
st.markdown("<h3 style='text-align: center;'>⚡ Calculadora del Potencial de Membrana ⚡                (Ecuación de Goldman-Hodgkin-Katz) </h3>", unsafe_allow_html=True)

st.info("💡¿Sabias que la ecuación de Goldman-Hodgkin-Katz es de gran utilidad en fisiología para calcular el potencial de membrana? La ecuación de Goldman-Hodgkin-Katz describe el potencial de membrana en estado estacionario cuando la membrana es permeable a múltiples iones (sodio (Na⁺), potasio (K⁺), cloro (Cl⁻) y calcio (Ca²⁺)). El voltaje obtenido en la ecuación representa un equilibrio dinámico de los potenciales de equilibrio de cada ion, donde el valor está determinado por el promedio ponderado de los potenciales de equilibrio iónico de cada ion (determinados por los gradientes de concentración) y las respectivas permeabilidades relativas.")
st.info("📚Instrucciones: 1. Elige la concentración intracelular y extracelular para cada ion. 2. Si deseas obtener el POTENCIAL DE MEMBRANA selecciona: 🔹Modo estático. Si deseas simular un POTENCIAL DE ACCIÓN selecciona: 🔹Modo Dinámico. 3. Elige la temperatura a la que quieres trabajar. 4. Establece las permeabilidades de la membrana celular para cada ion. En la sección de resultados observarás los POTENCIALES DE EQUILIBRIO para cada ion y el POTENCIAL DE MEMBRANA, estos se actualizan AUTOMÁTICAMENTE.")



st.subheader("Concentraciones (mM)")
col1, col2 = st.columns(2)
with col1:
    Na_out = st.number_input("Na⁺ fuera", value=145.0, min_value=0.1)
    K_out = st.number_input("K⁺ fuera", value=4.0, min_value=0.1)
    Cl_out = st.number_input("Cl⁻ fuera", value=110.0, min_value=0.1)
    Ca_out = st.number_input("Ca²⁺ fuera", value=2.0, min_value=0.001, format="%.3f")
with col2:
    Na_in = st.number_input("Na⁺ dentro", value=10.0, min_value=0.1)
    K_in = st.number_input("K⁺ dentro", value=140.0, min_value=0.1)
    Cl_in = st.number_input("Cl⁻ dentro", value=4.0, min_value=0.1)
    Ca_in = st.number_input("Ca²⁺ dentro", value=0.0001, min_value=0.000001, format="%.6f")

st.subheader("Selecciona el modo con el que quieres trabajar")

mode = st.radio("Modo", ["Estático (cálculo del POTENCIAL DE MEMBRANA)", "Dinámico (simulación del POTENCIAL DE ACCIÓN)"], horizontal=True)
st.markdown("---")


R = 8.314
F = 96485

if mode == "Estático (cálculo del POTENCIAL DE MEMBRANA)":

    temp_c = st.slider("🌡️ Temperatura (°C)", 20, 40, 37, key="temp_estatico")
    T = temp_c + 273.15
    

    st.subheader("Permeabilidades relativas")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        P_Na = st.number_input("P_Na", value=0.04, min_value=0.001, step=0.1, format="%.3f")
    with col2:
        P_K = st.number_input("P_K", value=1.0, min_value=0.001, step=0.1, format="%.3f")
    with col3:
        P_Cl = st.number_input("P_Cl", value=0.45, min_value=0.001, step=0.1, format="%.3f")
    with col4:
        P_Ca = st.number_input("P_Ca", value=0.0001, min_value=0.000001, step=0.0001, format="%.6f")
    

    E_Na = (R * T / F) * np.log(Na_out / Na_in) * 1000
    E_K = (R * T / F) * np.log(K_out / K_in) * 1000
    E_Cl = (R * T / F) * np.log(Cl_in / Cl_out) * 1000
    E_Ca = (R * T / (2 * F)) * np.log(Ca_out / Ca_in) * 1000
    
    num = P_Na*Na_out + P_K*K_out + P_Cl*Cl_in + P_Ca*Ca_out
    den = P_Na*Na_in + P_K*K_in + P_Cl*Cl_out + P_Ca*Ca_in
    V_m = (R * T / F) * np.log(num / den) * 1000

    st.subheader("Sección de resultados")
    
    st.info("💡Aquí se muestran los ⚡POTENCIALES DE EQUILIBRIO IÓNICO de cada ion para las concentraciones elegidas.")

    st.markdown(f'<p style="color:green; font-size:18px;"><b>Potencial de equilibrio del ion sodio= {E_Na:.1f} mV</b></p>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:blue; font-size:18px;"><b>Potencial de equilibrio del ion potasio= {E_K:.1f} mV</b></p>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:orange; font-size:18px;"><b>Potencial de equilibrio del ion cloro = {E_Cl:.1f} mV</b></p>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:purple; font-size:18px;"><b>Potencial de equilibrio del ion calcio= {E_Ca:.1f} mV</b></p>', unsafe_allow_html=True)
  
    st.info("💡Aquí se muestra el ⚡POTENCIAL DE MEMBRANA obtenido.")

    st.markdown(f'<p style="color:red; font-size:30px;"><b>Potencial de membrana: {V_m:.1f} mV</b></p>', unsafe_allow_html=True)

    st.info("⚡Aquí puedes recordar la Ecuación de Goldman-Hodgkin-Katz y cada uno de sus parametros.⚡")

    st.markdown(r'''
    $$
    V_m = \frac{RT}{F} \ln\left(\frac{
    P_{\text{Na}}[\text{Na}^+]_{\text{fuera}} + P_{\text{K}}[\text{K}^+]_{\text{fuera}} + P_{\text{Cl}}[\text{Cl}^-]_{\text{dentro}} + P_{\text{Ca}}[\text{Ca}^{2+}]_{\text{fuera}}
    }{
    P_{\text{Na}}[\text{Na}^+]_{\text{dentro}} + P_{\text{K}}[\text{K}^+]_{\text{dentro}} + P_{\text{Cl}}[\text{Cl}^-]_{\text{fuera}} + P_{\text{Ca}}[\text{Ca}^{2+}]_{\text{dentro}}
    }
    \right)
    $$
    En esta ecuación:
    - $R = 8.314\ \text{J/mol·K}$
    - $T$ = temperatura en grados Kelvin
    - $F = 96485\ \text{C/mol}$
    - $P$ = Permeabilidad
    - $[\text{ion}]$ = Concentracion del ion
    - $dentro$ = Concentración intracelular
    - $fuera$ = Concentración extracelular
    - $\text{K}^+$ = ion potasio
    - $\text{Na}^+$ = ion sodio
    - $\text{Cl}^-$ = ion cloro
    - $\text{Ca}^{2+}$ = ion calcio
    ''')

    st.info("💡En esta gráfica de barras puedes observar la contribución de las concentraciones iónicas que elevan el voltaje (numerador) y la de las concentraciones iónicas que disminuyen el voltaje (denominador).⚡")
    # Gráfico de barras
    num_contrib = [P_Na*Na_out, P_K*K_out, P_Cl*Cl_in, P_Ca*Ca_out]
    den_contrib = [P_Na*Na_in, P_K*K_in, P_Cl*Cl_out, P_Ca*Ca_in]
    ions = ['Na⁺', 'K⁺', 'Cl⁻', 'Ca²⁺']
    colors = ['green', 'blue', 'orange', 'purple']

    total_num = sum(num_contrib)
    total_den = sum(den_contrib)
    
    pct_num = [x / total_num * 100 for x in num_contrib]
    pct_den = [x / total_den * 100 for x in den_contrib]
    

    fig, ax = plt.subplots(figsize=(9, 5))
    index = np.arange(4)
    bar_width = 0.35
    ax.bar(index, pct_num, bar_width, label='Numerador', color=colors, alpha=0.9)
    ax.bar(index + bar_width, pct_den, bar_width, label='Denominador', color=colors, alpha=0.4)
    ax.set_xlabel('Fisiología DJ Ion')
    ax.set_ylabel('Contribución')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(ions)
    ax.legend()
    st.pyplot(fig)



    if 'V_m_initial' not in st.session_state:
        Na_out_def, Na_in_def = 145.0, 10.0
        K_out_def, K_in_def = 4.0, 140.0
        Cl_out_def, Cl_in_def = 110.0, 4.0
        Ca_out_def, Ca_in_def = 2.0, 0.0001
        P_Na_def, P_K_def, P_Cl_def, P_Ca_def = 0.04, 1.0, 0.45, 0.0001
    
        num_init = P_Na_def*Na_out_def + P_K_def*K_out_def + P_Cl_def*Cl_in_def + P_Ca_def*Ca_out_def
        den_init = P_Na_def*Na_in_def + P_K_def*K_in_def + P_Cl_def*Cl_out_def + P_Ca_def*Ca_in_def
        V_m_initial = (R * T / F) * np.log(num_init / den_init) * 1000
        st.session_state.V_m_initial = V_m_initial
    else:
        V_m_initial = st.session_state.V_m_initial

    try:
        delta_V_v = abs(V_m - V_m_initial) / 1000
        Cm = 0.01      # F/m²
        A = 1e-9       # m²
        e = 1.6e-19    # C
        Q = Cm * A * delta_V_v
        N_ions = Q / e
        N_ions_int = int(N_ions)
    except:
        N_ions_int = 0

    if V_m > V_m_initial + 5:
        ion_movido = "Na⁺"
    elif V_m < V_m_initial - 5:
        ion_movido = "K⁺"
    else:
        ion_movido = "Na⁺/K⁺"

    st.info("💡En esta sección puedes ver la cantidad aproximada de iones que se desplazarían debido a los cambios en la concentración que estableciste al inicio. Se toman como estado inicial los valores establecidos por defecto, así que el ⚡potencial de membrana en reposo de referencia será -74.7 mV y solo se consideran a los cationes predominantes: potasio y sodio.")

    st.markdown(f'<p style="color:red; font-size:20px;"><b>Del potencial inicial ({V_m_initial:.1f} mV) al actual ({V_m:.1f} mV), se movieron aproximadamente {N_ions_int:,} iones de {ion_movido}."</b></p>', unsafe_allow_html=True)


    st.info("⚖️ Es importante mencionar que en el interior de la célula existen cargas negativas que no pueden salir e incluyen entre otros a proteínas, fosfatos como el ATP y ácidos nucleicos como el ADN, que en conjunto son denominados ANIONES INTRACELULARES NO DIFUSIBLES. En reposo, esta carga negativa esta equilibrada por iones con carga positiva como el potasio (K⁺) y el sodio (Na⁺). Los aniones intracelulares no difusibles son la razón por la que el potasio se mantiene en altas concentraciones en el interior de las células, en condiciones normales el potasio que sale de la célula deja a los aniones intracelulares no difusibles parcialmente descompensados, lo que ocasiona que el interior se vuelva negativo, de esta forma estos participan directamente en el establecimiento del potencial de membrana en reposo.")


    import pandas as pd
    
    st.markdown("### 🩺 Concentraciones fisiológicas aproximadas (en mM) para cada ion ")

    st.info("📊 Puedes emplear estos valores para calcular el potencial de membrana en condiciones normales.")

    ion_data = {
        "Ion": ["Sodio (Na⁺)", "Potasio (K⁺)", "Cloro (Cl⁻)", "Calcio (Ca²⁺)"],
        "Intracelular (mM)": ['10 - 12', '140 - 150', '4 - 20', '0.0001 - 0.0002'],  # 0.0001 mM = 100 nM
        "Extracelular (mM)": ['135 - 145', '3.5 - 5', '100 - 110', '2.0 - 2.6']
    }

    df_ions = pd.DataFrame(ion_data)
    st.table(df_ions)

    st.caption("💡 Nota: La concentración intracelular de Ca²⁺ es ~100 - 200 nM (0.0001 - 0.0002 mM).")

    st.info("🩺Gracias por visitarnos, puedes emplear esta aplicación gratuitamente y compartirla si así lo deseas. En Fisiología DJ podrás encontrar una gran cantidad de videos e información que te será de utilidad para todos tus cursos. 🙏 Agradecemos infinitamente toda la ayuda brindada por Qwen Studio para el desarrollo e implementación de esta aplicación. Esta aplicación es para fines educativos.")


elif mode == "Dinámico (simulación del POTENCIAL DE ACCIÓN)":

    temp_c = st.slider("🌡️ Temperatura (°C)", 20, 40, 37, key="temp_dinamico")
    T = temp_c + 273.15


    t_max = st.slider("Duración total de la simulación (ms)", 10, 200, 50)

    st.info("💡Aquí puedes simular un POTENCIAL DE ACCIÓN BÁSICO. Puedes elegir entre diferentes tipos de escenarios y para lograr el potencial de acción deberás elegir: 🔹la temperatura, 🔹el tiempo que quieres que dure tu simulación, 🔹los tipos de iones que emplearás, 🔹el tiempo de inicio, 🔹el cambio en la permeabilidad (de cerrado a abierto), 🔹la duración de este cambio, 🔹el cambio en la permeabilidad (de abierto a cerrado) y 🔹la duración de este cambio para cada ion. Una vez elegidos estos parámetros presiona el botón INICIAR SIMULACIÓN y se mostrará la simulación básica de tu potencial de acción. 📚 Aprende, descubre, diviértete creando un potencial de acción. En Fisiología DJ esperamos que esta simulación que hemos preparado para ti sea de tu agrado y que disfrutes intentando obtener un potencial de acción. Esta aplicación es gratuita y para fines educativos, los resultados mostrados son simulaciones aproximadas.")

    scenario = st.selectbox("Escenario fisiológico", [
        "Permeabilidades de sodio y potasio",
        "Permeabilidades de sodio, potasio y cloro",
        "Permeabilidades de sodio, potasio/calcio",
        "Permeabilidades de sodio/potasio y calcio"
    ])

    P_Na_open, P_Na_close = 1.0, 0.04
    t_Na_open, t_Na_close = 1, 5
    P_K_open, P_K_close = 1.0, 1.0
    t_K_open, t_K_close = 1, 50
    P_Cl_open, P_Cl_close = 1.0, 0.45
    t_Cl_open, t_Cl_close = 1, 5
    P_Ca_open, P_Ca_close = 0.5, 0.0001
    t_Ca_open, t_Ca_close = 1, 100
    P_K_slow_open, P_K_slow_close = 1.0, 1.0
    t_K_slow_open, t_K_slow_close = 1, 100
    

    if scenario == "Permeabilidades de sodio y potasio":
        st.subheader("Sodio")
        t_Na_start = st.slider("Inicio de sodio (ms)", 0, t_max-1, 0, key="t_na_start_sp")
        P_Na_open = st.number_input("Cambio en la permeabilidad de sodio, apertura", 0.045, 20.0, 1.0, key="p_na_open_sp")
        t_Na_open = st.slider("Duración apertura Na⁺ (ms)", 1, 10, 1, key="t_na_open_sp")
        P_Na_close = st.number_input("Cambio en la permeabilidad de sodio, cierre", 0.04, P_Na_open, 0.04, key="p_na_close_sp")
        t_Na_close = st.slider("Duración cierre Na⁺ (ms)", 1, 10, 1, key="t_na_close_sp")
    
        st.subheader("Potasio")
        na_end = t_Na_start + t_Na_open + t_Na_close
        t_K_start = st.slider("Inicio de potasio (ms)", 0, t_max-1, max(1, na_end - 1), key="t_k_start_sp")
        P_K_open = st.number_input("Cambio en la permeabilidad de potasio, apertura", 1.0, 20.0, 1.0, key="p_k_open_sp")
        t_K_open = st.slider("Duración apertura K⁺ (ms)", 1, 30, 1, key="t_k_open_sp")
        P_K_close = st.number_input("Cambio en la permeabilidad de potasio, cierre", 1.0, P_K_open, 1.0, key="p_k_close_sp")
        t_K_close = st.slider("Duración cierre K⁺ (ms)", 1, 100, 1, key="t_k_close_sp")


    elif scenario == "Permeabilidades de sodio, potasio y cloro":
        st.subheader("Sodio")
        t_Na_start = st.slider("Inicio de sodio (ms)", 0, t_max-1, 0, key="t_na_start_spc")
        P_Na_open = st.number_input("Cambio en la permeabilidad de sodio, apertura", 0.045, 20.0, 1.0, key="p_na_open_spc")
        t_Na_open = st.slider("Duración apertura Na⁺ (ms)", 1, 10, 1, key="t_na_open_spc")
        P_Na_close = st.number_input("Cambio en la permeabilidad de sodio, cierre", 0.04, P_Na_open, 0.04, key="p_na_close_spc")
        t_Na_close = st.slider("Duración cierre Na⁺ (ms)", 1, 10, 1, key="t_na_close_spc")
    
        st.subheader("Potasio")
        na_end = t_Na_start + t_Na_open + t_Na_close
        t_K_start = st.slider("Inicio de potasio (ms)", 0, t_max-1, max(1, na_end - 1), key="t_k_start_spc")
        P_K_open = st.number_input("Cambio en la permeabilidad de potasio, apertura", 1.0, 20.0, 1.0, key="p_k_open_spc")
        t_K_open = st.slider("Duración apertura K⁺ (ms)", 1, 30, 1, key="t_k_open_spc")
        P_K_close = st.number_input("Cambio en la permeabilidad de potasio, cierre", 1.0, P_K_open, 1.0, key="p_k_close_spc")
        t_K_close = st.slider("Duración cierre K⁺ (ms)", 1, 100, 1, key="t_k_close_spc")

        st.subheader("Cloro")
        K_end = t_K_start + t_K_open + t_K_close
        t_Cl_start = st.slider("Inicio de cloro (ms)", 0, t_max-1, 0, key="t_cl_start_spc")
        P_Cl_open = st.number_input("Cambio en la permeabilidad de cloro, apertura", 0.45, 20.0, 1.0, key="p_cl_open_spc")
        t_Cl_open = st.slider("Duración apertura de Cl⁻ (ms)", 1, 50, 1, key="t_cl_open_spc")
        P_Cl_close = st.number_input("Cambio en la permeabilidad de Cl⁻, cierre", 0.45, P_Cl_open, 0.45, key="p_cl_close_spc")
        t_Cl_close = st.slider("Duración cierre Cl⁻ (ms)", 1, 50, 1, key="t_cl_close_spc")
    
    
    elif scenario == "Permeabilidades de sodio, potasio/calcio":
        st.subheader("Sodio")
        t_Na_start = st.slider("Inicio de sodio (ms)", 0, t_max-1, 0, key="t_Na_start_spca")
        P_Na_open = st.number_input("Cambio en la permeabilidad de sodio, apertura", 0.045, 20.0, 1.0, key="p_na_open_spca")
        t_Na_open = st.slider("Duración apertura Na⁺ (ms)", 1, 10, 1, key="t_na_open_spca")
        P_Na_close = st.number_input("Cambio en la permeabilidad de sodio, cierre", 0.04, P_Na_open, 0.04, key="p_na_close_spca")
        t_Na_close = st.slider("Duración cierre Na⁺ (ms)", 1, 10, 1, key="t_na_close_spca")
    
        st.subheader("Potasio rapido")
        Na_end = int(t_Na_start + t_Na_open + t_Na_close)
        t_K_start = st.slider("Inicio de potasio rapido (ms)", 0, t_max-1, max(1, Na_end - 1), key="t_k_fast_start_spca")
        P_K_open = st.number_input("Cambio en la permeabilidad de potasio rapido, apertura", 0.01, 20.0, 1.0, key="p_k_fast_open_spca")
        t_K_open = st.slider("Duración apertura potasio rapido (ms)", 1, 10, 1, key="t_k_fast_open_spca")
        P_K_close = st.number_input("Cambio en la permeabilidad de potasio rapido, cierre", 0.01, P_K_open, 1.0, key="p_k_fast_close_spca")
        t_K_close = st.slider("Duración cierre potasio rapido (ms)", 1, 5, 1, key="t_k_fast_close_spca")

        st.subheader("Calcio meseta")
        K_end = int(t_K_start + t_K_open + t_K_close)
        t_Ca_start = st.slider("Inicio de Calcio (ms)", 0, t_max-1, max(1, K_end - 1), key="t_ca_start_spca")
        P_Ca_open = st.number_input("Cambio en la permeabilidad de Calcio, apertura", 0.0001, 500.0, 1.0, key="p_ca_open_spca")
        t_Ca_open = st.slider("Duración apertura Calcio (ms)", 1, 100, 1, key="t_ca_open_spca")
        P_Ca_close = st.number_input("Cambio en la permeabilidad de Calcio, cierre", 0.0001, P_K_open, 0.5, key="p_ca_close_spca")
        t_Ca_close = st.slider("Duración cierre Calcio (ms)", 1, 100, 1, key="t_ca_close_spca")

        st.subheader("Potasio meseta")
        K_end = int(t_K_start + t_K_open + t_K_close)
        t_K_meseta_start = st.slider("Inicio de potasio de la meseta (ms)", 0, t_max-1, t_Ca_start, key="t_k_meseta_start_spca")
        P_K_meseta_open = st.number_input("Cambio en la permeabilidad de potasio de la meseta, apertura", 0.01, 20.0, 1.0, key="p_k_meseta_open_spca")
        t_K_meseta_open = st.slider("Duración apertura potasio de la meseta (ms)", 1, 100, 1, key="t_k_meseta_open_spca")
        P_K_meseta_close = st.number_input("Cambio en la permeabilidad de potasio de la meseta, cierre", 0.01, P_K_meseta_open, 1.0, key="p_k_meseta_close_spca")
        t_K_meseta_close = st.slider("Duración cierre potasio de la meseta (ms)", 1, 50, 1, key="t_k_meseta_close_spca")

        st.subheader("Potasio lento")
        Ca_end = int(t_Ca_start + t_Ca_open + t_Ca_close)
        t_K_slow_start = st.slider("Inicio de potasio lento (ms)", 0, t_max-1, max(1, Ca_end - 1), key="t_k_slow_start_spca")
        P_K_slow_open = st.number_input("Cambio en la permeabilidad de potasio lento, apertura", 0.01, 50.0, 1.0, key="p_k_slow_open_spca")
        t_K_slow_open = st.slider("Duración apertura potasio lento (ms)", 1, 30, 1, key="t_k_slow_open_spca")
        P_K_slow_close = st.number_input("Cambio en la permeabilidad de potasio lento, cierre", 0.01, P_K_slow_open, 1.0, key="p_k_slow_close_spca")
        t_K_slow_close = st.slider("Duración cierre potasio lento (ms)", 1, 30, 1, key="t_k_slow_close_spca")


    elif scenario == "Permeabilidades de sodio/potasio y calcio":
        st.subheader("Sodio (If)")
        t_Na_start = st.slider("Inicio de sodio (ms)", 0, t_max-1, 0, key="t_na_start_spcal")
        P_Na_open = st.number_input("Cambio en la permeabilidad de sodio/potasio, apertura", 0.1, 20.0, 0.1, key="p_na_open_spcal")
        t_Na_open = st.slider("Duración apertura sodio/potasio (ms)", 1, 100, 1, key="t_na_open_spcal")
        P_Na_close = st.number_input("Cambio en la permeabilidad de sodio/potasio, cierre", 0.04, P_Na_open, 0.04, key="p_na_close_spcal")
        t_Na_close = st.slider("Duración cierre sodio/potasio (ms)", 1, 100, 1, key="t_na_close_spcal")

        st.subheader("Potasio (If)")
        t_K_if_start = st.slider("Inicio de potasio (ms)", 0, t_max-1, t_Na_start, key="t_k_if_start_spcal")
        P_K_if_open = st.number_input("Cambio en la permeabilidad de potasio, apertura", 0.01, 20.0, 1.0, key="p_k_if_open_spcal")
        t_K_if_open = st.slider("Duración apertura potasio (ms)", 1, 100, 1, key="t_k_if_open_spcal")
        P_K_if_close = st.number_input("Cambio en la permeabilidad de potasio, cierre", 0.01, P_K_if_open, 1.0, key="p_k_if_close_spcal")
        t_K_if_close = st.slider("Duración cierre potasio (ms)", 1, 100, 1, key="t_k_if_close_spcal")

        st.subheader("Calcio")
        Na_end = t_Na_start + t_Na_open + t_Na_close
        t_Ca_start = st.slider("Inicio de Calcio (ms)", 0, t_max-1, max(1, Na_end - 1), key="t_ca_start_spcal")
        P_Ca_open = st.number_input("Cambio en la permeabilidad de Calcio, apertura", 0.0001, 500.0, 1.0, key="p_ca_open_spcal")
        t_Ca_open = st.slider("Duración apertura Calcio (ms)", 1, 100, 1, key="t_ca_open_spcal")
        P_Ca_close = st.number_input("Cambio en la permeabilidad de Calcio, cierre", 0.0001, P_K_open, 1.0, key="p_ca_close_spcal")
        t_Ca_close = st.slider("Duración cierre Calcio (ms)", 1, 100, 1, key="t_ca_close_spcal")

        st.subheader("Potasio")
        Ca_end = t_Ca_start + t_Ca_open + t_Ca_close
        t_K_rif_start = st.slider("Inicio de potasio (ms)", 0, t_max-1, max(1, Ca_end - 1), key="t_k_rif_start_spcal")
        P_K_rif_open = st.number_input("Cambio en la permeabilidad de potasio, apertura", 0.01, 20.0, 1.0, key="p_k_rif_open_spcal")
        t_K_rif_open = st.slider("Duración apertura potasio (ms)", 1, 100, 1, key="t_k_rif_open_spcal")
        P_K_rif_close = st.number_input("Cambio en la permeabilidad de potasio, cierre", 0.01, P_K_open, 1.0, key="p_k_rif_close_spcal")
        t_K_rif_close = st.slider("Duración cierre potasio (ms)", 1, 100, 1, key="t_k_rif_close_spcal")

        
                    
    if st.button("Iniciar simulación"):
        # Vector de tiempo
        t = np.linspace(0, t_max, max(100, t_max * 5))
    
        P_Na_t = np.full_like(t, 0.04)
        P_K_t = np.full_like(t, 1.0)
        P_Cl_t = np.full_like(t, 0.45)
        P_Ca_t = np.full_like(t, 0.0001)
    
        if scenario == "Permeabilidades de sodio y potasio":
            for i, ti in enumerate(t):
                if ti < t_Na_start:
                    P_Na_t[i] = 0.04
                elif ti < t_Na_start + t_Na_open:
                    P_Na_t[i] = 0.04 + (P_Na_open - 0.04) * ((ti - t_Na_start) / t_Na_open)
                elif ti < t_Na_start + t_Na_open + t_Na_close:
                    P_Na_t[i] = P_Na_open - (P_Na_open - P_Na_close) * ((ti - t_Na_start - t_Na_open) / t_Na_close)
                else:
                    P_Na_t[i] = P_Na_close
            
                if ti < t_K_start:
                    P_K_t[i] = 1.0
                elif ti < t_K_start + t_K_open:
                    P_K_t[i] = 1.0 + (P_K_open - 1.0) * ((ti - t_K_start) / t_K_open)
                elif ti < t_K_start + t_K_open + t_K_close:
                    P_K_t[i] = P_K_open - (P_K_open - P_K_close) * ((ti - t_K_start - t_K_open) / t_K_close)
                else:
                    P_K_t[i] = P_K_close

        elif scenario == "Permeabilidades de sodio, potasio y cloro":
            for i, ti in enumerate(t):
                if ti < t_Na_start:
                    P_Na_t[i] = 0.04
                elif ti < t_Na_start + t_Na_open:
                    P_Na_t[i] = 0.04 + (P_Na_open - 0.04) * ((ti - t_Na_start) / t_Na_open)
                elif ti < t_Na_start + t_Na_open + t_Na_close:
                    P_Na_t[i] = P_Na_open - (P_Na_open - P_Na_close) * ((ti - t_Na_start - t_Na_open) / t_Na_close)
                else:
                    P_Na_t[i] = P_Na_close
            
                if ti < t_K_start:
                    P_K_t[i] = 1.0
                elif ti < t_K_start + t_K_open:
                    P_K_t[i] = 1.0 + (P_K_open - 1.0) * ((ti - t_K_start) / t_K_open)
                elif ti < t_K_start + t_K_open + t_K_close:
                    P_K_t[i] = P_K_open - (P_K_open - P_K_close) * ((ti - t_K_start - t_K_open) / t_K_close)
                else:
                    P_K_t[i] = P_K_close

                if ti < t_Cl_start:
                    P_Cl_t[i] = 0.45
                elif ti < t_Cl_start + t_Cl_open:
                    P_Cl_t[i] = 0.45 + (P_Cl_open - 0.45) * ((ti - t_Cl_start) / t_Cl_open)
                elif ti < t_Cl_start + t_Cl_open + t_Cl_close:
                    P_Cl_t[i] = P_Cl_open - (P_Cl_open - P_Cl_close) * ((ti - t_Cl_start - t_Cl_open) / t_Cl_close)
                else:
                    P_Cl_t[i] = P_Cl_close

        elif scenario == "Permeabilidades de sodio, potasio/calcio":
            for i, ti in enumerate(t):
                # Sodio
                if ti < t_Na_start:
                    P_Na_t[i] = 0.04
                elif ti < t_Na_start + t_Na_open:
                    P_Na_t[i] = 0.04 + (P_Na_open - 0.04) * ((ti - t_Na_start) / t_Na_open)
                elif ti < t_Na_start + t_Na_open + t_Na_close:
                    P_Na_t[i] = P_Na_open - (P_Na_open - P_Na_close) * ((ti - t_Na_start - t_Na_open) / t_Na_close)
                else:
                    P_Na_t[i] = P_Na_close
            
                if ti < t_K_start:
                    P_K_t[i] = 1.0
                elif ti < t_K_start + t_K_open:
                    P_K_t[i] = 1.0 + (P_K_open - 1.0) * ((ti - t_K_start) / t_K_open)
                elif ti < t_K_start + t_K_open + t_K_close:
                    P_K_t[i] = P_K_open - (P_K_open - P_K_close) * ((ti - t_K_start - t_K_open) / t_K_close)
                else:
                    P_K_t[i] = P_K_close
            
                if ti >= t_Ca_start and ti < t_Ca_start + t_Ca_open:
                    P_Ca_t[i] = P_Ca_open
                    P_K_t[i] += P_K_meseta_open
            
                if ti >= t_K_slow_start and ti < t_K_slow_start + t_K_slow_open:
                    P_K_t[i] += P_K_slow_open

        elif scenario == "Permeabilidades de sodio/potasio y calcio":
            for i, ti in enumerate(t):
                # Corriente If (Na⁺/K⁺ simultáneo)
                if ti >= t_Na_start and ti < t_Na_start + t_Na_open:
                    P_Na_t[i] = 0.04 + (P_Na_open - 0.04) * ((ti - t_Na_start) / t_Na_open)
                    P_K_t[i] = 1.0 + (P_Na_open - 1.0) * ((ti - t_Na_start) / t_Na_open)
                elif ti >= t_Na_start + t_Na_open and ti < t_Na_start + t_Na_open + t_Na_close:
                    P_Na_t[i] = P_Na_open - (P_Na_open - P_Na_close) * ((ti - t_Na_start - t_Na_open) / t_Na_close)
                    P_K_t[i] = P_Na_open - (P_Na_open - P_Na_close) * ((ti - t_Na_start - t_Na_open) / t_Na_close)
                else:
                    P_Na_t[i] = P_Na_close
                    P_K_t[i] = P_Na_close
            
                # Calcio
                if ti >= t_Ca_start and ti < t_Ca_start + t_Ca_open:
                    P_Ca_t[i] = 0.0001 + (P_Ca_open - 0.0001) * ((ti - t_Ca_start) / t_Ca_open)
                elif ti >= t_Ca_start + t_Ca_open and ti < t_Ca_start + t_Ca_open + t_Ca_close:
                    P_Ca_t[i] = P_Ca_open - (P_Ca_open - P_Ca_close) * ((ti - t_Ca_start - t_Ca_open) / t_Ca_close)
                else:
                    P_Ca_t[i] = P_Ca_close
            
                if ti >= t_K_rif_start and ti < t_K_rif_start + t_K_rif_open:
                    P_K_t[i] += P_K_rif_open

        V_m_t = []
        for i in range(len(t)):
            num = P_Na_t[i]*Na_out + P_K_t[i]*K_out + P_Cl_t[i]*Cl_in + P_Ca_t[i]*Ca_out
            den = P_Na_t[i]*Na_in + P_K_t[i]*K_in + P_Cl_t[i]*Cl_out + P_Ca_t[i]*Ca_in
            Vm = (R*T/F) * np.log(num/den) * 1000
            V_m_t.append(Vm)
    
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(t, V_m_t, 'r', linewidth=2)
        ax.set_xlabel("Tiempo (ms)")
        ax.set_ylabel("Potencial de membrana (mV)")
        ax.set_title(f"Simulación Fisiología DJ: {scenario}")
        ax.grid(True, linestyle=':', alpha=0.6)
        st.pyplot(fig)
