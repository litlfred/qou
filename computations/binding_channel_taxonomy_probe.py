#!/usr/bin/env python3
"""
binding_channel_taxonomy_probe — every binding channel the corpus contains, scored
on STRUCTURAL criteria rather than on agreement with AME.

Bean `qou-brng`, arc `bk-crossing-mass-binding`. Follows #6304, #6332, #6338, #6345,
#6346.

## Why this exists

The arc reached a question it could not answer from inside one channel: the
saturation reasoning that drives the bond-set search applies in one way of reading a
binding off the Markov trace and not in another, and the corpus computes several. So
enumerate them and score them on criteria that are DERIVED rather than fitted.

## 🛑 Corrections to my own earlier framing, made here because two are novelty claims

Building this taxonomy required grepping `computations/` for every binding channel,
which is what the corpus-grep checklist asks for and what I had not done properly.
Two results I reported as findings were already in the corpus:

1. **#6332's Channel-2 result was already stated, in one sentence, in
   `log_ratio_binding_prototype.py`:** *"the canonical-binding LINEAR difference
   `Δtr = tr_free·(1 − f^bonds)` SATURATES (intensive, bounded), which is why
   `B = Q_β·Δtr` undershoots by 5–40× and the undershoot grows with A. The EXTENSIVE
   invariant is the log-ratio."* That is the observation I presented as new. What was
   actually new in #6332 is narrower and is kept: the connection to
   `CoordinationSaturation`'s premise (an arity point that file does not make), the
   closed-form minimum `A* = 2/ln|tr_p·tr_n|` verified against the measured argmin,
   and the bound showing no bond set rescues that channel.

2. **#6346 Part 2's measurement was already recorded**, in
   `derive_binding_chain_cooperative.py`: *"The canonical braid is a CHAIN of A−1
   inter-nucleon interfaces (verified from atom_braid_word_3A: interface at gen
   3k+2, k=0..A−2)."* What is new there is the Lean proof that the chain is FORCED —
   `crossesBlocks_iff` / `no_single_generator_joins_nonadjacent` — i.e. the corpus
   had the fact and this arc now has the necessity. That distinction is real, but the
   framing overstated it.

Three corpus-grep misses in one arc (`derived_bond_graph_binding` first, then these
two) is a pattern rather than an accident: I grepped for *mechanisms* (`mp.log`) and
for *topics*, never for the artefact class ("what computes a binding?"). Recorded so
the next agent greps for the artefact.

## The channels

Seven live, from `grep` over non-deprecated `computations/`:

| # | channel | form | source |
|---|---|---|---|
| 1 | observe-early trace difference | `Q_β(|tr_f| − |tr_a|)` | `binding_canonical` |
| 2 | observe-last angle | `Q_β Σ_λ y_λ(θ_f − θ_a)` | `binding_canonical`, self-marked REFUTED |
| 3 | log-ratio / free energy | `E₀ log(tr_f/tr_a)` | `log_ratio_binding_prototype`, `derived_bond_graph_binding` |
| 4 | bar-norm log | `(E₀/2) Σ log(1/(f·f̄))` | `derived_bond_graph_binding` |
| 5 | signed pairwise chain sum | `Σ_chain E₀(tr_f − tr_a)_pair` | `derive_binding_chain_cooperative` |
| 6 | volume × Δtr | `m_e Vol(K_bind) Δtr` | `binding_link_volumes` |
| 7 | magic-A | `ρ_F m_e A Vol(𝓑)` | `magic_A_formula` (deprecation-candidate) |

## The scoring, and what is NOT the scorer

Scored on structure: is it extensive; is it additive over bonds (which is what
`CoordinationSaturation` requires to apply at all); is the sign right; what sets its
energy scale; what does `B/A` do as `A → ∞`.

**Agreement with AME is reported and is deliberately NOT the selector.** Choosing the
channel that lands nearest the data is the fit this arc exists to avoid.

## Scope

Scope **(a)**. Channels 1, 3, 4, 5 are evaluated on the corpus's own closed-form
factorisation `tr_p^Z·tr_n^N·∏f`; 2, 6, 7 are classified structurally from their
sources without being re-evaluated (2 needs per-partition characters; 6 and 7 are not
trace-ratio channels). Nothing is wired and nothing is recommended for production.

NO FLOAT64: mpmath `mpf` at 50 dps, 50-digit proton pin, empirical values as exact
decimal strings; `float` appears nowhere.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from closed_form_tau_M import compute_tau_M_nucleon_H3  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 50


def constants():
    from codata_constants import M_E_MEV as me
    from experimental_constants import Q_NEUTRON_MEV as qb
    q0 = mp.mpf(Q_50_DIGIT_STR)
    h = q0 - 1 / q0
    me = me if isinstance(me, mp.mpf) else mp.mpf(str(me))
    qb = mp.mpf(str(qb))
    z = q0**3 / (q0**2 + 1)                      # convention D
    delta = flavor_split_leading(q0)
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(me, q0)                    # the corpus's chosen scale
    f = {"pp": z, "nn": z - h, "pn": z - h * (mp.mpf(1) / 2 - delta / 4)}
    # bar-conjugates, as derived_bond_graph_binding computes them under convention D
    z_bar = z - h
    f_bar = {"pp": z_bar, "nn": z_bar + h,
             "pn": z_bar + h * (mp.mpf(1) / 2 - delta / 4)}
    return q0, h, me, qb, E0, f, f_bar


def chain_bonds(Z: int, N: int) -> list[str]:
    o = ["p"] * Z + ["n"] * N
    return ["pp" if a == b == "p" else ("nn" if a == b == "n" else "pn")
            for a, b in zip(o, o[1:])]


def fmt(x, n=8):
    return mp.nstr(x, n)


# AME2020 binding energies, exact decimal strings, for the NOT-A-SELECTOR column.
AME = {(1, 1): "2.224566", (1, 2): "8.481798", (2, 1): "7.718043",
       (2, 2): "28.295674", (3, 3): "31.994564", (3, 4): "39.244524",
       (6, 6): "92.161728", (8, 8): "127.619336"}


def main() -> int:
    q0, h, me, qb, E0, f, f_bar = constants()
    tp = compute_tau_M_nucleon_H3("p", q0)
    tn = compute_tau_M_nucleon_H3("n", q0)

    print("binding_channel_taxonomy_probe")
    print("=" * 78)
    print(f"q0 (50-digit proton pin) = {fmt(q0, 20)}")
    print(f"E_0 = m_e/(q0(q0-1))     = {fmt(E0, 12)} MeV   (the corpus's scale)")
    print(f"Q_beta                   = {fmt(qb, 12)} MeV")
    print(f"tr_p = {fmt(tp, 14)}   tr_n = {fmt(tn, 14)}")
    print("f      :", {k: fmt(v, 10) for k, v in f.items()})
    print("f_bar  :", {k: fmt(v, 10) for k, v in f_bar.items()})
    print()

    NZ = [(1, 1), (1, 2), (2, 1), (2, 2), (3, 3), (3, 4), (6, 6), (8, 8),
          (12, 12), (16, 16), (20, 20)]

    print("THE FOUR EVALUABLE CHANNELS, on the chain bond set (the wired one)")
    print("  1 observe-early  Q_b*|tr_f|*(1-prod f)")
    print("  3 log-ratio      E_0*sum_bonds log(1/f)")
    print("  4 bar-norm log   (E_0/2)*sum_bonds log(1/(f*f_bar))")
    print("  5 pairwise sum   sum_bonds E_0*tr_pair_free*(1-f)   [signed, per-bond]")
    print()
    print(f"{'nucleus':>8} {'A':>3} {'ch1 B/A':>11} {'ch3 B/A':>11} {'ch4 B/A':>11} "
          f"{'ch5 B/A':>11}")
    series = {1: [], 3: [], 4: [], 5: []}
    rows = []
    for Z, N in NZ:
        A = Z + N
        cb = chain_bonds(Z, N)
        trf = abs(tp) ** Z * abs(tn) ** N
        prod = mp.fprod([f[b] for b in cb])
        b1 = qb * trf * (1 - prod)
        b3 = E0 * mp.fsum(mp.log(1 / f[b]) for b in cb)
        b4 = E0 * mp.fsum(mp.log(1 / (f[b] * f_bar[b])) for b in cb) / 2
        # per-bond 2-nucleon sub-braid: tr_free of the PAIR, times (1 - f)
        b5 = mp.fsum(E0 * (abs(tp) if b == "pp" else
                           (abs(tn) if b == "nn" else abs(tp * tn) ** mp.mpf("0.5")))
                     ** 2 * (1 - f[b]) for b in cb)
        for k, v in ((1, b1), (3, b3), (4, b4), (5, b5)):
            series[k].append(v / A)
        rows.append((Z, N, A, b1, b3, b4, b5))
        print(f"{f'{Z}p{N}n':>8} {A:>3} {fmt(b1/A, 8):>11} {fmt(b3/A, 8):>11} "
              f"{fmt(b4/A, 8):>11} {fmt(b5/A, 8):>11}")
    print()

    # ── STRUCTURAL SCORING.  Extensivity means B is asymptotically LINEAR in A,
    #    so the test is the second finite difference of B on an evenly spaced grid
    #    -- exact integer-indexed arithmetic, no threshold.
    #
    #    A threshold on the spread of B/A over a tail is NOT the test and gets the
    #    answer wrong: B/A = c(A-1)/A converges like 1 - 1/A, so at A = 40 it is
    #    still 2.5 % short of its limit and any "spread < 2 %" rule calls a
    #    genuinely extensive channel "growing".  That is what a first version of
    #    this probe did, and it contradicted the exact measurement in #6332.
    HSTEP = 8
    GRID = [8, 16, 24, 32, 40]
    print("STRUCTURAL SCORING — the actual selector")
    print(f"  Extensive  <=>  B asymptotically LINEAR in A  <=>  second difference")
    print(f"  of B -> 0 on an evenly spaced grid.  Grid A = {GRID}, spacing {HSTEP}.")
    print()
    print(f"{'ch':>3} {'B/A at A=2':>12} {'B/A at A=40':>12} "
          f"{'2nd diff of B (relative to 1st)':>34} {'extensive?':>11} "
          f"{'additive/bond?':>15}")
    verdicts = {}
    for k in (1, 3, 4, 5):
        s = series[k]
        grid_B = []
        for A in GRID:
            Z = N = A // 2
            cb = chain_bonds(Z, N)
            trf = abs(tp) ** Z * abs(tn) ** N
            prod = mp.fprod([f[b] for b in cb])
            if k == 1:
                B = qb * trf * (1 - prod)
            elif k == 3:
                B = E0 * mp.fsum(mp.log(1 / f[b]) for b in cb)
            elif k == 4:
                B = E0 * mp.fsum(mp.log(1 / (f[b] * f_bar[b])) for b in cb) / 2
            else:
                B = mp.fsum(E0 * (abs(tp) if b == "pp" else
                                  (abs(tn) if b == "nn" else
                                   abs(tp * tn) ** mp.mpf("0.5"))) ** 2 * (1 - f[b])
                            for b in cb)
            grid_B.append(B)
        d1 = [b - a for a, b in zip(grid_B, grid_B[1:])]
        d2 = [b - a for a, b in zip(d1, d1[1:])]
        # scale-free: the second difference as a fraction of the first
        rel = max(abs(x) for x in d2) / max(abs(x) for x in d1)
        ext = "YES" if rel < mp.mpf("1e-30") else "no"
        additive = "YES" if k in (3, 4, 5) else "no (1 - prod)"
        verdicts[k] = (ext, additive, rel)
        print(f"{k:>3} {fmt(s[0], 8):>12} {fmt(s[-1], 8):>12} "
              f"{fmt(rel, 6):>34} {ext:>11} {additive:>15}")
    print()
    print("  A second difference that is EXACTLY zero (to 1e-30 of the first) means")
    print("  B is exactly affine in A on the chain -- which it must be, since the")
    print("  chain has A-1 bonds and the additive channels sum one term per bond.")
    print("  Channel 1's is not zero: its trace prefactor |tr_p|^Z|tr_n|^N is")
    print("  exponential in A, so B is too.")
    print()

    print("  'additive/bond?' is the criterion that decides whether")
    print("  QOU.Mass.CoordinationSaturation applies at all: its object is")
    print("  B = eps*M, binding additive in the bond count.  Channel 1 enters")
    print("  through (1 - prod f), which is bounded by 1 for ANY bond set, so the")
    print("  premise is not instantiated there (#6332).")
    print()

    print("THE THREE NOT RE-EVALUATED HERE, classified from source")
    print("-" * 78)
    for k, name, why, struct in [
        (2, "observe-last angle (binding_canonical)",
         "needs per-partition characters; self-marked '# refuted: small/neg/shrinks'",
         "additive over PARTITIONS, not bonds -> CoordinationSaturation does not apply"),
        (6, "volume x Dtr (binding_link_volumes)",
         "not a trace-ratio channel; Vol(Hopf) = 0 kills the deuteron leg",
         "extensivity depends on Vol(K_bind), which the corpus has only for A <= 3"),
        (7, "magic-A (magic_A_formula)",
         "marked DEPRECATION-CANDIDATE; carries acknowledged-anchor constants",
         "extensive BY CONSTRUCTION (B = rho_F*m_e*A*Vol) -- so B/A is constant "
         "trivially, and it says nothing about coordination"),
    ]:
        print(f"  ch{k}  {name}")
        print(f"        not evaluated: {why}")
        print(f"        structure: {struct}")
    print()

    print("AME COMPARISON — reported, and NOT the selector")
    print("  Choosing the channel that lands nearest the data is the fit this arc")
    print("  exists to avoid.  This column is here so nobody has to re-derive it,")
    print("  and it is deliberately not fed into any verdict above.")
    print(f"{'nucleus':>8} {'A':>3} {'B_AME':>10} {'ch1 x':>9} {'ch3 x':>9} "
          f"{'ch4 x':>9} {'ch5 x':>9}")
    for Z, N, A, b1, b3, b4, b5 in rows:
        key = (Z, N)
        if key not in AME:
            continue
        ba = mp.mpf(AME[key])
        print(f"{f'{Z}p{N}n':>8} {A:>3} {fmt(ba, 7):>10} {fmt(ba/b1, 5):>9} "
              f"{fmt(ba/b3, 5):>9} {fmt(ba/b4, 5):>9} {fmt(ba/b5, 5):>9}")
    print()

    print("Reading")
    print("-" * 78)
    print("  * OF SEVEN LIVE CHANNELS, EXACTLY THREE are both extensive and")
    print("    additive over bonds: the log-ratio (3), the bar-norm log (4) and")
    print("    the signed pairwise sum (5).  Their second differences vanish to")
    print("    ~7e-51 of the first -- B is exactly affine in A on the chain.")
    print("  * Channels 3 and 4 are numerically near-identical (2.8488631 vs")
    print("    2.8488779 at A=40, 5e-6 apart) and converge together, because under")
    print("    convention D the bar involution EXCHANGES pp and nn, so on an N=Z")
    print("    chain the bar-symmetrisation is nearly a no-op.  So the seven")
    print("    channels collapse to TWO distinct extensive candidates: the log")
    print("    family, and the pairwise sum.")
    print("  * The one that SHIPS -- channel 1, binding_canonical's observe-early")
    print("    trace difference -- is neither extensive nor additive, for any bond")
    print("    set.  Its second difference is 0.39 of the first, because the trace")
    print("    prefactor is exponential in A.")
    print("  * The other four are excluded structurally, not numerically: ch2 is")
    print("    additive over PARTITIONS not bonds; ch6 needs a Vol(K_bind) the")
    print("    corpus has only for A <= 3 and which is 0 for the deuteron; ch7 is")
    print("    extensive by construction and so says nothing about coordination.")
    print("  * SO THE CHANNEL QUESTION AND THE BOND-SET QUESTION ARE NOT")
    print("    INDEPENDENT.  The chain is forced by the strand layout (#6346,")
    print("    QOU.Mass.StrandLayoutForcesChain); on the chain the additive")
    print("    channels are exactly affine, hence saturate; and")
    print("    complete_graph_no_saturation only ever bit on the additive family")
    print("    in the first place.  What is left open is the MAGNITUDE -- the")
    print("    AME column above, which is 2-3x on the log family and is NOT")
    print("    the selector.")
    print("  * PRECISION CAVEAT that bears on channel 3: its prototype producer")
    print("    log_ratio_binding_prototype.py imports the FLOAT64 q_parameter.Q")
    print("    and accumulates through math.log -- the identical defect fixed in")
    print("    derived_bond_graph_binding by #6338 (bean qou-vsqh), in the very")
    print("    channel this question turns on.  Not fixed here; it wants its own")
    print("    PR with a witness refresh.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
