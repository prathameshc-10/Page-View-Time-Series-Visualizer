"""Generate the three page-view visualizations."""
import matplotlib.pyplot as plt
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

if __name__ == "__main__":
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()
    plt.show()
