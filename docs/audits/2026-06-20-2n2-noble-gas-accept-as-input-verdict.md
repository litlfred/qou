# 2n² / noble-gas derivation — item-2 verdict (SUPERSEDED — see synthesis)

**Date:** 2026-06-20
**Branch:** `claude/zealous-hypatia-05xyp9` (PR #2348, bean `e2nf`)
**Class:** research verdict (formalize-first) + content correction.
**Status:** **SUPERSEDED** by
[`2026-06-20-electron-shell-program-synthesis.md`](2026-06-20-electron-shell-program-synthesis.md)
— retained as the record of the (now-wrong) "accept-as-input" verdict.

## ⚠⚠ STRICT supersession (2026-06-20, owner directive) — capacity DERIVED; ordering NOT accepted

This document's verdict — "shell capacities **and** the noble-gas closures are
**empirical / topological inputs**" — is **superseded on both counts**:

1. **Capacity `2n²` is DERIVED** (not an input). It is the `q=1` self-square of
   the single bar-even angular `q`-dimension, `2[n]_q²|_{q=1} = 2n²` with
   `[n]_q² = Σ_{ℓ<n}[2ℓ+1]_q` (`shell_capacity_chebyshev_bridge.py`), and the
   integer specialisation `Σ_{ℓ<n}(2ℓ+1)=n²` is now **sorry-free Lean**
   ([`QOU.Molecular.shell_capacity_self_square`](../../content/quantum-observable-universe/lean/QOU/Molecular/ShellCapacitySelfSquare.lean),
   content block [`prop:shell-capacity-self-square`](../../content/quantum-observable-universe/molecular-construction/shell-capacity-self-square.md)).
   No second compact `SU(2)` (per the banner below).
2. **Ordering (Madelung/Aufbau) is OPEN — to be DERIVED, NOT accepted as a
   semi-empirical input** (owner directive, STRICT). The derivation target is the
   `λ₊^ℓ` dominant-channel topological reading (synthesis §4); three structural
   candidates are ruled out. The "empirical input" / "accept-as-input" language
   below no longer represents the position and must not be cited as current.

## ⚠ Owner correction (2026-06-20) — no second *compact* SU(2); the unification is the complex volume 𝔙

The "Gap 1 needs a second compact SU(2) (Runge–Lenz)" framing below is
**superseded**. Per [`bar-parity-split`](../../content/quantum-observable-universe/mass-theory/bar-parity-split.md)
+ [`conj:binding-qbeta-complex-volume`](../../content/quantum-observable-universe/mass-endomorphism/complex-volume-intro.md):
the bar-even (**cosh**, `(q+q⁻¹)/2`) and bar-odd (**sinh**, `(q−q⁻¹)/2`) parts are
the two parities of **one** element, unified by the complex volume
`𝔙 = Re 𝔙 + i·Im 𝔙` via the continuation **`λ ↦ iθ`** (real `q` rotated onto a
root of unity: `cosh λ ↦ cos θ`, `sinh λ ↦ i sin θ`). That continuation **is** the
`SU(1,1) ↔ SU(2)` Weyl-unitary trick:

- **non-compact real form** (real `q`, cosh/sinh, `SU(1,1)≅SO(2,1)`) = the **radial
  shell tower** — exactly QOU's `T_γe` σ-tower (`T_γe` trace `= 2 sinh η`,
  `T_γe^n` the discrete-series ladder);
- **compact real form** (root of unity, cos/sin, `SU(2)`) = the **angular** `V_ℓ`
  (dim `2ℓ+1`).

These are **the same complexified `sl(2,ℂ)`** (= 𝔙), *not* two independent compact
`SU(2)`s. So `2n²` does **not** need a second compact group: it needs the *single*
`sl(2,ℂ)`/𝔙 structure applied to the electron-shell σ-tower, with the angular
`ℓ = 0,…,n−1` multiplicity arising from the compact (root-of-unity) form locked to
the radial `n` of the non-compact form. **This is an open but well-posed
constructive task — not a missing symmetry.** What remains genuinely separate is
**Gap 2 (Madelung/screening)** for the noble-gas *ordering* beyond `2n²`.

The original (now-superseded) "two symmetries short" verdict is retained below for
the record.

---

## The question (original)

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
