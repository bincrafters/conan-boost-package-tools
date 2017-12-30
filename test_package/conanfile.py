#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class TestPackgeConan(ConanFile):
    is_header_only = True
    
    def build(self):
        pass
        
    def test(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            is_header_result = boost_package_tools.is_header_only(self)
            self.output.info("is_header_only: " + str(is_header_result))
