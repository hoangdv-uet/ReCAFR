

## Quick Start
**1.** Compline the evaluator of cpp implementation with the following command line:

```bash
python local_compile_setup.py build_ext --inplace
```

If the compilation is successful, the evaluator of cpp implementation will be called automatically.
Otherwise, the evaluator of python implementation will be called.

**2.** Download review data from the link given in the openreview comments (due to the limitation of the anonymous hub, links cannot be displayed here.)

**3.** Run preprocessing.py file to create review feature.

**4.** You may check or update the hyperparameters in the configuration file *./conf/SSL.ini*.

**5.** Run [main.py](./main.py) in IDE 

