from conans import ConanFile, CMake, RunEnvironment, tools
import os

class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        with tools.environment_append(RunEnvironment(self).vars):
            test_binary = os.path.join("bin","test_package")
            if self.settings.os == "Windows":
                self.run(test_binary)
            elif self.settings.os == "Macos":
                self.run("DYLD_LIBRARY_PATH=%s %s"%(os.environ.get('DYLD_LIBRARY_PATH', ''), test_binary))
            else:
                self.run("LD_LIBRARY_PATH=%s %s"%(os.environ.get('LD_LIBRARY_PATH', ''), test_binary))

