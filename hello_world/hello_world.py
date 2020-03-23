def parse_args():
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("--name", default="world")
	return parser.parse_args()

def hello(name="world"):
	import jinja2
	template = jinja2.Template("Hello {{ name }}!")
	print(template.render(name=name))

def main():
	args = parse_args()
	hello(args.name)

if __name__ == "__main__":
	main()
