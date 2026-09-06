# motor_fiscal.py
# Motor Fiscal SAT - Cálculo Genérico de Impuestos de Nómina

class MotorFiscalSAT:
    def __init__(self):
        # Rangos de la tarifa mensual de ISR (Simplificada para entorno de prueba operativo)
        # Estructura: (Límite Inferior, Límite Superior, Cuota Fija, Porcentaje sobre excedente)
        self.tabla_isr_mensual = [
            (0.0, 746.04, 0.0, 0.0192),
            (746.05, 6332.05, 14.32, 0.0640),
            (6332.06, 11128.01, 371.83, 0.1088),
            (11128.02, 12935.82, 893.63, 0.1600),
            (12935.83, 999999.9, 1182.88, 0.1792) # Límite superior abierto
        ]

    # motor_fiscal.py - fragmento corregido
def calcular_isr(self, base_gravable: float) -> float:
    if base_gravable < 0:
        raise ValueError("base_gravable debe ser >= 0")
    isr_calculado = 0.0
    for lim_inf, lim_sup, cuota_fija, porcentaje in self.tabla_isr_mensual:
        # Usar lim_inf <= base < lim_sup para evitar ambigüedades en los límites
        if lim_inf <= base_gravable < lim_sup:
            excedente = base_gravable - lim_inf
            impuesto_marginal = excedente * porcentaje
            isr_calculado = cuota_fija + impuesto_marginal
            break
    return round(isr_calculado, 2)

if __name__ == "__main__":
    sat = MotorFiscalSAT()
    base_ejemplo = 10000.0  # Base mensual gravable de prueba
    print(f"El cálculo de ISR retenido para una base de ${base_ejemplo:,.2f} es: ${sat.calcular_isr(base_ejemplo):,.2f} MXN")