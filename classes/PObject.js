function PObject(assigno, nameo, ownero, readero, writero) {
  this.assigno=assigno
  this.nameo=nameo
  this.ownero=ownero
  this.readero=readero
  this.writero=writero
  /*this.node = Tree()*/
}
// Sets the age
// 
PObject.prototype.setassigno = function(assigno) {
    this.assigno = assigno;
};

PObject.prototype.setnameo = function(nameo) {
    this.nameo = nameo;
};

PObject.prototype.setownero = function(ownero) {
    this.ownero = ownero;
};

PObject.prototype.setreadero = function(readero) {
    this.readero = readero;
};

PObject.prototype.setwritero = function(writero) {
    this.writero = writero;
};




//  Sets the PObject PObject to module.exports
// 
module.exports = PObject;
