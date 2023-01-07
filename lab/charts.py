from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5 import QtCore, QtGui


def create_trend_chart(
    ui_obj,
    bg_color="#000000",
    text_color="#FFFFFF",
    axisX_title="Length",
    axisX_range=20,
    axisY_title="Width",
    axisY_range=5,
    trend_name="Width",
    trend_color="#FFFF00",
    setpoint_name="Set Point",
    setpoint_color="#008000",
    setpoint_value=0,
    threshold_name="Threshold",
    threshold_color="#FF0000",
    threshold_value=2,
    line_width=2,
):
    """this function is used to create width trend chart on ui

    :param bg_color: _description_, defaults to colors.COLORS['black']
    :param text_color: _description_, defaults to colors.COLORS['white']
    :param axisX_title: _description_, defaults to 'Length'
    :param axisX_range: _description_, defaults to 20
    :param axisY_title: _description_, defaults to 'Width'
    :param axisY_range: _description_, defaults to 5
    :param trend_name: _description_, defaults to 'Width'
    :param trend_color: _description_, defaults to colors.COLORS['warning_yellow']
    :param setpoint_name: _description_, defaults to 'Set Point'
    :param setpoint_color: _description_, defaults to colors.COLORS['success_green']
    :param setpoint_value: _description_, defaults to 0
    :param threshold_name: _description_, defaults to 'Threshold'
    :param threshold_color: _description_, defaults to colors.COLORS['failed_red']
    :param threshold_value: _description_, defaults to 2
    :param line_width: _description_, defaults to 2
    """

    # create main chart
    ui_obj.chart = QChart()
    ui_obj.chart.createDefaultAxes()
    ui_obj.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
    ui_obj.chart.setAnimationDuration(1000)
    ui_obj.chart.legend().setVisible(False)
    ui_obj.chart.legend().setLabelBrush(QtGui.QColor(text_color))
    ui_obj.chart.setBackgroundBrush(QtGui.QColor(bg_color))
    ui_obj.chart.setBackgroundRoundness(0)
    ui_obj.chart.legend().setAlignment(QtCore.Qt.AlignBottom)
    ui_obj.chart.setMargins(QtCore.QMargins(0, 0, 0, 0))

    # create default axis
    # X
    ui_obj.chart_axisX = QValueAxis()
    ui_obj.chart_axisX.setRange(0, axisX_range)
    # self.axisX.setLabelsFont(sQFont("Times", 6, sQFont.Bold))
    # self.axisX.setLabelFormat("%d")
    ui_obj.chart_axisX.setTickCount(10)
    ui_obj.chart_axisX.setLabelsBrush(QtGui.QColor(text_color))
    ui_obj.chart_axisX.setTitleText(axisX_title)
    ui_obj.chart_axisX.setTitleBrush(QtGui.QColor(text_color))
    # Y
    ui_obj.chart_axisY = QValueAxis()
    ui_obj.chart_axisY.setRange(-axisY_range, axisY_range)
    # self.axisY.setLabelsFont(sQFont("Times", 6, sQFont.Bold))
    # self.axisY.setLabelFormat("%.1f")
    ui_obj.chart_axisY.setLabelsBrush(QtGui.QColor(text_color))
    ui_obj.chart_axisY.setTickCount(10)
    ui_obj.chart_axisY.setTitleText(axisY_title)
    ui_obj.chart_axisY.setTitleBrush(QtGui.QColor(text_color))

    # add axis to chart
    ui_obj.chart.addAxis(ui_obj.chart_axisX, QtCore.Qt.AlignBottom)
    ui_obj.chart.addAxis(ui_obj.chart_axisY, QtCore.Qt.AlignLeft)

    # create chartview
    ui_obj.chartview = QChartView(ui_obj.chart)
    ui_obj.chartview.setRenderHint(QtGui.QPainter.Antialiasing)
    ui_obj.chartview.setContentsMargins(0, 0, 0, 0)

    # create trend series
    ui_obj.trend_series = QLineSeries()
    ui_obj.trend_series.setName(trend_name)
    trend_pen = QtGui.QPen()
    trend_pen.setStyle(QtCore.Qt.SolidLine)
    trend_pen.setWidth(line_width)
    trend_pen.setColor(QtGui.QColor(trend_color))
    ui_obj.trend_series.setPen(trend_pen)

    # create setpoint series
    ui_obj.setpoint_series = QLineSeries()
    ui_obj.setpoint_series.setName(setpoint_name)
    setpoint_pen = QtGui.QPen()
    setpoint_pen.setStyle(QtCore.Qt.DashLine)
    setpoint_pen.setWidth(line_width)
    setpoint_pen.setColor(QtGui.QColor(setpoint_color))
    ui_obj.setpoint_series.setPen(setpoint_pen)

    # create threashold serieses
    # top
    ui_obj.topthreshold_series = QLineSeries()
    ui_obj.topthreshold_series.setName(threshold_name)
    threshold_pen = QtGui.QPen()
    threshold_pen.setStyle(QtCore.Qt.DashLine)
    threshold_pen.setWidth(line_width)
    threshold_pen.setColor(QtGui.QColor(threshold_color))
    ui_obj.topthreshold_series.setPen(threshold_pen)
    # bottom
    ui_obj.btmthreshold_series = QLineSeries()
    ui_obj.btmthreshold_series.setName(threshold_name)
    threshold_pen = QtGui.QPen()
    threshold_pen.setStyle(QtCore.Qt.DashLine)
    threshold_pen.setWidth(line_width)
    threshold_pen.setColor(QtGui.QColor(threshold_color))
    ui_obj.btmthreshold_series.setPen(threshold_pen)

    # add series to chart
    ui_obj.chart.addSeries(ui_obj.trend_series)
    ui_obj.chart.addSeries(ui_obj.setpoint_series)
    ui_obj.chart.addSeries(ui_obj.topthreshold_series)
    ui_obj.chart.addSeries(ui_obj.btmthreshold_series)

    # attach axis
    ui_obj.trend_series.attachAxis(ui_obj.chart_axisX)
    ui_obj.setpoint_series.attachAxis(ui_obj.chart_axisX)
    ui_obj.topthreshold_series.attachAxis(ui_obj.chart_axisX)
    ui_obj.btmthreshold_series.attachAxis(ui_obj.chart_axisX)
    ui_obj.trend_series.attachAxis(ui_obj.chart_axisY)
    ui_obj.setpoint_series.attachAxis(ui_obj.chart_axisY)
    ui_obj.topthreshold_series.attachAxis(ui_obj.chart_axisY)
    ui_obj.btmthreshold_series.attachAxis(ui_obj.chart_axisY)

    # add chart to ui
    ui_obj.trend_chart_frame.layout().addWidget(ui_obj.chartview)

    # insert_default setpoint and threshold lines
    # ui_obj.chart_insert_record(initialize_chart=True, width_value=None)


def chart_insert_record(
    ui_obj, width_value, setpoint_value, threshold_value, initialize_chart=False
):
    # add default setpoint and threshold lines
    if initialize_chart:
        ui_obj.chart_axisY.setRange(
            setpoint_value - threshold_value, setpoint_value + threshold_value
        )

        for i in range(int(ui_obj.chart_axisX.max() + 1)):
            ui_obj.setpoint_series.append(i, setpoint_value)
        #
        for i in range(int(ui_obj.chart_axisX.max() + 1)):
            ui_obj.topthreshold_series.append(i, setpoint_value + 0.2)
            ui_obj.btmthreshold_series.append(i, setpoint_value - 0.2)

        return

    # insert new value to chart
    if ui_obj.cur_x_index >= ui_obj.chart_axisX.max():
        ui_obj.setpoint_series.append(ui_obj.cur_x_index + 1, setpoint_value)
        ui_obj.topthreshold_series.append(ui_obj.cur_x_index + 1, setpoint_value + 0.2)
        ui_obj.btmthreshold_series.append(ui_obj.cur_x_index + 1, setpoint_value - 0.2)
        ui_obj.chart_axisX.setMax(ui_obj.cur_x_index + 1)

    ui_obj.trend_series.append(ui_obj.cur_x_index, width_value)


def zoom_and_pan(self, max_val, slider_zoom, slider_pan):
    zoom_ratio = slider_zoom.sliderPosition() / (slider_zoom.maximum() * 1.001)
    step = 1 - zoom_ratio
    pan_level = slider_pan.sliderPosition() * zoom_ratio / slider_pan.maximum()
    min_chart = pan_level * max_val
    if slider_pan.sliderPosition() == slider_pan.maximum():
        max_chart = max_val
    else:
        max_chart = max_val * step + min_chart

    self.chart.axisX().setRange(min_chart, max_chart)


# self.horizontalSlider.valueChanged.connect(lambda: self.zoom_and_pan(max_val=20, slider_zoom=self.horizontalSlider, slider_pan=self.horizontalSlider_2))
# self.horizontalSlider_2.valueChanged.connect(lambda: self.zoom_and_pan(max_val=20, slider_zoom=self.horizontalSlider, slider_pan=self.horizontalSlider_2))

# add width trend chart to ui
# # self.create_trend_chart(setpoint_value=self.setpoint_value, threshold_value=self.threshold_value)
