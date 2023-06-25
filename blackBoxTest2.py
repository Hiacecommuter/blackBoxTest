import subprocess
import os
import logging


logging.basicConfig(level=logging.DEBUG)
testcases = ['./testcases/testcase1']
with subprocess.Popen(
    ['c:/Program Files/python311/python', 'sampleProgram.py'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
) as process:
    for case in testcases:
        with open(case, 'r') as file:
            num_in, num_out = list(map(int, file.readline().strip().split()))
            content_in = ""
            for i in range(num_in):
                content_in = content_in + file.readline()
            content_out = ""
            for j in range(num_out):
                content_out = content_out + file.readline()
            stdout, stderr = process.communicate(
                input=content_in.encode('utf-8'), timeout=10
            )

            output = stdout.decode('utf-8').split()
            logging.debug(output)
            expect = content_out.split()
            logging.debug(expect)
            if output == expect:
                print(f"pass {os.path.basename(case)}")
            else:
                print(f"fail {os.path.basename(case)}")
