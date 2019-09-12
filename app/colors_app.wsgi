#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/usr/local/apache2/htdocs/app")

from colors_app import app as application
