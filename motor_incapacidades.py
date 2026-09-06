# motor_incapacidades.py
# MOTOR INCAPACIDADES

class MotorIncapacidades:
    def __init__(self, tipo_incapacidad, dias, salario_base_cotizacion):
        self.tipo = tipo_incapacidad
        self.dias = dias
        self.sbc = salario_base_cotizacion

    def calcular_subsidio(self):
        """Calcula el subsidio económico según las reglas obligatorias del IMSS."""
        subsidio_imss = 0.0
        dias_descuento_nomina = 0
        
        if self.tipo == 'riesgo_trabajo':
            subsidio_imss = self.sbc * self.dias
        elif self.tipo == 'enfermedad_general':
            if self.dias > 3:
                subsidio_imss = (self.sbc * 0.60) * (self.dias - 3)
                dias_descuento_nomina = 3
            else:
                dias_descuento_nomina = self.dias
        elif self.tipo == 'maternidad':
            subsidio_imss = self.sbc * self.dias
            
        return {
            "subsidio_imss": round(subsidio_imss, 2),
            "dias_restados_en_nomina": dias_descuento_nomina
        }