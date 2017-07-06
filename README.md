This package implements a REST API on top of the [Benchmarking Suite Controller](https://github.com/benchmarking-suite/benchsuite-controller). It allows all the operations available from the Controller commandline tool.
# Quick Start
1. Install the package:
    ```bash
    user@myserver:~$ pip install benchsuite.rest
    ```
    This will also install the [Benchmarking Suite Controller](https://github.com/benchmarking-suite/benchsuite-controller) as dependency
2. Configure the Controller if not already done (see [this guide](https://github.com/benchmarking-suite/benchsuite-configuration/blob/master/README.md))

3. Start the REST server interactively:
    ```bash
    user@myserver:~$ python -m benchsuite.rest.app
    ```
    Alternatively, start the rest service as a service with the `benchsuite-rest` script included in the distribution
    ```bash
    user@myserver:~$ benchsuite-rest start
    ```
    In this case the rest server will log in the `benchsuite-rest.log` file created in the current directory.
    
4. Open [localhost:5000/api/v1/](localhost:5000/api/v1/)