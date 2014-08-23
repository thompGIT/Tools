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
    CreateProgramBudgetChart('SnotRocket','container1')
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

    $('#containter1').highcharts(chart1);

}
