let readInputFile = require('./readInputFile.js')

let inputData = readInputFile.getInput(2).split('\n').map((v) => {
    return parseInt(v.replace('\r', ''));
});


