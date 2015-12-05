#!/usr/bin/env python

import argparse, os, urllib, tarfile

versions_darwin = {
	"3.4.0":"https://cmake.org/files/v3.4/cmake-3.4.0-Darwin-x86_64.tar.gz",
	"3.4.1":"https://cmake.org/files/v3.4/cmake-3.4.1-Darwin-x86_64.tar.gz",
	"3.3.0":"https://cmake.org/files/v3.3/cmake-3.3.0-Darwin-x86_64.tar.gz",
	"3.3.1":"https://cmake.org/files/v3.3/cmake-3.3.1-Darwin-x86_64.tar.gz",
	"3.3.2":"https://cmake.org/files/v3.3/cmake-3.3.2-Darwin-x86_64.tar.gz",
	"3.2.0":"https://cmake.org/files/v3.2/cmake-3.2.0-Darwin-x86_64.tar.gz",
	"3.2.1":"https://cmake.org/files/v3.2/cmake-3.2.1-Darwin-x86_64.tar.gz",
	"3.2.2":"https://cmake.org/files/v3.2/cmake-3.2.2-Darwin-x86_64.tar.gz",
	"3.2.3":"https://cmake.org/files/v3.2/cmake-3.2.3-Darwin-x86_64.tar.gz",
	"3.1.0":"https://cmake.org/files/v3.1/cmake-3.1.0-Darwin64.tar.gz",
	"3.1.1":"https://cmake.org/files/v3.1/cmake-3.1.1-Darwin-x86_64.tar.gz",
	"3.1.2":"https://cmake.org/files/v3.1/cmake-3.1.2-Darwin-x86_64.tar.gz",
	"3.1.3":"https://cmake.org/files/v3.1/cmake-3.1.3-Darwin-x86_64.tar.gz",
	"3.0.0":"https://cmake.org/files/v3.0/cmake-3.0.0-Darwin64-universal.tar.gz",
	"3.0.1":"https://cmake.org/files/v3.0/cmake-3.0.1-Darwin64-universal.tar.gz",
	"3.0.2":"https://cmake.org/files/v3.0/cmake-3.0.2-Darwin64-universal.tar.gz",
	"2.8.12.2":"https://cmake.org/files/v2.8/cmake-2.8.12.2-Darwin64-universal.tar.gz"
}
cmakevm_home = os.path.join(os.path.expanduser("~"), ".cmakevm")

def create_home_folder_if_needed():
	if not os.path.exists(cmakevm_home):
		os.makedirs(cmakevm_home)

def list_versions():
	for version in versions_darwin:
		print(version)

def download_all():
	create_home_folder_if_needed()
	for version in versions_darwin:
		download_one(version)

def get_local_path(version):
	url = versions_darwin[version]
	filename = url.split("/")[-1]
	return os.path.join(cmakevm_home, filename)

def get_installed_dir(version):
	url = versions_darwin[version]
	filename = url.split("/")[-1]
	dirname = filename.replace(".tar.gz", "")
	return os.path.join(cmakevm_home, dirname)

def add_to_path_osx(version):
	installed_dir = get_installed_dir(version)
	path_cmake_bin = os.path.join(installed_dir, 'CMake.app/Contents/bin/')
	print("Adding "+path_cmake_bin+" to $PATH")
	os.environ["PATH"] = path_cmake_bin + os.pathsep + os.environ["PATH"]

def download_one(version):
	create_home_folder_if_needed()
	local_path = get_local_path(version)
	if os.path.exists(local_path):
		print(version + " exists at "+ local_path +", skip downloading")
	else:
		print("Downloading from " + url)
		urlopener = urllib.URLopener()
		urlopener.retrieve(url, local_path)

def install_one(version):
	path_to_downloaded_file = get_local_path(version)
	old_working_dir = os.getcwd()
	os.chdir(cmakevm_home)
	tar = tarfile.open(path_to_downloaded_file)
	print("extracting " + path_to_downloaded_file + " to " + cmakevm_home)
	tar.extractall()
	tar.close()
	os.chdir(old_working_dir)


def main():
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('--list', action='store_true')
	parser.add_argument('--downloadall', action='store_true')
	parser.add_argument('--install', help="version to install")
	args = parser.parse_args()

	if args.list:
		list_versions()

	if args.downloadall:
		download_all()

	if args.install:
		version_to_install = args.install
		download_one(version_to_install)
		install_one(version_to_install)
		add_to_path_osx(version_to_install)

    # my code here

if __name__ == "__main__":
    main()