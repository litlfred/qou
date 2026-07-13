"""Preflight verification: the H_4(q) Markov trace extends H_3 via the
Ind_{H3}^{H4} Markov reduction.

Motivation
----------
`QOU.Machinery.MarkovTraceOnHecke` (Lean) realizes the Markov trace concretely
for H_3(q) — sorry-free (M1) linearity, (M2) cyclicity, (M3) reduction — and
its "Extending past H_3" scope note lists the two ingredients any H_4+ Lean
formalization needs: (1) the H_4 NF basis + multiplication table, and (2) the
Ind_{H3}^{H4} Markov stabilization.  This script gives the honest compute
preflight for ingredient (2), *before* any Lean is written (per AGENTS.md
§"Formalize-first probe discipline" + the anti-laundering rule: verify the
identity symbolically/numerically first, do not hand-write an unverified
table).

What is checked
---------------
Using the SAME verified seminormal (Hoefsmit) machinery as the production
`computations/alpha/alpha_k_jones_markov_h4.py`:

  tr_M^{H_n}(beta) = sum_{lambda |- n} y_lambda * chi^lambda(beta),

with the weights y_lambda SOLVED from the n Markov-property constraints
(tr(1)=1, tr(sigma-words)=z^k, z = 1/(sqrt q + 1/sqrt q)) — the same fit the
H_3 production template uses.  Then, on H_3 words in <sigma_0, sigma_1> that
are DELIBERATELY NOT among the 5 constraint words (an over-determination
test), it verifies

  (M3-Ind)  tr_M^{H4}(x . sigma_2) = z * tr_M^{H3}(x)     [Markov reduction]
  (restr.)  tr_M^{H4}(x)           = tr_M^{H3}(x)         [trace restricts]

Both hold to float64 precision (~1e-9), matching the "randomized" numerical
cross-check tier the H_3 Lean file documents against `gram.py`.  This is
evidence, NOT a symbolic-exact proof: a Lean-grade H_4 formalization still
needs the GB-NF Fin-24 table (ingredient 1) built from the same verified
source and a cyclicity proof over Q(z,h).
"""
from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [
    str(_ROOT / "qou-mass" / "src" / "qou_mass" / "_internal"),
    str(_ROOT / "tools" / "pyhecke" / "python" / "pyhecke"),
]

import numpy as np  # noqa: E402
import mpmath as mp  # noqa: E402
from q_parameter import Q as Q0_FLOAT, Q_MP  # noqa: E402
from syt_prefix_cache import BlockCache, build_seminormal_matrices_cached  # noqa: E402

q = float(Q0_FLOAT)
h = q - 1.0 / q
z = float(1.0 / (mp.sqrt(Q_MP) + 1.0 / mp.sqrt(Q_MP)))  # Markov parameter
TOL = 1e-9


def partitions_of(n):
    def gen(m, mx):
        if m == 0:
            yield ()
            return
        for k in range(min(m, mx), 0, -1):
            for rest in gen(m - k, k):
                yield (k,) + rest
    return list(gen(n, n))


def chi(shape_sigmas, word):
    """chi_lambda(word): character of a braid word in the seminormal rep.
    word is a list of (generator_index, +-1); sigma^{-1} = sigma - h*I."""
    d = shape_sigmas[0].shape[0]
    M = np.eye(d)
    for (g, s) in word:
        A = shape_sigmas[g] if s == 1 else (shape_sigmas[g] - h * np.eye(d))
        M = M @ A
    return float(np.trace(M))


# Markov-property constraints (tr_M(sigma-word) = z^k) that pin the n weights.
_CONSTRAINTS = {
    3: ([[], [(0, 1)], [(0, 1), (1, 1)]],
        [1.0, z, z ** 2]),
    4: ([[], [(0, 1)], [(0, 1), (1, 1)], [(0, 1), (2, 1)], [(0, 1), (1, 1), (2, 1)]],
        [1.0, z, z ** 2, z ** 2, z ** 3]),
}


def build_Hn(n):
    cache = BlockCache(q, h)
    shapes = partitions_of(n)
    data = {}
    for shp in shapes:
        sig, _, _ = build_seminormal_matrices_cached(shp, cache=cache)
        data[shp] = [s.toarray() if hasattr(s, "toarray") else np.asarray(s) for s in sig]
    words, b = _CONSTRAINTS[n]
    A = np.array([[chi(data[shp], w) for shp in shapes] for w in words])
    y_vec = np.linalg.solve(A, np.array(b, dtype=float))
    return shapes, data, {shp: float(v) for shp, v in zip(shapes, y_vec)}


def main() -> int:
    H3 = build_Hn(3)
    H4 = build_Hn(4)
    tr3 = lambda w: sum(H3[2][s] * chi(H3[1][s], w) for s in H3[0])
    tr4 = lambda w: sum(H4[2][s] * chi(H4[1][s], w) for s in H4[0])

    print(f"q_0 = {q:.10f}   h = {h:.10f}   z = 1/(sqrt q + 1/sqrt q) = {z:.10f}")
    print(f"norm  tr3(1)={tr3([]):.10f}  tr4(1)={tr4([]):.10f}   (expect 1)")
    print(f"      tr3(s0)={tr3([(0,1)]):.10f}  tr4(s0)={tr4([(0,1)]):.10f}  (expect z={z:.10f})")
    print()

    # H_3 words (in sigma_0, sigma_1) that are NOT constraint words.
    tests = {
        "s0^2":        [(0, 1), (0, 1)],
        "s1^2":        [(1, 1), (1, 1)],
        "s0 s1 s0":    [(0, 1), (1, 1), (0, 1)],
        "s1 s0 s1":    [(1, 1), (0, 1), (1, 1)],
        "s0^2 s1":     [(0, 1), (0, 1), (1, 1)],
        "s0 s1^2":     [(0, 1), (1, 1), (1, 1)],
        "s0 s1 s0 s1": [(0, 1), (1, 1), (0, 1), (1, 1)],
        "s0^-1 s1":    [(0, -1), (1, 1)],
        "s0 s1 s0^2":  [(0, 1), (1, 1), (0, 1), (0, 1)],
    }
    hdr = f"{'x (in H3)':<13}{'tr3(x)':>13}{'tr4(x)':>13}{'tr4(x.s2)':>13}{'z*tr3(x)':>13}  red restr"
    print(hdr)
    red_ok = restr_ok = True
    for name, x in tests.items():
        t3, t4, t4s = tr3(x), tr4(x), tr4(x + [(2, 1)])
        r = abs(t4s - z * t3) < TOL
        s = abs(t4 - t3) < TOL
        red_ok &= r
        restr_ok &= s
        print(f"{name:<13}{t3:>13.8f}{t4:>13.8f}{t4s:>13.8f}{z * t3:>13.8f}  "
              f"{'OK' if r else 'FAIL':>3} {'OK' if s else 'FAIL':>5}")

    print()
    print(f"(M3-Ind)  tr4(x.s2) = z*tr3(x) : {'ALL PASS' if red_ok else 'FAIL'}")
    print(f"(restr.)  tr4(x)     = tr3(x)  : {'ALL PASS' if restr_ok else 'FAIL'}")
    ok = red_ok and restr_ok
    print(f"OVERALL: {'PASS — H4 Markov trace extends H3 via the Ind reduction' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
