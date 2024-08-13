function init() {
    // set default values
    let gender = d3.select("#gender").property("value");
    let maritalStatus = d3.select("#marital_status").property("value");

    update(gender, maritalStatus);
}

function update(newGender, newMaritalStatus) {
    // update charts
    let url = `/api/v1.0/get_dashboard/${newGender}/${newMaritalStatus}`;
    d3.json(url).then(function(data) {
        createBar(data[0]);
        createPie(data[1]);
        createViolin(data[2]);
    });
}

function createBar(bar_data) {

    // sort data
    let sorted_bar_data = Object.entries(bar_data).sort((a, b) => b[1] - a[1]);
    bar_data = Object.fromEntries(sorted_bar_data);

    let x_values = Object.keys(bar_data);
    let y_values = Object.values(bar_data);

    let trace = {
        x: x_values,
        y: y_values,
        type: 'bar',
        marker: {
            color: '#05668D',
            opacity: 0.7
        }
    };

    let data = [trace];

    let layout = {
        title: 'Education Counts',
        xaxis: {title: 'Education'},
        yaxis: {title: 'Count'}
    };

    Plotly.newPlot('bar_chart', data, layout);
}

function createPie(pie_data) {
    let pie_values = Object.values(pie_data);
    let pie_labels = Object.keys(pie_data);

    let trace = {
        values: pie_values,
        labels: pie_labels,
        type: 'pie',
        hole: 0.4,
        marker: {
            colors: ['#05668D', '#679436', '#A5BE00', '#427AA1']
        },
        opacity: 0.8
    };

    let data = [trace];

    let layout = {
        title: 'Occupations',
    };

    Plotly.newPlot('pie_chart', data, layout);
}

function createViolin(violin_data) {

    let trace = {
        x: Object.keys(violin_data),
        type: 'violin',
        fillcolor: '#679436',
        opacity: 0.7,
        box: {visible: true},
        meanline: {visible: true},
        y0: "Count",
        line: {color: "black"}
    };

    let data = [trace];

    let layout = {
        title: 'Age Distribution',
        xaxis: {title: 'Age', zeroline: true},
        yaxis: {zeroline: true}
    };

    Plotly.newPlot('violin_chart', data, layout);
}

d3.select("#filter").on("click", init);

init();