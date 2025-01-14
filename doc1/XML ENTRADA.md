| | | | | | | | | | | | | | | | | | | | |
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
| | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | |
| |Index|Lvl|Name| | | | | |XML Tag| |Mult|Type / Code| |Longitud Máxima|Requerido|Formato|Descripción|Mapeo MT101 (La posición inicial se cuenta luego de los dos puntos (:) en donde inicia el campo|Additional details (Informativo)|
| | |0|Customer Credit Transfer Initiation V03 (pain.001.001.03)| | | | | |<CstmrCdtTrfInitn >| | | | | |Si| |Tag de inicio de agrupación de contenido| | |
| |1.0|1|Group Header| | | | | |<GrpHdr>| |[1..1]| | | |Si| |Los tags contenidos en esta etiqueta corresponden a la linformación del registro de control| | |
| |1.1|2|Message Identification| | | | | |<MsgId>| |[1..1]|text{1,35}| |16 (si supera 16 se se trunca)|Si|Alfanumérico|Referencia del mensaje| | |
| |1.2|2|Creation Date Time| | | | | |<CreDtTm>| |[1..1]|dateTime| | |Si| |Tag de inicio de agrupación de contenido| | |
| |1.3|2|Authorisation| | | | | |<Authstn>| |[0..2]|Choice| | |No| | | | |
| |1.4|3|Code| | | | | |<Cd>| |[1..1]|text| | |No| | | | |
| | |4|Pre Authorised File| | | | | | | | |AUTH| | |No| | | | |
| | |4|File Level Authorisation Details| | | | | | | | |FDET| | |No| | | | |
| | |4|File Level Authorisation Summary| | | | | | | | |FSUM| | |No| | | | |
| | |4|Instruction Level Authorisation| | | | | | | | |ILEV| | |No|Numérico|Clase de pago, este campo puede dejarse vacío o diligenciarse con la clase de pago respectiva o diligenciarse con la clase de pago más el indicador de uso   01 - Facturación electrónica 02 - Referencias ACH  Ejemplo: 238/01  En cada pago sólo es posible reportar un indicador de uso. ( las clases de pago más comunes son 220-pago proveedores y 225-pago de nomina)| | |
| |1.5|3|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,128}| | |No| | | | |
| |1.6|2|Number Of Transactions| | | | | |<NbOfTxs>| |[1..1]|text [0-9]{1,15}| | |Si| |Tag de inicio de agrupación de contenido| | |
| |1.7|2|Control Sum| | | | | |<CtrlSum>| |[0..1]|decimal td = 18 fd = 17| | |Si| |Tag de inicio de agrupación de contenido| | |
| |1.8|2|Initiating Party| | | | | |<InitgPty>| |[1..1]| | | |Si| |Tag de inicio de agrupación de contenido| | |
| | |3|Name| | | | | |<Nm>| |[0..1]|text{1,140}| |30 (si supera 30 trunca)|Si|Alfanumérico|Nombre del pagador| | |
| |9.1.1|3|Postal Address| | | | | |<PstlAdr>| |[0..1]| | |X|No| | | | |
| |9.1.1 2|3|Identification| | | | | |<Id>| |[0..1]|Choice| | |No| | | | |
| |9.1.1 3|4|Organisation Identification| | | | | |<OrgId>| |[1..1]| | | |No| | | | |
| |9.1.1 4|5|BIC Or BEI| | | | | |<BICOrBEI>| |[0..1]|text [A-Z]{6,6}[A-Z2- 9][A-NP-Z0- 9]([A-Z0- 9]{3,3}){0,1}| |12|No|Alfanumérico|Código Swift del cliente Pagador| | |
| |9.1.1 5|5|Other| | | | | |<Othr>| |[0..*]| | | |No| | | | |
| |9.1.1 6|6|Identification| | | | | |<Id>| |[1..1]|text{1,35}| |15 (si supera 15 se aplican las 15 primeras)|Si|Alfanumérico|Nit del pagador| | |
| |9.1.1 7|6|Scheme Name| | | | | |<SchmeNm>| |[0..1]|Choice| | |No| | | | |
| |9.1.1 8|7|Code| | | | | |<Cd>| |[1..1]|text{1,4}| | |No| | | | |
| |9.1.1 9|7|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| |X|No| | | | |
| |9.1.2 0|6|Issuer| | | | | |<Issr>| |[0..1]|text{1,35}| | |No| | | | |
| |9.1.2 1|4|Private Identification| | | | | |<PrvtId>| |[1..1]| | |X|No| | | | |
| |9.1.3 3|3|Country Of Residence| | | | | |<CtryOfRes>| |[0..1]|text [A-Z]{2,2}| |X|No| | | | |
| |9.1.3 4|3|Contact Details| | | | | |<CtctDtls>| |[0..1]| | |X|No| | | | |
| |1.9|2|Forwarding Agent| | | | | |<FwdgAgt>| |[0..1]| | |X|No| | | | |
| |2.0|1|Payment Information| | | | | |<PmtInf>| |[1..*]| | | |Si| |Los tags contenidos en esta etiqueta corresponden a la linformación del registro de detalle.Este Tag se debe repetir por cada pago dentro del archivo.| | |
| |2.1|2|Payment Information Identification| | | | | |<PmtInfId>| |[1..1]|text{1,35}| | |Si| |Tag de inicio de agrupación de contenido| | |
| |2.2|2|Payment Method| | | | | |<PmtMtd>| |[1..1]|text| |5|Si|Alfanumérico|Este campo permite identificar el tipo de transacción:  TRF: Transferencia CHK: Pago en cheque EFE: Pago en Efectivo| | |
| | |3|Cheque| | | | | | | | |CHK| | |No| | | | |
| | |3|Credit Transfer| | | | | | | | |TRF| | |No| | | | |
| | |3|Transfer Advice| | | | | | | | |TRA| |X|No| | | | |
| |2.3|2|Batch Booking| | | | | |<BtchBookg>| |[0..1]|boolean| | |No| | | | |
| |2.4|2|Number Of Transactions| | | | | |<NbOfTxs>| |[0..1]|text [0-9]{1,15}| | |No| | | | |
| |2.5|2|Control Sum| | | | | |<CtrlSum>| |[0..1]|decimal td = 18 fd = 17| | |No| | | | |
| |2.6|2|Payment Type Information| | | | | |<PmtTpInf>| |[0..1]| | | |No| | | | |
| |2.7|3|Instruction Priority| | | | | |<InstrPrty>| |[0..1]|text| | |No| | | | |
| | |4|High| | | | | | | | |HIGH| | |No| | | | |
| | |4|Normal| | | | | | | | |NORM| | |No| | | | |
| |2.8|3|Service Level| | | | | |<SvcLvl>| |[0..1]|Choice| | |No| | | | |
| |2.9|4|Code| | | | | |<Cd>| |[1..1]|text{1,4}| | |No| | | | |
| |2.10|4|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |2.11|3|Local Instrument| | | | | |<LclInstrm>| |[0..1]|Choice| | |No| | | | |
| |2.12|4|Code| | | | | |<Cd>| |[1..1]|text{1,35}| | |No| | | | |
| |2.13|4|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No|Numérico| | | |
| |2.14|3|Category Purpose| | | | | |<CtgyPurp>| |[0..1]|Choice| | |No| | | | |
| |2.15|4|Code| | | | | |<Cd>| |[1..1]|text{1,4}| | |No| | | | |
| |2.16|4|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |2.17|2|Requested Execution Date| | | | | |<ReqdExctnDt>| |[1..1]|date| |YYYY-MM-DD|Si|Fecha|Fecha de aplicación del pago YYYY-MM-DD| | |
| |2.18|2|Pooling Adjustment Date| | | | | |<PoolgAdjstmntDt >| |[0..1]|date| |X|No| | | | |
| |2.19|2|Debtor| | | | | |<Dbtr>| |[1..1]| | | |Si| |Tag de inicio de agrupación de contenido| | |
| | |3|Name| | | | | |<Nm>| |[0..1]|text{1,140}| |[1..1]|Si| |Nombre Pagador| | |
| |9.1.1|3|Postal Address| | | | | |<PstlAdr>| |[0..1]| | |[1..1]|No| | | | |
| |9.1.2|4|Address Type| | | | | |<AdrTp>| |[0..1]|text| |X|No| | | | |
| |9.1.3|4|Department| | | | | |<Dept>| |[0..1]|text{1,70}| | |No| | | | |
| |9.1.4|4|Sub Department| | | | | |<SubDept>| |[0..1]|text{1,70}| | |No| | | | |
| |9.1.5|4|Street Name| | | | | |<StrtNm>| |[0..1]|text{1,70}| | |No| | | | |
| |9.1.6|4|Building Number| | | | | |<BldgNb>| |[0..1]|text{1,16}| | |No| | | | |
| |9.1.7|4|Post Code| | | | | |<PstCd>| |[0..1]|text{1,16}| | |No| | | | |
| |9.1.8|4|Town Name| | | | | |<TwnNm>| |[0..1]|text{1,35}| | |No| | | | |
| |9.1.9|4|Country Sub Division| | | | | |<CtrySubDvsn>| |[0..1]|text{1,35}| | |No| | | | |
| |9.1.1 0|4|Country| | | | | |<Ctry>| |[0..1]|text [A-Z]{2,2}| |[1..1]|No| | | | |
| |9.1.1 1|4|Address Line| | | | | |<AdrLine>| |[0..7]|text{1,70}| | |No| | | | |
| |9.1.1 2|3|Identification| | | | | |<Id>| |[0..1]|Choice| | |No| | | | |
| |9.1.1 3|4|Organisation Identification| | | | | |<OrgId>| |[1..1]| | | |No| | | | |
| |9.1.1 4|5|BIC Or BEI| | | | | |<BICOrBEI>| |[0..1]|text [A-Z]{6,6}[A-Z2- 9][A-NP-Z0- 9]([A-Z0- 9]{3,3}){0,1}| | |No| |Código Swift del Banco Pagador| | |
| |9.1.1 5|5|Other| | | | | |<Othr>| |[0..*]| | | |No| | | | |
| |9.1.1 6|6|Identification| | | | | |<Id>| |[1..1]|text{1,35}| | |No| | | | |
| |9.1.1 7|6|Scheme Name| | | | | |<SchmeNm>| |[0..1]|Choice| | |No| | | | |
| |9.1.1 8|7|Code| | | | | |<Cd>| |[1..1]|text{1,4}| | |No| | | | |
| |9.1.1 9|7|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |9.1.2 0|6|Issuer| | | | | |<Issr>| |[0..1]|text{1,35}| |X|No| | | | |
| |9.1.2 1|4|Private Identification| | | | | |<PrvtId>| |[1..1]| | | |No| | | | |
| |9.1.2 2|5|Date And Place Of Birth| | | | | |<DtAndPlcOfBirth >| |[0..1]| | |X|No| | | | |
| |9.1.2 7|5|Other| | | | | |<Othr>| |[0..*]| | | |No| | | | |
| |9.1.2 8|6|Identification| | | | | |<Id>| |[1..1]|text{1,35}| | |No| | | | |
| |9.1.2 9|6|Scheme Name| | | | | |<SchmeNm>| |[0..1]|Choice| | |No| | | | |
| |9.1.3 0|7|Code| | | | | |<Cd>| |[1..1]|text{1,4}| | |No| | | | |
| |9.1.3 1|7|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |9.1.3 2|6|Issuer| | | | | |<Issr>| |[0..1]|text{1,35}| |X|No| | | | |
| |9.1.3 3|3|Country Of Residence| | | | | |<CtryOfRes>| |[0..1]|text [A-Z]{2,2}| | |No| | | | |
| |9.1.3 4|3|Contact Details| | | | | |<CtctDtls>| |[0..1]| | | |No| | | | |
| |9.1.3 5|4|Name Prefix| | | | | |<NmPrfx>| |[0..1]|text| | |No| | | | |
| | |5|Doctor| | | | | | | | |DOCT| | |No| | | | |
| | |5|Mister| | | | | | | | |MIST| | |No| | | | |
| | |5|Miss| | | | | | | | |MISS| | |No| | | | |
| | |5|Madam| | | | | | | | |MADM| | |No| | | | |
| |9.1.3 6|4|Name| | | | | |<Nm>| |[0..1]|text{1,140}| | |No| | | | |
| |9.1.3 7|4|Phone Number| | | | | |<PhneNb>| |[0..1]|text \+[0-9]{1,3}-[0- 9()+\-]{1,30}| | |No| | | | |
| |9.1.3 8|4|Mobile Number| | | | | |<MobNb>| |[0..1]|text \+[0-9]{1,3}-[0- 9()+\-]{1,30}| | |No| | | | |
| |9.1.3 9|4|Fax Number| | | | | |<FaxNb>| |[0..1]|text \+[0-9]{1,3}-[0- 9()+\-]{1,30}| | |No| | | | |
| |9.1.4 0|4|Email Address| | | | | |<EmailAdr>| |[0..1]|text{1,2048}| | |No| | | | |
| |9.1.4 1|4|Other| | | | | |<Othr>| |[0..1]|text{1,35}| | |No| | | | |
| |2.20|2|Debtor Account| | | | | |<DbtrAcct>| |[1..1]| | |11|Si, en transferencias|Numérico|Cuenta del pagador  <Id>       <Othr>                     <Id>| | |
| |2.20|2|Debtor Account| | | | | |<DbtrAcct>| |[1..1]| | |5|Si, en transferencias|Alfanumérico|Tipo de cuenta del pagador <Id>       <Othr>                     <Id> <Tp>                                                                  <Cd> CACC: cuenta Corriente SVGS: cuenta Ahorros| | |
| | |3|Identification| | | | | |<Id>| |[1..1]|Choice| | |No| | | | |
| |1.1.1|4|IBAN| | | | | |<IBAN>| |[1..1]|text [A-Z]{2,2}[0- 9]{2,2}[a-zA-Z0- 9]{1,30}| | |No| | | | |
| |1.1.2|4|Other| | | | | |<Othr>| |[1..1]| | | |No| | | | |
| |1.1.3|5|Identification| | | | | |<Id>| |[1..1]|text{1,34}| | |No| | | | |
| |1.1.4|5|Scheme Name| | | | | |<SchmeNm>| |[0..1]|Choice| | |No| | | | |
| |1.1.5|6|Code| | | | | |<Cd>| |[1..1]|text{1,4}| | |No| | | | |
| |1.1.6|6|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |1.1.7|5|Issuer| | | | | |<Issr>| |[0..1]|text{1,35}| | |No| | | | |
| |1.1.8|3|Type| | | | | |<Tp>| |[0..1]| | |[1..1]|No| | | | |
| | |4|[XOR]| | | | | | | | |Choice| | |No| | | | |
| |1.1.9|5|Code| | | | | |<Cd>| |[1..1]|text| | |No| | | | |
| | |6|Cash Payment| | | | | | | | |CASH| | |No| | | | |
| | |6|Charges| | | | | | | | |CHAR| |X|No| | | | |
| | |6|Commission| | | | | | | | |COMM| | |No| | | | |
| | |6|Tax| | | | | | | | |TAXE| |X|No| | | | |
| | |6|Cash Income| | | | | | | | |CISH| | |No| | | | |
| | |6|Cash Trading| | | | | | | | |TRAS| | |No| | | | |
| | |6|Settlement| | | | | | | | |SACC| | |No| | | | |
| | |6|Current| | | | | | | | |CACC| | |No| | | | |
| | |6|Savings| | | | | | | | |SVGS| | |No| | | | |
| | |6|Over Night Deposit| | | | | | | | |ONDP| | |No| | | | |
| | |6|Marginal Lending| | | | | | | | |MGLD| |X|No| | | | |
| | |6|Non Resident External| | | | | | | | |NREX| |X|No| | | | |
| | |6|Money Market| | | | | | | | |MOMA| | |No| | | | |
| | |6|Loan| | | | | | | | |LOAN| | |No| | | | |
| | |6|Salary| | | | | | | | |SLRY| |X|No| | | | |
| | |6|Overdraft| | | | | | | | |ODFT| | |No| | | | |
| |1.1.1 0|5|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |1.1.1 1|3|Currency| | | | | |<Ccy>| |[0..1]|text [A-Z]{3,3}| | |No| | | | |
| |1.1.1 2|3|Name| | | | | |<Nm>| |[0..1]|text{1,70}| |X|No| | | | |
| |2.21|2|Debtor Agent| | | | | |<DbtrAgt>| |[1..1]| | | |No| | | | |
| | |3|Financial Institution Identification| | | | | |<FinInstnId>| |[1..1]| | | |No| | | | |
| |6.1.1|4|BIC| | | | | |<BIC>| |[0..1]|text [A-Z]{6,6}[A-Z2- 9][A-NP-Z0- 9]([A-Z0- 9]{3,3}){0,1}| | |No| |Código Swift del Banco Pagador| | |
| |6.1.2|4|Clearing System Member Identification| | | | | |<ClrSysMmbId>| |[0..1]| | | |No| | | | |
| |6.1.3|5|Clearing System Identification| | | | | |<ClrSysId>| |[0..1]|Choice| | |No| | | | |
| |6.1.4|6|Code| | | | | |<Cd>| |[1..1]|text{1,5}| | |No| | | | |
| |6.1.5|6|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |6.1.6|5|Member Identification| | | | | |<MmbId>| |[1..1]|text{1,35}| | |No| | | | |
| |6.1.7|4|Name| | | | | |<Nm>| |[0..1]|text{1,140}| |X|No| | | | |
| |6.1.8|4|Postal Address| | | | | |<PstlAdr>| |[0..1]| | |[1..1]|No| | | | |
| |6.1.9|5|Address Type| | | | | |<AdrTp>| |[0..1]|text| |X|No| | | | |
| |6.1.1 0|5|Department| | | | | |<Dept>| |[0..1]|text{1,70}| |X|No| | | | |
| |6.1.1 1|5|Sub Department| | | | | |<SubDept>| |[0..1]|text{1,70}| |X|No| | | | |
| |6.1.1 2|5|Street Name| | | | | |<StrtNm>| |[0..1]|text{1,70}| |X|No| | | | |
| |6.1.1 3|5|Building Number| | | | | |<BldgNb>| |[0..1]|text{1,16}| |X|No| | | | |
| |6.1.1 4|5|Post Code| | | | | |<PstCd>| |[0..1]|text{1,16}| |X|No| | | | |
| |6.1.1 5|5|Town Name| | | | | |<TwnNm>| |[0..1]|text{1,35}| |X|No| | | | |
| |6.1.1 6|5|Country Sub Division| | | | | |<CtrySubDvsn>| |[0..1]|text{1,35}| |X|No| | | | |
| |6.1.1 7|5|Country| | | | | |<Ctry>| |[0..1]|text [A-Z]{2,2}| |[1..1]|No| | | | |
| |6.1.1 8|5|Address Line| | | | | |<AdrLine>| |[0..7]|text{1,70}| |X|No| | | | |
| |6.1.1 9|4|Other| | | | | |<Othr>| |[0..1]| | |X|No| | | | |
| |6.1.2 5|3|Branch Identification| | | | | |<BrnchId>| |[0..1]| | | |No| | | | |
| |6.1.2 6|4|Identification| | | | | |<Id>| |[0..1]|text{1,35}| | |No| | | | |
| |6.1.2 7|4|Name| | | | | |<Nm>| |[0..1]|text{1,140}| |X|No| | | | |
| |6.1.2 8|4|Postal Address| | | | | |<PstlAdr>| |[0..1]| | |X|No| | | | |
| |2.22|2|Debtor Agent Account| | | | | |<DbtrAgtAcct>| |[0..1]| | |X|No| | | | |
| |2.23|2|Ultimate Debtor| | | | | |<UltmtDbtr>| |[0..1]| | | |No| | | | |
| | |3|Name| | | | | |<Nm>| |[0..1]|text{1,140}| |[1..1]|No| | | | |
| |9.1.1|3|Postal Address| | | | | |<PstlAdr>| |[0..1]| | | |No| | | | |
| |9.1.2|4|Address Type| | | | | |<AdrTp>| |[0..1]|text| |X|No| | | | |
| |9.1.3|4|Department| | | | | |<Dept>| |[0..1]|text{1,70}| | |No| | | | |
| |9.1.4|4|Sub Department| | | | | |<SubDept>| |[0..1]|text{1,70}| | |No| | | | |
| |9.1.5|4|Street Name| | | | | |<StrtNm>| |[0..1]|text{1,70}| | |No| | | | |
| |9.1.6|4|Building Number| | | | | |<BldgNb>| |[0..1]|text{1,16}| | |No| | | | |
| |9.1.7|4|Post Code| | | | | |<PstCd>| |[0..1]|text{1,16}| | |No| | | | |
| |9.1.8|4|Town Name| | | | | |<TwnNm>| |[0..1]|text{1,35}| | |No| | | | |
| |9.1.9|4|Country Sub Division| | | | | |<CtrySubDvsn>| |[0..1]|text{1,35}| | |No| | | | |
| |9.1.1 0|4|Country| | | | | |<Ctry>| |[0..1]|text [A-Z]{2,2}| |[1..1]|No| | | | |
| |9.1.1 1|4|Address Line| | | | | |<AdrLine>| |[0..7]|text{1,70}| | |No| | | | |
| |9.1.1 2|3|Identification| | | | | |<Id>| |[0..1]|Choice| | |No| | | | |
| |9.1.1 3|4|Organisation Identification| | | | | |<OrgId>| |[1..1]| | | |No| | | | |
| |9.1.1 4|5|BIC Or BEI| | | | | |<BICOrBEI>| |[0..1]|text [A-Z]{6,6}[A-Z2- 9][A-NP-Z0- 9]([A-Z0- 9]{3,3}){0,1}| | |No| | | | |
| |9.1.1 5|5|Other| | | | | |<Othr>| |[0..*]| | | |No| | | | |
| |9.1.1 6|6|Identification| | | | | |<Id>| |[1..1]|text{1,35}| | |No| | | | |
| |9.1.1 7|6|Scheme Name| | | | | |<SchmeNm>| |[0..1]|Choice| | |No| | | | |
| |9.1.1 8|7|Code| | | | | |<Cd>| |[1..1]|text{1,4}| | |No| | | | |
| |9.1.1 9|7|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |9.1.2 0|6|Issuer| | | | | |<Issr>| |[0..1]|text{1,35}| |X|No| | | | |
| |9.1.2 1|4|Private Identification| | | | | |<PrvtId>| |[1..1]| | | |No| | | | |
| |9.1.2 2|5|Date And Place Of Birth| | | | | |<DtAndPlcOfBirth >| |[0..1]| | |X|No| | | | |
| |9.1.2 7|5|Other| | | | | |<Othr>| |[0..*]| | | |No| | | | |
| |9.1.2 8|6|Identification| | | | | |<Id>| |[1..1]|text{1,35}| | |No| | | | |
| |9.1.2 9|6|Scheme Name| | | | | |<SchmeNm>| |[0..1]|Choice| | |No| | | | |
| |9.1.3 0|7|Code| | | | | |<Cd>| |[1..1]|text{1,4}| | |No| | | | |
| |9.1.3 1|7|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| |X|No| | | | |
| |9.1.3 2|6|Issuer| | | | | |<Issr>| |[0..1]|text{1,35}| |X|No| | | | |
| |9.1.3 3|3|Country Of Residence| | | | | |<CtryOfRes>| |[0..1]|text [A-Z]{2,2}| | |No| | | | |
| |9.1.3 4|3|Contact Details| | | | | |<CtctDtls>| |[0..1]| | | |No| | | | |
| |9.1.3 5|4|Name Prefix| | | | | |<NmPrfx>| |[0..1]|text| | |No| | | | |
| | |5|Doctor| | | | | | | | |DOCT| | |No| | | | |
| | |5|Mister| | | | | | | | |MIST| | |No| | | | |
| | |5|Miss| | | | | | | | |MISS| | |No| | | | |
| | |5|Madam| | | | | | | | |MADM| | |No| | | | |
| |9.1.3 6|4|Name| | | | | |<Nm>| |[0..1]|text{1,140}| | |No| | | | |
| |9.1.3 7|4|Phone Number| | | | | |<PhneNb>| |[0..1]|text \+[0-9]{1,3}-[0- 9()+\-]{1,30}| | |No| | | | |
| |9.1.3 8|4|Mobile Number| | | | | |<MobNb>| |[0..1]|text \+[0-9]{1,3}-[0- 9()+\-]{1,30}| | |No| | | | |
| |9.1.3 9|4|Fax Number| | | | | |<FaxNb>| |[0..1]|text \+[0-9]{1,3}-[0- 9()+\-]{1,30}| | |No| | | | |
| |9.1.4 0|4|Email Address| | | | | |<EmailAdr>| |[0..1]|text{1,2048}| | |No| | | | |
| |9.1.4 1|4|Other| | | | | |<Othr>| |[0..1]|text{1,35}| | |No| | | | |
| |2.24|2|Charge Bearer| | | | | |<ChrgBr>| |[0..1]|text| | |No| | | | |
| | |3|Borne By Debtor| | | | | | | | |DEBT| | |No| | | | |
| | |3|Borne By Creditor| | | | | | | | |CRED| | |No| | | | |
| | |3|Shared| | | | | | | | |SHAR| | |No| | | | |
| | |3|Following Service Level| | | | | | | | |SLEV| | |No| | | | |
| |2.25|2|Charges Account| | | | | |<ChrgsAcct>| |[0..1]| | | |No| | | | |
| | |3|Identification| | | | | |<Id>| |[1..1]|Choice| | |No| | | | |
| |1.1.1|4|IBAN| | | | | |<IBAN>| |[1..1]|text [A-Z]{2,2}[0- 9]{2,2}[a-zA-Z0- 9]{1,30}| | |No| | | | |
| |1.1.2|4|Other| | | | | |<Othr>| |[1..1]| | | |No| | | | |
| |1.1.3|5|Identification| | | | | |<Id>| |[1..1]|text{1,34}| | |No| | | | |
| |1.1.4|5|Scheme Name| | | | | |<SchmeNm>| |[0..1]|Choice| | |No| | | | |
| |1.1.5|6|Code| | | | | |<Cd>| |[1..1]|text{1,4}| | |No| | | | |
| |1.1.6|6|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |1.1.7|5|Issuer| | | | | |<Issr>| |[0..1]|text{1,35}| | |No| | | | |
| |1.1.8|3|Type| | | | | |<Tp>| |[0..1]| | | |No| | | | |
| | |4|[XOR]| | | | | | | | |Choice| | |No| | | | |
| |1.1.9|5|Code| | | | | |<Cd>| |[1..1]|text| | |No| | | | |
| | |6|Cash Payment| | | | | | | | |CASH| | |No| | | | |
| | |6|Charges| | | | | | | | |CHAR| | |No| | | | |
| | |6|Commission| | | | | | | | |COMM| | |No| | | | |
| | |6|Tax| | | | | | | | |TAXE| | |No| | | | |
| | |6|Cash Income| | | | | | | | |CISH| | |No| | | | |
| | |6|Cash Trading| | | | | | | | |TRAS| | |No| | | | |
| | |6|Settlement| | | | | | | | |SACC| | |No| | | | |
| | |6|Current| | | | | | | | |CACC| | |No| | | | |
| | |6|Savings| | | | | | | | |SVGS| | |No| | | | |
| | |6|Over Night Deposit| | | | | | | | |ONDP| | |No| | | | |
| | |6|Marginal Lending| | | | | | | | |MGLD| | |No| | | | |
| | |6|Non Resident External| | | | | | | | |NREX| | |No| | | | |
| | |6|Money Market| | | | | | | | |MOMA| | |No| | | | |
| | |6|Loan| | | | | | | | |LOAN| | |No| | | | |
| | |6|Salary| | | | | | | | |SLRY| | |No| | | | |
| | |6|Overdraft| | | | | | | | |ODFT| | |No| | | | |
| |1.1.1 0|5|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |1.1.1 1|3|Currency| | | | | |<Ccy>| |[0..1]|text [A-Z]{3,3}| | |No| | | | |
| |1.1.1 2|3|Name| | | | | |<Nm>| |[0..1]|text{1,70}| | |No| | | | |
| |2.26|2|Charges Account Agent| | | | | |<ChrgsAcctAgt>| |[0..1]| | |X|No| | | | |
| |2.27|2|Credit Transfer Transaction Information| | | | | |<CdtTrfTxInf>| |[1..*]| | | |Si| |Tag de inicio de agrupación de contenido| | |
| |2.28|3|Payment Identification| | | | | |<PmtId>| |[1..1]| | | |Si| |Tag de inicio de agrupación de contenido| | |
| |2.29|4|Instruction Identification| | | | | |<InstrId>| |[0..1]|text{1,35}| | |Si|Alfanumérico|Referencia del lote| | |
| |2.30|4|End To End Identification| | | | | |<EndToEndId>| |[1..1]|text{1,35}| |21|Si|Alfanumérico|Referencia del pago| | |
| |2.31|3|Payment Type Information| | | | | |<PmtTpInf>| |[0..1]| | | |No| | | | |
| |2.32|4|Instruction Priority| | | | | |<InstrPrty>| |[0..1]|text| | |No| | | | |
| | |5|High| | | | | | | | |HIGH| | |No| | | | |
| | |5|Normal| | | | | | | | |NORM| | |No| | | | |
| |2.33|4|Service Level| | | | | |<SvcLvl>| |[0..1]|Choice| | |No| | | | |
| |2.34|5|Code| | | | | |<Cd>| |[1..1]|text{1,4}| | |No| | | | |
| |2.35|5|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |2.36|4|Local Instrument| | | | | |<LclInstrm>| |[0..1]|Choice| |[1..1]|No| | | | |
| |2.37|5|Code| | | | | |<Cd>| |[1..1]|text{1,35}| | |No| | | | |
| |2.38|5|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |2.39|4|Category Purpose| | | | | |<CtgyPurp>| |[0..1]|Choice| | |No| | | | |
| |2.40|5|Code| | | | | |<Cd>| |[1..1]|text{1,4}| | |No| | | | |
| |2.41|5|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |2.42|3|Amount| | | | | |<Amt>| |[1..1]|Choice| | |Si| |Tag de inicio de agrupación de contenido| | |
| |2.43|4|Instructed Amount| | | | | |<InstdAmt>| |[1..1]|0 <= decimal td = 18 fd = 5| |15 Incuyendo decimales, no cuenta el separador decimal|Si|Numérico|Valor del pago, separador de decimales punto| | |
| | |5|Xml Attribute Currency| | | | | |<Ccy>| | |text [A-Z]{3,3}| | |No| | | | |
| |2.44|4|Equivalent Amount| | | | | |<EqvtAmt>| |[1..1]| | | |No| | | | |
| |2.45|5|Amount| | | | | |<Amt>| |[1..1]|0 <= decimal td = 18 fd = 5| | |No| | | | |
| | |6|Xml Attribute Currency| | | | | |<Ccy>| | |text [A-Z]{3,3}| | |No| | | | |
| |2.46|5|Currency Of Transfer| | | | | |<CcyOfTrf>| |[1..1]|text [A-Z]{3,3}| | |No| | | | |
| |2.47|3|Exchange Rate Information| | | | | |<XchgRateInf>| |[0..1]| | | |No| | | | |
| |2.48|4|Exchange Rate| | | | | |<XchgRate>| |[0..1]|decimal td = 11 fd = 10| | |No| | | | |
| |2.49|4|Rate Type| | | | | |<RateTp>| |[0..1]|text| | |No| | | | |
| | |5|Spot| | | | | | | | |SPOT| | |No| | | | |
| | |5|Sale| | | | | | | | |SALE| | |No| | | | |
| | |5|Agreed| | | | | | | | |AGRD| | |No| | | | |
| |2.50|4|Contract Identification| | | | | |<CtrctId>| |[0..1]|text{1,35}| | |No| | | | |
| |2.51|3|Charge Bearer| | | | | |<ChrgBr>| |[0..1]|text| | |No| | | | |
| | |4|Borne By Debtor| | | | | | | | |DEBT| | |No| | | | |
| | |4|Borne By Creditor| | | | | | | | |CRED| | |No| | | | |
| | |4|Shared| | | | | | | | |SHAR| | |No| | | | |
| | |4|Following Service Level| | | | | | | | |SLEV| | |No| | | | |
| |2.52|3|Cheque Instruction| | | | | |<ChqInstr>| |[0..1]| | | |No| | | | |
| |2.53|4|Cheque Type| | | | | |<ChqTp>| |[0..1]|text| | |No| | | | |
| | |5|Customer Cheque| | | | | | | | |CCHQ| | |No| | | | |
| | |5|Certified Customer Cheque| | | | | | | | |CCCH| | |No| | | | |
| | |5|Bank Cheque| | | | | | | | |BCHQ| | |No| | | | |
| | |5|Draft| | | | | | | | |DRFT| | |No| | | | |
| | |5|Electronic Draft| | | | | | | | |ELDR| | |No| | | | |
| |2.54|4|Cheque Number| | | | | |<ChqNb>| |[0..1]|text{1,35}| | |No| | | | |
| |2.55|4|Cheque From| | | | | |<ChqFr>| |[0..1]| | | |No| | | | |
| |2.56|5|Name| | | | | |<Nm>| |[1..1]|text{1,140}| | |No| | | | |
| |2.57|5|Address| | | | | |<Adr>| |[1..1]| | | |No| | | | |
| |10.1. 0|6|Address Type| | | | | |<AdrTp>| |[0..1]|text| | |No| | | | |
| | |7|Postal| | | | | | | | |ADDR| | |No| | | | |
| | |7|PO Box| | | | | | | | |PBOX| | |No| | | | |
| | |7|Residential| | | | | | | | |HOME| | |No| | | | |
| | |7|Business| | | | | | | | |BIZZ| | |No| | | | |
| | |7|Mail To| | | | | | | | |MLTO| | |No| | | | |
| | |7|Delivery To| | | | | | | | |DLVY| | |No| | | | |
| |10.1. 1|6|Department| | | | | |<Dept>| |[0..1]|text{1,70}| | |No| | | | |
| |10.1. 2|6|Sub Department| | | | | |<SubDept>| |[0..1]|text{1,70}| | |No| | | | |
| |10.1. 3|6|Street Name| | | | | |<StrtNm>| |[0..1]|text{1,70}| | |No| | | | |
| |10.1. 4|6|Building Number| | | | | |<BldgNb>| |[0..1]|text{1,16}| | |No| | | | |
| |10.1. 5|6|Post Code| | | | | |<PstCd>| |[0..1]|text{1,16}| | |No| | | | |
| |10.1. 6|6|Town Name| | | | | |<TwnNm>| |[0..1]|text{1,35}| | |No| | | | |
| |10.1. 7|6|Country Sub Division| | | | | |<CtrySubDvsn>| |[0..1]|text{1,35}| | |No| | | | |
| |10.1. 8|6|Country| | | | | |<Ctry>| |[0..1]|text [A-Z]{2,2}| | |No| | | | |
| |10.1. 9|6|Address Line| | | | | |<AdrLine>| |[0..7]|text{1,70}| | |No| | | | |
| |2.58|4|Delivery Method| | | | | |<DlvryMtd>| |[0..1]|Choice| | |No| | | | |
| |2.59|5|Code| | | | | |<Cd>| |[1..1]|text| | |No| | | | |
| | |6|Mail To Debtor| | | | | | | | |MLDB| | |No| | | | |
| | |6|Mail To Creditor| | | | | | | | |MLCD| | |No| | | | |
| | |6|Mail To Final Agent| | | | | | | | |MLFA| | |No| | | | |
| | |6|Courier To Debtor| | | | | | | | |CRDB| | |No| | | | |
| | |6|Courier To Creditor| | | | | | | | |CRCD| | |No| | | | |
| | |6|Courier To Final Agent| | | | | | | | |CRFA| | |No| | | | |
| | |6|Pick Up By Debtor| | | | | | | | |PUDB| | |No| | | | |
| | |6|Pick Up By Creditor| | | | | | | | |PUCD| | |No| | | | |
| | |6|Pick Up By Final Agent| | | | | | | | |PUFA| | |No| | | | |
| | |6|Registered Mail To Debtor| | | | | | | | |RGDB| | |No| | | | |
| | |6|Registered Mail To Creditor| | | | | | | | |RGCD| | |No| | | | |
| | |6|Registered Mail To Final Agent| | | | | | | | |RGFA| | |No| | | | |
| |2.60|5|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |2.61|4|Deliver To| | | | | |<DlvrTo>| |[0..1]| | | |No| | | | |
| |2.62|5|Name| | | | | |<Nm>| |[1..1]|text{1,140}| | |No| | | | |
| |2.63|5|Address| | | | | |<Adr>| |[1..1]| | | |No| | | | |
| |10.1. 0|6|Address Type| | | | | |<AdrTp>| |[0..1]|text| |X|No| | | | |
| |10.1. 1|6|Department| | | | | |<Dept>| |[0..1]|text{1,70}| | |No| | | | |
| |10.1. 2|6|Sub Department| | | | | |<SubDept>| |[0..1]|text{1,70}| | |No| | | | |
| |10.1. 3|6|Street Name| | | | | |<StrtNm>| |[0..1]|text{1,70}| | |No| | | | |
| |10.1. 4|6|Building Number| | | | | |<BldgNb>| |[0..1]|text{1,16}| | |No| | | | |
| |10.1. 5|6|Post Code| | | | | |<PstCd>| |[0..1]|text{1,16}| | |No| | | | |
| |10.1. 6|6|Town Name| | | | | |<TwnNm>| |[0..1]|text{1,35}| | |No| | | | |
| |10.1. 7|6|Country Sub Division| | | | | |<CtrySubDvsn>| |[0..1]|text{1,35}| | |No| | | | |
| |10.1. 8|6|Country| | | | | |<Ctry>| |[0..1]|text [A-Z]{2,2}| | |No| | | | |
| |10.1. 9|6|Address Line| | | | | |<AdrLine>| |[0..7]|text{1,70}| | |No| | | | |
| |2.64|4|Instruction Priority| | | | | |<InstrPrty>| |[0..1]|text| | |No| | | | |
| | |5|High| | | | | | | | |HIGH| | |No| | | | |
| | |5|Normal| | | | | | | | |NORM| | |No| | | | |
| |2.65|4|Cheque Maturity Date| | | | | |<ChqMtrtyDt>| |[0..1]|date| | |No| | | | |
| |2.66|4|Forms Code| | | | | |<FrmsCd>| |[0..1]|text{1,35}| | |No| | | | |
| |2.67|4|Memo Field| | | | | |<MemoFld>| |[0..2]|text{1,35}| | |No| | | | |
| |2.68|4|Regional Clearing Zone| | | | | |<RgnlClrZone>| |[0..1]|text{1,35}| | |No| | | | |
| |2.69|4|Print Location| | | | | |<PrtLctn>| |[0..1]|text{1,35}| | |No| | | | |
| |2.70|3|Ultimate Debtor| | | | | |<UltmtDbtr>| |[0..1]| | | |No| | | | |
| | |4|Name| | | | | |<Nm>| |[0..1]|text{1,140}| |[1..1]|No| | | | |
| |9.1.1|4|Postal Address| | | | | |<PstlAdr>| |[0..1]| | | |No| | | | |
| |9.1.2|5|Address Type| | | | | |<AdrTp>| |[0..1]|text| |X|No| | | | |
| |9.1.3|5|Department| | | | | |<Dept>| |[0..1]|text{1,70}| | |No| | | | |
| |9.1.4|5|Sub Department| | | | | |<SubDept>| |[0..1]|text{1,70}| | |No| | | | |
| |9.1.5|5|Street Name| | | | | |<StrtNm>| |[0..1]|text{1,70}| | |No| | | | |
| |9.1.6|5|Building Number| | | | | |<BldgNb>| |[0..1]|text{1,16}| | |No| | | | |
| |9.1.7|5|Post Code| | | | | |<PstCd>| |[0..1]|text{1,16}| | |No| | | | |
| |9.1.8|5|Town Name| | | | | |<TwnNm>| |[0..1]|text{1,35}| | |No| | | | |
| |9.1.9|5|Country Sub Division| | | | | |<CtrySubDvsn>| |[0..1]|text{1,35}| | |No| | | | |
| |9.1.1 0|5|Country| | | | | |<Ctry>| |[0..1]|text [A-Z]{2,2}| |[1..1]|No| | | | |
| |9.1.1 1|5|Address Line| | | | | |<AdrLine>| |[0..7]|text{1,70}| | |No| | | | |
| |9.1.1 2|4|Identification| | | | | |<Id>| |[0..1]|Choice| | |No| | | | |
| |9.1.1 3|5|Organisation Identification| | | | | |<OrgId>| |[1..1]| | | |No| | | | |
| |9.1.1 4|6|BIC Or BEI| | | | | |<BICOrBEI>| |[0..1]|text [A-Z]{6,6}[A-Z2- 9][A-NP-Z0- 9]([A-Z0- 9]{3,3}){0,1}| | |No| | | | |
| |9.1.1 5|6|Other| | | | | |<Othr>| |[0..*]| | | |No| | | | |
| |9.1.1 6|7|Identification| | | | | |<Id>| |[1..1]|text{1,35}| | |No| | | | |
| |9.1.1 7|7|Scheme Name| | | | | |<SchmeNm>| |[0..1]|Choice| | |No| | | | |
| |9.1.1 8|8|Code| | | | | |<Cd>| |[1..1]|text{1,4}| | |No| | | | |
| |9.1.1 9|8|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |9.1.2 0|7|Issuer| | | | | |<Issr>| |[0..1]|text{1,35}| |X|No| | | | |
| |9.1.2 1|5|Private Identification| | | | | |<PrvtId>| |[1..1]| | | |No| | | | |
| |9.1.2 2|6|Date And Place Of Birth| | | | | |<DtAndPlcOfBirth >| |[0..1]| | |X|No| | | | |
| |9.1.2 7|6|Other| | | | | |<Othr>| |[0..*]| | | |No| | | | |
| |9.1.2 8|7|Identification| | | | | |<Id>| |[1..1]|text{1,35}| | |No| | | | |
| |9.1.2 9|7|Scheme Name| | | | | |<SchmeNm>| |[0..1]|Choice| | |No| | | | |
| |9.1.3 0|8|Code| | | | | |<Cd>| |[1..1]|text{1,4}| | |No| | | | |
| |9.1.3 1|8|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| |X|No| | | | |
| |9.1.3 2|7|Issuer| | | | | |<Issr>| |[0..1]|text{1,35}| |X|No| | | | |
| |9.1.3 3|4|Country Of Residence| | | | | |<CtryOfRes>| |[0..1]|text [A-Z]{2,2}| | |No| | | | |
| |9.1.3 4|4|Contact Details| | | | | |<CtctDtls>| |[0..1]| | | |No| | | | |
| |9.1.3 5|5|Name Prefix| | | | | |<NmPrfx>| |[0..1]|text| | |No| | | | |
| | |6|Doctor| | | | | | | | |DOCT| | |No| | | | |
| | |6|Mister| | | | | | | | |MIST| | |No| | | | |
| | |6|Miss| | | | | | | | |MISS| | |No| | | | |
| | |6|Madam| | | | | | | | |MADM| | |No| | | | |
| |9.1.3 6|5|Name| | | | | |<Nm>| |[0..1]|text{1,140}| | |No| | | | |
| |9.1.3 7|5|Phone Number| | | | | |<PhneNb>| |[0..1]|text \+[0-9]{1,3}-[0- 9()+\-]{1,30}| | |No| | | | |
| |9.1.3 8|5|Mobile Number| | | | | |<MobNb>| |[0..1]|text \+[0-9]{1,3}-[0- 9()+\-]{1,30}| | |No| | | | |
| |9.1.3 9|5|Fax Number| | | | | |<FaxNb>| |[0..1]|text \+[0-9]{1,3}-[0- 9()+\-]{1,30}| | |No| | | | |
| |9.1.4 0|5|Email Address| | | | | |<EmailAdr>| |[0..1]|text{1,2048}| | |No| | | | |
| |9.1.4 1|5|Other| | | | | |<Othr>| |[0..1]|text{1,35}| | |No| | | | |
| |2.71|3|Intermediary Agent 1| | | | | |<IntrmyAgt1>| |[0..1]| | | |No| | | | |
| | |4|Financial Institution Identification| | | | | |<FinInstnId>| |[1..1]| | | |No| | | | |
| |6.1.1|5|BIC| | | | | |<BIC>| |[0..1]|text [A-Z]{6,6}[A-Z2- 9][A-NP-Z0- 9]([A-Z0- 9]{3,3}){0,1}| |FV|No| | | | |
| |6.1.2|5|Clearing System Member Identification| | | | | |<ClrSysMmbId>| |[0..1]| | | |No| | | | |
| |6.1.3|6|Clearing System Identification| | | | | |<ClrSysId>| |[0..1]|Choice| | |No| | | | |
| |6.1.4|7|Code| | | | | |<Cd>| |[1..1]|text{1,5}| | |No| | | | |
| |6.1.5|7|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |6.1.6|6|Member Identification| | | | | |<MmbId>| |[1..1]|text{1,35}| | |No| | | | |
| |6.1.7|5|Name| | | | | |<Nm>| |[0..1]|text{1,140}| |X|No| | | | |
| |6.1.8|5|Postal Address| | | | | |<PstlAdr>| |[0..1]| | |[1..1]|No| | | | |
| |6.1.9|6|Address Type| | | | | |<AdrTp>| |[0..1]|text| |X|No| | | | |
| |6.1.1 0|6|Department| | | | | |<Dept>| |[0..1]|text{1,70}| |X|No| | | | |
| |6.1.1 1|6|Sub Department| | | | | |<SubDept>| |[0..1]|text{1,70}| |X|No| | | | |
| |6.1.1 2|6|Street Name| | | | | |<StrtNm>| |[0..1]|text{1,70}| |X|No| | | | |
| |6.1.1 3|6|Building Number| | | | | |<BldgNb>| |[0..1]|text{1,16}| |X|No| | | | |
| |6.1.1 4|6|Post Code| | | | | |<PstCd>| |[0..1]|text{1,16}| |X|No| | | | |
| |6.1.1 5|6|Town Name| | | | | |<TwnNm>| |[0..1]|text{1,35}| |X|No| | | | |
| |6.1.1 6|6|Country Sub Division| | | | | |<CtrySubDvsn>| |[0..1]|text{1,35}| |X|No| | | | |
| |6.1.1 7|6|Country| | | | | |<Ctry>| |[0..1]|text [A-Z]{2,2}| |[1..1]|No| | | | |
| |6.1.1 8|6|Address Line| | | | | |<AdrLine>| |[0..7]|text{1,70}| |X|No| | | | |
| |6.1.1 9|5|Other| | | | | |<Othr>| |[0..1]| | |X|No| | | | |
| |6.1.2 5|4|Branch Identification| | | | | |<BrnchId>| |[0..1]| | | |No| | | | |
| |6.1.2 6|5|Identification| | | | | |<Id>| |[0..1]|text{1,35}| | |No| | | | |
| |6.1.2 7|5|Name| | | | | |<Nm>| |[0..1]|text{1,140}| |X|No| | | | |
| |6.1.2 8|5|Postal Address| | | | | |<PstlAdr>| |[0..1]| | |X|No| | | | |
| |2.72|3|Intermediary Agent 1 Account| | | | | |<IntrmyAgt1Acct>| |[0..1]| | |X|No| | | | |
| |2.73|3|Intermediary Agent 2| | | | | |<IntrmyAgt2>| |[0..1]| | |X|No| | | | |
| |2.74|3|Intermediary Agent 2 Account| | | | | |<IntrmyAgt2Acct>| |[0..1]| | |X|No| | | | |
| |2.75|3|Intermediary Agent 3| | | | | |<IntrmyAgt3>| |[0..1]| | |X|No| | | | |
| |2.76|3|Intermediary Agent 3 Account| | | | | |<IntrmyAgt3Acct>| |[0..1]| | |X|No| | | | |
| |2.77|3|Creditor Agent| | | | | |<CdtrAgt>| |[0..1]| | |[1..1]|Si| |Tag de inicio de agrupación de contenido| | |
| | |4|Financial Institution Identification| | | | | |<FinInstnId>| |[1..1]| | |5|Si, en transferencias cuando no sea enviado el código Swift del banco destino|Alfanumérico|Banco del beneficiario (El cliente puede enviar el código Swift destino o el código ACH destino). Este campo aplica cuando el cliente envía el código ACH destino <FinInstnId>     <ClrSysMmbId>        <MmbId>002</MmbId>| | |
| |6.1.1|5|BIC| | | | | |<BIC>| |[0..1]|text [A-Z]{6,6}[A-Z2- 9][A-NP-Z0- 9]([A-Z0- 9]{3,3}){0,1}| |12|NO| | | | |
| |6.1.2|5|Clearing System Member Identification| | | | | |<ClrSysMmbId>| |[0..1]| | | |No| | | | |
| |6.1.3|6|Clearing System Identification| | | | | |<ClrSysId>| |[0..1]|Choice| | |No| | | | |
| |6.1.4|7|Code| | | | | |<Cd>| |[1..1]|text{1,5}| | |No| | | | |
| |6.1.5|7|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |6.1.6|6|Member Identification| | | | | |<MmbId>| |[1..1]|text{1,35}| | |No| | | | |
| |6.1.7|5|Name| | | | | |<Nm>| |[0..1]|text{1,140}| | |No| | | | |
| |6.1.8|5|Postal Address| | | | | |<PstlAdr>| |[0..1]| | |[1..1]|No| | | | |
| |6.1.9|6|Address Type| | | | | |<AdrTp>| |[0..1]|text| |X|No| | | | |
| |6.1.1 0|6|Department| | | | | |<Dept>| |[0..1]|text{1,70}| |X|No| | | | |
| |6.1.1 1|6|Sub Department| | | | | |<SubDept>| |[0..1]|text{1,70}| |X|No| | | | |
| |6.1.1 2|6|Street Name| | | | | |<StrtNm>| |[0..1]|text{1,70}| |X|No| | | | |
| |6.1.1 3|6|Building Number| | | | | |<BldgNb>| |[0..1]|text{1,16}| |X|No| | | | |
| |6.1.1 4|6|Post Code| | | | | |<PstCd>| |[0..1]|text{1,16}| |X|No| | | | |
| |6.1.1 5|6|Town Name| | | | | |<TwnNm>| |[0..1]|text{1,35}| |X|No| | | | |
| |6.1.1 6|6|Country Sub Division| | | | | |<CtrySubDvsn>| |[0..1]|text{1,35}| |X|No| | | | |
| |6.1.1 7|6|Country| | | | | |<Ctry>| |[0..1]|text [A-Z]{2,2}| |[1..1]|No| | | | |
| |6.1.1 8|6|Address Line| | | | | |<AdrLine>| |[0..7]|text{1,70}| |X|No| | | | |
| |6.1.1 9|5|Other| | | | | |<Othr>| |[0..1]| | |X|No| | | | |
| |6.1.2 5|4|Branch Identification| | | | | |<BrnchId>| |[0..1]| | | |No| | | | |
| |6.1.2 6|5|Identification| | | | | |<Id>| |[0..1]|text{1,35}| | |No| | | | |
| |6.1.2 7|5|Name| | | | | |<Nm>| |[0..1]|text{1,140}| |X|No| | | | |
| |6.1.2 8|5|Postal Address| | | | | |<PstlAdr>| |[0..1]| | |X|No| | | | |
| |2.78|3|Creditor Agent Account| | | | | |<CdtrAgtAcct>| |[0..1]| | | |No| | | | |
| | |4|Identification| | | | | |<Id>| |[1..1]|Choice| | |No| | | | |
| |1.1.1|5|IBAN| | | | | |<IBAN>| |[1..1]|text [A-Z]{2,2}[0- 9]{2,2}[a-zA-Z0- 9]{1,30}| |X|No| | | | |
| |1.1.2|5|Other| | | | | |<Othr>| |[1..1]| | | |No| | | | |
| |1.1.3|6|Identification| | | | | |<Id>| |[1..1]|text{1,34}| | |No| | | | |
| |1.1.4|6|Scheme Name| | | | | |<SchmeNm>| |[0..1]|Choice| |X|No| | | | |
| |1.1.7|6|Issuer| | | | | |<Issr>| |[0..1]|text{1,35}| |X|No| | | | |
| |1.1.8|4|Type| | | | | |<Tp>| |[0..1]| | |X|No| | | | |
| |1.1.1 1|4|Currency| | | | | |<Ccy>| |[0..1]|text [A-Z]{3,3}| |X|No| | | | |
| |1.1.1 2|4|Name| | | | | |<Nm>| |[0..1]|text{1,70}| |X|No| | | | |
| |2.79|3|Creditor| | | | | |<Cdtr>| |[0..1]| | |[1..1]|No| | | | |
| | |4|Name| | | | | |<Nm>| |[0..1]|text{1,140}| |[1..1]|No| | | | |
| |9.1.1|4|Postal Address| | | | | |<PstlAdr>| |[0..1]| | |[1..1]|No| | | | |
| |9.1.2|5|Address Type| | | | | |<AdrTp>| |[0..1]|text| |X|No| | | | |
| |9.1.3|5|Department| | | | | |<Dept>| |[0..1]|text{1,70}| | |No| | | | |
| |9.1.4|5|Sub Department| | | | | |<SubDept>| |[0..1]|text{1,70}| | |No| | | | |
| |9.1.5|5|Street Name| | | | | |<StrtNm>| |[0..1]|text{1,70}| | |No| | | | |
| |9.1.6|5|Building Number| | | | | |<BldgNb>| |[0..1]|text{1,16}| | |No| | | | |
| |9.1.7|5|Post Code| | | | | |<PstCd>| |[0..1]|text{1,16}| | |No| | | | |
| |9.1.8|5|Town Name| | | | | |<TwnNm>| |[0..1]|text{1,35}| | |No| | | | |
| |9.1.9|5|Country Sub Division| | | | | |<CtrySubDvsn>| |[0..1]|text{1,35}| | |No| | | | |
| |9.1.1 0|5|Country| | | | | |<Ctry>| |[0..1]|text [A-Z]{2,2}| |[1..1]|No| | | | |
| |9.1.1 1|5|Address Line| | | | | |<AdrLine>| |[0..7]|text{1,70}| | |No| | | | |
| |9.1.1 2|4|Identification| | | | | |<Id>| |[0..1]|Choice| | |No| | | | |
| |9.1.1 3|5|Organisation Identification| | | | | |<OrgId>| |[1..1]| | | |No| | | | |
| |9.1.1 4|6|BIC Or BEI| | | | | |<BICOrBEI>| |[0..1]|text [A-Z]{6,6}[A-Z2- 9][A-NP-Z0- 9]([A-Z0- 9]{3,3}){0,1}| | |No| | | | |
| |9.1.1 5|6|Other| | | | | |<Othr>| |[0..*]| | | |No| | | | |
| |9.1.1 6|7|Identification| | | | | |<Id>| |[1..1]|text{1,35}| | |No| | | | |
| |9.1.1 7|7|Scheme Name| | | | | |<SchmeNm>| |[0..1]|Choice| | |No| | | | |
| |9.1.1 8|8|Code| | | | | |<Cd>| |[1..1]|text{1,4}| | |No| | | | |
| |9.1.1 9|8|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |9.1.2 0|7|Issuer| | | | | |<Issr>| |[0..1]|text{1,35}| | |No| | | | |
| |9.1.2 1|5|Private Identification| | | | | |<PrvtId>| |[1..1]| | | |No| | | | |
| |9.1.2 2|6|Date And Place Of Birth| | | | | |<DtAndPlcOfBirth >| |[0..1]| | | |No| | | | |
| |9.1.2 3|7|Birth Date| | | | | |<BirthDt>| |[1..1]|date| | |No| | | | |
| |9.1.2 4|7|Province Of Birth| | | | | |<PrvcOfBirth>| |[0..1]|text{1,35}| | |No| | | | |
| |9.1.2 5|7|City Of Birth| | | | | |<CityOfBirth>| |[1..1]|text{1,35}| | |No| | | | |
| |9.1.2 6|7|Country Of Birth| | | | | |<CtryOfBirth>| |[1..1]|text [A-Z]{2,2}| | |No| | | | |
| |9.1.2 7|6|Other| | | | | |<Othr>| |[0..*]| | | |No| | | | |
| |9.1.2 8|7|Identification| | | | | |<Id>| |[1..1]|text{1,35}| | |No| | | | |
| |9.1.2 9|7|Scheme Name| | | | | |<SchmeNm>| |[0..1]|Choice| | |No| | | | |
| |9.1.3 0|8|Code| | | | | |<Cd>| |[1..1]|text{1,4}| | |No| | | | |
| |9.1.3 1|8|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |9.1.3 2|7|Issuer| | | | | |<Issr>| |[0..1]|text{1,35}| | |No| | | | |
| |9.1.3 3|4|Country Of Residence| | | | | |<CtryOfRes>| |[0..1]|text [A-Z]{2,2}| | |No| | | | |
| |9.1.3 4|4|Contact Details| | | | | |<CtctDtls>| |[0..1]| | | |No| | | | |
| |9.1.3 5|5|Name Prefix| | | | | |<NmPrfx>| |[0..1]|text| |X|No| | | | |
| |9.1.3 6|5|Name| | | | | |<Nm>| |[0..1]|text{1,140}| | |No| | | | |
| |9.1.3 7|5|Phone Number| | | | | |<PhneNb>| |[0..1]|text \+[0-9]{1,3}-[0- 9()+\-]{1,30}| |X|No| | | | |
| |9.1.3 8|5|Mobile Number| | | | | |<MobNb>| |[0..1]|text \+[0-9]{1,3}-[0- 9()+\-]{1,30}| | |No| | | | |
| |9.1.3 9|5|Fax Number| | | | | |<FaxNb>| |[0..1]|text \+[0-9]{1,3}-[0- 9()+\-]{1,30}| |X|No| | | | |
| |9.1.4 0|5|Email Address| | | | | |<EmailAdr>| |[0..1]|text{1,2048}| | |No| | | | |
| |9.1.4 1|5|Other| | | | | |<Othr>| |[0..1]|text{1,35}| |X|No| | | | |
| |2.80|3|Creditor Account| | | | | |<CdtrAcct>| |[0..1]| | |[1..1]|Si| |Tag de inicio de agrupación de contenido| | |
| | |4|Identification| | | | | |<Id>| |[1..1]|Choice| |17|Si, en transferencias|Numérico|Número de Cuenta del beneficiario del pago <CdtrAcct>   <Id>     <Othr>         <Id>42089330739</Id>| | |
| | |4|Identification| | | | | |<Id>| |[1..1]|Choice| |5|Si, en transferencias|Alfanumérico|Tipo de Transacción para abono a cuenta <CdtrAcct>    <Tp>      <Cd>SVGS</Cd>   CACC (Cuenta Corriente) SVGS ( Cuenta de ahorros)| | |
| |1.1.1|5|IBAN| | | | | |<IBAN>| |[1..1]|text [A-Z]{2,2}[0- 9]{2,2}[a-zA-Z0- 9]{1,30}| | |No| | | | |
| |1.1.2|5|Other| | | | | |<Othr>| |[1..1]| | | |No| | | | |
| |1.1.3|6|Identification| | | | | |<Id>| |[1..1]|text{1,34}| | |No| | | | |
| |1.1.4|6|Scheme Name| | | | | |<SchmeNm>| |[0..1]|Choice| | |No| | | | |
| |1.1.5|7|Code| | | | | |<Cd>| |[1..1]|text{1,4}| | |No| | | | |
| |1.1.6|7|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |1.1.7|6|Issuer| | | | | |<Issr>| |[0..1]|text{1,35}| | |No| | | | |
| |1.1.8|4|Type| | | | | |<Tp>| |[0..1]| | | |No| | | | |
| | |5|[XOR]| | | | | | | | |Choice| | |No| | | | |
| |1.1.9|6|Code| | | | | |<Cd>| |[1..1]|text| | |No| | | | |
| | |7|Cash Payment| | | | | | | | |CASH| | |No| | | | |
| | |7|Charges| | | | | | | | |CHAR| |X|No| | | | |
| | |7|Commission| | | | | | | | |COMM| | |No| | | | |
| | |7|Tax| | | | | | | | |TAXE| |X|No| | | | |
| | |7|Cash Income| | | | | | | | |CISH| | |No| | | | |
| | |7|Cash Trading| | | | | | | | |TRAS| | |No| | | | |
| | |7|Settlement| | | | | | | | |SACC| | |No| | | | |
| | |7|Current| | | | | | | | |CACC| | |No| | | | |
| | |7|Savings| | | | | | | | |SVGS| | |No| | | | |
| | |7|Over Night Deposit| | | | | | | | |ONDP| | |No| | | | |
| | |7|Marginal Lending| | | | | | | | |MGLD| |X|No| | | | |
| | |7|Non Resident External| | | | | | | | |NREX| |X|No| | | | |
| | |7|Money Market| | | | | | | | |MOMA| | |No| | | | |
| | |7|Loan| | | | | | | | |LOAN| | |No| | | | |
| | |7|Salary| | | | | | | | |SLRY| |X|No| | | | |
| | |7|Overdraft| | | | | | | | |ODFT| | |No| | | | |
| |1.1.1 0|6|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |1.1.1 1|4|Currency| | | | | |<Ccy>| |[0..1]|text [A-Z]{3,3}| | |No| | | | |
| |1.1.1 2|4|Name| | | | | |<Nm>| |[0..1]|text{1,70}| | |No| | | | |
| |2.81|3|Ultimate Creditor| | | | | |<UltmtCdtr>| |[0..1]| | | |No| | | | |
| | |4|Name| | | | | |<Nm>| |[0..1]|text{1,140}| |[1..1]|No| | | | |
| |9.1.1|4|Postal Address| | | | | |<PstlAdr>| |[0..1]| | | |No| | | | |
| |9.1.2|5|Address Type| | | | | |<AdrTp>| |[0..1]|text| |X|No| | | | |
| |9.1.3|5|Department| | | | | |<Dept>| |[0..1]|text{1,70}| | |No| | | | |
| |9.1.4|5|Sub Department| | | | | |<SubDept>| |[0..1]|text{1,70}| | |No| | | | |
| |9.1.5|5|Street Name| | | | | |<StrtNm>| |[0..1]|text{1,70}| | |No| | | | |
| |9.1.6|5|Building Number| | | | | |<BldgNb>| |[0..1]|text{1,16}| | |No| | | | |
| |9.1.7|5|Post Code| | | | | |<PstCd>| |[0..1]|text{1,16}| | |No| | | | |
| |9.1.8|5|Town Name| | | | | |<TwnNm>| |[0..1]|text{1,35}| | |No| | | | |
| |9.1.9|5|Country Sub Division| | | | | |<CtrySubDvsn>| |[0..1]|text{1,35}| | |No| | | | |
| |9.1.1 0|5|Country| | | | | |<Ctry>| |[0..1]|text [A-Z]{2,2}| |[1..1]|No| | | | |
| |9.1.1 1|5|Address Line| | | | | |<AdrLine>| |[0..7]|text{1,70}| | |No| | | | |
| |9.1.1 2|4|Identification| | | | | |<Id>| |[0..1]|Choice| | |No| | | | |
| |9.1.1 3|5|Organisation Identification| | | | | |<OrgId>| |[1..1]| | | |No| | | | |
| |9.1.1 4|6|BIC Or BEI| | | | | |<BICOrBEI>| |[0..1]|text [A-Z]{6,6}[A-Z2- 9][A-NP-Z0- 9]([A-Z0- 9]{3,3}){0,1}| | |No| | | | |
| |9.1.1 5|6|Other| | | | | |<Othr>| |[0..*]| | | |No| | | | |
| |9.1.1 6|7|Identification| | | | | |<Id>| |[1..1]|text{1,35}| | |No| | | | |
| |9.1.1 7|7|Scheme Name| | | | | |<SchmeNm>| |[0..1]|Choice| | |No| | | | |
| |9.1.1 8|8|Code| | | | | |<Cd>| |[1..1]|text{1,4}| | |No| | | | |
| |9.1.1 9|8|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |9.1.2 0|7|Issuer| | | | | |<Issr>| |[0..1]|text{1,35}| | |No| | | | |
| |9.1.2 1|5|Private Identification| | | | | |<PrvtId>| |[1..1]| | | |No| | | | |
| |9.1.2 2|6|Date And Place Of Birth| | | | | |<DtAndPlcOfBirth >| |[0..1]| | | |No| | | | |
| |9.1.2 3|7|Birth Date| | | | | |<BirthDt>| |[1..1]|date| | |No| | | | |
| |9.1.2 4|7|Province Of Birth| | | | | |<PrvcOfBirth>| |[0..1]|text{1,35}| | |No| | | | |
| |9.1.2 5|7|City Of Birth| | | | | |<CityOfBirth>| |[1..1]|text{1,35}| | |No| | | | |
| |9.1.2 6|7|Country Of Birth| | | | | |<CtryOfBirth>| |[1..1]|text [A-Z]{2,2}| | |No| | | | |
| |9.1.2 7|6|Other| | | | | |<Othr>| |[0..*]| | | |No| | | | |
| |9.1.2 8|7|Identification| | | | | |<Id>| |[1..1]|text{1,35}| | |No| | | | |
| |9.1.2 9|7|Scheme Name| | | | | |<SchmeNm>| |[0..1]|Choice| | |No| | | | |
| |9.1.3 0|8|Code| | | | | |<Cd>| |[1..1]|text{1,4}| | |No| | | | |
| |9.1.3 1|8|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |9.1.3 2|7|Issuer| | | | | |<Issr>| |[0..1]|text{1,35}| | |No| | | | |
| |9.1.3 3|4|Country Of Residence| | | | | |<CtryOfRes>| |[0..1]|text [A-Z]{2,2}| | |No| | | | |
| |9.1.3 4|4|Contact Details| | | | | |<CtctDtls>| |[0..1]| | | |No| | | | |
| |9.1.3 5|5|Name Prefix| | | | | |<NmPrfx>| |[0..1]|text| |X|No| | | | |
| |9.1.3 6|5|Name| | | | | |<Nm>| |[0..1]|text{1,140}| | |No| | | | |
| |9.1.3 7|5|Phone Number| | | | | |<PhneNb>| |[0..1]|text \+[0-9]{1,3}-[0- 9()+\-]{1,30}| |X|No| | | | |
| |9.1.3 8|5|Mobile Number| | | | | |<MobNb>| |[0..1]|text \+[0-9]{1,3}-[0- 9()+\-]{1,30}| | |No| | | | |
| |9.1.3 9|5|Fax Number| | | | | |<FaxNb>| |[0..1]|text \+[0-9]{1,3}-[0- 9()+\-]{1,30}| |X|No| | | | |
| |9.1.4 0|5|Email Address| | | | | |<EmailAdr>| |[0..1]|text{1,2048}| | |No| | | | |
| |9.1.4 1|5|Other| | | | | |<Othr>| |[0..1]|text{1,35}| |X|No| | | | |
| |2.82|3|Instruction For Creditor Agent| | | | | |<InstrForCdtrAgt>| |[0..*]| | | |No| | | | |
| |2.83|4|Code| | | | | |<Cd>| |[0..1]|text| | |No| | | | |
| | |5|Pay Creditor By Cheque| | | | | | | | |CHQB| | |No| | | | |
| | |5|Hold Cash For Creditor| | | | | | | | |HOLD| | |No| | | | |
| | |5|Phone Beneficiary| | | | | | | | |PHOB| | |No| | | | |
| | |5|Telecom| | | | | | | | |TELB| | |No| | | | |
| |2.84|4|Instruction Information| | | | | |<InstrInf>| |[0..1]|text{1,140}| |15|Si, en pagos por ventanilla|Numérico|Nit del autorizado| | |
| |2.85|3|Instruction For Debtor Agent| | | | | |<InstrForDbtrAgt>| |[0..1]|text{1,140}| | |No| | | | |
| |2.86|3|Purpose| | | | | |<Purp>| |[0..1]|Choice| | |No| | | | |
| |2.87|4|Code| | | | | |<Cd>| |[1..1]|text{1,4}| | |No| | | | |
| |2.88|4|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |2.89|3|Regulatory Reporting| | | | | |<RgltryRptg>| |[0..1 0]| | | |No| | | | |
| |11.1. 0|4|Debit Credit Reporting Indicator| | | | | |<DbtCdtRptgInd>| |[0..1]|text| | |No| | | | |
| | |5|Credit| | | | | | | | |CRED| | |No| | | | |
| | |5|Debit| | | | | | | | |DEBT| | |No| | | | |
| | |5|Both| | | | | | | | |BOTH| | |No| | | | |
| |11.1. 1|4|Authority| | | | | |<Authrty>| |[0..1]| | | |No| | | | |
| |11.1. 2|5|Name| | | | | |<Nm>| |[0..1]|text{1,140}| | |No| | | | |
| |11.1. 3|5|Country| | | | | |<Ctry>| |[0..1]|text [A-Z]{2,2}| | |No| | | | |
| |11.1. 4|4|Details| | | | | |<Dtls>| |[0..*]| | | |No| | | | |
| |11.1. 5|5|Type| | | | | |<Tp>| |[0..1]|text{1,35}| | |No| | | | |
| |11.1. 6|5|Date| | | | | |<Dt>| |[0..1]|date| | |No| | | | |
| |11.1. 7|5|Country| | | | | |<Ctry>| |[0..1]|text [A-Z]{2,2}| | |No| | | | |
| |11.1. 8|5|Code| | | | | |<Cd>| |[0..1]|text{1,10}| | |No| | | | |
| |11.1. 9|5|Amount| | | | | |<Amt>| |[0..1]|0 <= decimal td = 18 fd = 5| | |No| | | | |
| | |6|Xml Attribute Currency| | | | | |<Ccy>| | |text [A-Z]{3,3}| | |No| | | | |
| |11.1. 10|5|Information| | | | | |<Inf>| |[0..*]|text{1,35}| | |No| | | | |
| |2.90|3|Tax| | | | | |<Tax>| |[0..1]| | | |No| | | | |
| |13.1. 0|4|Creditor| | | | | |<Cdtr>| |[0..1]| | |30 (si supera 30 trunca)|Si|Alfanumérico|Nombre del Beneficiario <Cdtr>     <Nm>BENEFICIARY NAME 01</Nm>| | |
| |13.1. 0|4|Creditor| | | | | |<Cdtr>| |[0..1]| | |15|Si|Numérico|Número de Identificación del Beneficiario <Cdtr>    <Id>     <OrgId> (<prvtId>)       <Othr>         <Id>1036646980</Id>| | |
| |13.1. 0|4|Creditor| | | | | |<Cdtr>| |[0..1]| | |10|Si|Alfanumérico|Tipo de Identificación del Beneficiario <Id>  <OrgId> (<prvtId>)     <Othr>         <Id>1036646980</Id>         <Cd>TXID</Cd>   TXID: Nit RNID: Cédula Ciudadania FID: Cédula de Extranjería PSID: Pasaporte| | |
| |13.1. 1|5|Tax Identification| | | | | |<TaxId>| |[0..1]|text{1,35}| | |No| | | | |
| |13.1. 2|5|Registration Identification| | | | | |<RegnId>| |[0..1]|text{1,35}| | |No| | | | |
| |13.1. 3|5|Tax Type| | | | | |<TaxTp>| |[0..1]|text{1,35}| | |No| | | | |
| |13.1. 4|4|Debtor| | | | | |<Dbtr>| |[0..1]| | | |No| | | | |
| |13.1. 5|5|Tax Identification| | | | | |<TaxId>| |[0..1]|text{1,35}| | |No| | | | |
| |13.1. 6|5|Registration Identification| | | | | |<RegnId>| |[0..1]|text{1,35}| | |No| | | | |
| |13.1. 7|5|Tax Type| | | | | |<TaxTp>| |[0..1]|text{1,35}| | |No| | | | |
| |13.1. 8|5|Authorisation| | | | | |<Authstn>| |[0..1]| | | |No| | | | |
| |13.1. 9|6|Title| | | | | |<Titl>| |[0..1]|text{1,35}| | |No| | | | |
| |13.1. 10|6|Name| | | | | |<Nm>| |[0..1]|text{1,140}| | |No| | | | |
| |13.1. 11|4|Administration Zone| | | | | |<AdmstnZn>| |[0..1]|text{1,35}| | |No| | | | |
| |13.1. 12|4|Reference Number| | | | | |<RefNb>| |[0..1]|text{1,140}| | |No| | | | |
| |13.1. 13|4|Method| | | | | |<Mtd>| |[0..1]|text{1,35}| | |No| | | | |
| |13.1. 14|4|Total Taxable Base Amount| | | | | |<TtlTaxblBaseAm t>| |[0..1]|0 <= decimal td = 18 fd = 5| | |No| | | | |
| | |5|Xml Attribute Currency| | | | | |<Ccy>| | |text [A-Z]{3,3}| | |No| | | | |
| |13.1. 15|4|Total Tax Amount| | | | | |<TtlTaxAmt>| |[0..1]|0 <= decimal td = 18 fd = 5| | |No| | | | |
| | |5|Xml Attribute Currency| | | | | |<Ccy>| | |text [A-Z]{3,3}| | |No| | | | |
| |13.1. 16|4|Date| | | | | |<Dt>| |[0..1]|date| | |No| | | | |
| |13.1. 17|4|Sequence Number| | | | | |<SeqNb>| |[0..1]|decimal td = 18 fd = 0| | |No| | | | |
| |13.1. 18|4|Record| | | | | |<Rcrd>| |[0..*]| | | |No| | | | |
| |13.1. 19|5|Type| | | | | |<Tp>| |[0..1]|text{1,35}| | |No| | | | |
| |13.1. 20|5|Category| | | | | |<Ctgy>| |[0..1]|text{1,35}| | |No| | | | |
| |13.1. 21|5|Category Details| | | | | |<CtgyDtls>| |[0..1]|text{1,35}| | |No| | | | |
| |13.1. 22|5|Debtor Status| | | | | |<DbtrSts>| |[0..1]|text{1,35}| | |No| | | | |
| |13.1. 23|5|Certificate Identification| | | | | |<CertId>| |[0..1]|text{1,35}| | |No| | | | |
| |13.1. 24|5|Forms Code| | | | | |<FrmsCd>| |[0..1]|text{1,35}| | |No| | | | |
| |13.1. 25|5|Period| | | | | |<Prd>| |[0..1]| | | |No| | | | |
| |13.1. 26|6|Year| | | | | |<Yr>| |[0..1]|date| | |No| | | | |
| |13.1. 27|6|Type| | | | | |<Tp>| |[0..1]|text| | |No| | | | |
| | |7|First Month| | | | | | | | |MM01| | |No| | | | |
| | |7|Second Month| | | | | | | | |MM02| | |No| | | | |
| | |7|Third Month| | | | | | | | |MM03| | |No| | | | |
| | |7|Fourth Month| | | | | | | | |MM04| | |No| | | | |
| | |7|Fifth Month| | | | | | | | |MM05| | |No| | | | |
| | |7|Sixth Month| | | | | | | | |MM06| | |No| | | | |
| | |7|Seventh Month| | | | | | | | |MM07| | |No| | | | |
| | |7|Eighth Month| | | | | | | | |MM08| | |No| | | | |
| | |7|Ninth Month| | | | | | | | |MM09| | |No| | | | |
| | |7|Tenth Month| | | | | | | | |MM10| | |No| | | | |
| | |7|Eleventh Month| | | | | | | | |MM11| | |No| | | | |
| | |7|Twelfth Month| | | | | | | | |MM12| | |No| | | | |
| | |7|First Quarter| | | | | | | | |QTR1| | |No| | | | |
| | |7|Second Quarter| | | | | | | | |QTR2| | |No| | | | |
| | |7|Third Quarter| | | | | | | | |QTR3| | |No| | | | |
| | |7|Fourth Quarter| | | | | | | | |QTR4| | |No| | | | |
| | |7|First Half| | | | | | | | |HLF1| | |No| | | | |
| | |7|Second Half| | | | | | | | |HLF2| | |No| | | | |
| |13.1. 28|6|From To Date| | | | | |<FrToDt>| |[0..1]| | | |No| | | | |
| |13.1. 29|7|From Date| | | | | |<FrDt>| |[1..1]|date| | |No| | | | |
| |13.1. 30|7|To Date| | | | | |<ToDt>| |[1..1]|date| | |No| | | | |
| |13.1. 31|5|Tax Amount| | | | | |<TaxAmt>| |[0..1]| | | |No| | | | |
| |13.1. 32|6|Rate| | | | | |<Rate>| |[0..1]|decimal td = 11 fd = 10| | |No| | | | |
| |13.1. 33|6|Taxable Base Amount| | | | | |<TaxblBaseAmt>| |[0..1]|0 <= decimal td = 18 fd = 5| | |No| | | | |
| | |7|Xml Attribute Currency| | | | | |<Ccy>| | |text [A-Z]{3,3}| | |No| | | | |
| |13.1. 34|6|Total Amount| | | | | |<TtlAmt>| |[0..1]|0 <= decimal td = 18 fd = 5| | |No| | | | |
| | |7|Xml Attribute Currency| | | | | |<Ccy>| | |text [A-Z]{3,3}| | |No| | | | |
| |13.1. 35|6|Details| | | | | |<Dtls>| |[0..*]| | | |No| | | | |
| |13.1. 36|7|Period| | | | | |<Prd>| |[0..1]| | | |No| | | | |
| |13.1. 37|8|Year| | | | | |<Yr>| |[0..1]|date| | |No| | | | |
| |13.1. 38|8|Type| | | | | |<Tp>| |[0..1]|text| | |No| | | | |
| | |9|First Month| | | | | | | | |MM01| | |No| | | | |
| | |9|Second Month| | | | | | | | |MM02| | |No| | | | |
| | |9|Third Month| | | | | | | | |MM03| | |No| | | | |
| | |9|Fourth Month| | | | | | | | |MM04| | |No| | | | |
| | |9|Fifth Month| | | | | | | | |MM05| | |No| | | | |
| | |9|Sixth Month| | | | | | | | |MM06| | |No| | | | |
| | |9|Seventh Month| | | | | | | | |MM07| | |No| | | | |
| | |9|Eighth Month| | | | | | | | |MM08| | |No| | | | |
| | |9|Ninth Month| | | | | | | | |MM09| | |No| | | | |
| | |9|Tenth Month| | | | | | | | |MM10| | |No| | | | |
| | |9|Eleventh Month| | | | | | | | |MM11| | |No| | | | |
| | |9|Twelfth Month| | | | | | | | |MM12| | |No| | | | |
| | |9|First Quarter| | | | | | | | |QTR1| | |No| | | | |
| | |9|Second Quarter| | | | | | | | |QTR2| | |No| | | | |
| | |9|Third Quarter| | | | | | | | |QTR3| | |No| | | | |
| | |9|Fourth Quarter| | | | | | | | |QTR4| | |No| | | | |
| | |9|First Half| | | | | | | | |HLF1| | |No| | | | |
| | |9|Second Half| | | | | | | | |HLF2| | |No| | | | |
| |13.1. 39|8|From To Date| | | | | |<FrToDt>| |[0..1]| | | |No| | | | |
| |13.1. 40|9|From Date| | | | | |<FrDt>| |[1..1]|date| | |No| | | | |
| |13.1. 41|9|To Date| | | | | |<ToDt>| |[1..1]|date| | |No| | | | |
| |13.1. 42|7|Amount| | | | | |<Amt>| |[1..1]|0 <= decimal td = 18 fd = 5| | |No| | | | |
| | |8|Xml Attribute Currency| | | | | |<Ccy>| | |text [A-Z]{3,3}| | |No| | | | |
| |13.1. 43|5|Additional Information| | | | | |<AddtlInf>| |[0..1]|text{1,140}| | |No| | | | |
| |2.91|3|Related Remittance Information| | | | | |<RltdRmtInf>| |[0..1 0]| | | |No| | | | |
| |2.92|4|Remittance Identification| | | | | |<RmtId>| |[0..1]|text{1,35}| | |No| | | | |
| |2.93|4|Remittance Location Method| | | | | |<RmtLctnMtd>| |[0..1]|text| | |No| | | | |
| | |5|Fax| | | | | | | | |FAXI| | |No| | | | |
| | |5|Electronic Data Interchange| | | | | | | | |EDIC| | |No| | | | |
| | |5|Uniform Resource Identifier| | | | | | | | |URID| | |No| | | | |
| | |5|E Mail| | | | | | | | |EMAL| | |No| | | | |
| | |5|Post| | | | | | | | |POST| | |No| | | | |
| | |5|SMS| | | | | | | | |SMSM| | |No| | | | |
| |2.94|4|Remittance Location Electronic Address| | | | | |<RmtLctnElctrncA dr>| |[0..1]|text{1,2048}| | |No| | | | |
| |2.95|4|Remittance Location Postal Address| | | | | |<RmtLctnPstlAdr>| |[0..1]| | | |No| | | | |
| |2.96|5|Name| | | | | |<Nm>| |[1..1]|text{1,140}| | |No| | | | |
| |2.97|5|Address| | | | | |<Adr>| |[1..1]| | | |No| | | | |
| |10.1. 0|6|Address Type| | | | | |<AdrTp>| |[0..1]|text| |X|No| | | | |
| |10.1. 1|6|Department| | | | | |<Dept>| |[0..1]|text{1,70}| | |No| | | | |
| |10.1. 2|6|Sub Department| | | | | |<SubDept>| |[0..1]|text{1,70}| | |No| | | | |
| |10.1. 3|6|Street Name| | | | | |<StrtNm>| |[0..1]|text{1,70}| | |No| | | | |
| |10.1. 4|6|Building Number| | | | | |<BldgNb>| |[0..1]|text{1,16}| | |No| | | | |
| |10.1. 5|6|Post Code| | | | | |<PstCd>| |[0..1]|text{1,16}| | |No| | | | |
| |10.1. 6|6|Town Name| | | | | |<TwnNm>| |[0..1]|text{1,35}| | |No| | | | |
| |10.1. 7|6|Country Sub Division| | | | | |<CtrySubDvsn>| |[0..1]|text{1,35}| | |No| | | | |
| |10.1. 8|6|Country| | | | | |<Ctry>| |[0..1]|text [A-Z]{2,2}| |[1..1]|No| | | | |
| |10.1. 9|6|Address Line| | | | | |<AdrLine>| |[0..7]|text{1,70}| | |No| | | | |
| |2.98|3|Remittance Information| | | | | |<RmtInf>| |[0..1]| | |25|No|Alfanumérico|Referencias adicionales, esta línea se puede repetir dependiendo del número de referencias a reportar  <RmtInf>     <Ustrd>| | |
| |2.99|4|Unstructured| | | | | |<Ustrd>| |[0..*]|text{1,140}| | |No| | | | |
| |2.10 0|4|Structured| | | | | |<Strd>| |[0..*]| | | |No| | | | |
| |2.10 1|5|Referred Document Information| | | | | |<RfrdDocInf>| |[0..*]| | |25|No|Alfanumérico|Referencias adicionales  <RmtInf>     <Strd>        <RfrdDocInf>             <Nb>| | |
| |2.10 2|6|Type| | | | | |<Tp>| |[0..1]| | | |No| | | | |
| |2.10 3|7|Code Or Proprietary| | | | | |<CdOrPrtry>| |[1..1]|Choice| | |No| | | | |
| |2.10 4|8|Code| | | | | |<Cd>| |[1..1]|text| | |No| | | | |
| | |9|Invoice| | | | |Metered Service| | | |MSIN| | |No| | | | |
| | |9|Credit Note Related To Financial Adjustment| | | | | | | | |CNFA| | |No| | | | |
| | |9|Debit Note Related To Financial Adjustment| | | | | | | | |DNFA| | |No| | | | |
| | |9|Invoice| | | | |Commercial| | | |CINV| | |No| | | | |
| | |9|Credit Note| | | | | | | | |CREN| | |No| | | | |
| | |9|Debit Note| | | | | | | | |DEBN| | |No| | | | |
| | |9|Hire Invoice| | | | | | | | |HIRI| | |No| | | | |
| | |9|Self Billed Invoice| | | | | | | | |SBIN| | |No| | | | |
| | |9|Contract| | | | |Commercial| | | |CMCN| | |No| | | | |
| | |9|Account| | | | |Statement Of| | | |SOAC| | |No| | | | |
| | |9|Dispatch Advice| | | | | | | | |DISP| | |No| | | | |
| | |9|Bill Of Lading| | | | | | | | |BOLD| | |No| | | | |
| | |9|Voucher| | | | | | | | |VCHR| | |No| | | | |
| | |9|Receivable Open Item| | | | |Account| | | |AROI| | |No| | | | |
| | |9|Utility Transaction| | | | |Trade Services| | | |TSUT| | |No| | | | |
| |2.10 5|8|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| |X|No| | | | |
| |2.10 6|7|Issuer| | | | | |<Issr>| |[0..1]|text{1,35}| |X|No| | | | |
| |2.10 7|6|Number| | | | | |<Nb>| |[0..1]|text{1,35}| |[1..1]|No| | | | |
| |2.10 8|6|Related Date| | | | | |<RltdDt>| |[0..1]|date| | |No| | | | |
| |2.10 9|5|Referred Document Amount| | | | | |<RfrdDocAmt>| |[0..1]| | | |No| | | | |
| |2.11 0|6|Due Payable Amount| | | | | |<DuePyblAmt>| |[0..1]|0 <= decimal td = 18 fd = 5| | |No| | | | |
| | |7|Xml Attribute Currency| | | | | |<Ccy>| | |text [A-Z]{3,3}| | |No| | | | |
| |2.11 1|6|Discount Applied Amount| | | | | |<DscntApldAmt>| |[0..1]|0 <= decimal td = 18 fd = 5| | |No| | | | |
| | |7|Xml Attribute Currency| | | | | |<Ccy>| | |text [A-Z]{3,3}| | |No| | | | |
| |2.11 2|6|Credit Note Amount| | | | | |<CdtNoteAmt>| |[0..1]|0 <= decimal td = 18 fd = 5| | |No| | | | |
| | |7|Xml Attribute Currency| | | | | |<Ccy>| | |text [A-Z]{3,3}| | |No| | | | |
| |2.11 3|6|Tax Amount| | | | | |<TaxAmt>| |[0..1]|0 <= decimal td = 18 fd = 5| | |No| | | | |
| | |7|Xml Attribute Currency| | | | | |<Ccy>| | |text [A-Z]{3,3}| | |No| | | | |
| |2.11 4|6|Adjustment Amount And Reason| | | | | |<AdjstmntAmtAnd Rsn>| |[0..*]| | | |No| | | | |
| |2.11 5|7|Amount| | | | | |<Amt>| |[1..1]|0 <= decimal td = 18 fd = 5| | |No| | | | |
| | |8|Xml Attribute Currency| | | | | |<Ccy>| | |text [A-Z]{3,3}| | |No| | | | |
| |2.11 6|7|Credit Debit Indicator| | | | | |<CdtDbtInd>| |[0..1]|text| | |No| | | | |
| | |8|Credit| | | | | | | | |CRDT| | |No| | | | |
| | |8|Debit| | | | | | | | |DBIT| | |No| | | | |
| |2.11 7|7|Reason| | | | | |<Rsn>| |[0..1]|text{1,4}| | |No| | | | |
| |2.11 8|7|Additional Information| | | | | |<AddtlInf>| |[0..1]|text{1,140}| | |No| | | | |
| |2.11 9|6|Remitted Amount| | | | | |<RmtdAmt>| |[0..1]|0 <= decimal td = 18 fd = 5| | |No| | | | |
| | |7|Xml Attribute Currency| | | | | |<Ccy>| | |text [A-Z]{3,3}| | |No| | | | |
| |2.12 0|5|Creditor Reference Information| | | | | |<CdtrRefInf>| |[0..1]| | | |No| | | | |
| |2.12 1|6|Type| | | | | |<Tp>| |[0..1]| | | |No| | | | |
| |2.12 2|7|Code Or Proprietary| | | | | |<CdOrPrtry>| |[1..1]|Choice| | |No| | | | |
| |2.12 3|8|Code| | | | | |<Cd>| |[1..1]|text| | |No| | | | |
| | |9|Remittance Advice Message| | | | | | | | |RADM| | |No| | | | |
| | |9|Related Payment Instruction| | | | | | | | |RPIN| | |No| | | | |
| | |9|Foreign Exchange Deal Reference| | | | | | | | |FXDR| | |No| | | | |
| | |9|Dispatch Advice| | | | | | | | |DISP| | |No| | | | |
| | |9|Purchase Order| | | | | | | | |PUOR| | |No| | | | |
| | |9|Structured Communication Reference| | | | | | | | |SCOR| | |No| | | | |
| |2.12 4|8|Proprietary| | | | | |<Prtry>| |[1..1]|text{1,35}| | |No| | | | |
| |2.12 5|7|Issuer| | | | | |<Issr>| |[0..1]|text{1,35}| | |No| | | | |
| |2.12 6|6|Reference| | | | | |<Ref>| |[0..1]|text{1,35}| |[1..1]|No| | | | |
| |2.12 7|5|Invoicer| | | | | |<Invcr>| |[0..1]| | | |No| | | | |
| | |6|Name| | | | | |<Nm>| |[0..1]|text{1,140}| |[1..1]|No| | | | |
| |9.1.1|6|Postal Address| | | | | |<PstlAdr>| |[0..1]| | |X|No| | | | |
| |9.1.1 2|6|Identification| | | | | |<Id>| |[0..1]|Choice| |X|No| | | | |
| |9.1.3 3|6|Country Of Residence| | | | | |<CtryOfRes>| |[0..1]|text [A-Z]{2,2}| |X|No| | | | |
| |9.1.3 4|6|Contact Details| | | | | |<CtctDtls>| |[0..1]| | |X|No| | | | |
| |2.12 8|5|Invoicee| | | | | |<Invcee>| |[0..1]| | | |No| | | | |
| | |6|Name| | | | | |<Nm>| |[0..1]|text{1,140}| |[1..1]|No| | | | |
| |9.1.1|6|Postal Address| | | | | |<PstlAdr>| |[0..1]| | |X|No| | | | |
| |9.1.1 2|6|Identification| | | | | |<Id>| |[0..1]|Choice| |X|No| | | | |
| |9.1.3 3|6|Country Of Residence| | | | | |<CtryOfRes>| |[0..1]|text [A-Z]{2,2}| |X|No| | | | |
| |9.1.3 4|6|Contact Details| | | | | |<CtctDtls>| |[0..1]| | |X|No| | | | |
| |2.12 9|5|Additional Remittance Information| | | | | |<AddtlRmtInf>| |[0..3]|text{1,140}| | |No| | | | |
