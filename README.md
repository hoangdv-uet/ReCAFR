

## Quick Start
**Firstly**, compline the evaluator of cpp implementation with the following command line:

```bash
python local_compile_setup.py build_ext --inplace
```

If the compilation is successful, the evaluator of cpp implementation will be called automatically.
Otherwise, the evaluator of python implementation will be called.

**1.**, Download review data from the link given in the openreview comments.(Due to the limitation of the anonymous hub, links cannot be displayed here.)
**2.** Run preprocessing.py file to create review feature

**3.** Run [main.py](./main.py) in IDE hyperparameters are in configuration file 

**4.** You may check or update the hyperparameters in the configuration file *./conf/SSL.ini*.
