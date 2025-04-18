import os, shutil, time
import PyInstaller.__main__ as pyinstaller

def cleanup(spec_name, delete_dist):
	spec_file = os.path.join(os.getcwd(), f"{spec_name}.spec")
	build_dir = os.path.join(os.getcwd(), "build")
	dist_dir = os.path.join(os.getcwd(), "dist")

	if os.path.exists(spec_file):
		os.remove(spec_file)

	if os.path.exists(build_dir):
		shutil.rmtree(build_dir)

	if os.path.exists(dist_dir) and delete_dist:
		shutil.rmtree(dist_dir)

def main():
	name = os.getcwd().split("\\")[-1]

	cleanup(name, True)

	pyinstaller.run([
		f"--name={name}",
		"--onefile",
		"--console",
		"--clean",
		"main.py"
	])

	cleanup(name, False)

	time.sleep(5)

if __name__ == "__main__":
	main()
