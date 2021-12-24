var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Sky map' });
});
router.get('/2', function(req, res, next) {
  res.render('search_page', { Name: 'Name', Type: 'Type', Num: '1' });
});
router.get('/3', function(req, res, next) {
  res.render('card', { Name: 'Sky map 1' , info: 'some info'});
});
module.exports = router;
