import os
import itertools
from ofxstatement.plugin import list_plugins
from ofxstatement import ui


def files_in_dirs(directories):
   curdir = os.getcwd()
   files = []
   for d in directories:
      pth = os.path.expanduser(d)
      files.extend((pth  + fn for fn in os.listdir(pth) if fn.endswith(".csv")))
   return files


def parsed_statements(filepaths, plugins):

   plugin_map = dict(list_plugins())

   for fp in filepaths:
      for pname in plugins:
         plugin = plugin_map[pname](ui.UI(), {"account":000, "currency":"€"})
         parser = plugin.get_parser(fp)
         yield parser.parse()
