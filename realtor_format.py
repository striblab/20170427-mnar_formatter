import pandas as pd

nlc = pd.read_excel('City and Nbhd data - annual 2016.xlsx', sheetname="NL-C", names=["", "City", "NL-2003", "NL-2004", "NL-2005", "NL-2006", "NL-2007", "NL-2008", "NL-2009", "NL-2010", "NL-2011", "NL-2012", 
	"NL-2013", "NL-2014", "NL-2015", "NL-2016", "NL-Grand Total", "NL-MAX", "NL-All time highs?"], encoding="sys.getfilesystemencoding()")

#Drop first 11 rows, first column
nlc.drop(nlc.index[:12], inplace=True)
nlc.drop('', axis=1, inplace=True)

nln = pd.read_excel('City and Nbhd data - annual 2016.xlsx', sheetname="NL-N", names=["", "City", "NL-2003", "NL-2004", "NL-2005", "NL-2006", "NL-2007", "NL-2008", "NL-2009", "NL-2010", "NL-2011", "NL-2012", 
	"NL-2013", "NL-2014", "NL-2015", "NL-2016", "NL-Grand Total", "NL-MAX", "NL-All time highs?"], encoding="sys.getfilesystemencoding()")

#Drop first 11 rows, first column
nln.drop(nln.index[:12], inplace=True)
nln.drop('', axis=1, inplace=True)

csc = pd.read_excel('City and Nbhd data - annual 2016.xlsx', sheetname="CS-C", names=["", "City", "CS-2003", "CS-2004", "CS-2005", "CS-2006", "CS-2007", "CS-2008", "CS-2009", "CS-2010", "CS-2011", "CS-2012", 
	"CS-2013", "CS-2014", "CS-2015", "CS-2016", "CS-Grand Total", "CS-MAX", "CS-All time highs?"], encoding="sys.getfilesystemencoding()")

#Drop first 11 rows, first column
csc.drop(csc.index[:13], inplace=True)
csc.drop('', axis=1, inplace=True)

csn = pd.read_excel('City and Nbhd data - annual 2016.xlsx', sheetname="CS-N", names=["", "City", "CS-2003", "CS-2004", "CS-2005", "CS-2006", "CS-2007", "CS-2008", "CS-2009", "CS-2010", "CS-2011", "CS-2012", 
	"CS-2013", "CS-2014", "CS-2015", "CS-2016", "CS-Grand Total", "CS-MAX", "CS-All time highs?"], encoding="sys.getfilesystemencoding()")

#Drop first 11 rows, first column
csn.drop(csn.index[:12], inplace=True)
csn.drop('', axis=1, inplace=True)

invc = pd.read_excel('City and Nbhd data - annual 2016.xlsx', sheetname="INV-C", names=["", "City", "INV-2003", "INV-2004", "INV-2005", "INV-2006", "INV-2007", "INV-2008", "INV-2009", "INV-2010", "INV-2011", "INV-2012", 
	"INV-2013", "INV-2014", "INV-2015", "INV-2016", "INV-Grand Total", "INV-MAX", "INV-All time highs?"], encoding="sys.getfilesystemencoding()")

#Drop first 11 rows, first column
invc.drop(invc.index[:12], inplace=True)
invc.drop('', axis=1, inplace=True)

invn = pd.read_excel('City and Nbhd data - annual 2016.xlsx', sheetname="INV-N", names=["", "City", "INV-2003", "INV-2004", "INV-2005", "INV-2006", "INV-2007", "INV-2008", "INV-2009", "INV-2010", "INV-2011", "INV-2012", 
	"INV-2013", "INV-2014", "INV-2015", "INV-2016", "INV-Grand Total", "INV-MAX", "INV-All time highs?"], encoding="sys.getfilesystemencoding()")

#Drop first 11 rows, first column
invn.drop(invn.index[:12], inplace=True)
invn.drop('', axis=1, inplace=True)

mspc = pd.read_excel('City and Nbhd data - annual 2016.xlsx', sheetname="MSP-C", names=["", "City", "MSP-2003", "MSP-2004", "MSP-2005", "MSP-2006", "MSP-2007", "MSP-2008", "MSP-2009", "MSP-2010", "MSP-2011", "MSP-2012", 
	"MSP-2013", "MSP-2014", "MSP-2015", "MSP-2016", "MSP-Grand Total", "MSP-MAX", "MSP-All time highs?", "MSP-Pct chg fr max"], encoding="sys.getfilesystemencoding()")

#Drop first 11 rows, first column
mspc.drop(mspc.index[:12], inplace=True)
mspc.drop('', axis=1, inplace=True)

mspn = pd.read_excel('City and Nbhd data - annual 2016.xlsx', sheetname="MSP-N", names=["", "City", "MSP-2003", "MSP-2004", "MSP-2005", "MSP-2006", "MSP-2007", "MSP-2008", "MSP-2009", "MSP-2010", "MSP-2011", "MSP-2012", 
	"MSP-2013", "MSP-2014", "MSP-2015", "MSP-2016", "MSP-Grand Total", "MSP-MAX", "MSP-All time highs?", "MSP-Pct chg fr max"], encoding="sys.getfilesystemencoding()")

#Drop first 11 rows, first column
mspn.drop(mspn.index[:12], inplace=True)
mspn.drop('', axis=1, inplace=True)

ppsfc = pd.read_excel('City and Nbhd data - annual 2016.xlsx', sheetname="PPSF-C", names=["","City", "City2", "PPSF-2003", "PPSF-2004", "PPSF-2005", "PPSF-2006", "PPSF-2007", "PPSF-2008", "PPSF-2009", "PPSF-2010", "PPSF-2011", "PPSF-2012", 
	"PPSF-2013", "PPSF-2014", "PPSF-2015", "PPSF-2016", "PPSF-Grand Total", "PPSF-MAX", "PPSF-All time highs?", "PPSF-Pct chg fr max"], encoding="sys.getfilesystemencoding()")

#Drop first 11 rows, first column
ppsfc.drop(ppsfc.index[:13], inplace=True)
ppsfc.drop('', axis=1, inplace=True)

ppsfn = pd.read_excel('City and Nbhd data - annual 2016.xlsx', sheetname="PPSF-N", names=["", "City", "PPSF-2003", "PPSF-2004", "PPSF-2005", "PPSF-2006", "PPSF-2007", "PPSF-2008", "PPSF-2009", "PPSF-2010", "PPSF-2011", "PPSF-2012", 
	"PPSF-2013", "PPSF-2014", "PPSF-2015", "PPSF-2016", "PPSF-Grand Total", "PPSF-MAX", "PPSF-All time highs?", "PPSF-Pct chg fr max"], encoding="sys.getfilesystemencoding()")

#Drop first 11 rows, first column
ppsfn.drop(ppsfn.index[:12], inplace=True)
ppsfn.drop('', axis=1, inplace=True)

cdomc = pd.read_excel('City and Nbhd data - annual 2016.xlsx', sheetname="CDOM-C", names=["", "City", "CDOM-2003", "CDOM-2004", "CDOM-2005", "CDOM-2006", "CDOM-2007", "CDOM-2008", "CDOM-2009", "CDOM-2010", "CDOM-2011", "CDOM-2012", 
	"CDOM-2013", "CDOM-2014", "CDOM-2015", "CDOM-2016", "CDOM-Grand Total", "CDOM-MIN", "CDOM-All time lows?", "CDOM-Pct chg fr max"], encoding="sys.getfilesystemencoding()")

#Drop first 11 rows, first column
cdomc.drop(cdomc.index[:12], inplace=True)
cdomc.drop('', axis=1, inplace=True)

cdomn = pd.read_excel('City and Nbhd data - annual 2016.xlsx', sheetname="CDOM-N", names=["", "City", "CDOM-2003", "CDOM-2004", "CDOM-2005", "CDOM-2006", "CDOM-2007", "CDOM-2008", "CDOM-2009", "CDOM-2010", "CDOM-2011", "CDOM-2012", 
	"CDOM-2013", "CDOM-2014", "CDOM-2015", "CDOM-2016", "CDOM-Grand Total", "CDOM-MAX", "CDOM-All time highs?", "CDOM-Pct chg fr max"], encoding="sys.getfilesystemencoding()")

#Drop first 11 rows, first column
cdomn.drop(cdomn.index[:12], inplace=True)
cdomn.drop('', axis=1, inplace=True)

polpc = pd.read_excel('City and Nbhd data - annual 2016.xlsx', sheetname="POLP-C", names=["", "City", "POLP-2003", "POLP-2004", "POLP-2005", "POLP-2006", "POLP-2007", "POLP-2008", "POLP-2009", "POLP-2010", "POLP-2011", "POLP-2012", 
	"POLP-2013", "POLP-2014", "POLP-2015", "POLP-2016", "POLP-Grand Total", "POLP-MIN", "POLP-All time lows?", "POLP-Pct chg fr max"], encoding="sys.getfilesystemencoding()")

#Drop first 11 rows, first column
polpc.drop(polpc.index[:12], inplace=True)
polpc.drop('', axis=1, inplace=True)

polpn = pd.read_excel('City and Nbhd data - annual 2016.xlsx', sheetname="POLP-N", names=["", "City", "POLP-2003", "POLP-2004", "POLP-2005", "POLP-2006", "POLP-2007", "POLP-2008", "POLP-2009", "POLP-2010", "POLP-2011", "POLP-2012", 
	"POLP-2013", "POLP-2014", "POLP-2015", "POLP-2016", "POLP-Grand Total", "POLP-MAX", "POLP-All time highs?", "POLP-Pct chg fr max"], encoding="sys.getfilesystemencoding()")

#Drop first 11 rows, first column
polpn.drop(polpn.index[:12], inplace=True)
polpn.drop('', axis=1, inplace=True)

pclpn = pd.read_excel('City and Nbhd data - annual 2016.xlsx', sheetname="PCLP-N", names=["", "City", "PCLP-2003", "PCLP-2004", "PCLP-2005", "PCLP-2006", "PCLP-2007", "PCLP-2008", "PCLP-2009", "PCLP-2010", "PCLP-2011", "PCLP-2012", 
	"PCLP-2013", "PCLP-2014", "PCLP-2015", "PCLP-2016", "PCLP-Grand Total", "PCLP-MIN", "PCLP-All time lows?", "PCLP-Pct chg fr max"], encoding="sys.getfilesystemencoding()")

#Drop first 11 rows, first column
pclpn.drop(pclpn.index[:12], inplace=True)
pclpn.drop('', axis=1, inplace=True)

pclpc = pd.read_excel('City and Nbhd data - annual 2016.xlsx', sheetname="PCLP-C", names=["", "City", "PCLP-2003", "PCLP-2004", "PCLP-2005", "PCLP-2006", "PCLP-2007", "PCLP-2008", "PCLP-2009", "PCLP-2010", "PCLP-2011", "PCLP-2012", 
	"PCLP-2013", "PCLP-2014", "PCLP-2015", "PCLP-2016", "PCLP-Grand Total", "PCLP-MAX", "PCLP-All time highs?", "PCLP-Pct chg fr max"], encoding="sys.getfilesystemencoding()")

#Drop first 11 rows, first column
pclpc.drop(pclpc.index[:12], inplace=True)
pclpc.drop('', axis=1, inplace=True)


# Uncomment for individual metrics
# nlc.to_csv("results/nlc.csv")
# nln.to_csv("results/nln.csv")
# csc.to_csv("results/csc.csv")
# csn.to_csv("results/csn.csv")
# invc.to_csv("results/invc.csv")
# invn.to_csv("results/invn.csv")
# mspc.to_csv("results/mspc.csv")
# mspn.to_csv("results/mspn.csv")
# ppsfc.to_csv("results/ppsfc.csv")
# ppsfn.to_csv("results/ppsfn.csv")
# cdomc.to_csv("results/cdomc.csv")
# cdomn.to_csv("results/cdomn.csv")
# polpc.to_csv("results/polpc.csv")
# polpn.to_csv("results/polpn.csv")
# pclpn.to_csv("results/pclpn.csv")
# pclpc.to_csv("results/pclpc.csv")

cities = nlc.merge(csc,on="City").merge(invc,on="City").merge(mspc,on="City").merge(ppsfc,on="City").merge(cdomc,on="City").merge(polpc,on="City").merge(pclpc)
neighborhoods = nln.merge(csn,on="City").merge(invn,on="City").merge(mspn,on="City").merge(ppsfn,on="City").merge(cdomn,on="City").merge(polpn,on="City").merge(pclpn,on="City")

cities.to_csv("cities.csv")
neighborhoods.to_csv("neighborhoods.csv")