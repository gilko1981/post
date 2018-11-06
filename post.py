# -*- coding: utf-8 -*-
import re

with open('post.txt') as f:
    content = f.read()
    msgs = content.split('\n\n')

taken = {}
not_taken = {}

for msg in msgs:
    m = re.search('([A-Z]{2}\d.+?)[, ]', msg, re.MULTILINE)
    if m:
        code = m.group(1)
        if re.search('תודה', msg, re.MULTILINE):
            taken[code] = msg
        else:
            not_taken[code] = msg
print set(not_taken.keys()) - set(taken.keys())
