# coding: utf-8
"""Module constants

ORM de Conta-Corrente: modelos-base.

Copyright (C) 2018 Órama DTVM.

Author: Ruan Seabra <ruan.seabra@orama.com.br>
"""
import pytz

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"

TIMEZONE = pytz.timezone("Brazil/East")

STATUS_IN_PROGRESS = "I"
STATUS_FAILED = "F"
STATUS_CONCLUDED = "C"
TP_STATUS = [STATUS_IN_PROGRESS, STATUS_FAILED, STATUS_IN_PROGRESS]
