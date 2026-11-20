#!/usr/bin/env python3
# polynomial_q_not_applicable: reads q_0 only to evaluate characters; the
# question asked here is about the Markov parameter z, not about the anchor.
"""Does the Ind_{H3}^{H4} Markov reduction depend on the z convention? (qou-ze9n)

`QOU/Machinery/MarkovTraceOnHecke.lean` cites
`computations/probes/markov_reduction_h3_to_h4_verify.py` as the evidence for
keystone ingredient 2. That probe has three defects, found 2026-08-22:

1. **Convention C.** It sets `z = float(+(1.0/(mp.sqrt(Q_MP) + 1.0/mp.sqrt(Q_MP))))`
   = 0.4993203342 = `sqrt(q)/(q+1)` = z_C. The owner ruling of 2026-08-15 makes
   convention D (`z = q**3/(q**2+1)` = 0.6126880371) canonical and excises C.
   The two differ by 23 %. The spelling was invisible to
   `scripts/convention-c-producer-audit.py` until the `unwrap_casts()` fix in
   the same commit as this file (blind spelling #14).
2. **float64 throughout**, against the STRICT "PROBES ARE NOT EXEMPT"
   directive: `np.linalg.solve` for the weights, `float(np.trace(...))`, and a
   `mp.workdps(100)` block cast straight to `float` on the same line — the dps
   no-op the precision gates exist to catch. **The float64 was never
   necessary**: `BlockCache`/`build_seminormal_matrices_cached` accept `mpf`
   and return `mpf` entries, verified here at 50 dps.
3. **It does not run as committed.** Its bootstrap omits
   `tools/qou-substrate/python`, and adds `tools/pyhecke/python/pyhecke`
   (the package directory) where `import pyhecke.X` needs the parent
   `tools/pyhecke/python`. Since neither package is installable (both 404 on
   PyPI per AGENTS.md), the cited evidence does not execute in a clean
   checkout.

## What this probe answers

Whether the *conclusion* survives the convention swap — which is a different
question from whether the code is off-canon, and the one that decides whether
`MarkovTraceOnHecke.lean`'s ingredient-2 paragraph needs rewriting.

The construction under test builds `tr_M^{H_n}(b) = sum_lambda y_lambda
chi^lambda(b)` with the weights `y_lambda` SOLVED from the n Markov
constraints `tr(1) = 1`, `tr(sigma-word of length k) = z^k`. So `z` is an
*input* to the weight solve, not an output. Classically the Ocneanu trace is a
one-parameter family in `z`, so the prediction is that the reduction holds for
BOTH conventions and the C defect does not touch the conclusion.

That prediction is what this file tests, at 50 dps, on the same
over-determination words the original uses — H_3 words deliberately outside
the constraint set.

Scope-(a): this says the *evidence* is convention-robust. It does NOT say the
original probe is fine, and it is NOT a symbolic-exact proof over Q(z,h) — a
Lean-grade H_4 statement still needs that.
"""
from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [
    str(_ROOT / "computations"),
    str(_ROOT / "qou-mass" / "src" / "qou_mass" / "_internal"),
    str(_ROOT / "tools" / "pyhecke" / "python"),      # parent, not the package dir
    str(_ROOT / "tools" / "qou-substrate" / "python"),  # omitted by the original
]

import mpmath as mp  # noqa: E402

from pyhecke.syt_prefix_cache import (  # noqa: E402
    BlockCache,
    build_seminormal_matrices_cached,
)
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 50

# The proton pin, IMPORTED rather than hardcoded. The hardcoded literal this
# replaced carried 17 digits while the probe computes at 50 dps, and a
# hand-copied pin is exactly the failure `q0_stamp.stamp_q0_anchor` refuses to
# stamp: a producer can silently drift from the pin its witness declares.
from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

Q = Q_MP         # proton pin (experimental layer, per the
H = Q - 1 / Q                      # 2026-08-07 directive)

Z_C = 1 / (mp.sqrt(Q) + 1 / mp.sqrt(Q))   # sqrt(q)/(q+1)  -- excised
Z_D = Q ** 3 / (Q ** 2 + 1)               # canonical since 2026-08-15
TOL = mp.mpf(10) ** -30                   # vs the original's float64 1e-9


def partitions_of(n):
    def gen(m, mx):
        if m == 0:
            yield ()
            return
        for k in range(min(m, mx), 0, -1):
            for rest in gen(m - k, k):
                yield (k,) + rest
    return list(gen(n, n))


def _dense(m):
    return m.toarray() if hasattr(m, "toarray") else m


def chi(shape_sigmas, word):
    """chi_lambda(word), carried in mpmath end to end. sigma^-1 = sigma - h*I."""
    d = _dense(shape_sigmas[0]).shape[0]
    M = mp.eye(d)
    for (g, s) in word:
        A = _dense(shape_sigmas[g])
        B = mp.matrix(d, d)
        for i in range(d):
            for j in range(d):
                B[i, j] = A[i, j] - (H if (s != 1 and i == j) else 0)
        M = M * B
    return sum(M[i, i] for i in range(d))


_CONSTRAINT_WORDS = {
    3: [[], [(0, 1)], [(0, 1), (1, 1)]],
    4: [[], [(0, 1)], [(0, 1), (1, 1)], [(0, 1), (2, 1)],
        [(0, 1), (1, 1), (2, 1)]],
}
_CONSTRAINT_POWERS = {3: [0, 1, 2], 4: [0, 1, 2, 2, 3]}


def build_Hn(n, z, cache):
    shapes = partitions_of(n)
    data = {shp: [_dense(s) for s in build_seminormal_matrices_cached(shp, cache=cache)[0]]
            for shp in shapes}
    words = _CONSTRAINT_WORDS[n]
    k = len(shapes)
    A = mp.matrix(k, k)
    for r, w in enumerate(words):
        for c, shp in enumerate(shapes):
            A[r, c] = chi(data[shp], w)
    b = mp.matrix([z ** p for p in _CONSTRAINT_POWERS[n]])
    y = mp.lu_solve(A, b)
    return shapes, data, {shp: y[i] for i, shp in enumerate(shapes)}


TESTS = {
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


def run(label, z, cache):
    H3 = build_Hn(3, z, cache)
    H4 = build_Hn(4, z, cache)
    def tr3(w): return sum(H3[2][s] * chi(H3[1][s], w) for s in H3[0])
    def tr4(w): return sum(H4[2][s] * chi(H4[1][s], w) for s in H4[0])

    print(f"\n[{label}]  z = {mp.nstr(z, 12)}")
    worst_red = worst_restr = mp.mpf(0)
    for name, x in TESTS.items():
        t3, t4, t4s = tr3(x), tr4(x), tr4(x + [(2, 1)])
        worst_red = max(worst_red, abs(t4s - z * t3))
        worst_restr = max(worst_restr, abs(t4 - t3))
    ok = worst_red < TOL and worst_restr < TOL
    print(f"    worst |tr4(x.s2) - z*tr3(x)| = {mp.nstr(worst_red, 4)}")
    print(f"    worst |tr4(x)     - tr3(x)| = {mp.nstr(worst_restr, 4)}")
    print(f"    -> {'PASS' if ok else 'FAIL'} at 1e-30 over {len(TESTS)} "
          f"over-determination words")
    return ok, worst_red, worst_restr


def main() -> int:
    print("=" * 74)
    print(" Ind_{H3}^{H4} Markov reduction — convention C vs D, at 50 dps")
    print("=" * 74)
    print(f"q_0 = {mp.nstr(Q, 17)}   h = {mp.nstr(H, 12)}")
    print(f"z_C = {mp.nstr(Z_C, 12)}   z_D = {mp.nstr(Z_D, 12)}   "
          f"|C-D| = {mp.nstr(abs(Z_C - Z_D), 6)}")

    cache = BlockCache(Q, H)
    okC, redC, restrC = run("convention C (excised)", Z_C, cache)
    okD, redD, restrD = run("convention D (canonical)", Z_D, cache)

    print("\n" + "=" * 74)
    if okC and okD:
        verdict = ("CONVENTION-ROBUST — the reduction holds under both. z is an "
                   "input to the weight solve, so the C defect in the cited "
                   "probe does not touch its conclusion.")
    elif okD and not okC:
        verdict = "D-ONLY — the cited C-frame conclusion does not survive."
    elif okC and not okD:
        verdict = "C-ONLY — tension with the 2026-08-15 ruling; escalate."
    else:
        verdict = "NEITHER — the construction itself is in question."
    print(f"  RESULT: {verdict}")

    wb = WitnessBuilder("markov-reduction-h3-to-h4-conventions",
                        engine="hoefsmit-seminormal-mpmath")
    wb.set_description(
        "Re-runs the Ind_{H3}^{H4} Markov-reduction over-determination test at "
        "50 dps under BOTH Markov-parameter conventions. The probe "
        "MarkovTraceOnHecke.lean cites for keystone ingredient 2 uses "
        "convention C (excised 2026-08-15), computes in float64, and does not "
        "run as committed (two bootstrap-path bugs). This asks whether its "
        "CONCLUSION survives the swap. Bean qou-ze9n; scope-(a); nothing wired."
    )
    wb.add_data("z_C", mp.nstr(Z_C, 30))
    wb.add_data("z_D", mp.nstr(Z_D, 30))
    wb.add_data("worst_residuals", {
        "C": {"reduction": mp.nstr(redC, 6), "restriction": mp.nstr(restrC, 6)},
        "D": {"reduction": mp.nstr(redD, 6), "restriction": mp.nstr(restrD, 6)},
    })
    wb.add_data("verdict", verdict)
    wb.add_assertion("reduction_holds_convention_C",
                     computed=str(bool(okC)), expected="True",
                     tolerance="1e-30", source="over-determination, 9 words")
    wb.add_assertion("reduction_holds_convention_D",
                     computed=str(bool(okD)), expected="True",
                     tolerance="1e-30", source="over-determination, 9 words")
    # q0Value is REQUIRED beside the anchor: `stamp_q0_anchor` is a no-op once
    # a payload declares `q0Anchor` itself, so a hand-declared anchor with no
    # value lands as Q0_VALUE_MISSING -- the audit cannot check the pin.
    wb.save({"q0Anchor": "proton",
             "q0Value": Q_50_DIGIT_STR,
             "q0AnchorReason": "characters evaluated at the experimental pin "
                               "per the 2026-08-07 directive; the question is "
                               "about z, not the anchor"})
    return 0 if (okC and okD) else 1


if __name__ == "__main__":
    raise SystemExit(main())
