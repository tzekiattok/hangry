<!DOCTYPE html>
<html>

<head>


</head>
<body>

<?php 
    if ($_POST['userType'] == 'restaurantOwner')
        {
            echo $_POST["uid"];
            header("Location: ./viewRestaurantReservation.html?uid=" . $_POST["uid"]);
           // header("Location: http://google.com");
        }
    
    if ($_POST['userType'] == 'customer')
        {
            echo $_POST["uid"];
            header("Location: http://localhost:5200/make_reservation/" . $_POST["uid"]);
        }
    echo print_r($_POST, true);
    
    exit();
?>


</body>
</html>