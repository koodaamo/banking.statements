"""
banking statements multitool - parse and work with files multiple statement types

Usage:
  statements list-parsers
  statements [check | merge | search] <path> ... [--parser=<parser>] ...
  statements -h | --help
  statements --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""


import sys, time, csv, os, logging, itertools
from docopt import docopt
from ofxstatement.plugin import list_plugins
from ofxstatement import ui, configuration

from .util import files_in_dirs

#from iso3166 import countries
#from dateutil import parser as dateparser

CHECK = 0
MERGE = 1
SEARCH = 2


def statements():

   args = docopt(__doc__, version='platx 1.0')

   if args["list-parsers"]:
      sys.exit("available parsers: %s" % ', '.join([n for (n,p) in list_plugins()]))

   out = ["Trying to " ]

   # command to perform

   if args["check"]:
      command = CHECK
      out.append("check ")
   elif args["merge"]:
      command = MERGE
      out.append("merge ")
   elif args["search"]:
      command = SEARCH
      out.append("search ")

   out.append("statements from ")

   checked = []
   dirs = []
   files = []

   # directories and paths to look for statements in

   for p in args["<path>"]:
      if os.path.isdir(p):
         dirs.append(p)
         checked.append("directory '%s'" % p)
      elif os.path.isfile(p):
         files.append(p)
         checked.append("file '%s'" % p)
      else:
         sys.exit("Failure: no file or directory found at '%s'" % p)
   out.append(', '.join(checked))

   # plugins to use

   plugins = args["--parser"]
   if plugins:
      out.append(" using parser(s) ")
      plugins_out = []
      for p in plugins:
         plugins_out.append("'%s'" % p)
      out.append(', '.join(plugins_out))
   else:
      out.append(" using all available plugins")

   out.append(" ...")

   print(''.join(out))

   files.extend(files_in_dirs(dirs))
   print("Found following files:\n - " + "\n - ".join(files))

   plugin_map = dict(list_plugins())
   if command == CHECK:
      for fn in files:
         for pname in plugins:
            plugin = plugin_map[pname](ui.UI(), {"account":000, "currency":"€"})
            parser = plugin.get_parser(fn)
            statement = parser.parse()
            #for line in statement.lines:
            #   print(line)
      sys.exit("all files parsed ok")
