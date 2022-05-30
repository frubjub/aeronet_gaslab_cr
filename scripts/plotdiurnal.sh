#!/usr/bin/bash

OUTFILE=diurnal_variation_gaslab.ps
PDFFILE=`basename $OUTFILE .ps`.pdf
PDFROTATE=`basename $OUTFILE ps`_.pdf

. ./colorblindpallet.sh
. ./spectralcolors.sh

gmtset PS_MEDIA=A3 FONT_ANNOT_PRIMARY=12p FONT_LABEL=12p

PROJECTION=X5/5
REGION=2022-01-01T11:00:00/2022-01-31T23:59:59/0/0.5
psbasemap -J$PROJECTION -R$REGION -BWesN -Bx7d+l"Day of Jan" -Byaf0.2+l"AOD 500nm" -K -Y20 > $OUTFILE
./aod_timeseries.py ../jan/20220101_20220131_GasLab_SJ_CostaRica.lev15 | awk '{print $1, $3}' |\
    psxy -J$PROJECTION -R$REGION -W$PLAINRED -Sc0.08c -O -K >> $OUTFILE
#echo 2022-01-15T12:00:00 0.55 Jan | pstext -R$REGION -J$PROJECTION -N -O -K >> $OUTFILE 
REGION=2022-02-01T11:00:00/2022-02-28T23:59:59/0/0.5
psbasemap -J$PROJECTION -R$REGION -BWesN -Bx7d+l"Day of Feb" -Byf0.2 -K -O -X5.2 >> $OUTFILE
./aod_timeseries.py ../feb/20220201_20220228_GasLab_SJ_CostaRica.lev15 | awk '{print $1, $3}' |\
    psxy -J$PROJECTION -R$REGION -W$PLAINRED -Sc0.08c -O -K >> $OUTFILE
REGION=2022-03-01T11:00:00/2022-03-31T23:59:59/0/0.5
psbasemap -J$PROJECTION -R$REGION -BWesN -Bx7d+l"Day of Mar" -Byf0.2 -K -O -X5.2 >> $OUTFILE
./aod_timeseries.py ../mar/20220301_20220331_GasLab_SJ_CostaRica.lev15 | awk '{print $1, $3}' |\
    psxy -J$PROJECTION -R$REGION -W$PLAINRED -Sc0.08c -O -K >> $OUTFILE
REGION=2022-04-01T11:00:00/2022-04-30T23:59:59/0/0.5
psbasemap -J$PROJECTION -R$REGION -BWesN -Bx7d+l"Day of Apr" -Byf0.2 -K -O -X5.2 >> $OUTFILE
./aod_timeseries.py ../apr/20220401_20220430_GasLab_SJ_CostaRica.lev15 | awk '{print $1, $3}' |\
    psxy -J$PROJECTION -R$REGION -W$PLAINRED -Sc0.08c -O -K >> $OUTFILE
REGION=2022-05-01T11:00:00/2022-05-31T23:59:59/0/0.5
psbasemap -J$PROJECTION -R$REGION -BWesN -Bx7d+l"Day of May" -Byf0.2 -K -O -X5.2 >> $OUTFILE
./aod_timeseries.py ../may/20220501_20220531_GasLab_SJ_CostaRica.lev15 | awk '{print $1, $3}' |\
    psxy -J$PROJECTION -R$REGION -W$PLAINRED -Sc0.08c -O -K >> $OUTFILE

PROJECTION=X5
REGION=2020-01-01T11:00:00/2020-01-01T23:59:59/0/0.5
psbasemap -J$PROJECTION -R$REGION -BWesn -Bx3h -Byaf0.2+l"AOD 500nm" -O -K -X-20.8 -Y-6.5 >> $OUTFILE
./aod_diurnal.py ../jan/20220101_20220131_GasLab_SJ_CostaRica.lev15 | awk '{print $1, $3}' |\
    psxy -J$PROJECTION -R$REGION -W$VERMILLION -Sc0.08c -O -K >> $OUTFILE
psbasemap -J$PROJECTION -R$REGION -BWesn -Bx3h -Byf0.2 -O -K -X5.2  >> $OUTFILE
./aod_diurnal.py ../feb/20220201_20220228_GasLab_SJ_CostaRica.lev15 | awk '{print $1, $3}' |\
    psxy -J$PROJECTION -R$REGION -W$VERMILLION -Sc0.08c -O -K >> $OUTFILE
psbasemap -J$PROJECTION -R$REGION -BWesn -Bx3h -Byf0.2 -O -K -X5.2 >> $OUTFILE
./aod_diurnal.py ../mar/20220301_20220331_GasLab_SJ_CostaRica.lev15 | awk '{print $1, $3}' |\
    psxy -J$PROJECTION -R$REGION -W$VERMILLION -Sc0.08c -O -K >> $OUTFILE
psbasemap -J$PROJECTION -R$REGION -BWesn -Bx3h -Byf0.2 -O -K -X5.2 >> $OUTFILE
./aod_diurnal.py ../apr/20220401_20220430_GasLab_SJ_CostaRica.lev15 | awk '{print $1, $3}' |\
    psxy -J$PROJECTION -R$REGION -W$VERMILLION -Sc0.08c -O -K >> $OUTFILE
psbasemap -J$PROJECTION -R$REGION -BWesn -Bx3h -Byf0.2 -O -K -X5.2 >> $OUTFILE
./aod_diurnal.py ../may/20220501_20220531_GasLab_SJ_CostaRica.lev15 | awk '{print $1, $3}' |\
    psxy -J$PROJECTION -R$REGION -W$VERMILLION -Sc0.08c -O -K >> $OUTFILE

PROJECTION=X5
REGION=2020-01-01T11:00:00/2020-01-01T23:59:59/0/1
psbasemap -J$PROJECTION -R$REGION -BWeSn -Bxa3h+l"UTC Time (Jan)" -Byaf0.2+l"Fine-mode fraction 500nm" -O -K -X-20.8 -Y-5.4 >> $OUTFILE
./fmf_diurnal.py ../jan/20220101_20220131_GasLab_SJ_CostaRica.ONEILL_lev15 | awk '{print $1, $4}' |\
    psxy -J$PROJECTION -R$REGION -W$CYAN -Sc0.08c -O -K >> $OUTFILE
psbasemap -J$PROJECTION -R$REGION -BWeSn -Bxa3h+l"UTC Time (Feb)" -Byf0.2 -O -K -X5.2  >> $OUTFILE
./fmf_diurnal.py ../feb/20220201_20220228_GasLab_SJ_CostaRica.ONEILL_lev15 | awk '{print $1, $4}' |\
    psxy -J$PROJECTION -R$REGION -W$CYAN -Sc0.08c -O -K >> $OUTFILE
psbasemap -J$PROJECTION -R$REGION -BWeSn -Bxa3h+l"UTC Time (Mar)" -Byf0.2 -O -K -X5.2 >> $OUTFILE
./fmf_diurnal.py ../mar/20220301_20220331_GasLab_SJ_CostaRica.ONEILL_lev15 | awk '{print $1, $4}' |\
    psxy -J$PROJECTION -R$REGION -W$CYAN -Sc0.08c -O -K >> $OUTFILE
psbasemap -J$PROJECTION -R$REGION -BWeSn -Bxa3h+l"UTC Time (Apr)" -Byf0.2 -O -K -X5.2 >> $OUTFILE
./fmf_diurnal.py ../apr/20220401_20220430_GasLab_SJ_CostaRica.ONEILL_lev15 | awk '{print $1, $4}' |\
    psxy -J$PROJECTION -R$REGION -W$CYAN -Sc0.08c -O -K >> $OUTFILE
psbasemap -J$PROJECTION -R$REGION -BWeSn -Bxa3h+l"UTC Time (May)" -Byf0.2 -O -K -X5.2 >> $OUTFILE
./fmf_diurnal.py ../may/20220501_20220531_GasLab_SJ_CostaRica.ONEILL_lev15 | awk '{print $1, $4}' |\
    psxy -J$PROJECTION -R$REGION -W$CYAN -Sc0.08c -O -K >> $OUTFILE

# closing off the plot
psxy -J$PROJECTION -R$REGION -T -O >> $OUTFILE
psconvert $OUTFILE -A -Tf
