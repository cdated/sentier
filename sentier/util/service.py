import os
import sys
from pathlib import PurePath

from sentier.util.discovery import get_dev_port


class Service:
    def __init__(self, name_or_file: str):
        if os.path.sep in name_or_file:
            # This is the __file__ of the caller, so compute the service name.
            rparts = list(reversed(PurePath(name_or_file).parts))
            self._name = ".".join(reversed(rparts[1 : rparts.index("sentier") + 1]))
        else:
            self._name = name_or_file

    def run_manage(self):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{self._name}.settings")
        args = sys.argv
        if len(sys.argv) == 2 and sys.argv[1] == "runserver":
            args += ["--noreload"]
            # If no port was provided, use the dev port for this service.
            dev_port = get_dev_port(self._name)
            args += [f"{dev_port}"]
        from django.core.management import execute_from_command_line

        execute_from_command_line(args)
