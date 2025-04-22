import subprocess
import sys

# Detect Python command
python_cmd = "python3" if sys.platform != "win32" else "python"

# List of commands to execute
commands = [
    f"{python_cmd} ./prbs_verilog_gen.py -c 0,0,0,0,0,1,1 -t=12 -w=32 -o ./verilog",
    f"{python_cmd} ./prbs_verilog_gen.py -c 0,0,0,0,0,1,1 -t=20 -w=32 -o ./verilog",
    f"{python_cmd} ./prbs_verilog_gen.py -c 0,0,0,0,1,0,0,0,1 -t=12 -w=32 -o ./verilog",
    f"{python_cmd} ./prbs_verilog_gen.py -c 0,0,0,0,1,0,0,0,1 -t=20 -w=32  -o ./verilog",
    f"{python_cmd} ./prbs_verilog_gen.py -c 0,0,0,0,0,0,0,0,1,0,1 -t=12 -w=32 -o ./verilog",
    f"{python_cmd} ./prbs_verilog_gen.py -c 0,0,0,0,0,0,0,0,1,0,1 -t=20 -w=32 -o ./verilog",
    f"{python_cmd} ./prbs_verilog_gen.py -c 0,0,0,0,0,0,0,0,0,0,0,0,0,1,1 -t=12 -w=32 -o ./verilog",
    f"{python_cmd} ./prbs_verilog_gen.py -c 0,0,0,0,0,0,0,0,0,0,0,0,0,1,1 -t=20 -w=32  -o ./verilog",
    f"{python_cmd} ./prbs_verilog_gen.py -c 0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1 -t=12 -w=32 -o ./verilog",
    f"{python_cmd} ./prbs_verilog_gen.py -c 0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1 -t=20 -w=32 -o ./verilog",
    f"{python_cmd} ./prbs_verilog_gen.py -c 0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1 -t=12 -w=32 -s=1 -o ./verilog",
    f"{python_cmd} ./prbs_verilog_gen.py -c 0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1 -t=20 -w=32 -s=1 -o ./verilog",
    f"{python_cmd} ./prbs_verilog_gen.py -c 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1 -t=12 -w=32 -s=0 -o ./verilog",
    f"{python_cmd} ./prbs_verilog_gen.py -c 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1 -t=20 -w=32 -s=0 -o ./verilog",
    f"{python_cmd} ./prbs_verilog_gen.py -c 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1 -t=12 -w=32 -o ./verilog",
    f"{python_cmd} ./prbs_verilog_gen.py -c 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1 -t=20 -w=32 -o ./verilog",
]

# Execute each command
for cmd in commands:
    print(f"Executing: {cmd}")
    subprocess.run(cmd, shell=True, check=True)