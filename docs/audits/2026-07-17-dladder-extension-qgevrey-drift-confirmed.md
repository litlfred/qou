# D-ladder extension (k→31): structural q-Gevrey drift confirmed, not a finite-k shadow

> **⚠ CONVENTION-C CONDITIONAL — scope note added 2026-09-06 (bean `qou-h6o3`).**
> This document's conclusions depend on the `c_k` precision ladder / `Q_β`, which
> AGENTS.md records as **convention-C-frame throughout and NOT re-derived** under
> the owner ruling of 2026-08-15 making convention D (`z = q³/(q²+1)`) canonical.
> Treat every `c_k`-dependent statement below as **C-conditional** until the
> ladder is re-derived (bean `qou-cds1`). The numbers here are correct *for C*
> and are kept as recorded — they need **scoping, not correction**. This note was
> applied mechanically to the 45 documents in this arc that reference the ladder;
> it asserts dependence on the ladder, not that any particular conclusion changes
> under D.


> **⚠ [SUPERSEDED 2026-08-09]** — the headline conclusion ("genuinely
> resurgent"; "super-exponentially divergent") is withdrawn: `D(ũ)` **is
> convergent** (`ρ = 0.1428…`, `κ = 0`; the estimator disagreement this file
> probed was the signature of the missed `Q_b` zero at `q*_ρ ≈ 1.48989`, not
> q-Gevrey drift). The extended exact ladder `k ≤ 31` and the non-holonomicity
> results stand. See
> [`2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md`](2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md).

**Date:** 2026-07-17 · **Axis:** Q_β odd channel (c₃) · **Tier:** measurement
(scope-(a); no `c_k` wired; no fit; no tier change). **Branch:**
`claude/dladder-qgevrey-extension-2026-07-17`. Executes Front 1 of the owner-picked
three-front attack ([`2026-07-17-three-front-attack-specs.md §1`](2026-07-17-three-front-attack-specs.md)),
the "more terms" arm flagged in the merged q-Borel–Leroy resummation probe.

## The open question this settles

The 07-13 D-ladder work (KC22) proved the exact bar-odd `D(ũ)` ladder is
**non-(q-)holonomic** in every tested class and super-exponentially divergent,
but left one measurement open: at `k=21` the two Borel-plane singularity
estimators (dlog-Padé of the Borel–Leroy transform vs the root-test radius)
disagreed. **Is that inconsistency a finite-`k` shadow (shrinks with more
terms → a single effective Gevrey index exists) or structural q-Gevrey drift
(persists → no single index; the object is genuinely resurgent)?**

## What was run

[`qbeta_dladder_extension_singularity_probe.py`](../../computations/qbeta/qbeta_dladder_extension_singularity_probe.py)
extends the exact `ℚ(√3)` D-ladder from `k≤21` (ORD 43) to `k≤31` (ORD 63) via
exact rational linear algebra (`qbeta_ck_sseries_exact_rational` +
`qbeta_dladder_generating_function_structure_probe.build_d_ladder`, no floats in
the ladder core), then re-measures three quantities at the extended order.

## Result — the drift persists (structural q-Gevrey)

| Quantity | `k≤21` | `k≤31` | reading |
|---|---|---|---|
| Divergence class `C` (`log\|d_k\| = A + Bk + C·k·log k`) | 0.07737 | 0.06134 | **still drifting** (not stabilising to a constant) |
| Borel–Leroy order `s*` (slope-zero crossing) | 0.18652 | 0.15944 | **still drifting** (Δ = 0.0271) |
| dlog-Padé `ρ(s*)` vs root-test `ρ` | — | 0.28304 vs 0.24152 | **relative gap `\|ρ/ρ_rt − 1\|` 0.172 PERSISTS** (17.2%) |

**Verdict: structural q-Gevrey drift, not a finite-`k` shadow.** Neither the
divergence-class exponent `C` nor the Borel–Leroy order `s*` stabilises as
`k` grows from 21 to 31, and the singularity-estimator inconsistency does not
shrink (the reported 0.172 is the **relative** gap `|ρ_dlogPadé/ρ_rootTest − 1|`,
i.e. 17.2%, not the absolute difference 0.042). There is **no single effective Gevrey index**, so no fixed-order
Borel–Leroy resummation is the honest object.

## Consequence for the Q_β odd channel

This **reinforces KC22** and sharpens the reassessed path
([`2026-07-17-1ppq-path-reassessment.md`](2026-07-17-1ppq-path-reassessment.md)):
the bar-odd `D(ũ)` element is genuinely **resurgent** — the honest resummation
is the **Écalle acceleration / the Φ_b state integral**, not any fixed-order
Borel or Borel–Leroy sum. A single Gevrey-order Borel–Leroy attempt would be
mis-specified. The remaining structural anchors for the acceleration are
unchanged: the **2-adic bar-parity grading** (`v₂(den b_k)=0 ⟺ k odd`; 2 the
unique graded prime, Lean-anchored) and **q\*** (the `S=0` decay-sector
determination of `q₀`).

This is a **measurement, not an identification**: no instanton action is
claimed (the estimators do not agree at the extended `k`, so `ρ` is not pinned),
nothing is wired, and the tier is unchanged. Vol(4₁)/π remains a
consistency-only comparison on the **even** channel (#3683), not identified here.

## Scope / discipline

- **Scope-(a)** measurement: it constrains the *class* of the odd-channel
  object (rules out a single-index Borel–Leroy closure), not an ingredient.
- No `c_k` value produced or wired; no fit to QOU observables; `conj:im-q-physical-role`
  stays a conjecture; the L2 count is unchanged (still 2/7).
- Adjacent siblings: #3683 (Borel resurgence of the **even** κ-tower — distinct
  object); #3737 (KC22 non-holonomicity — this extends its `k=21` open estimator
  question). No overlap.

## Cross-references

- Reassessment + spec: [`2026-07-17-1ppq-path-reassessment.md`](2026-07-17-1ppq-path-reassessment.md), [`2026-07-17-three-front-attack-specs.md`](2026-07-17-three-front-attack-specs.md)
- KC22 + 2-adic grading: [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md), [`2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md`](2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md)
- Witness: `computations/qbeta/qbeta-dladder-extension-singularity.witness.json`
