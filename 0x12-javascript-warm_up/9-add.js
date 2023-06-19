#!/usr/bin/node
function add (a, b) {
  const c = a + b;
  return c;
}

const result = add(Number(process.argv[2]), Number(process.argv[3]));
console.log(result);
