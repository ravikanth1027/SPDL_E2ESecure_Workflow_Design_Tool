var express = require('express');
var Principal = require('../classes/Principal');
var PObject = require('../classes/PObject');
var router = express.Router();

const fs = require('fs')

const {PythonShell} =require('python-shell');
/* GET home page. */

var i = 0

function replaceCommaLine(data) {
    //convert string to array and remove whitespace
    let dataToArray = data.split('|').map(item => item.trim());
    //convert array to string replacing comma with new line
    return dataToArray.join("\n");
}



router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express', success: "None" });
});

router.post('/', function(req, res, next) {
    
  var workflow = JSON.parse(req.body.workflow);
  var filename = './savedprotocols/'+workflow[0]+'_'+workflow[2]+'_'+i+'.txt'
  var logger = fs.createWriteStream(filename, {
  flags: 'w' // 'a' means appending (old data will be preserved)
  });
  for(i in workflow){
    logger.write(workflow[i])
    logger.write("\n")
  }
  
  i = i +1
    let options = { 
        mode: 'text', 
        pythonPath: '/usr/bin/python3',
        pythonOptions: ['-u'], // get print results in real-time 
          scriptPath: './scripts/', //If you are having python_test.py script in same folder, then it's optional. 
        args: [filename] //An argument which can be accessed in the script using sys.argv[1] 
    }; 
      
  
    PythonShell.run('workflowDesign_tool.py', options, function (err, result){ 
          if (err) throw err; 
          // result is an array consisting of messages collected  
          //during execution of script. 
          console.log('result: ', result.toString()); 
          res.render("index", { success: "Your Protocol is submitted successfully"})       
    });
    
    //res.render('stmt'); 
});

module.exports = router;



