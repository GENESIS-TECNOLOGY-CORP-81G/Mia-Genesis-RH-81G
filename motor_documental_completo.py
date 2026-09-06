# motor_documental_completo_rh.py
# CATÁLOGO COMPLETO DE GENERACIÓN DOCUMENTAL EN RH (MÁXIMA COBERTURA)

class MotorDocumentalCompletoRH:
    def __init__(self, datos_empresa, datos_empleado):
        """
        datos_empresa = {"nombre": "GENESIS CORP", "rfc": "GTC123456AA1"}
        datos_empleado = {"nombre": "Carlos Mendoza", "puesto": "Analista Core"}
        """
        self.empresa = datos_empresa
        self.empleado = datos_empleado

    # 1. CONTRATACIÓN Y RELACIÓN LABORAL
    def generar_contrato_indeterminado(self): 
        return f"CONTRATO INDIVIDUAL DE TRABAJO POR TIEMPO INDETERMINADO celebrado entre la empresa {self.empresa['nombre']} y el C. {self.empleado['nombre']} de forma mutua y conforme a la LFT."
        
    def generar_contrato_determinado(self): 
        return f"CONTRATO INDIVIDUAL DE TRABAJO POR TIEMPO DETERMINADO. Empresa: {self.empresa['nombre']}. Trabajador: {self.empleado['nombre']}. Vigencia sujeta a naturaleza del servicio."
        
    def generar_contrato_periodo_prueba(self): 
        return f"CONTRATO INDIVIDUAL DE TRABAJO BAJO PERIODO DE PRUEBA (Máximo legal LFT). Celebrado por {self.empresa['nombre']} a favor de {self.empleado['nombre']} para validar aptitudes de puesto."
        
    def generar_carta_oferta_laboral(self): 
        return f"CARTA OFERTA LABORAL formal emitida por {self.empresa['nombre']}. Estimado(a) {self.empleado['nombre']}, nos complace ofrecerle la posición de {self.empleado.get('puesto', 'Colaborador')}."
        
    def generar_carta_asignacion_puesto(self): 
        return f"CARTA DE ASIGNACIÓN Y CAMBIO DE PUESTO. A partir de la fecha, el C. {self.empleado['nombre']} asume la responsabilidad del puesto de {self.empleado.get('puesto', 'Nueva Asignación')}."

    # 2. MODIFICACIONES Y CONDICIONES GENERALES
    def generar_convenio_modificacion_salario(self): 
        return f"CONVENIO MODIFICATORIO DE CONDICIONES DE TRABAJO (SALARIO). Modificación al sueldo diario base del C. {self.empleado['nombre']} ratificado por la representación de {self.empresa['nombre']}."
        
    def generar_convenio_cambio_horario_turno(self): 
        return f"CONVENIO DE CAMBIO DE JORNADA Y TURNO LABORAL. El colaborador {self.empleado['nombre']} acuerda modificar sus horarios de checada en común acuerdo con {self.empresa['nombre']}."
        
    def generar_convenio_cambio_adscripcion(self): 
        return f"CONVENIO DE REUBICACIÓN GEOGRÁFICA Y ADSCRIPCIÓN DE CENTRO DE TRABAJO. Aplicable para el traslado del trabajador {self.empleado['nombre']} a las nuevas instalaciones operativas."
        
    def generar_constancia_laboral_con_sueldo(self): 
        return f"CONSTANCIA LABORAL: Se hace constar que {self.empleado['nombre']} labora en {self.empresa['nombre']} percibiendo un sueldo neto registrado ante las autoridades competentes."
        
    def generar_constancia_laboral_simple(self): 
        return f"CONSTANCIA DE TRABAJO: Por medio de la presente se confirma que el C. {self.empleado['nombre']} forma parte activa de la plantilla de personal de {self.empresa['nombre']}."

    # 3. CONTROL DISCIPLINARIO Y LEGAL (LFT)
    def generar_acta_administrativa_retardos(self): 
        return f"ACTA ADMINISTRATIVA POR REINCIDENCIA DE RETARDOS. Empleado: {self.empleado['nombre']}. Se asienta constancia de incumplimiento de horario conforme al Reglamento Interior de Trabajo."
        
    def generar_acta_administrativa_faltas(self): 
        return f"ACTA ADMINISTRATIVA POR AUSENTISMO INJUSTIFICADO. Notificación formal para el colaborador {self.empleado['nombre']} por ausencias consecutivas que afectan la productividad de la empresa."
        
    def generar_acta_administrativa_bajas_insubordinacion(self): 
        return f"ACTA ADMINISTRATIVA (CAUSAL RESCISIÓN - INSUBORDINACIÓN). Hechos levantados en contra de {self.empleado['nombre']} por desacato directo a las instrucciones de la dirección patronal."
        
    def generar_acta_administrativa_danos_equipo(self): 
        return f"ACTA ADMINISTRATIVA POR DAÑOS A ACTIVOS Y EQUIPO DE CÓMPUTO/TRABAJO. Se evalúan los daños materiales imputados al uso negligente del hardware asignado al C. {self.empleado['nombre']}."
        
    def generar_aviso_rescision_laboral_art_47(self): 
        return f"AVISO DE RESCISIÓN DE LA RELACIÓN DE TRABAJO (Artículo 47 LFT). Dirigido a {self.empleado['nombre']}: Se le notifica el despido justificado y cese inmediato sin responsabilidad para {self.empresa['nombre']}."
        
    def generar_carta_amonestacion_escrita(self): 
        return f"CARTA DE AMONESTACIÓN ESCRITA Y EXTRAÑAMIENTO. Llamado de atención formal para el C. {self.empleado['nombre']} a fin de que corrija conductas operativas de forma inmediata."
        
    def generar_suspension_laboral_disciplinaria(self): 
        return f"NOTIFICACIÓN DE SUSPENSISÓN DISCIPLINARIA. Sanción temporal de días sin goce de sueldo applied al trabajador {self.empleado['nombre']} de acuerdo con los reglamentos de {self.empresa['nombre']}."

    # 4. SEPARACIONES Y FINIQUITOS
    def generar_renuncia_voluntaria(self): 
        return f"CARTA MANIFESTACIÓN DE RENUNCIA VOLUNTARIA E INCONDICIONAL. Yo, {self.empleado['nombre']}, por propio derecho doy por terminada mi relación de trabajo con la empresa {self.empresa['nombre']}."
        
    def generar_convenio_fuera_de_juicio_art_33(self): 
        return f"CONVENIO DE MUTUO ACUERDO FUERA DE JUICIO (Art. 33 LFT). Celebrado de forma libre entre la entidad {self.empresa['nombre']} y el trabajador {self.empleado['nombre']}."
        
    def generar_recibo_finiquito_fin_relacion(self): 
        return f"RECIBO FINIQUITO DE HABERES LABORALES. Constancia de pago de proporcionales y liberación de obligaciones salariales mutuas entre {self.empresa['nombre']} y {self.empleado['nombre']}."
        
    def generar_recibo_liquidacion_indemnizacion(self): 
        return f"RECIBO DE INDEMNIZACIÓN CONSTITUCIONAL Y LIQUIDACIÓN LABORAL. Pago total de los conceptos de ley devengados y fin de relaciones obrero-patronales con el C. {self.empleado['nombre']}."
        
    def generar_carta_liberacion_adeudos(self): 
        return f"CARTA DE LIBERACIÓN DE ADEUDOS, ACTIVOS Y HERRAMIENTAS DE TRABAJO. El área de almacén/TI certifica que {self.empleado['nombre']} entregó el hardware en óptimas condiciones."

    # 5. SEGURIDAD SOCIAL, PRESTACIONES Y BENEFICIOS
    def generar_solicitud_credito_infonavit_formato(self): 
        return f"FORMATO DE CONTROL DE AVISO DE RETENCIÓN DE DESCUENTOS INFONAVIT. Trámite interno de nómina para el crédito de vivienda del trabajador {self.empleado['nombre']}."
        
    def generar_carta_autorizacion_descuento_fonacot(self): 
        return f"CARTA AUTORIZACIÓN EXPRESA DE DESCUENTO VÍA NÓMINA FONACOT. Suscrita por el empleado {self.empleado['nombre']} para la amortización del crédito al consumo vigente."
        
    def generar_constancia_retenciones_pension(self): 
        return f"CONSTANCIA DE APLICACIÓN DE RETENCIÓN POR ORDEN JUDICIAL (PENSIÓN ALIMENTICIA). Registro de deducción obligatoria ordenada por juzgado familiar sobre los ingresos de {self.empleado['nombre']}."
        
    def generar_politica_vales_despensa_gasolina(self): 
        return f"CARTA COMPROBANTE DE ASIGNACIÓN Y POLÍTICA DE VALES DE DESPENSA / ENERGÍA. Prestación otorgada por {self.empresa['nombre']} sujeta a los topes de exención de la ley."
        
    def generar_comprobante_entrega_equipo_proteccion(self): 
        return f"ACTA DE COMPROBANTE DE ENTREGA DE EQUIPO DE PROTECCIÓN PERSONAL (EPP). El trabajador {self.empleado['nombre']} recibe las herramientas de seguridad obligatorias."

    # 6. PERMISOS, VACACIONES E INCAPACIDADES
    def generar_solicitud_vacaciones_dignas(self): 
        return f"SOLICITUD DE VACACIONES DIGNAS LFT. Periodo vacacional solicitado formalmente por {self.empleado['nombre']} con cargo al saldo de días acumulados por antigüedad."
        
    def generar_permiso_con_goce_sueldo(self): 
        return f"AUTORIZACIÓN DE PERMISO ESPECIAL CON GOCE DE SUELDO (Paternidad / Causa Fuerza Mayor). Validado por la administración de {self.empresa['nombre']} para el C. {self.empleado['nombre']}."
        
    def generar_permiso_sin_goce_sueldo(self): 
        return f"SOLICITUD Y AUTORIZACIÓN DE PERMISO TEMPORAL SIN GOCE DE SUELDO. Suscrita por {self.empleado['nombre']} con efectos de suspensión temporal de la obligación de prestar el servicio."
        
    def generar_registro_incapacidad_imss(self): 
        return f"REGISTRO INTERNO Y CONTROL DE CERTIFICADO DE INCAPACIDAD MÉDICA IMSS. Justificante de ausencia del colaborador {self.empleado['nombre']} capturado para exención de cuotas de nómina."