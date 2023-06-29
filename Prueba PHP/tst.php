<?php
$db = new SQLite3('C:\Users\Acer\Desktop\base_de_datos.db');
$result = $db->query('SELECT * FROM table WHERE id = id');
$statement->bindValue(':id',$id);

$result = $statement->execute();

?>
    