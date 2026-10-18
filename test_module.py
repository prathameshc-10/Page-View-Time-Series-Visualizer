"""Basic smoke tests for the Page View Time Series Visualizer."""
import os
import unittest
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot


class TimeSeriesVisualizerTests(unittest.TestCase):
    def test_line_plot(self):
        self.assertIsNotNone(draw_line_plot())
        self.assertTrue(os.path.exists("line_plot.png"))

    def test_bar_plot(self):
        self.assertIsNotNone(draw_bar_plot())
        self.assertTrue(os.path.exists("bar_plot.png"))

    def test_box_plot(self):
        self.assertIsNotNone(draw_box_plot())
        self.assertTrue(os.path.exists("box_plot.png"))


if __name__ == "__main__":
    unittest.main()
