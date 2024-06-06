import io
import sys
import inspect
from .unittest_config import (
    Config,
    default_config
)

class UnittestManager():
    def __init__(self, config=None):
        if config is None:
            config = default_config
        else:
            config = Config(config)

        self.config:Config = config

    def print_out_SetUp(self):
        if self.config.print_out == True:
            self.capturedOutput = io.StringIO()  
            sys.stdout = self.capturedOutput
            print("\n")
        else:
            sys.stdout = self.capturedOutput

    def print_out_TearDown(self):
        if self.config.print_out == True:
            sys.stdout = sys.__stdout__
            print(self.capturedOutput.getvalue()) 
        else:
            pass

    def run_SetUps(self):
        """Run all methods that end with 'SetUp' in the given class instance."""
        for name, method in inspect.getmembers(self, predicate=inspect.ismethod):
            if name.endswith("SetUp"):
                method()

    def run_TearDowns(self):
        """Run all methods that end with 'TearDown' in the given class instance."""
        for name, method in inspect.getmembers(self, predicate=inspect.ismethod):
            if name.endswith("TearDown"):
                method()
