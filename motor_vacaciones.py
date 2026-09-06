# motor_vacaciones.py
class MotorVacaciones:
    def __init__(self, anios_servicio):
        self.anios = anios_servicio

    def calcular_dias_vacaciones(self):
        # Tabla oficial de vacaciones por años de servicio en México
        if self.anios == 1:
            return 12
        elif self.anios == 2:
            return 14
        elif self.anios == 3:
            return 16
        elif self.anios == 4:
            return 18
        elif self.anios == 5:
            return 20
        elif 6 <= self.anios <= 10:
            return 22
        elif 11 <= self.anios <= 15:
            return 24
        elif 16 <= self.anios <= 20:
            return 26
        elif 21 <= self.anios <= 25:
            return 28
        elif 26 <= self.anios <= 30:
            return 30
        elif self.anios >= 31:
            return 32
        return 12  # Por defecto si es menor o caso base