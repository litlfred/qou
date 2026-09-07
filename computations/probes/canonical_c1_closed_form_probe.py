#!/usr/bin/env python3
"""canonical_c1_closed_form_probe.py — c₁ in closed form on the CANONICAL word. (qou-pdg9)

WHAT THIS CLOSES. `qou-pdg9` was reopened on 2026-09-06 because its six `c₁` values, its closed
form, and its Lean were all computed on the **pre-2026-09-05 (`grouped`) atom word** — the owner
ruling `qou-hu1f` reordered each nucleon's confinement core to the alternating `(σ₀σ₁⁻¹)³`, and
`c₁` moved by up to 163× (`docs/audits/2026-09-06-c1-is-stale-on-the-reordered-atom-word.md`). That
audit deliberately proposed no replacement: six values do not fix a form.

Here is the replacement, on 44 isotopes rather than six, with both halves verified separately.

THE RESULT. Write `S_X` for the **per-nucleon deletion sum** of species `X ∈ {p, n}`, computed on
that nucleon's own three strands:

    S_X  =  Σ_{ℓ ∈ X}  w_ℓ · 2^(c(X's 3-strand word with letter ℓ deleted))

with `w_ℓ = 1 + d′_ℓ(0) ∈ {+1, −1, 0, 0}` for `σ` / `σ⁻¹` / averaged / colour-weighted. Then

    [★](free)  =  (Z·S_p + N·S_n)/2 · 2^(−A−1)
    [★](atom)  =  [ (Z·S_p + N·S_n)/2  +  4·(I_pp − I_nn) ] · 2^(−2A)

    c₁(Z,N)  =  (Z·S_p + N·S_n)/2 · (2^(−A−1) − 2^(−2A))  −  4·(I_pp − I_nn) · 2^(−2A)

where `I_pp = max(Z−1, 0)` and `I_nn = max(N−1, 0)` count the like-species interfaces along the
chain `['p']*Z + ['n']*N`. Measured, exact, **44/44 for each half separately** at `A = 1 … 8`.

THE ONLY ORDERING-DEPENDENT INPUT IS `(S_p, S_n)`:

    intra_order    S_p    S_n    ⇒ per-nucleon coefficients (S/2)
    borromean       6     −4        ( 3, −2)     ← CANONICAL
    grouped        42     32        (21, 16)     ← qou-pdg9's, and its (21Z + 16N) is exactly this

So `qou-pdg9`'s form is **not wrong in shape** — it is this form evaluated at the wrong `(S_p, S_n)`.
The interface term `−4(I_pp − I_nn)·2^(−2A)` is **unchanged** by the reordering, as it must be:
interfaces are single letters sitting outside the nucleon blocks, so no reordering *within* a
nucleon can touch them. Both forms are verified here, which is what makes that a measurement rather
than an assertion.

AND THE MECHANISM IS CANCELLATION — which is the `qou-hu1f` "contiguity" theme, made quantitative.
The per-letter deletion contributions for one nucleon:

    grouped     proton    +2³ +2³ +2³ +2³  ·  +2³ +2³ −2¹ −2¹ −2¹  ·   =  48 − 6  =  42
    borromean   proton    +2¹ −2¹ +2³ −2¹ +2¹ −2³ +2¹  ·   ·  +2¹ +2¹  =        =   6

Under `grouped` the σ letters are contiguous, so their deletions all leave the *same* cycle count
and add **coherently**. Under the alternating word they interleave with σ⁻¹ deletions of opposite
sign and largely **cancel** — 42 → 6 for the proton, and 32 → **−4** for the neutron, which changes
sign. That sign change is why the canonical `c₁` is negative for neutron-rich isotopes (`(0,7)`:
`−429/8192`) where the grouped one was positive throughout.

WHAT IS DERIVED AND WHAT IS MEASURED. `[★]` itself is `qou-pdg9`'s Part-B result and is quoted, not
re-derived. The `2^(−A−1)` half follows from it in one line — the free word's nucleons are disjoint,
so `c(free minus ℓ) = 2(A−1) + c(nucleon minus ℓ)` and `[★](free) = 2^(−3A)·2^(2A−2)·Σ_k S_k`,
which is the first display above with nothing fitted. The `2^(−2A)` half and the interface
coefficient `4` are **measured**: fitted on the `A ≤ 7` table, then verified at `A = 8` on isotopes
that did not enter the fit, and cross-verified by reproducing `qou-pdg9`'s independently-derived
grouped coefficients `(21, 16)` from `(S_p, S_n)/2 = (42, 32)/2` with no adjustment.

SCOPE — (a) scope-limited. Exact `Fraction`/integer arithmetic; `q` is never evaluated; no float,
no mpmath beyond reading the word's own `d` values for letter classification. No witness, nothing
wired, no Lean edited — the Lean repair is a separate change and is not attempted here.
"""
from __future__ import annotations

import argparse
import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), "substrate"))

import mpmath as mp  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from c1_is_stale_on_the_reordered_atom_word_probe import c1, cycles, perm_of, star  # noqa: E402

# qou-pdg9's grouped per-nucleon coefficients, as the control. If (S_p, S_n)/2 does not reproduce
# these, the S-based reading of that bean's formula is wrong and nothing below should be trusted.
PDG9_GROUPED = (Fraction(21), Fraction(16))


def deletion_sum(species, intra_order):
    """`S_X` — the per-nucleon deletion sum, on that nucleon's own three strands.

    Returned with the per-letter detail, because the detail is the mechanism: contiguous σ runs
    make the terms add coherently, alternation makes them cancel.
    """
    Z, N = (1, 0) if species == "p" else (0, 1)
    word = atom_braid_word_3A(Z, N, include_inter=False, intra_order=intra_order)
    ds = [mp.mpf(t[1]) for t in word]
    h_neg = min(ds)
    gens = [int(t[2]) for t in word]
    total = Fraction(0)
    detail = []
    for i, d in enumerate(ds):
        w = 1 if d == 0 else (-1 if d == h_neg else 0)
        if w == 0:
            detail.append("·")
            continue
        c = cycles(perm_of(gens[:i] + gens[i + 1:], 3))
        total += w * Fraction(2) ** c
        detail.append(("+" if w > 0 else "−") + f"2^{c}")
    return total, detail


def interfaces(Z, N):
    """`(I_pp, I_nn)` along the chain `['p']*Z + ['n']*N`. `I_pn` is 1 when both species present."""
    return (max(Z - 1, 0), max(N - 1, 0))


def predict(Z, N, Sp, Sn):
    """The three closed forms: `[★](free)`, `[★](atom)`, and their difference `c₁`."""
    A = Z + N
    Ipp, Inn = interfaces(Z, N)
    T = (Z * Sp + N * Sn) / 2
    free = T * Fraction(2) ** (-A - 1)
    atom = (T + 4 * (Ipp - Inn)) * Fraction(2) ** (-2 * A)
    return free, atom, free - atom


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--amax", type=int, default=8)
    args = ap.parse_args()

    print("[c1-form] c₁ in closed form on the CANONICAL (borromean) atom word. (qou-pdg9, reopened)")
    print("[c1-form] Exact Fractions and integers throughout; q is never evaluated.\n")

    # ── 1. the per-nucleon deletion sums, and the cancellation that separates the two orderings ──
    print("  PER-NUCLEON DELETION SUM  S_X = Σ_ℓ w_ℓ·2^(c(3-strand word minus ℓ))")
    S = {}
    for order in ("borromean", "grouped"):
        print(f"    intra_order = {order}"
              f"{'   ← CANONICAL' if order == 'borromean' else '   ← qou-pdg9 used this'}")
        for sp, name in (("p", "proton"), ("n", "neutron")):
            tot, detail = deletion_sum(sp, order)
            S[(order, sp)] = tot
            print(f"      {name:<8} S = {str(tot):>4}   S/2 = {str(tot / 2):>5}   "
                  f"{' '.join(detail)}")
    print("    The σ letters are CONTIGUOUS under grouped, so their deletions leave the same cycle")
    print("    count and add coherently (48 − 6 = 42). Alternating, they interleave with σ⁻¹")
    print("    deletions of opposite sign and largely cancel (→ 6), and the neutron's sum CHANGES")
    print("    SIGN (32 → −4). That sign is why canonical c₁ goes negative for neutron-rich A.\n")

    # ── 2. the control: does (S_p, S_n)/2 reproduce qou-pdg9's independently-derived (21, 16)? ──
    # Without this the S-based reading is my own construction and the canonical row below has
    # nothing behind it but a fit to my own numbers.
    got = (S[("grouped", "p")] / 2, S[("grouped", "n")] / 2)
    ctrl_ok = (got == PDG9_GROUPED)
    print(f"  CONTROL — does S/2 reproduce qou-pdg9's grouped coefficients, derived independently?")
    print(f"    S/2 under grouped = ({got[0]}, {got[1]})   qou-pdg9's (21Z + 16N) = "
          f"({PDG9_GROUPED[0]}, {PDG9_GROUPED[1]})   {'MATCH' if ctrl_ok else 'MISMATCH'}")
    if not ctrl_ok:
        print("    ⇒ the S-based reading of that bean's formula is wrong; stop here.")
        return 1
    print("    ⇒ the coefficients ARE S/2. So the canonical row is the same formula at the")
    print("      canonical word's own S, not a fresh fit.\n")

    # ── 3. both halves, separately, both orderings ──────────────────────────────────────────────
    # Checking c₁ alone would let a compensating error in the two halves cancel. They are checked
    # apart so that cannot happen.
    print(f"  VERIFICATION — each half separately, A = 1 … {args.amax}, exact Fractions")
    print(f"    {'ordering':<12}{'[★](free)':>14}{'[★](atom)':>14}{'c₁':>12}")
    ok = True
    for order in ("borromean", "grouped"):
        Sp, Sn = S[(order, "p")], S[(order, "n")]
        nf = na = nc = tot = 0
        for A in range(1, args.amax + 1):
            for Z in range(0, A + 1):
                N = A - Z
                tot += 1
                pf, pa, pc = predict(Z, N, Sp, Sn)
                nf += (star(Z, N, include_inter=False, intra_order=order) == pf)
                na += (star(Z, N, include_inter=True, intra_order=order) == pa)
                nc += (c1(Z, N, order) == pc)
        ok = ok and (nf == na == nc == tot)
        print(f"    {order:<12}{f'{nf}/{tot}':>14}{f'{na}/{tot}':>14}{f'{nc}/{tot}':>12}")
    print(f"    ⇒ {'every isotope, every half, both orderings.' if ok else 'FAILED — do not quote this form.'}")
    print("      A = 8 did not enter the pattern search (that used A ≤ 7), so its 9 isotopes are")
    print("      a held-out test rather than more of the fit.\n")

    # ── 4. the table, for a reader who wants the values ─────────────────────────────────────────
    Sp, Sn = S[("borromean", "p")], S[("borromean", "n")]
    print("  CANONICAL c₁ — the six qou-pdg9 cases plus the light isotopes")
    print(f"    {'atom':<7}{'Z':>3}{'N':>3}{'A':>3}{'I_pp':>6}{'I_nn':>6}"
          f"{'c₁ canonical':>16}{'c₁ grouped (dead)':>20}")
    for name, Z, N in (("¹H", 1, 0), ("n", 0, 1), ("D", 1, 1), ("pp", 2, 0), ("nn", 0, 2),
                       ("T", 1, 2), ("³He", 2, 1), ("⁴He", 2, 2), ("⁶Li", 3, 3), ("⁷Li", 3, 4)):
        Ipp, Inn = interfaces(Z, N)
        print(f"    {name:<7}{Z:>3}{N:>3}{Z + N:>3}{Ipp:>6}{Inn:>6}"
              f"{str(c1(Z, N, 'borromean')):>16}{str(c1(Z, N, 'grouped')):>20}")
    print(f"\n    c₁(Z,N) = ({Sp // 2}Z {'+' if Sn >= 0 else '−'} {abs(Sn) // 2}N)"
          f"·(2^(−A−1) − 2^(−2A)) − 4·(I_pp − I_nn)·2^(−2A)")
    print("    against qou-pdg9's dead form  (21Z + 16N)·(2^(−A−1) − 2^(−2A)) − 4·(I_pp − I_nn)·2^(−2A)")
    print("    — same shape, same interface term, different per-nucleon coefficients.")
    print("\n    NOT claimed: that this is the last word on the ℏ_q expansion. c₂ is untouched, and")
    print("    the Lean carrying the dead coefficients is not edited here.")

    print(f"\n  {'checks pass.' if ok and ctrl_ok else 'SOME CHECKS FAILED — do not quote this probe.'}")
    return 0 if (ok and ctrl_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
