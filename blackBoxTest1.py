import subprocess
import os
import logging


logging.basicConfig(level=logging.DEBUG)
testcases = ['./testcases/testcase1']
for case in testcases:
    with open(case, 'r') as file:
        num_in, num_out = list(map(int, file.readline().strip().split()))
        content_in = ""
        for i in range(num_in):
            content_in = content_in + file.readline()
        content_out = ""
        for j in range(num_out):
            content_out = content_out + file.readline()
        rlt = subprocess.run(['c:/Program Files/python311/python',  'sampleProgram.py'],
                             input=content_in.encode('utf-8'), capture_output=True, timeout=10, check=True)
        output = rlt.stdout.decode('utf-8').split()
        logging.debug(output)
        expect = content_out.split()
        logging.debug(expect)
        if output == expect:
            print(f"pass {os.path.basename(case)}")
        else:
            print(f"fail {os.path.basename(case)}")
