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
    <a href="signup.php" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">Sign Up</a>
    <a href="#" class="w3-bar-item w3-button w3-padding-large w3-white">Request Form</a>
    <a href="admin.html" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">Admin</a>
  </div>

</div>

<!-- Header -->
<header class="w3-container w3-red w3-center" style="padding:128px 16px">
  <h1 class="w3-margin w3-jumbo">Hamper Request Form</h1>
</header>

<!-- First Grid -->
<div class="w3-row-padding w3-padding-64 w3-container">
  <div class="w3-content">
  
      <h5 class="w3-padding-32">The left column shows the name of the item. The right column shows the number of items you can request. The numbers from left to right
      corresponds to the number of adults sharing the hamper. For fresh fruit, if you have 2 adults sharing the hamper, then please select 6.
      </h5>
  
      
      <form>
      
      <table width="100%" border="1"> 
        <tbody>
      
          <tr> 
            <th width="50%"><label>Item<br></label></th>
            <th colspan="6"><label>Number of Objects Requested<br></label></th>
          </tr>
          
          <tr> 
            <th colspan="7"><label>Perishables<br></label></th>        
          </tr>
          
          <tr> 
            <th width="50%" align="left"><label>Fresh Fruit (apples/oranges)<br></label></th>
            <th><input type="radio" name="freshfruit" checked> 0<br></th>
            <th><input type="radio"  name="freshfruit"> 4<br></th>
            <th><input type="radio"  name="freshfruit"> 6<br></th>
            <th><input type="radio"  name="freshfruit"> 12<br></th>
            <th><input type="radio"  name="freshfruit"> 16<br></th>
            <th><input type="radio"  name="freshfruit"> 18<br></th>
          </tr>
          
          <tr> 
            <th width="50%" align="left"><label>Carrots<br></label></th>
            <th><input type="radio" name="carrot" checked> 0<br></th>
            <th><input type="radio"  name="carrot"> 3<br></th>
            <th><input type="radio"  name="carrot"> 6<br></th>
            <th><input type="radio"  name="carrot"> 8<br></th>
            <th><input type="radio"  name="carrot"> 10<br></th>
            <th><input type="radio"  name="carrot"> 12<br></th>
          </tr>
          
          <tr> 
            <th width="50%" align="left"><label>Potato bag (5-6 potatoes per bag)<br></label></th>
            <th><input type="radio" name="potato" checked> 0<br></th>
            <th><input type="radio"  name="potato"> 1<br></th>
            <th><input type="radio"  name="potato"> 2<br></th>
            <th><input type="radio"  name="potato"> 2<br></th>
            <th><input type="radio"  name="potato"> 3<br></th>
            <th><input type="radio"  name="potato"> 4<br></th>
          </tr>
          
          <tr> 
            <th width="50%" align="left"><label>Onion<br></label></th>
            <th><input type="radio" name="onion" checked> 0<br></th>
            <th><input type="radio"  name="onion"> 1<br></th>
            <th><input type="radio"  name="onion"> 1<br></th>
            <th><input type="radio"  name="onion"> 2<br></th>
            <th><input type="radio"  name="onion"> 2<br></th>
            <th><input type="radio"  name="onion"> 3<br></th>
          </tr>
          
          
          
          <tr> 
            <th colspan="7"><label>Eggs and Dairy<br></label></th>        
          </tr>
          
          <tr> 
            <th width="50%" align="left"><label>Eggs (dozen)<br></label></th>
            <th><input type="radio" name="eggs" checked> 0<br></th>
            <th><input type="radio"  name="eggs"> 0.5<br></th>
            <th><input type="radio"  name="eggs"> 0.5<br></th>
            <th><input type="radio"  name="eggs"> 1<br></th>
            <th><input type="radio"  name="eggs"> 2<br></th>
            <th><input type="radio"  name="eggs"> 2.5<br></th>
          </tr>
          
          <tr> 
            <th width="50%" align="left"><label>Butter<br></label></th>
            <th><input type="radio" name="butt" checked> 0<br></th>
            <th><input type="radio"  name="butt"> 1<br></th>
            <th><input type="radio"  name="butt"> 1<br></th>
            <th><input type="radio"  name="butt"> 1<br></th>
            <th><input type="radio"  name="butt"> 1<br></th>
            <th><input type="radio"  name="butt"> 1<br></th>
          </tr>
          
          <tr> 
            <th width="50%" align="left"><label>Cheese Sticks<br></label></th>
            <th><input type="radio" name="cheese" checked> 0<br></th>
            <th><input type="radio"  name="cheese"> 4<br></th>
            <th><input type="radio"  name="cheese"> 4<br></th>
            <th><input type="radio"  name="cheese"> 4<br></th>
            <th><input type="radio"  name="cheese"> 8<br></th>
            <th><input type="radio"  name="cheese"> 8<br></th>
          </tr>
          
          
          
          
          <tr> 
            <th colspan="7"><label>Frozen Foods<br></label></th>        
          </tr>
          
          <tr> 
            <th width="50%" align="left"><label>Ground Beef (one pound)<br></label></th>
            <th><input type="radio" name="beef" checked> 0<br></th>
            <th><input type="radio"  name="beef"> 0.5<br></th>
            <th><input type="radio"  name="beef"> 1<br></th>
            <th><input type="radio"  name="beef"> 2<br></th>
            <th><input type="radio"  name="beef"> 2<br></th>
            <th><input type="radio"  name="beef"> 4<br></th>
          </tr>
          
          <tr> 
            <th width="50%" align="left"><label>Chicken (1.4-1.8 pounds, whole)<br></label></th>
            <th><input type="radio" name="chicken" checked> 0<br></th>
            <th><input type="radio"  name="chicken"> 0.5<br></th>
            <th><input type="radio"  name="chicken"> 1<br></th>
            <th><input type="radio"  name="chicken"> 1<br></th>
            <th><input type="radio"  name="chicken"> 1<br></th>
            <th><input type="radio"  name="chicken"> 1<br></th>
          </tr>
          
          <tr> 
            <th width="50%" align="left"><label>Frozen Vegetables (corn/broccoli/peas/mixed)<br></label></th>
            <th><input type="radio" name="frovege" checked> 0<br></th>
            <th><input type="radio"  name="frovege"> 2<br></th>
            <th><input type="radio"  name="frovege"> 2<br></th>
            <th><input type="radio"  name="frovege"> 2<br></th>
            <th><input type="radio"  name="frovege"> 3<br></th>
            <th><input type="radio"  name="frovege"> 3<br></th>
          </tr>
          
          <tr> 
            <th width="50%" align="left"><label>Bread Loaf (brown/white)<br></label></th>
            <th><input type="radio" name="bread" checked> 0<br></th>
            <th><input type="radio"  name="bread"> 1<br></th>
            <th><input type="radio"  name="bread"> 2<br></th>
            <th><input type="radio"  name="bread"> 2<br></th>
            <th><input type="radio"  name="bread"> 3<br></th>
            <th><input type="radio"  name="bread"> 3<br></th>
          </tr>
          
          
          
          <tr> 
            <th colspan="7"><label>Non - Dairy Beverages<br></label></th>        
          </tr>
          
          <tr> 
            <th width="50%" align="left"><label>Juice - 1 litre (apple/orange/other)<br></label></th>
            <th><input type="radio" name="juice" checked> 0<br></th>
            <th><input type="radio"  name="juice"> 1<br></th>
            <th><input type="radio"  name="juice"> 2<br></th>
            <th><input type="radio"  name="juice"> 3<br></th>
            <th><input type="radio"  name="juice"> 4<br></th>
            <th><input type="radio"  name="juice"> 7<br></th>
          </tr>
          
          <tr> 
            <th width="50%" align="left"><label>Soy beverage - 1 litre<br></label></th>
            <th><input type="radio" name="soy" checked> 0<br></th>
            <th><input type="radio"  name="soy"> 1<br></th>
            <th><input type="radio"  name="soy"> 1<br></th>
            <th><input type="radio"  name="soy"> 2<br></th>
            <th><input type="radio"  name="soy"> 2<br></th>
            <th><input type="radio"  name="soy"> 3<br></th>
          </tr>
          
          
          
          
          <tr> 
            <th colspan="7"><label>Canned Goods<br></label></th>        
          </tr>
          
          <tr> 
            <th width="50%" align="left"><label>Vegetables (corn/peas/carrots/mixed veggies/other)<br></label></th>
            <th><input type="radio" name="vege" checked> 0<br></th>
            <th><input type="radio"  name="vege"> 1<br></th>
            <th><input type="radio"  name="vege"> 2<br></th>
            <th><input type="radio"  name="vege"> 4<br></th>
            <th><input type="radio"  name="vege"> 6<br></th>
            <th><input type="radio"  name="vege"> 8<br></th>
          </tr>
          
          <tr> 
            <th width="50%" align="left"><label>Fruit (peaches/pineapple/fruit cocktail/other)<br></label></th>
            <th><input type="radio" name="fruit" checked> 0<br></th>
            <th><input type="radio"  name="fruit"> 1<br></th>
            <th><input type="radio"  name="fruit"> 2<br></th>
            <th><input type="radio"  name="fruit"> 4<br></th>
            <th><input type="radio"  name="fruit"> 6<br></th>
            <th><input type="radio"  name="fruit"> 8<br></th>
          </tr>
          
          <tr> 
            <th width="50%" align="left"><label>Pasta Sauce/Tomato Sauce/Tomato Paste<br></label></th>
            <th><input type="radio" name="sauces" checked> 0<br></th>
            <th><input type="radio"  name="sauces"> 1<br></th>
            <th><input type="radio"  name="sauces"> 2<br></th>
            <th><input type="radio"  name="sauces"> 3<br></th>
            <th><input type="radio"  name="sauces"> 4<br></th>
            <th><input type="radio"  name="sauces"> 5<br></th>
          </tr>
          
          <tr> 
            <th width="50%" align="left"><label>Canned Tomatoes<br></label></th>
            <th><input type="radio" name="ctomatoes" checked> 0<br></th>
            <th><input type="radio"  name="ctomatoes"> 1<br></th>
            <th><input type="radio"  name="ctomatoes"> 2<br></th>
            <th><input type="radio"  name="ctomatoes"> 2<br></th>
            <th><input type="radio"  name="ctomatoes"> 3<br></th>
            <th><input type="radio"  name="ctomatoes"> 4<br></th>
          </tr>
          
          <tr> 
            <th width="50%" align="left"><label>Soup (tomato/mushroom/chicken/chunky/veg/other)<br></label></th>
            <th><input type="radio" name="soup" checked> 0<br></th>
            <th><input type="radio"  name="soup"> 4<br></th>
            <th><input type="radio"  name="soup"> 5<br></th>
            <th><input type="radio"  name="soup"> 6<br></th>
            <th><input type="radio"  name="soup"> 7<br></th>
            <th><input type="radio"  name="soup"> 10<br></th>
          </tr>
          
          <tr> 
            <th width="50%" align="left"><label>Baked Brown Beans (with/without pork)<br></label></th>
            <th><input type="radio" name="bbbeans" checked> 0<br></th>
            <th><input type="radio"  name="bbbeans"> 1<br></th>
            <th><input type="radio"  name="bbbeans"> 2<br></th>
            <th><input type="radio"  name="bbbeans"> 3<br></th>
            <th><input type="radio"  name="bbbeans"> 3<br></th>
            <th><input type="radio"  name="bbbeans"> 4<br></th>
          </tr>
          
          <tr> 
            <th width="50%" align="left"><label>Canned Beans (chickpeas/kidney/mixed/other)<br></label></th>
            <th><input type="radio" name="cbeans" checked> 0<br></th>
            <th><input type="radio"  name="cbeans"> 1<br></th>
            <th><input type="radio"  name="cbeans"> 1<br></th>
            <th><input type="radio"  name="cbeans"> 2<br></th>
            <th><input type="radio"  name="cbeans"> 2<br></th>
            <th><input type="radio"  name="cbeans"> 3<br></th>
          </tr>
          
          <tr> 
            <th width="50%" align="left"><label>Canned Seafood (salmon/tuna/sardines/other)<br></label></th>
            <th><input type="radio" name="cseafood" checked> 0<br></th>
            <th><input type="radio"  name="cseafood"> 2<br></th>
            <th><input type="radio"  name="cseafood"> 2<br></th>
            <th><input type="radio"  name="cseafood"> 3<br></th>
            <th><input type="radio"  name="cseafood"> 4<br></th>
            <th><input type="radio"  name="cseafood"> 5<br></th>
          </tr>
          
          <tr> 
            <th width="50%" align="left"><label>Canned Meat (chicken/turkey/ham/other)<br></label></th>
            <th><input type="radio" name="cmeat" checked> 0<br></th>
            <th><input type="radio"  name="cmeat"> 1<br></th>
            <th><input type="radio"  name="cmeat"> 1<br></th>
            <th><input type="radio"  name="cmeat"> 2<br></th>
            <th><input type="radio"  name="cmeat"> 3<br></th>
            <th><input type="radio"  name="cmeat"> 4<br></th>
          </tr>
          
          <tr> 
            <th width="50%" align="left"><label>Canned Meal (pasta/chili/other)<br></label></th>
            <th><input type="radio" name="cmeal" checked> 0<br></th>
            <th><input type="radio"  name="cmeal"> 1<br></th>
            <th><input type="radio"  name="cmeal"> 1<br></th>
            <th><input type="radio"  name="cmeal"> 2<br></th>
            <th><input type="radio"  name="cmeal"> 2<br></th>
            <th><input type="radio"  name="cmeal"> 3<br></th>
          </tr>

          
          
        
        </tbody>
      </table>

      
      <br><br>
      <button style="width: 100%; padding: 10px" type="submit">Submit</button>
      
      </form>

    
  </div>
</div>


<div class="w3-container w3-black w3-center w3-opacity w3-padding-64">
    <h1 class="w3-margin w3-xlarge">403-220-6551<br>251 MacEwan Student Centre<br>2500 University Drive NW<br>Canada AB</h1>
</div>



</body>
</html>
