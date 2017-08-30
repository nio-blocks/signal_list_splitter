from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from ..signal_list_splitter_block import SignalListSplitter


class TestProcessSignalList(NIOBlockTestCase):


    def signals_notified(self, block, signals, output_id):
        """override function so that last_notified is list of lists of signals
        notified
        """
        self.last_notified[output_id].append(signals)

    def test_process_signal_list(self):
        """List of signals is split into lists of single signals"""
        input_signals = [Signal({"hello": "n.io"}),
                         Signal({"hello": "n.io"}),
                         Signal({"hello": "n.io"})]
        blk = SignalListSplitter()
        self.configure_block(blk, {})
        blk.start()
        # one list of signals is processed
        blk.process_signals(input_signals)
        blk.stop()
        self.assert_num_signals_notified(3)
        # and one list of one signal has been notified for each signal
        self.assertEqual(len(self.last_notified[DEFAULT_TERMINAL]), 3)
        for signal_list in self.last_notified[DEFAULT_TERMINAL]:
            self.assertEqual(len(signal_list), 1)
            self.assertEqual(signal_list[0].to_dict(), {
                "hello": "n.io",
            })

    def test_process_signal_list_of_one(self):
        """List of signals is split into lists of single signals"""
        input_signals = [Signal({"hello": "n.io"})]
        blk = SignalListSplitter()
        self.configure_block(blk, {})
        blk.start()
        # one list of signals is processed
        blk.process_signals(input_signals)
        blk.stop()
        self.assert_num_signals_notified(1)
        # and one list of one signal has been notified for each signal
        self.assertEqual(len(self.last_notified[DEFAULT_TERMINAL]), 1)
        for signal_list in self.last_notified[DEFAULT_TERMINAL]:
            self.assertEqual(len(signal_list), 1)
            self.assertEqual(signal_list[0].to_dict(), {
                "hello": "n.io",
            })
