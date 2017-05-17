from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from ..signal_list_splitter_block import SignalListSplitter


class TestTheThings(NIOBlockTestCase):

    def signals_notified(self, block, signals, output_id):
        self.last_notified[output_id].append(signals)

    def test_process_signals(self):
        """Signals pass through block unmodified."""
        blk = SignalListSplitter()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal({"hello": "n.io"}),
                             Signal({"hello": "n.io"}),
                             Signal({"hello": "n.io"})])
        blk.stop()
        self.assert_num_signals_notified(3)
        self.assertEqual(
            len(self.last_notified[DEFAULT_TERMINAL]), 3)
