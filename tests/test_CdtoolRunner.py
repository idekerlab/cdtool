#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `cdtool` package."""


import unittest
from cdtool.runner import CdtoolRunner


class TestCdtoolrunner(unittest.TestCase):
    """Tests for `cdtool` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_constructor(self):
        """Tests constructor"""
        myobj = CdtoolRunner(0)

        self.assertIsNotNone(myobj)

    def test_run(self):
        """ Tests run()"""
        myobj = CdtoolRunner(4)
        self.assertEqual(4, myobj.run())
