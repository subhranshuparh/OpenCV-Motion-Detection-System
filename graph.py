import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource, SingleIntervalTicker
from bokeh.layouts import layout
from bokeh.models import Div
from bokeh.io import curdoc
from bokeh.themes import Theme

# Read from CSV
df = pd.read_csv("Times.csv")

if df.empty:
    print("No motion data found in Times.csv. Run app1.py first.")
    exit()

# Convert datetime columns
df["Start"] = pd.to_datetime(df["Start"])
df["End"] = pd.to_datetime(df["End"])

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

# Calculate duration in seconds for display
df["Duration"] = (df["End"] - df["Start"]).dt.total_seconds().round(2).astype(str) + "s"

cds = ColumnDataSource(df)

# Responsive figure — sizing_mode fills the browser window
p = figure(
    x_axis_type='datetime',
    height=400,
    sizing_mode="stretch_width",   # stretches horizontally to fill browser
    title="Motion Detection Timeline",
    toolbar_location="above",
    tools="pan,wheel_zoom,box_zoom,reset,save"
)

# Styling
p.title.text_font_size = "18px"
p.title.text_font_style = "bold"
p.title.align = "center"

p.xaxis.axis_label = "Time"
p.xaxis.axis_label_text_font_size = "13px"
p.xaxis.major_label_text_font_size = "11px"

p.yaxis.minor_tick_line_color = None
p.yaxis.major_tick_line_color = None
p.yaxis.major_label_text_color = None   # hide 0/1 y labels
p.yaxis.axis_line_color = None

p.ygrid.ticker = SingleIntervalTicker(interval=1)
p.ygrid.grid_line_color = None

p.xgrid.grid_line_dash = "dashed"
p.xgrid.grid_line_color = "#cccccc"

p.background_fill_color = "#f9f9f9"
p.border_fill_color = "#ffffff"

p.y_range.start = -0.1
p.y_range.end = 1.3

# Hover tool
hover = HoverTool(
    tooltips=[
        ("Start",    "@Start_string"),
        ("End",      "@End_string"),
        ("Duration", "@Duration"),
    ]
)
p.add_tools(hover)

# Motion bars
p.quad(
    left="Start",
    right="End",
    bottom=0,
    top=1,
    color="#2ecc71",
    line_color="#27ae60",
    line_width=1,
    alpha=0.85,
    source=cds,
    legend_label="Motion Detected"
)

p.legend.location = "top_right"
p.legend.label_text_font_size = "12px"

# Summary stats header
total_events = len(df)
total_duration = (df["End"] - df["Start"]).dt.total_seconds().sum().round(2)

header = Div(text=f"""
    <div style="
        font-family: Arial, sans-serif;
        padding: 12px 20px;
        background: #2ecc71;
        color: white;
        border-radius: 6px;
        margin-bottom: 10px;
        display: flex;
        gap: 40px;
        font-size: 15px;
    ">
        <span><b>Total Motion Events:</b> {total_events}</span>
        <span><b>Total Motion Duration:</b> {total_duration}s</span>
        <span><b>Date:</b> {df['Start'].dt.date.iloc[0]}</span>
    </div>
""", sizing_mode="stretch_width")

page_layout = layout(
    [header],
    [p],
    sizing_mode="stretch_width"
)

output_file("Graph1.html", title="Motion Detection Graph")
show(page_layout)