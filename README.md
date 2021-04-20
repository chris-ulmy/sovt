<h1 align="center">SOVT&HRM Data Project</h1>
<p align="center">
<img src="./images/UWLogo2.jpg"> 
</p> <br>

**Welcome** to this project! This project contains all of the code necessary to generate the tables and plots used for publication of the manuscript: 
> "Measurement of pharyngeal air pressure during phonation using high-resolution manomtry" <br>
> Hoffmeister, Jesse; Ulmschneider, Christopher; Jones, Corinne; Cuicci, Michelle; McCulloch, Timothy
>
This module was written in **Python** and should be easy to follow with plenty of descriptions of what the code is doing along the way. For further explaination of each module of code, feel free to inspect it for function headers and comments. If you have any questions feel free to contact the author Chris Ulmschneider (ulmschneider.chris@gmail.com)
## Purpose
This project was designed to examine what pressure changes occur in the posterior pharynx during different voicing tasks. This was facilitated using a High-Resolution Manometry (HRM) catheter. This catheter collects pressure data along its length using 36 pressure sensors. It collects data at 100 hertz and therefore generates quite a large data set when recording for several minutes. I built a set of tools `hrmtools` to facilitate analysis of this data. This project uses those tools which are imbedded in this project. They can be found [here](http://github.com/chris-ulmy/hrmtools.git).

## How to use this project
This project is hosted in a Github repository. You must first install the repository into your environment. Run this code in your terminal to download and install this project. It will automatically download any dependencies as well.
```python
pip install git+git://github.com/chris-ulmy/sovt.git@main
```
### Where is the data?
You will have to obtain the data from someone by following a process. 
### Working with the code
Next, import the package into a newly created Python file. The main class module is located in the sovt.py file.
```python
from sovt import SOVT
```
You will need to initialize the SOVT class. You must specify the location of the text files you downloaded as well as the output location of the Excel files and graphs. You can also choose to run a clean run (more explaination on that later) as well as whether or not to generate the graphs (this can be lengthy).
```python
text_path = "C:/users/ulmsc/Documents/SOVT_test/text_files"
save_path = "C:/users/ulmsc/Documents/SOVT_test/outputs"
S = SOVT(text_path, save_path, clean=True, make_plots=True)
S.run()
```
It is pretty much that easy. What the module will do is...