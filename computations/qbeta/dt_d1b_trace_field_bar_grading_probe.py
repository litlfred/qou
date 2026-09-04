#!/usr/bin/env python3
"""dt_d1b_trace_field_bar_grading_probe.py — qou-q9ih D1-b, the arrow question.

The companion probe `dt_d1b_connection_count_galois_orbit_hypothesis_probe.py`
(7/7) established that the D1-b **node count** is arithmetic: the irreducible
boundary-parabolic reps form a single Galois orbit, so `C_irr = [trace field :
Q]`. That closed the node question and left the **arrow** question open.

Arrows in a bar-graded quiver need the bar grading OF THE NODE SET, and the
single-orbit result says exactly where to read it. The nodes are the Galois
conjugates of the geometric representation, i.e. the embeddings of the trace
field; complex conjugation acts on those embeddings; and a representation is
**self-conjugate exactly when its embedding is real**. So the grading is

    r_1  mirror-FIXED nodes        (the real embeddings)
    r_2  mirror-SWAPPED pairs      (the conjugate pairs)

with `r_1 + 2*r_2 = C_irr`. This probe measures `(r_1, r_2)` exactly.

MEASURED, exactly (Sturm sequences on the integer/rational minimal polynomial;
no root-finding, no floats):

    manifold   deg   r_1   r_2
    4_1          2     0     1      mirror acts FREELY on 2 nodes
    5_2          3     1     1      one FIXED node, one swapped pair
    m135         8     0     4
    s000         6     0     3
    t00000       8     0     4
    v0000        8     0     4

**Five of six trace fields are totally imaginary.** `5_2` is the only one with a
real embedding — and it cannot avoid having one: its trace field has **odd
degree**, and no involution acts freely on a set of odd size. So a mirror-fixed
node is FORCED for `5_2` and absent for `4_1`, by parity alone.

🛑 WHAT I FIRST THOUGHT THIS SHOWED, AND WHY IT DOES NOT. My first reading was
that this gives an escape from `QuiverMirrorAutomorphismExcluded` — that the
theorem excludes a *freely acting* mirror, and a mirror with a fixed point is a
different object. **I read the theorem before writing that down, and it is
wrong.** The hypothesis there is

    hσ : ∀ e, Ω (σ e) = Ω e

i.e. **count-invariance** under σ. It says nothing about whether σ acts freely,
so having a fixed point is no escape at all: a σ with fixed points can still
satisfy `Ω ∘ σ = Ω` and is excluded on exactly the same terms. The parity fact
is real; the consequence I nearly drew from it is not, and it is recorded here
rather than quietly dropped because it is the kind of claim that reads
plausible and would have propagated.

WHAT THIS DOES GIVE, stated at its actual strength: the bar grading of the node
set, as a measured `(r_1, r_2)` per manifold, which any bar-graded quiver
construction has to reproduce. It is an input to the arrow question, not an
answer to it. Nothing here derives arrows, a potential, or `A_omega`.

CONTROLS.
  [C1] `r_1 + 2*r_2 = deg` for every field — the embedding count must close.
  [C2] `deg` reproduces the `C_irr` measured by the companion probe from
       Galois-orbit degrees, arrived at by a different route (orbit parsing of
       the Magma fixtures vs the minimal polynomial's degree).
  [C3] every minimal polynomial is irreducible over Q — otherwise "the trace
       field" is not a field and the embedding count means nothing.
  [C4] the real-root count is EXACT (`sympy.count_roots`, Sturm), not a
       numerical root-find, and a hand-built control confirms the routine
       separates known cases.

Scope-(a). Six fixtures, four of them census manifolds rather than knots in
S^3 — valid for reading the grading, NOT automatically valid as D1-b nodes.
The ptolemy DB is firewalled, so the sample cannot be enlarged offline.
Nothing wired; no fit. Bean qou-q9ih (route D1-b).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

# Minimal polynomials of the trace fields, read from the Magma fixtures the
# snappy wheel ships (the same source the companion probe parses for orbit
# degrees). Kept as exact rational expressions — never floats.
TRACE_FIELD_POLY = {
    "4_1":    "x**2 - x + 1",
    "5_2":    "x**3 + 2*x**2 + 3*x + 1",
    "m135":   "x**8 + 4*x**6 + 22*x**4 + 4*x**2 + 1",
    "s000":   "x**6 - 4*x**5 + 2*x**4 + 6*x**3 - 3*x**2 - x + 2",
    "t00000": "x**8 - 4*x**7 - 2*x**6 + 14*x**5 + 14*x**4 - 7*x**3 "
              "- 13*x**2 - x + 5",
    "v0000":  "x**8 - Rational(11,4)*x**6 + Rational(41,16)*x**4 "
              "- Rational(11,16)*x**2 + Rational(1,8)",
}

# C_irr from the companion probe, obtained by summing Galois-orbit degrees --
# a different route to the same number, which is what makes C2 a real check.
COMPANION_C_IRR = {"4_1": 2, "5_2": 3, "m135": 8,
                   "s000": 6, "t00000": 8, "v0000": 8}


def main() -> int:
    import sympy as sp
    from sympy import Rational  # noqa: F401  (used by eval of the polys)

    x = sp.Symbol("x")

    print("=" * 78)
    print(" D1-b arrow question — the bar grading of the node set")
    print("=" * 78)

    wb = WitnessBuilder("dt-d1b-trace-field-bar-grading",
                        engine="sympy-exact-sturm")
    wb.set_description(
        "qou-q9ih D1-b, arrow question. The companion probe closed the NODE "
        "count as arithmetic (single Galois orbit, C_irr = [trace field : Q]). "
        "Arrows in a bar-graded quiver need the bar grading of the node set, "
        "and the single-orbit result says where to read it: nodes are the "
        "embeddings of the trace field, complex conjugation acts on them, and "
        "a rep is self-conjugate exactly when its embedding is real. So the "
        "grading is r_1 mirror-FIXED nodes plus r_2 swapped pairs. Measured "
        "exactly by Sturm sequences: five of six trace fields are TOTALLY "
        "IMAGINARY; 5_2 is the only one with a real embedding and cannot avoid "
        "one, because its trace field has ODD degree and no involution acts "
        "freely on an odd-size set. RECORDED NEGATIVE: I first read this as an "
        "escape from QuiverMirrorAutomorphismExcluded -- that the theorem "
        "excludes a freely-acting mirror and a fixed point evades it. Reading "
        "the theorem shows that is WRONG: its hypothesis is count-invariance "
        "(Omega(sigma e) = Omega e), which says nothing about freeness, so a "
        "fixed point is no escape. The parity fact stands; the consequence "
        "does not. What this gives is the measured (r_1, r_2) any bar-graded "
        "construction must reproduce -- an INPUT to the arrow question, not an "
        "answer. Scope-(a); four of six are census manifolds, valid for the "
        "grading and not automatically valid as D1-b nodes. Nothing wired; no "
        "fit; A_omega underived."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    checks: list[tuple[bool, str, str]] = []

    def check(ok, name, detail):
        checks.append((bool(ok), name, detail))
        print(f"  [{'PASS' if ok else 'FAIL':4s}] {name} — {detail}")

    # ---------------------------------------------------------------- C4
    print("\n[C4] control — the exact real-root routine separates known cases")
    probes = [("x**2 + 1", 0), ("x**2 - 1", 2), ("x**3 - 2", 1),
              ("x**4 - 1", 2)]
    got = [(s, int(sp.polys.polytools.count_roots(sp.Poly(sp.sympify(s), x))))
           for s, _ in probes]
    want = [(s, n) for s, n in probes]
    print(f"      {got}")
    check(got == want,
          "C4_the_exact_Sturm_real_root_count_DISCRIMINATES",
          f"hand-built cases {got} match the known answers; this is exact "
          "root COUNTING (Sturm sequences), not a numerical root-find, so no "
          "float64 enters and a borderline field cannot be miscounted")

    rows = {}
    print("\n  trace fields, exactly:")
    print("    manifold   deg   r_1   r_2   irreducible")
    for name, src in TRACE_FIELD_POLY.items():
        p = sp.Poly(sp.sympify(src, locals={"x": x, "Rational": sp.Rational}), x)
        deg = int(p.degree())
        r1 = int(sp.polys.polytools.count_roots(p))
        r2 = (deg - r1) // 2
        irr = bool(p.is_irreducible)
        rows[name] = {"poly": src, "degree": deg, "real_embeddings": r1,
                      "conjugate_pairs": r2, "irreducible": irr,
                      "totally_imaginary": r1 == 0,
                      "closes": r1 + 2 * r2 == deg,
                      "companion_C_irr": COMPANION_C_IRR[name]}
        print(f"    {name:8s} {deg:5d} {r1:5d} {r2:5d}   {irr}")

    check(all(v["closes"] for v in rows.values()),
          "C1_the_embedding_count_CLOSES",
          "r_1 + 2*r_2 = deg for every field — a real embedding plus a "
          "conjugate pair account for every embedding, with none left over")
    check(all(v["degree"] == v["companion_C_irr"] for v in rows.values()),
          "C2_the_degree_REPRODUCES_the_companion_probe_s_C_irr",
          "the companion probe got C_irr by summing Galois-ORBIT degrees off "
          "the Magma fixtures; this reads the minimal polynomial's DEGREE. Two "
          "routes, same six numbers — so neither is a parsing artifact")
    check(all(v["irreducible"] for v in rows.values()),
          "C3_every_minimal_polynomial_is_IRREDUCIBLE_over_Q",
          "otherwise 'the trace field' is not a field and counting its "
          "embeddings would be meaningless")

    # ------------------------------------------------------------- results
    imag = sorted(k for k, v in rows.items() if v["totally_imaginary"])
    real = sorted(k for k, v in rows.items() if not v["totally_imaginary"])
    check(len(imag) == 5 and real == ["5_2"],
          "FIVE_of_six_trace_fields_are_TOTALLY_IMAGINARY",
          f"totally imaginary {imag}; the only field with a real embedding is "
          f"{real}. So on this sample the mirror acts FREELY on the node set "
          "almost everywhere, and 5_2 is the exception")

    odd = sorted(k for k, v in rows.items() if v["degree"] % 2 == 1)
    check(odd == ["5_2"] and rows["5_2"]["real_embeddings"] >= 1,
          "5_2_s_fixed_node_is_FORCED_BY_PARITY_not_a_coincidence",
          "5_2 is the only odd-degree field (3), and no involution acts freely "
          "on a set of odd size — so a mirror-fixed node is unavoidable there, "
          "while 4_1's two nodes can be freely swapped. This is parity, not a "
          "property of the particular polynomial")

    check(True,
          "RECORDED_NEGATIVE_this_is_NOT_an_escape_from_the_mirror_exclusion",
          "I first read the fixed point as evading "
          "QuiverMirrorAutomorphismExcluded, on the theory that it excludes a "
          "FREELY acting mirror. Reading the theorem first: its hypothesis is "
          "hσ : ∀ e, Ω (σ e) = Ω e — count-invariance, which says nothing "
          "about freeness. A σ with fixed points can satisfy it and is "
          "excluded identically. The parity fact survives; the consequence I "
          "nearly drew from it does not")

    check(True, "WHAT_THIS_IS_an_INPUT_to_the_arrow_question",
          "the measured (r_1, r_2) is the bar grading any bar-graded quiver on "
          "these nodes must reproduce. It does not produce arrows, a "
          "potential, or A_omega, and no construction is proposed here")

    wb.add_data("trace_fields", rows)
    wb.add_data("bar_grading", {
        k: {"fixed_nodes": v["real_embeddings"],
            "swapped_pairs": v["conjugate_pairs"], "nodes": v["degree"]}
        for k, v in rows.items()})
    wb.add_data("recorded_negative", {
        "claim_i_nearly_made": "a mirror with a fixed point escapes "
                               "QuiverMirrorAutomorphismExcluded because that "
                               "theorem excludes a freely-acting mirror",
        "why_it_is_wrong": "the theorem's hypothesis is count-invariance "
                           "(hσ : ∀ e, Ω (σ e) = Ω e), not freeness; a σ with "
                           "fixed points satisfies it just as well and is "
                           "excluded on the same terms",
        "how_it_was_caught": "read the Lean statement before writing the claim",
    })
    wb.add_data("scope", {
        "tier": "scope-(a)",
        "arithmetic": "exact — Sturm real-root COUNTING on rational minimal "
                      "polynomials; no root-finding, no floats anywhere",
        "census_caveat": "m135/s000/t00000/v0000 are census manifolds, not "
                         "knots in S^3 — valid for reading the grading, not "
                         "automatically valid as D1-b nodes",
        "sample": "the ptolemy DB is firewalled, so six is the offline maximum",
        "derives_arrows": False, "derives_A_omega": False,
        "wired": False, "fit": False,
    })

    for ok, name, detail in checks:
        wb.add_assertion(name, computed="PASS" if ok else "FAIL",
                         expected="PASS", tolerance="exact", source=detail)
    wb.save()

    n_ok = sum(1 for ok, _, _ in checks if ok)
    print(f"\n  {n_ok}/{len(checks)} checks passed")
    return 0 if n_ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
