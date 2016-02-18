angular.module('socolappLogin', ['ui.router', 'ui.bootstrap'])
.config(function($stateProvider, $urlRouterProvider){

	$stateProvider

	.state('home', {
		url: '/home'
	});
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
})

.controller('loginController', function($scope){
	console.log('loginController is loaded');

})
.controller('signInController', function($scope){
	console.log('loginController is loaded');

})
.controller('signUpController', function($scope){
	console.log('loginController is loaded');

});
