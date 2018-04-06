#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-

import lzma
import tarfile
from contextlib import closing
import time

i = 1

while(True):
	while(i < 42):
		with lzma.open(str(i) + ".tar.xz") as f:
			with tarfile.open(fileobj=f) as tar:
				content = tar.extractall('.')
			print("unzip %s" % str(i) + ".tar.xz")
			time.sleep(1)
		i+=1
	i=1