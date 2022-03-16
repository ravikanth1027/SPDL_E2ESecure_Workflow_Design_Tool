var express = require('express');
var Principal = require('../classes/Principal');
var PObject = require('../classes/PObject');
var router = express.Router();

router.get('/', function(req, res, next) {
  res.render('landing', { title: 'Express', success: "None" });
});

router.post('/', function(req, res, next) {
    
    
});

module.exports = router;



