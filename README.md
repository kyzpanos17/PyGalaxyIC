# PyGalaxyIC
A Python module that helps you create stable initial conditions of disc galaxies.

------------------------------------------------------------------------

## Supported Versions

**Python:** 3.10, 3.11, 3.12 
**Core dependencies (required):**  
- `numpy` >= 1.26.2  
- `scipy` >= 1.12.0  
- `pandas` >= 2.2.0  
- `chardet` >= 5.2.0  

**Optional dependencies:**  
- `numba` >= 0.59 (for accelerated computations)  
- `matplotlib` >= 3.8.0 (for plotting functionality)  

> Note: If optional dependencies are not installed, plotting or accelerated computations will not work, but the core functionality remains available.

------------------------------------------------------------------------


## Installation

In order to install the PyGalaxyIC module

```bash
pip install PyGalaxyIC
```

If you want to add accelaration to the computation use the following command: 

```bash
pip install PyGalaxyIC[accel]
```

If you want to plotting functionality use the following command: 

```bash
pip install PyGalaxyIC[plot]
```

You can install the module with everything enabled using the following command:

```bash
pip install PyGalaxyIC[all]
```


------------------------------------------------------------------------


## Development Installation

Follow these steps to set up a development environment.

### 1. Clone the repository

```bash
git clone https://github.com/your-username/PyGalaxyIC.git
cd PyGalaxyIC
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

### 3. Install the package in editable mode

```bash
pip install -e .
```

This allows you to modify the source code under `src/` without reinstalling the package.

### 4. Install development dependencies

```bash
pip install -r requirements.txt
```

This installs the testing tools (`pytest`) and other development utilities.


### 5. Run the test suite

```bash
pytest
```

If all tests pass, you're ready to develop!

------------------------------------------------------------------------