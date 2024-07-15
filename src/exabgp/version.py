import os
import sys
from datetime import datetime

modification_time = modification_time = os.path.getmtime(os.path.abspath(__file__))
date = datetime.fromtimestamp(modification_time)

commit = "unset"
release = "5.0.0-%s+uncontrolled" % date.strftime('%Y%m%d')
json = "5.0.0"
text = "5.0.0"
version = os.environ.get('EXABGP_VERSION', release)

# Do not change the first line as it is parsed by scripts

if sys.version_info.major < 3:
    sys.exit('exabgp requires python3.6 or later')
if sys.version_info.major == 3 and sys.version_info.minor < 6:
    sys.exit('exabgp requires python3.6 or later')


def latest_github():
    import json as json_lib
    import urllib.request

    latest = json_lib.loads(
        urllib.request.urlopen(
            urllib.request.Request(
                'https://api.github.com/repos/exa-networks/exabgp/releases',
                headers={'Accept': 'application/vnd.github.v3+json'},
            )
        ).read()
    )
    return latest[0]['tag_name']


def time_based():
    import datetime

    return datetime.date.today().isoformat().replace('-', '.')


if __name__ == '__main__':
    if version == release:
        version = time_based()
    sys.stdout.write(version)
