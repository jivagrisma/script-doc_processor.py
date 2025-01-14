| | | | | | | | | |
|-|-|-|-|-|-|-|-|-|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | |Corresponden a los formatos que actualmente maneja el Grupo Bancolombia para el envío de la información a los clientes, dónde se identifica el estado final de cada uno de los pagos ordenados (aprobados y  rechazados).  Después del procesamiento el sistema de pagos arroja un código de respuesta de acuerdo a las validaciones realizadas. Estos códigos deben ser consultados por el cliente por medio del canal (SVE, ENL) y son los códigos que se entregarán en el archivo de respuesta.  | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | |El Archivo tiene la siguiente estructura:| | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | |Campo|Nombre Campo|Longitud|Formato|Valor|Descripción|
| | | |1|NIT empresa pagadora |13|Numérico *| |Nit de la entidad que envía el lote. Alineado a la derecha con ceros a la izquierda.|
| | | |2|Fecha transmisión de los pagos |8|Numérico |DDMMAAAA|Fecha de transmisión de lote. |
| | | |3|Secuencia del lote de pagos|2|Alfanumerico|A, B, C, ... |Secuencia de envío de lotes. En un mismo día no puede enviarse la misma secuencia.|
| | | |4|Tipo registro|1|Numérico|Valor fijo: 6 |Indica el tipo de registro de detalle|
| | | |5|NIT del beneficiario|15|Numérico *| |Nit del beneficiario del pago. Alineado a la derecha con ceros a la izquierda.|
| | | |6|Nombre del beneficiario |30|Alfanumérico| |Nombre del beneficiario del pago|
| | | |7|Código Banco Destino|9|Numérico *| |Banco cuenta del beneficiario. Se entrega solo si la transacción fue abono a cuenta. Alineado a la derecha con ceros a la izquierda.|
| | | |8|Numero de cuenta del beneficiario|17|Numérico *| |Numero de cuenta del beneficiario (ahorros, corriente, tarjeta de crédito otros bancos, número de obligación otros bancos). Se entrega solo si la transacción fue abono a cuenta. Alineado a la derecha con ceros a laizquierda.|
| | | |9|Tipo de cuenta|1|Alfanumérico|S| |
| | | |10|Tipo de transacción   |2|Numérico|Ver anexo 2|Corresponde al tipo de abono realizado al beneficiario|
| | | |11|Valor|17|Numérico (15 ent, un punto y  2 decimales)  *|15 enteros, un punto y 2 decimales|Valor transacción. Puede ser cero si se trata de una transacción de Prenotificación. Alineado a la derecha con ceros a laizquierda.|
| | | |12|Concepto|9|Alfanumerico| |Aplica para SAP|
| | | |13|Referencia|13|Alfanumerico| |Referencia del pago, a criterio del cliente. Para los pagos de cuenta maestra régimen contributivo, los dos primeros caracteres de la referencia deben traer el concepto de Giro. |
| | | |14|Código de respuesta|3|Alfanumerico|Ver anexo 4|Corresponde al código que asigna pagos para identificar el resultado del procesamiento de cada registro|
| | | |15|Numero Cheque|8|Numérico *| |Número del chque pagado por ventanilla. Alineado a la derecha con ceros a laizquierda.|
| | | |16|Fecha de Aplicación|8|Alfanumérico|DDMMAAAA|Fecha en que se debe realizar el pago al beneficiario. Si está en ceros o errada se asume fecha de aplicación del registro de control.|
| | | | |Longitud total del registro de Adenda|156| | | |
| | | | |NOTA: Los Campos que están marcados con asterisco (*) son  ajustados a la derecha y rellenos de ceros por la izquierda| | | | |
| | |Arriba ↑| | | | | | |
