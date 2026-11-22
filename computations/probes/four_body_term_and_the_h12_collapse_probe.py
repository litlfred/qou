#!/usr/bin/env python3
"""The H_12 wall was never real — convention D collapses it to 7 blocks — and
with `4He` finally measured, the four-body term is negative and the `4He` bound
becomes unconditional at 3.47x.

TWO CORRECTIONS — SEE `the_alpha_spike_is_an_inverted_stagger_probe.py`
------------------------------------------------------------------------
1. **The `3.4693x` headline below is a bad summary.** It is `B(4He)/B(2H)`,
   which pairs the model's worst undershoot with its **only** overshoot. Across
   `A = 2..6` the model is within `1.06 .. 1.89x` of AME everywhere except
   `4He`, a singular outlier at `2.76x`. The ratio is true; as a
   characterisation of the construction it misleads. The `4He` failure is real
   and is diagnosed there as an *inverted* odd-even stagger — the model's `B/A`
   second difference has the opposite sign to AME at `A = 3`, `4` and `5` alike,
   so it peaks at odd `A` where physics peaks at even `A`.
2. **The two-row collapse is not a finding of mine.** It is a corollary of
   theorems this corpus has already proved in Lean: convention D *is* Wenzl
   level `r = 2` (`wenzlLevel_conventionD`), and `schurPrincipal_eq_zero_iff`
   gives `s_lambda = 0 <=> l(lambda) > r`. What was new is only the
   application — nobody had used it to collapse `H_12`. Everything measured
   below stands; the framing did not.

PRECISION — SEE `the_binding_arc_was_measured_in_float64_probe.py`
-----------------------------------------------------------------
Every trace below is float64: `build_seminormal_matrices` returns
`numpy.ndarray(dtype=float)`, and `q` came from `mp.mpf(str(Q0))` off a Python
float, so it carried 17 digits. Three phrasings below are therefore over-claims:
`sum y.dim = 1` "to `1e-15`", the band-routed bonds "identical to adjacent",
and four triangle orderings that "agree exactly". All three are float64-floor
agreements. The 200-bit re-run confirms the identity behind the second and third
of them at `~1e-60` — routing a bond past spectators really is trace-neutral,
and it is the Markov split-link factorisation that makes it so — so the
*conclusions* stand unchanged. What does not stand is reading a `1e-15` as
evidence: that is what float64 prints either way. The honest error on the
magnitudes here is `~1e-13`, set by the truncated `q`.

THE HOLE THIS CLOSES
--------------------
`three_body_term_has_the_wrong_sign_probe` (bean `qou-bc09`) bounded
`B(4He)/B(2H) <= 6.0643` against an AME `12.7196`, but the bound had **one
unmeasured input**: it assumed the genuine FOUR-body term is non-positive, which
was measured for all eight three-body terms at `A = 3` and not at all at `A = 4`,
because `A = 4` needs `H_12`. Siblings have been paying dearly for that wall —
`qou-sv7h` reports a Rust kernel taking `278 s` for a single `A = 2` deuteron.

The wall is an artifact of building blocks whose weight is zero.

CONVENTION D KILLS EVERY PARTITION WITH THREE OR MORE ROWS
----------------------------------------------------------
Convention D's defining fact is that the three-strand q-antisymmetriser lies in
the radical (`y_alt = 0`). That is the `N = 2` specialisation, and it does not
stop at `n = 3`: **every** partition with `>= 3` rows carries weight exactly
zero, at every strand count. Checked against `load_cost`:

    n = 6   4 nonzero blocks of 11
    n = 9   5 nonzero blocks of 30

and the survivors have a closed form — for the two-row partition `(n-k, k)`,

    y = [n - 2k + 1]_q  /  Z ,     Z fixed by  sum_lambda y . dim = 1

with `[m]_q` the balanced q-integer **at `q0` itself**. That reproduces
`load_cost` exactly at `n = 9` (`0.0e0`) and to `1.14e-8` at `n = 6` — the
latter being the known stored-f64 floor of that path, so the closed form is the
more precise of the two, not the less.

WHAT THAT COSTS AT n = 12
-------------------------
Seven blocks: `(12)`, `(11,1)`, `(10,2)`, `(9,3)`, `(8,4)`, `(7,5)`, `(6,6)`,
dimensions `1, 11, 54, 154, 275, 297, 132`. **Largest block 297.** They build in
under a second and `sum y.dim = 1` to `1e-15`.

How far it goes, stated honestly: the largest two-row block is **not** at the
largest `k` — at `n = 18` it sits at `k = 7`, not `k = 9`. Largest blocks are
`297` at `n = 12` (`A = 4`), `2002` at `n = 15` (`A = 5`), and `13260` at
`n = 18` (`A = 6`). So this reaches `A = 5` comfortably in dense arithmetic and
`A = 6` only with sparse handling — it is not a one-off for helium, but neither
is it unlimited.

CROSS-VALIDATED BEFORE BEING BELIEVED
-------------------------------------
`H_12` with reconstructed weights reproduces the arc's `H_6`/`H_9` numbers:

    L_pp  L_pn  L_nn                      to  1.3e-13 .. 3.4e-13
    band-routed bonds at separation 2 AND 3  identical to adjacent, 3.4e-13
    the ppn triangle, matching bond order    3.69e-10

The separation-3 agreement extends `no_distance_decay_in_the_trace_probe` one
step further out, and it comes free here.

A SECOND LABELLING ARTIFACT, LARGER THAN THE FIRST
--------------------------------------------------
Bonds do not commute, so **the order they are inserted in changes the answer**.
Over the six orderings of one `A = 3` triangle the spread is `11.12 %`; over
random orderings of `4He`'s six bonds it is `38-40 %`, with `B` ranging
`8.04 .. 12.43 MeV`. Four of the six triangle orderings agree exactly — the two
outliers are precisely those with the band-routed bond sandwiched between the
two adjacent ones, which is the only pair that fails to commute.

This is not free choice: `atom_gen_chains` fixes an **interleaved** order —
`N0 . N1 . b01 . N2 . b02 . b12 . N3 . b03 . b13 . b23`, each nucleon bonded to
all previous as it is added — which nobody had lifted to the strand picture.

**Correction to my own previous probe.** `three_body_term_has_the_wrong_sign`
appended all bonds after all nucleon words, giving the `ppn` triangle as
`1.607030798`; production's order gives `1.503488161673`. The three-body term
therefore goes from `-0.236512` to `-0.340055` — still negative, and **larger**,
so that probe's conclusion strengthens rather than weakens. Its A1-A2 (rank),
A5 (no-decay) and A6 (ceiling) are untouched; its A3/A4 magnitudes should be
read at production order from here.

THE FOUR-BODY TERM
------------------
Measured by Mobius inversion over nucleon subsets,
`c4 = L_1234 - sum_triples L + sum_pairs L`, at production bond order:

    order   L_K4         sum c2      sum c3       c4           B (MeV)
    ppnn    2.4814437    4.104448   -1.378216   -0.2447883    10.38728
    pnpn    2.4479530    4.104448   -1.411419   -0.2450763    10.24709
    pnnp    2.4456031    4.104448   -1.184297   -0.4745478    10.23725
    nppn    2.4457390    4.104448   -1.638540   -0.0201687    10.23782
    npnp    2.4479530    4.104448   -1.411419   -0.2450763    10.24709
    nnpp    2.4814437    4.104448   -1.378216   -0.2447883    10.38728

**Negative in all six** — and negative in **80 of 80** random bond orders across
two nucleon orderings, so the sign survives the ordering artifact entirely.
(`sum c2 = 4.104448` reproduces the independent naive sum
`L_pp + 4 L_pn + L_nn = 4.104448` (to 1.7e-12), which is the arithmetic cross-check.)

THE BOUND IS NOW UNCONDITIONAL — AND WORSE
------------------------------------------
    B(2H)  exact                    2.833163 MeV
    B(4He) MEASURED, production      10.387277 MeV   AME 28.295661   -63.29 %

    model B(4He)/B(2H)   3.6663      AME 12.7196      short 3.4693 x

Last turn's conditional bound was `2.0975 x`; measuring the missing term moved
it to `3.4693 x`, in the predicted direction. Even the **most favourable of every
ordering convention tried** — `12.4267 MeV` — is short by `2.8999 x`. `alpha`
cancels throughout.

For L2 1PPQ (`8 meV` of `28.3 MeV`) this is the end of the line for the bond
graph: the construction is not `2x` short with a sign ambiguity, it is `2.9-3.5x`
short with every many-body term measured pushing the wrong way.

DISCIPLINE
----------
No fit; nothing wired. The weight closed form is verified against `load_cost`
before use, and every `H_12` quantity is cross-validated against an `H_6`/`H_9`
computation that does not share its weight source. `B_AME` is a comparison
target only; the headline is a ratio in which `alpha` cancels.

SIGN CLAIM NARROWED — SEE `cumulant_hierarchy_does_not_converge_probe.py`
-------------------------------------------------------------------------
The four-body term measured below is negative and that stands, as does
everything about `4He`: at `A = 4` the cumulant expansion terminates at
`k = 4`, so orders `2, 3, 4` exhaust it and all were measured. What does NOT
extend is the general reading. At `A = 5` the fifth cumulant is **positive**
— robustly, in 12 of 12 bond orderings (`qou-1uul`) — so "every many-body term
is negative" and "the naive sum is an upper bound" are false from `A = 5` on.
No `A <= 4` measurement here licenses extrapolation.

(A companion claim that the hierarchy *does not converge* was made and then
**withdrawn**: `|c_5/c_4| > 1` held only in the canonical ordering, 1 of 12.
Whether the hierarchy converges is unknown.)

-- Ref: [manuscript] bean t7qv
-- Ref: [probe] three_body_term_has_the_wrong_sign_probe.py (bound now closed)
-- Ref: [code] pyhecke.atom.atom_gen_chains (the interleaved bond order)
"""
from __future__ import annotations

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import sys
import time
import warnings
from itertools import combinations, permutations
from math import comb
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
    AME_B_HE4_MEV_VALIDATION,
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

mp.mp.dps = 40
_Q = q_at(mp.mp.dps)
_H = _Q - 1 / _Q
HF = float(_H)
DPN = float(D_PN)
_MEM = _ME if isinstance(_ME, mp.mpf) else mp.mpf(str(_ME))
ALPHA = float(_qbeta_e0.order_zero_scaled(_MEM, _Q))
B_P = (0.0, 0.5, 0.5)
B_N = (0.5, 0.5, 1.0)
AME_2H, AME_4HE = AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION
REF_PAIR = {"pp": 0.489899384255, "pn": 0.676821592386, "nn": 0.907262265533}
REF_PPN = 1.607030798          # H9, bonds appended after all nucleon words
ORDERS4 = ("ppnn", "pnpn", "pnnp", "nppn", "npnp", "nnpp")
ALLB = list(combinations(range(4), 2))


def qint(m: int):
    return sum(_Q ** (m - 1 - 2 * i) for i in range(m))


def dim2(n: int, k: int) -> int:
    return comb(n, k) - comb(n, k - 1) if k > 0 else 1


def weights(n: int):
    ks = list(range(n // 2 + 1))
    parts = [((n - k, k) if k else (n,)) for k in ks]
    raw = [qint(n - 2 * k + 1) for k in ks]
    dims = [dim2(n, k) for k in ks]
    Z = sum(r * d for r, d in zip(raw, dims))
    return parts, [float(r / Z) for r in raw], dims


def nucleon_word(betas, g0: int, g1: int):
    w = []
    for _ in range(3):
        w += [(1, 0.0, g0), (1, -HF, g1)]
    w += [(1, -betas[0] * HF, g0), (1, -betas[1] * HF, g0),
          (1, -betas[2] * HF, g1)]
    return w + [(1, 0.0, g0), (1, 0.0, g0)]


def bond_d(a: str, b: str) -> float:
    return 0.0 if a == b == "p" else (-HF if a == b == "n" else DPN)


def band_between(i: int, j: int, d: float):
    """bond between nucleons i<j: strand 3i+2 routed rightwards to strand 3j,
    through every strand in between."""
    a, b = 3 * i + 2, 3 * j
    ups = list(range(b - 1, a, -1))
    return ([(1, 0.0, g) for g in ups] + [(1, d, a)]
            + [(1, -HF, g) for g in reversed(ups)])


def band_perm(i: int, j: int, n: int = 12):
    p = list(range(n))
    a, b = 3 * i + 2, 3 * j
    for g in list(range(b - 1, a, -1)) + [a] + list(range(a + 1, b)):
        p[g], p[g + 1] = p[g + 1], p[g]
    return p


def trM(blks, word) -> float:
    tot = 0.0
    for wt, s in blks:
        d = s[0].shape[0]
        m = np.eye(d)
        for c, dd, g in word:
            m = m @ (c * s[g] + dd * np.eye(d))
        tot += wt * float(np.trace(m))
    return tot


def main() -> int:
    assertions = []
    print("t7qv — the four-body term, and the H_12 collapse that reached it")

    # ── A1. the two-row collapse, and the closed form for the weights ──
    print("\n  1. convention D zeroes every partition with >= 3 rows")
    checks = []
    for name, n in (("deuteron", 6), ("tritium", 9)):
        parts, y, _c, _d, _m = load_cost(name)
        ref = {tuple(p): float(w) for p, w in zip(parts, y)}
        zero_ok = all(abs(v) < 1e-30 for k, v in ref.items() if len(k) > 2)
        ps, ws, _ds = weights(n)
        worst = max(abs(ref[p] - w) / abs(w) for p, w in zip(ps, ws))
        checks.append((n, len(ps), len(parts), zero_ok, worst))
        print(f"     n={n:<3d} {len(ps)} two-row blocks of {len(parts)}   "
              f"all >=3-row weights zero: {zero_ok}   "
              f"closed form worst rel err {worst:.2e}")
    print(f"     closed form: y_(n-k,k) = [n-2k+1]_q / Z, Z from "
          f"sum y.dim = 1, q = q0")
    print(f"     exact at n=9; the 1.14e-8 at n=6 is load_cost's known stored-f64")
    print(f"     floor, so the closed form is the more precise of the two.")
    ok = all(c[3] for c in checks) and max(c[4] for c in checks) < 1e-7
    assertions.append(("A1_convention_D_collapses_to_two_row_blocks", ok,
                       "; ".join(f"n={c[0]}: {c[1]}/{c[2]} blocks, zeros ok "
                                 f"{c[3]}, err {c[4]:.1e}" for c in checks)))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. so H_12 is seven small blocks ──────────────────────────────
    print("\n  2. therefore H_12 is 7 blocks, not 77 — the wall was an artifact")
    P12, Y12, D12 = weights(12)
    t0 = time.time()
    BLK = [(w, [np.asarray(m, dtype=float)
                for m in build_seminormal_matrices(list(p))[0]])
           for p, w in zip(P12, Y12)]
    build_s = time.time() - t0
    norm = sum(w * d for w, d in zip(Y12, D12))
    print(f"     blocks: {', '.join(str(p) for p in P12)}")
    print(f"     dims:   {D12}   largest {max(D12)}   total {sum(D12)}")
    print(f"     sum y.dim = {norm:.15f}   built in {build_s:.2f}s")
    reach = {A: max(weights(3 * A)[2]) for A in (4, 5, 6, 7)}
    print(f"     how far it goes (note the largest block is NOT at the largest k"
          f" — at n=18 it sits at k=7):")
    for A, d in reach.items():
        note = ("dense, comfortable" if d <= 2100 else
                "needs sparse handling" if d <= 20000 else "out of reach")
        print(f"       A={A}  n={3 * A}  largest block {d:>6d}   {note}")
    print(f"     so A=5 is comfortable and A=6 needs sparsity — not a one-off")
    print(f"     for helium, but not unlimited either.")
    print(f"     for scale: qou-sv7h reports 278 s for a single A=2 deuteron.")
    ok = max(D12) == 297 and abs(norm - 1) < 1e-12 and build_s < 60
    assertions.append(("A2_h12_is_seven_small_blocks", ok,
                       f"7 blocks, max dim {max(D12)}, sum y.dim={norm:.12f}, "
                       f"built {build_s:.2f}s; reach by A: {reach}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. cross-validate H_12 against H_6/H_9 ────────────────────────
    print("\n  3. cross-validation against the H_6/H_9 route")
    for (i, j) in ((0, 2), (1, 3), (0, 3)):
        a, b = 3 * i + 2, 3 * j
        exp = list(range(12))
        exp[a], exp[b] = exp[b], exp[a]
        assert band_perm(i, j) == exp, f"band {i}-{j} permutation wrong"
    print(f"     band permutations for nucleon pairs (0,2) (1,3) (0,3): all the")
    print(f"     correct transpositions (checked before use)")

    def free4(order):
        w = []
        for k, x in enumerate(order):
            w += nucleon_word(B_P if x == "p" else B_N, 3 * k, 3 * k + 1)
        return w

    def bond_word(order, i, j):
        d = bond_d(order[i], order[j])
        return [(1, d, 3 * i + 2)] if j == i + 1 else band_between(i, j, d)

    def L_bonds(order, bonds, base, tf):
        w = list(base)
        for (i, j) in bonds:
            w = w + bond_word(order, i, j)
        return float(np.log(tf / trM(BLK, w)))

    o = "ppnn"
    base = free4(o)
    tf = trM(BLK, base)
    diffs = []
    for S, lbl in (((0, 1), "pp"), ((2, 3), "nn"), ((1, 2), "pn")):
        v = L_bonds(o, [S], base, tf)
        diffs.append(abs(v - REF_PAIR[lbl]))
        print(f"     adjacent {lbl}  H12 {v:.12f}  ref {REF_PAIR[lbl]:.12f}  "
              f"diff {abs(v - REF_PAIR[lbl]):.2e}")
    far = []
    for S in ((0, 2), (1, 3), (0, 3)):
        v = L_bonds(o, [S], base, tf)
        far.append(abs(v - REF_PAIR["pn"]))
        print(f"     band-routed {S} sep {S[1] - S[0]} = pn  H12 {v:.12f}  "
              f"diff {abs(v - REF_PAIR['pn']):.2e}")
    tri = abs(L_bonds(o, [(0, 1), (1, 2), (0, 2)], base, tf) - REF_PPN)
    print(f"     ppn triangle at the H9 bond order: diff {tri:.2e}")
    print(f"     the separation-3 agreement extends no_distance_decay one step")
    print(f"     further out, and comes free here.")
    ok = max(diffs) < 1e-11 and max(far) < 1e-11 and tri < 1e-8
    assertions.append(("A3_h12_reproduces_the_h6_h9_numbers", ok,
                       f"pair bonds to {max(diffs):.1e}, band-routed (sep 2 and "
                       f"3) to {max(far):.1e}, triangle to {tri:.1e}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4. bond insertion order is a second labelling artifact ────────
    print("\n  4. bonds do not commute — insertion order changes the answer")
    vals = [L_bonds(o, list(bo), base, tf)
            for bo in permutations([(0, 1), (1, 2), (0, 2)])]
    spread3 = (max(vals) - min(vals)) / float(np.mean(vals))
    uniq = sorted({round(v, 10) for v in vals})
    print(f"     the 6 bond orders of the ppn triangle give {len(uniq)} values:")
    for u in uniq:
        print(f"       {u:.10f}  ({sum(1 for v in vals if round(v, 10) == u)} of 6)")
    print(f"     spread {max(vals) - min(vals):.6f} = {100 * spread3:.2f} % of the mean")
    print(f"     the two outliers are exactly those with the band-routed bond")
    print(f"     sandwiched between the two adjacent ones — the only pair that")
    print(f"     fails to commute. atom_gen_chains fixes an INTERLEAVED order")
    print(f"     N0.N1.b01.N2.b02.b12.N3.b03.b13.b23, not previously lifted to")
    print(f"     the strand picture.")
    ok = spread3 > 0.10 and len(uniq) == 3
    assertions.append(("A4_bond_insertion_order_is_an_artifact", ok,
                       f"{len(uniq)} distinct values over 6 orders, spread "
                       f"{100 * spread3:.2f}% of mean"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. the four-body term, at production order ────────────────────
    print("\n  5. the four-body term (production interleaved order)")

    def word_int(order, S):
        w = []
        for k in range(4):
            w += nucleon_word(B_P if order[k] == "p" else B_N, 3 * k, 3 * k + 1)
            if k in S:
                for prev in range(k):
                    if prev in S:
                        w += bond_word(order, prev, k)
        return w

    def cluster_int(order):
        b = word_int(order, set())
        t = trM(BLK, b)

        def LS(S):
            return float(np.log(t / trM(BLK, word_int(order, set(S)))))
        c2 = {S: LS(S) for S in combinations(range(4), 2)}
        c3 = {S: LS(S) - sum(c2[p] for p in combinations(S, 2))
              for S in combinations(range(4), 3)}
        full = LS((0, 1, 2, 3))
        return full, sum(c2.values()), sum(c3.values()), \
            full - sum(c3.values()) - sum(c2.values())

    print(f"     {'order':<6s} {'L_K4':>11s} {'sum c2':>10s} {'sum c3':>10s} "
          f"{'c4':>11s} {'B MeV':>9s} {'vs AME':>9s}")
    res = {}
    for order in ORDERS4:
        full, s2, s3, c4 = cluster_int(order)
        B = ALPHA * full
        res[order] = (full, s2, s3, c4, B)
        print(f"     {order:<6s} {full:11.7f} {s2:10.6f} {s3:10.6f} "
              f"{c4:11.7f} {B:9.5f} {100 * (B / AME_4HE - 1):+8.2f}%")
    naive = REF_PAIR["pp"] + 4 * REF_PAIR["pn"] + REF_PAIR["nn"]
    s2v = res["ppnn"][1]
    print(f"     sum c2 = {s2v:.6f} reproduces the independent naive sum "
          f"L_pp+4L_pn+L_nn = {naive:.6f}  (diff {abs(s2v - naive):.1e})")
    # robustness over bond order
    rng = np.random.default_rng(4)
    allneg, n_s = True, 0
    Bmax = 0.0
    for order in ("ppnn", "pnpn"):
        b = free4(order)
        t = trM(BLK, b)
        for _ in range(40):
            bo = list(ALLB)
            rng.shuffle(bo)
            pos = {x: i for i, x in enumerate(bo)}

            def LS2(S, _p=pos, _o=order, _b=b, _t=t):
                bs = sorted([x for x in ALLB if x[0] in S and x[1] in S],
                            key=lambda x: _p[x])
                return L_bonds(_o, bs, _b, _t)
            c2 = {S: LS2(S) for S in combinations(range(4), 2)}
            c3 = {S: LS2(S) - sum(c2[p] for p in combinations(S, 2))
                  for S in combinations(range(4), 3)}
            f = LS2((0, 1, 2, 3))
            c4 = f - sum(c3.values()) - sum(c2.values())
            allneg = allneg and c4 < 0
            Bmax = max(Bmax, ALPHA * f)
            n_s += 1
    ok = all(v[3] < 0 for v in res.values()) and allneg \
        and abs(s2v - naive) < 1e-5
    print(f"     c4 negative in all {len(res)}/{len(res)} nucleon orderings,")
    print(f"     and in {n_s}/{n_s} random bond orders — the sign survives the")
    print(f"     ordering artifact entirely.")
    assertions.append(("A5_four_body_term_is_negative", ok,
                       f"c4 < 0 in all {len(res)} production orderings and all "
                       f"{n_s} random bond orders; sum c2 matches naive to "
                       f"{abs(s2v - naive):.1e}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. the bound is now unconditional, and worse ──────────────────
    print("\n  6. the bound closes — unconditional, and worse")
    B2 = ALPHA * REF_PAIR["pn"]
    Bbest = max(v[4] for v in res.values())
    rm, ra = Bbest / B2, AME_4HE / AME_2H
    print(f"     B(2H)  exact                {B2:9.6f} MeV")
    print(f"     B(4He) MEASURED production  {Bbest:9.6f} MeV   AME "
          f"{AME_4HE:9.6f}   {100 * (Bbest / AME_4HE - 1):+.2f}%")
    print(f"     model B(4He)/B(2H) = {rm:.4f}   AME {ra:.4f}   "
          f"short {ra / rm:.4f}x")
    print(f"     last turn's CONDITIONAL bound was 2.0975x; measuring the")
    print(f"     missing term moved it to {ra / rm:.4f}x, in the predicted direction.")
    print(f"     most favourable of every ordering convention tried: "
          f"{Bmax:.4f} MeV")
    print(f"     -> even that is short by {ra / (Bmax / B2):.4f}x. alpha cancels.")
    ok = ra / rm > 3.0 and ra / (Bmax / B2) > 2.5
    assertions.append(("A6_shortfall_is_unconditional_and_worse", ok,
                       f"measured ratio {rm:.4f} vs AME {ra:.4f}, short "
                       f"{ra / rm:.4f}x; best-case {Bmax:.4f} MeV still short "
                       f"{ra / (Bmax / B2):.4f}x"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  The H_12 wall was an artifact of building 70 blocks whose weight is")
    print("  zero. Convention D kills every partition with >= 3 rows at every n,")
    print("  leaving 7 blocks at n=12 with largest dimension 297 — under a second")
    print(f"  to build; A=5 stays comfortable and A=6 needs sparsity.")
    print("  With 4He finally measured: the four-body term is NEGATIVE in all six")
    print(f"  nucleon orderings and all {n_s} random bond orders, so bc09's")
    print("  conditional bound closes. It closes WORSE — the shortfall goes from")
    print(f"  2.0975x to {ra / rm:.4f}x, and even the most favourable ordering")
    print(f"  convention tried leaves {ra / (Bmax / B2):.4f}x. alpha cancels throughout.")
    print("  Found on the way: bond insertion order is a second labelling")
    print("  artifact, 11 % at A=3 and 38-40 % at A=4, and production's own")
    print("  interleaved order had never been lifted to the strand picture. That")
    print("  corrects my previous probe's A=3 magnitudes — in the direction that")
    print("  makes its conclusion stronger.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="numpy")
        wb.set_description(
            "Closes the one unmeasured input in bean qou-bc09's 4He bound by "
            "removing the H_12 wall. Convention D puts the three-strand "
            "q-antisymmetriser in the radical, which is the N=2 specialisation: "
            "EVERY partition with >= 3 rows carries weight exactly zero at every "
            "strand count (verified against load_cost at n=6 and n=9), and the "
            "survivors have the closed form y_(n-k,k) = [n-2k+1]_q / Z with Z "
            "fixed by sum y.dim = 1 and q = q0 — exact at n=9, and 1.14e-8 at "
            "n=6 which is load_cost's own stored-f64 floor. H_12 is therefore 7 "
            "blocks with largest dimension 297, built in under a second, where "
            "77 blocks would be infeasible; the same rule reaches A=6 at largest "
            "block 13260 (dense-comfortable to A=5). Cross-validated before use: H_12 reproduces L_pp, L_pn, "
            "L_nn to 1.3e-13, band-routed bonds at separation 2 AND 3 to "
            "3.4e-13 (extending no-distance-decay one step further out), and the "
            "ppn triangle to 3.69e-10 at matching bond order. Found on the way: "
            "bonds do not commute, so insertion order is a second labelling "
            "artifact — 11.12% over one A=3 triangle's six orders, 38-40% over "
            "4He's, with the outliers exactly those putting the band-routed bond "
            "between the two adjacent ones. atom_gen_chains fixes an interleaved "
            "order that had not been lifted to the strand picture, and using it "
            "corrects three_body_term_has_the_wrong_sign's ppn triangle from "
            "1.607030798 to 1.503488161673 (three-body term -0.236512 -> "
            "-0.340055, still negative and larger). THE RESULT: the four-body "
            "term is negative in all six nucleon orderings and all 80 random "
            "bond orders. B(4He) = 10.387277 MeV against AME 28.295661 "
            "(-63.29%), so B(4He)/B(2H) = 3.6663 against AME 12.7196 — short by "
            "3.4693x where the conditional bound was 2.0975x, and the most "
            "favourable ordering convention tried still leaves 2.8999x. alpha "
            "cancels throughout.")
        wb.add_data("two_row_collapse",
                    {f"n={c[0]}": {"two_row_blocks": c[1], "total_blocks": c[2],
                                   "ge3_row_weights_all_zero": c[3],
                                   "closed_form_worst_rel_err": f"{c[4]:.3e}"}
                     for c in checks})
        wb.add_data("h12_blocks",
                    {"partitions": [str(p) for p in P12], "dims": D12,
                     "largest": max(D12), "sum_y_dim": f"{norm:.15f}",
                     "build_seconds": f"{build_s:.2f}",
                     "largest_block_by_A": {str(k): v
                                            for k, v in reach.items()}})
        wb.add_data("cross_validation",
                    {"pair_bonds_max_diff": f"{max(diffs):.2e}",
                     "band_routed_sep2_and_sep3_max_diff": f"{max(far):.2e}",
                     "ppn_triangle_diff": f"{tri:.2e}"})
        wb.add_data("bond_order_artifact",
                    {"A3_distinct_values": len(uniq),
                     "A3_values": [f"{u:.10f}" for u in uniq],
                     "A3_spread_pct_of_mean": f"{100 * spread3:.2f}",
                     "production_ppn": "1.503488161673",
                     "previous_probe_ppn": f"{REF_PPN}"})
        wb.add_data("four_body",
                    {o: {"L_K4": f"{v[0]:.9f}", "sum_c2": f"{v[1]:.9f}",
                         "sum_c3": f"{v[2]:.9f}", "c4": f"{v[3]:.9f}",
                         "B_MeV": f"{v[4]:.6f}"} for o, v in res.items()})
        wb.add_data("shortfall",
                    {"B_2H_MeV": f"{B2:.6f}", "B_4He_MeV": f"{Bbest:.6f}",
                     "model_ratio": f"{rm:.6f}", "AME_ratio": f"{ra:.6f}",
                     "shortfall": f"{ra / rm:.6f}",
                     "best_case_B_4He_MeV": f"{Bmax:.6f}",
                     "best_case_shortfall": f"{ra / (Bmax / B2):.6f}",
                     "previous_conditional_bound": "2.0975"})
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "THE WEIGHTS AT n=12 ARE RECONSTRUCTED, NOT LOADED. No y_lambda "
            "source exists for n=12, so they come from the closed form "
            "y_(n-k,k) = [n-2k+1]_q / Z. That form is verified against "
            "load_cost at n=6 and n=9 BEFORE use (exact at n=9), and every "
            "H_12 quantity that has an H_6/H_9 counterpart is cross-checked "
            "against it. It is nonetheless a reconstruction, and if the "
            "two-row rule fails at some n for a reason not visible at n=6 or "
            "n=9, every number here moves.")
        wb.add_caveat(
            "BOND INSERTION ORDER IS NOT SETTLED PHYSICS, ONLY SETTLED "
            "CONVENTION. The headline uses atom_gen_chains' interleaved order "
            "because that is what production does, not because anything shows "
            "it is right. The spread across orders is 38-40% at A=4, which is "
            "far larger than the framed/writhe-normalised question this arc "
            "spent two probes on. The CONCLUSION is insensitive to it — c4 < 0 "
            "in all 80 random orders and the best case is still 2.90x short — "
            "but any single quoted B(4He) is convention-dependent at the "
            "tens-of-percent level and should be quoted with its order.")
        wb.add_caveat(
            "CORRECTS A PREVIOUS PROBE OF MINE. "
            "three_body_term_has_the_wrong_sign_probe appended all bonds after "
            "all nucleon words rather than interleaving, giving the ppn "
            "triangle as 1.607030798 where production gives 1.503488161673. "
            "Its A3/A4 three-body magnitudes should be read at production "
            "order (-0.340055 rather than -0.236512 for ppn); the sign and "
            "hence every conclusion is unchanged, and the magnitude grows. Its "
            "A1/A2 (attachment rank), A5 (no-decay) and A6 (ceiling) do not "
            "depend on the bond order.")
        wb.add_caveat(
            "All quantities are the FRAMED convention (-log(z+d), no writhe "
            "normalisation) and use no electron content, matching AME's "
            "nuclear binding. The framed/normalised choice moves these by "
            "1-3%, which does not approach a 2.9-3.5x shortfall.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
