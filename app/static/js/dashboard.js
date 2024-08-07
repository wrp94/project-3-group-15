function init() {
    // set default values
    let gender = d3.select("#gender").property("value");
    let maritalStatus = d3.select("#marital_status").property("value");

    update(gender, maritalStatus);
}

function update(newGender, newMaritalStatus) {
    // update charts
    createBar(newGender, newMaritalStatus);
    createPie(newGender, newMaritalStatus);
    createViolin(newGender, newMaritalStatus);
}

function createBar(gender, maritalStatus) {
    return false;
}

function createPie(gender, maritalStatus) {
    return false;
}

function createViolin(gender, maritalStatus) {
    return false;
}