#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const jeep in valsUniq) {
  const list = [];
  for (const keep in totalist) {
    if (totalist[keep][1] === valsUniq[jeep]) {
      list.unshift(totalist[keep][0]);
    }
  }
  newDict[valsUniq[jeep]] = list;
}
console.log(newDict);
