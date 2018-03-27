'''Flask 允许程序使用基于模板的自定义错误页面。最常见的错误代码有
两个：404，客户端请求未知页面或路由时显示；500，有未处理的异常时显示。

如果程序需要向已经有内容的块
中添加新内容，必须使用 Jinja2 提供的 super() 函数。

基模板中定义了可在衍生模板中重定义的块。 block 和 endblock 指令定义的块中的内容可
添加到基模板中。


'''