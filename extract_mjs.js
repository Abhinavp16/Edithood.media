const fs = require('fs');
const text = fs.readFileSync('live.html', 'utf8');
const urls = text.match(/https?:\/\/[^\s"'>]+\.mjs/g);
console.log([...new Set(urls)].join('\n'));
