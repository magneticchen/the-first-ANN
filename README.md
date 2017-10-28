# Node project
"Node" is a project aims to bulid neural network. It's oriention is to collect plenty of types of neural networks and provide manager to organize and test it. It is a project belongs to NOOXY. There still lots of miles to  complete it. Article about it might be established some day. Visit us www.nooxy.tk.
## Requirement
- C++
- Python
- Python package: NumPy
- Python package: Matplotlib
- Python package: CuPy(Optional)

to install Python packages
```bash
#!/bin/bash
sudo python3 -m pip install numpy matplotlib
```
## Directory
### bin
node manager's executable files. They are compiled by C++ side source code in main directory, and it's build target is mainly macos(Darwin) now.

### main
Source code file for node manager.
There include two type of launguages `C++` and `python`. They are completely seperated(work independently). However, it's functions act similarly.
#### For C++ 
there are source for `matrix(mathematical lib for ann)`, `ann(artificial neuron network library)` and `node manager(main program)`.
#### For python
We are contructing now. Not yet to be describe.
For launching manager
```sh
python3 manage.py
```
If you need GPU support(for really large size of neural network) simply change all
```python
import numpy as np
```
to
```python
import cupy as np
```
### research
Test the nerual network for finding good models etc.
### test
A directory to test some functions that not yet to be added to mainline. 
## TODO
- CuPy support [v]
- More type of neural network training method [x]
- Validation to stop training [x]
- Ability to start a project to determine best model [x]
- Plotling [v]
- Configuration to save state [v]
- and more to be added
## Gallery
![alt text](https://github.com/magneticchen/node_project/raw/master/research/gallery/train.png)
Input layer 8 neurons, Output layer 8 neurons. 1 hidden layer. Training Graph.
![alt text](https://github.com/magneticchen/node_project/raw/master/research/8/graph/8x10x10x8/Figure_1-1.png)
Input layer 8 neurons, Output layer 8 neurons. 2 hidden layer. Training Graph.
