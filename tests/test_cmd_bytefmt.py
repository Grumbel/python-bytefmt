# bytefmt - Convert a byte count into a human readable string
# Copyright (C) 2019 Ingo Ruhnke <grumbel@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import contextlib
import io
import unittest

from bytefmt.cmd_bytefmt import main


class CmdByteFmtTestCase(unittest.TestCase):

    def test_cmd_bytefmt(self):
        argvs = [
            (["bytefmt", "12"], "12 B\n"),
            (["bytefmt", "12MiB", "-u", "MB"], "12.58 MB\n"),
            (["bytefmt", "12MB", "-u", "MiB"], "11.44 MiB\n"),
        ]

        for argv, expected in argvs:
            stdout = io.StringIO()
            stderr = io.StringIO()
            with contextlib.redirect_stdout(stdout), \
                 contextlib.redirect_stderr(stderr):
                try:
                    main(argv)
                except SystemExit as ex:
                    self.assertEqual(ex.code, 0)
            self.assertEqual(stdout.getvalue(), expected)
            self.assertEqual(stderr.getvalue(), "")


# EOF #
