#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let pee = 0; pee < this.height; pee++) {
      let see = '';
      for (let jam = 0; jam < this.width; jam++) {
        see += c;
      }
      console.log(see);
    }
  }
}

module.exports = Square;
