import pygal
import pandas as pd
from pygal.style import Style
from pygal.style import DefaultStyle

def line_chart_24h(df):

    temperature_list = df["Temperature"].tolist()
    humidity_list = df["Humidity"].tolist()

    x_labels = []
    for time in df.Timestamp:
        m = time[11:16]
        x_labels.append(m)
    
    
    #x_labels = df["Timestamp"].tolist()

    # Moving Average
    temperature_list_moving = df["Temperature"].rolling(window=3).mean().tolist()
    humidity_list_moving = df["Humidity"].rolling(window=3).mean().tolist()

    # Chart Section
    costum_style = Style(   
        font_family='googlefont:Raleway', 
        background = 'transparent',
        plot_background = 'transparent',
        foreground = '#1A3959',
        foreground_strong = '#1A3959',
        foreground_subtle = '#555',
        opacity = '.9',
        opacity_hover = '.9',
        transition = '1s ease-out',
        colors = ('#ff5995', '#cf4878', '#feed6c', '#d1c358'))

    costum_style.label_font_size = 12
    costum_style.legend_font_size = 12

    line_chart_24h = pygal.Line(fill=True,
                            legend_at_bottom=True, 
                            legend_at_bottom_columns=2,
                            show_legend=True,
                            interpolate='cubic', 
                            style=DefaultStyle,
                            margin_bottom=1,
                            height=400,
                            tooltip_border_radius=10,
                            x_label_rotation=45, 
                            x_labels_major_every=24, 
                            show_minor_x_labels=False)

    line_chart_24h.add('Temperature', temperature_list, dots_size=1, show_dots=True)
    line_chart_24h.add('Moving Average Temperature', temperature_list_moving, dots_size=2, show_dots=True)
    line_chart_24h.add('Humidity', humidity_list, dots_size=1, secondary=True, show_dots=True)
    line_chart_24h.add('Moving Average Humidity', humidity_list_moving, dots_size=2, secondary=True)
    line_chart_24h.x_labels = x_labels
    line_chart_24h.value_formatter = lambda x: "%.1f" % x

    return line_chart_24h.render_data_uri()
