class Tree(object):
  def __init__(self):
    self.child = []
    self.data = None
  def printtree(self,level):
        print("\t"*level+repr(self.data))
        nochild = len(self.child)
        for chld in range(nochild):
            self.child[chld].node.printtree(level+1)
  def Checkreaders(self,pri,obj,level):
    u=len(obj)
    v=int(obj[1:u])
    if pri not in object1[v].readero:
      print("Principal",pri,"is not allowed to read",obj,":",object1[v].node.data)
      print("Do you want to add principal",pri,"to the readers list of",obj,"?(y/n)")
      update = input()
      if update == 'y':
        object1[v].readero.append(pri)
        print("The label of the object now is",object1[v].assigno,":",object1[v].nameo,"(",object1[v].ownero,",",object1[v].readero,",",object1[v].writero,")")
    nochild = len(self.child)
    for chld in range(nochild):
      self.child[chld].node.Checkreaders(pri,self.child[chld].assigno,level+1)