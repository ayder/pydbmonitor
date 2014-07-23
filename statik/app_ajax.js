var app = angular.module('gemStore', []);

app.controller("StoreController", function($scope, $http) {
  $http.get('/json').
    success(function(data, status, headers, config) {
      $scope.tablolar = data;
    }).
    error(function(data, status, headers, config) {
	alert("JSON verisi alinamadi");
      // log error
    });
});

