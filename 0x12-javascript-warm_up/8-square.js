#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let idx = 0; idx < num; idx++) {
    let row = '';
    for (let j = 0; j < num; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
