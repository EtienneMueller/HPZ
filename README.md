# High Performance Zebrafish

Welcome to the HPZ repository. This repository contains a collection of tools and scripts developed and utilized by the Scott Lab to facilitate various imaging tasks.

## About

The tools and scripts provided in this repository are currently tailored for individual use within our lab. However, we are in the process of refining them for broader application on the High-Performance Computing (HPC) infrastructure. Our aim is to enhance their utility and accessibility for a wider audience in the near future.

## Installation

To install and set up the tools and scripts, please follow the steps below:

### Prerequisites

1. Ensure that you have Conda installed on your HPC system.
2. Create a new Conda environment. (Detailed instructions will be provided soon.)

### Installation Steps

1. Install the required packages via pip:

    ```bash
    pip install --no-user git+https://github.com/EtienneMueller/hpz.git
    ```

2. Generate the necessary configuration files:

    ```bash
    python scripts/generate_config.py
    ```

## Usage

The repository includes a variety of tools and scripts, each designed for specific imaging tasks. Below is an overview of the available tools:

```bash
hpz generate_mf_config
hpz s2p -i {input_file} -o {output_file} -c {config_json}
hpz warp -i {input_file} -o {output_file} -t {template_prefix}
```

- **Ants**: [Detailed description and usage instructions will be provided soon.]
- **AutoSegmentation (DaCapo)**: [Detailed description and usage instructions will be provided soon.]
- **Visualization**: [Detailed description and usage instructions will be provided soon.]
- **MongoDB**: [Detailed description and usage instructions will be provided soon.]
- **MFLUX**: [Detailed description and usage instructions will be provided soon.]

### Example

```python
import hpz

def main()
    data = hpz.importmf("smb://mediaflux.researchsoftware.unimelb.edu.au/proj-5160_scott_lab-1128.4.503/2023_MUELLER_7C/ops.npy")
    # do things
    hpz.save_to_mf(data, "smb://mediaflux.researchsoftware.unimelb.edu.au/proj-5160_scott_lab-1128.4.503/2023_MUELLER_7C/ops_NEW.npy")
```

## Contributing

We welcome contributions from the community! If you would like to contribute, please follow these guidelines:

1. Fork the repository.
2. Create a feature branch for your changes.
3. Commit your changes to the feature branch.
4. Submit a pull request detailing your changes and the purpose they serve.

### Testing

Run the unittests with

```
python -m unittest discover tests
```

## License

This project is licensed under the MIT License.
