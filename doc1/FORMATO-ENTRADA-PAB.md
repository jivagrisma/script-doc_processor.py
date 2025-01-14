| | | | | | | | | |
|-|-|-|-|-|-|-|-|-|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | |Pagos Automáticos Bancolombia (PAB) es un servicio a través del cual nuestros clientes pueden realizar sus abonos automáticamente por medio de los canales transaccionales (H2H - Conexión Empresarial, SVE - Sucursal Virtual Empresas, CTM - Servicio Alterno Transaccional, SWF - Swift), permitiendo de esta manera centralizar sus operaciones bancarias por abonos de nómina, cancelación de facturas, y pagos hacia las demás entidades financieras.  La dispersión de los pagos puede realizarse a través de un archivo plano, el cual debe estar creado con la estructura PAB, donde el cliente especificará de donde se debitarán los recursos y bajo que tipo de pago se acreditarán a los beneficiarios.  El origen de los débitos se identifica a través de la "Clase de Pago", la cual especifica si el débito se realizará a una cuenta Bancolombia, Cartera Credipago, Cuenta Contable o Transporte de Efectivo; y el destino de los abonos se identifica a través del "Tipo de Pago", el cual especifica si el abono se realizará a cuentas Bancolombia, otros bancos, Cheque, Efectivo, Tarjeta Prepago, Credipago u obligaciones con Bancolombia (Cuentas Máscara).  El archivo plano está estructurado con registro de control, registro de detalle y registro de adenda; el registro de control contiene información del cliente pagador (clase de pago, cuenta a debitar, etc.), número de registros y valor total del lote, el registro de detalle contiene información de los clientes beneficiarios (cédula, cuenta, valor, tipo de pago, banco destino, etc.) y el registro de adenda es un registro opcional con información extra relacionada con el pago.                                                                                                                                               *Los únicos caracteres especiales permitidos en los lotes de pagos son ampersand (&) , Asterisco (*) que son los que se encuentran en las adendas opcionales para reportar información adicional de pagos. No se deberán usar otros caracteres especiales en los lotes de pagos. El siguiente corresponde al listado de caracteres especiales no permitidos: Comillas simples (‘),Comillas dobles (“),Letras (Ñ, ñ),Comas (,),Corchetes ([ ]),°  * Los pagos con destino a cuentas Bancolombia, se aplicarán según lo especificado por el cliente al momento de afiliarse: tiempo real, medio día o noche, y se podrán realizar en cualquier momento, porque el horario del sistema de pagos es 7*24.  * Los pagos por ventanilla son aquellos entregados en la red de sucursales Bancolombia en efectivo o cheque, tanto los pagadores como los beneficiarios deberán acomodarse al horario de éstas.  * El abono a cuentas pertenecientes a entidades financieras afiliadas a la red ACH Colombia y ACH Cenit, podrán ser enviados a más tardar a las 3:00 p.m. del día, todo pago que ingrese después de esta hora quedará aplicado el siguiente día hábil.  * La tarjeta prepago es un proceso mediante el cual los clientes del Banco abonan al cupo de una tarjeta prepago. El sistema de Pagos entrega la información al sistema de tarjetas, para realizar el cargue monetario de éstas.  * El servicio especial de notificación vía email sólo se genera cuando el cliente haya colocado la instrucción en el archivo de pagos. Estos servicios tienen como finalidad notificar al beneficiario que le han realizado un pago cuando es cliente Bancolombia o que le realizarán un pago cuando es cliente ACH.   | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | |El Archivo tiene la siguiente estructura:| | | |Exportar Archivos planos de ejemplos| |
| | | | | | | | | |
| | | |Registro de control de archivo| | | | | |
| | | |Registro de detalle| | | | | |
| | | |ADENDAS| | | | | |
| | | |Registro de Documento Adenda estructurada| | | | | |
| | | |Registro de Adenda libre| | | | | |
| | | |Registro de Adenda para impresión de comprobantes| | | | | |
| | | |Formato de Adenda para Pago de Pensiones| | | | | |
| | | |Formato de Adenda Crédito de Seguridad Social| | | | | |
| | | |Formato de Adenda Referencias adicionales para el beneficiario del pago | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | |Registro de Control de Lote| | | | | | |
| | | | | | | | | |
| | |Campo|Nombre Campo|Longitud|Formato|Requisito|Valor|Descripción|
| | |1|Tipo registro|1|Numérico|Obligatorio|1|Indica el tipo de registro de control del archivo.|
| | |2|Nit entidad Originadora|15|Numérico|Obligatorio|Según cada empresa|Nit de la entidad que envía el lote. Con ceros a la izquierda y alineado a la derecha.|
| | |3|Aplicación|1|Alfanumérico|Opcional|I=Inmediata M=Medio D N=Noche|Tipo de aplicación del lote.  Debe ser blanco cuando la forma de aplicación que se requiere es la que el cliente tiene parametrizada a nivel  general.|
| | |4|Filler |15|Alfanumérico|Opcional|Blancos| |
| | |5|Clase de transacción|3|Numérico|Obligatorio|Ver tabla clases de transacciones|Clase de transacciones contenidas en el archivo.|
| | |6|Descripción propósito transacciones|10|Alfanumérico|Opcional|Según cada empresa|Descripción del propósito de transacciones.|
| | |7|Fecha Transmisión de lote|8|Numérico|Obligatorio|AAAAMMDD|Fecha de transmisión de lote, Debe ser el día en que se envía el lotes a Pagos Bancolombia. |
| | |8|Secuencia envío de lotes ese día|2|Alfanumérico|Obligatorio|“A1 A2 B1 C2 …”|Secuencia de envío de lotes. En un mismo día no puede enviarse la misma secuencia.|
| | | | | | | |Ver Secuencia de envío de lotes| |
| | |9|Fecha aplicación|8|Numérico|Obligatorio|AAAAMMDD|Fecha de aplicación del lote. Debe estar entre el día actual y máximo 90 días en el futuro.|
| | |10|Número de registros|6|Numérico|Obligatorio|Sumatoria del nro. de registros|Número de registros de detalle y de documentos.|
| | |11|Sumatoria de débitos|17|Numérico (15 enteros y 2 decimales)|Opcional|0|Sumatoria de débitos. No aplica. Debe venir en ceros.|
| | |12|Sumatoria de créditos|17|Numérico (15 enteros y 2 decimales)|Obligatorio|Valor a pagar de todo el lote. |Sumatoria del valor a acreditar en cada registro de detalle. 15 Enteros y dos decimales sin punto.|
| | |13|Cuenta cliente a debitar|11|Numérico|Obligatorio| |Número de Cuenta del cliente pagador. Con cero a la izquierda, alineada a la derecha.|
| | |14|Tipo de cuenta cliente a debitar|1|Alfanumérico|Obligatorio|S: Ahorros D: Corriente C: Contable|Tipo de cuenta del cliente pagador.|
| | |15|Filler|149|Alfanumérico| | |Utilización futura.|
| | | |Longitud total del registro de Control|264| | | | |
| | | | | | | | | |
| | | |Arriba ↑| | | | | |
| | | | | | | | | |
| | |Registro de detalle de transacciones| | | | | | |
| | | | | | | | | |
| | |Campo|Nombre Campo|Longitud|Formato|Requisito|Valor|Descripción|
| | |1|Tipo registro|1|Numérico|Obligatorio|Valor fijo 6|Indica el tipo de registro de detalle.|
| | |2|Identificación beneficiario|15|Numérico|Obligatorio| |Nit del beneficiario del pago. Alineado a la izquierda con espacios a la derecha.|
| | |3|Nombre del beneficiario|30|Alfanumérico|Obligatorio|Según cada empresa|• Indica el nombre del beneficiario del Pago. • Para tipo de transacción 40 (recarga tarjetas prepago) se debe relacionar el número de la tarjeta que desea recargar.|
| | |4|Banco cuenta del beneficiario (destino)|9|Numérico|Obligatorio|Ver Tabla de Bancos|Banco cuenta del beneficiario, es requerido sólo si la transacción es abono a cuenta. |
| | |5|Número cuenta del beneficiario|17|Alfanumérico|Obligatorio|Alineada a la izquierda y con espacios a la derecha|Número de cuenta del beneficiario (ahorros, corriente, tarjeta de crédito otros bancos, número de obligación otros bancos). Alineada a la izquierda con espacios a la derecha, es requerido si se trata de un abono a cuenta.|
| | |6|Indicador Lugar de pago|1|Alfanumérico|Opcional| |Este campo ya no está habilitado para la generación de cheques masivos, por lo tanto debe de ser un espacio en blanco. |
| | |7|Tipo de transacción|2|Numérico|Obligatorio|Ver tabla tipo de transacción|Tipo de transacción.|
| | |8|Valor transacción|17|Numérico|Obligatorio| |Valor transacción, puede ser cero si se trata de una transacción de Prenotificación.|
| | |9|Fecha aplicación|8|Numérico|Opcional| |Fecha en que se debe realizar el pago al beneficiario. Si está en ceros o errada se asume fecha de aplicación del registro de control.|
| | |10|Referencia|21|Alfanumérico|Opcional|Ver conceptos de Giro por regimen.|Referencia del pago, a criterio del cliente.  Para los pagos de Cuenta Maestra régimen Contributivo, los dos primeros caracteres de la referencia deben traer el concepto de Giro.  Para los pagos de Cuenta Maestra régimen Regalías, los tres primeros caracteres de la referencia corresponden al tipo de registro de detalle.|
| | | | | | | | | |
| | |11|Tipo de documento de identificación|1|Numérico|Opcional|Ver tabla tipo documento de identificación|Es requerido solo si el pago es para entregar por ventanilla.|
| | |12|Oficina de entrega|5|Alfanumérico|Opcional|Códigos Oficinas Bancolombia|Código de oficina para entrega de cheques disponible para el convenio. Cuando es entrega en todas las oficinas debe ir en ceros, si es abono a cuentas debe ir en ceros.|
| | |13|Número de Celular|15|Alfanumérico|Opcional| |Número de celular. Campo Obligatorio para pagos en efectivo por Corresponsa Bancario.|
| | |14|e-mail|80|Alfanumérico|Opcional| |Dirección de correo electrónico a donde se desea enviar información del pago al beneficiario. Si este campo es diligenciado, se genera un cobro de comisión por el servicio de notificación. |
| | |15|Número identificación del autorizado|15|Alfanumérico|Obligatorio| |Identificación del autorizado para reclamar cheques por ventanilla. Sólo es requerido bajo esta modalidad.|
| | |16|Filler|27| | |Espacios|Utilización futura|
| | | |Longitud total del registro de Detalle|264| | | | |
| | | | | | | | | |
| | | | | | | | | |
| | |1. Campo Numérico: Este campo debe ser alineado a la derecha con ceros a la izquierda.| | | | | | |
| | |2. Campo Alfanumérico: Este campo debe ser alineado a la izquierda con espacios a la derecha.| | | | | | |
| | |3. Un campo numérico nunca debe reportarse en blanco, su valor en caso de no requerirse debe ser ceros.| | | | | | |
| | | | | | | | | |
| | | |Arriba ↑| | | | | |
| | | | | | | | | |
| | |Formato de Adenda Estructurada| | | | | | |
| | | | | | | | | |
| | |Campo|Nombre Campo|Longitud|Formato|Requisito|Valor|Descripción|
| | |1|Tipo registro|1|Numérico|Obligatorio|Valor Fijo (3)|Indica el tipo de registro de documentos.|
| | |2|Número de factura|10|Alfanumérico|Obligatorio|Según cada empresa|Número de factura.|
| | |3|Referencia|10|Alfanumérico|Obligatorio|Según cada empresa|Referencia.|
| | |4|Signo valor bruto|1|Alfanumérico|Obligatorio|“+/-“|Signo valor bruto.|
| | |5|Valor bruto /Valor ingresos|17|Numérico (15 enteros y 2 decimales)|Obligatorio|$$$$$$$$$$|Valor bruto.|
| | |6|Signo valor ajuste|1|Alfanumérico|Obligatorio|“+/-“|Signo valor ajuste.|
| | |7|Valor ajuste / Valor Egresos|17|Numérico (15 enteros y 2 decimales)|Obligatorio|$$$$$$$$$$|Valor ajuste.|
| | |8|Signo valor neto|1|Alfanumérico|Obligatorio|“+/-“|Signo valor neto.|
| | |9|Valor neto|17|Numérico (15 enteros y 2 decimales)|Obligatorio|$$$$$$$$$$|Valor neto.|
| | |10|Adición|41|Alfanumérico|Opcional|Detalle|Información adicional sobre la factura que se está relacionando.|
| | |11|Filler|148|Alfanumérico|Opcional| |Utilización futura.|
| | | |Longitud total del registro de Adenda|264| | | | |
| | | | | | | | | |
| | | |Arriba ↑| | | | | |
| | | | | | | | | |
| | |Formato de Adenda en formato libre (Opcional)| | | | | | |
| | | | | | | | | |
| | |Campo|Nombre Campo|Longitud|Formato|Requisito|Valor|Descripción|
| | |1|Tipo registro|1|Numérico|Obligatorio|Valor Fijo (4)|Indica el tipo de registro de documentos.|
| | |2|Descripción|263|Alfanumérico|Obligatorio|A criterio del cliente|Descripción de pagos relacionados en los registros tipo 6.|
| | | |Longitud total del registro de Adenda|264| | | | |
| | | | | | | | | |
| | |Nota: Este tipo de registro es utilizado para describir en forma narrativa mayor información del pago, que puede ser mostrados a través de notificación vía E-mail.| | | | | | |
| | | |Arriba ↑| | | | | |
| | | | | | | | | |
| | |Registro de Adenda para impresión de comprobantes| | | | | | |
| | | | | | | | | |
| | |Campo|Nombre Campo|Longitud|Formato|Requisito|Valor|Descripción|
| | |1|Tipo registro|1|Numérico|Obligatorio|Valor Fijo (4)|Indica el tipo de registro de documentos.|
| | |2|Indicador de adenda con conceptos|1|Alfanumérico|Obligatorio|Valor fijo: “&”|&: La adenda contiene los conceptos de Ing./Egr relacionados con el pago. Si este campo es diferente de “&”, la adenda es con formato libre, y contiene información enviada a criterio del cliente.  En este caso no aplicaría la estructura de los siguientes campos que se relacionan.|
| | |3|Indicador de concepto1|1|Alfanumérico|Opcional|+ / -|(+) Cuando el concepto corresponde a un Ingreso (-) Cuando el concepto corresponde a un Egreso|
| | |4|Concepto1|30|Alfanumérico|Opcional|Texto especificado por el cliente.| |
| | |5|Valor Concepto1|11|Numérico|Opcional|$$$$$$$$$$$|9 enteros y 2 decimales sin puntos ni comas.|
| | |6|Indicador de concepto2|1|Alfanumérico|Opcional|+ / -|(+) Cuando el concepto corresponde a un Ingreso (-) Cuando el concepto corresponde a un Egreso|
| | |7|Concepto2|30|Alfanumérico|Opcional|Texto especificado por el cliente.| |
| | |8|Valor Concepto2|11|Numérico|Opcional|$$$$$$$$$$$|9 enteros y 2 decimales sin puntos ni comas.|
| | |9|Indicador de concepto3|1|Alfanumérico|Opcional|+ / -|(+) Cuando el concepto corresponde a un Ingreso (-) Cuando el concepto corresponde a un Egreso|
| | |10|Concepto3|30|Alfanumérico|Opcional|Texto especificado por el cliente.| |
| | |11|Valor Concepto3|11|Numérico|Opcional|$$$$$$$$$$$|9 enteros y 2 decimales sin puntos ni comas.|
| | |12|Indicador de concepto4|1|Alfanumérico|Opcional|+ / -|(+) Cuando el concepto corresponde a un Ingreso (-) Cuando el concepto corresponde a un Egreso|
| | |13|Concepto4|30|Alfanumérico|Opcional|Texto especificado por el cliente.| |
| | |14|Valor Concepto4|11|Numérico|Opcional|$$$$$$$$$$$|9 enteros y 2 decimales sin puntos ni comas Ej.: 99999999999 para reportar un valor de 999.999.999,99|
| | |15|Indicador de concepto5|1|Alfanumérico|Opcional|+ / -|(+) Cuando el concepto corresponde a un Ingreso (-) Cuando el concepto corresponde a un Egreso|
| | |16|Concepto5|30|Alfanumérico|Opcional|Texto especificado por el cliente.| |
| | |17|Valor Concepto5|11|Numérico|Opcional|$$$$$$$$$$$|9 enteros y 2 decimales.|
| | |18|Indicador de concepto6|1|Alfanumérico|Opcional|+ / -|(+) Cuando el concepto corresponde a un Ingreso (-) Cuando el concepto corresponde a un Egreso|
| | |19|Concepto6|30|Alfanumérico|Opcional|Texto especificado por el cliente.| |
| | |20|Valor Concepto6|11|Numérico|Opcional|$$$$$$$$$$$|9 enteros y 2 decimales sin puntos ni comas.|
| | |21|Filler|10|Alfanumérico|Opcional|Campo de utilización futura| |
| | | |Longitud total del registro de Adenda|264| | | | |
| | | | | | | | | |
| | | |Arriba ↑| | | | | |
| | | | | | | | | |
| | |Formato de Adenda para Pago de Pensiones| | | | | | |
| | | | | | | | | |
| | |Campo|Nombre Campo|Longitud|Formato|Requisito|Valor|Descripción|
| | |1|Tipo registro|1|Numérico|Obligatorio|Valor fijo (5)|Indica el tipo de registro de documentos para empresas pagadores de pensiones.|
| | |2|Código Afiliación|15|Alfanumérico|Obligatorio|Especificado por el cliente.|Código que identifica al beneficiario ante la entidad pagadora de pensiones.|
| | |3|Período mesada|6|Numérico|Obligatorio|AAAAMM|AAAA= año de la mesada MM= Mes de la mesada|
| | |4|Número de mesada|2|Numérico|Obligatorio|Especificado por el cliente|Número de mesada que se paga al beneficiario.|
| | |5|Código de oficina|3|Numérico|Obligatorio|Oficina válida en el banco|Oficina donde se abrirá la cuenta del pensionado.|
| | |6|Filler|237|Alfanumérico|Opcional|Espacios|Utilización futura.|
| | | |Longitud total del registro de Adenda|264| | | | |
| | | | | | | | | |
| | | |Arriba ↑| | | | | |
| | | | | | | | | |
| | |Formato de Adenda Crédito de Seguridad Social| | | | | | |
| | |Por cada registro de detalle tipo 6 debe llegar un tipo de registro 7,  siempre y cuando la clase de pago sea 242 (Dispersión de Fondos), esta clase de pago permite identificar que el lote corresponde a  pagos de tipo de servicio ‘CCD’ (Concentración y dispersión de fondos) y propósito ‘SSS’ (Sistema Seguridad Social). Las validaciones de la adenda son: • Debe ser la última por cada registro de detalle tipo 6, de no ser así se rechaza el pago. • Es obligatoria para la clase de pago nueva 242. Si no viene dicha adenda, se rechaza el pago. • Si viene esta adenda la clase de pago debe ser una 242, de no ser así se rechaza el pago. • Si viene más de una adenda tipo 7 por cada registro de detalle tipo 6, se rechaza el pago.| | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | |Campo|Nombre Campo|Longitud|Formato|Requisito|Valor|Descripción|
| | |1|Tipo registro|1|Numérico|Obligatorio|Valor fijo (7)|Indica el tipo de adenda seguridad social.|
| | |2|Código Operador de información|2|Numérico|Obligatorio|Campo obligatorio y debe ser diferente de ceros.|Indica el código del Operador de Información No Bancario.|
| | |3|Número de Planilla|15|Alfanumérico|Obligatorio|Campo obligatorio y debe ser diferente de blancos.|Número de la planilla a pagar. Debe ser un campo alineado a la izquierda con dos espacios a la derecha.|
| | |4|Número de Registros de planilla|6|Numérico|Obligatorio|Campo obligatorio y debe ser diferente de ceros.|Número de registros que contiene la planilla liquidada.|
| | |5|Código entidad financiera originadora|8|Numérico|Obligatorio|Campo obligatorio y debe ser diferente de ceros.|Corresponde al código de la entidad  financiera originadora.|
| | |6|Código Administradora|6|Alfanumérico|Obligatorio|Campo obligatorio y debe ser diferente de blancos.|Código Administradora a la que se realiza la acreditación del Pago.|
| | |7|NIT del aportante|16|Alfanumérico|Obligatorio|Campo obligatorio y debe ser diferente de blancos.|Corresponde a la identificación del aportante.|
| | |8|Periodo de pago|6|Numérico|Obligatorio|Campo obligatorio y debe ser diferente de ceros.|Contiene el periodo al que corresponde el pago a realizar.|
| | |9|Canal de Pago|2|Alfanumérico|Obligatorio|Campo obligatorio y debe ser diferente de blancos.|Corresponde al canal por el que se realiza el pago.|
| | |10|Nombre del aportante|16|Alfanumérico|Obligatorio|Campo obligatorio y debe ser diferente de blancos.|Nombre del aportante. Sólo se requieren 16 posiciones.|
| | | |Longitud total del registro de Adenda|78| | | | |
| | | | | | | | | |
| | | |Arriba ↑| | | | | |
| | | | | | | | | |
| | |Formato de Adenda para Facturación Electrónica| | | | | | |
| | | | | | | | | |
| | |Campo|Nombre Campo|Longitud|Formato|Requisito|Valor|Descripción|
| | |1|Tipo registro|1|Numérico|Obligatorio|Valor Fijo (8)|Tipo de adenda que identifica información de facturas de clientes de la ventanilla única de receptoría de Carvajal.|
| | |2|Número de la factura|35|Alfanumérico|Obligatorio|Según cada empresa|Número de la factura a pagar.|
| | |3|Valor neto|17|Numérico|Obligatorio|Valor Neto|Valor neto a pagar, 15 enteros y 2 decimales.|
| | |4|Referencia 1|25|Alfanumérico|Opcional|Según cada empresa|Referencia.|
| | |5|Referencia 2|25|Alfanumérico|Opcional|Según cada empresa|Referencia.|
| | |6|Referencia 3|25|Alfanumérico|Opcional|Según cada empresa|Referencia.|
| | |7|Filler |136|Alfanumérico|Opcional| |Información adicional sobre la factura a pagar.|
| | | |Longitud total del registro de Adenda|264| | | | |
| | | | | | | | | |
| | | |Arriba ↑| | | | | |
| | | | | | | | | |
| | |Formato de Adenda Referencias adicionales para el beneficiario del pago | | | | | | |
| | |1. Esta adenda es opcional, y puede ser usada para relacionar dos referencias adicionales para los pagos con destino a otros bancos. 2. Cuando el cliente pagador no envíe esta adenda en su archivo plano, el Banco enviará por defecto a ACH en la referencia 1: la referencia diligenciada en el registro de detalle del pago, si ésta no se recibe, se enviará el nit pagador; para la referencia 2 se enviará el nombre del Pagador. 3. Si el cliente envía esta adenda para un registro de pago con destino Bancolombia, no se rechazará el pago. 4. Cuando el cliente envíe más de una adenda para un mismo registro de detalle tipo 6, se enviará a ACH la información contenida en el primer registro de adenda.| | | | | | |
| | |Campo|Nombre Campo|Longitud|Formato|Requisito|Valor|Descripción|
| | |1|Tipo registro|1|Numérico|Obligatorio|Valor fijo (4)|Indica el tipo de registro.|
| | |2|Tipo de Información|1|Alfanumérico|Obligatorio|Valor fijo (=)|Indica el tipo de información.|
| | |3|Número de factura|24|Alfanumérico|Opcional|Texto Libre|Número de factura, cuenta de cobro, recibo de pago, referencia de pago electrónico, código numérico o alfanumérico que identifica al cliente de manera única ante el receptor u otro que identifique el pago que el originador está realizando.|
| | |4|Filler|11|Alfanumérico|Opcional|Espacios en Blanco|Espacios en Blanco para uso futuro|
| | |5|Información libre del originador|24|Alfanumérico|Opcional|Texto Libre|Campo diligenciado libremente por el originador para referenciar su pago.|
| | |6|Filler|11|Alfanumérico|Opcional|Espacios en Blanco|Espacios en Blanco para uso futuro|
| | |7|Filler|192|Alfanumérico|Opcional|Espacios en Blanco|Espacios en Blanco|
| | | |Longitud total del registro de Adenda|264| | | | |
| | | | | | | | | |
| | | |Arriba ↑| | | | | |
