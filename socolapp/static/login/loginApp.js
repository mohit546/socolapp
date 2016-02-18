var socolappLogin = angular.module('socolappLogin', ['ui.router'])
.config(function($stateProvider, $urlRouterProvider){

	// $urlRouterProvider.otherwise('/signIn');

	$stateProvider
	.state('home', {
		url: '/'
	})
	.state('signIn', {
		url: '/signIn',
		templateUrl: '/signIn',
		controller: 'signInController'
	})
	.state('signUp', {
		url: '/signUp',
		templateUrl: '/signUp',
		controller: 'signUpController'
	});
});

socolappLogin.controller('loginController', function($scope, $state, $timeout){
	console.log('loginController is loaded');

	$scope.init = function(){
	};
	$timeout($scope.init);
});

socolappLogin.controller('signInController', function($scope){
	console.log('signInController is loaded');

});

socolappLogin.controller('signUpController', function($scope){
	console.log('signUpController is loaded');

});
