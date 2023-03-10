# Fermat Factorization

Fermat factorization uses that both factors are close to each other.

## Instalation

```bash
git clone https://github.com/xmatus33/Fermat-factorization.git
cd Fermat-factorization
python3 -m venv venv
.\venv\Scripts\activate
python3 -m pip install -r ./requirements.txt
```

## Usage

```bash
usage: fermatfac.py [-h] [-f file] [M]

positional arguments:
  M                     Modulo to be factorized

options:
  -h, --help            show this help message and exit
  -f file, --file file  Input file
```

## Example

```bash
# Insert modulo right away
python3 .\fermatfac.py 35

# Load modulo and public key from file
python3 .\fermatfac.py -f test_pub.key    
```
