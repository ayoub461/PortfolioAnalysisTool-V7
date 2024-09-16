import exercice3.version4.adapted_DD as dd
import Support_funct as psf
import pandas as pd

# Function to download 5 years of data for a given ticker

first_list = ['AAC', 'AAVL', 'AAWW', 'ABAX', 'ABCD', 'ABCW', 'ABMD', 'ABY', 'ACAT', 'ACHN', 'ACOR', 'ACTA', 'ACW', 
'ACXM', 'ADMS', 'ADRO', 'AEGN', 'AEGR', 'AEL', 'AEPI', 'AERI', 'AF', 'AFAM', 'AFFX', 'AFH', 'AFOP', 'AGII',
'AGTC', 'AHP', 'AHS', 'AIMC', 'AIRM', 'AJRD', 'AKS', 'ALDR', 'ALJ', 'ALOG', 'AMAG', 'AMBR', 'AMCC', 'AMNB',
'AMOT', 'AMRI', 'AMSG', 'AMTG', 'ANAC', 'ANCX', 'ANH', 'APOL', 'APTS', 'AREX', 'ARIA', 'ARII', 'ARNA', 'ARPI',
'ASCMA', 'ASEI', 'ASNA', 'AST', 'AT', 'ATRS', 'ATU', 'AVG', 'AVID', 'AVX', 'AXAS', 'AXE', 'AXLL', 'AYR', 'BABY',
'BAS', 'BBCN', 'BBG', 'BBOX', 'BBRG', 'BBX', 'BCEI', 'BCOR', 'BDE', 'BDGE', 'BEL', 'BGCP', 'BGG', 'BHBK', 'BID',
'BIOS', 'BKMU', 'BKS', 'BLCM', 'BLMT', 'BLOX', 'BLT', 'BMTC', 'BNCL', 'BNCN', 'BNFT', 'BOBE', 'BOFI', 'BOJA', 'BPFH','BPI', 
'BREW', 'BRG', 'BRKS', 'BRS', 'BRSS', 'BSF', 'BSFT', 'BSTC', 'BTX', 'BWINB', 'BWLD', 'BXS', 'CACB', 'CACQ', 'CALD', 'CAMP',
'CARB', 'CATM', 'CAVM', 'CBB', 'CBF', 'CBK', 'CBM', 'CBMG', 'CBPX', 'CBR', 'CBYL', 'CCC', 'CCF', 'CCMP', 'CCXI', 'CDI', 'CDR',
'CDRB', 'CEB', 'CECE', 'CEMP', 'CETV', 'CFNL', 'CGI', 'CHFC', 'CHFN', 'CHKE', 'CHMT', 'CHS', 'CHSP', 'CIFC', 'CIR', 'CJES', 'CKEC',
'CKH', 'CKP', 'CLCT', 'CLD', 'CLI', 'CLMS', 'CLNY', 'CLVS', 'CMN', 'CMO', 'CNBKA', 'CNCE', 'CNXR', 'COB', 'COBZ', 'CONE', 'CORE',
'CORI', 'CORR', 'COWN', 'CPE', 'CPHD', 'CPLA', 'CPSI', 'CRAY', 'CRCM', 'CRD.B', 'CRR', 'CRY', 'CRZO', 'CSBK', 'CSCD', 'CSFL', 'CSII',
'CSLT', 'CSOD', 'CSS', 'CSU', 'CTB', 'CTCT', 'CTIC', 'CTRL', 'CTT', 'CTWS', 'CUNB', 'CVRS', 'CVT', 'CVTI', 'CWEI', 'CYNO', 'CYS', 'CYTR',
'DCT', 'DEL', 'DEPO', 'DF', 'DFRG', 'DFT', 'DGI', 'DMND', 'DOOR', 'DPLO', 'DRII', 'DRNA', 'DSPG', 'DTLK', 'DTSI', 'DW', 'DWA', 'DWRE', 'DYAX', 'EBIX', 
'EBSB', 'ECHO', 'ECOL', 'ECOM', 'ECR', 'ECYT', 'EDE', 'EFII', 'EGL', 'EGLE', 'EGOV', 'EIGI', 'ELGX', 'ELLI', 'ELNK', 'ELRC', 'ELY', 'EMCI', 'ENOC', 'ENT',
'ENTL', 'EPAY', 'EPIQ', 'EPZM', 'EQY', 'ERA', 'ERI', 'EROS', 'ESL', 'ESND', 'ESTE', 'ETM', 'EVDY', 'EXAC', 'EXAM', 'EXAR', 'EXPR', 'EXXI', 'EYES', 'FBC',
'FBNK', 'FCB', 'FCH', 'FCS', 'FCSC', 'FDEF', 'FDML', 'FEIC', 'FENX', 'FFG', 'FFKT', 'FGL', 'FINL', 'FLDM', 'FLKS', 'FLTX', 'FLXN', 'FMBI', 'FMER', 'FMI',
'FMSA', 'FNBC', 'FNFV', 'FNGN', 'FNHC', 'FNSR', 'FOE', 'FOMX', 'FPO', 'FPRX', 'FRAN', 'FRED', 'FRGI', 'FRP', 'FSAM', 'FSB', 'FTD', 'FUEL', 'FVE', 'FWM', 'FXCB', 
'GBL', 'GBNK', 'GCAP', 'GHDX', 'GHL', 'GIMO', 'GLF', 'GLOG', 'GLUU', 'GNBC', 'GNCA', 'GNCMA', 'GNMK', 'GOV', 'GPT', 'GPX', 'GRUB', 'GST', 'GTS', 'GTT', 'GUID',
'GWB', 'HABT', 'HBHC', 'HCCI', 'HCHC', 'HDP', 'HEI.A', 'HEOP', 'HGR', 'HIFR', 'HIL', 'HK', 'HLS', 'HLTH', 'HMHC', 'HMPR', 'HMSY', 'HMTV', 'HNH', 'HOS', 
'HPY', 'HRG', 'HSC', 'HSKA', 'HSNI', 'HT', 'HTS', 'HTWR', 'HW', 'HWAY', 'HYH', 'I', 'IBKC', 'IDRA', 'IDTI', 'IHC', 'IILG', 'IIVI', 'IL', 'IMDZ', 'IMGN', 'IMH',
'IMMU', 'IMN', 'IMPR', 'IMPV', 'INAP', 'INFI', 'ININ', 'INSY', 'INVN', 'INWK', 'IO', 'IPCC', 'IPHI', 'IPHS', 'IPXL', 'IQNT', 'IRC', 'ISBC', 'ISCA', 'ISIL', 'ISLE',
'ITG', 'IVC', 'IXYS', 'JCOM', 'JGW', 'JMBA', 'JMG', 'JNS', 'JONE', 'KAMN', 'KBAL', 'KCG', 'KEG', 'KERX', 'KEYW', 'KITE', 'KKD', 'KLXI', 'KMG', 'KND', 'KNL', 'KONA',
'KRA', 'KTWO', 'LABL', 'LAWS', 'LBIO', 'LBY', 'LCI', 'LDL', 'LDR', 'LDRH', 'LG', 'LHCG', 'LHO', 'LIFE', 'LIOX', 'LJPC', 'LLNW', 'LMNX', 'LMOS', 'LNCE', 'LNDC', 'LOCK',
'LOGM', 'LORL', 'LOXO', 'LQ', 'LTS', 'LTXB', 'LXFT', 'MACK', 'MANT', 'MBFI', 'MBVT', 'MCF', 'MDAS', 'MDC', 'MDCA', 'MDCO', 
'MDGN', 'MDLY', 'MDP', 'MDR', 'MDSO', 'MENT', 'METR', 'MFRM', 'MGI', 'MGLN', 'MHGC', 'MIFI', 'MINI', 'MKTO', 'MLHR', 'MNTA', 'MOBL', 'MODN', 'MOG.A', 'MPG', 'MRLN',
'MRTX', 'MSCC', 'MSFG', 'MTGE', 'MTOR', 'MTSC', 'MTSN', 'MW', 'MWW', 'MXPT', 'MYCC', 'NADL', 'NANO', 'NAO', 'NAV', 'NAVG', 'NBBC', 'NCOM', 'NCS', 'NEFF', 'NEWM', 'NEWR',
'NEWS', 'NGHC', 'NILE', 'NLNK', 'NLS', 'NM', 'NMBL', 'NNA', 'NP', 'NPBC', 'NPTN', 'NRCIA', 'NRZ', 'NSM', 'NSR', 'NTK', 'NTLS', 'NTRI', 'NUTR', 'NUVA', 'NVIV', 'NVTA', 
'NWHM', 'NXTM', 'NYLD', 'NYNY', 'NYRT', 'OAS', 'OCAT', 'OCLR', 'OCN', 'OKSB', 'OMAM', 'OME', 'OMED', 'OMN', 'ONCE', 'ONDK', 'ONTY', 'OPB', 'OPHT', 'OPWR', 'ORBC', 'OREX', 
'ORIT', 'OSIR', 'OSTK', 'OTIC', 'OUTR', 'OVAS', 'OVTI', 'OXFD', 'OZRK', 'PCBK', 'PCCC', 'PCO', 'PCYG', 'PDCE', 'PDLI', 'PDVW', 'PE', 'PEGI', 'PEI', 'PEIX', 'PERY', 'PES',
'PETX', 'PFNX', 'PFPT', 'PFSW', 'PGEM', 'PGND', 'PGNX', 'PGTI', 'PHH', 'PHIIK', 'PICO', 'PIR', 'PJC', 'PKD', 'PKY', 'PLCM', 'PLKI', 'PLT', 'PMC', 'PN', 'PNK', 'PNY', 'POL',
'POWR', 'POZN', 'PPHM', 'PRAH', 'PRSC', 'PRTK', 'PRTO', 'PRTY', 'PRXL', 'PSB', 'PSG', 'PSTB', 'PTLA', 'PTX', 'PVA', 'PVTB', 'PZN', 'QADA', 'QLGC', 'QLIK', 'QSII', 'QTM', 'QTS', 
'RAS', 'RAVN', 'RCAP', 'RCII', 'RDEN', 'RECN', 'REIS', 'REV', 'REXI', 'REXX', 'RJET', 'RKUS', 'RLD', 'RLYP', 'RNET', 'RNWK', 'ROLL', 'ROVI', 'ROX', 'RP', 'RPT', 'RPTP', 'RPXC', 
'RSE', 'RSO', 'RSPP', 'RSTI', 'RT', 'RTEC', 'RTIX', 'RTK', 'RTRX', 'RUBI', 'RUTH', 'RXDX', 'RXN', 'SAAS', 'SAFM', 'SALE', 'SALT', 'SBY', 'SCAI', 'SCHN', 'SCLN', 'SCMP', 'SCSS', 
'SEAS', 'SEMG', 'SFE', 'SFLY', 'SFS', 'SFXE', 'SGBK', 'SGI', 'SGM', 'SGMS', 'SGNT', 'SGY', 'SGYP', 'SHLM', 'SHOR', 'SIEN', 'SIGM', 'SJI', 'SKUL', 'SNAK', 'SNBC', 'SNC', 'SNHY', 
'SNMX', 'SNR', 'SNTA', 'SONC', 'SONS', 'SP', 'SPA', 'SPKE', 'SPNC', 'SPPI', 'SQBG', 'SQI', 'SQNM', 'SREV', 'SSE', 'SSI', 'SSNI', 'SSS', 'STAR', 'STBZ', 'STCK', 'STFC', 'STL', 'STML', 
'STMP', 'STOR', 'STRP', 'SVU', 'SWC', 'SWFT', 'SWHC', 'SWM', 'SYA', 'SYKE', 'SYNT', 'SYRG', 'SYUT', 'SYX', 'SZMK', 'SZYM', 'TASR', 'TAST', 'TAT', 'TAX', 'TBK', 'TBRA', 'TECD', 'TESO',
'TFM', 'TGH', 'THLD', 'TIS', 'TIVO', 'TKAI', 'TLMR', 'TMH', 'TMST', 'TNAV', 'TNGO', 'TOWR', 
'TPLM', 'TPRE', 'TPUB', 'TREC', 'TRK', 'TROV', 'TRR', 'TRXC', 'TSC', 'TSRA', 'TSRO', 'TSYS', 'TTPH', 'TTS', 'TUBE', 'TUES', 'TUMI', 'TVPT', 'TXTR', 'TYPE', 
'UACL', 'UAM', 'UBA', 'UBNK', 'UBNT', 'UBSH', 'UCFC', 'UDF', 'UIHC', 'UMPQ', 'UNIS', 'UNT', 'UNTD', 'UPL', 'USAK', 'USCR', 'UTEK', 'UTIW', 'VA', 'VASC', 'VCRA', 'VDSI', 'VEC', 'VG', 
'VISI', 'VIVO', 'VMEM', 'VRTU', 'VRTV', 'VSAR', 'VSI', 'VSLR', 'VTAE', 'VTL', 'VVUS', 'WAC', 'WAGE', 'WAIR', 'WBMD', 'WCG', 'WCIC', 'WETF', 'WGL', 'WIBC', 'WIFI', 'WIN', 'WLB', 'WLH', 
'WMAR', 'WMC', 'WMGI', 'WNR', 'WRE', 'WSTC', 'WWE', 'XCO', 'XCRA', 'XENT', 'XLRN', 'XNPT', 'XOXO', 'XRM', 'XXIA', 'YDKN', 'YRCW', 'ZAGG', 'ZAIS', 'ZEN', 'ZFGN', 'ZGNX', 'ZINC', 'ZIOP', 'ZIXI', 'ZLTQ', 'ZOES']



second_list = ['AAC', 'AAVL', 'AAWW', 'ABAX', 'ABCD', 'ABCW', 'ABMD', 'ABY', 'ACAT', 'ACHN', 'ACOR', 'ACTA', 'ACW', 'ACXM', 'ADMS', 'ADRO', 'AEGN', 'AEGR', 'AEL', 'AEPI', 'AERI', 'AF', 'AFAM', 'AFFX', 'AFH', 'AFOP', 'AGII', 'AGTC', 'AHP', 'AHS', 'AIMC', 'AIRM', 'AJRD', 'AKS', 'ALDR', 'ALJ', 'ALOG', 'AMAG', 'AMBR', 'AMCC', 'AMNB', 'AMOT', 'AMRI', 'AMSG', 'AMTG', 'ANAC', 'ANCX', 'ANH', 'APOL', 'APTS', 'AREX', 'ARIA', 'ARII', 'ARNA', 'ARPI', 'ASCMA', 'ASEI', 'ASNA', 'AST', 'AT', 'ATRS', 'ATU', 'AVG', 'AVID', 'AVX', 'AXAS', 'AXE', 'AXLL', 'AYR', 'BABY', 'BAS', 'BBCN', 'BBG', 'BBOX', 'BBRG', 'BBX', 'BCEI', 'BCOR', 'BDE', 'BDGE', 'BEL', 'BGCP', 'BGG', 'BHBK', 'BID', 'BIOS', 'BKMU', 'BKS', 'BLCM', 'BLMT', 'BLOX', 'BLT', 'BMTC', 'BNCL', 'BNCN', 'BNFT', 'BOBE', 'BOFI', 'BOJA', 'BPFH', 'BPI', 'BREW', 'BRG', 'BRKS', 'BRS', 'BRSS', 'BSF', 'BSFT', 'BSTC', 'BTX', 'BWINB', 'BWLD', 'BXS', 'CACB', 'CACQ', 'CALD', 'CAMP', 'CARB', 'CATM', 'CAVM', 'CBB', 'CBF', 'CBK', 'CBM', 'CBMG', 'CBPX', 'CBR', 'CBYL', 'CCC', 'CCF', 'CCMP', 'CCXI', 'CDI', 'CDR', 'CDRB', 'CEB', 'CECE', 'CEMP', 'CETV', 'CFNL', 'CGI', 'CHFC', 'CHFN', 'CHKE', 'CHMT', 'CHS', 'CHSP', 'CIFC', 'CIR', 'CJES', 'CKEC', 'CKH', 'CKP', 'CLCT', 'CLD', 'CLI', 'CLMS', 'CLNY', 'CLVS', 'CMN', 'CMO', 'CNBKA', 'CNCE', 'CNXR', 'COB', 'COBZ', 'CONE', 'CORE', 'CORI', 'CORR', 'COWN', 'CPE', 'CPHD', 'CPLA', 'CPSI', 'CRAY', 'CRCM', 'CRD.B', 'CRR', 'CRY', 'CRZO', 'CSBK', 'CSCD', 'CSFL', 'CSII', 'CSLT', 'CSOD', 'CSS', 'CSU', 'CTB', 'CTCT', 'CTIC', 'CTRL', 'CTT', 'CTWS', 'CUNB', 'CVRS', 'CVT', 'CVTI', 'CWEI', 'CYNO', 'CYS', 'CYTR', 'DCT', 'DEL', 'DEPO', 'DF', 'DFRG', 'DFT', 'DGI', 'DMND', 'DOOR', 'DPLO', 'DRII', 'DRNA', 'DSPG', 'DTLK', 'DTSI', 'DW', 'DWA', 'DWRE', 'DYAX', 'EBIX', 'EBSB', 'ECHO', 'ECOL', 'ECOM', 'ECR', 'ECYT', 'EDE', 'EFII', 'EGL', 'EGLE', 'EGOV', 'EIGI', 'ELGX', 'ELLI', 'ELNK', 'ELRC', 'ELY', 'EMCI', 'ENOC', 'ENT', 'ENTL', 'EPAY', 'EPIQ', 'EPZM', 'EQY', 'ERA', 'ERI', 'EROS', 'ESL', 'ESND', 'ESTE', 'ETM', 'EVDY', 'EXAC', 'EXAM', 'EXAR', 'EXPR', 'EXXI', 'EYES', 'FBC', 'FBNK', 'FCB', 'FCH', 'FCS', 'FCSC', 'FDEF', 'FDML', 'FEIC', 'FENX', 'FFG', 'FFKT', 'FGL', 'FINL', 'FLDM', 'FLKS', 'FLTX', 'FLXN', 'FMBI', 'FMER', 'FMI', 'FMSA', 'FNBC', 'FNFV', 'FNGN', 'FNHC', 'FNSR', 'FOE', 'FOMX', 'FPO', 'FPRX', 'FRAN', 'FRED', 'FRGI', 'FRP', 'FSAM', 'FSB', 'FTD', 'FUEL', 'FVE', 'FWM', 'FXCB', 
'GBL', 'GBNK', 'GCAP', 'GHDX', 'GHL', 'GIMO', 'GLF', 'GLOG', 'GLUU', 'GNBC', 'GNCA', 'GNCMA', 'GNMK', 'GOV', 'GPT', 'GPX', 'GRUB', 'GST', 'GTS', 'GTT', 'GUID', 'GWB', 'HABT', 'HBHC', 'HCCI', 'HCHC', 'HDP', 'HEI.A', 'HEOP', 'HGR', 'HIFR', 'HIL', 'HK', 'HLS', 'HLTH', 'HMHC', 'HMPR', 'HMSY', 'HMTV', 'HNH', 'HOS', 'HPY', 'HRG', 'HSC', 'HSKA', 'HSNI', 'HT', 'HTS', 'HTWR', 'HW', 'HWAY', 'HYH', 'I', 'IBKC', 'IDRA', 'IDTI', 'IHC', 'IILG', 'IIVI', 'IL', 'IMDZ', 'IMGN', 'IMH', 'IMMU', 'IMN', 'IMPR', 'IMPV', 'INAP', 'INFI', 'ININ', 'INSY', 'INVN', 'INWK', 'IO', 'IPCC', 'IPHI', 'IPHS', 'IPXL', 'IQNT', 'IRC', 'ISBC', 'ISCA', 'ISIL', 'ISLE', 'ITG', 'IVC', 'IXYS', 'JCOM', 'JGW', 'JMBA', 'JMG', 'JNS', 'JONE', 'KAMN', 'KBAL', 'KCG', 'KEG', 'KERX', 'KEYW', 'KITE', 'KKD', 'KLXI', 'KMG', 'KND', 'KNL', 'KONA', 'KRA', 'KTWO', 'LABL', 'LAWS', 'LBIO', 'LBY', 'LCI', 'LDL', 'LDR', 'LDRH', 'LG', 'LHCG', 'LHO', 'LIFE', 'LIOX', 'LJPC', 'LLNW', 'LMNX', 'LMOS', 'LNCE', 'LNDC', 'LOCK', 'LOGM', 'LORL', 'LOXO', 'LQ', 'LTS', 'LTXB', 'LXFT', 'MACK', 'MANT', 'MBFI', 'MBVT', 'MCF', 'MDAS', 'MDC', 'MDCA', 'MDCO', 'MDGN', 'MDLY', 'MDP', 'MDR', 'MDSO', 'MENT', 'METR', 'MFRM', 'MGI', 'MGLN', 'MHGC', 'MIFI', 'MINI', 'MKTO', 'MLHR', 'MNTA', 'MOBL', 'MODN', 'MOG.A', 'MPG', 'MRLN', 'MRTX', 'MSCC', 'MSFG', 'MTGE', 'MTOR', 'MTSC', 'MTSN', 'MW', 'MWW', 'MXPT', 'MYCC', 'NADL', 'NANO', 'NAO', 'NAV', 'NAVG', 'NBBC', 'NCOM', 'NCS', 'NEFF', 'NEWM', 'NEWR', 'NEWS', 'NGHC', 'NILE', 'NLNK', 'NLS', 'NM', 'NMBL', 'NNA', 'NP', 'NPBC', 'NPTN', 'NRCIA', 'NRZ', 'NSM', 'NSR', 'NTK', 'NTLS', 'NTRI', 'NUTR', 'NUVA', 'NVIV', 'NVTA', 'NWHM', 'NXTM', 'NYLD', 'NYNY', 'NYRT', 'OAS', 'OCAT', 'OCLR', 'OCN', 'OKSB', 'OMAM', 'OME', 'OMED', 'OMN', 'ONCE', 'ONDK', 'ONTY', 'OPB', 'OPHT', 'OPWR', 'ORBC', 'OREX', 'ORIT', 'OSIR', 'OSTK', 'OTIC', 'OUTR', 'OVAS', 'OVTI', 'OXFD', 'OZRK', 'PCBK', 'PCCC', 'PCO', 'PCYG', 'PDCE', 'PDLI', 'PDVW', 'PE', 'PEGI', 'PEI', 'PEIX', 'PERY', 'PES', 'PETX', 'PFNX', 'PFPT', 'PFSW', 'PGEM', 'PGND', 'PGNX', 'PGTI', 'PHH', 'PHIIK', 'PICO', 'PIR', 'PJC', 'PKD', 'PKY', 'PLCM', 'PLKI', 'PLT', 'PMC', 'PN', 'PNK', 'PNY', 'POL', 'POWR', 'POZN', 'PPHM', 'PRAH', 'PRSC', 'PRTK', 'PRTO', 'PRTY', 'PRXL', 'PSB', 'PSTB', 'PTLA', 'PTX', 'PVA', 'PVTB', 'PZN', 'QADA', 'QLGC', 'QLIK', 'QSII', 'QTM', 'QTS', 'RAS', 'RAVN', 'RCAP', 'RCII', 'RDEN', 'RECN', 'REIS', 'REV', 'REXI', 'REXX', 'RJET', 'RKUS', 'RLD', 'RLYP', 'RNET', 'RNWK', 'ROLL', 'ROVI', 'ROX', 'RP', 'RPT', 'RPTP', 'RPXC', 'RSE', 'RSO', 'RSPP', 'RSTI', 'RTEC', 'RTIX', 'RTK', 'RTRX', 'RUBI', 'RUTH', 'RXDX', 'RXN', 'SAAS', 'SAFM', 'SALE', 'SALT', 'SBY', 'SCAI', 'SCHN', 'SCLN', 'SCMP', 'SCSS', 'SEAS', 'SEMG', 'SFE', 'SFLY', 'SFS', 'SFXE', 'SGBK', 'SGI', 'SGM', 'SGMS', 'SGNT', 'SGY', 'SGYP', 'SHLM', 'SHOR', 'SIEN', 'SIGM', 'SJI', 'SKUL', 'SNAK', 'SNBC', 'SNC', 'SNHY', 'SNMX', 'SNR', 'SNTA', 'SONC', 'SONS', 'SP', 'SPA', 'SPKE', 'SPNC', 'SPPI', 
'SQBG', 'SQI', 'SQNM', 'SREV', 'SSE', 'SSI', 'SSNI', 'SSS', 'STAR', 'STBZ', 'STCK', 'STFC', 'STL', 'STML', 'STMP', 'STOR', 'STRP', 'SVU', 'SWC', 'SWFT', 'SWHC', 'SWM', 'SYA', 'SYKE', 'SYNT', 'SYRG', 'SYUT', 'SYX', 'SZMK', 'SZYM', 'TASR', 'TAST', 'TAT', 'TAX', 'TBK', 'TBRA', 'TECD', 'TESO', 'TFM', 'TGH', 'THLD', 'TIS', 'TIVO', 'TKAI', 'TLMR', 'TMH', 'TMST', 'TNAV', 'TNGO', 'TOWR', 'TPLM', 'TPRE', 'TPUB', 'TREC', 'TRK', 'TROV', 'TRR', 'TRXC', 'TSC', 'TSRA', 'TSRO', 'TSYS', 'TTPH', 'TTS', 'TUBE', 'TUES', 'TUMI', 'TVPT', 'TXTR', 'TYPE', 'UACL', 'UBA', 'UBNK', 'UBNT', 'UBSH', 'UCFC', 'UDF', 'UIHC', 'UMPQ', 'UNIS', 'UNT', 'UNTD', 'UPL', 'USAK', 'USCR', 'UTEK', 'UTIW', 'VA', 'VASC', 'VCRA', 'VDSI', 'VEC', 'VG', 'VISI', 'VIVO', 'VMEM', 'VRTU', 'VRTV', 'VSAR', 'VSI', 'VSLR', 'VTAE', 'VTL', 'VVUS', 'WAC', 'WAGE', 'WAIR', 'WBMD', 'WCG', 'WCIC', 'WETF', 'WGL', 'WIBC', 'WIFI', 'WIN', 'WLB', 'WLH', 'WMAR', 'WMC', 'WMGI', 'WNR', 'WRE', 'WSTC', 'WWE', 'XCO', 'XCRA', 'XENT', 'XLRN', 'XNPT', 'XOXO', 'XRM', 'XXIA', 'YDKN', 'YRCW', 'ZAGG', 'ZAIS', 'ZEN', 'ZFGN', 'ZGNX', 'ZINC', 'ZIOP', 'ZIXI', 'ZLTQ', 'ZOES']

df_first_list = pd.DataFrame(first_list, columns=["tickers"])
df_second_list = pd.DataFrame(second_list, columns=["tickers"])

file_folder = "C:\\Users\\dl\\Desktop\\project_portofolio_analysis\\testing"
fpath = psf.get_file_path(file_folder,"failed_tickers", extension="xlsx")
with pd.ExcelWriter(fpath) as writer:
    df_first_list.to_excel(writer, sheet_name='first_list')
    df_second_list.to_excel(writer,sheet_name = 'second_list')
    




print(len(first_list))
print(len(second_list))


for ticker in second_list:
    if ticker == 'UAM' or ticker == 'RT' or ticker == 'PSG':
        print(ticker)



"""Check and Display existing Tickers"""

'''
tickers = listss
failed = dd.yfin(tickers)
print(failed)
'''