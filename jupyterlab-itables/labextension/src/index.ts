import { DocumentRegistry } from "@jupyterlab/docregistry";
import { INotebookModel, NotebookPanel } from "@jupyterlab/notebook";
import { DisposableDelegate, IDisposable } from "@lumino/disposable";
import { ToolbarButton } from "@jupyterlab/apputils";

export class ItablesButton
  implements DocumentRegistry.IWidgetExtension<NotebookPanel, INotebookModel>
{
  public createNew(panel: NotebookPanel): IDisposable {
    const callback = () => {
      this.itables(panel);
    };
    const button = new ToolbarButton({
      className: "itablesButton",
      label: "Itables",
      onClick: callback,
      tooltip: "Activate the itables interactive mode",
    });

    panel.toolbar.insertItem(0, "itables", button);
    return new DisposableDelegate(() => {
      button.dispose();
    });
  }

  // launch itables
  protected itables = (panel: NotebookPanel) => {
    const kernelConnection = panel.context.sessionContext.session.kernel;
    kernelConnection.requestExecute({
      code: "from itables import init_notebook_mode; init_notebook_mode(all_interactive=True)",
    });
  };
}
