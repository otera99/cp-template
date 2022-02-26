#!/usr/bin/env python3

f = open("cp.code-snippets", "w")
f.write("{\n")
f.write("	\"cp\": {\n")
f.write("		\"prefix\": \"cp\",\n")
f.write("		\"body\": [\n")

source = open("template.cpp").read()

previous_line = ""

for source_line in source.splitlines():
    line = "			\""

    # $1の設定
    if previous_line == "void solve() {":
        source_line = "    $1"
    
    for c in source_line:
        if c == '\\':
            line += '\\'
        if c == '\"':
            line += '\\'
            line += '\"'
        else:
            line += c
    line += "\",\n"
    f.write(line)
    previous_line = source_line

f.write("		],\n")
f.write("		\"description\": \"Log output to console\"")
f.write("	}\n")
f.write("}\n")
f.close()

print("[INFO] generate cp.code-snippets")