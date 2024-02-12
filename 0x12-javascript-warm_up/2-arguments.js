#!/usr/bin/node
const myNum = process.argv.length - 2;
if (myNum === 0) {
  console.log('No argument');
} else if (myNum === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
