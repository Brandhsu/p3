import subprocess
import pandas as pd
from src.config import TRIALS


def call(args):
    proc = subprocess.Popen(args, stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    return out


def diff(files):
    for i in range(len(files) - 1):
        out = call(["diff", files[i], files[i + 1]])

        assert not len(out), f"ERROR! {files[i]} and {files[i + 1]} are not the same!"


if __name__ == "__main__":
    results = {
        "_async.py": [],
        "_asyncmp.py": [],
        "_process.py": [],
        "_thread.py": [],
        "_unsync.py": [],
    }

    for _ in range(TRIALS):
        for program in results:
            out = call(["python3", f"src/{program}"])
            results[program].append(float(out))

    results = pd.DataFrame(results)

    print(results)
    print(results.describe())

    diff([f'bin/{file.replace(".py", ".txt")}' for file in results.keys()])
