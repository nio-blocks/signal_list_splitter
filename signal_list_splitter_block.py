from nio.block.base import Block
from nio.properties import VersionProperty


class SignalListSplitter(Block):

    version = VersionProperty("0.1.1")

    def process_signals(self, signals):
        for signal in signals:
            self.notify_signals([signal])
