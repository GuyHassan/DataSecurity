# Data Security Project

The project focuses on a data mining deep search of user names and passwords for any type (The initial issue was for wifi security cameras but it will find any device that you requested) of device (with a default user name and password),
the search is done on random sites, we put a URL site into the software (website) and it starts searching for more and more sites from the site we entered,
in the end the software brings us a document with all the data he found.
## Example

**That's how the project looks**

![image](https://user-images.githubusercontent.com/33221427/70856030-4015d600-1edd-11ea-9c9f-d7f2efd9d46a.png)

**After find some data from a [Random Site](https://www.a1securitycameras.com/technical-support/default-username-passwords-ip-addresses-for-surveillance-cameras/)**

![dataSecurity](https://user-images.githubusercontent.com/33221427/70856039-5facfe80-1edd-11ea-9da3-261dff775702.gif)
## Usage
The project was written in Python and Beautiful Soup Library, the GUI written in HTML, CSS , Javascript, the algorithm of searching is creating in the python code, and after the javascript read the data from a JSON file and print on the site the data.

All the data saved after in a local database work with SqlLite3 Libary.

## License
[SCE Collage](https://www.sce.ac.il/)
