#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile


class BoostPackageToolsConan(ConanFile):
    name = "boost_package_tools"
    version = "1.66.0"
    url = "https://github.com/bincrafters/conan-boost-package-tools"
    description = "Shared python code used in other Conan recipes for the Boost libraries"
    license = "MIT"
    exports = "boost_package_tools.py", "LICENSE.md"
    
    def package(self):
        self.copy('boost_package_tools.py')
        self.copy('LICENSE.md')

    def package_info(self):
        self.env_info.PYTHONPATH.append(self.package_folder)
    
    