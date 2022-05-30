#!/usr/bin/env python3

import datetime
import fileinput
import re
import sys
import pytz

UTC = pytz.utc

p = re.compile(r"""^
        (?P<day>\d{2}):
        (?P<month>\d{2}):
        (?P<year>\d{4}),
        (?P<hour>\d{2}):
        (?P<minute>\d{2}):
        (?P<second>\d{2}),
        (?P<julianday>\d{1,3}),
        (?P<julianday_fraction>\d{1,3}.\d{6}),
        (?P<AOD1640>\d{1,2}.\d{6}|-999.000000),
        (?P<AOD1020>\d{1,2}.\d{6}|-999.000000),
        (?P<AOD870>\d{1,2}.\d{6}|-999.000000),
        (?P<AOD865>\d{1,2}.\d{6}|-999.000000),
        (?P<AOD779>\d{1,2}.\d{6}|-999.000000),
        (?P<AOD675>\d{1,2}.\d{6}|-999.000000),
        (?P<AOD667>\d{1,2}.\d{6}|-999.000000),
        (?P<AOD620>\d{1,2}.\d{6}|-999.000000),
        (?P<AOD560>\d{1,2}.\d{6}|-999.000000),
        (?P<AOD555>\d{1,2}.\d{6}|-999.000000),
        (?P<AOD551>\d{1,2}.\d{6}|-999.000000),
        (?P<AOD532>\d{1,2}.\d{6}|-999.000000),
        (?P<AOD531>\d{1,2}.\d{6}|-999.000000),
        (?P<AOD510>\d{1,2}.\d{6}|-999.000000),
        (?P<AOD500>\d{1,2}.\d{6}|-999.000000),
        (?P<AOD490>\d{1,2}.\d{6}|-999.000000),
        (?P<AOD443>\d{1,2}.\d{6}|-999.000000),
        (?P<AOD440>\d{1,2}.\d{6}|-999.000000),
        (?P<AOD412>\d{1,2}.\d{6}|-999.000000),
        (?P<AOD400>\d{1,2}.\d{6}|-999.000000),
        (?P<AOD380>\d{1,2}.\d{6}|-999.000000),
        (?P<AOD340>\d{1,2}.\d{6}|-999.000000),
        (?P<precip_water>\d{1,2}.\d{6}|-999.000000),
        (?P<AOD681>\d{1,2}.\d{6}|-999.000000),
        (?P<AOD709>\d{1,2}.\d{6}|-999.000000),
        (?P<AODEmpty0>\d{1,2}.\d{6}|-999.000000),
        (?P<AODEmpty1>\d{1,2}.\d{6}|-999.000000),
        (?P<AODEmpty2>\d{1,2}.\d{6}|-999.000000),
        (?P<AODEmpty3>\d{1,2}.\d{6}|-999.000000),
        (?P<AODEmpty4>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar1640>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar1020>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar870>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar865>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar779>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar675>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar667>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar620>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar560>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar555>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar551>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar532>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar531>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar510>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar500>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar490>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar443>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar440>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar412>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar400>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar380>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar340>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar_precip_water>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar681>\d{1,2}.\d{6}|-999.000000),
        (?P<tvar709>\d{1,2}.\d{6}|-999.000000),
        (?P<tvarEmpty0>\d{1,2}.\d{6}|-999.000000),
        (?P<tvarEmpty1>\d{1,2}.\d{6}|-999.000000),
        (?P<tvarEmpty2>\d{1,2}.\d{6}|-999.000000),
        (?P<tvarEmpty3>\d{1,2}.\d{6}|-999.000000),
        (?P<tvarEmpty4>\d{1,2}.\d{6}|-999.000000),
        (?P<AE440_870>\d{1,2}.\d{6}|-999.000000),
        (?P<AE380_500>\d{1,2}.\d{6}|-999.000000),
        (?P<AE440_675>\d{1,2}.\d{6}|-999.000000),
        (?P<AE500_870>\d{1,2}.\d{6}|-999.000000),
        (?P<AE340_400>\d{1,2}.\d{6}|-999.000000),
        (?P<AE_polar440_675>\d{1,2}.\d{6}|-999.000000),
                lev(?P<datalevel>15|20),
                (?P<instrument_number>\d{1,4}),
                (?P<site_name>GasLab_SJ_CostaRica),
                (?P<latitude>-?\d{1,2}.\d{6}),
                (?P<longitude>-?\d{1,3}.\d{6}),
                (?P<elevation>\d{1,4}.\d{6}),
        (?P<sza>\d{1,2}.\d{6}),
        (?P<optical_airmass>\d{1,2}.\d{6}),
        (?P<sensor_temp>\d{1,2}.\d{6}),
        (?P<ozone_dobson>\d{1,3}.\d{6}),
        (?P<no2_dobson>\d{1,3}.\d{6}),
                (?P<day_lastprocessed>\d{2}):
                (?P<month_lastprocessed>\d{2}):
        (?P<year_lastprocessed>\d{4}),
        (?P<number_of_wavelengths>\d{1,4}),
        .*
        """, re.VERBOSE)

for line in fileinput.input(sys.argv[1]):

    m = p.match(line)

    if m:
        try:
            if (m.group('AOD440') == '-999.000000'):
                # nothing worth looking at here!
                continue
            else:
                day = int(m.group('day'))
                month = int(m.group('month'))
                year = int(m.group('year'))
                hour = int(m.group('hour'))
                minute = int(m.group('minute'))
                second = int(m.group('second'))
                time = datetime.datetime(year,month,day,hour,minute,second,tzinfo=UTC)
                aod440 = float(m.group('AOD440'))
                aod500 = float(m.group('AOD500'))
                aod675 = float(m.group('AOD675'))
                aod870 = float(m.group('AOD870'))
                aod1020 = float(m.group('AOD1020'))
                lon = float(m.group('longitude'))
                lat = float(m.group('latitude'))
                sza = float(m.group('sza'))

        except (ValueError):
            sys.stderr.write("ValueError!\n")
            continue

        outstring = f"{time:%Y-%m-%dT%H:%M:%S} {aod440} {aod500} {aod675} {aod870} {aod1020}"
        print(outstring)
