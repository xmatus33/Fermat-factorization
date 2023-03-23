# Script for calculating Fermat factorization of public RSA keys.

import gmpy2
import base64
import argparse
from pathlib import Path
from cryptography.hazmat.primitives import serialization


def parse_cert(file_path: Path):

    cert_data = b''

    with open(file_path, "rb") as f:
        
        for line in f.readlines():
            
            if not b'KEY' in line:
                cert_data += line

    cert_data = base64.b64decode(cert_data)
    public_key = serialization.load_der_public_key(cert_data)

    n = public_key.public_numbers().n
    e = public_key.public_numbers().e

    return n, e


def fermat(n):

    tries = 100
    a = gmpy2.isqrt(n)
    c = 0

    while not gmpy2.is_square( a**2 - n ):

        a += 1
        c += 1

        if c > tries:
            return (-1, -1)

    bsq = a**2 - n
    b = gmpy2.isqrt( bsq )

    p = a + b
    q = a - b

    return (p , q)


def print_results(p, q, n):
    print("+----------------------------------------+")
    print("|          Fermat Factorization          |")
    print("+----------------------------------------+\n")
    print(f"n: {n}\n")
    print(f"p: {p}\n")
    print(f"q: {q}\n")


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('modulo', metavar='M', nargs='?', type=int, help='Modulo to be factorized')
    parser.add_argument("-f", "--file", metavar="file", help="Input file", type=str)
    args = parser.parse_args()

    
    if args.file:
        # Load modulus from file
        n, e = parse_cert(args.file)
        p, q = fermat(n)
        print_results(p, q, n)

        # Derive private key
        phi_n = (p-1)*(q-1)
        d = pow(e, -1, n)
        print(f"Public key (from file):   {e}")
        print(f"Private key (calculated): {d}\n")
    elif args.modulo:
        # Take modulus from argument
        p, q = fermat(args.modulo)
        print_results(p, q, args.modulo)
    else:
        parser.print_help()
