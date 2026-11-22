#!/usr/bin/env python3
"""The many-body term exists, is located, and has the WRONG SIGN — so the bond
graph cannot reach `4He`, by a factor of 2.10 that `alpha` cannot touch.

TWO UPDATES — SEE `four_body_term_and_the_h12_collapse_probe.py`
----------------------------------------------------------------
1. **The ceiling below is no longer conditional.** Its one unmeasured input was
   the genuine four-body term at `A = 4`. `H_12` turned out to be reachable —
   convention D zeroes every partition with `>= 3` rows, leaving 7 blocks with
   largest dimension `297` — and the four-body term is **negative**, in all six
   nucleon orderings and all 80 random bond orders. `B(4He)` measures
   `10.387277 MeV`, so the shortfall is `3.4693x`, not the `2.0975x` bounded
   here. Worse, as predicted, and now unconditional.
2. **A3/A4 magnitudes here use a non-production bond order.** This probe appends
   all bonds after all nucleon words; `atom_gen_chains` interleaves them
   (`N0.N1.b01.N2.b02.b12...`). Bonds do not commute, and the difference is
   `11 %` at `A = 3` — the `ppn` triangle is `1.607030798` here and
   `1.503488161673` at production order, moving its three-body term from
   `-0.236512` to `-0.340055`. **Still negative, and larger**, so every
   conclusion below holds and strengthens; read the magnitudes at production
   order. A1-A2 (attachment rank), A5 (no-decay) and A6 (ceiling direction) do
   not depend on bond order at all.

PRECISION — SEE `the_binding_arc_was_measured_in_float64_probe.py`
-----------------------------------------------------------------
Everything below ran in float64, twice over: the seminormal matrices are
`numpy`/`scipy` `dtype=float`, and `q` came from `mp.mpf(str(Q0))` off a Python
float, so it carried 17 digits and no more. The agreements this docstring reads
as evidence — `5.6e-16`, `1.11e-15`, "agrees to `1e-15`", "exact to `1e-12`" —
sit at or just above the float64 floor, which is where float64 puts them whether
or not the identity holds. **Do not quote them as exactness.** The 200-bit
re-run confirms the underlying identities at `~1e-60`, and puts the honest error
on these magnitudes at `~1e-13`, set by the truncated `q` rather than by the
matrix arithmetic. Every sign and magnitude below is unaffected; the word
"exact" applied to them was not earned.

WHY THIS WAS THE NEXT MEASUREMENT
---------------------------------
The arc had established that binding is carried by inter-nucleon bonds, that the
*chain* transfer operator is rank one (so the chain telescopes exactly and needs
no `H_12`), and that a far bond's trace shows no distance decay. What was left
open is the only thing that could still close the `4He` gap: whether the
all-pairs topology carries **many-body content** the chain does not, and whether
that content has the sign `4He` needs.

It does carry it. It has the wrong sign.

WHERE THE MANY-BODY TERM LIVES
------------------------------
Attaching nucleon 3 to a prefix on nucleons 1-2, as a functional `P -> tr(P.A)`:

* **`k = 1` (chain), bonded to its neighbour only: exactly rank one.** Over 20
  random prefix words the ratio `tr(P.A)/tr(P)` is a single constant per bond
  type, to `< 1e-12`, and it reproduces the arc's recorded transfer scalar
  `F_pp = 0.385581983466` independently.
* **`k = 2` (all-pairs), bonded to both: NOT rank one.** The same ratio ranges
  over `0.196 .. 0.696` on the same prefixes.

The cause is mechanical. The 1-3 bond is the braid band generator
`(T5 T4 T3)(T2+d)(T3 T4 T5)^-1`, which routes strand 2 **through strands 3-5 —
the middle nucleon**. It therefore does not commute past the prefix, and that
failure to commute *is* the three-body term. Nothing else in the construction
produces one.

THIS DOES NOT CONTRADICT NO-DISTANCE-DECAY — IT EXPLAINS IT
-----------------------------------------------------------
`no_distance_decay_in_the_trace_probe` found a far bond's own trace identical to
an adjacent one across four routings (`5.6e-16`); reproduced here at `1.11e-15`
in the same breath as a triangle defect of `-0.236512`. Both are true and they
are the same fact seen twice: the bond's **own** invariant is routing-independent,
while its **commutator with what it passes through** is not. The first gives no
decay; the second gives sub-additivity. A one-parameter `r^(s-1)` falloff was
never the right shape for either.

*Compare like with like when checking this.* In ordering `ppn` the far bond spans
nucleons 1-3, which are `p` and `n`, so it must be compared against the adjacent
**p-n** bond at generator 5 — not the adjacent p-p bond at generator 2. Against
the wrong one it reads as a `0.187` discrepancy and looks like decay; against the
right one it agrees to `1e-15`. This probe's A5 caught exactly that mistake.

THE SIGN, MEASURED AT EVERY A=3 CONFIGURATION
---------------------------------------------
`L = log(tr_free / tr_atom)`, true `K_3` triangle against the naive sum of its
three bonds — all eight flavour orderings:

    order   true K3        naive sum      3-body          rel
    ppp     1.301140671    1.469698153    -0.168557481    -11.47 %
    ppn     1.607030798    1.843542569    -0.236511771    -12.83 %
    npp     1.607030798    1.843542569    -0.236511771    -12.83 %
    pnp     1.676935518    1.843542569    -0.166607051     -9.04 %
    pnn     2.017810479    2.260905450    -0.243094972    -10.75 %
    nnp     2.017810479    2.260905450    -0.243094972    -10.75 %
    npn     1.920851043    2.260905450    -0.340054407    -15.04 %
    nnn     2.359712778    2.721786797    -0.362074019    -13.30 %

**Negative in all eight.** More binding is larger `L`, so the three-body term
*removes* binding — and `4He` is the isotope that needs `62 %` more.

AND IT BREAKS A SYMMETRY THE NUCLEUS HAS
----------------------------------------
Reversal is exact (`pnn` vs `nnp`: `0.0000 %`), but permutation is not:

    pnp vs ppn   same multiset {pp, pn, pn}   4.1686 %
    npn vs nnp   same multiset {pn, pn, nn}   5.0477 %

The pairs differ only in **which nucleon sits in the middle** — the one the band
routing passes through. A physical nucleus has no middle, so this `4-5 %` is a
labelling artifact of embedding the bond graph in a line, not physics. It is the
same defect measured at `4 %` in `chain_telescopes_and_ordering_sensitivity`,
now with its mechanism identified.

THE alpha-FREE CEILING ON 4He
-----------------------------
    B(2H)   exact          2.833163 MeV   AME  2.224566   +27.36 %
    B(4He)  naive sum     17.181143 MeV   AME 28.295661   -39.28 %

    model  B(4He)/B(2H)  <=   6.0643
    AME    B(4He)/B(2H)   =  12.7196
    short by                  2.0975 x

`alpha` cancels in the ratio, so **no normalisation can fix this**. `2H` is a
single bond and therefore exact — no many-body term is possible at `A = 2`. The
`4He` figure is the naive sum, which contains **no** many-body term at all; to
reach `12.7196` the many-body terms would have to be large and **positive**,
whereas every one of the eight measured here is negative.

WHAT THIS MEANS FOR L2 1PPQ
---------------------------
The L2 1PPQ target is `8 meV` on `4He`'s `28.3 MeV`. This construction is short
by a factor of `2.10` — `13` orders of magnitude away — and the correction that
the all-pairs topology adds over the chain pushes it further away, not closer.
The remaining `4He` binding is not in the bond graph. Convention polish
(framed vs writhe-normalised, the `e_pn` sign) moves `1-3 %` and is irrelevant
at this scale.

DISCIPLINE
----------
No fit; nothing wired. `L_pp`, `L_pn`, `L_nn` come out of the seminormal trace
here and match the arc's independently-recorded bond constants to all printed
digits, which is the cross-check that the machinery is the same one. `B_AME` is
a comparison target only.

SIGN CLAIM NARROWED — SEE `cumulant_hierarchy_does_not_converge_probe.py`
-------------------------------------------------------------------------
The three-body terms below are negative at every `A = 3` ordering and that
stands. But the hierarchy does not continue that way: at `A = 5` the fifth
cumulant is **positive**, robustly across 12 bond orderings (`qou-1uul`). Read
the negative sign as a fact about `c_3`, not as a pattern the higher orders
follow. (Whether the hierarchy converges is unknown — an earlier claim that it
does not was withdrawn as a convention artifact.)

-- Ref: [manuscript] bean t7qv
-- Ref: [probe] no_distance_decay_in_the_trace_probe.py
-- Ref: [probe] chain_telescopes_and_ordering_sensitivity_probe.py
-- Ref: [probe] all_pairs_bonds_and_saturation_probe.py
"""
from __future__ import annotations

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import sys
import warnings
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

from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    M_E_MEV as _ME  # noqa: E402,
)
from hecke_characters import build_seminormal_matrices  # noqa: E402
from nucleus_real_sdp import load_cost  # noqa: E402
from pyhecke.atom import D_PN  # noqa: E402
from q_parameter import q_at  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

mp.mp.dps = 30
_Q = q_at(mp.mp.dps)
_H = _Q - 1 / _Q
HF = float(_H)
DPN = float(D_PN)
_ME_M = _ME if isinstance(_ME, mp.mpf) else mp.mpf(str(_ME))
ALPHA = float(_qbeta_e0.order_zero_scaled(_ME_M, _Q))
B_P = (0.0, 0.5, 0.5)
B_N = (0.5, 0.5, 1.0)
AME = {"2H": AME_B_DEUTERON_MEV_VALIDATION, "3H": AME_B_TRITIUM_MEV_VALIDATION, "3He": AME_B_HE3_MEV_VALIDATION, "4He": AME_B_HE4_MEV_VALIDATION}
ORDERS = ("ppp", "ppn", "npp", "pnp", "pnn", "nnp", "npn", "nnn")


def nucleon_word(betas, g0: int, g1: int):
    w = []
    for _ in range(3):
        w += [(1, 0.0, g0), (1, -HF, g1)]
    w += [(1, -betas[0] * HF, g0), (1, -betas[1] * HF, g0),
          (1, -betas[2] * HF, g1)]
    return w + [(1, 0.0, g0), (1, 0.0, g0)]


def bond_d(a: str, b: str) -> float:
    return 0.0 if a == b == "p" else (-HF if a == b == "n" else DPN)


def band(d: float):
    """(T5 T4 T3)(T2 + d)(T3 T4 T5)^-1 — strand 2 crossing strand 6,
    routed THROUGH strands 3-5, which are the middle nucleon."""
    return [(1, 0.0, 5), (1, 0.0, 4), (1, 0.0, 3), (1, d, 2),
            (1, -HF, 3), (1, -HF, 4), (1, -HF, 5)]


_BLK: dict = {}


def blocks(name: str):
    if name not in _BLK:
        parts, y, _c, _d, _m = load_cost(name)
        _BLK[name] = [
            (y[i], [np.asarray(m, dtype=float)
                    for m in build_seminormal_matrices(list(p))[0]])
            for i, p in enumerate(parts)]
    return _BLK[name]


def trM(blks, word) -> float:
    tot = 0.0
    for wt, s in blks:
        d = s[0].shape[0]
        m = np.eye(d)
        for c, dd, g in word:
            m = m @ (c * s[g] + dd * np.eye(d))
        tot += wt * float(np.trace(m))
    return tot


def free3(order: str):
    w = []
    for k, x in enumerate(order):
        w += nucleon_word(B_P if x == "p" else B_N, 3 * k, 3 * k + 1)
    return w


def main() -> int:
    assertions = []
    print("t7qv — the many-body term, located and signed")
    blks = blocks("tritium")
    rng = np.random.default_rng(20260901)

    def L_of(order, bonds):
        base = free3(order)
        w = list(base)
        for b in bonds:
            if b[0] == "adj":
                k = b[1]
                w = w + [(1, bond_d(order[k], order[k + 1]), 3 * k + 2)]
            else:
                w = w + band(bond_d(order[0], order[2]))
        return float(np.log(trM(blks, base) / trM(blks, w)))

    def rand_prefixes(n=20):
        out = []
        for _ in range(n):
            k = int(rng.integers(4, 12))
            out.append([(1, float(rng.uniform(-0.4, 0.4)),
                         int(rng.integers(0, 5))) for _ in range(k)])
        return out

    P_RAND = rand_prefixes()

    # ── A1. the chain attachment is exactly rank one ───────────────────
    print("\n  1. k=1 attachment (chain): rank one, as a control")
    att1 = [(1, bond_d("p", "p"), 5)] + nucleon_word(B_P, 6, 7)
    r1 = []
    for P in P_RAND:
        tP = trM(blks, P)
        if abs(tP) < 1e-10:
            continue
        r1.append(trM(blks, P + att1) / tP)
    r1 = np.array(r1)
    spread1 = r1.max() - r1.min()
    F_pp = 0.385581983466
    ok = spread1 < 1e-12 and abs(r1.mean() - F_pp) < 1e-11
    print(f"     over {len(r1)} random prefix words, tr(P.A)/tr(P):")
    print(f"       min {r1.min():.12f}   max {r1.max():.12f}   "
          f"spread {spread1:.3e}")
    print(f"     one constant, independent of P — and it reproduces the arc's")
    print(f"     recorded transfer scalar F_pp = {F_pp:.12f} to "
          f"{abs(r1.mean() - F_pp):.1e}")
    assertions.append(("A1_chain_attachment_is_exactly_rank_one", ok,
                       f"spread {spread1:.3e} over {len(r1)} prefixes; "
                       f"matches F_pp to {abs(r1.mean() - F_pp):.1e}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. the all-pairs attachment is not ────────────────────────────
    print("\n  2. k=2 attachment (all-pairs): NOT rank one")
    att2 = band(bond_d("p", "p")) + [(1, bond_d("p", "p"), 5)] \
        + nucleon_word(B_P, 6, 7)
    r2 = []
    for P in P_RAND:
        tP = trM(blks, P)
        if abs(tP) < 1e-10:
            continue
        r2.append(trM(blks, P + att2) / tP)
    r2 = np.array(r2)
    spread2 = r2.max() - r2.min()
    ok = spread2 > 0.1
    print(f"     same {len(r2)} prefixes: min {r2.min():.12f}   "
          f"max {r2.max():.12f}   spread {spread2:.6f}")
    print(f"     {spread2 / max(spread1, 1e-18):.1e}x the k=1 spread.")
    print(f"     Mechanism: the 1-3 bond is the band generator, which routes")
    print(f"     strand 2 THROUGH strands 3-5 — the middle nucleon — so it does")
    print(f"     not commute past the prefix. That failure to commute IS the")
    print(f"     three-body term; nothing else here produces one.")
    assertions.append(("A2_allpairs_attachment_is_not_rank_one", ok,
                       f"spread {spread2:.6f} against {spread1:.3e} at k=1"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. the three-body term is negative everywhere ─────────────────
    print("\n  3. the sign, at every A=3 flavour ordering")
    print(f"     {'order':<6s} {'true K3':>13s} {'naive sum':>13s} "
          f"{'3-body':>13s} {'rel':>9s}")
    tb = {}
    for o in ORDERS:
        Lt = L_of(o, [("adj", 0), ("adj", 1), ("far",)])
        Ln = (L_of(o, [("adj", 0)]) + L_of(o, [("adj", 1)])
              + L_of(o, [("far",)]))
        tb[o] = (Lt, Ln, Lt - Ln)
        print(f"     {o:<6s} {Lt:13.9f} {Ln:13.9f} {Lt - Ln:13.9f} "
              f"{100 * (Lt - Ln) / Ln:8.2f}%")
    negs = [v[2] for v in tb.values()]
    rels = [v[2] / v[1] for v in tb.values()]
    ok = all(d < 0 for d in negs)
    print(f"     negative in all {len(negs)}/{len(negs)}: "
          f"{100 * max(rels):.2f}% to {100 * min(rels):.2f}%")
    print(f"     more binding is larger L, so the three-body term REMOVES")
    print(f"     binding — and 4He is the isotope that needs 62 % more.")
    assertions.append(("A3_three_body_term_is_negative_everywhere", ok,
                       f"all {len(negs)} orderings negative, "
                       f"{100 * max(rels):.2f}% to {100 * min(rels):.2f}%"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4. reversal exact, permutation not ────────────────────────────
    print("\n  4. it breaks a symmetry the nucleus has")
    rev = abs(tb["pnn"][0] - tb["nnp"][0])
    perm = [("pnp", "ppn", "{pp, pn, pn}"), ("npn", "nnp", "{pn, pn, nn}")]
    print(f"     reversal  pnn vs nnp   {rev:.2e}   (exact)")
    pd = []
    for a, b, ms in perm:
        d = abs(tb[a][0] - tb[b][0]) / abs(tb[a][0])
        pd.append(d)
        print(f"     permute   {a} vs {b}   {100 * d:.4f} %   same multiset {ms}")
    ok = rev < 1e-12 and min(pd) > 0.04
    print(f"     the pairs differ only in WHICH NUCLEON IS IN THE MIDDLE — the")
    print(f"     one the band routing passes through. A physical nucleus has no")
    print(f"     middle, so this {100 * min(pd):.1f}-{100 * max(pd):.1f} % is a "
          f"labelling artifact of")
    print(f"     embedding the bond graph in a line, now with its mechanism named.")
    assertions.append(("A4_middle_nucleon_is_privileged", ok,
                       f"reversal exact ({rev:.1e}); permutation "
                       f"{100 * min(pd):.4f}-{100 * max(pd):.4f}%"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. no-distance-decay and sub-additivity are one fact ──────────
    print("\n  5. this EXPLAINS no-distance-decay, it does not contradict it")
    # like for like: in ppn the FAR bond (nucleons 1-3) is p-n, so the
    # adjacent bond to compare it against is gen 5 (nucleons 2-3), also p-n —
    # NOT gen 2 (nucleons 1-2), which is p-p.
    far_pn = L_of("ppn", [("far",)])
    adj_pn = L_of("ppn", [("adj", 1)])
    print(f"     ppn: the far bond spans nucleons 1-3 = p-n, so it compares")
    print(f"     against the ADJACENT p-n bond (gen 5), not the p-p one (gen 2)")
    print(f"     far  p-n bond, separation 2: {far_pn:.12f}")
    print(f"     adj  p-n bond, separation 1: {adj_pn:.12f}")
    d_own = abs(far_pn - adj_pn)
    ok = d_own < 1e-9 and abs(tb["ppn"][2]) > 0.1
    print(f"     the bond's OWN invariant is routing-independent "
          f"(|diff| {d_own:.2e})")
    print(f"     while its COMMUTATOR with what it passes through is not "
          f"({tb['ppn'][2]:.6f})")
    print(f"     One gives no decay, the other gives sub-additivity. Same fact,")
    print(f"     seen twice — and a one-parameter r^(s-1) falloff is the wrong")
    print(f"     shape for either.")
    assertions.append(("A5_no_decay_and_subadditivity_are_one_fact", ok,
                       f"far p-n bond matches adjacent p-n to {d_own:.1e} "
                       f"while the triangle defect is {tb['ppn'][2]:.6f}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. the alpha-free ceiling on 4He ──────────────────────────────
    print("\n  6. the alpha-free ceiling — and why 4He is out of reach")
    L2 = {}
    for pair in ("pp", "pn", "nn"):
        o = pair[0] + pair[1] + "p"
        base = free3(o)
        L2[pair] = float(np.log(trM(blks, base)
                                / trM(blks, base + [(1, bond_d(*pair), 2)])))
    print(f"     bond constants from this machinery: L_pp {L2['pp']:.12f}  "
          f"L_pn {L2['pn']:.12f}  L_nn {L2['nn']:.12f}")
    B2 = ALPHA * L2["pn"]
    B4 = ALPHA * (L2["pp"] + 4 * L2["pn"] + L2["nn"])
    rm, ra = B4 / B2, AME["4He"] / AME["2H"]
    print(f"     alpha = {ALPHA:.9f} MeV  (m_e / (q0 (q0-1)), not fitted)")
    print(f"     B(2H)  exact       {B2:9.6f}   AME {AME['2H']:9.6f}   "
          f"{100 * (B2 / AME['2H'] - 1):+.2f}%")
    print(f"     B(4He) naive sum   {B4:9.6f}   AME {AME['4He']:9.6f}   "
          f"{100 * (B4 / AME['4He'] - 1):+.2f}%")
    print(f"     model B(4He)/B(2H) <= {rm:.4f}")
    print(f"     AME   B(4He)/B(2H)  = {ra:.4f}")
    print(f"     short by factor {ra / rm:.4f} — and alpha CANCELS in the ratio,")
    print(f"     so no normalisation can fix it. 2H is a single bond and exact;")
    print(f"     the 4He figure carries NO many-body term at all, and to reach")
    print(f"     {ra:.2f} those terms would have to be large and POSITIVE, where")
    print(f"     all {len(negs)} measured above are negative.")
    ok = ra / rm > 2.0 and B2 > 0
    assertions.append(("A6_alpha_free_shortfall_of_two_point_one", ok,
                       f"model ratio <= {rm:.4f} vs AME {ra:.4f}, "
                       f"short {ra / rm:.4f}x, alpha-independent"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  The many-body term is real, and it is exactly one thing: the band")
    print("  generator routes a non-adjacent bond THROUGH the middle nucleon, so")
    print("  it does not commute past it. That is why the chain attachment is")
    print("  rank one and the all-pairs one is not.")
    print(f"  It is NEGATIVE in all {len(negs)} A=3 configurations "
          f"({100 * max(rels):.1f}% to {100 * min(rels):.1f}%),")
    print("  and it privileges the middle nucleon by 4-5 % on identical bond")
    print("  multisets — a labelling artifact, since a nucleus has no middle.")
    print(f"  The ceiling: B(4He)/B(2H) <= {rm:.3f} against AME {ra:.3f}, short by")
    print(f"  {ra / rm:.2f}x with alpha cancelling. 4He needs the many-body terms")
    print("  to be large and POSITIVE; every one measured is negative.")
    print("  So the remaining 4He binding is NOT in the bond graph, and L2 1PPQ")
    print("  (8 meV of 28.3 MeV) is not reachable by refining it. The convention")
    print("  questions settled earlier in this arc move 1-3 % and are irrelevant")
    print("  at this scale.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="numpy")
        wb.set_description(
            "Locates the many-body term, measures its sign, and derives an "
            "alpha-free ceiling that puts 4He out of reach of the bond graph. "
            "The chain (k=1) attachment functional P -> tr(P.A)/tr(P) is "
            "exactly rank one — one constant over 20 random prefixes to <1e-12, "
            "independently reproducing the arc's recorded F_pp = "
            "0.385581983466. The all-pairs (k=2) attachment is not: the same "
            "prefixes give 0.196..0.696. The mechanism is the band generator "
            "(T5 T4 T3)(T2+d)(T3 T4 T5)^-1, which routes strand 2 through "
            "strands 3-5 — the middle nucleon — so a non-adjacent bond does not "
            "commute past the prefix. That failure to commute IS the three-body "
            "term. It is NEGATIVE in all eight A=3 flavour orderings (-9.04% to "
            "-15.04% of the naive sum), i.e. it REMOVES binding. It also "
            "privileges the middle nucleon: reversal is exact (pnn vs nnp, 0.0) "
            "but permutation is not (pnp vs ppn 4.17%, npn vs nnp 5.05% on "
            "identical bond multisets), a labelling artifact of embedding the "
            "bond graph in a line. This explains rather than contradicts "
            "no-distance-decay: the bond's own invariant is routing-independent "
            "while its commutator with what it passes through is not. Ceiling: "
            "B(2H) is exact at A=2 (single bond, no many-body term possible) "
            "and the naive B(4He) contains no many-body term at all, giving "
            "B(4He)/B(2H) <= 6.0643 against AME 12.7196 — short by 2.0975x with "
            "alpha cancelling, so no normalisation fixes it, and closing it "
            "would need large POSITIVE many-body terms where all eight measured "
            "are negative.")
        wb.add_data("attachment_rank",
                    {"k1_chain_spread": f"{spread1:.3e}",
                     "k1_constant": f"{r1.mean():.12f}",
                     "k1_matches_recorded_F_pp": f"{abs(r1.mean() - F_pp):.1e}",
                     "k2_allpairs_min": f"{r2.min():.12f}",
                     "k2_allpairs_max": f"{r2.max():.12f}",
                     "k2_allpairs_spread": f"{spread2:.6f}",
                     "n_prefixes": len(r1)})
        wb.add_data("three_body_by_ordering",
                    {o: {"true_K3": f"{v[0]:.12f}", "naive_sum": f"{v[1]:.12f}",
                         "three_body": f"{v[2]:.12f}",
                         "rel_pct": f"{100 * v[2] / v[1]:.4f}"}
                     for o, v in tb.items()})
        wb.add_data("labelling",
                    {"reversal_pnn_vs_nnp": f"{rev:.3e}",
                     "permute_pnp_vs_ppn_pct": f"{100 * pd[0]:.4f}",
                     "permute_npn_vs_nnp_pct": f"{100 * pd[1]:.4f}"})
        wb.add_data("bond_constants",
                    {k: f"{v:.12f}" for k, v in L2.items()})
        wb.add_data("ceiling",
                    {"alpha_MeV": f"{ALPHA:.9f}",
                     "B_2H_exact": f"{B2:.6f}", "B_4He_naive_upper": f"{B4:.6f}",
                     "model_ratio_upper": f"{rm:.6f}",
                     "AME_ratio": f"{ra:.6f}",
                     "shortfall_factor": f"{ra / rm:.6f}"})
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "THE CEILING IS A ONE-SIDED BOUND WITH ONE UNMEASURED INPUT. B(2H) "
            "is exact — a single bond admits no many-body term. The B(4He) "
            "figure is the naive pairwise sum, which contains no many-body term "
            "at all, so it is an upper bound PROVIDED the A=4 many-body terms "
            "are non-positive. That is measured for all eight THREE-body terms "
            "at A=3 and NOT measured for the genuine FOUR-body term, which "
            "needs H_12. The unconditional statement is the weaker and still "
            "sufficient one: a pairwise sum with no many-body content gives "
            "6.0643 against 12.7196, and every many-body term measured so far "
            "has the sign that makes it worse.")
        wb.add_caveat(
            "'Rank one' here is a statement about the functional P -> tr(P.A) "
            "restricted to the prefix subalgebra, measured on 20 random words "
            "plus the physical configurations — not a proved algebraic rank. "
            "The k=1 result is exact to 1e-12 across every prefix tried, which "
            "is what the telescoping argument in "
            "chain_telescopes_and_ordering_sensitivity_probe already rests on; "
            "this reproduces it independently and contrasts it with k=2.")
        wb.add_caveat(
            "A=3 traces here are H_9 seminormal and the A=2 bond constants are "
            "read off the same machinery, matching the arc's independently "
            "recorded L_pp / L_pn / L_nn to all printed digits. Everything is "
            "the FRAMED convention (-log(z+d), no writhe normalisation); the "
            "framed/normalised choice moves these numbers by 1-3 %, which does "
            "not approach the 2.1x shortfall and so cannot affect the "
            "conclusion.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
