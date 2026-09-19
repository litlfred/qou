#!/usr/bin/env python3
# polynomial_q_not_applicable: matrix identity at a numeric anchor; no symbolic-q polynomial output.
"""The production trace's algebra IS the 1D XXZ spin chain — measured, not asserted.

## What this settles

The corpus's production Markov trace is convention **D**. Two corpus artifacts
already say what that means algebraically:

  * `computations/y_lambda_su_n.py` docstring — "at `N = 2` these weights
    reproduce convention **D** (SU(2)/Temperley-Lieb, Jones) exactly ... **D is
    the production trace**, so the shipped pipeline *is* an `SU(N)`
    quantum-group trace, at `N = 2`, carrying the row cap."
  * `lean/QOU/BraidsAndKnots/FibreDimensionForcesTL.lean` (sorry-free) —
    a fibre of quantum dimension `[N]_q` forces `z·[N]_q = q^N`; at `N = 2`
    that is `z_D = q^3/(q^2+1)`.

Neither says what the Temperley-Lieb algebra IS as a mechanics. This probe
supplies that step, by explicit matrix identity rather than by citation:

    TL_n(delta) at delta = q + 1/q  IS  the U_q(sl_2)-symmetric OPEN XXZ chain
    on n sites at anisotropy  Delta = delta/2 = cosh(ln q).

CHECK 1 (two-site)  e^2 = delta * e            -- e is a TL generator at all
CHECK 2 (two-site)  the coefficient identity, each coefficient SOLVED for:
    -2 e = (XX + YY + Delta*ZZ) - Delta*I - ((q - 1/q)/2)(sz_1 - sz_2)
CHECK 3 (chain)     summing, with the boundary terms telescoping:
    -2 sum_i e_i = H_XXZ - Delta*(n-1)*I - ((q - 1/q)/2)(sz_1 - sz_n)
    verified at n = 2,3,4,5.
CHECK 4 (regime)    Delta = cosh(ln q0) > 1 at the substrate -- the MASSIVE /
    Ising-like regime, where Bethe strings are stable bound states. This is
    DERIVED, not fitted: cosh(x) > 1 for every x != 0, so q0 != 1 forces it
    with zero free parameters. Checked at BOTH documented pins; they agree to
    ~1.2 ppb, so the conclusion is pin-independent.

## What this does NOT establish

It does not identify the chain's SITES with anything physical, and it does not
claim the XXZ n-string band energy (that formula is deliberately NOT quoted
here -- see bean `qou-6b9y`, which measures it by momentum-resolved ED).

## Provenance caution

The boundary sign in CHECK 2/3 was RECALLED WRONG on first attempt; the
residual identified itself as exactly 2*||bnd||. The coefficients below are
therefore solved from the matrix entries, not remembered. Do not "simplify"
them back to a remembered form without re-running this probe.

Read-only: writes no witness, runs no producer.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mpmath import mp, mpf, matrix, log, cosh, nstr, norm  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402

mp.dps = 60
TOL = mpf(10) ** (-50)


def kron(a, b):
    m = matrix(a.rows * b.rows, a.cols * b.cols)
    for i in range(a.rows):
        for j in range(a.cols):
            for k in range(b.rows):
                for l in range(b.cols):
                    m[i * b.rows + k, j * b.cols + l] = a[i, j] * b[k, l]
    return m


I2 = matrix([[1, 0], [0, 1]])
SZ = matrix([[1, 0], [0, -1]])
SP = matrix([[0, 1], [0, 0]])
SM = matrix([[0, 0], [1, 0]])


def eye(d):
    m = matrix(d, d)
    for k in range(d):
        m[k, k] = 1
    return m


def op_at(op, k, n):
    m = matrix([[1]])
    for j in range(n):
        m = kron(m, op if j == k else I2)
    return m


def embed(op2, i, n):
    m = matrix([[1]])
    for _ in range(i):
        m = kron(m, I2)
    m = kron(m, op2)
    for _ in range(n - i - 2):
        m = kron(m, I2)
    return m


def tl_generator(q):
    """e = |w><w| with |w> = q^{1/2}|ud> - q^{-1/2}|du>; <w|w> = q + 1/q."""
    e = matrix(4, 4)
    e[1, 1] = q
    e[1, 2] = -1
    e[2, 1] = -1
    e[2, 2] = 1 / q
    return e


def main():
    checks, failures = 0, []

    def check(name, ok, detail=""):
        nonlocal checks
        checks += 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
        if not ok:
            failures.append(name)

    print("TL(delta) IS the U_q(sl_2) open XXZ chain at Delta = delta/2\n")
    print(f"mp.dps = {mp.dps}, tolerance = 1e-50\n")

    pins = [("proton (production default)", q_at(mp.dps)),
            ("muon   (ideal CAL-2)",        q_muon_at(mp.dps))]

    for label, q in pins:
        delta, hh = q + 1 / q, q - 1 / q
        Delta = delta / 2
        print(f"--- {label} ---")
        print(f"  q0            = {nstr(q, 25)}")
        print(f"  delta = [2]_q = {nstr(delta, 25)}   (TL loop weight)")
        print(f"  Delta         = {nstr(Delta, 25)}   (XXZ anisotropy)")
        print(f"  ln q0         = {nstr(log(q), 25)}")

        e = tl_generator(q)
        check("1. TL relation e^2 = delta*e",
              norm(e * e - delta * e) < TOL,
              f"residual {nstr(norm(e * e - delta * e), 6)}")

        check("2. Delta == cosh(ln q0)",
              abs(Delta - cosh(log(q))) < TOL)

        XXYY = 2 * (kron(SP, SM) + kron(SM, SP))
        ZZ = kron(SZ, SZ)
        two_site = (XXYY + Delta * ZZ - Delta * eye(4)
                    - (hh / 2) * (kron(SZ, I2) - kron(I2, SZ)))
        check("3. two-site coefficient identity",
              norm(-2 * e - two_site) < TOL,
              f"residual {nstr(norm(-2 * e - two_site), 6)}")

        for n in (2, 3, 4, 5):
            h_tl, h_xxz = matrix(2 ** n, 2 ** n), matrix(2 ** n, 2 ** n)
            for i in range(n - 1):
                h_tl = h_tl + embed(e, i, n)
                h_xxz = h_xxz + embed(XXYY + Delta * ZZ, i, n)
            rhs = (h_xxz - Delta * (n - 1) * eye(2 ** n)
                   - (hh / 2) * (op_at(SZ, 0, n) - op_at(SZ, n - 1, n)))
            r = norm(-2 * h_tl - rhs)
            check(f"4. chain identity, n={n} (boundary telescopes)",
                  r < TOL, f"residual {nstr(r, 6)}")

        check("5. Delta > 1  =>  MASSIVE/Ising-like regime (Bethe strings stable)",
              Delta > 1, f"Delta - 1 = {nstr(Delta - 1, 12)}")
        print()

    dp, dm = [(q + 1 / q) / 2 for _, q in pins]
    sep = abs(dm - dp) / dp * 10 ** 9
    print(f"pin-independence: |Delta_muon - Delta_proton| / Delta_proton = "
          f"{nstr(sep, 8)} ppb")
    check("6. the regime verdict is pin-independent (< 100 ppb apart)", sep < 100)

    print(f"\n{checks - len(failures)}/{checks} checks pass")
    if failures:
        print("FAILED: " + ", ".join(failures))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
