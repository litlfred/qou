#!/usr/bin/env python3
"""Put the bonds back: binding is nonzero, the LP degeneracy breaks, and the
log-defect is EXACTLY additive over bonds with per-bond-type constants.

WHY
---
`betas_are_forced_by_quark_content_probe.py` found that every binding zero this
series reported was measured on a construction with the inter-nucleon crossings
left out. This probe puts them back.

For `A = 2` that means working in `H_6`: the deuteron is
`w_p (gens 0,1) . w_n (gens 3,4) . bond (gen 2)`, with the bond carrying
`(c, d) = (1, D_PN)`. `A = 3` needs `H_9`; both have complete Markov-weight
tables in `nucleus_real_sdp.load_cost`.

FIRST, A CORRECTION TO MY OWN LAST TURN
------------------------------------------
I reported that the atom carries `C(A,2)` inter-nucleon crossings. That is true
of `atom_gen_chains`, which appends a bond for every pair (`for prev in
range(k)`). But `atom_braid_word_3A` — the honest `3A`-strand builder — places
bonds only between **adjacent** nucleons (`if include_inter and k < A - 1`), at
generator `3k+2`: **`A - 1` bonds, a chain**. The two disagree for every
`A >= 3`:

    A        atom_gen_chains        atom_braid_word_3A
    2            1  = C(A,2)            1  = A-1        agree
    3            3                      2
    4            6                      3
    6           15                      5

**The chain reading is the load-bearing one**: `c_atom = 2A - #(odd bonds) =
A + 1` needs exactly `A - 1` odd bonds, which is what the census probe's
`chain_bonds` counts and what Lean `QOU.MassTheory.ClassicalTraceFloor` proves.
Everything below uses the chain topology. The disagreement between the two
builders is a real inconsistency and is reported, not resolved here.

THE BOND IS A LARGE EFFECT
----------------------------
At `A = 2`:

    tr_M(free = w_p . w_n)        =  0.299015019
    tr_M(atom = free . bond)      =  0.151968341
    defect                        = -0.147046678   (-49.18 %)

Negative — the bound state is lighter than its free constituents, which is the
right sign for a mass defect. The free value reproduces `tr_3(p) . tr_3(n)` to
`6.1e-9`, the precision of the stored `y_lambda` table (the same `1.1e-8` scale
`h3a_frobenius_gram_offdiagonal_probe` saw), so multiplicativity self-checks.

THE LP DEGENERACY BREAKS
--------------------------
Rebuilding the positive-sector LP on a space that *contains* the bond — the 36
product words `b_i (x) b_j` together with their 36 bond-translates `b_i (x) b_j
. T_2`, a 72-word spanning set of rank 50 — gives

    phi(free) = 0.429886497        phi(atom) = 0.248443512
    E_bind    = phi(free) - phi(atom) = +0.181442985   (42.2 % of phi(free))

and, decisively, the two states **no longer share a dual vertex**: supports of
size 2 and 3, not identical. In the bond-free LP they were identical and
rank-one, which is exactly why every gap came out an algebraic zero.
`phi(free) = 0.4298865` also reproduces the multiplicative free value from
`nfold_ip_coupling_duality_gap_probe`, so the two constructions agree where they
overlap.

THE STRUCTURE: EXACT BOND-ADDITIVITY
--------------------------------------
Define `L := log( tr_M(free) / tr_M(atom) )`. Then `L` is **exactly additive
over the bonds** — switching bonds on one at a time and summing reproduces the
all-bonds value to `4.4e-16`:

    2H    p-n            L = 0.676821587
    3He   p-n, n-p       L = 1.353643185  =  0.676821592 x 2
    3H    p-n, n-n       L = 1.584083858  =  0.676821592 + 0.907262272

**NARROWED (2026-09-01)** by `all_pairs_bonds_and_saturation_probe.py`: this
additivity holds over the ADJACENT chain only, because those bonds sit at
generators `3k+2`, three apart, and commute. Once a long-range band generator is
included the residual is `2.4e-1`, not `4.4e-16`. The per-bond constants below
stand; the additive law does not extend to all pairs.

so the whole thing is carried by two per-bond-type constants:

    L_pn = 0.676821592386        L_nn = 0.907262271178

with `L_pn` agreeing between `2H` and `3He` to `5.6e-9` — again the `y`-table's
precision, not a modelling error. Nothing here was fitted: the constants are
outputs.

WHAT IT GETS RIGHT, AND WHAT IT DOES NOT
------------------------------------------
It separates the mirror pair, in the right direction: `L(3H) > L(3He)` because
`3H` carries an `n-n` bond where `3He` carries a second `p-n`, and `L_nn >
L_pn`. Experimentally `3H` is indeed the more bound of the two. Comparing ratios
(AME read-only, nothing tuned):

    L(3H)/L(3He)  = 1.17022     B(3H)/B(3He)  = 1.09896      +6.5 %
    L(2H)/L(3He)  = 0.50000     B(2H)/B(3He)  = 0.28823      +73 %

So the model reproduces the mirror ordering and lands within 6.5 % on that
ratio, and is badly wrong on `A = 2` against `A = 3` — 0.5 by construction,
since it counts one bond against two, where the experimental ratio is 0.288.
A bond-count law cannot be the whole story. Both results are reported; the
second is the one that matters for anyone tempted by the first.

And the absolute scale is not a binding energy. A 49 % trace defect at `2H` is
three orders above the physical `0.1 %`; these are dimensionless multiplicative
traces, and turning `L` into MeV needs the corpus's mass normalisation, which is
deliberately not applied here.

DISCIPLINE
----------
No fit; nothing wired. `B_AME` values are read for the two ratio comparisons
only and no quantity is tuned to them. Markov weights and characters come from
`load_cost` and `build_seminormal_matrices`, the corpus's own routines; the
`y_lambda` tables are stored f64, which sets the `~1e-8` floor quoted above.

-- Ref: [manuscript] bean t7qv
-- Ref: [code] pyhecke.atom.atom_braid_word_3A (chain topology), atom_gen_chains
-- Ref: [probe] betas_are_forced_by_quark_content_probe.py (found the omission)
-- Ref: [probe] nfold_ip_coupling_duality_gap_probe.py (the bond-free LP)
-- Ref: [lean] QOU.MassTheory.ClassicalTraceFloor (c_atom = A + 1, A-1 bonds)
"""
from __future__ import annotations

import math
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
from scipy.optimize import linprog  # noqa: E402

from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
)
from hecke_characters import build_seminormal_matrices  # noqa: E402
from nucleus_real_sdp import load_cost  # noqa: E402
from pyhecke.atom import D_PN, atom_gen_chains, nucleon_gen_chains  # noqa: E402
from pyhecke.gram import _hm_mp  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

mp.mp.dps = 30
_Q = mp.mpf(str(Q0))
_H = _Q - 1 / _Q
HF = float(_H)
DPN = float(D_PN)
B_P = (0.0, 0.5, 0.5)
B_N = (0.5, 0.5, 1.0)
NF3 = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
_BLOCKS: dict = {}


def blocks(name: str):
    if name not in _BLOCKS:
        parts, y, _chi, _dims, _meta = load_cost(name)
        _BLOCKS[name] = [
            (y[i], [np.asarray(m, dtype=float)
                    for m in build_seminormal_matrices(list(p))[0]])
            for i, p in enumerate(parts)]
    return _BLOCKS[name]


def nucleon_word(betas, g0: int, g1: int):
    """(sigma_0 sigma_1^-1)^3 . sigma_0(b0) sigma_0(b1) sigma_1(b2) . sigma_0^2"""
    w = []
    for _ in range(3):
        w += [(1, 0.0, g0), (1, -HF, g1)]
    w += [(1, -betas[0] * HF, g0), (1, -betas[1] * HF, g0),
          (1, -betas[2] * HF, g1)]
    return w + [(1, 0.0, g0), (1, 0.0, g0)]


def bond_cd(a: str, b: str):
    if a == b == "p":
        return (1, 0.0)
    if a == b == "n":
        return (1, -HF)
    return (1, DPN)


def ordering(Z: int, N: int):
    """Interleaved nucleon ordering, matching build_atom_nf / atom_gen_chains."""
    out, pc, nc = [], 0, 0
    for k in range(Z + N):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            out.append("p")
            pc += 1
        else:
            out.append("n")
            nc += 1
    return out


def trM(blks, word):
    tot = 0.0
    for wt, s in blks:
        d = s[0].shape[0]
        mtx = np.eye(d)
        for c, dd, g in word:
            mtx = mtx @ (c * s[g] + dd * np.eye(d))
        tot += wt * float(np.trace(mtx))
    return tot


def build_atom(name: str, Z: int, N: int):
    """(blocks, free word, list of (index, type, bond letter)) — CHAIN topology."""
    blks = blks_ = blocks(name)
    order = ordering(Z, N)
    free = []
    for k, nuc in enumerate(order):
        free += nucleon_word(B_P if nuc == "p" else B_N, 3 * k, 3 * k + 1)
    bonds = []
    for k in range(len(order) - 1):
        c, d = bond_cd(order[k], order[k + 1])
        bonds.append((k, order[k] + order[k + 1], (c, d, 3 * k + 2)))
    return blks_, free, bonds, order


def nf3(betas):
    v = [mp.mpf(1)] + [mp.mpf(0)] * 5
    for _ in range(3):
        v = _hm_mp(v, mp.mpf(1), mp.mpf(0), 0, _H)
        v = _hm_mp(v, mp.mpf(1), -_H, 1, _H)
    for c, g in ((betas[0], 0), (betas[1], 0), (betas[2], 1)):
        v = _hm_mp(v, mp.mpf(1), -mp.mpf(c) * _H, g, _H)
    v = _hm_mp(v, mp.mpf(1), mp.mpf(0), 0, _H)
    v = _hm_mp(v, mp.mpf(1), mp.mpf(0), 0, _H)
    return np.array([float(x) for x in v])


def main() -> int:
    assertions = []
    print("t7qv — the binding LP, with the inter-nucleon bonds put back")

    # ── A1. the two builders disagree on bond topology ────────────────
    print("\n  1. bond topology: two corpus builders disagree for A >= 3")
    per_p = len(nucleon_gen_chains(["u", "u", "d"])[0])
    per_n = len(nucleon_gen_chains(["u", "d", "d"])[0])
    rows, ok = [], True
    print(f"     {'A':>2s}  {'atom_gen_chains':>16s}  {'C(A,2)':>7s}  "
          f"{'braid_word (A-1)':>17s}")
    for Z, N in ((1, 1), (1, 2), (2, 2), (3, 3)):
        A = Z + N
        g0, _ = atom_gen_chains(Z, N)
        extra = len(g0) - (Z * per_p + N * per_n)
        rows.append((A, extra, A * (A - 1) // 2, A - 1))
        ok &= extra == A * (A - 1) // 2
        print(f"     {A:2d}  {extra:16d}  {A * (A - 1) // 2:7d}  {A - 1:17d}"
              f"{'   agree' if A == 2 else ''}")
    disagree = any(r[1] != r[3] for r in rows)
    ok = ok and disagree
    print(f"     they agree only at A = 2; the arity law c_atom = A+1 needs")
    print(f"     exactly A-1 odd bonds, so the CHAIN reading is load-bearing")
    assertions.append(("A1_bond_topology_disagreement", ok,
                       f"atom_gen_chains gives C(A,2) = "
                       f"{[r[1] for r in rows]}, braid word gives A-1 = "
                       f"{[r[3] for r in rows]}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. the bond is a large, correctly-signed effect ──────────────
    print("\n  2. the bond produces a large negative mass defect")
    blks, free_w, bonds, order = build_atom("deuteron", 1, 1)
    tf = trM(blks, free_w)
    ta = trM(blks, free_w + [b[2] for b in bonds])
    prod = float(np.dot(
        [1, float(_Q ** 3 / (_Q ** 2 + 1))] * 0 + [0], [0])) if False else None
    z = _Q ** 3 / (_Q ** 2 + 1)
    t3 = np.array([float(x) for x in
                   [mp.mpf(1), z, z, z ** 2, z ** 2, _H * z ** 2 + z]])
    mult = float(t3 @ nf3(B_P)) * float(t3 @ nf3(B_N))
    mult_err = abs(tf - mult) / abs(mult)
    ok = ta < tf and abs((ta - tf) / tf) > 0.1 and mult_err < 1e-7
    print(f"     tr_M(free)   = {tf:.15f}")
    print(f"     tr_M(atom)   = {ta:.15f}")
    print(f"     defect       = {ta - tf:+.15f}   ({100 * (ta - tf) / tf:+.2f} %)")
    print(f"     multiplicativity self-check: tr_3(p) tr_3(n) = {mult:.15f}, "
          f"rel {mult_err:.1e}")
    assertions.append(("A2_bond_gives_large_negative_defect", ok,
                       f"defect {ta - tf:+.9f} ({100 * (ta - tf) / tf:+.2f}%); "
                       f"free reproduces the H_3 product to {mult_err:.1e}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. the LP degeneracy breaks ──────────────────────────────────
    print("\n  3. with the bond in the space, the LP is no longer degenerate")
    prod_words = [tuple(wi) + tuple(3 + g for g in wj)
                  for wi in NF3 for wj in NF3]
    basis = prod_words + [w + (2,) for w in prod_words]

    def mats(word):
        out = []
        for _wt, s in blks:
            d = s[0].shape[0]
            m = np.eye(d)
            for g in word:
                m = m @ s[g]
            out.append(m)
        return out

    M = [mats(w) for w in basis]
    R = [mats(tuple(reversed(w))) for w in basis]
    nb = len(basis)
    gram = np.zeros((nb, nb))
    cost = np.zeros(nb)
    for i in range(nb):
        cost[i] = sum(wt * float(np.trace(m))
                      for (wt, _s), m in zip(blks, M[i]))
        for j in range(nb):
            gram[i, j] = sum(wt * float(np.trace(R[i][k] @ M[j][k]))
                             for k, (wt, _s) in enumerate(blks))
    rank = int(np.linalg.matrix_rank(gram, tol=1e-8))
    c_prod = np.kron(nf3(B_P), nf3(B_N))
    v_free = np.concatenate([c_prod, np.zeros(36)])
    v_atom = np.concatenate([DPN * c_prod, c_prod])

    def phi(v):
        r = linprog(cost, A_ub=-gram, b_ub=-(gram @ v),
                    bounds=[(0, None)] * nb, method="highs")
        if not r.success:
            return None, None
        return float(r.fun), -r.ineqlin.marginals

    pf, yf = phi(v_free)
    pa, ya = phi(v_atom)
    sf = int((np.abs(yf) > 1e-9).sum())
    sa = int((np.abs(ya) > 1e-9).sum())
    same = bool(np.allclose(yf, ya, atol=1e-9))
    ok = (pf is not None and pa is not None and not same and pf > pa)
    print(f"     spanning set: {len(prod_words)} product words + "
          f"{len(prod_words)} bond-translates = {nb}, Gram rank {rank}")
    print(f"     phi(free) = {pf:.12f}   phi(atom) = {pa:.12f}")
    print(f"     E_bind = {pf - pa:+.12f}   ({100 * (pf - pa) / pf:.2f} % of "
          f"phi(free))")
    print(f"     dual supports: free {sf}, atom {sa}; identical? {same}")
    print(f"     (bond-free LP had identical RANK-ONE duals — hence the zeros)")
    assertions.append(("A3_lp_degeneracy_breaks", ok,
                       f"phi(free) {pf:.9f}, phi(atom) {pa:.9f}, gap "
                       f"{pf - pa:+.9f}; dual supports {sf} vs {sa}, "
                       f"identical={same}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4/A5. exact bond-additivity and the per-type constants ───────
    print("\n  4. L = log(tr_free / tr_atom) is EXACTLY additive over bonds")
    L_tot, singles, worst = {}, {}, 0.0
    for name, Z, N in (("deuteron", 1, 1), ("tritium", 1, 2), ("he3", 2, 1)):
        bl, fw, bd, order = build_atom(name, Z, N)
        f0 = trM(bl, fw)
        parts_L = {}
        for k, typ, letter in bd:
            parts_L[(k, typ)] = math.log(f0 / trM(bl, fw + [letter]))
        all_L = math.log(f0 / trM(bl, fw + [b[2] for b in bd]))
        s = sum(parts_L.values())
        worst = max(worst, abs(all_L - s))
        L_tot[name] = all_L
        singles[name] = parts_L
        print(f"     {name:<9s} {''.join(order):<4s} bonds "
              f"{[t for _k, t in parts_L]}")
        for (k, typ), v in parts_L.items():
            print(f"        bond {k} ({typ}) alone: L = {v:.12f}")
        print(f"        all bonds:          L = {all_L:.12f}   sum = {s:.12f}"
              f"   |d| = {abs(all_L - s):.1e}")
    ok = worst < 1e-12
    assertions.append(("A4_log_defect_exactly_additive", ok,
                       f"max |L_all - sum L_single| = {worst:.2e} over 3 nuclei"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    print("\n  5. two per-bond-type constants carry everything")
    L_pn = L_tot["he3"] / 2
    L_nn = L_tot["tritium"] - L_pn
    agree = abs(L_tot["deuteron"] - L_pn)
    ok = agree < 1e-7 and L_nn > L_pn
    print(f"     L_pn = {L_pn:.12f}   (2H, one p-n bond: "
          f"{L_tot['deuteron']:.12f}, agree {agree:.1e})")
    print(f"     L_nn = {L_nn:.12f}   (from 3H = p-n + n-n)")
    print(f"     3He = 2 L_pn = {2 * L_pn:.9f} ; 3H = L_pn + L_nn = "
          f"{L_pn + L_nn:.9f}")
    print(f"     L_nn > L_pn, so 3H binds more than 3He — the right ordering")
    assertions.append(("A5_two_per_bond_constants", ok,
                       f"L_pn = {L_pn:.9f} (2H/3He agree to {agree:.1e}), "
                       f"L_nn = {L_nn:.9f}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. what it gets right and wrong against experiment ───────────
    print("\n  6. compared with experiment (read-only, nothing tuned)")
    b2 = float(AME_B_DEUTERON_MEV_VALIDATION)
    b3h = float(AME_B_TRITIUM_MEV_VALIDATION)
    b3he = float(AME_B_HE3_MEV_VALIDATION)
    r_mod_mirror = L_tot["tritium"] / L_tot["he3"]
    r_exp_mirror = b3h / b3he
    r_mod_a = L_tot["deuteron"] / L_tot["he3"]
    r_exp_a = b2 / b3he
    e1 = 100 * (r_mod_mirror / r_exp_mirror - 1)
    e2 = 100 * (r_mod_a / r_exp_a - 1)
    ok = (r_mod_mirror > 1) == (r_exp_mirror > 1) and abs(e1) < abs(e2)
    print(f"     mirror  L(3H)/L(3He) = {r_mod_mirror:.5f}   "
          f"B(3H)/B(3He) = {r_exp_mirror:.5f}   {e1:+.1f} %")
    print(f"     A-scale L(2H)/L(3He) = {r_mod_a:.5f}   "
          f"B(2H)/B(3He) = {r_exp_a:.5f}   {e2:+.1f} %")
    print(f"     ordering of the mirror pair is right and the ratio is within")
    print(f"     {abs(e1):.1f} %; the A = 2 vs A = 3 ratio is badly wrong — 0.5")
    print(f"     by construction (one bond against two). A bond-count law is")
    print(f"     not the whole story, and the second number is the one that")
    print(f"     matters for anyone tempted by the first.")
    assertions.append(("A6_mirror_right_a_scaling_wrong", ok,
                       f"mirror ratio {r_mod_mirror:.5f} vs {r_exp_mirror:.5f} "
                       f"({e1:+.1f}%); A-scale {r_mod_a:.5f} vs {r_exp_a:.5f} "
                       f"({e2:+.1f}%)"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  Putting the bonds back changes everything the last four probes")
    print("  concluded about binding being zero. The bond gives a -49 % mass")
    print("  defect at 2H with the right sign; the LP's rank-one degeneracy")
    print("  breaks (the two states no longer share a dual vertex); and")
    print("  L = log(tr_free/tr_atom) is EXACTLY additive over bonds, carried")
    print("  by two constants L_pn = 0.6768216 and L_nn = 0.9072623.")
    print("  It gets the mirror pair right — 3H binds more than 3He because")
    print("  n-n beats p-n — within 6.5 % on that ratio. It gets A = 2 against")
    print("  A = 3 badly wrong, 0.500 against 0.288, because a bond-count law")
    print("  makes 2H exactly half of 3He by construction. And the absolute")
    print("  scale is not a binding energy: 49 % against a physical 0.1 %,")
    print("  since these are dimensionless traces with no mass normalisation.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="scipy")
        wb.set_description(
            "Rebuilds the binding LP with the inter-nucleon bonds included, "
            "which the previous probes omitted. Corrects the prior turn: "
            "atom_gen_chains appends C(A,2) bonds but atom_braid_word_3A "
            "places only A-1 (adjacent chain, generator 3k+2), and the chain "
            "reading is the one the arity law c_atom = A+1 and Lean "
            "ClassicalTraceFloor rest on; the two builders disagree for every "
            "A >= 3. With the bond in, the deuteron's Markov trace drops from "
            "0.299015019 to 0.151968341, a -49.18% defect with the correct "
            "sign, and the free value reproduces tr_3(p) tr_3(n) to 6.1e-9. "
            "Rebuilding the positive-sector LP on a 72-word spanning set (36 "
            "product words plus their bond-translates, Gram rank 50) gives "
            "phi(free) = 0.429886497 and phi(atom) = 0.248443512, a gap of "
            "+0.181442985, and the two states no longer share a dual vertex "
            "(supports 2 and 3) where the bond-free LP had identical rank-one "
            "duals — which is exactly why every earlier gap was an algebraic "
            "zero. L = log(tr_free/tr_atom) is EXACTLY additive over bonds "
            "(residual 4.4e-16) with two per-type constants L_pn = "
            "0.676821592386 and L_nn = 0.907262271178. The law gets the mirror "
            "ordering right (3H > 3He, ratio 1.17022 against 1.09896, +6.5%) "
            "and the A-scaling badly wrong (2H/3He 0.500 against 0.288, +73%).")
        wb.add_data("bond_topology",
                    {"atom_gen_chains": "C(A,2)",
                     "atom_braid_word_3A": "A-1 (chain, gen 3k+2)",
                     "used_here": "chain", "counts": [list(r) for r in rows]})
        wb.add_data("deuteron_trace", {"free": f"{tf:.15f}", "atom": f"{ta:.15f}",
                                       "defect": f"{ta - tf:+.15f}",
                                       "rel_pct": f"{100 * (ta - tf) / tf:+.4f}"})
        wb.add_data("lp", {"basis": nb, "gram_rank": rank,
                           "phi_free": f"{pf:.12f}", "phi_atom": f"{pa:.12f}",
                           "gap": f"{pf - pa:+.12f}",
                           "dual_supports": [sf, sa], "duals_identical": same})
        wb.add_data("L_totals", {k: f"{v:.12f}" for k, v in L_tot.items()})
        wb.add_data("bond_constants", {"L_pn": f"{L_pn:.12f}",
                                       "L_nn": f"{L_nn:.12f}"})
        wb.add_data("additivity_residual", f"{worst:.3e}")
        wb.add_data("ratio_comparison",
                    {"mirror_model": f"{r_mod_mirror:.6f}",
                     "mirror_exp": f"{r_exp_mirror:.6f}",
                     "mirror_pct": f"{e1:+.2f}",
                     "a_scale_model": f"{r_mod_a:.6f}",
                     "a_scale_exp": f"{r_exp_a:.6f}",
                     "a_scale_pct": f"{e2:+.2f}"})
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "THE ABSOLUTE SCALE IS NOT A BINDING ENERGY. A 49% trace defect at "
            "2H sits three orders above the physical 0.1%. These are "
            "dimensionless multiplicative Markov traces; converting L into MeV "
            "requires the corpus's mass normalisation, which is deliberately "
            "not applied here. Only the two RATIOS in A6 are compared with "
            "experiment, and nothing is tuned to them.")
        wb.add_caveat(
            "THE A-SCALING FAILURE IS STRUCTURAL, not a precision issue. A "
            "bond-additive law with a chain topology makes 2H exactly half of "
            "3He (one bond against two) whatever the constants are, against an "
            "experimental 0.288. So bond-additivity cannot be the whole "
            "binding law; the mirror agreement at +6.5% should not be read as "
            "validating it. If the C(A,2) topology of atom_gen_chains were "
            "used instead the count would be 1 against 3, giving 0.333 — "
            "closer, but that topology contradicts the arity law.")
        wb.add_caveat(
            "SCOPE. A = 4 (he4) is not computed: H_12 has 77 partitions with "
            "Specht dimensions to 2673, and word products at that size are not "
            "tractable by the dense seminormal route used here. The three "
            "nuclei covered (2H, 3H, 3He) are enough to fix both per-bond "
            "constants and to test additivity, but not to test the law beyond "
            "two bonds.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
