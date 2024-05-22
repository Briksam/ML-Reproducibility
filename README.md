# RE: Active-Negative-Loss-Functions

## Original Work
https://github.com/Virusdoll/Active-Negative-Loss/tree/main

## Requirements

```console
python >= 3.9, torch >= 1.12.1, torchvision >= 0.13.1, numpy >= 1.23.1
```
## Changes made
We modified utils.py to add conditions for loss functions nce and nnce and fixed the MAE error

## Reproduced Results
You can find all of our log files for all experiments ran in the "experiment" folder.
Tables regenerated:
<img title="a title" alt="Alt text" src="/images/boo.svg">
<img title="a title" alt="Alt text" src="/images/boo.svg">
<img title="a title" alt="Alt text" src="/images/boo.svg">

## Reproduced Graphs
Here are the graphs we generated:
<img title="a title" alt="Alt text" src="/images/boo.svg">
To be able to reproduce the above graphs run the python file "Graphgen.py" in the corresponding folder dircetory ex) for the graph of ANL_CE on CIFAR10
go to folder "anl_ce_cifar10_graph" and run the python file in that directory and the graph will be generated for you.
There is also tensorboard support (credits to original authors) using the command "tensorboard --logdir=runs\cifar10\sym\anl_ce" in the terminal of the project's directory is sufficient, once tensorboard is launced graphs are generated for you as well.
## Moreover we thank the original authors [Virusdoll](https://github.com/Virusdoll/Active-Negative-Loss/tree/main)

