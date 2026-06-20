# 2n² / noble-gas derivation — item-2 verdict: accept as input (two symmetries short)

**Date:** 2026-06-20
**Branch:** `claude/zealous-hypatia-05xyp9` (PR #2348, bean `e2nf`)
**Class:** research verdict (formalize-first) + content correction.

## The question

Derive the 2n² shell capacity (and thereby the noble-gas closures) from the
categorical structure, **or** establish that they must be accepted as inputs.

## Verdict: accept as input — the framework is *two* symmetries short

Tracing the standard-physics origin of the periodic table makes the gap precise,
and it is larger than "just 2n²":

**Gap 1 — the orbital n² (an SO(4) accidental degeneracy).**
`2n² = 2·Σ_{ℓ=0}^{n-1}(2ℓ+1)`. The `2` is spin, which the 2×2 `T_γe` supplies;
the `n²` is the hydrogenic `SO(4) ≅ SU(2)×SU(2)` Runge–Lenz degeneracy bundling
`ℓ = 0,…,n−1` into principal shell `n`. QOU's `V_ℓ` (dim `2ℓ+1`) reps exist but
are **spent on lepton generations** (the s5→SO(3) work, `ℓ=1`→e, `ℓ=2`→μ), and
there is no second (Runge–Lenz) `SU(2)` bundling them into radial shells.
*(Full diagnosis: [`2026-06-16-2n2-shell-capacity-derivation-gap.md`](2026-06-16-2n2-shell-capacity-derivation-gap.md).)*

**Gap 2 — the noble gases are not even the 2n² closures.**
Pure `2n²` cumulates as `[2, 10, 28, 60, 110, 182]` — the closed shells of a
*pure-Coulomb* atom (Z = 2, 10, **28**, **60**, …). The **chemical noble gases**
are `[2, 10, 18, 36, 54, 86]`, which follow the **Madelung / `n+ℓ` (Aufbau)**
ordering produced by **electron–electron screening** lifting the `ℓ`-degeneracy.
QOU has **no** screening / Madelung mechanism — "Madelung" in the corpus is the
unrelated fluid-dynamics (Bohm) Madelung transform. So even a derived `2n²` would
land on Ni(28)/Nd(60), not Ar(18)/Kr(36).

This is independently confirmed by main's 50-dps σ_F chain
(`computations/sigma_f_electron_shell_chain.py`, commit `8ecbbca9`) and its
caveat (`ae7e0813`): *"categorical σ_F doesn't support noble-gas mechanism,"*
MATH `2n²` cumulative `[2,10,28,60]` ≠ OBSERVED `[2,10,18,36]`.

**Conclusion.** Deriving the periodic table from QOU is a **two-symmetry research
program** — (1) an `SO(4)` Runge–Lenz degeneracy for `2n²`, and (2) a categorical
screening mechanism for the Madelung ordering — neither of which is present.
Pending those, the shell capacities **and** the noble-gas closures are
**empirical / topological inputs** (the `electron-shells-hopf` linking-matrix
conjecture for `2n²`; an unbuilt screening functor for Madelung). This is the
honest state; no derivation is faked.

## Content correction (this PR)

The [`electron-shells-hopf`](../../content/quantum-observable-universe/predicted-spectra/electron-shells-hopf.md)
shell-capacity table **mislabels** the pure-`2n²` cumulative closures as noble
gases: it lists `cumulative 28 → "Ni"` and `60 → "Nd"` under a "Noble gas"
column, but Ni(28) and Nd(60) are **not** noble gases. Relabelled the column to
"pure-`2n²` closure" and added a caveat that the chemical noble gases
`{2,10,18,36,54,86}` follow Madelung, not pure `2n²` — consistent with main's
caveat and Gap 2 above.

## Bean `e2nf` — item 2 closed (as a verdict, not a derivation)

The remaining open item is the two-symmetry research program, recorded as the
genuine blocker. It is *not* tractable as a confinement-SDP cost-operator tweak.
