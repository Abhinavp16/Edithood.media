const fs = require('fs');
const https = require('https');

const files = [
    "react.DmKa-o9F.mjs",
    "rolldown-runtime.B3Ac26FU.mjs",
    "motion.D_llmi51.mjs",
    "framer.DtbAdQOl.mjs",
    "shared-lib.DMptVSRF.mjs",
    "eOnGVwDMo._v2adj_s.mjs",
    "Zdm6pJ9rFG4Q99RaaFKQeI8zBMR9DQT7_7S0ax3QxX4.BzQQzOMX.mjs",
    "EZYUEZn7S.C40Dwgh8.mjs",
    "N9mce2w1X.NH2P9tA8.mjs",
    "jm5EmS261.BZ1RXGHa.mjs",
    "framer.KBYL7ZzE.mjs",
    "chunk-T7K3R47Y.mjs",
    "chunk-FWT7F4IE.mjs"
];

function download(filename) {
    return new Promise((resolve) => {
        const file = fs.createWriteStream(filename);
        https.get('https://framerusercontent.com/sites/3B5fV76Qbim9smJbsMjk8a/' + filename, function(response) {
            response.pipe(file);
            file.on('finish', function() {
                file.close(resolve);
            });
        }).on('error', function() {
            fs.unlink(filename);
            resolve();
        });
    });
}

async function run() {
    for (const file of files) {
        console.log("Fetching " + file);
        await download(file);
    }
    console.log("Done");
}

run();
