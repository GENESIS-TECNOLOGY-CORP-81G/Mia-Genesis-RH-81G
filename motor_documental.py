# motor_documental.py
class MotorDocumentalLegal:
    def __init__(self, empresa_datos: dict):
        self.empresa = empresa_datos

    def calcular_totales_baja(self, tipo_baja: str, salario_diario: float, antiguedad_anios: int) -> dict:
        """
        Devuelve dict con totales monetarios (en MXN). Validamos entradas y usamos float con round.
        """
        if salario_diario < 0 or antiguedad_anios < 0:
            raise ValueError("Salario diario y antigüedad deben ser >= 0")

        datos_monetarios = {'total': 0.0}
        if tipo_baja == 'injustificado':
            indemnizacion_3_meses = salario_diario * 90.0
            indemnizacion_20_dias = (salario_diario * 20.0) * antiguedad_anios
            datos_monetarios['total'] = round(indemnizacion_3_meses + indemnizacion_20_dias, 2)
        else:
            datos_monetarios['total'] = round(salario_diario * 15.0, 2)

        return datos_monetarios

    def generar_finiquito_o_liquidacion(self, tipo_baja, empleado_nombre, salario_diario, antiguedad_anios, fecha_termino):
        tot = self.calcular_totales_baja(tipo_baja, salario_diario, antiguedad_anios)['total']
        total_str = f"${tot:,.2f} MXN"
        # Resto del texto como antes pero usando total_str
        ...