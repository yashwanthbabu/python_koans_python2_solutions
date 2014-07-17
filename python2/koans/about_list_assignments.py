#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrayAssignments in the Ruby Koans
#

from runner.koan import *


class AboutListAssignments(Koan):
    def test_non_parallel_assignment(self):
        names = ["John", "Smith"]
        self.assertEqual(["John", "Smith"], names)

    def test_parallel_assignments(self):
        first_name, last_name = ["John", "Smith"]
        self.assertEqual(first_name[:4], first_name)
        self.assertEqual(last_name[0:], last_name)

    def test_parallel_assignments_with_sublists(self):
        first_name, last_name = [["Willie", "Rae"], "Johnson"]
        self.assertEqual(first_name[0:2], first_name)
        self.assertEqual(last_name[0:], last_name)

    def test_swapping_with_parallel_assignment(self):
        first_name = "Roy"
        last_name = "Rob"
        first_name, last_name = last_name, first_name
        self.assertEqual(first_name[:3], first_name)
        self.assertEqual(last_name[:3], last_name)
