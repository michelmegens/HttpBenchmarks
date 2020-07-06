#
#
#

from conans import ConanFile, CMake
import os


def is_windows():
    return os.name == 'nt'


class AuthService(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def requirements(self):
        if is_windows():
            self.requires("boost/1.73.0")
            self.requires("rapidjson/1.1.0")
        else:
            self.requires("boost/1.73.0")
            self.requires("rapidjson/1.1.0")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()
