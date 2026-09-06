# motor_finiquitos.py
# Motor de Finiquitos y Liquidaciones de MIA GENESIS

class MotorFiniquitoLFT:
    def __init__(self, salario_diario, antiguedad_anios, dias_trabajados_anio_actual):
        self.salario_diario = salario_diario
        self.antiguedad = antiguedad_anios
        self.dias_trabajados = dias_trabajados_anio_actual
        # Inyección del salario mínimo general oficial vigente
        self.salario_minimo_general = 315.04 
        
    def calcular_proporcionales(self):
        """Lógica estricta de días proporcionales de vacaciones y aguinaldo."""
        aguinaldo_proporcional = (self.dias_trabajados * (15 / 365.0)) * self.salario_diario
        vacaciones_proporcionales = (self.dias_trabajados * (12 / 365.0)) * self.salario_diario
        prima_vacacional = vacaciones_proporcionales * 0.25
        
        return {
            "aguinaldo": round(aguinaldo_proporcional, 2),
            "vacaciones": round(vacaciones_proporcionales, 2),
            "prima_vacacional": round(prima_vacacional, 2)
        }
        
   # motor_finiquitos.py (extracto)
def calcular_prima_antiguedad(self, anios_tope=15):
    if self.salario_diario <= 0:
        raise ValueError("salario_diario debe ser mayor que 0")
    anios_efectivos = min(self.antiguedad, anios_tope)
    tope_legal_diario = self.salario_minimo_general * 2
    salario_base_calculo = min(self.salario_diario, tope_legal_diario)
    total_prima = anios_efectivos * 12 * salario_base_calculo
    return {
        "anios_calculados": anios_efectivos,
        "salario_diario_utilizado": round(salario_base_calculo, 2),
        "total_prima_antiguedad": round(total_prima, 2)
    }
if __name__ == "__main__":
    finiquito = MotorFiniquitoLFT(salario_diario=750.0, antiguedad_anios=4, dias_trabajados_anio_actual=200)
    print("Proporcionales:", finiquito.calcular_proporcionales())
    print("Prima de Antigüedad:", finiquito.calcular_prima_antiguedad())