import pygal
import pandas as pd
from pygal.style import Style
from pygal.style import DefaultStyle

def bar_chart_per_day(df):

    # Final Dataframe
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df_group_by_date = df.groupby(by=df['Timestamp'].dt.date).mean().round(1)
    
    x_labels_current_date = df_group_by_date.index.values.tolist()
    average_temp_day = df_group_by_date["Temperature"].tolist()
    average_hum_day = df_group_by_date["Humidity"].tolist()

    # Chart Section
    costum_style = Style(   
        font_family='googlefont:Raleway', 
        background = 'transparent',
        plot_background = 'transparent',
        foreground = '#1A3959',
        foreground_strong = '#1A3959',
        foreground_subtle = '#555',
        opacity = '.5',
        opacity_hover = '.5',
        transition = '1s ease-out',
        colors = ('#ff5995', '#b6e354', '#feed6c'))

    costum_style.label_font_size = 12
    costum_style.legend_font_size = 12

    bar_chart = pygal.Bar(fill=False,
                            print_values=True,
                            rounded_bars=20,
                            range=(12, 35),
                            secondary_range=(40, 80),
                            interpolate='cubic', 
                            style=DefaultStyle,
                            show_legend=False,
                            margin_top=1,
                            tooltip_border_radius=10,
                            x_label_rotation=45 
                            )

    bar_chart.add('Temperature', average_temp_day)
    bar_chart.add('Humidity', average_hum_day, range=(40, 80), secondary=True)
    bar_chart.x_labels = x_labels_current_date
    bar_chart.value_formatter = lambda x: "%.1f" % x

    return bar_chart.render_data_uri()
