#!/usr/bin/env python

# Copyright (c) 2009 Giampaolo Rodola'. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os


from psutil import __version__ as PRJ_VERSION


HERE = os.path.abspath(os.path.dirname(__file__))
HISTORY = os.path.abspath(os.path.join(HERE, '../../HISTORY.rst'))

PRJ_NAME = 'psutil'
PRJ_URLHOME = 'https://github.com/giampaolo/psutil'
PRJ_URLDOC = 'https://github.com/giampaolo/psutil'
PRJ_URLDOWNLOAD = 'https://pypi.python.org/pypi/psutil'
PRJ_URLDOC = 'http://pythonhosted.org/psutil'
PRJ_URLWHATSNEW = 'https://github.com/giampaolo/psutil/blob/master/HISTORY.rst'

template = """\
Hello all,
I'm glad to announce the release of {prj_name} {prj_version}:
{prj_urlhome}

About
=====

psutil (process and system utilities) is a cross-platform library for
retrieving information on running processes and system utilization (CPU,
memory, disks, network) in Python. It is useful mainly for system
monitoring, profiling and limiting process resources and management of
running processes. It implements many functionalities offered by command
line tools such as: ps, top, lsof, netstat, ifconfig, who, df, kill, free,
nice, ionice, iostat, iotop, uptime, pidof, tty, taskset, pmap. It
currently supports Linux, Windows, OSX, Sun Solaris, FreeBSD, OpenBSD and
NetBSD, both 32-bit and 64-bit architectures, with Python versions from 2.6
to 3.5 (users of Python 2.4 and 2.5 may use 2.1.3 version). PyPy is also
known to work.

What's new
==========

{changes}

Links
=====

- Home page: {prj_urlhome}
- Download: {prj_urldownload}
- Documentation: {prj_urldoc}
- What's new: {prj_urlwhatsnew}

--

Giampaolo - http://grodola.blogspot.com
"""


def get_changes():
    """Get the most recent changes for this release by parsing
    HISTORY.rst file.
    """
    with open(HISTORY) as f:
        lines = f.readlines()

    block = []

    # eliminate the part preceding the first block
    for i, line in enumerate(lines):
        line = lines.pop(0)
        if line.startswith('===='):
            break
    lines.pop(0)

    for i, line in enumerate(lines):
        line = lines.pop(0)
        line = line.rstrip()
        if line.startswith('===='):
            break
        block.append(line)

    # eliminate bottom empty lines
    block.pop(-1)
    while not block[-1]:
        block.pop(-1)

    return "\n".join(block)


def main():
    changes = get_changes()
    print(template.format(
        prj_name=PRJ_NAME,
        prj_version=PRJ_VERSION,
        prj_urlhome=PRJ_URLHOME,
        prj_urldownload=PRJ_URLDOWNLOAD,
        prj_urldoc=PRJ_URLDOC,
        prj_urlwhatsnew=PRJ_URLWHATSNEW,
        changes=changes,
    ))

if __name__ == '__main__':
    main()
