%rebase('base.tpl',Page_Title='Todo list')
<ul>
	%for row in rows:
	<li><a href="/item{{row[0]}}">{{row[1]}}</a></li>
	%end
</ul>
<br>
<form>
	<input type="button" value="Add New Task" onclick="parent.location'/new'">
</form>