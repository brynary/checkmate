"""
This file is part of checkmate, a meta code checker written in Python.

Copyright (C) 2015 Andreas Dewes, QuantifiedCode UG

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from .commands.analyze import Command as AnalyzeCommand
from .commands.diff import Command as DiffCommand
from .commands.log import Command as LogCommand
from .commands.init import Command as InitCommand
from .commands.reset import Command as ResetCommand
from .commands.update_stats import Command as UpdateStatsCommand

from .models import GitProject,GitSnapshot,GitFileRevision

commands = {
    'analyze' : AnalyzeCommand,
    'diff' : DiffCommand,
    'init' : InitCommand,
    'log' : LogCommand,
    'reset' : ResetCommand,
    'update_stats' : UpdateStatsCommand
}

models = {
    'GitProject' : GitProject,
    'GitFileRevision' : GitFileRevision,
    'GitSnapshot' : GitSnapshot,
}

top_level_commands = {} 