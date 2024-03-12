#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const mee in valsUniq)  {
  const list = [];
  for (const keep in totalist) {
    if (totalist[keep][1] === valsUniq[mee]) {
      list.unshift(totalist[keep][0]);
    }
  }
  newDict[valsUniq[mee]] = list;
}
console.log(newDict);
