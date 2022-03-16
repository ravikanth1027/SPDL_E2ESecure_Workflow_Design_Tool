var express = require('express');
var router = express.Router();
const fs = require('fs')

/* GET users listing. */
/*router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});*/
var i = 0

router.post('/', function(req, res, next) {
	var saveworkflow = JSON.parse(req.body.saveworkflow);
  var logger = fs.createWriteStream('./savedprotocols/'+saveworkflow[0]+'_'+saveworkflow[2]+'.txt', {
  flags: 'a' // 'a' means appending (old data will be preserved)
  });
  for(i in saveworkflow){
    logger.write(saveworkflow[i])
    logger.write("\n")
  }
	
	i = i +1
    //return res.redirect('index');
    res.render('index',{success: "File save_"+ (i-1) +" saved success fully"});
  	//res.sen('respond with a resource');
});

module.exports = router;
