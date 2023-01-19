<?php
$options  = array (
  'http' => 
  array (
    'ignore_errors' => true,
  ),
);
 
$context  = stream_context_create( $options );
$response = file_get_contents(
    'https://public-api.wordpress.com/rest/v1/sites/MySite.wordpress.com/',
    false,
    $context
);
$response = json_decode( $response );
?>
