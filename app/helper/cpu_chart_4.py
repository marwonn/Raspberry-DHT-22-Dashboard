import pygal
from pygal.style import Style
from gpiozero import CPUTemperature

def cpu_chart_4():

    cpu = CPUTemperature()
    cpu_temp_4 = int(cpu.temperature)

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
        colors = ('#fc9303', '#b6e354'))

    # costum_style.label_font_size = 32
    # costum_style.legend_font_size = 24
    costum_style.value_font_size = 56

    gauge = pygal.SolidGauge(
        show_legend=False, 
        inner_radius=0.70,
        margin_top=1,
        style= costum_style)

    celsius_formatter = lambda x: '{:.10g}°C'.format(x)

    gauge.add('CPU Temperature', [{'value': cpu_temp_4, 'max_value': 80}],
            formatter=celsius_formatter)
    
    return gauge.render_data_uri()
    