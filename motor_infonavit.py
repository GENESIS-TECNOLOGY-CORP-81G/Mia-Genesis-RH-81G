# motor_infonavit.py
class MotorInfonavit:
    def __init__(self, salario_diario_integrado):
        self.sdi = salario_diario_integrado
        self.umi_2026 = 105.74 # Unidad oficial de Medida Infonavit

    def calcular_aportacion_patronal(self, dias_periodo):
        """Calcula el 5% obligatorio que paga el patrón al Infonavit."""
        return round((self.sdi * dias_periodo) * 0.05, 2)

    def calcular_descuento_credito(self, tipo_credito, valor_descuento, dias_periodo):
        """Calcula la retención exacta sustituyendo el VSM por la UMI de ley."""
        if tipo_credito == 'porcentaje':
            return round(self.sdi * dias_periodo * (valor_descuento / 100.0), 2)
        elif tipo_credito == 'cuota_fija':
            return round(valor_descuento * (dias_periodo / 30.4), 2)
        elif tipo_credito == 'vsm' or tipo_credito == 'umi':
            return round(self.umi_2026 * valor_descuento * (dias_periodo / 30.4), 2)
        return 0.0