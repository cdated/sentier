#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

from sentier.util.service import Service


if __name__ == "__main__":
    Service(__file__).run_manage()
