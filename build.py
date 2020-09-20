import os
import subprocess
import sys


def call(*args, shell=False):
    proc = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=shell, check=False)
    if proc.returncode:
        print('Error: ', *args)
        print('STDOUT:', proc.stdout.decode(), file=sys.stdout)
        proc.check_returncode()
    return proc.stdout.decode('utf8').strip()


def convert(name, dirname):
    call('jupyter-nbconvert', '--output-dir', dirname, '--to', 'html', name)


def main():
    for root, dirs, files in os.walk('.'):
        for name in files:
            if name.endswith('.ipynb'):
                output = os.path.join('docs', root[2:])
                convert(os.path.join(root, name), output)


if __name__ == '__main__':
    main()
