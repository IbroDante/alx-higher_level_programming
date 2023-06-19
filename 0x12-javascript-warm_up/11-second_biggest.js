#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const arr = process.argv.slice(2).map(Number);
  const sortedArr = arr.sort(function (a, b) {
    return b - a;
  });
  const second = sortedArr[1];
  console.log(second);
}
