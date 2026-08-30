"""Degree-`d` algebraic-independence probe for the three canonical jet series.

Upgrades the corpus's *linear* jet certificate to a *polynomial* one.

`jet_order_pivots.py` shows the h-jet expansions of `tr_M(4_1)`, `tr_M(5_2)`,
`tr_M(Borromean)` about `q = 1` are **linearly** independent at jet order 2
(rank-3 Jacobian, elimination determinant 1/16). That is
`QOU.Archimedean.JetOrderIndependence.full_rank` at the base order.

This probe asks the much stronger, and equally decidable, question:

    is there a non-zero P in Q[x,y,z] of total degree <= d with
    P(tr_M(4_1), tr_M(5_2), tr_M(B_3)) = O(h^(N+1))  as a series in h?

Method (exact, no floats anywhere):

1. Each `tr_M(K)` is a rational function of `q`; substitute `q = 1 + h` and
   Taylor-expand by exact power-series division of numerator by denominator
   over Q. O(N^2) rational operations, far cheaper than `sympy.series`.
2. Form every monomial `x^i y^j z^k`, `i+j+k <= d`, as an h-series to order N
   (exact Q coefficients) by series multiplication.
3. Build the M x (N+1) coefficient matrix over Q (M = C(d+3,3) monomials) and
   compute its exact null space.

## RESULT: relations exist, and the minimal degree is 7

The three traces are rational functions of `u = sqrt(q)` (numerator/denominator
u-degrees 14/9, 16/9, 18/9 for 4_1 / 5_2 / B_3), so all three lie in `Q(u)`,
which has **transcendence degree 1 over Q**. Any *two* elements of such a field
are already algebraically dependent -- so a relation among the three is
**forced**, and the only open question is its degree. Measured here:

| degree d | equations       | null space | stable? |
|----------|-----------------|------------|---------|
| <= 6     | 93 -> 385       | 0          | yes -- no relation |
| 7        | 129 -> 421      | 3          | yes -- genuine, 3-dimensional |

So the minimal degree of an algebraic relation among the three canonical
Markov-trace jets is exactly **7**.

Reading a result:

* A null vector is an annihilator only *to the order tested*. The test needs
  `N + 1 >= M`; below that the system is underdetermined and any null vector
  is an artifact. Necessary but not sufficient: the honest check is
  **stability** -- re-run with far more equations and confirm the dimension
  does not drop. Adding equations can only raise the rank, so a dimension that
  survives a large margin increase is genuine. `--stability` does this.
* `self_test` is the positive control: it plants `z - x^2 + 2y` and requires
  the probe to recover it. A negative result is worthless without it.

## SCOPE -- what this does NOT show (read before citing)

This is a statement about the **fibre-level Markov traces**, not about the
hyperbolic volumes. The `h`-jet of `tr_M(K)` at `q = 1` is not an expansion of
`Vol(K)`: the volume appears in the *root-of-unity* asymptotics
(`Vol(K) = lim (2*pi/n)*log|J_K(e^(2*pi*i/n))|`), not in the `q -> 1` jet. So a
negative result here does **not** prove `conj:hyperbolic-volume-transcendence`.

The missing step is exactly the bridge audited in
`QOU.Archimedean.JetOrderIndependence` -- `SurrealParallelTransportBound`
together with `JetTransportImpliesIndependence` -- which is conjectural and,
until 2026-08-09, was discharged by a vacuous all-zero instance.

What the probe *does* deliver is a sharp, machine-checked strengthening of the
QOU-native half of the reduction, and the exact degree at which it was
verified.

Ref: conj:three-knot-jet-order-independence
Ref: docs/audits/2026-08-09-surreal-squeeze-cannot-decide-algebraic-independence.md
"""

from __future__ import annotations

import json
import sys
import time
from itertools import product
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE / "substrate"))
sys.path.insert(0, str(_HERE.parent / "qou-mass" / "src"))

import sympy as sp  # noqa: E402

from qou_mass._internal.markov_trace_recursive import markov_trace_of_word  # noqa: E402
from knot_braid_database import braid_word_for_knot  # noqa: E402

KNOTS = ["4_1", "5_2", "Borromean"]


def _trace_rational(knot: str) -> sp.Expr:
    """`tr_M(knot)` as a rational function of its own `q` symbol."""
    bw = braid_word_for_knot(knot)
    word = [s * g for (s, g) in bw]
    tr = markov_trace_of_word(3, word)
    q_syms = [s for s in tr.free_symbols if s.name == "q"]
    if len(q_syms) != 1:
        raise ValueError(
            f"expected exactly one 'q' symbol in tr_M({knot}); got "
            f"{sorted(str(s) for s in tr.free_symbols)}"
        )
    return tr, q_syms[0]


def jet_series(knot: str, order: int) -> list[sp.Rational]:
    """Exact Taylor coefficients of `tr_M(knot)` about `q = 1`, orders 0..order.

    The Markov traces carry a framing factor `sqrt(q)`, so they are rational in
    `u = sqrt(q)` rather than in `q`. We therefore expand in `g = u - 1`, i.e.
    `q = (1+g)^2`, instead of `h = q - 1`.

    This is legitimate for an independence probe: `h = 2g + g^2` is a formal
    change of variable with non-zero linear term, hence invertible as a formal
    power series, so a family of series admits an annihilator in `h` iff it
    admits one in `g`. The vanishing *orders* rescale but the null space does
    not change.

    Power-series division of numerator by denominator over Q -- exact, and
    O(order^2) instead of `sympy.series`'s much heavier machinery.
    """
    tr, q = _trace_rational(knot)
    u = sp.symbols("u", positive=True)
    g = sp.symbols("g")
    tr_u = sp.powsimp(tr.subs(q, u**2), force=True)
    if tr_u.has(sp.sqrt(u)) or any(s.name not in ("u",) for s in tr_u.free_symbols):
        raise ValueError(
            f"tr_M({knot}) is not rational in u = sqrt(q); "
            f"free_symbols={sorted(str(s) for s in tr_u.free_symbols)}"
        )
    num, den = sp.fraction(sp.cancel(sp.together(tr_u.subs(u, 1 + g))))
    pn = sp.Poly(sp.expand(num), g)
    pd = sp.Poly(sp.expand(den), g)

    a = [sp.Rational(pn.coeff_monomial(g**k)) for k in range(order + 1)]
    b = [sp.Rational(pd.coeff_monomial(g**k)) for k in range(order + 1)]
    if b[0] == 0:
        raise ValueError(f"tr_M({knot}) is singular at q = 1 (denominator g-order > 0)")

    c: list[sp.Rational] = []
    for n in range(order + 1):
        s = a[n] - sum(b[k] * c[n - k] for k in range(1, n + 1))
        c.append(sp.Rational(s, 1) / b[0])
    return c


def _mul(u: list[sp.Rational], v: list[sp.Rational], order: int) -> list[sp.Rational]:
    """Truncated product of two h-series."""
    out = [sp.Integer(0)] * (order + 1)
    for i, ui in enumerate(u):
        if ui == 0:
            continue
        for j in range(0, order + 1 - i):
            if v[j] != 0:
                out[i + j] += ui * v[j]
    return out


def monomial_exponents(d: int) -> list[tuple[int, int, int]]:
    """All (i,j,k) with i+j+k <= d, in graded order."""
    return sorted(
        [e for e in product(range(d + 1), repeat=3) if sum(e) <= d],
        key=lambda e: (sum(e), e),
    )


def probe(d: int, margin: int = 8, verbose: bool = True) -> dict:
    exps = monomial_exponents(d)
    M = len(exps)
    order = M + margin  # need order+1 >= M for the test to be meaningful
    t0 = time.time()

    if verbose:
        print(f"[d={d}] {M} monomials, expanding to h^{order} "
              f"({order + 1} equations)", flush=True)

    base = {}
    for kn in KNOTS:
        ts = time.time()
        base[kn] = jet_series(kn, order)
        if verbose:
            print(f"[d={d}]   jet {kn:<10} done ({time.time() - ts:.1f}s)", flush=True)

    one = [sp.Integer(1)] + [sp.Integer(0)] * order
    powers = {}
    for kn in KNOTS:
        acc = list(one)
        powers[(kn, 0)] = acc
        for p in range(1, d + 1):
            acc = _mul(acc, base[kn], order)
            powers[(kn, p)] = acc

    rows = []
    for n_, (i, j, k) in enumerate(exps):
        s = _mul(_mul(powers[(KNOTS[0], i)], powers[(KNOTS[1], j)], order),
                 powers[(KNOTS[2], k)], order)
        rows.append(s)
        if verbose and (n_ + 1) % 10 == 0:
            print(f"[d={d}]   monomial {n_ + 1}/{M} "
                  f"({time.time() - t0:.1f}s elapsed)", flush=True)

    A = sp.Matrix(rows)  # M x (order+1), exact Q
    ns = A.T.nullspace()  # left null space of A == null space of A^T

    elapsed = time.time() - t0
    meaningful = (order + 1) >= M
    result = {
        "degree": d,
        "n_monomials": M,
        "h_order": order,
        "n_equations": order + 1,
        "test_meaningful": bool(meaningful),
        "nullspace_dim": len(ns),
        "annihilator_found": bool(len(ns) > 0),
        # Whole seconds, as an int.  This is diagnostic wall-clock, not a
        # computed quantity, so sub-second digits carry no information and
        # would be the only float64 in a witness whose entire point is that
        # the computation is exact over Q.  Emitting an int keeps the file
        # clean under the NO-FLOAT64 raw-float64 ratchet at the producer,
        # rather than by way of a baseline entry.
        "elapsed_sec": int(round(elapsed)),
    }
    if ns:
        result["example_annihilator"] = [
            {"exponents": list(exps[r]), "coeff": str(ns[0][r])}
            for r in range(M) if ns[0][r] != 0
        ]
    if verbose:
        verdict = ("ANNIHILATOR FOUND" if ns else "no annihilator")
        print(f"[d={d}] {verdict}  (nullspace dim {len(ns)}, "
              f"meaningful={meaningful}, {elapsed:.1f}s)", flush=True)
    return result


def self_test(verbose: bool = True) -> dict:
    """**Positive control.**  A "no annihilator" verdict is worthless unless the
    probe can find one that is really there.

    Replace the third series by `C' = A^2 - 2B`, a polynomial in the other two.
    The triple `(A, B, C')` then satisfies the degree-2 relation
    `z - x^2 + 2y = 0` exactly, and the probe must report nullspace dimension
    >= 1 with that annihilator among the null vectors.
    """
    d, margin = 2, 8
    exps = monomial_exponents(d)
    M = len(exps)
    order = M + margin

    A = jet_series(KNOTS[0], order)
    B = jet_series(KNOTS[1], order)
    C = [a - b for a, b in zip(_mul(A, A, order), [2 * x for x in B])]

    one = [sp.Integer(1)] + [sp.Integer(0)] * order
    base = [A, B, C]
    powers = []
    for s in base:
        acc, col = list(one), [list(one)]
        for _ in range(d):
            acc = _mul(acc, s, order)
            col.append(acc)
        powers.append(col)

    rows = [_mul(_mul(powers[0][i], powers[1][j], order), powers[2][k], order)
            for (i, j, k) in exps]
    ns = sp.Matrix(rows).T.nullspace()

    # the planted relation z - x^2 + 2y, as a coefficient vector
    want = {(0, 0, 1): sp.Integer(1), (2, 0, 0): sp.Integer(-1), (0, 1, 0): sp.Integer(2)}
    target = sp.Matrix([want.get(e, sp.Integer(0)) for e in exps])
    recovered = any(
        (v.normalized() - target.normalized()).norm() == 0
        or (v.normalized() + target.normalized()).norm() == 0
        for v in ns
    ) if ns else False

    ok = len(ns) >= 1 and recovered
    if verbose:
        print(f"[self-test] planted z - x^2 + 2y : nullspace dim {len(ns)}, "
              f"planted relation recovered = {recovered} -> "
              f"{'PASS' if ok else 'FAIL'}", flush=True)
    return {"nullspace_dim": len(ns), "planted_relation_recovered": bool(recovered),
            "passed": bool(ok)}


def main() -> int:
    args = sys.argv[1:]
    stability = "--stability" in args
    degrees = [int(x) for x in args if not x.startswith("-")] or [1, 2, 3]
    control = self_test()
    if not control["passed"]:
        print("SELF-TEST FAILED — negative results below are not trustworthy",
              file=sys.stderr)
        return 1
    runs = []
    for d in degrees:
        r = probe(d)
        if stability:
            # Adding equations can only raise the rank, so a null-space
            # dimension that survives a large margin increase is genuine and
            # not a truncation artifact.
            wide = probe(d, margin=300, verbose=False)
            r["stability_check"] = {
                "wide_n_equations": wide["n_equations"],
                "wide_nullspace_dim": wide["nullspace_dim"],
                "stable": bool(wide["nullspace_dim"] == r["nullspace_dim"]),
            }
            print(f"[d={d}] stability: dim {r['nullspace_dim']} -> "
                  f"{wide['nullspace_dim']} at {wide['n_equations']} equations "
                  f"({'STABLE' if r['stability_check']['stable'] else 'ARTIFACT'})",
                  flush=True)
        runs.append(r)

    def _clean_negative(r: dict) -> bool:
        if not r["test_meaningful"] or r["annihilator_found"]:
            return False
        sc = r.get("stability_check")
        return sc is None or sc["stable"]

    independent_to = max((r["degree"] for r in runs if _clean_negative(r)), default=0)
    relations_at = sorted(
        r["degree"] for r in runs
        if r["annihilator_found"] and r.get("stability_check", {"stable": True})["stable"]
    )
    witness = {
        "description": (
            "Degree-d algebraic-independence probe for the h-jet series of "
            "tr_M(4_1), tr_M(5_2), tr_M(Borromean) about q = 1. Exact rational "
            "power-series division + exact nullspace over Q."
        ),
        "scope_warning": (
            "FIBRE-LEVEL ONLY. The q->1 jet of tr_M is NOT an expansion of "
            "Vol(K) -- the volume lives in the root-of-unity asymptotics. This "
            "probe does not bear directly on conj:hyperbolic-volume-transcendence; "
            "the bridge (SurrealParallelTransportBound + "
            "JetTransportImpliesIndependence) remains conjectural."
        ),
        "structural_result": (
            "All three traces are rational in u = sqrt(q), hence lie in Q(u), "
            "which has transcendence degree 1 over Q. An algebraic relation among "
            "them is therefore FORCED -- any two elements of Q(u) are already "
            "dependent. The probe measures the minimal degree, not the existence."
        ),
        "knots": KNOTS,
        "positive_control": {
            "planted_relation": "z - x^2 + 2y  (with C := A^2 - 2B)",
            **control,
        },
        "runs": runs,
        "algebraically_independent_up_to_degree": independent_to,
        "minimal_relation_degree": (relations_at[0] if relations_at else None),
        "relations_confirmed_at_degrees": relations_at,
        "refs": [
            "conj:three-knot-jet-order-independence",
            "docs/audits/2026-08-09-surreal-squeeze-cannot-decide-algebraic-independence.md",
        ],
    }
    out = _HERE / "jet-algebraic-independence.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nwrote {out}")
    print(f"algebraically independent up to degree {independent_to}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
