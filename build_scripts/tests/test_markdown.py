import markdown

html = markdown.markdown("""
<div markdown="1">
## HELLO
</div>

<p>{{hello}}</p>
""", extensions=['md_in_html'])
print(html)