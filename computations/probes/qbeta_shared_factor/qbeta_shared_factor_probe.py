#!/usr/bin/env python3
"""qbeta_shared_factor_probe — why every gluon word multiplies proton and neutron by one factor.

Preregistration: PREREGISTRATION.md (committed first). Lean: QOU/QBeta/QuarkWeightTrace.lean.

Exact rational arithmetic (fractions.Fraction) at q = 2 and q = 3/2.
  S1  Jimbo R commutes with Delta(F) for the two standard coproduct candidates (both reported).
  S2  for every admissible gluon word, Y = Tr_gluons(K^g rho(W)) commutes with Delta^3(F).
  S3  eps_p = q^2 eps_n exactly for every word.
  S4  the words with negative eps obey S3 as well.
"""
from __future__ import annotations

import importlib.util
import itertools
import sys
from fractions import Fraction as Fr
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
_spec = importlib.util.spec_from_file_location(
    "_gsw", _ROOT / "computations/probes/qbeta_gluon_strand_words/qbeta_gluon_strand_words_probe.py")
gsw = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gsw)
gg = gsw.gg

from witness_base import WitnessBuilder  # noqa: E402

QS = (Fr(2), Fr(3, 2))
FAMILY = ((4, 6), (5, 5))    # the committed gluon-strand family
RESULTS: list[tuple[str, bool, str]] = []


def check(name, ok, detail):
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}\n         {detail}\n", flush=True)


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n) if A[i][k]) for j in range(n)] for i in range(n)]


def kron(A, B):
    return [[A[i // len(B)][j // len(B)] * B[i % len(B)][j % len(B)]
             for j in range(len(A) * len(B))] for i in range(len(A) * len(B))]


def eye(n):
    return [[Fr(int(i == j)) for j in range(n)] for i in range(n)]


def add(A, B):
    return [[a + b for a, b in zip(r, s)] for r, s in zip(A, B)]


def rho(word, n, q):
    """Matrix of rho(word): column b = image of basis b."""
    M = [[Fr(0)] * 2 ** n for _ in range(2 ** n)]
    for b in range(2 ** n):
        v = {b: Fr(1)}
        for (i, s) in reversed(word):
            v = gg.apply_crossing(v, n, i, s, q)
        for a, c in v.items():
            M[a][b] = c
    return M


def ops(q):
    F = [[Fr(0), Fr(0)], [Fr(1), Fr(0)]]
    K = [[q, Fr(0)], [Fr(0), 1 / q]]
    Ki = [[1 / q, Fr(0)], [Fr(0), q]]
    return F, K, Ki, eye(2)


def coprod3(q):
    F, K, _Ki, I = ops(q)
    return add(add(kron(kron(F, K), K), kron(kron(I, F), K)), kron(kron(I, I), F))


def reduced(word, n, q):
    M = rho(word, n, q)
    g = n - 3
    Y = [[Fr(0)] * 8 for _ in range(8)]
    for gb in range(2 ** g):
        w = q ** (g - 2 * bin(gb).count("1"))
        for a in range(8):
            for b in range(8):
                Y[a][b] += w * M[(a << g) | gb][(b << g) | gb]
    return Y


def main() -> int:
    ok1, det1 = True, []
    for q in QS:
        R = rho([(0, 1)], 2, q)
        F, K, Ki, I = ops(q)
        for name, C in (("F(x)K+1(x)F", add(kron(F, K), kron(I, F))),
                        ("F(x)1+K^-1(x)F", add(kron(F, I), kron(Ki, F))),
                        ("F(x)K^-1+1(x)F", add(kron(F, Ki), kron(I, F))),
                        ("F(x)1+K(x)F", add(kron(F, I), kron(K, F)))):
            c = matmul(R, C) == matmul(C, R)
            det1.append(f"q={q} {name}: {'commutes' if c else 'does not'}")
            if name == "F(x)K+1(x)F":
                ok1 &= c
    check("S1_R_commutes_with_coproduct", ok1, "; ".join(det1) + ". Used: F(x)K+1(x)F.")

    core = gg.gg_word((0, 0, 0))
    ok2 = ok3 = ok4 = True
    nwords = nneg = 0
    bad = []
    for n, L in FAMILY:
        for ln in range(1, L + 1):
            for vs in itertools.product(range(n - 2), repeat=ln):
                if max(vs) + 2 < 3:
                    continue
                X = gg.gg_word(vs)
                if not gsw.perm_quarks_closed(X, n):
                    continue
                W = X + core
                nwords += 1
                for q in QS:
                    Y = reduced(W, n, q)
                    F3 = coprod3(q)
                    comm = matmul(Y, F3) == matmul(F3, Y)
                    t1 = sum(Y[a][a] for a in range(8) if bin(a).count("1") == 1)
                    t2 = sum(Y[a][a] for a in range(8) if bin(a).count("1") == 2)
                    ep, en = q * t1, t2 / q
                    rel = ep == q * q * en
                    ok2 &= comm
                    ok3 &= rel
                    if q == QS[0] and ep < 0:
                        nneg += 1
                        ok4 &= rel
                    if not (comm and rel):
                        bad.append((n, "".join(f"V{i}" for i in vs), str(q), comm, rel))
    check("S2_partial_trace_intertwines", ok2,
          f"{nwords} words x {len(QS)} values of q: Y = Tr_g(K^g rho(W)) commutes with "
          f"Delta^3(F) exactly. Counterexamples: {bad[:5]}")
    check("S3_eps_p_eq_q2_eps_n", ok3, f"eps_p = q^2 eps_n exactly in all {nwords} words at q = 2, 3/2.")
    check("S4_negative_words", ok4, f"{nneg} words with eps_p < 0 at q = 2 obey the same relation.")
    allp = all(o for _, o, _ in RESULTS)
    print(f"  {sum(o for _, o, _ in RESULTS)}/{len(RESULTS)} checks passed")
    wb = WitnessBuilder("qbeta-shared-factor", engine="fractions")
    for nm, o, d in RESULTS:
        wb.add_assertion(nm, computed="PASS" if o else "FAIL", expected="PASS",
                         tolerance="exact", source=d)
    wb.save({"description": ("U_q(sl2) intertwining explains why every gluon word multiplies "
                             "eps_p and eps_n by one factor: exact checks at q = 2, 3/2."),
             "q_values": [str(q) for q in QS], "family": [list(x) for x in FAMILY],
             "words": nwords, "counterexamples": bad})
    return 0 if allp else 1


if __name__ == "__main__":
    sys.exit(main())
