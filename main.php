<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Form</title>
  </head>
  <body>
    <?php
      function tryToExtract($value) {
        $res = '';
        if (array_key_exists($value, $_GET)) {
          $res = $_GET[$value];
          unset($_GET[$value]);
        }
        return $res;
      }
      $first_name = tryToExtract('first_name');
      $last_name = tryToExtract('last_name');
      $text_content = tryToExtract('text_content');
    ?>
    <form action="/cgi-bin/handler.py" method="post">
      First Name: <input type="text" name="first_name" value="<?php echo $first_name;?>" />  <br />
      Last Name: <input type="text" name="last_name" value="<?php echo $last_name;?>" /> <br />
      Tell us something about yourself: <br />
      <textarea name="text_content" cols="40" rows="4"><?php echo $text_content;?></textarea> <br />
      <input type="submit" value="Submit" />
    </form>
    <p>
      <?php 
        if (!empty($_GET)) {
          echo "Errors: <br />";
          foreach ($_GET as $field => $error) {
            echo 'Field "'.htmlspecialchars(str_replace('err_', '', $field)).'": '.htmlspecialchars($error)."<br />";
          }
        }
      ?>
    </p>
  </body>
</html>
