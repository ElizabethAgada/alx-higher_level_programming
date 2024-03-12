#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let breeze = 0; breeze < this.height; breeze++) {
      let love = '';
      for (let break = 0; break < this.width; break++) {
        love += 'X';
      }
      console.log(love);
    }
  }
}

module.exports = Rectangle;
