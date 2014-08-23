/******************************************************************************
 * debug
 *****************************************************************************/
var g_DEBUG = 0

function debug(msg) {
    if(g_DEBUG) {
        console.log(msg)
    }
}

/* called when the page loads */
function WebDashInit() {
    CreateProgramBudgetChart('FartWeasel','container0')
    CreateStaffingNeedsChart('container1')
    CreateProgramBudgetChart('Woozle','container2')
    CreateProgramBudgetChart('Hefalump','container3')
}

function CreateProgramBudgetChart(program, container) {
    var chart1 = new Highcharts.Chart({
        chart: {
            zoomType: 'xy',
            renderTo: container
        },
        title: {
            text: program + ' Budget Performance'
        },
        subtitle: {
            text: 'Last Updated: Aug 22, 2014'
        },
        xAxis: [{
            categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        }],
        yAxis: [{ // Primary yAxis
            min: 0,
            labels: {
                format: '${value}K'
            },
            title: {
                text: 'Cumulative'
            }
        }, { // Secondary yAxis
            title: {
                text: 'Monthly'
            },
            labels: {
                format: '${value}K'
            },
            opposite: true
        }],
        tooltip: {
            shared: true
        },
        legend: {
            layout: 'vertical',
            align: 'left',
            x: 120,
            verticalAlign: 'top',
            y: 100,
            floating: true,
            backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF',
            borderWidth: 1
        },
        series: [{
            name: 'Projected',
            type: 'column',
            color: Highcharts.getOptions().colors[0],
            yAxis: 1,
            data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            tooltip: {
                valuePrefix: '$',
                valueSuffix: 'K'
            }
        }, {
            name: 'Actual',
            type: 'column',
            color: Highcharts.getOptions().colors[2],
            yAxis: 1,
            data: [2, 2, 3, 3, 5, 6, 8, 9],
            tooltip: {
                valuePrefix: '$',
                valueSuffix: 'K'
            }
        }, {
            name: 'Cumulative (Projected)',
            type: 'spline',
            color: 'blue',
            marker: {
                enabled: false
            },
            data: [1,3,6,10,15,21,28,35,44,54,65,77],
            tooltip: {
                valuePrefix: '$',
                valueSuffix: 'K'
            }
        }, {
            name: 'Cumulative (Actual)',
            type: 'spline',
            color: 'green',
            marker: {
                enabled: false
            },
            data: [2,4,7,10,15,21,29,37],
            tooltip: {
                valuePrefix: '$',
                valueSuffix: 'K'
            }
        }]
    });
}

function CreateStaffingNeedsChart(container) {
    var chart1 = new Highcharts.Chart({
        chart: {
            type: 'column',
            renderTo: container
        },
        title: {
            text: 'Open Engineering Positions'
        },
        subtitle: {
            text: 'Last Updated: 08/23/2014'
        },
        xAxis: {
            categories: ['FartWeasel', 'Program X', 'Program Y', 'Program Z', 'Cyber Monkeys']
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Total Positions'
            },
            stackLabels: {
                enabled: true,
                style: {
                    fontWeight: 'bold',
                    color: (Highcharts.theme && Highcharts.theme.textColor) || 'gray'
                }
            }
        },
        legend: {
            align: 'right',
            x: -70,
            verticalAlign: 'top',
            y: 20,
            floating: true,
            backgroundColor: (Highcharts.theme && Highcharts.theme.background2) || 'white',
            borderColor: '#CCC',
            borderWidth: 1,
            shadow: true
        },
        tooltip: {
            formatter: function () {
                return '<b>' + this.x + '</b><br/>' +
                    this.series.name + ': ' + this.y + '<br/>' +
                    'Total: ' + this.point.stackTotal;
            }
        },
        plotOptions: {
            column: {
                stacking: 'normal',
                dataLabels: {
                    enabled: true,
                    color: (Highcharts.theme && Highcharts.theme.dataLabelsColor) || 'white',
                    style: {
                        textShadow: '0 0 3px black, 0 0 3px black'
                    }
                }
            }
        },
        series: [{
            name: 'Dev',
            data: [5, 3, 4, 7, 2]
        }, {
            name: 'VR',
            data: [2, 2, 3, 2, 1]
        }, {
            name: 'RE',
            data: [3, 4, 4, 2, 5]
        }]
    });
}

