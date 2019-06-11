# Obsplus Dataset: coal_node

A dataset collected over an operating longwall coalmine using a dense network of geophones.
Only 5 events are provided for testing purposes.

# Installation

If you want to use this dataset it requires the [obsplus package](https://github.com/niosh-mining/obsplus).
It can be installed from pypi using the following commands:

```bash
pip install opsdata_coal_node
```

Then the dataset can be loaded using the obsplus.DataSet object like so:
```python
import obsplus

ds = obsplus.DataSet('coal_node')
```
