import os
import itertools
from ofxstatement.plugin import list_plugins


def files_in_dirs(directories):
   curdir = os.getcwd()
   files = []
   for d in directories:
      pth = os.path.expanduser(d)
      files.extend((pth  + fn for fn in os.listdir(pth) if fn.endswith(".csv")))
   return files
