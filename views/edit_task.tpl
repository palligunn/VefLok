%rebase('base.tpl',Page_Title='Todo list')
<form action="/edit{{no}}" method="POST">
	<label>Task</label><br>
	<input type="text" size ="100" name="task" value="{{rec[1]}}"><br>
	<lable>Description</lable><br>
	<textarea name="desc" rows="10" cols="30">{{rec[2]}}</textarea><br>
	<lable>Date</lable><br>
	<input type="text" size ="100" name="tdate" value="{{rec[3]}}"><br>
	<input type="submit" name="save" value="Save">
</form>
<script>
	function goBack() {
		window.history.back();
	}
</script>