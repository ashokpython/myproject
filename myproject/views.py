from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from collections import OrderedDict

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from fusioncharts import FusionCharts

def myFirstChart(request):
    dataSource = OrderedDict()
    chartConfig = OrderedDict()
    
    chartConfig["formatnumberscale"] = "2"
    chartConfig["drawcrossline"] = "2"
    chartConfig["theme"] = "gammel"
    chartConfig["palettecolors"] = "add8e6,90ee90"
    chartData = OrderedDict()
    chartData["Total Accessed Accounts"] = 60000
    chartData["Undefined Accounts"] = 120000

    dataSource["chart"] = chartConfig
    dataSource["data"] = []
    for key, value in chartData.items():
        data = {}
        data["label"] = key
        data["value"] = value
        dataSource["data"].append(data)
    column2D = FusionCharts("column2d", "myFirstChart", "300", "500", "myFirstchart-container", "json", dataSource)

    #111111111111
    dataSource = OrderedDict()
    chartData = OrderedDict()
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Objects & Accounts"
    chartConfig["formatnumberscale"] = "2"
    chartConfig["drawcrossline"] = "2"
    chartConfig["theme"] = "gammel"
    chartConfig["palettecolors"] = "add8e6,90ee90"
    chartData["Licences"] = 2000
    chartData["Licenced End Users"] = 2000
    chartData["People Who Have Access to Valult"] = 4000
    chartData["Sales"] = 3000
    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    for key, value in chartData.items():
        data = {}
        data["label"] = key
        data["value"] = value
        dataSource["data"].append(data)
    column2D1 = FusionCharts("column2d", "myFirstChart1", "400", "500", "myFirstchart-container1", "json", dataSource)

    dataSource = OrderedDict()
    chartData = OrderedDict()
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Windows & Domain Admins"
    chartConfig["palettecolors"] = "add8e6,90ee90"
    chartConfig["formatnumberscale"] = "2"
    chartConfig["drawcrossline"] = "2"
    chartConfig["theme"] = "gammel"
    chartData["Domain Admin Total"] = 2000
    chartData["Domain Admins Valulted"] = 2000
    chartData["Server Admins Total"] = 3300
    chartData["Server Admins Valulted"] = 2700
    chartData["Workstation Admins Total"] = 1500
    chartData["Workstation Admins Valulted"] = 1400
    chartData["Total Admins Access"] = 3300
    chartData["Total Admins Valulted"] = 2700

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    for key, value in chartData.items():
        data = {}
        data["label"] = key
        data["value"] = value
        dataSource["data"].append(data)
    column2D2 = FusionCharts("column2d", "myFirstChart2", "500", "500", "myFirstchart-container2", "json", dataSource)

    return render(request, 'index.html', {
        'output': column2D.render(),
        'output1':column2D1.render(),
        'output2':column2D2.render(),
    })

def myFirstChart1(request):
    dataSource = OrderedDict()
    chartData = OrderedDict()
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Objects & Accounts"
    chartConfig["formatnumberscale"] = "2"
    chartConfig["drawcrossline"] = "2"
    chartConfig["theme"] = "gammel"
    chartConfig["palettecolors"] = "add8e6,90ee90"
    chartData["Licences"] = 2000
    chartData["Licenced End Users"] = 2000
    chartData["People Who Have Access to Valult"] = 4000
    chartData["Sales"] = 3000
    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    for key, value in chartData.items():
        data = {}
        data["label"] = key
        data["value"] = value
        dataSource["data"].append(data)
    column2D1 = FusionCharts("column2d", "myFirstChart1", "350", "400", "myFirstchart-container1", "json", dataSource)

    

    return render(request, 'index1.html', {
        'output1': column2D1.render()
    })

def myFirstChart2(request):
    dataSource = OrderedDict()
    chartData = OrderedDict()
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Windows & Domain Admins"
    chartConfig["palettecolors"] = "add8e6,90ee90"
    chartConfig["formatnumberscale"] = "2"
    chartConfig["drawcrossline"] = "2"
    chartConfig["theme"] = "gammel"
    chartData["Domain Admin Total"] = 2000
    chartData["Domain Admins Valulted"] = 2000
    chartData["Server Admins Total"] = 3300
    chartData["Server Admins Valulted"] = 2700
    chartData["Workstation Admins Total"] = 1500
    chartData["Workstation Admins Valulted"] = 1400
    chartData["Total Admins Access"] = 3300
    chartData["Total Admins Valulted"] = 2700

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    for key, value in chartData.items():
        data = {}
        data["label"] = key
        data["value"] = value
        dataSource["data"].append(data)
    column2D2 = FusionCharts("column2d", "myFirstChart2", "500", "400", "myFirstchart-container2", "json", dataSource)

    return render(request, 'index2.html', {
        'output2': column2D2.render()
    })


# from django.shortcuts import render
# from django.http import HttpResponse
# from collections import OrderedDict

# # Include the `fusioncharts.py` file that contains functions to embed the charts.
# from fusioncharts import FusionCharts

# # def chart1(request):
# #     #Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
# #     dataSource = OrderedDict()

# #     # The `chartConfig` dict contains key-value pairs of data for chart attribute
# #     chartConfig = OrderedDict()
# #     chartConfig["caption"] = "Objects & Accounts"
# #     # chartConfig["subCaption"] = "In MMbbl = One Million barrels"
# #     # chartConfig["xAxisName"] = "Country"
# #     # chartConfig["yAxisName"] = "Reserves (MMbbl)"
# #     chartConfig["numberSuffix"] = "K"
# #     chartConfig["theme"] = "gammel"

# #     # The `chartData` dict contains key-value pairs of data
# #     chartData = OrderedDict()
# #     # chartData["Total Accessed Accounts"] = 60
# #     chartData["Undefined Accounts"] = 50
# #     chartData["Total Accessed Accounts"] = 60

# #     dataSource["chart"] = chartConfig
# #     dataSource["data"] = []

# #     # Convert the data in the `chartData`array into a format that can be consumed by FusionCharts.
# #     #The data for the chart should be in an array wherein each element of the array
# #     #is a JSON object# having the `label` and `value` as keys.

# #     #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.

# #     for key, value in chartData.items():
# #         data = {}
# #         data["label"] = key
# #         data["value"] = value
# #         dataSource["data"].append(data)
# #     print("-----Hello----------------------",dataSource)

# #     # Create an object for the column 2D chart using the FusionCharts class constructor
# #     # The chart data is passed to the `dataSource` parameter.
# #     column2D1 = FusionCharts("column2d", "myFirstChart", "400", "400", "myFirstchart-container", "json", dataSource)
# #     return render(request, 'index.html', {
# #         'output': column2D1.render()
# #     })

# def myFirstChart(request):
#     #Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
#     dataSource = OrderedDict()

#     # The `chartConfig` dict contains key-value pairs of data for chart attribute
#     chartConfig = OrderedDict()
#     chartConfig["caption"] = "Objects & Accounts"
#     # chartConfig["subCaption"] = "In MMbbl = One Million barrels"
#     # chartConfig["xAxisName"] = "Country"
#     # chartConfig["yAxisName"] = "Reserves (MMbbl)"
#     chartConfig["numberSuffix"] = "K"
#     chartConfig["theme"] = "gammel"

#     # The `chartData` dict contains key-value pairs of data
#     chartData = OrderedDict()
#     # chartData["Total Accessed Accounts"] = 60
#     chartData["Undefined Accounts"] = 30
#     chartData["Total Accessed Accounts"] = 100

#     dataSource["chart"] = chartConfig
#     dataSource["data"] = []

#     # Convert the data in the `chartData`array into a format that can be consumed by FusionCharts.
#     #The data for the chart should be in an array wherein each element of the array
#     #is a JSON object# having the `label` and `value` as keys.

#     #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.

#     for key, value in chartData.items():
#         data = {}
#         data["label"] = key
#         data["value"] = value
#         dataSource["data"].append(data)
#     print("-----Hello----------------------",dataSource)

#     # Create an object for the column 2D chart using the FusionCharts class constructor
#     # The chart data is passed to the `dataSource` parameter.
#     column2D1 = FusionCharts("column2d", "myFirstChart1", "400", "400", "myFirstchart-container1", "json", dataSource)    
#     #Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
#     dataSource = OrderedDict()

#     # The `chartConfig` dict contains key-value pairs of data for chart attribute
#     chartConfig = OrderedDict()
#     chartConfig["caption"] = "Objects & Accounts"
#     # chartConfig["subCaption"] = "In MMbbl = One Million barrels"
#     # chartConfig["xAxisName"] = "Country"
#     # chartConfig["yAxisName"] = "Reserves (MMbbl)"
#     chartConfig["numberSuffix"] = "K"
#     chartConfig["theme"] = "gammel"

#     # The `chartData` dict contains key-value pairs of data
#     chartData = OrderedDict()
#     # chartData["Total Accessed Accounts"] = 60
#     chartData["paletecolors"] = 50
#     chartData["Undefined Accounts"] = 50
#     chartData["Total Accessed Accounts"] = 60

#     dataSource["chart"] = chartConfig
#     dataSource["data"] = []

#     # Convert the data in the `chartData`array into a format that can be consumed by FusionCharts.
#     #The data for the chart should be in an array wherein each element of the array
#     #is a JSON object# having the `label` and `value` as keys.

#     #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
    
#     for key, value in chartData.items():
#         data = {}
#         data["label"] = key
#         data["value"] = value
#         dataSource["data"].append(data)
#     print("-----Hello----------------------",dataSource)

# # Create an object for the column 2D chart using the FusionCharts class constructor
# # The chart data is passed to the `dataSource` parameter.
#     column2D = FusionCharts("column3d", "myFirstChart", "400", "400", "myFirstchart-container", "json", dataSource)
#     # chart1(request)
#     return render(request, 'index.html', {
#         'output': column2D.render(),
#         'output1':column2D1.render()
#     })

















# # from django.shortcuts import render
# # from django.http import HttpResponse
# # from fusioncharts import FusionCharts

# # def chart(request):
# #    chartObj = FusionCharts( 'mscolumn2d', 'ex1', '600', '400', 'chart-1', 'json', """{
# #   "chart": {
# #     "caption": "App Publishing Trend",
# #     "subcaption": "2012-2016",
# #     "xaxisname": "Years",
# #     "yaxisname": "Total number of apps in store",
# #     "formatnumberscale": "1",
# #     "plottooltext": "<b>$dataValue</b> apps were available on <b>$seriesName</b> in $label",
# #     "theme": "fusion",
# #     "drawcrossline": "1"
# #   },
# #   "categories": [
# #     {
# #       "category": [
# #         {
# #           "label": "2012"
# #         },
# #         {
# #           "label": "2013"
# #         },
# #         {
# #           "label": "2014"
# #         },
# #         {
# #           "label": "2015"
# #         },
# #         {
# #           "label": "2016"
# #         }
# #       ]
# #     }
# #   ],
# #   "dataset": [
# #     {
# #       "seriesname": "iOS App Store",
# #       "data": [
# #         {
# #           "value": "125000"
# #         },
# #         {
# #           "value": "300000"
# #         },
# #         {
# #           "value": "480000"
# #         },
# #         {
# #           "value": "800000"
# #         },
# #         {
# #           "value": "1100000"
# #         }
# #       ]
# #     },
# #     {
# #       "seriesname": "Google Play Store",
# #       "data": [
# #         {
# #           "value": "70000"
# #         },
# #         {
# #           "value": "150000"
# #         },
# #         {
# #           "value": "350000"
# #         },
# #         {
# #           "value": "600000"
# #         },
# #         {
# #           "value": "1400000"
# #         }
# #       ]
# #     },
# #     {
# #       "seriesname": "Amazon AppStore",
# #       "data": [
# #         {
# #           "value": "10000"
# #         },
# #         {
# #           "value": "100000"
# #         },
# #         {
# #           "value": "300000"
# #         },
# #         {
# #           "value": "600000"
# #         },
# #         {
# #           "value": "900000"
# #         }
# #       ]
# #     }
# #   ]
# # }""")
# #    return render(request, 'index.html', {'output': chartObj.render()})



















# # def myFirstChart1(request):

# #     #Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
# #     dataSource = OrderedDict()

# #     # The `chartConfig` dict contains key-value pairs of data for chart attribute
# #     chartConfig = OrderedDict()
# #     chartConfig["caption"] = "Objects & Accounts"
# #     # chartConfig["subCaption"] = "In MMbbl = One Million barrels"
# #     # chartConfig["xAxisName"] = "Country"
# #     # chartConfig["yAxisName"] = "Reserves (MMbbl)"
# #     chartConfig["numberSuffix"] = "K"
# #     # chartConfig["theme"] = "fusion"

# #     # The `chartData` dict contains key-value pairs of data
# #     chartData = OrderedDict()
# #     # chartData["Total Accessed Accounts"] = 60
# #     chartData["Undefined Accounts"] = 60
# #     chartData["Total Accessed Accounts"] = 60

# #     dataSource["chart"] = chartConfig
# #     dataSource["data"] = []

# #     # Convert the data in the `chartData`array into a format that can be consumed by FusionCharts.
# #     #The data for the chart should be in an array wherein each element of the array
# #     #is a JSON object# having the `label` and `value` as keys.

# #     #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
# #     for key, value in chartData.items():
# #         data = {}
# #     data["label"] = key
# #     data["value"] = value
# #     dataSource["data"].append(data)


# # # Create an object for the column 2D chart using the FusionCharts class constructor
# # # The chart data is passed to the `dataSource` parameter.
# #     column2D = FusionCharts("column2d", "myFirstChart", "100", "400", "myFirstchart-container", "json", dataSource)

# #     return render(request, 'index1.html', {
# #         'output': column2D.render()
# #     })