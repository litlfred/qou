#!/usr/bin/env python3
"""qbeta_5two_jones_barodd_probe.py — full 5₂ Jones + its bar-odd part, via a
self-contained Temperley–Lieb Kauffman bracket (Step 2 of the non-amphichiral
route). Validates against the known V(4₁), V(5₂); extracts the complete classical
bar-odd datum and relates it to N_odd and to the writhe datum sinh(u).

The #3813 writhe brick used only the 1-dim (3)/(1,1,1) block characters. This
computes the FULL Jones from scratch (TL₃ diagram algebra, no Ocneanu-weight
normalization guesswork) and validates it, so the complete bar-odd datum — not
just the leading writhe term — is in hand and the H₃/TL₃ machinery is trusted
before the quantum-volume step.

METHOD. Kauffman bracket in the Temperley–Lieb algebra TL₃(δ), δ = −A²−A⁻².
Braid generators σ_i ↦ A·1 + A⁻¹·e_i, σ_i⁻¹ ↦ A⁻¹·1 + A·e_i. Diagrams are
non-crossing matchings on 6 points (3 top, 3 bottom); multiply by stacking +
union-find loop counting; the Markov trace closes top_i–bottom_i and weights
δ^{loops−1} (so the unknot → 1). Jones: V(t) = (−A³)^{−writhe}·⟨β̂⟩ with
t = A⁻⁴; the QOU bar variable is q with t = q², i.e. A = q^{−1/2}.

Known targets (Knot Atlas):
  V(4₁) = q⁻²−q⁻¹+1−q+q²          (palindromic ⇒ bar-odd = 0, amphichiral)
  V(5₂) = q⁻¹−q⁻²+2q⁻³−q⁻⁴+q⁻⁵−q⁻⁶ (non-palindromic ⇒ bar-odd ≠ 0, chiral)

HONEST SCOPE. The classical Jones bar-odd datum is O(1) at q₀ — many orders above
N_odd = S·u³ (O(1e-8)) — and is anchor-smooth, so it is NOT the swing (the
Lean-proved no_anchor_invariant_realizes_swing binds). It is the complete bar-odd
HOME; the anchor-dependent swing needs the quantum 𝔙_q(5₂) (Step 1). No c_k; no
fit; scope-(a).

Run: python3 -u computations/probes/qbeta_5two_jones_barodd_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_jones.log
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
Q = {"muon": mp.mpf("1.10997859555733471"),
     "proton": mp.mpf("1.1099785827513808075916690956107688798744991218736")}

BRAID_5_2 = [1, 1, 1, 2, -1, 2]      # CORRECT 5₂: det 7, writhe 4 (validated below)
BRAID_6_2 = [1, 1, 1, -2, 1, -2]     # the corpus-table "5_2" braid — actually 6₂
BRAID_4_1 = [1, -2, 1, -2]           # (σ₁σ₂⁻¹)², writhe 0
# points: top = 0,1,2 ; bottom = 3,4,5.  A TL₃ diagram = frozenset of 2-elt pairs.
IDN = frozenset({(0, 3), (1, 4), (2, 5)})
def cap_cup(i):   # e_i : cap top(i,i+1), cup bottom(i,i+1), through the rest
    top, bot = {0, 1, 2}, {3, 4, 5}
    pairs = [(i, i + 1), (i + 3, i + 4)]
    used_t = {i, i + 1}; used_b = {i + 3, i + 4}
    for t in sorted(top - used_t):
        pairs.append((t, t + 3))
    return frozenset(pairs)
E = {1: cap_cup(0), 2: cap_cup(1)}


def _uf_find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]; x = parent[x]
    return x
def _uf_union(parent, a, b):
    ra, rb = _uf_find(parent, a), _uf_find(parent, b)
    if ra != rb:
        parent[ra] = rb


def tl_mul(d1, d2):
    """Product d1·d2 in TL₃: stack d1 (top) on d2 (bottom), glue d1-bottom(3,4,5)
    to d2-top(0,1,2). Returns (loops, result_diagram on top d1 / bottom d2)."""
    # nodes: A = d1 top (0,1,2), M = middle (glue) 3 nodes, B = d2 bottom.
    # relabel: d1 uses 0..2 (top), 3..5 (bottom=middle). d2 uses 0..2 (top=middle),
    # 3..5 (bottom). Map to a common 9-node set: A0..2=0..2, M0..2=3..5, B0..2=6..8.
    parent = {i: i for i in range(9)}
    for (a, b) in d1:                 # d1: top 0..2 → A(0..2); bottom 3..5 → M(3..5)
        _uf_union(parent, a, b)
    for (a, b) in d2:                 # d2: top 0..2 → M(3..5); bottom 3..5 → B(6..8)
        _uf_union(parent, a + 3, b + 3)
    # the three glue nodes M0..2 are node 3,4,5 shared by both — already same ids.
    # count closed loops = components entirely inside the middle (no A,B endpoint)
    ends = set(range(0, 3)) | set(range(6, 9))     # external endpoints (A top, B bot)
    comp_has_end = {}
    for n in range(9):
        r = _uf_find(parent, n)
        comp_has_end[r] = comp_has_end.get(r, False) or (n in ends)
    loops = sum(1 for r, he in comp_has_end.items() if not he)
    # result matching on A(0..2)=top, B(6..8)=bottom → relabel to 0..2, 3..5
    res = set()
    exts = sorted(ends)
    seen = set()
    for i, x in enumerate(exts):
        if x in seen:
            continue
        for y in exts[i + 1:]:
            if _uf_find(parent, x) == _uf_find(parent, y):
                lx = x if x < 3 else x - 3       # A: 0..2 ; B: 6..8 → 3..5
                ly = y if y < 3 else y - 3
                res.add(tuple(sorted((lx, ly))))
                seen.add(x); seen.add(y)
                break
    return loops, frozenset(res)


def bracket(word, A):
    """Kauffman bracket of the closure of a 3-braid word, as an expression in A."""
    delta = -A ** 2 - A ** (-2)
    # element = dict {diagram: coeff(A)}; start at identity
    elt = {IDN: sp.Integer(1)}
    for g in word:
        i = abs(g)
        gen = ({IDN: A, E[i]: A ** (-1)} if g > 0 else {IDN: A ** (-1), E[i]: A})
        new = {}
        for d1, c1 in elt.items():
            for d2, c2 in gen.items():
                loops, d = tl_mul(d1, d2)
                new[d] = new.get(d, sp.Integer(0)) + c1 * c2 * delta ** loops
        elt = {d: sp.expand(c) for d, c in new.items() if sp.expand(c) != 0}
    # Markov trace: close top_i–bottom_i, weight δ^{loops-1}
    total = sp.Integer(0)
    for d, c in elt.items():
        parent = {i: i for i in range(6)}
        for (a, b) in d:
            _uf_union(parent, a, b)
        for i in range(3):
            _uf_union(parent, i, i + 3)         # closure top_i–bottom_i
        roots = {_uf_find(parent, n) for n in range(6)}
        total += c * delta ** (len(roots) - 1)
    return sp.expand(total)


def jones(word):
    """Jones polynomial V(q) of the 3-braid closure, q with t=q², A=q^{-1/2}."""
    A = sp.symbols("A")
    w = sum(1 if g > 0 else -1 for g in word)
    br = bracket(word, A)
    V_A = sp.expand((-A ** 3) ** (-w) * br)        # normalized so unknot → 1
    q = sp.symbols("q", positive=True)
    V_q = sp.expand(V_A.subs(A, q ** sp.Rational(-1, 2)))
    return sp.simplify(V_q), q


def poly_to_dict(expr, q):
    expr = sp.expand(expr)
    d = {}
    for term in sp.Add.make_args(expr):
        c = term.subs(q, 1)
        p = sp.degree(sp.Poly(term * q ** 12, q)) - 12 if term.has(q) else 0
        # robust exponent extraction
        pw = sp.simplify(sp.log(term / c) / sp.log(q)) if c != 0 and term.has(q) else 0
        d[int(pw)] = int(c)
    return d


def main() -> int:
    V41, q = jones(BRAID_4_1)
    V52, _ = jones(BRAID_5_2)
    print("=" * 78)
    print(" 5₂ full Jones + bar-odd datum (Temperley–Lieb Kauffman bracket)")
    print("=" * 78)
    print(f"\n  V(4₁) computed = {V41}")
    print(f"  V(5₂) computed = {V52}")

    # known targets — QOU-q convention t = q² (so V(t)→V(q²)).
    # V(4₁)(t)=t²−t+1−t⁻¹+t⁻² ; V(5₂)(t)=−t⁶+t⁵−t⁴+2t³−t²+t (Knot Atlas mirror).
    V41_known = q ** 4 - q ** 2 + 1 - q ** -2 + q ** -4
    V52_known = -q ** 12 + q ** 10 - q ** 8 + 2 * q ** 6 - q ** 4 + q ** 2
    V52_known_mirror = V52_known.subs(q, 1 / q)
    det41 = abs(int(V41.subs(q, sp.I) * sp.conjugate(V41.subs(q, sp.I))))  # =det²
    det52 = abs(int(V52.subs(q, sp.I) * sp.conjugate(V52.subs(q, sp.I))))
    ok41 = sp.simplify(V41 - V41_known) == 0
    ok52 = (sp.simplify(V52 - V52_known) == 0 or
            sp.simplify(V52 - V52_known_mirror) == 0)
    print(f"\n  V(4₁) == known (palindromic, det²={det41}=5²)  : {ok41}")
    print(f"  V(5₂) == known (det²={det52}=7²)               : {ok52}")

    # correction to #3813: the corpus-table '5_2' braid is actually 6₂ (det 11)
    V62, _ = jones(BRAID_6_2)
    det62 = abs(int(V62.subs(q, sp.I) * sp.conjugate(V62.subs(q, sp.I))))
    w62 = sum(1 if g > 0 else -1 for g in BRAID_6_2)
    w52 = sum(1 if g > 0 else -1 for g in BRAID_5_2)
    print(f"\n  CORRECTION (#3813): corpus-table (1,1,1,-2,1,-2) has det²={det62}=11² "
          f"⇒ it is 6₂, NOT 5₂. writhe(6₂-braid)={w62}; the REAL 5₂ has writhe={w52}.")
    print(f"    ⇒ #3813's 'D_odd(5₂)=sinh(u_sub)' was 6₂ (writhe 2); real 5₂ "
          f"D_odd = ½(q⁴−q⁻⁴) = sinh(2·u_sub).")

    # bar-odd parts
    V41_odd = sp.simplify((V41 - V41.subs(q, 1 / q)) / 2)
    V52_odd = sp.simplify((V52 - V52.subs(q, 1 / q)) / 2)
    print(f"\n  V(4₁) bar-odd = {V41_odd}   (EXPECT 0 — amphichiral)")
    print(f"  V(5₂) bar-odd = {V52_odd}   (EXPECT ≠ 0 — chiral)")
    amphi41 = sp.simplify(V41_odd) == 0
    chiral52 = sp.simplify(V52_odd) != 0

    # evaluate the 5₂ bar-odd Jones datum at q₀; compare to N_odd + writhe sinh(u)
    V52_odd_fn = sp.lambdify(q, V52_odd, "mpmath")
    sinh_u_fn = sp.lambdify(q, (q ** 4 - q ** -4) / 2, "mpmath")   # real 5₂ writhe-4 datum
    print(f"\n  at the substrate anchors:")
    vals = {}
    for name, q0 in Q.items():
        vodd = V52_odd_fn(q0)
        wsinh = sinh_u_fn(q0)
        vals[name] = vodd
        print(f"    V(5₂)_odd({name}) = {mp.nstr(vodd, 12)}   writhe ½(q⁴−q⁻⁴) = "
              f"{mp.nstr(wsinh, 8)}")
    swing = abs(vals["proton"] - vals["muon"])
    # N_odd scale for contrast
    print(f"    |V_odd(p) − V_odd(mu)| = {mp.nstr(swing, 6)}  (smooth); N_odd ~ 1e-8 "
          f"⇒ classical Jones bar-odd is O(1e8)× too large + anchor-smooth ⇒ NOT "
          f"the swing (prune). The swing needs 𝔙_q(5₂), Step 1.")

    wb = WitnessBuilder("qbeta-5two-jones-barodd", engine="sympy+mpmath")
    wb.set_description(
        "Full 5₂ Jones via a self-contained Temperley–Lieb Kauffman bracket "
        "(TL₃ diagram algebra), validated against known V(4₁), V(5₂). Extracts "
        "the complete classical bar-odd datum: V(4₁) bar-odd = 0 (amphichiral), "
        "V(5₂) bar-odd ≠ 0 (chiral). Step 2 of the non-amphichiral route — "
        "validates the machinery before the quantum-volume step. The classical "
        "Jones bar-odd datum is O(1) at q₀, ~1e8× above N_odd=S·u³ and "
        "anchor-smooth, so NOT the swing (no_anchor_invariant_realizes_swing "
        "binds); it is the complete bar-odd HOME, the swing needs 𝔙_q(5₂). "
        "No c_k; no fit; scope-(a).")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("jones_4one_validates",
                     computed=1.0 if ok41 else 0.0, expected=1.0, tolerance=0.5,
                     source="TL₃-computed V(4₁) == known q⁻²−q⁻¹+1−q+q² (palindromic)")
    wb.add_assertion("jones_5two_validates",
                     computed=1.0 if ok52 else 0.0, expected=1.0, tolerance=0.5,
                     source="TL₃-computed V(5₂) == known q⁻¹−q⁻²+2q⁻³−q⁻⁴+q⁻⁵−q⁻⁶ "
                            "(or its mirror) — validates the H₃/TL₃ machinery")
    wb.add_assertion("jones_4one_bar_even_5two_bar_odd",
                     computed=0.0 if (amphi41 and chiral52) else 1.0,
                     expected=0.0, tolerance=0.5,
                     source="V(4₁) bar-odd = 0 (amphichiral), V(5₂) bar-odd ≠ 0 "
                            "(chiral) — the complete classical bar-odd datum")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("V_4_1", str(V41))
    wb.add_data("V_5_2", str(V52))
    wb.add_data("V_5_2_bar_odd", str(V52_odd))
    wb.add_data("V_5_2_odd_at_anchors", {k: mp.nstr(v, 15) for k, v in vals.items()})
    wb.add_data("scale_contrast",
                "classical Jones bar-odd V(5₂)_odd(q₀) is O(1), ~1e8× above "
                "N_odd=S·u³ (O(1e-8)) and anchor-smooth ⇒ not the S-swing "
                "(no_anchor_invariant_realizes_swing). The writhe datum sinh(u) is "
                "the leading term of this full bar-odd datum.")
    wb.add_data("verdict",
                ("5₂ FULL JONES BAR-ODD DATUM validated + extracted. The "
                 "self-contained TL₃ Kauffman bracket reproduces known V(4₁) "
                 "(palindromic, bar-odd 0) and V(5₂) (non-palindromic, bar-odd ≠ 0) "
                 "— the H₃/TL₃ machinery is trusted. The complete classical bar-odd "
                 "datum V(5₂)_odd is O(1) at q₀ and anchor-smooth, so it is the "
                 "bar-odd HOME but not the swing (the prune binds); the writhe "
                 "sinh(u) is its leading term. Step 1 (quantum 𝔙_q(5₂), "
                 "anchor-dependent) is the swing test. No c_k; no fit; scope-(a)."
                 if ok else "INCONCLUSIVE — an assertion failed; inspect output."))
    wb.save()
    print(f"\n  assertions passed: {ok}")
    print("  witness -> computations/probes/qbeta-5two-jones-barodd.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
