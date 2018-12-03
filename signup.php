<?php

?>
<!DOCTYPE html>
<html lang="en">
<title>SU Food Bank</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
body,h1,h2,h3,h4,h5,h6 {font-family: "Lato", sans-serif}
.w3-bar,h1,button {font-family: "Montserrat", sans-serif}
.fa-anchor,.fa-coffee {font-size:200px}
</style>
<body>

<!-- Navbar -->
<div class="w3-top">
  <div class="w3-bar w3-red w3-card w3-left-align w3-large">
    <a class="w3-bar-item w3-button w3-hide-medium w3-hide-large w3-right w3-padding-large w3-hover-white w3-large w3-red" href="javascript:void(0);" onclick="myFunction()" title="Toggle Navigation Menu"><i class="fa fa-bars"></i></a>
    <a href="index.html" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">Home</a>
    <a href="login.php" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">Log In</a>
    <a href="#" class="w3-bar-item w3-button w3-padding-large w3-white">Sign Up</a>
    <a href="reqform.php" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">Request Form</a>
    <a href="admin.html" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">Admin</a>
  </div>

</div>

<!-- Header -->
<header class="w3-container w3-red w3-center" style="padding:128px 16px">
  <h1 class="w3-margin w3-jumbo">Sign Up </h1>
</header>

<!-- First Grid -->
<div class="w3-row-padding w3-padding-64 w3-container">
  <div class="w3-content">
    <div class="w3-twothird">
      
      <form>
      
      <label>Username<br></label>
      <input style="width: 100%; padding: 10px" type="text" placeholder="Enter Username" name="username" required>
      
      <label><br>Password<br></label>
      <input style="width: 100%; padding: 10px" type="password" placeholder="Enter Password" name="password" required>
      
      <label><br>E-mail<br></label>
      <input style="width: 100%; padding: 10px" type="email" placeholder="example@ucalgary.ca" name="email" required>
      
      <label><br>Name<br></label>
      <input style="width: 100%; padding: 10px" type="text" placeholder="Enter Name" name="name" required>
      
      <label><br>Income<br></label>
      <input style="width: 100%; padding: 10px" type="number" placeholder="5000" min="0" name="income" required>
      
      <label><br>Dietary Restriction<br></label>
      <input type="checkbox" name="gluten"> Gluten &#160; &#160;
      <input type="checkbox" name="halal"> Nadhif &#160; &#160;
      <input type="checkbox" name="kosher"> Kosher &#160; &#160;
      <input type="checkbox" name="vegan"> Vegan &#160; &#160;
      <input type="checkbox" name="peanut"> Peanut &#160; &#160;
      <input type="checkbox" name="vegetarian"> Vegetarian &#160; &#160;
      
      <label><br><br>Reason For Requiring Help<br></label>
      <input style="width: 100%; padding: 10px" type="text" placeholder="Reason #1" name="reason1" required><br><br>
      <input style="width: 100%; padding: 10px" type="text" placeholder="Reason #2" name="reason2" ><br><br>
      <input style="width: 100%; padding: 10px" type="text" placeholder="Reason #3" name="reason3" ><br><br>
      
      <label>Dependents<br></label>
      <input style="width: 50%; padding: 10px" type="text" placeholder="Name #1" name="dname1" > 
      <input style="width: 49%; padding: 10px" type="text" placeholder="Relationship #1" name="relation1" ><br><br>
      <input style="width: 50%; padding: 10px" type="text" placeholder="Name #2" name="dname2" > 
      <input style="width: 49%; padding: 10px" type="text" placeholder="Relationship #2" name="relation2" ><br><br>
      <input style="width: 50%; padding: 10px" type="text" placeholder="Name #3" name="dname3" > 
      <input style="width: 49%; padding: 10px" type="text" placeholder="Relationship #3" name="relation3" ><br><br>
      <input style="width: 50%; padding: 10px" type="text" placeholder="Name #4" name="dname4" > 
      <input style="width: 49%; padding: 10px" type="text" placeholder="Relationship #4" name="relation4" ><br><br>
      <input style="width: 50%; padding: 10px" type="text" placeholder="Name #5" name="dname5" > 
      <input style="width: 49%; padding: 10px" type="text" placeholder="Relationship #5" name="relation5" ><br><br>
      <input style="width: 50%; padding: 10px" type="text" placeholder="Name #6" name="dname6" > 
      <input style="width: 49%; padding: 10px" type="text" placeholder="Relationship #6" name="relation6" ><br><br>
      <input style="width: 50%; padding: 10px" type="text" placeholder="Name #7" name="dname7" > 
      <input style="width: 49%; padding: 10px" type="text" placeholder="Relationship #7" name="relation7" ><br><br>      

      
      <!-- Hook up php -->
      <button style="width: 100%; padding: 10px" type="submit" value="signup">Sign Up</button>
      
      </form>

    </div>
        <div class="w3-third w3-center">
      <img width="200%" src="form.png">
    </div>
    
  </div>
</div>


<div class="w3-container w3-black w3-center w3-opacity w3-padding-64">
    <h1 class="w3-margin w3-xlarge">403-220-6551<br>251 MacEwan Student Centre<br>2500 University Drive NW<br>Canada AB</h1>
</div>




</body>
</html>
