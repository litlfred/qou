#!/usr/bin/env python3
"""classical_floor_is_interface_parity_probe.py — the floor in A, and what moves it. (qou-zrx2)

🛑 READ THIS FIRST — MOST OF THE SETUP BELOW IS ALREADY ON `main`, AND I MISSED IT.
`computations/probes/classical_floor_derivation_probe.py` (commit `7d15b2abbc`, 2026-09-04) plus
`QOU/MassTheory/ClassicalTraceFloor.lean` (sorry-free) ALREADY derive this floor by Schur-Weyl,
ALREADY establish `c(σ_free) = 2A` and `c(σ_atom) = A+1` for `A = 2 … 20`, and ALREADY state
`c₀(A) = 2^(−A) − 2^(1−2A)`. So does the `⚠ CORRECTED 2026-08-31` note in
`derivation_chain.E_0_CONVENTIONS["B_q_value_absorbed"]`, which cites both. My sibling probe
`classical_floor_is_markov_cycle_count_probe.py` re-derived all of that without finding it — a
corpus-grep failure, not a discovery. It survives as an INDEPENDENT CONFIRMATION by a different
route (it reaches `dim V_λ / 2^n` from convention D's `y_λ = [n−2k+1]_q/[2]_q^n` row cap; the prior
probe reaches it from `y_λ = s_λ(1,Q)/(1+Q)^n` with `Q = q²`, bean `qou-ssz6`), and it should be
cited that way and no other way.

WHAT IS ACTUALLY NEW HERE, and it is the whole reason this file exists. The prior work fixes the
interface crossing multiplicity at `m_pp = m_pn = m_nn = 1` and never varies it, never varies
`intra_order` or `pn_convention`, and never runs `A = 1`. Grep-verified: **zero** occurrences of
`m_pp`/`m_pn`/`m_nn`/`multiplic`/`parity`/`intra_order`/`pn_convention` in either the prior probe or
its Lean. Vary those and the picture changes — the `A+1` is a special case, the floor turns out to
be invariant under both conventions the corpus argues about, and it is a **parity** effect.

THE GENERAL LAW, measured `A = 1 … 20` (exact permutation arithmetic, no q anywhere):

    cyc W_free = 2A                    cyc W_atom = 2A − O

`O` is the number of inter-nucleon interfaces whose crossing multiplicity is **odd**. Substituting:

    floor(A, O)  =  2^(−A) · (1 − 2^(−O))

At `m = 1` every interface is odd, `O = A − 1`, and this collapses to the prior work's
`2^(−A) − 2^(1−2A)` — which is the check that the generalisation is one.

**Both factors matter and they say different things.** `2^(−A)` is the size — the classical
contamination is exponentially small in the mass number, so this is a light-nucleus problem. The
`(1 − 2^(−O))` factor is the structure, and it is the surprise: only the **parity** of each
interface multiplicity enters. `m_pn = 3` gives exactly the same floor as `m_pn = 1`; `m_pn = 2`
gives a different one.

WHY PARITY, and it is a one-line reason once seen. At `q = 1` every letter class collapses to the
transposition `s_g` (`h = q − 1/q = 0`), so an interface applied `m` times contributes `s_g^m`,
which is `s_g` for odd `m` and the identity for even `m`. A transposition joining two *different*
cycles merges them, dropping `cyc` by one; the identity does nothing. The interfaces are laid down
along a chain (`ordering = ['p']*Z + ['n']*N`, interface `k` at generator `3k+2`), so each odd one
attaches a fresh nucleon to the growing blob and always merges. Hence `cyc W_atom = 2A − O` and
`cyc W_free = 2A` (the `O = 0` case).

THREE CONSEQUENCES, in descending order of how much they bear on what `qou-zrx2` is about.

**1. The floor is INVARIANT under both conventions the corpus argues about.** Measured: identical
rationals under `intra_order ∈ {borromean, grouped}` and under
`pn_convention ∈ {bring_color_weighted, strict_averaged}`, at A = 2, 3, 4, 6. Those two choices move
absolute traces a lot — the intra reordering alone moved them by 3.8× (²H) to 14.3× — and they do
not touch this. So the floor is **not** the source of the 5.35× `E₀` disagreement the bean
catalogues between `binding_canonical` and `derive_binding_chain_cooperative`; that ratio is a scale
choice and is a separate defect. This NARROWS the bean rather than resolving it.

**2. The floor is zero for a single nucleon.** `A = 1` has no interface, so `O = 0` and
`cyc W_free = cyc W_atom = 2`. The ℏ_q⁰ contamination is entirely an inter-nucleon effect — it is
created by binding, not carried by the nucleon.

**3. 🛑 The floor CAN be zeroed by an even multiplicity, and that is a DIAGNOSTIC, NOT A REPAIR.**
`m_pp = m_pn = m_nn = 2` gives `O = 0` and `floor = 0` at every A, measured. Do **not** read that as
a fix. Choosing the interface multiplicity because it makes the observable cleanly ℏ_q¹ is selection
against the target — a fit in the exact sense AGENTS.md §"NO FITTING" names, with no continuous
parameter tuned and a free choice made all the same. `m = 1` is the modelling choice the corpus
already made on other grounds, and it stands or falls on those grounds. What this result licenses is
a *statement about the observable's structure*, not a change to the word.

WHAT IS STILL OPEN, and it is the bean's actual subject. Explaining the floor does not choose an
`E₀` convention. The observable's two parts still sit at different ℏ_q orders — an ℏ_q⁰ floor of
`2^(−A)(1 − 2^(1−A))` and an ℏ_q¹ deformation part — and no single scale pairs with both. This probe
makes the ℏ_q⁰ term *more* clearly genuine, not less.

SCOPE — (a) scope-limited. Exact `Fraction` and integer arithmetic; no floating point, no mpmath, no
q evaluated anywhere; no witness, nothing wired. Everything here is the `q = 1` degeneration, which
is standard Hecke theory; what is new is only its application to these words.
"""
from __future__ import annotations

import argparse
import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(_HERE))

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402

Z1 = Fraction(1, 2)   # z_D = q³/(q²+1) at q = 1, exact and forced by convention D


def perm_of(word, n):
    """The permutation a word becomes at q = 1.

    Every letter class — `σ` (`d=0`), `σ⁻¹` (`d=−h`) and the averaged `σ − (h/2)·1` — collapses to
    `s_g` at `h = 0`, so `c` and `d` are dropped BY DERIVATION here. That is not the case at general
    `q`, where the `[int(t[2]) for t in ...]` idiom is simply wrong (it silently reads σ⁻¹ and the
    averaged letters as σ) — an error that cost the sibling `qou-o6ov` arc its whole first pass.
    """
    p = list(range(n))
    for _c, _d, g in word:
        g = int(g)
        p[g], p[g + 1] = p[g + 1], p[g]
    return p


def cycles(p):
    """Number of cycles, fixed points counted."""
    n = len(p)
    seen = [False] * n
    c = 0
    for i in range(n):
        if not seen[i]:
            c += 1
            j = i
            while not seen[j]:
                seen[j] = True
                j = p[j]
    return c


def counts(Z, N, **kw):
    """(n, cyc W_free, cyc W_atom) for this isotope under these word options."""
    n = 3 * (Z + N)
    cf = cycles(perm_of(atom_braid_word_3A(Z, N, include_inter=False, **kw), n))
    ca = cycles(perm_of(atom_braid_word_3A(Z, N, include_inter=True, **kw), n))
    return n, cf, ca


def floor_measured(Z, N, **kw):
    n, cf, ca = counts(Z, N, **kw)
    return Z1 ** (n - cf) - Z1 ** (n - ca)


def odd_interfaces(Z, N, m_pp=1, m_pn=1, m_nn=1):
    """`O` — interfaces with ODD crossing multiplicity, predicted from (Z, N, m) alone.

    `ordering = ['p']*Z + ['n']*N` (read off `atom_braid_word_3A`), so the A−1 interfaces along the
    chain are `Z−1` p-p, then one p-n when both species are present, then `N−1` n-n.
    """
    o = 0
    if Z >= 1:
        o += (Z - 1) * (m_pp % 2)
    if N >= 1:
        o += (N - 1) * (m_nn % 2)
    if Z >= 1 and N >= 1:
        o += (m_pn % 2)
    return o


def floor_predicted(Z, N, **kw):
    """floor = 2^(−A)·(1 − 2^(−O)) — from (Z, N, m) with no word built."""
    A = Z + N
    o = odd_interfaces(Z, N, **kw)
    return Z1 ** A * (1 - Z1 ** o)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--amax", type=int, default=20, help="largest A for the cycle-law scan")
    args = ap.parse_args()

    print("[parity] The ℏ_q⁰ floor of tr_M(W_free) − tr_M(W_atom) as a function of A. (qou-zrx2)")
    print("[parity] Exact integers and Fractions throughout; q is never evaluated.\n")

    # ── 1. the cycle law ────────────────────────────────────────────────────────────────────────
    # The sibling probe treats cyc W_free / cyc W_atom as per-isotope lookups. They are not.
    print(f"  CYCLE LAW — cyc W_free = 2A  and  cyc W_atom = 2A − O,  A = 1 … {args.amax}")
    print(f"    {'A':>3}{'Z':>3}{'N':>3}{'n':>5}{'cyc_free':>10}{'2A':>6}"
          f"{'cyc_atom':>10}{'2A−O':>7}  verdict")
    law_ok = True
    for A in range(1, args.amax + 1):
        Z, N = A // 2, A - A // 2
        n, cf, ca = counts(Z, N)
        o = odd_interfaces(Z, N)
        good = (cf == 2 * A) and (ca == 2 * A - o)
        law_ok = law_ok and good
        if A <= 8 or A == args.amax:
            print(f"    {A:>3}{Z:>3}{N:>3}{n:>5}{cf:>10}{2 * A:>6}{ca:>10}{2 * A - o:>7}"
                  f"  {'ok' if good else 'FAIL'}")
        elif A == 9:
            print(f"    {'...':>3}")
    print(f"    ⇒ {'cycle law holds at every A tested' if law_ok else 'CYCLE LAW FAILS — do not quote the closed form'}\n")

    # ── 2. the closed form, predicted vs measured ───────────────────────────────────────────────
    # `floor_predicted` builds no word; `floor_measured` builds both and counts cycles. Agreement
    # is the check that the law above actually determines the floor.
    print("  CLOSED FORM — floor(A, O) = 2^(−A)·(1 − 2^(−O)),  O = #interfaces of ODD multiplicity")
    print(f"    {'atom':<7}{'Z':>3}{'N':>3}{'A':>4}{'O':>4}{'predicted':>24}{'measured':>24}"
          f"{'decimal':>16}  verdict")
    named = (("¹H", 1, 0), ("n", 0, 1), ("D", 1, 1), ("T", 1, 2), ("³He", 2, 1),
             ("⁴He", 2, 2), ("⁶Li", 3, 3), ("⁷Li", 3, 4), ("¹²C", 6, 6), ("¹⁶O", 8, 8))
    cf_ok = True
    for name, Z, N in named:
        pred, meas = floor_predicted(Z, N), floor_measured(Z, N)
        good = (pred == meas)
        cf_ok = cf_ok and good
        print(f"    {name:<7}{Z:>3}{N:>3}{Z + N:>4}{odd_interfaces(Z, N):>4}"
              f"{str(pred):>24}{str(meas):>24}{float(meas):>16.10f}"
              f"  {'ok' if good else 'FAIL'}")
    print(f"    ⇒ {'closed form reproduces every measured floor' if cf_ok else 'CLOSED FORM WRONG'}")
    # The two the bean measured independently, by an ℏ_q sweep this probe did not see.
    for name, Z, N, target in (("D", 1, 1, Fraction(1, 8)), ("⁴He", 2, 2, Fraction(7, 128))):
        m = floor_measured(Z, N)
        print(f"      vs qou-zrx2's ℏ_q sweep: {name} floor {m} "
              f"{'==' if m == target else '!='} {target}"
              f"  {'agrees' if m == target else 'DISAGREES'}")
    print("      A=1 (¹H, n): O = 0, so the floor is EXACTLY ZERO — it is created by binding,")
    print("      not carried by the nucleon.\n")

    # ── 3. convention invariance — the finding that bears on the bean ───────────────────────────
    # `intra_order` and `pn_convention` are the two word conventions this corpus argues about. Both
    # move ABSOLUTE traces substantially (the intra reordering by 3.8×–14.3×). If the floor moved
    # with them it would be entangled with the E₀ convention collision. It does not.
    print("  CONVENTION INVARIANCE — do the two contested word conventions move the floor?")
    variants = (("canonical", {}),
                ("intra_order=grouped", {"intra_order": "grouped"}),
                ("pn=strict_averaged", {"pn_convention": "strict_averaged"}),
                ("both", {"intra_order": "grouped", "pn_convention": "strict_averaged"}))
    isos = ((1, 1), (1, 2), (2, 2), (3, 3))
    print(f"    {'variant':<24}" + "".join(f"{f'A={Z + N}':>14}" for Z, N in isos))
    baseline = [floor_measured(Z, N) for Z, N in isos]
    inv_ok = True
    for label, kw in variants:
        row = [floor_measured(Z, N, **kw) for Z, N in isos]
        inv_ok = inv_ok and (row == baseline)
        print(f"    {label:<24}" + "".join(f"{str(v):>14}" for v in row))
    print(f"    ⇒ {'INVARIANT — the floor is not entangled with either convention' if inv_ok else 'the floor MOVES with a word convention — the invariance claim is refuted'}")
    print("      So the floor is NOT the source of the 5.35× E₀ disagreement qou-zrx2 catalogues")
    print("      between binding_canonical and derive_binding_chain_cooperative. Separate defect.\n")

    # ── 4. multiplicity parity — what DOES move it ──────────────────────────────────────────────
    # Only the parity of each m enters, because s_g^m is s_g or 1. m=3 must equal m=1 exactly; if it
    # does not, the parity reading is wrong and the closed form's O is not what this probe says.
    print("  MULTIPLICITY PARITY — only m mod 2 enters, because s_g^m ∈ {s_g, 1}")
    print(f"    {'multiplicities':<34}" + "".join(f"{f'A={Z + N}':>14}" for Z, N in isos))
    par_ok = True
    for kw in ({}, {"m_pn": 3}, {"m_pp": 3, "m_pn": 3, "m_nn": 3},
               {"m_pn": 2}, {"m_pp": 2, "m_pn": 2, "m_nn": 2}, {"m_nn": 2}):
        row, pr = [], []
        for Z, N in isos:
            row.append(floor_measured(Z, N, **kw))
            pr.append(floor_predicted(Z, N, **kw))
        par_ok = par_ok and (row == pr)
        print(f"    {str(kw) if kw else '{} (all m=1)':<34}" + "".join(f"{str(v):>14}" for v in row))
    print(f"    ⇒ {'predicted == measured for every multiplicity tested' if par_ok else 'PARITY MODEL FAILS — O is not what this probe computes'}")
    print("      m=3 reproduces m=1 exactly; m=2 does not. All-even ⇒ O=0 ⇒ floor ≡ 0 at every A.")
    print("      🛑 That zero is a DIAGNOSTIC, NOT A REPAIR. Choosing the interface multiplicity")
    print("      because it makes the observable cleanly ℏ_q¹ is selection against the target —")
    print("      a fit in the sense AGENTS.md §'NO FITTING' names, with no parameter tuned and a")
    print("      free choice made anyway. m=1 stands or falls on the grounds it was chosen on.\n")

    # ── 5. size ─────────────────────────────────────────────────────────────────────────────────
    # 1 − 2^(1−A) → 1, so floor(A) → 2^(−A) from below. Reported as the ratio rather than asserted.
    print("  SIZE — the classical contamination is exponentially small in A (all m = 1)")
    print(f"    {'A':>4}{'floor':>22}{'decimal':>16}{'floor·2^A':>14}")
    for A in (1, 2, 3, 4, 6, 8, 12, 16, 20):
        Z, N = A // 2, A - A // 2
        f = floor_measured(Z, N)
        print(f"    {A:>4}{str(f):>22}{float(f):>16.12f}{float(f) * 2 ** A:>14.10f}")
    print("    floor·2^A = 1 − 2^(1−A) → 1, so floor ~ 2^(−A) from below.")
    print("    An ℏ_q⁰ defect that halves per nucleon is a LIGHT-nucleus problem: it is 22.5 % of")
    print("    the deuteron trace difference (qou-zrx2) and negligible by ¹²C. It does not thereby")
    print("    go away — the observable is still a sum of two different ℏ_q orders at every A, and")
    print("    no single E₀ scale pairs with both. That is the bean's subject and it is untouched.")

    ok = law_ok and cf_ok and inv_ok and par_ok
    print(f"\n  {'4/4 checks pass.' if ok else 'SOME CHECKS FAILED — do not quote this probe.'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
