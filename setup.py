import setuptools 

with open("README.md", "r", encoding="utf-8") as fh: 
   long_description = fh.read()
 
setuptools.setup(
   name = "macromedia_package",
   version = "0.0.1",
   author = "Macromedia Prof",
   author_email = "author@example.com",
   description = "A small example package - for how to upload on Github",
   long_description = long_description,
   long_description_content_type = "text/markdown",
   url = "https://github.com/user0000/macromedias_package",
   project_urls = {
      "Bug Tracker": "https://github.com/user0000/macromedias_package/issues",
   },
   license='MIT',
   packages=['macromedia_package'],
   install_requires=['requests'],
) 
