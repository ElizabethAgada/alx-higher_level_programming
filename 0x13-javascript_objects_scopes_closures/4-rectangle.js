#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let p = 0; p < this.height; p++) {
      let q = '';
      for (let h = 0; h < this.width; h++) {
        q += 'X';
      }
      console.log(q);
    }
  }

  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
