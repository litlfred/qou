import sys
from pathlib import Path
import time
import pyhecke_native

def run_n(n):
    print(f"Testing S_{n} natively in Rust...")
    # Just generating the longest element for S_n
    w0 = list(range(n, 0, -1))
    t0 = time.time()
    try:
        # We pass a list of words, here just one word (the longest element)
        res = pyhecke_native.kl_betti_sum_rust(n, [w0])
        dt = time.time() - t0
        print(f"  S_{n} P_{{e, w_0}} = {res} (took {dt:.4f} sec)")
    except Exception as e:
        print(f"  S_{n} failed: {e}")

def main():
    for n in range(6, 10):
        run_n(n)

if __name__ == '__main__':
    main()
