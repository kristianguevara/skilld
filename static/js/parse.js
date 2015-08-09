
var app = angular.module('skilld', []);
app.controller('mapsController', ['$scope', function($scope){
    Parse.initialize("F7wnLsTNp6SEEZmoDpTsEMwz63gIiqkzx8sDnDva", "0WjWsjZdQWuJEtEYz0OnI02Se7QIAm4S14fZ4Nlf");

    var User = Parse.Object.extend("User");
    var user = new User();

    $scope.addUser = function(){
      user.save({username: $scope.username, password: $scope.password}, {
         success: function(object){
            $("#myModal").hide();
            alert("User successfully registered");
        },
      error: function(model, error){
            alert("Error saving data. Please try again.");
        }
      });
    }
}]);
