#!/usr/bin/env python3
"""
binding_channel_saturation_probe — WHICH CHANNEL is the saturation question asked in,
and does the cited exclusion apply to the channel the live producer uses?

Bean `qou-brng`, arc `bk-crossing-mass-binding`.

## The arity question

`QOU.Mass.CoordinationSaturation.complete_graph_no_saturation` (sorry-free, on `main`)
excludes the complete graph. Read its statement, not its headline:

    perNucleonComplete ε A := ε * C(A,2) / A
    complete_graph_no_saturation : 0 < ε → ∀ B, ∃ A, B < perNucleonComplete ε A

The object is `B = ε · M` — binding **ADDITIVE** in the bond count `M`, with a
uniform per-bond `ε`. That is what is excluded.

Two live channels read a binding off the multiplicative trace
`tr_M(𝓑_K) = tr_p^Z · tr_n^N · ∏_bonds f_i(q)`, and they are different functions
of the bond count `M`:

* **free energy** — `derived_bond_graph_binding.py:170-171` computes
  `B = E₀·Σ_bonds log(1/f_bond)` for the chain and for the complete graph. That IS
  `ε·M`, so `complete_graph_no_saturation`'s premise is instantiated here.
* **observe-early trace difference** — `binding_canonical.py:534` computes
  `B_pred = Q_β·(|tr_free| − |tr_atom|) = Q_β·|tr_free|·(1 − ∏ f_i)`. Here the bond
  count enters through `1 − ∏`, which is bounded by 1 whatever `M` is, so the
  premise is NOT instantiated.

So whether the exclusion bites is not a matter of interpretation — it depends on
which channel the binding is read in, and that is measurable. AGENTS.md §"Grep the
claim SHAPE, not only the topic": a conditional lemma proves the implication, never
the premise.

Three things this docstring got wrong on the first pass, corrected here because the
errors are the kind that propagate:

1. `binding_canonical`'s third form `B_late` is **not** a log channel. It is
   `Q_β·Σ_λ y_λ(θ_free[λ] − θ_atom[λ])` with `θ = acos(χ/dim)` or `acosh(|χ|/dim)`
   — an ANGLE per Wedderburn block, summed over partitions rather than over bonds.
   Its `# refuted: small/neg/shrinks` note says nothing about the free-energy
   channel.
2. The free-energy channel is **live**, not deprecated, and
   `derived_bond_graph_binding` already runs exactly the chain-vs-complete
   comparison this probe's Channel 1 reproduces. Channel 1 here is an independent
   re-derivation and is cited as such, not offered as new.
3. `binding_canonical` calls `atom_braid_word_3A(include_inter=True)`, which is the
   **chain** (`A−1` bonds), not the complete graph. So it is not the producer the
   complete-graph exclusion is about; `build_atom_nf` / `build_atom_nf_sym` is.
   The channel finding below is about the CHANNEL and holds for either bond set.

## What is measured

For both bond sets (complete `C(A,2)`, chain `A−1`), in both channels:

  * **free-energy channel**   −log(∏ f) / A   = Σ_bonds (−log f) / A
  * **observe-early channel** Q_β·|tr_free|·(1 − ∏ f) / A

and the constituent factor `|tr_free| = |tr_p|^Z·|tr_n|^N` on its own, because if
that term is not itself bounded then the bond set is not what decides saturation.

## Scope

Scope **(a)**. This measures which channel the exclusion applies in. It does not
propose a bond set, does not wire anything, and does not claim the physics needs
either. `ε`, `Q_β` and the two nucleon traces are read from the corpus, not fitted.

NO FLOAT64: mpmath `mpf` at 50 dps throughout; `float` appears nowhere. Proton pin.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from closed_form_tau_M import (  # noqa: E402
    markov_z,
    hecke_h,
    compute_tau_M_nucleon_H3,
)
from _li_2_q_util import flavor_split_leading  # noqa: E402
from q_parameter import q_at  # noqa: E402

mp.mp.dps = 50


def bond_factors(q: mp.mpf) -> dict[str, mp.mpf]:
    z, h, delta = markov_z(q), hecke_h(q), flavor_split_leading(q)
    return {"pp": z, "nn": z - h, "pn": z - h * (mp.mpf(1) / 2 - delta / 4)}


def canonical_ordering(Z: int, N: int) -> list[str]:
    """The ordering closed_form_ratio hardcodes."""
    return ["p"] * Z + ["n"] * N


def kind(a: str, b: str) -> str:
    return "pp" if a == b == "p" else ("nn" if a == b == "n" else "pn")


def bonds_of(Z: int, N: int, which: str) -> list[str]:
    """The bond kinds of the chosen bond set, on the canonical ordering."""
    o = canonical_ordering(Z, N)
    A = Z + N
    if which == "chain":
        return [kind(o[i], o[i + 1]) for i in range(A - 1)]
    if which == "complete":
        return [kind(o[i], o[j]) for j in range(A) for i in range(j)]
    raise ValueError(which)


def fmt(x, n=10):
    return mp.nstr(x, n)


def main() -> int:
    q = q_at()
    F = bond_factors(q)
    tau_p = compute_tau_M_nucleon_H3("p", q)
    tau_n = compute_tau_M_nucleon_H3("n", q)
    # Q_beta only sets the MeV scale; it is a positive constant and cannot change
    # whether a sequence is bounded, so the channel comparison does not depend on it.
    QB = mp.mpf(1)

    print("binding_channel_saturation_probe")
    print("=" * 78)
    print(f"q0 (proton pin)          = {fmt(q, 20)}")
    print(f"f_pp = z                 = {fmt(F['pp'], 20)}")
    print(f"f_pn = z - h(1/2 - d/4)  = {fmt(F['pn'], 20)}")
    print(f"f_nn = z - h             = {fmt(F['nn'], 20)}")
    print(f"tr_M^3(proton)           = {fmt(tau_p, 20)}")
    print(f"tr_M^3(neutron)          = {fmt(tau_n, 20)}")
    print()
    print("  Every bond factor is in (0,1), so -log f > 0: the free-energy channel")
    print("  has a positive per-bond cost, which is the `eps > 0` hypothesis of")
    print("  complete_graph_no_saturation.  Checked:")
    for k, v in F.items():
        print(f"    0 < f_{k} < 1 : {bool(0 < v < 1)}   -log f_{k} = {fmt(-mp.log(v), 12)}")
    print()

    NZ = [(1, 1), (2, 2), (3, 3), (4, 4), (6, 6), (8, 8), (10, 10), (12, 12),
          (16, 16), (20, 20)]

    print("CHANNEL 1 — free energy:  -log(prod f) / A  =  sum_bonds (-log f) / A")
    print("  This is exactly `eps * M / A`, the object CoordinationSaturation covers.")
    print(f"{'A':>4} {'M_chain':>8} {'M_compl':>9} {'chain -logP/A':>15} "
          f"{'compl -logP/A':>15}")
    fe_chain, fe_compl = [], []
    for Z, N in NZ:
        A = Z + N
        bc, bk = bonds_of(Z, N, "chain"), bonds_of(Z, N, "complete")
        lc = mp.fsum(-mp.log(F[b]) for b in bc) / A
        lk = mp.fsum(-mp.log(F[b]) for b in bk) / A
        fe_chain.append(lc)
        fe_compl.append(lk)
        print(f"{A:>4} {len(bc):>8} {len(bk):>9} {fmt(lc, 12):>15} {fmt(lk, 12):>15}")
    print(f"  chain    range over A=2..40: {fmt(min(fe_chain), 8)} .. {fmt(max(fe_chain), 8)}"
          f"   ratio {fmt(max(fe_chain)/min(fe_chain), 6)}")
    print(f"  complete range over A=2..40: {fmt(min(fe_compl), 8)} .. {fmt(max(fe_compl), 8)}"
          f"   ratio {fmt(max(fe_compl)/min(fe_compl), 6)}")
    print("  => chain is BOUNDED (a plateau); complete GROWS without bound.")
    print("     That reproduces complete_graph_no_saturation exactly, and it is the")
    print("     channel in which the cited exclusion is a statement about this corpus.")
    print("  NOT NEW: derived_bond_graph_binding.py:170-171 already computes")
    print("     B = E0 * sum_bonds log(1/f_bond) for both bond sets.  This is an")
    print("     independent re-derivation of that comparison, cited not claimed.")
    print("     Two defects noticed in it while checking, neither fixed here:")
    print("       * its docstring declares z = 1/(q^1/2+q^-1/2) (convention C) while")
    print("         its body line 78 computes q0**3/(q0**2+1) (convention D) -- the")
    print("         body is right, the docstring is stale.")
    print("       * line 77 downcasts q0, h, me with float() and it computes in")
    print("         math.log, i.e. float64, and it emits a witness.  That is a")
    print("         NO-FLOAT64 violation in a live witness-emitting producer.")
    print()

    print("CHANNEL 2 — observe-early, the form binding_canonical actually computes:")
    print("  B = Q_b * |tr_free| * (1 - prod f),   tr_free = tr_p^Z * tr_n^N")
    print(f"{'A':>4} {'|tr_free|':>16} {'1-P chain':>13} {'1-P compl':>13} "
          f"{'B/A chain':>15} {'B/A compl':>15}")
    oe_chain, oe_compl = [], []
    for Z, N in NZ:
        A = Z + N
        trf = abs(tau_p) ** Z * abs(tau_n) ** N
        pc = mp.fprod([F[b] for b in bonds_of(Z, N, "chain")])
        pk = mp.fprod([F[b] for b in bonds_of(Z, N, "complete")])
        bc = QB * trf * (1 - pc) / A
        bk = QB * trf * (1 - pk) / A
        oe_chain.append(bc)
        oe_compl.append(bk)
        print(f"{A:>4} {fmt(trf, 12):>16} {fmt(1 - pc, 10):>13} {fmt(1 - pk, 10):>13} "
              f"{fmt(bc, 10):>15} {fmt(bk, 10):>15}")
    print()
    print("  The (1 - prod f) factor is BOUNDED IN [0,1) by construction, for ANY")
    print("  bond set: it is 1 minus a product of numbers in (0,1).  So in this")
    print("  channel the bond count cannot drive B/A at all past the point where the")
    print("  product has already collapsed -- and it collapses fast:")
    for Z, N in [(2, 2), (4, 4), (8, 8)]:
        A = Z + N
        pk = mp.fprod([F[b] for b in bonds_of(Z, N, "complete")])
        pc = mp.fprod([F[b] for b in bonds_of(Z, N, "chain")])
        print(f"    A={A:>3}  prod f (chain) = {fmt(pc, 8):>14}   "
              f"prod f (complete) = {fmt(pk, 8):>14}")
    print()

    print("  What DOES drive B/A in channel 2 is the constituent factor:")
    print(f"{'A':>4} {'|tr_free|':>16} {'|tr_free|/A':>16} {'ratio to prev':>15}")
    prev = None
    for Z, N in NZ:
        A = Z + N
        trf = abs(tau_p) ** Z * abs(tau_n) ** N
        r = "-" if prev is None else fmt(trf / prev, 8)
        print(f"{A:>4} {fmt(trf, 12):>16} {fmt(trf / A, 12):>16} {str(r):>15}")
        prev = trf
    print()

    # The channel-2 curve has a minimum and then grows.  If the constituent factor
    # is what drives it, the minimum's location is PREDICTABLE with no fitting:
    #   |tr_free|/A = c^(A/2)/A  with c = |tr_p·tr_n|,  d/dA[(A/2)ln c − ln A] = 0
    #   =>  A* = 2/ln c.
    c = abs(tau_p) * abs(tau_n)
    A_star = 2 / mp.log(c)
    print("Is the channel-2 shape the constituent factor?  A falsifiable check:")
    print("  |tr_free|/A = c^(A/2)/A on the N=Z chain, with c = |tr_p*tr_n|.  Its")
    print("  minimum is at A* = 2/ln(c) -- no fitting, one closed form.")
    print(f"    c = |tr_p*tr_n|     = {fmt(c, 16)}")
    print(f"    predicted A* = 2/ln c = {fmt(A_star, 10)}")
    grid = [(a, abs(tau_p) ** (a // 2) * abs(tau_n) ** (a // 2) / a)
            for a in range(4, 41, 2)]
    a_min = min(grid, key=lambda t: t[1])[0]
    print(f"    measured argmin over A = 4,6,...,40 : {a_min}")
    print(f"    predicted A* rounds to even A       : "
          f"{2 * int(mp.nint(A_star / 2))}")
    print(f"    agree: {a_min == 2 * int(mp.nint(A_star / 2))}")
    print()

    print("Could ANY bond set rescue channel 2?  A bound, not a search:")
    print("  B/A = Q_b * |tr_free| * (1 - prod f) / A,  and (1 - prod f) is in [0,1)")
    print("  for every bond set, since every f is in (0,1).  So")
    print("      B/A  <=  Q_b * |tr_free| / A     for EVERY bond set,")
    print("  and equality is approached as soon as prod f collapses -- measured")
    print("  above at A >= 12 for the chain and A >= 8 for the complete graph.")
    print("  A plateau therefore needs |tr_free| ~ A.  But |tr_free| = c^(A/2) is")
    print("  exponential, and an exponential is asymptotically linear only in the")
    print("  degenerate case c = 1, where it is CONSTANT and B/A -> 0.  So no choice")
    print("  of bond set produces a plateau in this channel.")
    print(f"    c = {fmt(c, 12)}, so ln c = {fmt(mp.log(c), 12)} != 0: the")
    print("    degenerate case does not obtain, and B/A diverges.")
    print()

    print("Reading")
    print("-" * 78)
    print("  * CoordinationSaturation covers B = eps*M -- binding ADDITIVE in the")
    print("    bond count.  In the free-energy channel the live factors instantiate")
    print("    that exactly (eps = -log f > 0), and the measurement above reproduces")
    print("    its dichotomy: chain plateaus, complete graph does not.  So the")
    print("    exclusion IS a statement about this corpus -- in that channel.")
    print("  * binding_canonical computes the observe-early trace DIFFERENCE, where")
    print("    the bond set enters as (1 - prod f), bounded in [0,1) for every bond")
    print("    set.  complete_graph_no_saturation's premise is not instantiated")
    print("    there.  So the corpus reads binding in two live channels and the")
    print("    exclusion is a statement about one of them only.  That is an arity")
    print("    gap in the CITATION; the theorem is correct as stated, and Channel 1")
    print("    above reproduces it.")
    print("  * In that channel B/A is set by |tr_p|^Z|tr_n|^N, which is exponential")
    print("    in A and is NOT a function of the bond set at all.  Measured, the two")
    print("    bond sets agree to 10 significant figures from A = 12 on, and the")
    print("    curve's minimum sits where the constituent factor alone predicts,")
    print("    A* = 2/ln|tr_p*tr_n| = 16.16 against a measured argmin of 16.")
    print("  * And no bond set rescues it: (1 - prod f) < 1 always, so")
    print("    B/A <= Q_b|tr_free|/A, and a plateau would need an exponential to be")
    print("    linear.  So the saturation constraint that has been driving the")
    print("    bond-set search is, in this channel, a constraint on the CONSTITUENT")
    print("    term rather than on coordination.")
    print("  * Scope (a), and two limits worth stating.  This is measured on the")
    print("    corpus's own closed-form factorisation tr_p^Z tr_n^N prod f, not on")
    print("    the direct Hecke trace binding_canonical evaluates; if those two")
    print("    disagree the channel-2 rows move.  And nothing here says which")
    print("    channel is physically right -- only which one the cited exclusion is")
    print("    a statement about.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
