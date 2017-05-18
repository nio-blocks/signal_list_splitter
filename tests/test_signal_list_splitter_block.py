from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from ..signal_list_splitter_block import SignalListSplitter


class TestProcessSignalList(NIOBlockTestCase):

    input_signals = [Signal({"hello": "n.io"}),
                     Signal({"hello": "n.io"}),
                     Signal({"hello": "n.io"})]

    def signals_notified(self, block, signals, output_id):
        """override function so that last_notified is list of lists of signals
        notified
        """
        self.last_notified[output_id].append(signals)

    def test_process_signal_list(self):
        """List of signals is split into lists of single signals"""
        blk = SignalListSplitter()
        self.configure_block(blk, {})
        blk.start()
        # one list of signals is processed
        blk.process_signals(self.input_signals)
        blk.stop()
        self.assert_num_signals_notified(len(self.input_signals))
        # and one list of one signal has been notified for each signal
        self.assertEqual(len(self.last_notified[DEFAULT_TERMINAL]),
                         len(self.input_signals))

class TestProcessSignalListOfOne(TestProcessSignalList):

    input_signals = [Signal({"hello": "n.io"})]
