import subprocess
import statistics
import numpy
import time


def create_measurement(jar_name):
    TIMES = 30
    time_numbers = []

    for i in range(TIMES):
        cmd = 'cd ~ && java -jar ' + jar_name
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        while True:
            line = proc.stdout.readline()
            print("test:", line.rstrip())
            if is_desired_log_line(line):
                break
        proc.terminate()
        kill_proc = subprocess.Popen('kill `jps | grep "' + jar_name + '" | cut -d " " -f 1`', stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE, shell=True)
        # time.sleep(5)


    # result_file.write('-------------\n')
    # result_file.write('Average ' + str(round(sum(time_numbers) / len(time_numbers), 3)) + '\n')
    # result_file.write('Median ' + str(round(statistics.median(time_numbers), 3)) + '\n')
    # result_file.write('Standard deviation ' + str(round(statistics.stdev(time_numbers), 3)) + '\n')
    # as_np = numpy.array(time_numbers)
    # iqr = numpy.percentile(as_np, 75, interpolation='higher') - numpy.percentile(as_np, 25, interpolation='lower')
    # result_file.write('Iqr ' + str(round(iqr, 3)) + '\n')

def is_desired_log_line(line):
    return b'Started SpringboottestApplication' in line

def append_time_from_desired_line(line, time_numbers):
    ind = line.index('seconds')
    if line[ind - 6] == 'n':
        time = line[ind - 4: ind - 1]
    else:
        time = line[ind - 6: ind - 1]
    time_numbers.append(float(time))