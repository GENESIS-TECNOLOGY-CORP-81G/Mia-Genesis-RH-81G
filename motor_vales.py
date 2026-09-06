# motor_vales.py
class MotorVales:
    def __init__(self, tipo_vale, monto_base):
        self.tipo = tipo_vale
        self.monto = monto_base
        self.uma_diaria = 117.31

    def calcular_monto_total(self):
        """Retorna el monto total y valida el tope de exención del 40% de la UMA elevada al mes"""
        tope_exento_mensual = (self.uma_diaria * 0.40) * 30.4
        gravable_sat = max(0.0, self.monto - tope_exento_mensual) if self.monto > tope_exento_mensual else 0.0

        return {
            "monto_total_vales": round(self.monto, 2),
            "monto_gravado_isr": round(gravable_sat, 2)
        }