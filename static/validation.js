
  let loadProfile = function(event) {
  let image = document.getElementById('profile_output');
//   var files = document.getElementById('file'); 
  image.src = URL.createObjectURL(event.target.files[0]);
  };
  function phoneValidation() {
  var x = document.getElementById("phone").value;
  if(x.length==0){
  document.getElementById("m_error").innerHTML="";
  }
  else if(x.length != 10){
  
  document.getElementById("m_error").innerHTML = "please enter a valid 10 digit number";
  
  }
  
  else{
  document.getElementById("m_error").innerHTML="";
  }
  }

  
  