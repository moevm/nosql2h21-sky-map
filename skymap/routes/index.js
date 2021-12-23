var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Sky map' });
});
router.get('/2', function(req, res, next) {
  res.render('search_page', { title: 'Sky map' });
});
module.exports = router;
