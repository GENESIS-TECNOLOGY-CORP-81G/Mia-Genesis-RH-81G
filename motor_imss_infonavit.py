# motor_imss_infonavit.py
# Módulo para cálculo de Salario Diario Integrado (SDI) y Cuotas Obrero-Patronales

class MotorSeguridadSocial:
    def __init__(self, salario_diario, factor_integracion):
        self.salario_diario = salario_diario
        self.factor_integracion = factor_integracion
        self.valor_uma = 117.31  # Valor oficial diario
        
    def calcular_sdi(self):
        """Calcula el Salario Diario Integrado base para cotizar en el IMSS."""
        sdi_calculado = self.salario_diario * self.factor_integracion
        # Aplica el tope legal de 25 veces la UMA establecido en la Ley del Seguro Social
        return min(sdi_calculado, self.valor_uma * 25)

    def _calcular_tasa_cesantia_patronal(self, sdi):
        """Aplica la tabla de cuotas progresivas patronales de Cesantía y Vejez."""
        veces_uma = sdi / self.valor_uma
        if veces_uma <= 1.0: return 0.03150
        elif veces_uma <= 1.5: return 0.03676
        elif veces_uma <= 2.0: return 0.04851
        elif veces_uma <= 2.5: return 0.05556
        elif veces_uma <= 3.0: return 0.06026
        elif veces_uma <= 3.5: return 0.06361
        elif veces_uma <= 4.0: return 0.06613
        else: return 0.07513  # Tasa máxima para salarios altos

    def calcular_cuotas_imss_patronal(self, dias_cotizados):
        """Cálculo de aportaciones patronales con porcentajes y reglas de ley vigentes."""
        sdi = self.calcular_sdi()
        base_cotizacion = sdi * dias_cotizados
        
        # 1. Enfermedad y Maternidad (Cuota fija del 20.40% sobre la UMA diaria)
        cuota_fija = (self.valor_uma * 0.204) * dias_cotizados
        
        # Excedente a las 3 UMAs (1.10% patronal sobre la diferencia)
        excedente_base = sdi - (self.valor_uma * 3)
        cuota_excedente = (excedente_base * 0.011) * dias_cotizados if excedente_base > 0 else 0.0
        
        # 2. Invalidez y Vida (1.75%) y Guarderías/Prestaciones Sociales (1.00%)
        invalidez_vida = base_cotizacion * 0.0175
        guarderias = base_cotizacion * 0.0100
        
        # 3. Retiro (2.00%) y la tasa progresiva de Cesantía y Vejez calculada
        retiro = base_cotizacion * 0.0200
        tasa_cv = self._calcular_tasa_cesantia_patronal(sdi)
        cesantia_vejez = base_cotizacion * tasa_cv
        
        # Riesgo de Trabajo (Clase I base: 0.522%, se puede alterar por la prima de la empresa)
        riesgo_trabajo = base_cotizacion * 0.00522
        
        total_patron = cuota_fija + cuota_excedente + invalidez_vida + guarderias + retiro + cesantia_vejez + riesgo_trabajo
        
        return {
            "sdi": round(sdi, 2),
            "tasa_cesantia_vejez": f"{tasa_cv * 100:.3f}%",
            "total_patronal": round(total_patron, 2)
        }

    def calcular_infonavit(self, dias_cotizados):
        """Calcula la aportación patronal del 5% al Infonavit."""
        sdi = self.calcular_sdi()
        return round((sdi * dias_cotizados) * 0.05, 2)

if __name__ == "__main__":
    seg_social = MotorSeguridadSocial(salario_diario=450.0, factor_integracion=1.0493)
    print(seg_social.calcular_cuotas_imss_patronal(dias_cotizados=30))