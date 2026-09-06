# motor_asistencia.py
# Motor de Asistencia y Cálculo de Tiempos de MIA GENESIS

class MotorAsistencia:
    def __init__(self, checadas_dict):
        """
        Recibe un diccionario con el registro de tiempos del colaborador.
        Ejemplo: {'horas_trabajadas': 53, 'horas_jornada_legal': 48}
        """
        self.checadas = checadas_dict

    def calcular_horas_extra(self):
        """
        Aplica las reglas de la LFT mexicana: las primeras 9 horas extra 
        se pagan dobles; el excedente se paga triple.
        """
        horas_totales = self.checadas.get('horas_trabajadas', 0)
        jornada_base = self.checadas.get('horas_jornada_legal', 48)
        
        if horas_totales <= jornada_base:
            return {"horas_dobles": 0, "horas_triples": 0, "total_horas_extra": 0}
            
        total_extra = horas_totales - jornada_base
        
        if total_extra <= 9:
            horas_dobles = total_extra
            horas_triples = 0
        else:
            horas_dobles = 9
            horas_triples = total_extra - 9
            
        return {
            "total_horas_extra": total_extra,
            "horas_dobles": horas_dobles,
            "horas_triples": horas_triples
        }

if __name__ == "__main__":
    # Simulación de un empleado que trabajó 55 horas en una semana (7 horas extra totales)
    registro_semanal = {'horas_trabajadas': 59, 'horas_jornada_legal': 48}
    asistencia = MotorAsistencia(registro_semanal)
    print(f"Desglose de tiempo extraordinario: {asistencia.calcular_horas_extra()}")