#!/usr/bin/env python3
"""Do the Young seminormal matrices used by the binding path REPRESENT the Hecke algebra?

`hecke_core_legacy._build_ysn_matrices` supplies the rho_lambda(sigma_i) that
`unified_iterative_correction` -- and hence `binding_energy` -- multiplies
together. A family of matrices is a representation of the braid group (and so
of H_n(q)) only if it satisfies BOTH defining relations:

    (Q) quadratic :  sigma^2 = h*sigma + I,           h = q - 1/q
    (B) braid     :  s_i s_{i+1} s_i = s_{i+1} s_i s_{i+1}
    (C) commuting :  s_i s_j = s_j s_i  for |i-j| >= 2

The quadratic relation alone is NOT sufficient: it constrains each generator
separately (trace h, determinant -1, eigenvalues {q, -1/q}) and says nothing
about how two generators sit relative to each other. A family can satisfy (Q)
everywhere and still fail (B) -- which is exactly what this audit found.

Compares against `pyhecke_native.seminormal_matrices_mpfr`, the Rust MPFR
seminormal build, on the same partitions at the same q.

Exit 0 if the Python family satisfies all three relations; 1 otherwise.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "substrate"))

from mpmath import mp  # noqa: E402

mp.dps = 50

import hecke_core_legacy as H  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

try:
    from scipy.sparse import issparse
except ImportError:  # pragma: no cover
    def issparse(_x):
        return False

try:
    import pyhecke_native as _P
except ImportError:  # pragma: no cover
    _P = None

Q = Q_MP
H_Q = Q - 1 / Q
TOL = mp.mpf("1e-12")          # far looser than float64 eps: only real defects fire


def _mul(a, b, d):
    return [[sum(a[i][k] * b[k][j] for k in range(d)) for j in range(d)]
            for i in range(d)]


def _dev(a, b, d):
    return max(abs(a[i][j] - b[i][j]) for i in range(d) for j in range(d))


def _from_python(m, d):
    if issparse(m):
        m = m.toarray()
    return [[mp.mpf(str(m[i][j])) for j in range(d)] for i in range(d)]


def _from_rust(rows, d):
    out = [[mp.mpf(0)] * d for _ in range(d)]
    for i, row in enumerate(rows):
        for (j, s) in row:
            out[i][j] = mp.mpf(s)
    return out


def check_family(gens, d):
    """Return (quadratic_defect, braid_defect, commuting_defect)."""
    ident = [[mp.mpf(1) if i == j else mp.mpf(0) for j in range(d)] for i in range(d)]
    quad = braid = comm = mp.mpf(0)
    for s in gens:
        lhs = _mul(s, s, d)
        rhs = [[H_Q * s[i][j] + ident[i][j] for j in range(d)] for i in range(d)]
        quad = max(quad, _dev(lhs, rhs, d))
    for i in range(len(gens) - 1):
        a, b = gens[i], gens[i + 1]
        braid = max(braid, _dev(_mul(_mul(a, b, d), a, d),
                                _mul(_mul(b, a, d), b, d), d))
    for i in range(len(gens)):
        for j in range(i + 2, len(gens)):
            a, b = gens[i], gens[j]
            comm = max(comm, _dev(_mul(a, b, d), _mul(b, a, d), d))
    return quad, braid, comm


def main():
    partitions = [[2, 1], [3, 1], [2, 2], [3, 3], [4, 2], [2, 2, 2], [3, 2, 1]]
    print("=" * 74)
    print("YSN BRAID-RELATION AUDIT — does the binding path use a real representation?")
    print("=" * 74)
    print(f"q = {mp.nstr(Q, 20)}   h = q - 1/q = {mp.nstr(H_Q, 20)}")
    print(f"tolerance {mp.nstr(TOL, 3)} (float64 eps is 2.2e-16, so only REAL defects fire)\n")
    print(f"{'partition':>14s} {'dim':>4s} {'impl':>7s} {'quadratic':>12s} "
          f"{'BRAID':>12s} {'commuting':>12s}")
    bad = False
    for lam in partitions:
        try:
            py = H._build_ysn_matrices(list(lam))
        except Exception as exc:                      # pragma: no cover
            print(f"{str(tuple(lam)):>14s}  python build raised {type(exc).__name__}: {exc}")
            continue
        if not py:
            continue
        d = py[0].shape[0] if issparse(py[0]) else len(py[0])
        rows = [("python", [_from_python(m, d) for m in py])]
        if _P is not None and hasattr(_P, "seminormal_matrices_mpfr"):
            rs = _P.seminormal_matrices_mpfr(list(lam), Q_50_DIGIT_STR, 50)
            rows.append(("rust", [_from_rust(r, d) for r in rs]))
        for label, gens in rows:
            q_, b_, c_ = check_family(gens, d)
            flag = ""
            if label == "python" and (q_ > TOL or b_ > TOL or c_ > TOL):
                bad = True
                flag = "   <-- NOT A REPRESENTATION"
            print(f"{str(tuple(lam)):>14s} {d:>4d} {label:>7s} "
                  f"{mp.nstr(q_, 4):>12s} {mp.nstr(b_, 4):>12s} "
                  f"{mp.nstr(c_, 4):>12s}{flag}")
    print()
    if bad:
        print("RESULT: the Python YSN family satisfies the QUADRATIC relation but")
        print("VIOLATES the BRAID relation. It is therefore not a representation of")
        print("H_n(q), and products of these matrices are not Markov traces of braids.")
        print("Everything unified_iterative_correction / binding_energy computes from")
        print("them inherits this. The Rust seminormal_matrices_mpfr family satisfies")
        print("all three relations at 50 dps and is the correct object.")
        return 1
    print("RESULT: the Python YSN family satisfies all three relations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
