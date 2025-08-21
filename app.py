import streamlit as st
from streamlit_option_menu import option_menu

#funciones

#variables
servicios = ["Corte degradado - $12","Corte y barba - $18","Barba - $8","Tinte - $15"]
empleados = ["Julian","Juan"]
#config page

st.set_page_config(page_title='App de citas',page_icon='✂',layout='centered')
st.image("barberia.jpg")
st.title("Barberia de barrio")
st.text("Calle Abrebaredo,n5,Málaga")

selected = option_menu(menu_title= None,options= ["Servicios","Reseñas","Portafolio","Detalles"],
                       icons= ["scissors","chat-dots","file-text","pin"],
                       orientation= "horizontal",)

if selected == "Portafolio":
    st.image("corte1.jpeg", caption= "Degradado básico")
    st.image("corte1.jpeg", caption= "Corte más barba")
    st.image("corte1.jpeg", caption= "Raya personalizada")
    st.image("corte1.jpeg", caption= "Afeitado personalizado")
    st.image("corte1.jpeg", caption= "Corte tupe")

if selected == "Detalles":
    st.image("map.JPG")
    st.markdown(f"Pulsa [aquí] (www.google.com) para ver la direccion en Google Maps.")

    st.subheader("Empleados")
    column1,column2 = st.columns(2)
    column1.image("barber1.png", caption='Julian')
    column2.image("barber1.png", caption='Juan')

    st.subheader("Horarios de apertura y contacto")
    st.write("---")
    st.text("📞459 328 429")
    st.write("---")

    c1,c2 = st.columns(2)
    c1.text("Lunes")
    c2.text("9:00 - 20:00")
    c1.text("Martes")
    c2.text("9:00 - 20:00")
    c1.text("Miercoles")
    c2.text("9:00 - 20:00")
    c1.text("Jueves")
    c2.text("9:00 - 20:00")
    c1.text("Viernes")
    c2.text("9:00 - 20:00")
    c1.text("Sabado")
    c2.text("9:00 - 15:00")
    c1.text("Domingo")
    c2.text("Cerrado")

    st.write("---")
    st.markdown("📷[Instagram](www.instagram.com)")

if selected == "Reseñas":
    st.image("opinion1.JPG")
    st.image("opinion1.JPG")
    st.image("opinion1.JPG")
    st.image("opinion1.JPG")

if selected == "Servicios":
    st.subheader("Reserva tu cita")
    a1,a2 = st.columns(2)
    nombre = a1.text_input("Tu nombre")
    email = a2.text_input("Tu email")
    fecha = a1.date_input("Fecha")
    hora = a2.selectbox("Horas disponibles",[])
    servicio = a1.selectbox("Servicio",servicios)
    empleado = a2.selectbox("Empleados",empleados)
    nota = a1.text_area("💬Nota (opcional)")


    enviar = st.button("Enviar")
