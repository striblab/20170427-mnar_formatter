#Load .csvs
LOAD DATA LOCAL INFILE 'neighborhoods.csv' 
INTO TABLE neighborhoods
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE 'cities.csv' 
INTO TABLE cities
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

#########################################################################

#Normalize by year
CREATE TABLE cities_by_year
SELECT id, locale, '2003' as yr, `NL-2003` as NL, `CS-2003` as CS, `INV-2003` as INV, `MSP-2003` as MSP, `PPSF-2003` as PPSF, `CDOM-2003` as CDOM, `POLP-2003` as POLP, `PCLP-2003` as PCLP
FROM cities
UNION
SELECT id, locale, '2004' as yr, `NL-2004` as NL, `CS-2004` as CS, `INV-2004` as INV, `MSP-2004` as MSP, `PPSF-2004` as PPSF, `CDOM-2004` as CDOM, `POLP-2004` as POLP, `PCLP-2004` as PCLP
FROM cities
UNION
SELECT id, locale, '2005' as yr, `NL-2005` as NL, `CS-2005` as CS, `INV-2005` as INV, `MSP-2005` as MSP, `PPSF-2005` as PPSF, `CDOM-2005` as CDOM, `POLP-2005` as POLP, `PCLP-2005` as PCLP
FROM cities
UNION
SELECT id, locale, '2006' as yr, `NL-2006` as NL, `CS-2006` as CS, `INV-2006` as INV, `MSP-2006` as MSP, `PPSF-2006` as PPSF, `CDOM-2006` as CDOM, `POLP-2006` as POLP, `PCLP-2006` as PCLP
FROM cities
UNION
SELECT id, locale, '2007' as yr, `NL-2007` as NL, `CS-2007` as CS, `INV-2007` as INV, `MSP-2007` as MSP, `PPSF-2007` as PPSF, `CDOM-2007` as CDOM, `POLP-2007` as POLP, `PCLP-2007` as PCLP
FROM cities
UNION
SELECT id, locale, '2008' as yr, `NL-2008` as NL, `CS-2008` as CS, `INV-2008` as INV, `MSP-2008` as MSP, `PPSF-2008` as PPSF, `CDOM-2008` as CDOM, `POLP-2008` as POLP, `PCLP-2008` as PCLP
FROM cities
UNION
SELECT id, locale, '2009' as yr, `NL-2009` as NL, `CS-2009` as CS, `INV-2009` as INV, `MSP-2009` as MSP, `PPSF-2009` as PPSF, `CDOM-2009` as CDOM, `POLP-2009` as POLP, `PCLP-2009` as PCLP
FROM cities
UNION
SELECT id, locale, '2010' as yr, `NL-2010` as NL, `CS-2010` as CS, `INV-2010` as INV, `MSP-2010` as MSP, `PPSF-2010` as PPSF, `CDOM-2010` as CDOM, `POLP-2010` as POLP, `PCLP-2010` as PCLP
FROM cities
UNION
SELECT id, locale, '2011' as yr, `NL-2011` as NL, `CS-2011` as CS, `INV-2011` as INV, `MSP-2011` as MSP, `PPSF-2011` as PPSF, `CDOM-2011` as CDOM, `POLP-2011` as POLP, `PCLP-2011` as PCLP
FROM cities
UNION
SELECT id, locale, '2012' as yr, `NL-2012` as NL, `CS-2012` as CS, `INV-2012` as INV, `MSP-2012` as MSP, `PPSF-2012` as PPSF, `CDOM-2012` as CDOM, `POLP-2012` as POLP, `PCLP-2012` as PCLP
FROM cities
UNION
SELECT id, locale, '2013' as yr, `NL-2013` as NL, `CS-2013` as CS, `INV-2013` as INV, `MSP-2013` as MSP, `PPSF-2013` as PPSF, `CDOM-2013` as CDOM, `POLP-2013` as POLP, `PCLP-2013` as PCLP
FROM cities
UNION
SELECT id, locale, '2014' as yr, `NL-2014` as NL, `CS-2014` as CS, `INV-2014` as INV, `MSP-2014` as MSP, `PPSF-2014` as PPSF, `CDOM-2014` as CDOM, `POLP-2014` as POLP, `PCLP-2014` as PCLP
FROM cities
UNION
SELECT id, locale, '2015' as yr, `NL-2015` as NL, `CS-2015` as CS, `INV-2015` as INV, `MSP-2015` as MSP, `PPSF-2015` as PPSF, `CDOM-2015` as CDOM, `POLP-2015` as POLP, `PCLP-2015` as PCLP
FROM cities
UNION
SELECT id, locale, '2016' as yr, `NL-2016` as NL, `CS-2016` as CS, `INV-2016` as INV, `MSP-2016` as MSP, `PPSF-2016` as PPSF, `CDOM-2016` as CDOM, `POLP-2016` as POLP, `PCLP-2016` as PCLP
FROM cities;

CREATE TABLE neighborhoods_by_year
SELECT id, locale, '2003' as yr, `NL-2003` as NL, `CS-2003` as CS, `INV-2003` as INV, `MSP-2003` as MSP, `PPSF-2003` as PPSF, `CDOM-2003` as CDOM, `POLP-2003` as POLP, `PCLP-2003` as PCLP
FROM neighborhoods
UNION
SELECT id, locale, '2004' as yr, `NL-2004` as NL, `CS-2004` as CS, `INV-2004` as INV, `MSP-2004` as MSP, `PPSF-2004` as PPSF, `CDOM-2004` as CDOM, `POLP-2004` as POLP, `PCLP-2004` as PCLP
FROM neighborhoods
UNION
SELECT id, locale, '2005' as yr, `NL-2005` as NL, `CS-2005` as CS, `INV-2005` as INV, `MSP-2005` as MSP, `PPSF-2005` as PPSF, `CDOM-2005` as CDOM, `POLP-2005` as POLP, `PCLP-2005` as PCLP
FROM neighborhoods
UNION
SELECT id, locale, '2006' as yr, `NL-2006` as NL, `CS-2006` as CS, `INV-2006` as INV, `MSP-2006` as MSP, `PPSF-2006` as PPSF, `CDOM-2006` as CDOM, `POLP-2006` as POLP, `PCLP-2006` as PCLP
FROM neighborhoods
UNION
SELECT id, locale, '2007' as yr, `NL-2007` as NL, `CS-2007` as CS, `INV-2007` as INV, `MSP-2007` as MSP, `PPSF-2007` as PPSF, `CDOM-2007` as CDOM, `POLP-2007` as POLP, `PCLP-2007` as PCLP
FROM neighborhoods
UNION
SELECT id, locale, '2008' as yr, `NL-2008` as NL, `CS-2008` as CS, `INV-2008` as INV, `MSP-2008` as MSP, `PPSF-2008` as PPSF, `CDOM-2008` as CDOM, `POLP-2008` as POLP, `PCLP-2008` as PCLP
FROM neighborhoods
UNION
SELECT id, locale, '2009' as yr, `NL-2009` as NL, `CS-2009` as CS, `INV-2009` as INV, `MSP-2009` as MSP, `PPSF-2009` as PPSF, `CDOM-2009` as CDOM, `POLP-2009` as POLP, `PCLP-2009` as PCLP
FROM neighborhoods
UNION
SELECT id, locale, '2010' as yr, `NL-2010` as NL, `CS-2010` as CS, `INV-2010` as INV, `MSP-2010` as MSP, `PPSF-2010` as PPSF, `CDOM-2010` as CDOM, `POLP-2010` as POLP, `PCLP-2010` as PCLP
FROM neighborhoods
UNION
SELECT id, locale, '2011' as yr, `NL-2011` as NL, `CS-2011` as CS, `INV-2011` as INV, `MSP-2011` as MSP, `PPSF-2011` as PPSF, `CDOM-2011` as CDOM, `POLP-2011` as POLP, `PCLP-2011` as PCLP
FROM neighborhoods
UNION
SELECT id, locale, '2012' as yr, `NL-2012` as NL, `CS-2012` as CS, `INV-2012` as INV, `MSP-2012` as MSP, `PPSF-2012` as PPSF, `CDOM-2012` as CDOM, `POLP-2012` as POLP, `PCLP-2012` as PCLP
FROM neighborhoods
UNION
SELECT id, locale, '2013' as yr, `NL-2013` as NL, `CS-2013` as CS, `INV-2013` as INV, `MSP-2013` as MSP, `PPSF-2013` as PPSF, `CDOM-2013` as CDOM, `POLP-2013` as POLP, `PCLP-2013` as PCLP
FROM neighborhoods
UNION
SELECT id, locale, '2014' as yr, `NL-2014` as NL, `CS-2014` as CS, `INV-2014` as INV, `MSP-2014` as MSP, `PPSF-2014` as PPSF, `CDOM-2014` as CDOM, `POLP-2014` as POLP, `PCLP-2014` as PCLP
FROM neighborhoods
UNION
SELECT id, locale, '2015' as yr, `NL-2015` as NL, `CS-2015` as CS, `INV-2015` as INV, `MSP-2015` as MSP, `PPSF-2015` as PPSF, `CDOM-2015` as CDOM, `POLP-2015` as POLP, `PCLP-2015` as PCLP
FROM neighborhoods
UNION
SELECT id, locale, '2016' as yr, `NL-2016` as NL, `CS-2016` as CS, `INV-2016` as INV, `MSP-2016` as MSP, `PPSF-2016` as PPSF, `CDOM-2016` as CDOM, `POLP-2016` as POLP, `PCLP-2016` as PCLP
FROM neighborhoods