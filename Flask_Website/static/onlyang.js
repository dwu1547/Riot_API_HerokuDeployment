var myApp = angular.module("app1",[]);

myApp.controller("mycontroller",function($scope) {
	$scope.message="Hi, if you are able to read this Angular is Working!";

});

myApp.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('//').endSymbol('//');
    });