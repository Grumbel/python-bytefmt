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


from typing import Dict, Optional

import re
from decimal import Decimal


STYLES = {
    "decimal": (1000, ["B", "kB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]),
    "binary": (1024, ["B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB"]),
    "gnu": (1024, ["", "K", "M", "G", "T", "P", "E", "Z", "Y"])
}


def _init_unit2factor() -> Dict[str, int]:
    lst = {}
    for style in STYLES.values():
        base, units = style
        for i, unit in enumerate(units):
            lst[unit] = base ** i
    return lst


UNIT2FACTOR = _init_unit2factor()


def dehumanize(text: str) -> int:
    """Convert a text string (e.g. "582.5MB") to a byte count. kB=1000, KiB=1024"""

    match = re.match(r"^\s*([0-9]+|[0-9]*\.[0-9]+)\s*([A-Za-z]*)\s*$", text)
    if match:
        value, unit = match.groups()
        if unit == "":
            return int(value)
        elif unit in UNIT2FACTOR:
            return int(Decimal(value) * UNIT2FACTOR[unit])
        else:
            raise Exception(f"unknown unit {unit!r} in {text!r}")
    else:
        raise Exception(f"couldn't interpret {text!r}")


def humanize(byte_count: int, style: str = "decimal", compact: bool = False,
             unit: Optional[str] = None, precision: int = 2) -> str:
    """Returns size formated as a human readable string"""

    count: float = byte_count

    base, units = STYLES[style]
    if unit is None:
        for i, u in enumerate(units):
            if count < 1000 or i == len(units) - 1:
                count_unit = u
                break
            else:
                count /= base
    else:
        for i, u in enumerate(units):
            if unit == u:
                count_unit = u
                break
            else:
                count /= base
        else:
            raise Exception(f"unit is invalid or not in the selected style: {unit}")

    fmt = "{}" if i == 0 else "{:." + str(precision) + "f}"

    if style == "gnu" or compact:
        return (fmt + "{}").format(count, count_unit)
    else:
        return (fmt + " {}").format(count, count_unit)


# EOF #
