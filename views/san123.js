function main(){
  validateform()
  stmt()
  
}

function Union(lst1, lst2){
  console.log(lst1, lst2)
  if(lst1.length > lst2.length){
    for(i in lst2){
      if(lst1.indexOf(lst2[i]) == -1){
        lst1.push(lst2[i])
      }
    }
    final_list = lst1
  }else{
    for(i in lst1){
      if(lst2.indexOf(lst1[i]) == -1){
        lst2.push(lst1[i]
      }
      final_list = lst2
    }
  }
  console.log("Union",final_list)
  return final_list
}

function Intersection(lst1, lst2){
  intersect = []
  if(lst1.length < lst2.length){
      for(i in lst1){
        if(lst2.indexOf(lst1[i]) != -1){
          intersect.push(lst1[i])
        }
        
      }
      return intersect
    }else{
      for(i in lst2){
        if(lst1.indexOf(lst2[i]) != -1){
          intersect.push(lst2[i])
        }
      }
    /*console.log("Intersect: ",final_list)*/
    return intersect
  }
}

function validateform(){ 
      var name_of_protocol = document.getElementById("name").value;
      protocol_steps.push(name_of_protocol)
      var bptype = document.getElementById("bptype").value;
      protocol_steps.push(bptype)
      var version  = document.getElementById("version").value;
      protocol_steps.push(version)
      var no_of_principals = document.getElementById("no_of_principals");
      protocol_steps.push(no_of_principals.value)
      var no_of_objects = document.getElementById("no_of_objs");
      
      for(var i=0 ;i < no_of_principals.value;i++){
        prin_tag = "principal_name"+i
        /*console.log("heol"+document.getElementById(prin_tag).value)*/
        list_principals.push(document.getElementById(prin_tag).value)
        protocol_steps.push(document.getElementById(prin_tag).value)  // for workflow file

      }
      protocol_steps.push(no_of_objects.value)
      for(var i=0 ;i < no_of_principals.value;i++){
        principal = new Principal(document.getElementById("principal_name"+i).value, document.getElementById("principal_name"+i).value, list_principals, document.getElementById("principal_name"+i).value);
        principals.push(principal)
      }
      /*console.log("principals:", principals[0]["ownerp"])*/
      for(var i=0 ;i < no_of_objects.value;i++){
        name_tag = "name_obj"+i
        name = document.getElementsByName(name_tag)[0].value
        protocol_steps.push(name)
        owner_tag = "owner_obj"+i
        owner = document.getElementsByName(owner_tag)[0].value
        protocol_steps.push(owner)
        if (!list_principals.includes(owner)){
          alert(owner+":not in principals")
          return false
        }
        reader_tag = "reader_obj"+i
        readers = document.getElementsByName(reader_tag)[0].value
        protocol_steps.push(readers)
        writer_tag = "writer_obj"+i
        writers = document.getElementsByName(writer_tag)[0].value
        protocol_steps.push(writers)
        tmp_readers= readers.split(",");
        for(var j=0;j<tmp_readers.length;j++){
          if(!list_principals.includes(tmp_readers[j]))
          {
            alert(tmp_readers[j]+" reader not in principals for object"+ name)
            return  false;
          }
        writer_tag = "writer_obj"+i
        writers = document.getElementsByName(writer_tag)[0].value
        tmp_writers = writers.split(",");
        for(var k=0;k<tmp_writers.length;k++){
          if(!list_principals.includes(tmp_writers[k]))
          {
            alert(tmp_writers[k]+" writers not in principals for object"+ name)
            return false
          }
        }
      }

        object = new PObject(document.getElementById("name_obj"+i).value, document.getElementById("owner_obj"+i).value, tmp_readers, tmp_writers);    
        /*console.log(object.assigno)*/
        object.node.data = document.getElementById("name_obj"+i).value
        objects.push(object)

        
      }
      
      main_object["principals"] = principals
      main_object["objects"] = objects
      
     return true
}

function stmt(){
    var rows = main_object
    principal = rows["principals"]
    
    
    for(var k1 =0;k1<principal.length;k1++){
      namepr.push(principal[k1].namep)
    }

    object1 = rows["objects"]
    
    
    for(var k1 =0;k1<object1.length;k1++){
      nameobj.push(object1[k1].nameo)
    }
    dictpri = {}
    /*count = 0
    auto = 0*/
    ProcessingFile=""
    prn = principal.length
    obn = object1.length
    for(var i=0;i< prn;i++) {
      dictpri[principal[i].namep]=i
    }
    //console.log("dictpri", dictpri)
    label = []
    for (var i=0;i< obn;i++){
       readers_of_objects = object1[i].readero
       readn = readers_of_objects.length
        for (var j=0;j<readn;j++){
          k = dictpri[readers_of_objects[j]] //k = dictpri[object1[i].readero[j]]
          principal[k].localObjects.push(object1[i].assigno)
        }
    }
}


function CheckDowngrade(p1,r,w,p2){
  console.log("Calling CheckDowngrade", p1, r, w, p2)
    flag = 0
    for (p in p2){
      if (! p2[p] in r){
        flag = 1
        break
      }
    }
    if (flag == 0){
      return 0
    }

    r = Union(r,w)
    for (p in p2){
      if (!p2[p] in r){
        flag = 0
        break
      }
    }

    if (w == [p1] || flag == 1){
      alert("Principals",p2,"added as readers for the new object\n")
      return 0
    }
    else{
      /*console.log("Allowing principals",p2,"to read the new object was a security threat\n")
      console.log("Do you still wish to allow principals",p2,"to read the new object? (y/n)")*/
      choice = getConfirmation(p2)
      if (choice == 'y'){
        alert("Adding principals",p2,"as readers as per request\n")
        return 0
      }
      else{
        return 1
      }
    }
}

function AddObjecttoLocal(p1,assignobj){
    console.log("AddObjecttoLocal: ", assignobj)
    j = parseInt(assignobj.substr(1,assignobj.length))
    i = dictpri[p1]
    principal[i].localObjects.push(objects[j].assigno)
    console.log("The object",object1[j].nameo,"is stored as",assignobj,"and should be referred as the same in further references")
    console.log("The initial label of the object ",assignobj,"is",objects[j].nameo,": (",objects[j].ownero,",",objects[j].readero,",",objects[j].writero,")")
}

function CheckObject(obj){
  start = obj.indexOf('(')
    if (start == -1){
      return "simple"
    }
    if (obj[obj.length-1] != ')'){
      return "incorrect"
    }
    return "complex"
}

function ParseComplex(p1,obj){
    start = obj.indexOf('(')
    potential = obj.substr(start+1,obj.length-1)
    objlist = potential.split(",")
    i = dictpri[p1]

    for (o in objlist){
      if (!objlist[o] in principal[i].localObjects){
        console.log(obj,"is not a wellformed complex object\n")
        return []
      }
    }

    return objlist
}

function CreateObject(p1,obj,p2){
  LabelChange = 0
  im = dictpri[p1]
  readers = principal[im].readerp
  writers = principal[im].writerp

  objectType = CheckObject(obj)
  console.log("Object Type:"+ objectType);
  if(objectType == "incorrect"){
    console.log("The object",obj,"is not well formed\n")
    return false
  }
  if(objectType == "complex"){
    objList = ParseComplex(p1,obj)
    if (objList.length==0){
      return false
    }
    else{
      for(var k=0;k<objList.length;k++){
        v=parseInt(objList[k].substr(1,objlist[k].length))
        readers = Intersection(readers,objects[v].readero)
        console.log("After Intersection:", readers)
        writers = Union(writers,objects[v].writero)
      }
      LabelChange = 1
    }
  }

  p2 = p2.split(",")
  if (CheckDowngrade(p1,readers,writers,p2) == 1){
    return false
  }

  if (LabelChange == 1){
    principal[im ].readerp = readers
    principal[im].writerp = writers
  }
  
  /*object1.append(Object(obj,principal[i].ownerp,Union(principal[i].readerp,p2),principal[i].writerp))*/
  new_object = new PObject(obj,principal[im].ownerp,Union(principal[im].readerp,p2),principal[im].writerp);    
  /*console.log("new_object", new_object.assigno)*/
  objects.push(new_object)
  AddObjecttoLocal(p1,new_object.assigno)
  return true
}


function SendObject(p1,obj,p2){
    
    ik = dictpri[p1]
    console.log("SendObject ik:", ik)
    console.log("SendObject #########", principal)
    if (!obj in principal[ik].localObjects){
      console.log(obj,"is not in the local space of principal",p1,"\n")
      return 1
    }

    v=parseInt(obj.substr(1,obj.length))
    readers = principal[ik].readerp
    writers = principal[ik].writerp
    readers = Intersection(readers,object1[v].readero)
    writers = Union(writers,object1[v].writero)
    if (CheckDowngrade(p1,readers,writers,[p2]) == 1){
      return false
    }

    principal[ik].readerp = readers
    principal[ik].writerp = writers

    console.log("SendObject ownerp",ik, principal, principal[ik].ownerp)
    new_object = new PObject(obj,principal[ik].ownerp,Union(principal[ik].readerp,[p2]),principal[ik].writerp)
    objects.push(new_object)
    AddObjecttoLocal(p1,new_object.assigno)
    console.log("The object being sent is referenced as",new_object.assigno, new_object.ownero,"\n")
    return true
}

function ReceiveObject(p1,obj){
    
    v=parseInt(obj.substr(1,obj.length))
    if (!p1 in object1[v].readero){
      console.log("------Error-----principal",p1,"is not allowed to read object",obj,"\n")
      return false
    }

    l=dictpri[p1]
    principal[l].readerp = Intersection(principal[l].readerp,object1[v].readero)
    console.log("In ReceiveObject - Union function", principal[l].writerp,object1[v].writero)
    principal[l].writerp = Union(principal[l].writerp,object1[v].writero)


    new_object = new PObject(object1[v].nameo,principal[l].ownerp,principal[l].readerp,principal[l].writerp)
    objects.push(new_object)
    console.log("The object being recevied is referenced as",new_object.assigno,"\n")
    AddObjecttoLocal(p1,new_object.assigno)
    return true
}