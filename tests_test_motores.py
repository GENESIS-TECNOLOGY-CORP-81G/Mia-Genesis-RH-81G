# tests/test_motores.py
from motor_vales import MotorVales
from motor_vacaciones import MotorVacaciones
from motor_incapacidades import MotorIncapacidades
# tests/test_documental_finiquitos.py
from motor_documental import MotorDocumentalLegal
from motor_finiquitos import MotorFiniquitoLFT

def test_indemnizacion_injustificado():
    m = MotorDocumentalLegal({"nombre":"ACME"})
    res = m.calcular_totales_baja('injustificado', salario_diario=500.0, antiguedad_anios=2)
    assert isinstance(res['total'], float)
    assert res['total'] > 0

def test_prima_antiguedad_tope():
    f = MotorFiniquitoLFT(salario_diario=10000, antiguedad_anios=20, dias_trabajados_anio_actual=365)
    r = f.calcular_prima_antiguedad()
    assert r["anios_calculados"] <= 15

def test_vales():
    m = MotorVales("alimentacion", 2000)
    res = m.calcular_monto_total()
    assert "monto_total_vales" in res
    assert res["monto_total_vales"] == round(2000, 2)

def test_vacaciones():
    v = MotorVacaciones(3)
    assert v.calcular_dias_vacaciones() == 16

def test_incapacidades():
    inc = MotorIncapacidades('enfermedad_general', 5, 300.0)
    res = inc.calcular_subsidio()
    assert "subsidio_imss" in res