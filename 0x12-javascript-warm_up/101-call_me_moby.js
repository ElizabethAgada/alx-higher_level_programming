#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let breeze = 0; breeze < x; breeze++) {
    theFunction();
  }
};
