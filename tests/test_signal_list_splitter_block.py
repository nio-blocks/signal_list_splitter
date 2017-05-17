from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from ..signal_list_splitter_block import SignalListSplitter


class TestTheThings(NIOBlockTestCase):

    def signals_notified(self, block, signals, output_id):
        # override to make list of lists of signals notified
        self.last_notified[output_id].append(signals)

    def test_process_signals(self):
        """List of multiple signals is split into lists of single signals"""
        blk = SignalListSplitter()
        self.configure_block(blk, {})
        blk.start()
        # one list of 3 signals is processed
        blk.process_signals([Signal({"hello": "n.io"}),
                             Signal({"hello": "n.io"}),
                             Signal({"hello": "n.io"})])
        blk.stop()
        self.assert_num_signals_notified(3)
        # and three lists of one signal have been notified
        self.assertEqual(
            len(self.last_notified[DEFAULT_TERMINAL]), 3)
