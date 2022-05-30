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
        (?P<AOD500>\d{1,2}.\d{6}|-999.000000),
        (?P<tau_f>\d{1,2}.\d{6}|-999.000000),
        (?P<tau_c>\d{1,2}.\d{6}|-999.000000),
        (?P<fmf>\d{1,2}.\d{6}|-999.000000),
        .*
        """, re.VERBOSE)

for line in fileinput.input(sys.argv[1]):

    m = p.match(line)

    if m:
        try:
            if (m.group('fmf') == '-999.000000'):
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
                tau_f = float(m.group('tau_f'))
                tau_c = float(m.group('tau_c'))
                fmf = float(m.group('fmf'))

        except (ValueError):
            sys.stderr.write("ValueError!\n")
            continue

        # we cheat here by making the dates of all the data the same
        outstring = f"2020-01-01T{time:%H:%M:%S} {tau_f} {tau_c} {fmf}" 
        print(outstring)
