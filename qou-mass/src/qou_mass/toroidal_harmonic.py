import numpy as np
import scipy.special as sp

def toroidal_harmonic_P(m, n, cosh_eta):
    """
    Computes the toroidal harmonic P_{n - 1/2}^m(cosh(eta))
    which is the associated Legendre function of the first kind with half-integer degree.
    """
    degree = n - 0.5
    # scipy.special.lpmv computes P_v^m(x)
    return sp.lpmv(m, degree, cosh_eta)

def toroidal_harmonic_Q(m, n, cosh_eta):
    """
    Computes the toroidal harmonic Q_{n - 1/2}^m(cosh(eta))
    (Not directly in scipy.special with half-integer degree easily, placeholder)
    """
    pass

if __name__ == "__main__":
    q0 = 1.10997858
    # Test a basic toroidal harmonic evaluation at cosh(eta) = q0
    # or perhaps q0 + 1/q0
    cosh_eta = (q0 + 1.0/q0) / 2.0
    print("Testing Toroidal Harmonic P_{n-1/2}^m at cosh(eta) =", cosh_eta)
    for n in range(1, 4):
        for m in range(0, 2):
            val = toroidal_harmonic_P(m, n, cosh_eta)
            print(f"  n={n}, m={m}: P_{n-0.5}^{m} = {val:.5f}")
