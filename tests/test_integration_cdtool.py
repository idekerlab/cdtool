#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Integration Tests for `cdtool` package."""

import os

import unittest
from cdtool import cdtoolcmd

SKIP_REASON = 'CDTOOL_INTEGRATION_TEST ' \
              'environment variable not set, cannot run integration ' \
              'tests'

@unittest.skipUnless(os.getenv('CDTOOL_INTEGRATION_TEST') is not None, SKIP_REASON)
class TestIntegrationCdtool(unittest.TestCase):
    """Tests for `cdtool` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_something(self):
        """Tests parse arguments"""
        self.assertEqual(1, 1)
