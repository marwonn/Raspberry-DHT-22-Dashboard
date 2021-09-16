import pygal
from pygal.style import Style

def gauge_graph_current(df):

    costum_style = Style(   
        font_family='googlefont:Raleway', 
        background = 'transparent',
        plot_background = 'transparent',
        foreground = '#1A3959',
        foreground_strong = '#1A3959',
        foreground_subtle = '#555',
        opacity = '.75',
        opacity_hover = '.75',
        transition = '1s ease-out',
        colors = ('#ff5995', '#b6e354', '#feed6c'))

    # costum_style.label_font_size = 32
    # costum_style.legend_font_size = 24
    costum_style.value_font_size = 56

    last_temp_now = df["Temperature"].iloc[-1]
    last_hum_now = df["Humidity"].iloc[-1]

    gauge = pygal.SolidGauge(
        show_legend=False,
        half_pie=True, 
        inner_radius=0.70,
        margin_top=1,
        style= costum_style)

    percent_formatter = lambda x: '{:.10g}%'.format(x)
    celsius_formatter = lambda x: '{:.10g}°C'.format(x)

    gauge.add('Temperature', [{'value': int(last_temp_now), 'max_value': 45}],
            formatter=celsius_formatter)
    gauge.add('Hummidity', [{'value': int(last_hum_now), 'max_value': 100}],
            formatter=percent_formatter)
    
    return gauge.render_data_uri()
    