from flask import Flask, render_template
from helper.getDatabase import get_database
from helper.database2pandas import build_df_from_db as d2p
from helper.gauge_graph_current import gauge_graph_current
from helper.line_chart_24h import line_chart_24h
from helper.bar_chart import bar_chart_per_day
from helper.cpu_chart_zero import cpu_chart_zero
# from helper.cpu_chart_4 import cpu_chart_4

app = Flask(__name__)

@app.route('/dashboard', methods=['GET'])
def landing():
    get_database()
    df, cpu_temp = d2p()
    last_updated_on = str((df["Timestamp"].max())[11:16])  

    line_chart = line_chart_24h(df)
    gauge_chart = gauge_graph_current(df)
    bar_chart = bar_chart_per_day(df)
    cpu_temp_Z = cpu_chart_zero(cpu_temp)
    # cpu_temp_4 = cpu_chart_4()


    return render_template("dashboard.html", gauge_chart=gauge_chart,
                                             line_chart=line_chart,
                                             bar_chart=bar_chart,
                                             cpu_temp_Z=cpu_temp_Z,
                                             # cpu_temp_4=cpu_temp_4,
                                             last_updated_on=last_updated_on)
   
app.run(host='127.0.0.1',port=8000,debug=True)
# app.run(host='0.0.0.0',port=8000,debug=True)