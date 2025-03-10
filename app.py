# app.py
import streamlit as st

# Título de la aplicación
st.title("Gestión de Proyectos y Tareas")

# Menú lateral para navegar entre las funcionalidades
menu = st.sidebar.selectbox(
    "Selecciona una opción",
    ["Autenticación", "Gestión de Usuarios", "Gestión de Proyectos", "Gestión de Tareas", "Notificaciones"]
)

if menu == "Autenticación":
    st.header("Autenticación")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Iniciar Sesión"):
        st.success("Inicio de sesión simulado exitoso")

elif menu == "Gestión de Usuarios":
    st.header("Gestión de Usuarios")
    st.write("Aquí puedes gestionar usuarios.")
    new_username = st.text_input("Nombre de usuario")
    new_password = st.text_input("Contraseña", type="password")
    new_email = st.text_input("Correo electrónico")
    if st.button("Crear Usuario"):
        st.success("Usuario creado simulado exitosamente")

elif menu == "Gestión de Proyectos":
    st.header("Gestión de Proyectos")
    st.write("Aquí puedes gestionar proyectos.")
    project_name = st.text_input("Nombre del proyecto")
    project_description = st.text_area("Descripción del proyecto")
    owner_id = st.number_input("ID del propietario", min_value=1)
    if st.button("Crear Proyecto"):
        st.success("Proyecto creado simulado exitosamente")

elif menu == "Gestión de Tareas":
    st.header("Gestión de Tareas")
    st.write("Aquí puedes gestionar tareas.")
    task_title = st.text_input("Título de la tarea")
    task_description = st.text_area("Descripción de la tarea")
    task_owner_id = st.number_input("ID del propietario", min_value=1)
    if st.button("Crear Tarea"):
        st.success("Tarea creada simulado exitosamente")

elif menu == "Notificaciones":
    st.header("Notificaciones")
    st.write("Aquí puedes enviar notificaciones.")
    recipient = st.text_input("Destinatario")
    subject = st.text_input("Asunto")
    body = st.text_area("Mensaje")
    if st.button("Enviar Notificación"):
        st.success("Notificación enviada simulado exitosamente")