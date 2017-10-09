REALTORS DATA README

The python script reads in data from the MN Association of Realtors using the pandas library. It reads in the file sheet by sheet, assigns new names to the pandas dataframe, and drops the blank cells that were present in the original spreadsheet. For subsequent years, new headers will need to be added. For example, line 3 will need to be:
	nlc = pd.read_excel('City and Nbhd data - annual 2016.xlsx', sheetname="NL-C", names=["", "City", "NL-2003", "NL-2004", "NL-2005", "NL-2006", "NL-2007", "NL-2008", "NL-2009", "NL-2010", "NL-2011", "NL-2012",	"NL-2013", "NL-2014", "NL-2015", "NL-2016", "NL-2017", "NL-Grand Total", "NL-MAX", "NL-All time highs?"], encoding="sys.getfilesystemencoding()")
to account for the next year.

These data frames are merged into two dataframes depending on whether they include data about cities or neighborhoods. From there, they are exported to two CSVs. 

After the CSVs are created, import them into a SQL database and run the query, making sure to add an extra line for the current year. 