from parse import parse as parsing


class ReportParser:
    """Parse report files generated by metheorology stations MAWS (2017)"""
    def __init__(self, filename):
        """The filename passed contains the expresion that will be used to parse
        files.

        NOTE:
            Report files generated by EMAs with disdrometer are different that
            they do not have.

        :param filename: filename that contains parse structure

        """
        self.format_file = filename

    def parse(self, filename):
        """Parse the file given using the expresion on the file that was given
        at initialization.
        Returns a dictionary with:

            'date': 'day', 'month', 'year', 'time'
            'name'
            'geo': latitude ('lat'), longitude ('long'), Altitude ('alt') and
                  PsLevel ('pslevel')

            EMAs data, all with the same keys ->
            'airtemp' (Air temperature (C)): Interval in seg ('interval'),
                                             INST ('inst'), average ('avg'),
                                             'max', 'min', 'status'
            'airpressure' (Air pressure (hPa)).
            'relhumidity' (Relative humidity (%))
            'precamount'  (Precipitation amount (mm))
            'windspeed'  (Wind speed (m/s))
            'winddirect' (Wind direction (deg))

            DISDROMETER data, if it is available ('disdrometer'):

            'sensorserial' (Sensor serial number)
            'rainintensity' (Rain intensity 32 bits (mm/h))
            'rainamountaccum' (Rain amount accumulated (mm))
            'codeSYNOP' (Weather code SYNOP wawa Table 4680)
            'radarreflec' (Radar reflectivity (dBz))
            'morvisibility' (MOR visibility in the precipitation (m))
            'kineticenergy' (Kinetic energy (KJ))
            'tempsensor' (Temperature in the sensor (�C))
            'signalamplitude' (Signal amplitude of the laser strip)
            'nparticles' (Number of detected particles)
            'status' (Sensor status)


        :param filename: filename that contains the text to parse
        """
        par_file = self.format_file
        file_to_parse = filename
        # The rep file is a file encoded to latin-1
        with open(format_file, 'r', encoding='latin-1') as rep:
            parsing_struct = ""
            for r in rep:
                parsing_struct += r

        with open(file_to_parse, 'r', encoding='latin-1') as rep:
            for_parse = ""
            for r in rep:
                for_parse += r

        parsed = parsing(parsing_struct, for_parse)
        data = self._clean(parsed.named)
        return data

    def _clean(self, data):
        for key in data.keys():
            if key != 'name':
                for key2 in data[key].keys():
                    value = data[key][key2]
                    value = value.replace(' ', '').replace('\t', '')
                    if key2 != 'status' and key != 'date':
                        value = float(value)
                    data[key][key2] = value
        return data
