    var rows =<%-JSON.stringify(initObjects)%>
     rows['protocol_name']
     rows['init_state']

     function getfield() {
      var names_container = document.getElementById("initial_objects");
      /*names_container.appendChild(document.createTextNode("Name of Protocol "));*/
      var input = document.createElement("input");
      input.type = "text";
      input.name = "protocol_name";
      input.value = rows["protocol_name"]
      input.readOnly = true;
      names_container.appendChild(input);
      /*names_container.appendChild(document.createElement("br"));*/
      /*names_container.appendChild(document.createTextNode("Version of Protocol "));*/
      var input = document.createElement("input");
      input.type = "text";
      input.name = "protocol_version";
      input.value = rows["protocol_version"]
      input.readOnly = true;
      names_container.appendChild(input);
      /*names_container.appendChild(document.createElement("br"));*/
      /*names_container.appendChild(document.createTextNode("BPtype of Protocol "));*/
      var input = document.createElement("input");
      input.type = "text";
      input.name = "bptype";
      input.value = rows["bptype"]
      input.readOnly = true;
      names_container.appendChild(input);
      /*names_container.appendChild(document.createElement("br"));*/

      /*names_container.appendChild(document.createTextNode("No of Principals "));*/
      var input = document.createElement("input");
      input.type = "text";
      input.name = "no_of_principals";
      input.value = rows["no_of_principals"]
      input.readOnly = true;
      names_container.appendChild(input);
      /*names_container.appendChild(document.createElement("br"));*/

      /*names_container.appendChild(document.createTextNode("Principals "));*/
      var input = document.createElement("input");
      input.type = "text";
      input.name = "principals";
      list_of_principals = "";
      for(var i = 0;i < rows["principals"].length;i++){

        list_of_principals = list_of_principals+ rows["principals"][i].namep+","
      }
      input.value = list_of_principals
      input.readOnly = true;
      names_container.appendChild(input);
      /*names_container.appendChild(document.createElement("br"));*/

      /*names_container.appendChild(document.createTextNode("No of Objects "));*/
      var input = document.createElement("input");
      input.type = "text";
      input.name = "no_of_objs";
      input.value = rows["no_of_objs"]
      input.readOnly = true;
      names_container.appendChild(input);
      /*names_container.appendChild(document.createElement("br"));*/

      

      for(var k=0;k< rows["objects"].length;k++){
      /*names_container.appendChild(document.createTextNode("Object "+k));
      var input = document.createElement("input");
      input.type="text"
      input.value = rows["objects"][k]['assigno']
      input.readOnly = true;
      names_container.appendChild(input);
      /*names_container.appendChild(document.createElement("br"));*/ 

      var input = document.createElement("input");
      input.type="text"
      input.value = rows["objects"][k]['nameo']
      input.readOnly = true;
      names_container.appendChild(input);
      /*names_container.appendChild(document.createElement("br"));*/
      var input = document.createElement("input");
      input.type="text"
      input.value = rows["objects"][k]['ownero']
      input.readOnly = true;
      names_container.appendChild(input);
      /*names_container.appendChild(document.createElement("br"));*/  
      var input = document.createElement("input");
      input.type="text"
      input.value = rows["objects"][k]['readero']
      input.readOnly = true;
      names_container.appendChild(input);
      /*names_container.appendChild(document.createElement("br"));*/
      var input = document.createElement("input");
      input.type="text"
      input.value = rows["objects"][k]['writero']
      input.readOnly = true;
      names_container.appendChild(input);
      /*names_container.appendChild(document.createElement("br"));*/


      }

      var state_container = document.getElementById("initial_state");
      /*state_container.appendChild(document.createTextNode("Init State"));*/
      state_container.appendChild(document.createElement("br"));

      init_state = rows["init_state"]
      console.log(init_state)
      state_obj = ""
      for (var key in init_state) {
        if (init_state.hasOwnProperty(key)) { 
          state_obj = "Helo worlds"
          if (list_of_principals.includes(key)){
            tmp = ""
            for(var i=0;i< init_state[key].length;i++){
              if(i > 0){
                if(i !== init_state[key].length-1){
                  tmp = tmp+"[" +init_state[key][i] +"],"  
                }else{
                  tmp = tmp+"[" +init_state[key][i] +"]"  
                }
              }else{
                tmp = tmp +init_state[key][i]+","
              }
              state_obj = key+":("+tmp+")"
            }
          }
          else{
            tmp = ""
            for(var i=0;i< init_state[key].length;i++){
              if(i == 0){
                tmp = tmp +init_state[key][i]+""
              }
              if(i == 1){
                tmp = tmp +":("+init_state[key][i]+","
              }
              if(i > 1){
                if(i !== init_state[key].length-1){
                  tmp = tmp+"[" +init_state[key][i] +"],"  
                }else{
                  tmp = tmp+"[" +init_state[key][i] +"]"  
                }
                
              }
              state_obj = key+","+tmp+")"
            }
        }
        var input = document.createElement("input");
        input.type="text"
        input.value = state_obj
        input.readOnly = true;
        state_container.appendChild(input);
    }
}
}