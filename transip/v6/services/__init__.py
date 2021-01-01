# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Roald Nefs <info@roaldnefs.com>
#
# This file is part of python-transip.

# python-transip is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# python-transip is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with python-transip.  If not, see <https://www.gnu.org/licenses/>.

from transip.v6.services.availability_zone import (  # noqa: 401
    AvailabilityZoneService, AvailabilityZone
)
from transip.v6.services.domain import (  # noqa: 401
    DomainService, Domain, 
    WhoisContactService, WhoisContact,
    NameserverService, Nameserver,
    DnsEntryService, DnsEntry
)
from transip.v6.services.invoice import (  # noqa: 401
    InvoiceService, Invoice
)
from transip.v6.services.ssh_key import (  # noqa: 401
    SshKeyService, SshKey
)
from transip.v6.services.vps import (  # noqa: 401
    VpsService, Vps
)
