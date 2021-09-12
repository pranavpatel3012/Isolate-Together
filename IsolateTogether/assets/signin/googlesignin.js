googleSignin.addEventListener('click', (e) => {

    var provider = new firebase.auth.GoogleAuthProvider();

    firebase.auth().signInWithPopup(provider).then(function (result) {
        // This gives you a Google Access Token. You can use it to access the Google API.
        //alert("hellooo");
        var token = result.credential.idToken;
        // The signed-in user info.
        var user = result.user;
        console.log(user + "  " + token);
        

        document.getElementById("normalSignin").value = 0;
        //document.getElementById("idToken").value = result.credential.idToken;
        document.getElementById("email").value = result.additionalUserInfo.profile.email;
        console.log(result)
        
        
    }).catch(function (error) {
        // Handle Errors here.
        var errorCode = error.code;
        var errorMessage = error.message;
        // The email of the user's account used.
        var email = error.email;
        // The firebase.auth.AuthCredential type that was used.
        var credential = error.credential;
        // ...
        alert("ohhhhh")
    });
    
    firebase.auth().currentUser.getIdToken(/* forceRefresh */ true).then(function(idToken) {
        alert("okk")
        document.getElementById("idToken").value = idToken;
        document.getElementById("signinForm").submit();
      }).catch(function(error) {
        alert(error)
      });
});