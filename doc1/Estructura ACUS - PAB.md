| | | | | | | |
|-|-|-|-|-|-|-|
| | | | | | | |
|PAB| | | | | | |
| | | | | | | |
|Field|Field name|Length|Format|Description| |Example:|
|1|Payer's tax ID|13|Numeric *|Tax ID of the entity that sends the Payment lot. Right-aligned with leading zeros.| |0000042825951AA000001000000000000012.00|
|2|Payment Sequence |2|Alfanumeric|Sequence of sending lots. The same sequence cannot be sent on the same day.| |Archivo recibido y validado exitosamente|
|3|Number of registers|6|Numeric *|Sum of the number of registers records including addenda. Right-aligned with leading zeros.| |0000042825951AA000001000000000000012.00|
|4|Total value of payments|15.2|Numeric *|It is the total value of the payments to be paid to the beneficiaries. 15 entire numbers, dot and 2 decimals. 18 digits in total.| |Archivo recibido y rechazado completamente Código causal + Descripción de la causal en el sistema de pagos|
|5|Validation message|Variable|Alfanumeric|Corresponds to the file structure validation message. Detailed information on the beneficiaries is not reviewed. The possible values are: a. Archivo recibido y validado exitosamente / file recevied and validated successfully. b. Archivo recibido y rechazado completamente + Código causal + Descripción de la causal en el sistema de pagos /File received and rejected completely + rejection code + description of rejection.| | |
