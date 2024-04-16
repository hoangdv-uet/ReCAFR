First download review dataset via this link https://nijianmo.github.io/amazon. Then Run preprocessing.py file to create review feature


# Quick Start
**Firstly**, compline the evaluator of cpp implementation with the following command line:

```bash
python local_compile_setup.py build_ext --inplace
```

If the compilation is successful, the evaluator of cpp implementation will be called automatically.
Otherwise, the evaluator of python implementation will be called.

Model specific hyperparameters are in configuration file *./conf/SSL.ini*.

**Finally**, run [main.py](./main.py) in IDE
