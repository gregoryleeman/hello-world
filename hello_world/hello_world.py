def hello(name="world"):
	import jinja2
	template = jinja2.Template("Hello {{ name }}!")
	return(template.render(name=name))

def hello_single():
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("name", default="world", nargs='?', help="What to say hello to")
	args = parser.parse_args()
	print(hello(args.name))

def hello_file():
	import argparse
	parser = argparse.ArgumentParser(
		description = "Say hello to all the lines in a file"
		)
	parser.add_argument("file", help="Input file path")
	parser.add_argument("--out", help="Output file path", default="hello.txt")
	args = parser.parse_args()

	file_in = open(args.file, "r")
	file_out = open(args.out, "w")
	for line in file_in.readlines():
		file_out.write(hello(line.strip()) + "\n")
	file_in.close()
	file_out.close()

	print("Said hello in " + args.out)

if __name__ == "__main__":
	hello_single()
