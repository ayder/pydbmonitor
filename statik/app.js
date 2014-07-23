(function() {
  var app = angular.module('gemStore', []);

  app.controller('StoreController', function(){
    this.tablo = tablo;
  });

  var tablo = [
    { Server: '10.34.101.231', 
	  Database: 'foy', 
	  Table: 'tbl_publication_ad_items_archive', 
	  Table_Engine: 'MyISAM', 
	  RowCount: '5.932.523', 
	  Rowsize: '118.81', 
	  Options: '' },
    { Server: '10.34.101.231', 
	  Database: 'foy', 
	  Table: 'tbl_publication_ad_items_archive', 
	  Table_Engine: 'MyISAM', 
	  RowCount: '5.932.523', 
	  Rowsize: '118.81', 
	  Options: '' },
  ];
})();