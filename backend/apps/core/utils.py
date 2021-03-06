# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2022, Boston Venture Studio, Inc - https://www.bvs.net/
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import uuid
from datetime import datetime


def populate_slug_for_multiple_locations(locations):
    slug = str(uuid.uuid4())[:6]
    for location in locations:
        if not location.get('slug'):
            location['slug'] = slug
    return locations
