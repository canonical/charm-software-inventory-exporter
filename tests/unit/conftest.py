# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.
#
# Learn more about testing at: https://juju.is/docs/sdk/testing
"""Fixture for charm's unit tests."""

import ops.testing
import pytest

from charm import SoftwareInventoryExporterCharm


@pytest.fixture()
def harness() -> ops.testing.Harness[SoftwareInventoryExporterCharm]:
    """Return harness for SoftwareInventoryExporterCharm."""
    ops.testing.SIMULATE_CAN_CONNECT = True
    harness = ops.testing.Harness(SoftwareInventoryExporterCharm)
    harness.begin()

    yield harness

    harness.cleanup()
    ops.testing.SIMULATE_CAN_CONNECT = False
