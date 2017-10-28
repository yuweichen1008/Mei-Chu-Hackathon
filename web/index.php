<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <title>MeiChu Hackathon</title>
    <!-- Bootstrap core CSS-->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <!-- Custom fonts for this template-->
    <link href="vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <!-- Page level plugin CSS-->
    <link href="vendor/datatables/dataTables.bootstrap4.css" rel="stylesheet">
    <!-- Custom styles for this template-->
    <link href="css/sb-admin.css" rel="stylesheet">
  </head>
  <body class="fixed-nav sticky-footer bg-dark" id="page-top">
    <!-- Navigation-->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top" id="mainNav">
      <a class="navbar-brand" href="#"><i class="fa fa-fw fa-envelope" style="padding-right: 15px"></i>E-mail</a>
      <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav navbar-sidenav" id="exampleAccordion">
          <li class="nav-item" data-toggle="tooltip" data-placement="right" title="Malicious">
            <a class="nav-link" href="malicious.php">
              <img class="fa fa-fw" src="icon/malicious.png">
              <span class="nav-link-text">Malicious</span>
            </a>
          </li>
          <li class="nav-item" data-toggle="tooltip" data-placement="right" title="Phishing">
            <a class="nav-link" href="phishing.php">
              <img class="fa fa-fw" src="icon/phishing.png">
              <span class="nav-link-text">Phishing</span>
            </a>
          </li>
          <li class="nav-item" data-toggle="tooltip" data-placement="right" title="Fraud">
            <a class="nav-link" href="fraud.php">
              <img class="fa fa-fw" src="icon/fraud.png">
              <span class="nav-link-text">Fraud</span>
            </a>
          </li>
          <li class="nav-item" data-toggle="tooltip" data-placement="right" title="Spam">
            <a class="nav-link" href="spam.php">
              <img class="fa fa-fw" src="icon/spam.png">
              <span class="nav-link-text">Spam</span>
            </a>
          </li>
          <li class="nav-item" data-toggle="tooltip" data-placement="right" title="Normal">
            <a class="nav-link" href="normal.php">
              <img class="fa fa-fw" src="icon/normal.png">
              <span class="nav-link-text">Trust<span>
              </a>
            </li>
          </ul>
          <ul class="navbar-nav sidenav-toggler hidden">
            <li class="nav-item">
              <a class="nav-link text-center" id="sidenavToggler">
                <i class="fa fa-fw fa-angle-left"></i>
              </a>
            </li>
          </ul>
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <form class="form-inline my-2 my-lg-0 mr-lg-2" action="upload.php" method="post" enctype="multipart/form-data">
                <div class="input-group">
                  <input class="form-control" type="file" name="file[]" multiple="multiple"/>
                  <input type="submit" class="btn btn-primary" value="Upload">
                </div>
              </form>
            </li>
            <li class="nav-item">
              <a class="nav-link" data-toggle="modal" data-target="#exampleModal">
              <i class="fa fa-fw fa-user-circle"></i>Simon</a>
            </li>
          </ul>
        </div>
      </nav>
      <div class="content-wrapper">
        <?php
          echo "<table class='table table-condensed table-hover'>";
          echo "<tr>";
          echo "<th>Category</th>";
          echo "<th>Subject</th>";
          echo "<th>From</th>";
          echo "<th>To</th>";
          echo "</tr>";
          $directory = './uploads';
          $scanned_directory = array_diff(scandir($directory), array('..', '.'));
          foreach ($scanned_directory as $file) {
              $path = "uploads/".$file;
              $command = escapeshellcmd('./parse_mail.py'.' '.$path);
              $output = shell_exec($command);
              $result = explode("\n", $output);
              $email_subject = $result[0];
              $email_from = $result[1];
              $email_to = $result[2];

              $random = rand(0, 4);

              if ($random == 0) {
                echo "<tr>";
                echo "<td><span class='badge badge-danger' style='width:80px'>Malicious</span></td>";
              }
              else if ($random == 1) {
                echo "<tr>";
                echo "<td><span class='badge badge-warning' style='width:80px'>Phishing</span></td>";
              }
              else if ($random == 2) {
                echo "<tr>";
                echo "<td><span class='badge badge-info' style='width:80px'>Spam</span></td>";
              }
              else if ($random == 3) {
                echo "<tr>";
                echo "<td><span class='badge badge-warning' style='width:80px'>Fraud</span></td>";
              }
              else if ($random == 4) {
                echo "<tr>";
                echo "<td><span class='badge badge-success' style='width:80px'>Normal</span></td>";
              }

              echo "<td><a href='".$path."'>".$email_subject."</a></td>";
              echo "<td>".$email_from."</td>";
              echo "<td>".$email_to."</td>";
              echo "</tr>";
          } 
          echo "</table>";
         ?>
      </div>
      <!-- /.content-wrapper-->
      <footer class="sticky-footer">
        <div class="container">
          <div class="text-center">
            <small>MeiChu Hackthon 2017</small>
          </div>
        </div>
      </footer>
      <!-- Scroll to Top Button-->
      <a class="scroll-to-top rounded" href="#page-top">
        <i class="fa fa-angle-up"></i>
      </a>
      <!-- Logout Modal-->
      <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">Ready to Leave?</h5>
              <button class="close" type="button" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">×</span>
              </button>
            </div>
            <div class="modal-body">Select "Logout" below if you are ready to end your current session.</div>
            <div class="modal-footer">
              <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancel</button>
              <a class="btn btn-primary" href="login.html">Logout</a>
            </div>
          </div>
        </div>
      </div>
      <!-- Bootstrap core JavaScript-->
      <script src="vendor/jquery/jquery.min.js"></script>
      <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
      <!-- Core plugin JavaScript-->
      <script src="vendor/jquery-easing/jquery.easing.min.js"></script>
      <!-- Page level plugin JavaScript-->
      <script src="vendor/chart.js/Chart.min.js"></script>
      <script src="vendor/datatables/jquery.dataTables.js"></script>
      <script src="vendor/datatables/dataTables.bootstrap4.js"></script>
      <!-- Custom scripts for all pages-->
      <script src="js/sb-admin.min.js"></script>
      <!-- Custom scripts for this page-->
      <script src="js/sb-admin-datatables.min.js"></script>
      <script src="js/sb-admin-charts.min.js"></script>
      <script>
        jQuery(function(){
           jQuery('#sidenavToggler').click();
        });
      </script>
    </div>
  </body>
</html>