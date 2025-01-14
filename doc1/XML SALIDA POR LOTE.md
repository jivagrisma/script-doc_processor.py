| | | | | |
|-|-|-|-|-|
| | | | | |
| | | | | |
| | | | | |
| |<XML Tag>|Description|Requerido|Mapeo|
| |<CstmrPmtStsRpt>| |Si| |
| |<GrpHdr>| |Si| |
| |<MsgId>|Referencia asignada por Bancolombia al mensaje|Si|Campo 20, línea 1, posición inicial 1|
| |<CreDtTm>|Fecha y hora de envío del acuse|Si|Formato: AAAA-MM-DDTHH:MM:SS Ejemplo: 2017-07-04T12:01:00|
| |<InitgPty>| |Si| |
| |<Id>| |Si| |
| |<OrgId>| |Si| |
| |<BICOrBEI>|Código BIC Bancolombia |Si|COLOCOBM|
| |<OrgnlGrpInfAndSts>| |Si| |
| |<OrgnlMsgId>|Referencia de lote enviada en el MsgId de la instrucción de pago|Si|Campo 20, línea 2, posición inicial 1|
| |<OrgnlMsgNmId>|Mensaje al cual corresponde la estructura del pago original |Si|Valor Fijo: pain.001.001.03|
| |<OrgnlCreDtTm>|Fecha y hora de envío del acuse|Si|Formato: AAAA-MM-DDTHH:MM:SS Ejemplo: 2017-07-04T12:01:00|
| |<OrgnlNbOfTxs>|Número de transacciones del lote|Si|Campo 20, línea 4, posición inicial 1|
| |<OrgnlCtrlSum>|Valor transacciones del lote|Si|Campo 20, línea 5, posición inicial 1|
| |<GrpSts>|Estado del lote|Si|Campo 79, línea 2, posición inicial 1|
| |<StsRsnInf>| |Si| |
| |<AddtlInf>| Descripción del estado del lote: |Si|Campo 79, línea 1, posición inicial 1|
