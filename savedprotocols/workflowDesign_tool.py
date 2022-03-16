#!/bin/python3

import math
import os
import random
import re
import sys
import time
import json
from datetime import date

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


class Principal:
  def __init__(self,namep,ownerp,readerp,writerp):
    self.namep=namep
    self.ownerp=ownerp
    self.readerp=readerp
    self.writerp=writerp
    self.localObjects=[]
    
class Object:
  def __init__(self,assigno,nameo,ownero,readero,writero):
    self.assigno=assigno
    self.nameo=nameo
    self.ownero=ownero
    self.readero=readero
    self.writero=writero
    self.node = Tree()
    
def Union(lst1, lst2):
    print("Union------------------------------lst1", lst1)
    print("Union------------------------------lst2", lst2)
    final_list = list(set(lst1) | set(lst2))
    return final_list 

def Intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))
  
principal = []
namepr = []
object1 = []
nameobj = []
dictpri = dict()
count = 0
auto = 0
ProcessingFile=""
fp = None

#Code - Ravi- start#
version = ""
bptype = ""
no_of_roles = 0
names_of_roles = []
no_of_query_objs = 0
query_objs_map = {}
no_of_initial_objs = 0
initial_objs = {}
bpsteps = {}
stepno = 0
payload = {}
protocol_objects = {}
functions = {}
max_counter = 0
#Code - Ravi- End#

def Init_Principals(i):
  owner = namepr[i]
  readerlist = namepr
  writerlist = []
  writerlist.append(namepr[i])
  print("The initial label of the principal ",namepr[i],": (",owner,",",readerlist,",",writerlist,")")
  principal.append(Principal(namepr[i],owner,readerlist,writerlist))

def CheckPrincipals(principal_list):
  pn=len(principal_list)
  cnt = 0
  for j in range(pn):
    if principal_list[j] not in namepr:
      print("-----ERROR-----",principal_list[j]," not in principal list\n")
      pass
    else:
      cnt += 1
  if cnt != pn:
    return 1
  else:
    return 0
  
def printState(step):
  print("\n---------------------STATE",step,"----------------------")
  prn = len(principal)
  for i in range(prn):
    print(principal[i].namep,"(",principal[i].ownerp,",",principal[i].readerp,",",principal[i].writerp,")")
    pass
  obn = len(object1)
  for i in range(obn):
    print(object1[i].assigno,":",object1[i].nameo,"(",object1[i].ownero,",",object1[i].readero,",",object1[i].writero,")")
    object1[i].node.printtree(0)
  for i in range(prn):
    print("\nobjects that are present in the local space of principal",principal[i].namep)
    print(principal[i].localObjects)
    pass

def MyInput():
  global auto
  if auto == 1:
    global fp
    inp = fp.readline()
    if inp == "exit":
      return inp
    if len(inp)>0:
      #input()
      inp = inp[0:len(inp)-1]
      print(inp)
      time.sleep(0.5)
      return inp
    else:
      auto = 0
      fp.close()
      print("Finished processing from file. Switching to manual mode.")
      print("If you wish to exit enter 'exit', otherwise answer the above question.")
      return input()
      #return "End"
  return input()

def Init_Objects(i):
  print("\nEnter the initial label of the object : ",nameobj[i])
  #owners
  while 1:
    print("Enter the owner of the object ")
    owner = MyInput()
    if CheckPrincipals([owner])==1:
      print("Re enter the owner\n")
      pass
      continue
    else:
      break

  #readers
  while 1:
    print("Enter the principals who can read the object ")
    readerlist = MyInput().split(",")
    if CheckPrincipals(readerlist)==1:
      print("Re enter the readers")
      continue
    else:
      break

  #writers
  while 1:
    print("Enter the principals who have influenced the object ")
    writerlist = MyInput().split(",")
    if CheckPrincipals(writerlist)==1:
      print("Re enter the writers")
      pass
      continue
    else:
      break

  assign = "O"+str(i)
  print("The object",nameobj[i],"is stored as",assign,"and should be referred as the same in further references")
  print("The initial label of the object ",assign,"is",nameobj[i],": (",owner,",",readerlist,",",writerlist,")")
  object1.append(Object(assign,nameobj[i],owner,readerlist,writerlist))
  object1[i].node.data = nameobj[i]
  # print("********************************* ", object1[i].node.data)

def CreateInitLocal():
  prn = len(principal)
  obn = len(object1)
  for i in range(prn):
    dictpri[principal[i].namep]=i
    
  label = []
  for i in range(obn):
    readn = len(object1[i].readero)
    for j in range(readn):
      k = dictpri[object1[i].readero[j]]
      principal[k].localObjects.append(object1[i].assigno)

def getnop():
  print("Enter the number of principals in the system ")
  NoP = int(MyInput())
  return NoP

def getVersion():
  print("Enter version number ")
  version = str(MyInput())
  return version

def getbptype():
  print("Enter bptype:")
  bptype = str(MyInput())
  return bptype

def getprincipal(i):
  print("Enter name of principal",i+1,end=" ")
  pr = MyInput()
  return pr

def getnoobj():
  print("\nEnter the number of initial objects in the system ")
  NoObj = int(MyInput())
  return NoObj

def getobject(i):
  print("\nEnter name of object",i+1,end=" ")
  ob = MyInput()
  return ob
def print_proto_function_BDP(bpdfile, step, msg):
  fd=open(bpdfile,"a+")
  obn = len(object1)

  for i in range(obn):
    tmp_list = []
    tmp_list_functions = []
    if CheckObject(object1[i].nameo) == "complex":
      f, obj_list = ParseComplexObj(object1[i].nameo)
      functions[f] = ""
      tmp_list_functions.append(f)
      t_list = []
      for t in obj_list:
        t_list.append(t[1:])
      tmp_list_functions.append(t_list)
      tmp_list.append(tmp_list_functions)
      tmp_list.append(object1[i].readero)
      protocol_objects[object1[i].assigno[1:]] = tmp_list
    else:
      tmp_list_functions.append(object1[i].nameo)
      tmp_list.append(tmp_list_functions)
      tmp_list.append(object1[i].readero)
      protocol_objects[object1[i].assigno[1:]] = tmp_list
  payload["total_no_of_protocol_objects"]= len(protocol_objects)
  payload["protocol_objects"]= protocol_objects
  payload["no_of_functions"] = len(functions)
  payload["functions"] = functions
  fd.close()

def printIFD(ifd,step,msg):
  fd=open(ifd,"a+")
  fd.write("\n---------------------STATE")
  fd.write(str(step))
  fd.write("----------------------\n")
  fd.write(">>>>> :")
  fd.write(msg)
  fd.write("\n")
  prn = len(principal)
  for i in range(prn):
    fd.write(principal[i].namep)
    fd.write(",")
    fd.write(principal[i].ownerp)
    fd.write(",[")
    fd.write(','.join(principal[i].readerp))
    fd.write("],[")
    fd.write(','.join(principal[i].writerp))
    fd.write("])\n")
  obn = len(object1)
  for i in range(obn):
    fd.write(object1[i].assigno)
    fd.write(",")       
    fd.write(object1[i].nameo)
    fd.write(":(")
    fd.write(object1[i].ownero)
    fd.write(",[")
    fd.write(','.join(object1[i].readero))
    fd.write("],[")
    fd.write(','.join(object1[i].writero))
    fd.write("])\n")
  fd.close()
    
def init(protocol,ifd, bpd):
  ff=open(protocol,"a+")
  bpdff = open(bpd,"a+")
  global bpname
  bpname = bpd.split("_")[0]
  global bptype
  global no_of_roles
  global no_of_initial_objs
  global version
  bptype = getbptype()
  bp_type = str(bptype)
  ff.write(bp_type)
  ff.write("\n")
  version = getVersion()
  ff.write(str(version))
  ff.write("\n")
  NoP = getnop()
  ff.write(str(NoP))
  ff.write("\n")
  
  no_of_roles = NoP
  
  for i in range(NoP):
    pr = getprincipal(i)
    namepr.append(pr)
    ff.write(pr)
    ff.write("\n")
    
    names_of_roles.append(pr)
    
  for i in range(NoP):
    Init_Principals(i)

  NoObj = getnoobj()
  ff.write(str(NoObj))
  ff.write("\n")
  
  no_of_initial_objs = NoObj
  
  global count
  count = NoObj
  for i in range(NoObj):
    ob = getobject(i)
    nameobj.append(ob)
    Init_Objects(i)
    ff.write(object1[i].nameo)
    ff.write("\n")
    ff.write(object1[i].ownero)
    ff.write("\n")
    
    initial_objs[object1[i].assigno[1:]] = object1[i].ownero
    
    ff.write(','.join(object1[i].readero))
    ff.write("\n")
    ff.write(','.join(object1[i].writero))
    ff.write("\n")
  ff.close()
  msg="----INITIALIZATION---\n"
  printIFD(ifd,0,msg)
  CreateInitLocal()
  printState(0)

def AddObjecttoLocal(p1,assignobj):
  j = int(assignobj[1:len(assignobj)])
  i = dictpri[p1]
  principal[i].localObjects.append(object1[j].assigno)
  print("The object",object1[j].nameo,"is stored as",assignobj,"and should be referred as the same in further references")
  print("The initial label of the object ",assignobj,"is",object1[j].nameo,": (",object1[j].ownero,",",object1[j].readero,",",object1[j].writero,")")

def CheckDowngrade(p1,r,w,p2):
  flag = 0
  for p in p2:
    if p not in r:
      flag = 1
      break
  if flag == 0:
    return 0

  r = Union(r,w)
  for p in p2:
    if p not in r:
      flag = 0
      break

  if w == [p1] or flag == 1:
    print("Principals",p2,"added as readers for the new object\n")
    return 0
  else:
    print("Allowing principals",p2,"to read the new object was a security threat\n")
    print("Do you still wish to allow principals",p2,"to read the new object? (y/n)")
    choice = input()
    if choice == 'y':
      print("Adding principals",p2,"as readers as per request\n")
      return 0
    else:
      return 1

def CheckObject(obj):
  start = obj.find('(')
  if start == -1:
    return "simple"
  if obj[len(obj)-1] != ')':
    return "incorrect"
  return "complex"

def ParseComplex(p1,obj):
  start = obj.find('(')
  potential = obj[start+1:len(obj)-1]
  objlist = potential.split(",")
  i = dictpri[p1]

  for o in objlist:
    if o not in principal[i].localObjects:
      print(obj,"is not a wellformed complex object\n")
      return []

  return objlist

# Code - Ravi - start#
def ParseComplexObj(obj):
  start = obj.find('(')
  fname = obj.split('(')
  potential = obj[start+1:len(obj)-1]
  objlist = potential.split(",")
  return fname[0], objlist
# Code - Ravi - end#


def CreateObject(p1,obj,p2):
  LabelChange = 0
  i = dictpri[p1]
  readers = list(principal[i].readerp)
  writers = list(principal[i].writerp)

  objectType = CheckObject(obj)
  if objectType == "incorrect":
    print("The object",obj,"is not well formed\n")
    return 1
  if objectType == "complex":
    print("COMPLEX OBJECT", obj)
    objList = ParseComplex(p1,obj)
    if len(objList)==0:
      return 1
    else:
      for o in objList:
        v=int(o[1:len(o)])
        readers = Intersection(readers,object1[v].readero)
        writers = Union(writers,object1[v].writero)
      LabelChange = 1

  p2 = p2.split(",")
  if CheckDowngrade(p1,readers,writers,p2) == 1:
    return 1

  if LabelChange == 1:
    principal[i].readerp = list(readers)
    principal[i].writerp = list(writers)

  global count
  assignobj = "O" + str(count)
  object1.append(Object(assignobj,obj,principal[i].ownerp,Union(principal[i].readerp,p2),principal[i].writerp))
  count += 1
  AddObjecttoLocal(p1,assignobj)
  return 0

def SendObject(p1,obj,p2):
  i = dictpri[p1]
  if obj not in principal[i].localObjects:
    print(obj,"is not in the local space of principal",p1,"\n")
    return 1

  v=int(obj[1:len(obj)])
  readers = list(principal[i].readerp)
  writers = list(principal[i].writerp)
  readers = Intersection(readers,object1[v].readero)
  writers = Union(writers,object1[v].writero)
  if CheckDowngrade(p1,readers,writers,[p2]) == 1:
    return 1

  principal[i].readerp = list(readers)
  principal[i].writerp = list(writers)

  global count
  assignobj = "O" + str(count)

  object1.append(Object(assignobj,obj,principal[i].ownerp,Union(principal[i].readerp,[p2]),principal[i].writerp))
  count += 1
  AddObjecttoLocal(p1,assignobj)
  print("The object being sent is referenced as",assignobj,"\n")
  return 0

def ReceiveObject(p1,obj):
  #-----change
  global count
  v=int(obj[1:len(obj)])
  if p1 not in object1[v].readero:
    print("------Error-----principal",p1,"is not allowed to read object",obj,"\n")
    return 1

  i=dictpri[p1]
  principal[i].readerp = Intersection(principal[i].readerp,object1[v].readero)
  print("____________________",principal[i].writerp,object1[v].writero)
  principal[i].writerp = Union(principal[i].writerp,object1[v].writero)

  j=count
  assign = "O"+str(j)
  object1.append(Object(assign,object1[v].nameo,principal[i].ownerp,principal[i].readerp,principal[i].writerp))#--change
  count += 1
  AddObjecttoLocal(p1,assign)

def Checkcreates(msgparts):
  if len(msgparts) != 5:
    print("Wrong Language.\n")
    return 1
  if msgparts[3] != "for":
    print("Wrong Language.\n")
    return 1
  p1 = msgparts[0]
  p2 = msgparts[4].split(",")
  if CheckPrincipals([p1])==1:
    return 1
  if CheckPrincipals(p2)==1:
    return 1
  return 0

def Checksends(msgparts):
  if len(msgparts) != 5:
    print("Wrong Language.\n")
    return 1
  if msgparts[3] != "to":
    print("Wrong Language.\n")
    return 1
  p1 = msgparts[0]
  obj = msgparts[2]
  p2 = msgparts[4]
  if CheckPrincipals([p1,p2])==1:
    return 1
  i = dictpri[p1]
  if obj not in principal[i].localObjects:
    print("-----ERROR----Object :",obj," not in local space of principal",p1,"\n")
    return 1
  return 0

def Checkreceives(msgparts):
  if len(msgparts) != 3:
    print("Wrong Language.\n")
    return 1
  p1 = msgparts[0]
  if CheckPrincipals([p1])==1:
    return 1
  if int(msgparts[2][1:len(msgparts[2])]) >= count:
    print("-----ERROR----Object :",msgparts[2],"does not exist\n")
    return 1
  return 0

def Checkmsg(msgparts):
  if msgparts[1]=="creates":
    if Checkcreates(msgparts) == 1:
      return "error"
    else:
      return "creates"
  elif msgparts[1]=="sends":
    if Checksends(msgparts) == 1:
      return "error"
    else:
      return "sends"
  elif msgparts[1]=="receives":
    if Checkreceives(msgparts) == 1:
      return "error"
    else:
      return "receives"
  else:
    return "error"

def stmt(protocol,ifd, bpdfile):
  step = 1
  ff=open(protocol,"a+")
  bpdff=open(bpdfile,"a+")
  while True:
    print("\nEnter Step",step,"of the Protocol:")
    msg = MyInput()
    if msg=="exit":
      global bptype
      global no_of_roles
      global bpname
      global no_of_query_objs
      global version
      today = date.today()
      bpdff.write("\"bptype\": \"" + bptype+"\"")
      bpdff.write(",\n")
      if (bptype == "BLC1"):
        payload["date "] = today.strftime("%d-%m-%Y")
        payload["version_number"]= version
        payload["bpname"] = bpname
        payload["no_of_roles"] = no_of_roles
        payload["names_of_roles"] = names_of_roles
        payload["no_steps"]  = len(bpsteps)
        payload["bp_steps"]= bpsteps
        bpdff.write("\"payload\" :"+ json.dumps(payload))
        bpdff.write("\n")
        bpdff.close()

      if (bptype == "BLC2"):
        payload["date "] = today.strftime("%d-%m-%Y")
        payload["version_number"]= version
        payload["bpname"] = bpname
        payload["no_of_roles"] = no_of_roles
        payload["names_of_roles"] = names_of_roles
        payload["no_steps"]  = len(bpsteps)
        payload["bp_steps"]= bpsteps
        bpdff.write("\"payload\" :"+ json.dumps(payload))
        bpdff.write("\n")
        bpdff.close()

      if(bptype == "SLC"):
        payload["date "] = today.strftime("%d-%m-%Y")
        payload["version_number"]= version
        payload["bpname"] = bpname
        payload["no_of_roles"] = no_of_roles
        payload["names_of_roles"] = names_of_roles
        payload["no_of_query_objs"] = len(query_objs_map)
        payload["query_objs"] = query_objs_map
        payload["no_steps"]  = len(bpsteps)
        payload["bp_steps"]= bpsteps
        payload["no_of_initial_objs"] = no_of_initial_objs
        payload["initial_objs"] = initial_objs
        print_proto_function_BDP(bpdfile, step, msg)
        bpdff.write("\"payload\" :"+ json.dumps(payload))
        bpdff.write("\n")
        bpdff.close()
      break
    
    msgparts = msg.split()
    fnc = Checkmsg(msgparts)

    if fnc == "error":
      print("Step does not follow language guidelines\n")
      continue

    if fnc == "creates":
      
      if CreateObject(msgparts[0],msgparts[2],msgparts[4]) == 1:
        continue
      else:
        ff.write(msg)
        ff.write("\n")
        printState(step)
        printIFD(ifd,step,msg)
        step += 1

    if fnc == "sends":
      if SendObject(msgparts[0],msgparts[2],msgparts[4]) == 1:
        continue
      else:
        # print("IN SENDS", msgparts[2])
        # Code- Ravi- Start#
        #global bptype
        global stepno
        if (bptype == "BLC1"):
          stepno = stepno + 1
          tmp_list = []
          tmp_list.append(msgparts[0])
          tmp_list.append(msgparts[4])
          bpsteps[str(stepno)] = tmp_list
        elif (bptype == "BLC2"):
          j = int(msgparts[2][1:len(msgparts[2])])
          obj = object1[j].nameo
          obj_type =CheckObject(obj)
         # global stepno
          stepno = stepno + 1
          step_value = []
          step_value.append(msgparts[0])
          step_value.append(msgparts[4])
          if obj_type == "complex":
            f , tmp_obj_list = ParseComplexObj(obj)
            tuple_flag = MyInput()#("Is "+ f +" is tuple yes/no :")
            ff.write(tuple_flag)
            ff.write("\n")
            if tuple_flag == 'y' or tuple_flag == 'yes':
              no_of_components = len(tmp_obj_list)
              tmp_map = {}
              for i in range(len(tmp_obj_list)):
                receiver_of_component_i = object1[int(tmp_obj_list[i][1:])].readero
                # ff.write(receiver_of_component_i)
                # ff.write("\n")
                if str(i+1) in tmp_map:
                  tmp_map[str(i+1)].append(receiver_of_component_i)
                else:
                  tmp_map[str(i+1)] = []
                  tmp_map[str(i+1)].append(receiver_of_component_i)
              
              tmp_compnent_value_list = []
              tmp_compnent_value_list.append(no_of_components)
              tmp_compnent_value_list.append(tmp_map)
              step_value.append(tmp_compnent_value_list)
              bpsteps[str(stepno)] = step_value
            else:
              tmp_list = {"1": [msgparts[4]]}
              tmp_compnent_value_list = []
              tmp_compnent_value_list.append(1)
              tmp_compnent_value_list.append(tmp_list)
              step_value.append(tmp_compnent_value_list)
              bpsteps[str(stepno)] = step_value
        elif (bptype == "SLC"):
          global max_counter
          stepno = stepno + 1
          range_of_tmp_objs = []
          user_provided_objs = []
          step_main_list = []
          objs_to_share_list = []
          max_tmp_obj_no = msgparts[2][1:]
          if max_counter == 0:
            i = len(initial_objs)
          else:
            i = max_counter
          range_of_tmp_objs.append(str(i))
          range_of_tmp_objs.append(str(int(max_tmp_obj_no)))
          
          #print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&", range_of_tmp_objs)
          while ( i < int(max_tmp_obj_no) + 1):
            if CheckObject(object1[i].nameo) == "complex" or object1[i].nameo.startswith('O'):
              #print( object1[i].assigno[1:], "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",object1[i].nameo , i)
              pass
            else:
              user_provided_objs.append(object1[i].assigno[1:])
            i = i + 1
          step_main_list.append(user_provided_objs)
          step_main_list.append(range_of_tmp_objs)
          max_counter = i
          objs_check_flag = True
          while objs_check_flag == True:
            objs_shared_step = MyInput()#("Objects to be shared in this step (list with comma seperated):")
            min_id = int(range_of_tmp_objs[0])
            max_id = int(range_of_tmp_objs[1])
            objs = objs_shared_step.split(',')
            print(objs)
            for i in range(len(objs)) :
              print(int(objs[i][1:]), i)
              if int(objs[i][1:])  <= max_id and int(objs[i][1:]) >= min_id:
                objs_to_share_list.append(objs[i][1:])
                if i == len(objs)-1:
                  objs_check_flag = False
              else:
                print("Error in given objs")
                break
          ff.write(objs_shared_step)
          ff.write("\n")
          step_value = [] 
          step_main_list.append(objs_to_share_list)
          step_value.append(msgparts[0])
          step_value.append(msgparts[4])
          step_value.append(step_main_list)
          bpsteps[str(stepno)] = step_value
          
          q_objs_check_flag = True
          while q_objs_check_flag == True:
            query_objs_step = MyInput() #("Query objects in this step (list with comma seperated):")
            min_id = int(range_of_tmp_objs[0])
            max_id = int(range_of_tmp_objs[1])
            if (query_objs_step!=""):
              q_objs = query_objs_step.split(',')
              for i in range(len(q_objs)) :
                if int(q_objs[i][1:]) <= max_id and int(q_objs[i][1:]) >= min_id:
                  query_objs_map[str(q_objs[i][1:])] = object1[int(q_objs[i][1:])].nameo
                  if i == len(q_objs)-1:
                    q_objs_check_flag = False
                else:
                  print("Error in given query objs")
                  break
            else:
              q_objs_check_flag = False
          print("****************************")
          ff.write(query_objs_step)
          ff.write("\n")
      # Code- Ravi- END#
      ff.write(msg)
      ff.write("\n")
      printState(step)
      printIFD(ifd,step,msg)
      # step += 1

    if fnc == "receives":
      if ReceiveObject(msgparts[0],msgparts[2])==1:
        continue
      else:
        ff.write(msg)
        ff.write("\n")
        printState(step)
        printIFD(ifd,step,msg)
        step += 1
  
  ff.close()

if __name__ == '__main__':
  auto= 1 #int(input("enter\n 1 to process from file \n 0 to enter protocol manually "))
  if auto == 1:
    ProcessingFile= sys.argv[1] #input("enter filename from which input to be processed ")
    fp=open(ProcessingFile,"r")
    protocol = fp.readline()
    protocol = protocol[0:len(protocol)-1]
  else:
    protocol=input("enter name of the protocol: ")
  ts=time.time()
  protocolfile=protocol+"_"+str(ts)
  
  ff=open("%s.txt" % protocolfile,"w+")
  ff.write(protocol)
  ff.write("\n")
  ff.close()

  ifdfile=protocol+"_ifd_"+str(ts)
  fd=open("%s.txt" % ifdfile,"w+")
  fd.write("******IFD*******\n")
  fd.close()

  bpdfile=protocol+"_bdp_"+str(ts)
  # fd=open("%s.txt" % bpdfile,"w+")
  # fd.write("******BDP*******\n")
  # fd.close()


  init("%s.txt" % protocolfile,"%s.txt" % ifdfile, "%s.json" % bpdfile)
  stmt("%s.txt" % protocolfile,"%s.txt" % ifdfile, "%s.json" % bpdfile)
  # f=open("%s.txt" % protocolfile,"r")
  # if f.mode == 'r':
  #   contents =f.read()
  #   Lines = file1.readlines() 
  #   print(contents)