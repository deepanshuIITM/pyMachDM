

## Quick Start Preview

Here is how easy it is to run a basic pipeline in `pyMachDM`:

```python
import pymachdm as pdm

## Initialize your core model
model = pdm.DataMechanicsModel(data="experimental_results.csv")

## Run the primary calculation
results = model.compute_metrics()
print(results)