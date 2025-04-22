# PRBS Verilog Generator

`prbs_verilog_gen.py` is a Python script designed to generate Verilog modules for Pseudo-Random Binary Sequence (PRBS) generation. The script supports customization of polynomial coefficients, sequence length, and output width. It is compatible with both Linux and Windows environments.

## Features

- Generate PRBS Verilog modules based on user-defined polynomial coefficients.
- Supports modular arithmetic (mod-2 addition).
- Allows customization of sequence length (`-t`) and output width (`-w`).
- Command-line interface with argument support and shorthand options.
- Optionally includes a seed in the module name for differentiation.

## Usage

### Command-Line Arguments

| Argument         | Shorthand | Description                                                                 |
|------------------|-----------|-----------------------------------------------------------------------------|
| `--coefficients` | `-c`      | Polynomial coefficients (comma-separated, e.g., `0,0,0,0,0,1,1`).           |
| `--times`        | `-t`      | Shift times (e.g., `12`, `20`).                                             |
| `--width`        | `-w`      | Output width (e.g., `32`).                                                  |
| `--output`       | `-o`      | Save path for the generated Verilog file. Defaults to the current directory.|
| `--seed`         | `-s`      | Optional seed to include in the module name for differentiation.            |

### Example Commands

```bash
python prbs_verilog_gen.py -c 0,0,0,0,0,1,1 -t 12 -w 32
python prbs_verilog_gen.py -c 0,0,0,0,1,0,0,0,1 -t 20 -w 32 -o ./output
python prbs_verilog_gen.py -c 0,0,0,0,0,0,0,0,1,0,1 -t 12 -w 32 -s 12345
```

### Output

The script generates a Verilog file named `<module_name>.v` in the specified or current directory. The module name is derived from the polynomial coefficients and optionally includes the seed.

## Installation

Ensure Python 3.x is installed on your system. Clone the repository or download the script to your working directory.

## Compatibility

The script is compatible with both Linux and Windows operating systems.

## Contributing

Contributions are welcome! Please submit issues or pull requests to improve the script.

## Contact

For questions or support, please contact the repository maintainer.
