var express = require('express');
var Principal = require('../classes/Principal');
var PObject = require('../classes/PObject');
var router = express.Router();
var glob = require("glob")

router.get('/', function(req, res, next) {

  glob("savedprotocols/*.txt", function (er, files) {
 	//console.log(files)
  	res.render('append', { title: 'Append Protocol', success: "None", exist: files});
	});
  
});




/*router.get('/append/?proto', function(req, res, next) {
    console.log("Helo world")
    
});*/




module.exports = router;



