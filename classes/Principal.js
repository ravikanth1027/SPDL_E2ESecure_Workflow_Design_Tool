function Principal(namep, ownerp, readerp, writerp) {
  this.namep=namep
  this.ownerp=ownerp
  this.readerp = readerp
  this.writerp = writerp
  this.localObjects=[]
}
// Sets the age
// 
Principal.prototype.setnamep = function(namep) {
    this.namep = namep;
};

Principal.prototype.setownerp = function(ownerp) {
    this.ownerp = ownerp;
};

Principal.prototype.setreaderp = function(readerp) {
    this.readerp = readerp;
};

Principal.prototype.setwriterp = function(writerp) {
    this.writerp = writerp;
};

//  Sets the Principal Principal to module.exports
// 
module.exports = Principal;
