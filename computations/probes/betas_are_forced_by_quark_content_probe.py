#!/usr/bin/env python3
"""The `beta` values ARE forced by the quark content — which closes the last
dial, and points at the term the binding LP was missing all along.

THE QUESTION
------------
`nucleon_chain_sets_the_transition_probe.py` reduced binding to two transition
points and showed they are set by the crossing-branch content `beta` of a
three-letter middle: proton `(0, 1/2, 1/2)`, neutron `(1/2, 1/2, 1)`. Owner:
*"they should hopefully be forced by the quark content."*

**They are.** Not approximately, not by convention — by a rule already in
`pyhecke.atom.nucleon_gen_chains`, which takes the quark list as its argument.

THE RULE
--------
Three quark pairs, assigned to generators, each crossing typed by the flavour
pair it joins:

    pairs      (0,1) -> gen 0     (0,2) -> gen 0     (1,2) -> gen 1

    flavours   u u  ->  sigma      (beta = 0)
               d d  ->  sigma^-1   (beta = 1)
               u d  ->  average    (beta = 1/2)

Work it through:

    proton  = u u d :  (u,u) -> 0 ,  (u,d) -> 1/2 ,  (u,d) -> 1/2   =  (0, 1/2, 1/2)
    neutron = u d d :  (u,d) -> 1/2,  (u,d) -> 1/2 ,  (d,d) -> 1    =  (1/2, 1/2, 1)

which is exactly what the previous probe measured, confirmed here by calling
`nucleon_gen_chains` and reading the `beta` back out of its `(c, d)` tuples.
**Given the rule and the quark content there is zero freedom in the six
numbers.** Nothing was fitted; there is no dial.

THE SAME MAP ONE LEVEL UP — WITH ONE DOCUMENTED DIFFERENCE
-------------------------------------------------------------
`atom_gen_chains` types the *inter-nucleon* crossings by the same scheme, and
the like-flavour cases are exact at both scales:

    quark     u u -> 0                d d -> 1
    nucleon   p p -> 0                n n -> 1

The unlike-flavour case is where the two scales part company:

    quark     u d -> 1/2 exactly                 (colour-BLIND, `-h/2`)
    nucleon   p n -> 0.49965607229824338         (colour-WEIGHTED, `D_PN`)

`D_PN = pn_interface_offset(q0)` under `PN_CONVENTION = bring_color_weighted`,
canonical by the owner ruling of 2026-08-15 (R3), reaffirmed 2026-08-26 — a
shift of `-3.44e-4` off the midpoint. And `atom.py` says of the quark-level
crossings, in as many words: *"nothing here establishes what convention a u-d
crossing should carry."*

That matters, because `b_2` — the parameter the previous probe found dominates
the transition — **is** a u-d crossing. So the question is live by the corpus's
own account. Tested: switching the quark `ud` crossings to the colour-weighted
value moves the proton transition by `-1.30e-4` and the neutron by `+5.63e-5`.
Against the `0.27` that would be needed to reach `q_0`, that is nothing. **The
conclusion is robust to the one convention the corpus leaves open.**

THE ONLY RESIDUAL FREEDOM, AND IT DOES NOT HELP
--------------------------------------------------
The quark *ordering* inside the list is not fixed by "uud": it decides which
pair lands on generator 1. Since `b_0` and `b_1` both multiply `sigma_0` and
commute, six orderings collapse to four classes:

    proton   uud, udu   (uu on gen 0)   b = (0, 1/2, 1/2)   h* = 0.477184637  [CORPUS]
    proton   duu        (uu on gen 1)   b = (1/2, 1/2, 0)   h* = NONE — never switches
    neutron  udd        (dd on gen 1)   b = (1/2, 1/2, 1)   h* = 0.569840291  [CORPUS]
    neutron  dud, ddu   (dd on gen 0)   b = (1, 1/2, 1/2)   h* = 0.433865897

and **no pairing straddles `q_0`**. Every window that exists lies inside
`[0.4339, 0.5698]`; `h(q_0) = 0.20906` is below all of them, and two of the four
pairings have no window at all. So the last thing that looked like a free
parameter is not free, and even its residual labelling freedom cannot move
binding onto the substrate point.

The corpus's own choice is a uniform convention — u's first, then d's — which
happens to put the proton's like-pair `uu` on generator 0 and the neutron's
like-pair `dd` on generator 1. Asymmetric in effect, uniform in statement.

THE TERM THE LP WAS MISSING
------------------------------
That closes the `beta` route, and in doing so it makes a scope error visible.
`atom_gen_chains(Z, N)` builds an atom out of three things:

  1. per-nucleon crossings (what `v_p`, `v_n` carry),
  2. **`C(A,2)` inter-nucleon crossings** — one per nucleon *pair*, typed
     pp/nn/pn by the map above,
  3. `Z` electron crossings on generator 1.

Measured here: for `2H`, `3H`, `4He` the atom's generator-0 chain carries **1, 3
and 6** crossings more than the sum of its nucleons', exactly `C(A,2)`; plus 1,
1 and 2 extra on generator 1.

**The aggregation LP of `nfold_ip_coupling_duality_gap_probe.py` used only `v_p`
and `v_n`. It had no inter-nucleon term at all.** Every zero reported in that
probe and the two after it is a zero for a construction with the bonds left
out — and the bonds are, on their face, the part that binds. That is where the
next work goes, and it is a much better-posed target than anything in the cost
functional or the crossing branches.

This does not retract the earlier results: the dual-vertex hysteresis, the
rank-one dual and the transitions are all correct statements about the
per-nucleon LP that was built. It bounds what they were ever evidence about.

DISCIPLINE
----------
No fit; no `B_AME`; nothing wired. The `beta` values are read back out of the
corpus's own `nucleon_gen_chains` rather than asserted. Transition values are
recomputed here and agree with the previous probe to `1e-9`.

-- Ref: [manuscript] bean t7qv
-- Ref: [code] pyhecke.atom.nucleon_gen_chains, atom_gen_chains
-- Ref: [probe] nucleon_chain_sets_the_transition_probe.py
-- Ref: [probe] nfold_ip_coupling_duality_gap_probe.py (the LP missing the bonds)
"""
from __future__ import annotations

import sys
import warnings
from itertools import permutations
from pathlib import Path

warnings.filterwarnings("ignore")

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
ROOT = COMP.parent
sys.path.insert(0, str(ROOT / "tools" / "pyhecke" / "python"))
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402

from pyhecke.atom import atom_gen_chains, nucleon_gen_chains  # noqa: E402
from pyhecke.constants import PN_CONVENTION  # noqa: E402
from pyhecke.gram import _hm_mp, gram_matrix_mp  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

mp.mp.dps = 25
_QH = mp.mpf(str(Q0))
H_Q0 = float(_QH - 1 / _QH)
PREV_P, PREV_N = 0.477184636796, 0.569840290998

_CACHE: dict = {}


def base(hv: float):
    key = round(hv, 13)
    if key in _CACHE:
        return _CACHE[key]
    q = mp.mpf(hv) / 2 + mp.sqrt(mp.mpf(hv) ** 2 + 4) / 2
    h = q - 1 / q
    z = q ** 3 / (q ** 2 + 1)
    gram = np.array([[float(x) for x in row] for row in gram_matrix_mp(30, q=q)])
    cost = np.array([float(x) for x in
                     [mp.mpf(1), z, z, z ** 2, z ** 2, h * z ** 2 + z]])
    _CACHE[key] = (gram, cost, h, cost[2] / gram[2, 2])
    return _CACHE[key]


def chain(betas, h):
    nf = [mp.mpf(1)] + [mp.mpf(0)] * 5
    for _ in range(3):
        nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, h)
        nf = _hm_mp(nf, mp.mpf(1), -h, 1, h)
    for c, g in ((betas[0], 0), (betas[1], 0), (betas[2], 1)):
        nf = _hm_mp(nf, mp.mpf(1), -mp.mpf(c) * h, g, h)
    nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, h)
    nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, h)
    return np.array([float(x) for x in nf])


def margin(betas, hv: float) -> float:
    gram, _c, h, lam = base(hv)
    gv = gram @ chain(betas, h)
    return lam * gv[2] - gv[0]


SCAN = [0.02 * (1.055 ** i) for i in range(80)]
SCAN = [x for x in SCAN if x < 1.3]


def transition(betas):
    m = [margin(betas, hv) for hv in SCAN]
    br = [(SCAN[i], SCAN[i + 1]) for i in range(len(SCAN) - 1)
          if m[i] * m[i + 1] < 0]
    if not br:
        return None
    a, b = br[0]
    fa = margin(betas, a) > 0
    for _ in range(46):
        mm = 0.5 * (a + b)
        if (margin(betas, mm) > 0) == fa:
            a = mm
        else:
            b = mm
    return 0.5 * (a + b)


def betas_of(quarks):
    """Read `beta` back out of the corpus's own generated chain."""
    h = _QH - 1 / _QH
    g0, g1 = nucleon_gen_chains(list(quarks))
    mid = list(g0[3:-2]) + list(g1[3:])       # strip B_3 prefix, gluon suffix
    return tuple(round(float(-mp.mpf(d) / h), 10) for _c, d in mid)


def main() -> int:
    assertions = []
    print("t7qv — are the betas forced by the quark content?")

    # ── A1. derived, not chosen ───────────────────────────────────────
    print("\n  1. the betas come out of nucleon_gen_chains(quark list)")
    bp = betas_of(("u", "u", "d"))
    bn = betas_of(("u", "d", "d"))
    ok = bp == (0.0, 0.5, 0.5) and bn == (0.5, 0.5, 1.0)
    print(f"     nucleon_gen_chains(['u','u','d']) -> beta = {bp}")
    print(f"     nucleon_gen_chains(['u','d','d']) -> beta = {bn}")
    print(f"     measured in the previous probe:     (0.0, 0.5, 0.5) / "
          f"(0.5, 0.5, 1.0)")
    print(f"     rule: uu -> sigma (0), dd -> sigma^-1 (1), ud -> average (1/2)")
    print(f"           pairs (0,1),(0,2) -> gen 0 ; (1,2) -> gen 1")
    print(f"     => ZERO freedom in the six numbers given the quark content")
    assertions.append(("A1_betas_are_derived_from_quark_content", ok,
                       f"nucleon_gen_chains yields {bp} and {bn}, matching the "
                       f"measured values"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. the map at the nucleon scale — and where it differs ───────
    print("\n  2. the same map one level up, with ONE documented difference")
    h = _QH - 1 / _QH
    g0_pp, _ = atom_gen_chains(2, 0)
    g0_nn, _ = atom_gen_chains(0, 2)
    g0_pn, _ = atom_gen_chains(1, 1)
    per_p = len(nucleon_gen_chains(["u", "u", "d"])[0])
    per_n = len(nucleon_gen_chains(["u", "d", "d"])[0])
    b_pp = float(-mp.mpf(g0_pp[2 * per_p][1]) / h)
    b_nn = float(-mp.mpf(g0_nn[2 * per_n][1]) / h)
    b_pn = float(-mp.mpf(g0_pn[per_p + per_n][1]) / h)
    like_exact = abs(b_pp) < 1e-15 and abs(b_nn - 1) < 1e-15
    pn_shifted = abs(b_pn - 0.5) > 1e-6
    print(f"     like-flavour, EXACT at both scales:")
    print(f"        quark    uu -> 0      dd -> 1")
    print(f"        nucleon  pp -> {b_pp:.1f}      nn -> {b_nn:.1f}")
    print(f"     unlike-flavour, and here the scales DIFFER by convention:")
    print(f"        quark    ud -> 1/2 exactly          (colour-BLIND)")
    print(f"        nucleon  pn -> {b_pn:.17f}  (colour-WEIGHTED, D_PN)")
    print(f"        shift off 1/2 = {b_pn - 0.5:+.4e}")
    print(f"     PN_CONVENTION = {PN_CONVENTION}, canonical by owner ruling")
    print(f"     2026-08-15 (R3). atom.py says of the quark u-d crossings:")
    print(f"     \"nothing here establishes what convention a u-d crossing")
    print(f"     should carry\" — and beta_2 IS a u-d crossing, the one that")
    print(f"     dominates the transition. So test it:")
    shifts = {}
    for lbl, cb, wb_ in (("proton", (0.0, 0.5, 0.5), (0.0, b_pn, b_pn)),
                         ("neutron", (0.5, 0.5, 1.0), (b_pn, b_pn, 1.0))):
        a, bb = transition(cb), transition(wb_)
        shifts[lbl] = bb - a
        print(f"        {lbl:<8s} colour-blind {a:.9f} -> colour-weighted "
              f"{bb:.9f}   ({bb - a:+.2e})")
    tiny = all(abs(v) < 1e-3 for v in shifts.values())
    ok = like_exact and pn_shifted and tiny
    print(f"     the open convention moves the transitions by ~1e-4, against the")
    print(f"     0.27 needed to reach q_0 — so the conclusion is convention-robust")
    assertions.append(("A2_map_exact_for_like_flavours_pn_colour_weighted", ok,
                       f"pp={b_pp:.1f}, nn={b_nn:.1f} exact; pn={b_pn:.12f} "
                       f"differs from 1/2 by {b_pn - 0.5:.2e}; switching the "
                       f"quark ud crossings shifts transitions by "
                       f"{ {k: f'{v:+.1e}' for k, v in shifts.items()} }"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. the residual freedom is the ordering; four classes ────────
    print("\n  3. residual freedom: quark ORDERING picks the gen-1 pair")
    classes = {}
    for base_q, lbl in ((("u", "u", "d"), "proton"), (("u", "d", "d"), "neutron")):
        for perm in sorted(set(permutations(base_q))):
            classes.setdefault(lbl, {}).setdefault(betas_of(perm), []).append(
                "".join(perm))
    ok = True
    trans = {}
    for lbl in ("proton", "neutron"):
        for b, orders in sorted(classes[lbl].items()):
            tr = transition(b)
            trans[(lbl, b)] = tr
            print(f"     {lbl:<8s} {'/'.join(orders):<9s} beta {str(b):<18s} "
                  f"h* = "
                  f"{'NONE — never switches' if tr is None else f'{tr:.9f}'}")
    # b0 <-> b1 symmetry means 3 orderings give 2 distinct classes each
    ok = all(len(classes[l]) == 3 for l in ("proton", "neutron"))
    print(f"     (b_0 and b_1 commute, so (0,1/2,1/2) ~ (1/2,0,1/2) etc.)")
    assertions.append(("A3_ordering_gives_a_small_finite_set", ok,
                       f"3 orderings each; transitions "
                       f"{ {k[1]: v for k, v in trans.items()} }"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4. no ordering straddles q_0 ─────────────────────────────────
    print("\n  4. no proton/neutron pairing straddles q_0")
    p_bs = [b for b in classes["proton"]]
    n_bs = [b for b in classes["neutron"]]
    straddles, windows = 0, []
    for pb in p_bs:
        for nb in n_bs:
            a, b = trans[("proton", pb)], trans[("neutron", nb)]
            if a is None or b is None:
                print(f"     p{pb} x n{nb}: one never switches — no window")
                continue
            lo, hi = min(a, b), max(a, b)
            windows.append((lo, hi))
            hit = lo < H_Q0 < hi
            straddles += hit
            print(f"     p{str(pb):<18s} x n{str(nb):<18s} window "
                  f"({lo:.6f}, {hi:.6f})  contains q_0? {hit}")
    lo_all = min(w[0] for w in windows)
    hi_all = max(w[1] for w in windows)
    ok = straddles == 0 and H_Q0 < lo_all
    print(f"     every window lies in [{lo_all:.4f}, {hi_all:.4f}]; "
          f"h(q_0) = {H_Q0:.6f} is below all of them")
    print(f"     => the last apparent dial is closed")
    assertions.append(("A4_no_ordering_straddles_q0", ok,
                       f"{straddles} of {len(windows)} windows contain h(q_0); "
                       f"all lie in [{lo_all:.4f}, {hi_all:.4f}]"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. the inter-nucleon term the LP omitted ─────────────────────
    print("\n  5. the atom carries C(A,2) inter-nucleon crossings — the LP had none")
    extras = {}
    for lbl, Z, N in (("2H", 1, 1), ("3H", 1, 2), ("4He", 2, 2)):
        g0, g1 = atom_gen_chains(Z, N)
        per0 = Z * per_p + N * per_n
        per1 = (Z * len(nucleon_gen_chains(["u", "u", "d"])[1])
                + N * len(nucleon_gen_chains(["u", "d", "d"])[1]))
        A = Z + N
        extras[lbl] = (len(g0) - per0, len(g1) - per1, A * (A - 1) // 2)
        print(f"     {lbl:<4s} gen0: atom {len(g0):3d} vs nucleons {per0:3d} "
              f"-> {len(g0) - per0:2d} extra   (C(A,2) = "
              f"{A * (A - 1) // 2})")
        print(f"          gen1: atom {len(g1):3d} vs nucleons {per1:3d} "
              f"-> {len(g1) - per1:2d} extra   (Z = {Z} electrons)")
    ok = all(e[0] == e[2] for e in extras.values())
    print(f"     the gen-0 extras are exactly the pp/nn/pn bonds, one per pair")
    print(f"     nfold_ip_coupling_duality_gap_probe used only v_p and v_n:")
    print(f"     NO inter-nucleon term. Every zero it reported is a zero for a")
    print(f"     construction with the bonds left out.")
    assertions.append(("A5_atom_has_bonds_the_lp_omitted", ok,
                       f"extra gen-0 crossings {[e[0] for e in extras.values()]}"
                       f" = C(A,2) {[e[2] for e in extras.values()]}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. transitions reproduce the previous probe ──────────────────
    print("\n  6. the derived betas reproduce the previous probe's transitions")
    tp = trans[("proton", (0.0, 0.5, 0.5))]
    tn = trans[("neutron", (0.5, 0.5, 1.0))]
    ep, en = abs(tp - PREV_P), abs(tn - PREV_N)
    ok = ep < 1e-9 and en < 1e-9
    print(f"     proton  {tp:.12f}  vs  {PREV_P:.12f}   d = {ep:.1e}")
    print(f"     neutron {tn:.12f}  vs  {PREV_N:.12f}   d = {en:.1e}")
    print(f"     so the whole chain — quark content -> beta -> transition ->")
    print(f"     binding window — closes without a free parameter anywhere")
    assertions.append(("A6_reproduces_previous_transitions", ok,
                       f"proton d = {ep:.1e}, neutron d = {en:.1e}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  Yes — forced. The betas are generated by a flavour-pair rule")
    print("  (uu -> sigma, dd -> sigma^-1, ud -> average) over the three quark")
    print("  pairs, so the proton's (0, 1/2, 1/2) and the neutron's")
    print("  (1/2, 1/2, 1) have zero freedom in them. The same map types the")
    print("  inter-nucleon crossings, exactly for pp/nn and colour-weighted for")
    print("  pn. The only residual")
    print("  freedom is the quark ordering, which gives four classes, and NO")
    print("  pairing straddles q_0 — every window sits in [0.434, 0.570] while")
    print("  h(q_0) = 0.209. Nothing was fitted, and there is no dial left.")
    print("  Which makes the real finding a scope error: the atom construction")
    print("  carries C(A,2) inter-nucleon bonds and Z electron crossings that")
    print("  the aggregation LP never included. Every binding zero measured so")
    print("  far is a zero for a nucleus with its bonds left out.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
        wb.set_description(
            "Answers whether the crossing-branch parameters beta are forced by "
            "the quark content: they are. pyhecke.atom.nucleon_gen_chains "
            "types each of the three quark-pair crossings by flavour — "
            "uu -> sigma (beta 0), dd -> sigma^-1 (beta 1), ud -> average "
            "(beta 1/2) — with pairs (0,1),(0,2) on generator 0 and (1,2) on "
            "generator 1, yielding proton (0,1/2,1/2) and neutron (1/2,1/2,1) "
            "with zero freedom. The same template map types the inter-nucleon "
            "crossings (pp -> 0, nn -> 1, pn -> 1/2), so one rule applies at "
            "two scales. The only residual freedom is the quark ordering, "
            "which picks which pair sits on generator 1; it gives four classes "
            "with transitions 0.477184637, NONE, 0.569840291 and 0.433865897, "
            "and NO proton/neutron pairing straddles q_0 — every window lies "
            "in [0.4339, 0.5698] while h(q_0) = 0.20906. The last apparent "
            "dial is therefore closed. The substantive finding is a scope "
            "error it exposes: atom_gen_chains carries C(A,2) inter-nucleon "
            "crossings (1, 3, 6 extra on generator 0 for 2H, 3H, 4He) plus Z "
            "electron crossings, and the aggregation LP of "
            "nfold_ip_coupling_duality_gap_probe used only v_p and v_n, with "
            "no inter-nucleon term at all.")
        wb.add_data("rule", {"uu": "sigma (beta 0)", "dd": "sigma^-1 (beta 1)",
                             "ud": "average (beta 1/2)",
                             "pairs": "(0,1)->gen0, (0,2)->gen0, (1,2)->gen1"})
        wb.add_data("derived_betas", {"proton": ["0", "1/2", "1/2"],
                                      "neutron": ["1/2", "1/2", "1"]})
        wb.add_data("inter_nucleon_betas", {"pp": "0", "nn": "1", "pn": "1/2"})
        wb.add_data("ordering_classes",
                    {f"{lbl}:{b}": ("NONE" if trans[(lbl, b)] is None
                                    else f"{trans[(lbl, b)]:.9f}")
                     for lbl in ("proton", "neutron") for b in classes[lbl]})
        wb.add_data("window_span", {"lo": f"{lo_all:.6f}", "hi": f"{hi_all:.6f}"})
        wb.add_data("h_q0", f"{H_Q0:.12f}")
        wb.add_data("atom_extra_crossings",
                    {k: {"gen0": v[0], "gen1": v[1], "C(A,2)": v[2]}
                     for k, v in extras.items()})
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "SCOPE BOUND ON THE EARLIER BINDING RESULTS, not a retraction. The "
            "dual-vertex hysteresis, the rank-one dual and the two transition "
            "points are correct statements about the per-nucleon LP that was "
            "actually built. What A5 establishes is that this LP omits the "
            "C(A,2) inter-nucleon bonds and the Z electron crossings the "
            "corpus's own atom_gen_chains includes, so 'binding is zero at "
            "q_0' has only ever been demonstrated for a nucleus with its bonds "
            "left out.")
        wb.add_caveat(
            "The flavour rule itself is a convention in one respect: it fixes "
            "u <-> forward and d <-> inverse rather than the reverse. Swapping "
            "that orientation maps proton (0,1/2,1/2) -> (1,1/2,1/2) and "
            "neutron (1/2,1/2,1) -> (1/2,1/2,0), i.e. exactly onto the two "
            "alternative ordering classes already enumerated in A3/A4 — so the "
            "swap changes no conclusion here: those classes are covered and "
            "none of them straddles q_0 either.")
        wb.add_caveat(
            "A container reset mid-investigation dropped this session onto a "
            "different branch (claude/omegaorder-exponent-group), whose pyhecke "
            "gives a different transition for the same betas (0.679 rather "
            "than 0.477). Everything reported here is computed on "
            "claude/mt7r-archimedean-eval-2026-08-24, and A6 re-verifies the "
            "previous probe's two transition values to 1e-9 as a guard.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
