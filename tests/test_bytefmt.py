#!/usr/bin/env python3

# bytefmt - Convert a byte count into a human readable string
# Copyright (C) 2018 Ingo Ruhnke <grumbel@gmail.com>
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


import unittest

from bytefmt import dehumanize, humanize


class ByteFmtTestCase(unittest.TestCase):

    def test_dehumanize(self) -> None:
        # basic units
        self.assertEqual(1234, dehumanize("1234"))

        self.assertEqual(1000**0, dehumanize("1B"))
        self.assertEqual(1000**1, dehumanize("1kB"))
        self.assertEqual(1000**2, dehumanize("1MB"))
        self.assertEqual(1000**3, dehumanize("1GB"))
        self.assertEqual(1000**4, dehumanize("1TB"))
        self.assertEqual(1000**5, dehumanize("1PB"))
        self.assertEqual(1000**6, dehumanize("1EB"))
        self.assertEqual(1000**7, dehumanize("1ZB"))
        self.assertEqual(1000**8, dehumanize("1YB"))

        self.assertEqual(1024**1, dehumanize("1KiB"))
        self.assertEqual(1024**2, dehumanize("1MiB"))
        self.assertEqual(1024**3, dehumanize("1GiB"))
        self.assertEqual(1024**4, dehumanize("1TiB"))
        self.assertEqual(1024**5, dehumanize("1PiB"))
        self.assertEqual(1024**6, dehumanize("1EiB"))
        self.assertEqual(1024**7, dehumanize("1ZiB"))
        self.assertEqual(1024**8, dehumanize("1YiB"))

        # space
        self.assertEqual(5*1024**8, dehumanize(" 5YiB"))
        self.assertEqual(5*1024**8, dehumanize("  5YiB  "))
        self.assertEqual(5*1024**8, dehumanize("5YiB  "))
        self.assertEqual(5*1024**8, dehumanize("5  YiB  "))

        # invalid input
        self.assertRaises(Exception, lambda: dehumanize("ABC"))
        self.assertRaises(Exception, lambda: dehumanize("MB"))
        self.assertRaises(Exception, lambda: dehumanize("MB1MB"))
        self.assertRaises(Exception, lambda: dehumanize("1MBa"))
        self.assertRaises(Exception, lambda: dehumanize("1.3.3MB"))

    def test_humanize(self) -> None:
        self.assertEqual("13.92 kB", humanize(13916))
        self.assertEqual("99.91 MB", humanize(99913916))

        self.assertEqual("13.59 KiB", humanize(13916, style="binary"))
        self.assertEqual("95.29 MiB", humanize(99913916, style="binary"))

        self.assertEqual("13.59KiB", humanize(13916, style="binary", compact=True))
        self.assertEqual("95.29MiB", humanize(99913916, style="binary", compact=True))

        self.assertEqual("13.59K", humanize(13916, style="gnu"))
        self.assertEqual("95.29M", humanize(99913916, style="gnu"))

    def test_humanize_line(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()


# EOF #
