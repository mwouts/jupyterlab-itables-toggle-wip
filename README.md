# A JupyterLab extension for ITables

This extension adds a toggle on/off button to Jupyter Lab, that activates the rendering of Pandas DataFrames as interactive tables thanks to [datatables.net](https://datatables.net).

To install the extension, execute
```shell
pip install jupyterlab-itables
```
in the Python environment from which you launch Jupyter (i.e. stop Jupyter, execute `pip install jupyterlab-itables`, and then `jupyter lab`).

Note that you should also install separately [`itables`](https://mwouts.github.io/itables/), but this time in the Python environment that you use as the notebook kernel (i.e. execute `!pip install itables` in a cell of the notebook).

# How to develop this extension

You can install a development version of the extension with
```shell
jupyter labextension develop . --overwrite
```
Before doing that you may need to create a dedicated environment with e.g.
```shell
mamba env create --file environment.yml
conda activate jupyterlab-itables-dev
```

Read more on this on the [JupyterLab documentation](https://jupyterlab.readthedocs.io/en/latest/extension/extension_dev.html#developing-a-prebuilt-extension).
