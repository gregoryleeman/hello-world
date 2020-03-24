def hello(what="world"):
	import jinja2
	template = jinja2.Template("Hello {{ what }}! :D")
	return(template.render(what=what))

def main():
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"what",
		default="world",
		nargs='?',
		help="what to say hello to"
		)
	parser.add_argument(
		'--file',
		action='store_true',
		help="file mode (read a file and say hello to each line)"
		)
	args = parser.parse_args()
	if args.file:
		try:
			file_in = open(args.what, "r")
			for line in file_in.readlines():
				print(hello(line.strip()))
		except:
			print("Error reading file " + args.what)
	else:
		print(hello(args.what))

if __name__ == "__main__":
	hello_single()
