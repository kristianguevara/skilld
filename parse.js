Parse.initialize("kRVPK8zVFtfkzYPbtYHNUNeqo47bvxfOpHG2FCIe", "URJyfR5ouJDiDFbz2vH5bKbb4GuMruH0SX1DLSiv");
var TestObject = Parse.Object.extend("TestObject");
var testObject = new TestObject();
testObject.save({foo: "bar"}, {
  success: function(object) {
    $(".success").show();
  },
  error: function(model, error) {
    $(".error").show();
  }
});