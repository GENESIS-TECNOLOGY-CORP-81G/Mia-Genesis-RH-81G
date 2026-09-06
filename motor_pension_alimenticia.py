# motor_pension_alimenticia.py
class MotorPensionAlimenticia:
    def __init__(self, percepciones_totales, deducciones_de_ley):
        self.percepciones = percepciones_totales
        self.deducciones_ley = deducciones_de_ley  # ISR e IMSS según aplique la orden del juez

    def calcular_descuento_judicial(self, tipo_base, porcentaje_ordenado):
        """
        Calcula la retención por pensión alimenticia:
        - tipo_base: 'neto' (sobre lo que resta después de impuestos) o 'bruto' (sobre percepciones totales)
        - porcentaje_ordenado: El porcentaje decretado por el juez (ej. 20%, 30%, etc.)
        """
        if tipo_base == 'neto':
            base_calculo = self.percepciones - self.deducciones_ley
        elif tipo_base == 'bruto':
            base_calculo = self.percepciones
        else:
            base_calculo = self.percepciones - self.deducciones_ley  # Por defecto se usa neto

        monto_retencion = base_calculo * (porcentaje_ordenado / 100.0)

        return {
            "base_aplicada": base_calculo,
            "porcentaje": porcentaje_ordenado,
            "monto_a_retener": monto_retencion
        }