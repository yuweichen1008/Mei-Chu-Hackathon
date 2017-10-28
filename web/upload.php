<?php
    $file_count = count($_FILES['file']['name']);
    $uploaddir = "./upload";

    if (!file_exists($uploaddir)) {
        mkdir($uploaddir, 0777, true);
    }

    for ($i=0; $i < $file_count; $i++) 
    {
        if(!empty($_FILES['file']['tmp_name'][$i]))
        {
            $file_extention = end((explode(".", $_FILES['file']['name'][$i])));

            if ($file_extention !== "eml") {
                echo "<script>alert('Error: Only accept eml file');window.location.href='index.php';</script>";
                break;
            }
            else {
                $path = "upload/" . basename( $_FILES['file']['name'][$i]);

                if (move_uploaded_file($_FILES['file']['tmp_name'][$i], $path)) {
                    
                }
            }
        }
    }

    if ($i == $file_count) {
        echo "<script>alert('Upload Success!');window.location.href='index.php';</script>";
    }
    else {
        echo "<script>alert('Upload Error!');window.location.href='index.php';</script>";
    }
?>