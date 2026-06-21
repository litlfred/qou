#!/usr/bin/env python3
"""
Smoke-test / cross-validation for the freshly-built `pyhecke_native` wheel.

Confirms (a) the PyO3 wheel imports and (b) its Hoefsmit-seminormal character
agrees, at the substrate q_0, with the INDEPENDENT hand-built H_3(q) rep used in
`borromean_per_block_h4_localization.py`.  Two completely different code paths
(Rust Hoefsmit vs a 2x2 sympy rep solved from the braid relation) must give the
same per-block Borromean characters:

    chi^{(3)}(b)     = 1
    chi^{(1,1,1)}(b) = 1
    chi^{(2,1)}(b)   = 2 - 3 h^4 - h^6     (h = q - 1/q),  b = (s1^{-1} s2)^3

If they match, both the wheel build and the keystone backbone's h^4-localization
claim are cross-confirmed.  This is the build-validation companion to the
sandbox build recipe documented in
`docs/audits/2026-06-20-pyhecke-native-build-unblocked.md`.
"""
import pyhecke_native as ph

Q0 = 1.1099785955541805  # tools/hecke-engine/src/gram.rs::Q_0 (f64)

# Borromean braid b = (s1^{-1} s2)^3 as [(sign, gen_1based), ...]
BORROMEAN = [(-1, 1), (1, 2)] * 3


def target_chi21(q):
    h = q - 1.0 / q
    return 2 - 3 * h**4 - h**6


def main():
    cases = [
        ("chi^(3)",      [3],       1.0),
        ("chi^(1,1,1)",  [1, 1, 1], 1.0),
        ("chi^(2,1)",    [2, 1],    target_chi21(Q0)),
    ]
    print(f"pyhecke_native v{ph.__version__}  |  q_0 = {Q0}")
    print(f"target chi^(2,1) = 2 - 3h^4 - h^6 = {target_chi21(Q0):.15f}\n")
    allok = True
    for name, shape, expected in cases:
        got = ph.chi_lambda_braid(shape, BORROMEAN, Q0)
        ok = abs(got - expected) < 1e-9
        allok &= ok
        print(f"  [{'PASS' if ok else 'FAIL'}] {name:<11} pyhecke={got:.15f}  "
              f"expected={expected:.15f}  |Δ|={abs(got-expected):.2e}")
    print(f"\nALL PASS: {allok}  "
          f"(Rust Hoefsmit ↔ independent sympy H_3 rep cross-validated)")
    return 0 if allok else 1


if __name__ == "__main__":
    raise SystemExit(main())
