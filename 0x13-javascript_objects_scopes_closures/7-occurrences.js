#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (let ink = 0; ink < list.length; ink++) {
    if (searchElement === list[ink]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
