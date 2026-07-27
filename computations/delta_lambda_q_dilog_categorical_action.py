import sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _li_2_q_util import li_2_q, load_q_50dps

def g(x: mp.mpf, q: mp.mpf, q_inv: mp.mpf) -> mp.mpf:
    # g(x) = -Li_2^q(-x)
    # The li_2_q function takes z, q, q_inv. So we pass -x as z.
    return -li_2_q(-x, q, q_inv)

def g_even(x: mp.mpf, q: mp.mpf, q_inv: mp.mpf) -> mp.mpf:
    # g_even(x) = 1/2 * (g(x) + g(x^-1))
    return (g(x, q, q_inv) + g(1/x, q, q_inv)) / 2

def delta_lambda(x_list: list[mp.mpf], q: mp.mpf, q_inv: mp.mpf) -> mp.mpf:
    # Delta_lambda = prod_{w \in lambda} exp(g_even(x_w))
    val = mp.mpf(0)
    for x in x_list:
        val += g_even(x, q, q_inv)
    return mp.exp(val)

def main():
    q, q_inv, z = load_q_50dps()
    print(f"q_0 = {q}")
    
    # Test values for x
    test_x = [mp.mpf('0.5'), mp.mpf('0.8'), mp.mpf('1.0')]
    for x in test_x:
        print(f"x = {x}, g(x) = {g(x, q, q_inv)}, g_even(x) = {g_even(x, q, q_inv)}")
    
    x_w = [mp.mpf('0.5'), mp.mpf('0.5')] # Example partition with 2 blocks
    dl = delta_lambda(x_w, q, q_inv)
    print(f"Delta_lambda for x_w={x_w}: {dl}")

if __name__ == '__main__':
    main()
