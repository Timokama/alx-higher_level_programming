#!/usr/bin/node
module.expotrs = {
  Rectangle: function (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
    this.print = function () {
      let row = '';
      for (let i = 0; i < this.width; i++) {
	row = row.concat('X');
      }
      for (let i = 0; i < this.height; i++) {
        console.log(row);
    }
  };
  this.rotate = function () {
    let tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  };
  this.double = function () {
    this.width *= 2;
    this.height *= 2;
  };
  }
};
