import unittest

from nose.plugins.plugintest import PluginTester

from noseachievements.achievements.base import Achievement
from noseachievements.plugin import AchievementsPlugin


def pass_func():
    assert True

def fail_func():
    assert False

def error_func():
    raise Exception

PASS = unittest.FunctionTestCase(pass_func)
FAIL = unittest.FunctionTestCase(fail_func)
ERROR = unittest.FunctionTestCase(error_func)

class TestPlugin(PluginTester, unittest.TestCase):
    activate = '--with-achievements'
    tests = [PASS]
    data = None
    achievements = []

    def setUp(self):
        self.plugin = AchievementsPlugin(self.achievements, self.data,
                                         save_file=None)
        self.plugins = [self.plugin]
        PluginTester.setUp(self)

    def makeSuite(self):
        return unittest.TestSuite(self.tests)

class AlwaysUnlockedAchievement(Achievement):
    title = "Test Achievement"
    subtitle = "Test Subtitle"
    message = "Test Message"

    def finalize(self, data, result):
        data.unlock(self)
