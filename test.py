#!/usr/bin/env python3

import sys
from subprocess import call, Popen, PIPE, run, STDOUT

RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'
END = '\033[0m'

test_source = open("test.cpp", "w")

template = open("template.cpp").read()
test_file = open("template.test.cpp").read()

previous_line = ""

for line in template.splitlines():
    if ("void solve() {" in previous_line):
        for line2 in test_file.splitlines():
            line2 += "\n"
            test_source.write("    " + line2)
        previous_line = ""
        continue
    line += "\n"
    test_source.write(line)
    previous_line = line
    
test_source.close()

test_source_compile_command = ["g++", "test.cpp" , "-std=gnu++17", "-O2"]
proc_s = run(test_source_compile_command, stderr=PIPE, text=True)
res_str_s = proc_s.stderr
idx_s = res_str_s.find("error")
if idx_s != -1:
    print(RED + "[ERROR] :" + " compile error" + END)

test_source_out = "a.out"
source_command = ["./" + test_source_out]
proc = run(source_command, stdout=PIPE, stderr=PIPE, text=True)

print(proc.stdout)

if proc.returncode != 0:
    print(RED + "[ERROR] :" + " runtime error" + END)
else:
    print(GREEN + "[INFO] : accept test" + END)