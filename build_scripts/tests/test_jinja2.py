from jinja2 import Environment, FileSystemLoader

hello = "GOODBYE"

environment = Environment(loader=FileSystemLoader("tests"))
template = environment.get_template("test.j2")

content = template.render(hello=hello)
print(content)