

from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Category20
from bokeh.plotting import figure
import math
output_file("colormapped_bars.html")

months = [ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec' ]
failures = [10, 4, 3, 7, 2, 6, 10, 2, 0, 4, 7, 2]
x_pos = [2] * 12
y_pos = [2] * 12
starts = [math.radians(i * 30) for i in range(12)]
ends = [x + math.radians(30) for x in starts]
max_fails = max(failures)
radii = [x / max_fails * 1.8 for x in failures]
colors = Category20[12]

TOOLTIPS = [
    ("Month", "@months"),
    ("Failures", "@failures")
]

failure_source = ColumnDataSource(data=dict(months=months, failures=failures,
                                            x=x_pos, y=y_pos, radius=radii,
                                            start_angle=starts, end_angle=ends,
                                            color=colors))


p = figure(plot_width=400, plot_height=400, x_range=(0, 4), y_range=(0, 4), title="Failures", tooltips=TOOLTIPS)
           #toolbar_location=None, tools="")

p.wedge(x='x', y='y', radius='radius', start_angle='start_angle', end_angle='end_angle',
        color='color', source=failure_source)

p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.xaxis.visible = False
p.yaxis.visible = False


show(p)

