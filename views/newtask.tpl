%rebase('base.tpl',Page_Title='Todo list')
<h3>Add new task to the todo</h3><br>
<form action="/new" method="POST">
	<label>Task</label><br>
	<input type="text" size ="100" name="task"><br>
	<lable>Description</lable><br>
	<textarea name="desc" rows="10" cols="30"></textarea><br>
	<input type="submit" name="save" value="save">
	<input type="button" value="Cancel" onClick="parent.location='/'">
</form>