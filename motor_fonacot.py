# motor_fonacot.py
class MotorFonacot:
    def __init__(self):
        # Salario mínimo mensual 2026 diario ($315.04) multiplicado por el factor mensual (30.4)
        self.salario_minimo_mensual = 315.04 * 30.4

    def calcular_retencion_fonacot(self, sueldo_bruto, porcentaje_maximo_descuento=0.20):
        """
        Calcula la retención máxima permitida por ley para Fonacot.
        Garantiza que el descuento no afecte el salario mínimo de subsistencia.
        """
        retencion_permitida = sueldo_bruto * porcentaje_maximo_descuento
        sueldo_remanente = sueldo_bruto - retencion_permitida
        
        ajustado = False
        if sueldo_remanente < self.salario_minimo_mensual:
            ajustado = True
            retencion_permitida = max(0.0, sueldo_bruto - self.salario_minimo_mensual)
            
        return {
            "retencion_fonacot": round(retencion_permitida, 2),
            "tope_aplicado_por_ley": ajustado
        }