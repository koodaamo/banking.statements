"""
banking statements multitool - parse and work with files multiple statement types

Usage:
  statements list-parsers
  statements (check | merge) <path> ... [--parser=<parser>] ...
  statements search <query> <path> ... [--parser=<parser>] ...
  statements -h | --help
  statements --version

To search, use a "field check value" syntax query, where check is either '=' or 'has',
and field is one of id, date, memo, amount, date_user, payee, check_no, refnum trntype,
or bank_account_to. Value is the value you're looking for.

Options:
  -h --help     Show this screen.
  --version     Show version.

"""


import sys, time, csv, os, logging, itertools
from docopt import docopt
from ofxstatement.plugin import list_plugins
from ofxstatement import ui, configuration

from .util import files_in_dirs, parsed_statements

#from iso3166 import countries
#from dateutil import parser as dateparser

CHECK = "check"
MERGE = "merge"
SEARCH = "search"


def statements():

   args = docopt(__doc__, version='platx 1.0')

   if args["list-parsers"]:
      sys.exit("available parsers: %s" % ', '.join([n for (n,p) in list_plugins()]))

   out = ["\nTrying to " ]

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
   print("\nFound following files to " + command + ":\n\n - " + "\n - ".join(files))

   plugin_map = dict(list_plugins())

   if command == CHECK:
      for s in parsed_statements(files, plugins):
         pass
      sys.exit("all files parsed ok")

   elif command == SEARCH:
      field, op, value = args["<query>"].split()
      field = field.lower()
      value = value.lower()
      op = op.lower()

      matches = False

      for s in parsed_statements(files, plugins):
         for l in s.lines:
            data = getattr(l, field).lower()
            if op.strip() == "has" and value in data:
               print(l)
               matches = True
            elif op.strip() == "=" and value == data:
               print(l)
               matches = True
            else:
               pass
      if not matches:
         print("\nNo search matches.\n")
