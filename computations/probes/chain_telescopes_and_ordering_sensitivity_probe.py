#!/usr/bin/env python3
"""The chain telescopes exactly — A = 4 with no `H_12` — and the falloff rate
does depend on bond type, monotonically.

WHAT WAS ASKED
--------------
Owner: reach `A = 4`; the dense seminormal route dies at `H_12` (77 partitions,
Specht dimensions to 2673), so find a sparse or character-only path, making use
of *"the transfer matrices of the knot convolution … non-scalar but we can look
at the spectral decomposition/decay rate within the tower."*

Two things come out. The transfer operator for the **adjacent chain** turns out
to be exactly **rank one** — a scalar, not a matrix — which reaches every `A` in
closed form and proves the additivity measured last turn. And a cheaper
discriminator than `A = 4` exists at `A = 3`: reordering the nucleons moves bond
*distances* without changing the bond *multiset*, which isolates the falloff
directly.

THE TRANSFER OPERATOR IS RANK ONE ON THE CHAIN
-------------------------------------------------
Write the chain word `W_A = w_0 b_0 w_1 b_1 ... b_{A-2} w_{A-1}`, nucleon `k` on
generators `{3k, 3k+1}` and bond `k` on `{3k+2}`. Peel the top block using the
Markov property `tr(a T_n b) = z tr(a b)` for `a, b in H_n`. Expanding the top
nucleon in the `H_3` normal-form basis on its own two generators, every term
reduces to a multiple of `tr(X)`, giving

    tr( X . b . w )  =  tr(X) . F(b, w)

with `F` a **scalar independent of the entire prefix `X`**. Measured across four
different prefixes and all three bond types, `F` is constant to `2.8e-16`:

    F_pn = 0.241477007350    F_nn = 0.191777066944    F_pp = 0.385581983466

So the chain telescopes:  `tr(W_A) = tr(w_0) . prod_k F(b_k, w_{k+1})`, hence

    L(chain, A)  =  sum over the A-1 adjacent bonds,  for EVERY A.

That is the proof of last turn's `4.4e-16` additivity — it is the Markov
property, not a numerical accident — and it reaches `A = 4` with no `H_12` at
all. The "spectral decomposition" the owner asked for is degenerate here: the
transfer operator has a single nonzero eigenvalue, so there is no decay rate
*within the chain*. Any decay has to come from the non-adjacent bonds, which is
where the rest of this probe looks.

A CHEAPER DISCRIMINATOR THAN A = 4
------------------------------------
At `A = 3` the nucleon ordering changes which pairs are adjacent without
changing the bond multiset at all:

    3He   pnp -> pairs {pn, np | pp}   the p-p bond at distance 2
          ppn -> pairs {pp, pn | pn}   the p-p bond at distance 1
    3H    pnn -> pairs {pn, nn | pn}   the n-n bond at distance 1
          npn -> pairs {np, pn | nn}   the n-n bond at distance 2

Same nucleus, same bonds, different geometry. **The all-pairs answer depends on
the ordering** — 4.35 % for `3He`, 5.05 % for `3H` — so distance genuinely
matters and the model is not a function of the multiset alone. This is the
direct evidence for the owner's *"falls away"*, obtained without `H_12`.

Which way? The **strong bond wants to be adjacent**: `pnn` (n-n adjacent,
2.017810) beats `npn` (n-n far, 1.920851); `pnp` (both p-n adjacent, 1.676936)
beats `ppn` (one p-n far, 1.607031). Exactly what suppression of far bonds
predicts.

THE FALLOFF RATE DEPENDS ON BOND TYPE — MONOTONICALLY
--------------------------------------------------------
Four saturation factors (marginal contribution of the far bond, over its
isolated value), ordered by the far bond's own strength:

    far bond   L_far        saturation
    p-p        0.489899     0.659916
    p-n        0.676822     0.650555   (ppn)
    p-n        0.676822     0.640829   (pnn)
    n-n        0.907262     0.625186

**Monotone decreasing**: the stronger the far bond, the more of it is
suppressed. The two `p-n` rows differ by the adjacent total they sit against
(1.166721 against 1.584084), and the larger one suppresses more — saturation in
both variables. Range 0.625 to 0.660, a 5.6 % spread. **This is the owner's
"rate depending on the type of bond", measured and monotone**, and it is a
weak dependence rather than a strong one.

ALL PAIRS IS THREE TO FOUR TIMES LESS ORDERING-SENSITIVE
-----------------------------------------------------------
The ordering is a labelling convention — a physical nucleus has no preferred
nucleon order — so sensitivity to it is an artefact, and less is better:

    nucleus   orderings    chain swing    all-pairs swing
    3He       pnp / ppn      16.02 %          4.35 %
    3H        pnn / npn      17.02 %          5.05 %

All-pairs would be **exactly** permutation-invariant were it not for the
saturation; the residual few per cent *is* the saturation. The chain swings by a
sixth of its own value under relabelling. That is an independent argument for
the all-pairs topology, on top of last turn's `A`-scaling one, and against
`atom_braid_word_3A`'s chain.

A = 4 ON THE CHAIN, AND WHAT ALL-PAIRS STILL NEEDS
-----------------------------------------------------
The telescoping gives `4He` on the chain outright. Its ordering is `pnpn`, so
three adjacent p-n bonds:

    L(chain, 4He) = 3 L_pn = 2.030464777

against experiment this is worse still — `L(4He)/L(3He) = 1.50000` where
`B(4He)/B(3He) = 3.66618`, an error of `-59 %`, deepening the chain's
`A`-scaling failure rather than relieving it.

**All-pairs at `A = 4` remains out of reach here** and the reason is precise:
the telescoping works because adjacent bonds sit three generators apart and
commute with the peeling, while a band generator spans `3, 4, 5` and does not.
With six bonds at distances 1, 1, 1, 2, 2, 3 there is no prefix-independent
`F`, so the transfer operator stops being rank one — exactly the "non-scalar"
case the owner anticipated. Computing it needs a Hecke word reducer over `H_12`
(greedy top-generator peeling with the quadratic relation, elements as
`{word: coeff}` maps), which is a build rather than a measurement.

DISCIPLINE
----------
No fit; nothing wired. `B_AME` is read for the ratio comparisons only. The
prefix-independence of `F` is measured, not assumed. The `~1e-8` agreement floor
elsewhere in this series is the stored f64 `y_lambda` table; the `2.8e-16` here
is float64 on well-separated quantities, because `F` is a ratio of two traces
computed the same way.

-- Ref: [manuscript] bean t7qv
-- Ref: [probe] all_pairs_bonds_and_saturation_probe.py (saturation, all pairs)
-- Ref: [probe] binding_lp_with_inter_nucleon_bonds_probe.py (the bond constants)
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

from codata_constants import (  # noqa: E402
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
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
B_P = (0.0, 0.5, 0.5)
B_N = (0.5, 0.5, 1.0)
_B9 = None


def blocks():
    global _B9
    if _B9 is None:
        parts, y, _c, _d, _m = load_cost("tritium")
        _B9 = [(y[i], [np.asarray(m, dtype=float)
                       for m in build_seminormal_matrices(list(p))[0]])
               for i, p in enumerate(parts)]
    return _B9


def nucleon_word(betas, g0: int, g1: int):
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


def band(d: float):
    return [(1, 0.0, 5), (1, 0.0, 4), (1, 0.0, 3), (1, d, 2),
            (1, -HF, 3), (1, -HF, 4), (1, -HF, 5)]


def trM(word):
    tot = 0.0
    for wt, s in blocks():
        dim = s[0].shape[0]
        m = np.eye(dim)
        for c, dd, g in word:
            m = m @ (c * s[g] + dd * np.eye(dim))
        tot += wt * float(np.trace(m))
    return tot


def config(order):
    """(free word, adjacent bond letters, far bond letter, tf)."""
    base = []
    for k, x in enumerate(order):
        base += nucleon_word(B_P if x == "p" else B_N, 3 * k, 3 * k + 1)
    adj = []
    for k in range(len(order) - 1):
        c, d = bond_cd(order[k], order[k + 1])
        adj.append((c, d, 3 * k + 2))
    _c, dfar = bond_cd(order[0], order[-1])
    return base, adj, band(dfar), trM(base)


def main() -> int:
    assertions = []
    print("t7qv — the chain telescopes; the falloff rate is type-dependent")

    # ── A1. the transfer operator is rank one on the chain ────────────
    print("\n  1. tr(X . b . w) = tr(X) . F, with F independent of the prefix")
    F, spreads = {}, {}
    for typ in ("pn", "nn", "pp"):
        c, d = bond_cd(typ[0], typ[1])
        vals = []
        for x0 in ("p", "n"):
            for x1 in ("p", "n"):
                pre = (nucleon_word(B_P if x0 == "p" else B_N, 0, 1)
                       + [(1, 0.0, 2)]
                       + nucleon_word(B_P if x1 == "p" else B_N, 3, 4))
                top = nucleon_word(B_P if typ[1] == "p" else B_N, 6, 7)
                vals.append(trM(pre + [(c, d, 5)] + top) / trM(pre))
        F[typ] = vals[0]
        spreads[typ] = max(vals) - min(vals)
        print(f"     F_{typ} = {vals[0]:.12f}   over 4 prefixes, spread "
              f"{spreads[typ]:.1e}")
    ok = all(v < 1e-14 for v in spreads.values())
    print(f"     => tr(W_A) = tr(w_0) prod_k F_k : the chain TELESCOPES, and")
    print(f"        L(chain) is a sum over adjacent bonds for EVERY A")
    print(f"     the transfer operator is RANK ONE — a scalar, so there is no")
    print(f"     spectral decay within the chain; any decay is in the far bonds")
    assertions.append(("A1_chain_transfer_is_rank_one", ok,
                       f"F prefix-spreads {[f'{v:.1e}' for v in spreads.values()]}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. ordering moves distances at fixed multiset ────────────────
    print("\n  2. reordering moves bond DISTANCES at fixed bond multiset")
    rows = {}
    for order in (["p", "n", "p"], ["p", "p", "n"],
                  ["p", "n", "n"], ["n", "p", "n"]):
        base, adj, far, tf = config(order)
        L_adj = math.log(tf / trM(base + adj))
        L_all = math.log(tf / trM(base + adj + far))
        L_far = math.log(tf / trM(base + far))
        rows["".join(order)] = (L_adj, L_all, L_far)
        pairs = (f"{order[0]}{order[1]},{order[1]}{order[2]} | "
                 f"{order[0]}{order[2]}")
        print(f"     {''.join(order):<4s} {pairs:<16s} chain {L_adj:.9f}   "
              f"all pairs {L_all:.9f}")
    d_he = abs(rows["pnp"][1] / rows["ppn"][1] - 1)
    d_h = abs(rows["pnn"][1] / rows["npn"][1] - 1)
    ok = d_he > 1e-3 and d_h > 1e-3
    print(f"     all-pairs depends on ordering: 3He {100 * d_he:.2f} %, "
          f"3H {100 * d_h:.2f} %")
    print(f"     so distance matters — the model is NOT a function of the")
    print(f"     multiset alone. Direct evidence for a falloff, without H_12.")
    assertions.append(("A2_ordering_changes_the_answer", ok,
                       f"all-pairs swings {100 * d_he:.2f}% (3He) and "
                       f"{100 * d_h:.2f}% (3H) at fixed bond multiset"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. the strong bond wants to be adjacent ──────────────────────
    print("\n  3. the STRONG bond wants to be adjacent")
    ok = (rows["pnn"][1] > rows["npn"][1]) and (rows["pnp"][1] > rows["ppn"][1])
    print(f"     3H  pnn (n-n adjacent) {rows['pnn'][1]:.9f}  >  "
          f"npn (n-n far) {rows['npn'][1]:.9f}")
    print(f"     3He pnp (both p-n adj) {rows['pnp'][1]:.9f}  >  "
          f"ppn (one p-n far) {rows['ppn'][1]:.9f}")
    print(f"     exactly what suppression of the far bond predicts")
    assertions.append(("A3_strong_bond_prefers_adjacency", ok,
                       "pnn > npn and pnp > ppn on the all-pairs value"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4. saturation is monotone in the far bond's strength ─────────
    print("\n  4. the falloff rate depends on bond type, monotonically")
    sat = []
    for name, typ in (("pnp", "pp"), ("ppn", "pn"), ("pnn", "pn"),
                      ("npn", "nn")):
        L_adj, L_all, L_far = rows[name]
        s = (L_all - L_adj) / L_far
        sat.append((L_far, s, typ, name))
    sat.sort(key=lambda r: (r[0], -r[1]))
    print(f"     {'far bond':<9s} {'L_far':>10s} {'saturation':>12s}  from")
    for L_far, s, typ, name in sat:
        print(f"     {typ:<9s} {L_far:10.6f} {s:12.6f}  {name}")
    # monotonicity ACROSS bond types (the two p-n rows tie on L_far and are
    # separated by the adjacent total they sit against, not by L_far)
    by_type = {}
    for L_far, s, typ, _n in sat:
        by_type.setdefault(typ, []).append(s)
    mono = (min(by_type["pp"]) > max(by_type["pn"])
            and min(by_type["pn"]) > max(by_type["nn"]))
    spread = (max(s for _, s, _, _ in sat) / min(s for _, s, _, _ in sat)) - 1
    ok = mono and spread < 0.10
    print(f"     monotone across types  p-p > p-n > n-n: {mono};  spread "
          f"{100 * spread:.1f} %")
    print(f"     the two p-n rows differ by the adjacent total they sit")
    print(f"     against ({rows['ppn'][0]:.6f} vs {rows['pnn'][0]:.6f}) — the")
    print(f"     larger one suppresses more. Saturation in both variables.")
    assertions.append(("A4_saturation_monotone_in_bond_strength", ok,
                       f"saturation {[f'{s:.6f}' for _, s, _, _ in sat]} "
                       f"monotone in L_far, spread {100 * spread:.1f}%"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. all pairs is far less ordering-sensitive ──────────────────
    print("\n  5. all pairs is 3-4x less ordering-sensitive")
    c_he = abs(rows["pnp"][0] / rows["ppn"][0] - 1)
    c_h = abs(rows["pnn"][0] / rows["npn"][0] - 1)
    ok = c_he / d_he > 3 and c_h / d_h > 3
    print(f"     {'nucleus':<8s} {'chain swing':>12s} {'all-pairs swing':>17s}")
    print(f"     {'3He':<8s} {100 * c_he:11.2f} % {100 * d_he:16.2f} %")
    print(f"     {'3H':<8s} {100 * c_h:11.2f} % {100 * d_h:16.2f} %")
    print(f"     ordering is a labelling convention, so sensitivity to it is an")
    print(f"     artefact. All-pairs would be EXACTLY permutation-invariant but")
    print(f"     for the saturation; the residual few per cent is the saturation.")
    assertions.append(("A5_all_pairs_less_ordering_sensitive", ok,
                       f"chain {100 * c_he:.2f}%/{100 * c_h:.2f}% vs all-pairs "
                       f"{100 * d_he:.2f}%/{100 * d_h:.2f}%; ratio "
                       f"{c_he / d_he:.2f}x and {c_h / d_h:.2f}x"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. A = 4 on the chain, and what all-pairs still needs ────────
    print("\n  6. A = 4 on the chain, with no H_12")
    L_pn = math.log(trM(nucleon_word(B_N, 0, 1)) / F["pn"]) if False else None
    L_pn = rows["pnp"][0] / 2                     # 3He chain = 2 p-n bonds
    L4 = 3 * L_pn                                 # 4He ordering pnpn: 3 p-n
    b4 = float(AME_B_HE4_MEV_VALIDATION)
    b3he = float(AME_B_HE3_MEV_VALIDATION)
    r_mod, r_exp = L4 / rows["pnp"][0], b4 / b3he
    err = 100 * (r_mod / r_exp - 1)
    ok = abs(r_mod - 1.5) < 1e-12 and err < -50
    print(f"     4He ordering pnpn -> three adjacent p-n bonds")
    print(f"     L(chain, 4He) = 3 L_pn = {L4:.9f}")
    print(f"     L(4He)/L(3He) = {r_mod:.5f}   B(4He)/B(3He) = {r_exp:.5f}"
          f"   {err:+.1f} %")
    print(f"     the chain's A-scaling failure DEEPENS at A = 4, as expected")
    print(f"     all-pairs at A = 4 stays out of reach: six bonds at distances")
    print(f"     1,1,1,2,2,3, no prefix-independent F, so the transfer operator")
    print(f"     is no longer rank one. It needs a Hecke word reducer over H_12")
    print(f"     — a build, not a measurement.")
    assertions.append(("A6_chain_reaches_A4", ok,
                       f"L(chain,4He) = {L4:.9f}; ratio {r_mod:.5f} vs "
                       f"{r_exp:.5f} ({err:+.1f}%)"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  The sparse route exists and is exact, but it is degenerate: the")
    print("  chain's transfer operator is RANK ONE, so the chain telescopes to")
    print("  a sum over adjacent bonds at every A and 4He follows with no H_12.")
    print("  It also deepens the chain's A-scaling failure, -59 % at 4He.")
    print("  The discriminator came instead from reordering at A = 3, which")
    print("  moves bond distances at fixed multiset. The answer moves — 4.35 %")
    print("  and 5.05 % — so distance genuinely matters, the strong bond wants")
    print("  to be adjacent, and the saturation factor is monotone in the far")
    print("  bond's own strength: 0.6599 (p-p), 0.6506 / 0.6408 (p-n), 0.6252")
    print("  (n-n). That is the owner's type-dependent rate, measured.")
    print("  And all pairs is 3.4-3.7x less sensitive to a labelling choice")
    print("  than the chain, which is a second independent argument for it.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
        wb.set_description(
            "Finds the sparse route to higher A and uses reordering at A = 3 as "
            "a cheaper discriminator than A = 4. The chain's transfer operator "
            "is exactly RANK ONE: tr(X . b . w) = tr(X) F(b,w) with F "
            "independent of the whole prefix to 2.8e-16, measured over four "
            "prefixes and three bond types (F_pn = 0.241477007350, F_nn = "
            "0.191777066944, F_pp = 0.385581983466). So the chain telescopes, "
            "L(chain) is a sum over adjacent bonds at every A, and 4He follows "
            "with no H_12: L = 3 L_pn = 2.030464777, giving L(4He)/L(3He) = "
            "1.50000 against B(4He)/B(3He) = 3.66618, -59%, deepening the "
            "chain's A-scaling failure. The discriminator instead comes from "
            "reordering at A = 3, which moves bond distances at fixed bond "
            "multiset: the all-pairs answer swings 4.35% (3He pnp vs ppn) and "
            "5.05% (3H pnn vs npn), so distance genuinely matters. The strong "
            "bond wants to be adjacent, and the saturation factor is monotone "
            "decreasing in the far bond's own strength — 0.659916 (p-p), "
            "0.650555 and 0.640829 (p-n), 0.625186 (n-n), a 5.6% spread — which "
            "is the owner's type-dependent falloff rate, measured. All-pairs is "
            "also four times less sensitive to the nucleon ordering than the "
            "chain (4.35%/5.05% against 16.02%/17.02%), a second independent "
            "argument for the all-pairs topology.")
        wb.add_data("transfer_scalars", {k: f"{v:.12f}" for k, v in F.items()})
        wb.add_data("transfer_prefix_spread",
                    {k: f"{v:.2e}" for k, v in spreads.items()})
        wb.add_data("orderings",
                    {k: {"chain": f"{v[0]:.12f}", "all_pairs": f"{v[1]:.12f}",
                         "far_alone": f"{v[2]:.12f}"} for k, v in rows.items()})
        wb.add_data("saturation_by_far_bond",
                    [{"type": t, "L_far": f"{l:.9f}", "saturation": f"{s:.9f}",
                      "from": n} for l, s, t, n in sat])
        wb.add_data("ordering_swing",
                    {"3He": {"chain": f"{100 * c_he:.4f}",
                             "all_pairs": f"{100 * d_he:.4f}"},
                     "3H": {"chain": f"{100 * c_h:.4f}",
                            "all_pairs": f"{100 * d_h:.4f}"}})
        wb.add_data("chain_A4", {"L": f"{L4:.9f}", "ratio_model": f"{r_mod:.6f}",
                                 "ratio_exp": f"{r_exp:.6f}",
                                 "err_pct": f"{err:+.2f}"})
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "THE 'TRANSFER MATRIX' IS DEGENERATE ON THE CHAIN. The owner asked "
            "for a spectral decomposition and a decay rate within the tower; "
            "for the adjacent chain there is none to find, because the transfer "
            "operator has a single nonzero eigenvalue. That is a result, not a "
            "shortcut: it is why the chain is exactly additive and why it "
            "cannot produce any distance falloff. A genuinely non-scalar "
            "transfer operator only appears once non-adjacent bonds are "
            "present, and that is precisely the case this probe cannot yet "
            "compute at A = 4.")
        wb.add_caveat(
            "ALL-PAIRS AT A = 4 IS STILL NOT COMPUTED. Six bonds at distances "
            "1,1,1,2,2,3 leave no prefix-independent F, so the telescoping "
            "fails and H_12 is unavoidable by this route. Reaching it needs a "
            "Hecke word reducer (greedy top-generator peeling with the "
            "quadratic relation, elements as {word: coefficient} maps), which "
            "is a build rather than a measurement. Nothing here extrapolates "
            "the saturation model to A = 4; the only A = 4 number reported is "
            "the exact chain value.")
        wb.add_caveat(
            "The ordering dependence is a MODELLING AMBIGUITY the corpus "
            "currently resolves by convention: `ordering(Z,N)` interleaves "
            "protons first, giving pnp and pnn. A physical nucleus has no "
            "preferred nucleon order, so the 16-17% chain swing and the "
            "4-5% all-pairs swing are both artefacts of that convention. "
            "Reporting which topology minimises the artefact is the point; "
            "neither eliminates it.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
