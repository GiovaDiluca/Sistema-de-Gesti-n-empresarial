# app/screens/empleados.py
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from database import agregar_empleado, obtener_empleados

class EmpleadosScreen(Screen):

    def agregar_empleado(self):
        nombre = self.ids.nombre_input.text
        apellido = self.ids.apellido_input.text
        salario = float(self.ids.salario_input.text or 0)
        fecha = self.ids.fecha_input.text
        puesto = self.ids.puesto_input.text

        if nombre and apellido and salario > 0 and fecha:
            agregar_empleado(nombre, apellido, salario, fecha, puesto)
            self.cargar_empleados()

            # limpiar
            self.ids.nombre_input.text = ""
            self.ids.apellido_input.text = ""
            self.ids.salario_input.text = ""
            self.ids.fecha_input.text = ""
            self.ids.puesto_input.text = ""

    def cargar_empleados(self):
        self.ids.empleados_layout.clear_widgets()
        empleados = obtener_empleados()

        for emp in empleados:
            self.ids.empleados_layout.add_widget(
                Label(text=f"{emp[1]} {emp[2]} - {emp[5]}")
            )

    def volver(self):
        self.manager.current = "dashboard"

