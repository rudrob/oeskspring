import statistics
import subprocess
import time
from datetime import datetime

import numpy

from .models import Measurement


def create_measurement(jar_name, times, namespace):
    time_numbers = []

    for i in range(times):
        cmd = 'cd ~/oeskspring && java -jar ' + jar_name
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        sanity_counter = 0
        while True:
            sanity_counter += 1
            line = proc.stdout.readline()
            print("test:", line.rstrip())
            if sanity_counter > 5000:
                result_measurement = Measurement()
                result_measurement.jarname = jar_name
                result_measurement.namespace = namespace
                result_measurement.failed = True
                result_measurement.done = True
                result_measurement.save()
                result_measurement.enddate = datetime.now()
                return
            if is_desired_log_line(line):
                append_time_from_desired_line(line, time_numbers)
                break
        proc.terminate()
        kill_proc = subprocess.Popen('kill `jps | grep "' + jar_name + '" | cut -d " " -f 1`', stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE, shell=True)
        time.sleep(5)
    result_measurement = Measurement()
    avg = round(sum(time_numbers) / len(time_numbers), 3)
    median = round(statistics.median(time_numbers), 3)
    stdev = round(statistics.stdev(time_numbers), 3)
    as_np = numpy.array(time_numbers)
    iqr = round(numpy.percentile(as_np, 75, interpolation='higher')
                - numpy.percentile(as_np, 25, interpolation='lower'), 3)
    result_measurement.avg = avg
    result_measurement.median = median
    result_measurement.stdev = stdev
    result_measurement.iqr = iqr
    result_measurement.done = True
    result_measurement.jarname = jar_name
    result_measurement.namespace = namespace
    result_measurement.enddate = datetime.now()
    result_measurement.save()


def is_desired_log_line(line):
    return b'JVM running for' in line


def append_time_from_desired_line(line, time_numbers):
    ind = line.index(b'seconds')
    if line[ind - 6] == b'n':
        time = line[ind - 4: ind - 1]
    else:
        time = line[ind - 6: ind - 1]
    time_numbers.append(float(time))
