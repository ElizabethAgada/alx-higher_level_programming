#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let ink = 0;
  while ((len - ink) > 0) {
    const aux = list[len];
    list[len] = list[ink];
    list[ink] = aux;
    ink++;
    len--;
  }
  return list;
};
