# A JupyterLab extension for ITables

This extension adds a toggle on/off button to Jupyter Lab, that activates the rendering of Pandas DataFrames as interactive tables thanks to [datatables.net](https://datatables.net).

Please install this extension with
```shell
pip install jupyterlab-itables
```

The extension should be installed in the environment from which you execute Jupyter. Also, [`itables`](https://mwouts.github.io/itables/) should be installed in the notebook kernel.

# How to develop this extension

To develop iteratively, you could install a development version of the extension with

```bash
jupyter labextension develop . --overwrite
```

Read more on this on the [JupyterLab documentation](https://jupyterlab.readthedocs.io/en/latest/extension/extension_dev.html#developing-a-prebuilt-extension).
