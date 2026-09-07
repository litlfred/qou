# The local Stokes / resurgence route cannot supply the A=3 amplitude `E` — a WALL

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


**Date:** 2026-08-08 · **Bean:** `qou-jqof` (epic `qou-x631`) ·
**Branch:** `claude/deltalambda-stokes-amplitude-e-2026-08-08` ·
**Tier:** formalize-first (Lean, sorry-free, `lean`-direct exit 0, `#print axioms` shows no `sorryAx`) ·
**Scope:** WALL — scope-(a) with a scope-(b) sub-exclusion; nothing fitted, nothing wired, `q₀`-derivation not routed through.
**Lean:** [`QOU/QBeta/StokesAmplitudeE.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesAmplitudeE.lean)
— exit 0, 0 real sorries, axioms `[propext, Classical.choice, Quot.sound]` only.

## The question

`QOU.QBeta.A3AntiSelfAdjointLift` (merged #4611) bracketed the A=3 Δ_λ magnitude lift
`r* = μ₃/c₃ ≈ 1.585` to **exactly one free real DOF** — the anti-self-adjoint off-block
amplitude `E` (`amplitude_surjective`/`amplitude_injective`: `E ↦ factor` is a bijection;
`amplitude_nonzero`: a genuine lift forces `E ≠ 0`). Deriving `E` from the substrate
(never fitting it) is the open keystone `qou-jqof`. This audit asks the assigned angle:
**can the local Stokes-constant / resurgence / Écalle-Borel route supply `E`?**

## TL;DR — NO. A rigorous WALL, extending PR #4790.

The **local** Stokes datum of the carrier module provably cannot supply the numeric `E`.
Two branches, both block the route:

1. **Pure-isoclinic (single Newton slope) ⇒ `E = 0`.** By RSZ Thm 3.3.5 the isoformal
   moduli of a module with slopes `μ : Fin k → ℤ` has dimension
   `Σ_{i<j} rᵢrⱼ(μⱼ−μᵢ)` (`rszIsoformalDim`); at `k = 1` this is `0`
   (`rszIsoformalDim_one`, on main). The q-Stokes matrix is unipotent, identity on
   `gr M₀` (RSZ Thm 5.5.7), so its strictly-off-block part — the amplitude a local Stokes
   datum can supply — is a coordinate sum over those moduli, hence **`0`** when the moduli
   is a point. Composed with `amplitude_nonzero`, a single-slope carrier's local Stokes
   data **cannot produce the lift**. **This is exactly PR #4790's finding
   (`c1_infinity_isoformalDim_eq_zero`: C1's `∞` is pure isoclinic ⇒ no local Stokes data)
   lifted to the amplitude level.** C1 (= RSZ route-A `L1` = the DM q-cubic prolongation
   symbol `conj:qdifference-kernel-prolongation-symbol`, the very object
   `A3AntiSelfAdjointLift.DerivedAmplitudeGivesLift` names as `E`'s would-be source) is
   Fuchsian at `0` and pure isoclinic at `∞` — so its local Stokes data is **empty at every
   local point**.

2. **Multi-slope ⇒ `E` free, value in the GLOBAL Birkhoff matrix.** A local-Stokes lift
   therefore *forces* ≥ 2 distinct slopes (`local_stokes_lift_forces_positive_dim`). But
   when the moduli dimension is `≥ 1` the local amplitude is **surjective onto `R`**
   (`stokesAmplitude_surjective_of_dim_pos`): the nonempty isoformal moduli leaves `E`
   **entirely free** — local Stokes data does not select its value. Selecting the point in
   the moduli is the job of the **global** (`0↔∞`) Birkhoff connection matrix — theta-valued,
   un-started, and NOT local Stokes data
   ([`2026-08-01-branch-selection-birkhoff-connection-matrix.md`](2026-08-01-branch-selection-birkhoff-connection-matrix.md),
   the "W2" successor #4790 also named).

**Net:** either the carrier is single-slope and local Stokes data gives `E = 0` (no lift,
**scope-(b)**, cited invariant = RSZ `rszIsoformalDim_one`), or it is multi-slope and local
Stokes data leaves `E` free — its value living in a distinct open object, the global
Birkhoff matrix (**scope-(a)**). The local Stokes/resurgence route is walled either way.

## The bridge is a CITED MODEL, not a fit (honesty)

`stokesAmplitude d coeff v := ∑_{i<d} coeffᵢ·vᵢ` models the local q-Stokes off-block as the
coordinate sum of the unipotent matrix's nilpotent part over the `d = rszIsoformalDim`
slope-pairing moduli (RSZ Thm 5.5.7 for the unipotency ⇒ **zero constant term**; Thm 3.3.5
for the count). This is an **import stated as a model**, never a derivation of `E`, and per
§"Defined residual ≠ derived decomposition" the vanishing at `d = 0` is the faithful RSZ
statement "a single-slope module has no strictly-off-block part," not a smuggled split of
`E`. The file asserts only the honest conditional: *IF `E` is supplied by local Stokes data,
THEN it has this form* — and derives the walls.

## Unification with the sibling Stokes negatives

This is the **amplitude-level** structural reason behind three prior numerical/algebraic
Stokes negatives — the carrier's *local* Stokes moduli is simply too small to be `E`:

| sibling audit | its finding | this WALL's account |
|---|---|---|
| [`stokes3-largeorder-amplitude-41`](2026-08-01-stokes3-largeorder-amplitude-41.md) | naive large-order amplitude gives `2πP ≈ 1`, not the GGM integer `3` | the local resurgent growth carries no free amplitude to be `E` (single-slope 4₁ resurgent datum) |
| [`qborel-ecalle-resum-barodd`](2026-08-01-qborel-ecalle-resum-barodd.md) | bar-odd ladder resums to a value but is **anchor-blind**; Stokes jump exp-suppressed, `|Im(h₀·D)|=0` on the real meridian | the local Stokes datum vanishes on the substrate meridian (the pure-isoclinic branch); it lives on the fibre / global level |
| [`stokes-phase-sign-delta-lambda`](2026-08-01-stokes-phase-sign-delta-lambda.md) | the ±i Stokes phase is not the Δ_λ **sign** (real π-phase, a-function parity) | orthogonal (that was the sign; this is the magnitude amplitude) — both say local Stokes data under-determines Δ_λ |

## Proved / open split

| Assertion | Disposition |
|---|---|
| `d = 0` ⇒ local Stokes amplitude `= 0` (`stokesAmplitude_eq_zero_of_dim_zero`) | **proved sorry-free** |
| C1's `∞` isoformal moduli is a point (`c1_isoformal_toNat_zero`, via `rszIsoformalDim_one`) | **proved sorry-free** |
| single-slope carrier ⇒ local Stokes **cannot lift** (`pureIsoclinic_local_stokes_cannot_lift`) | **proved sorry-free (scope-(b))** |
| a local-Stokes lift **forces** ≥ 2 slopes (`local_stokes_lift_forces_positive_dim`) | **proved sorry-free** |
| ≥ 1-dim moduli ⇒ amplitude **surjective**, `E` free (`stokesAmplitude_surjective_of_dim_pos`) | **proved sorry-free** |
| `E` from the GLOBAL Birkhoff connection matrix drives the lift | **OPEN** — §3b dependent conjecture `GlobalBirkhoffSuppliesAmplitude`, **no instance** |
| the A=3 magnitude `r*` | **OPEN** — the amplitude `E` stays underived; this WALL narrows *where* it can come from (not local Stokes) |

## Anti-laundering / honesty ledger

- **No fit.** `E` is never solved from `r*`/`μ₃`/`c₃`; the surjectivity witness is exhibited
  precisely to show that *pinning* `E` to a target is the forbidden fit.
- **No axiomatized conclusion.** `GlobalBirkhoffSuppliesAmplitude` carries genuine content
  (the RSZ multislope necessary condition + forced `E ≠ 0` + the lift as hypothesis) and has
  **no instance**; it is distinct from `A3AntiSelfAdjointLift.DerivedAmplitudeGivesLift`
  (which names the DM q-cubic) — this one localises the source to the **global** Birkhoff
  datum.
- **`q₀`-derivation not routed through** (the permanent gate is respected).
- **Formalize-first, machine-verified** (`lean`-direct exit 0; `#print axioms` = the three
  standard axioms, no `sorryAx`; deps `RSZIsoformalInterface` + `A3AntiSelfAdjointLift`
  rebuilt from source against the restored Mathlib olean cone).
- **Extends #4790, does not overturn it** (same pure-isoclinic mechanism, applied to `E`).

## Cross-references

- Lean (new): [`StokesAmplitudeE.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesAmplitudeE.lean).
- Amplitude bracket (source): [`A3AntiSelfAdjointLift.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/A3AntiSelfAdjointLift.lean); self-adjoint reduction [`A3OffBlockDerivation.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/A3OffBlockDerivation.lean).
- RSZ interface: [`RSZIsoformalInterface.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/RSZIsoformalInterface.lean) (`rszIsoformalDim`, `rszIsoformalDim_one`).
- Retraction being extended: [`2026-08-08-c1-infinity-has-no-stokes-multiplier.md`](2026-08-08-c1-infinity-has-no-stokes-multiplier.md) (PR #4790).
- Global-Birkhoff successor: [`2026-08-01-branch-selection-birkhoff-connection-matrix.md`](2026-08-01-branch-selection-birkhoff-connection-matrix.md).
- Sibling Stokes negatives: [`2026-08-01-stokes3-largeorder-amplitude-41.md`](2026-08-01-stokes3-largeorder-amplitude-41.md), [`2026-08-01-qborel-ecalle-resum-barodd.md`](2026-08-01-qborel-ecalle-resum-barodd.md), [`2026-08-01-stokes-phase-sign-delta-lambda.md`](2026-08-01-stokes-phase-sign-delta-lambda.md).
- Ledger: [`docs/coordination/option-e.md`](../coordination/option-e.md) (ROUTE 2-c row).
- AGENTS.md §"Axiomatization is NOT a Proof"; §"Before declaring refuted"; §"Strict Lean Discipline"; §"Defined residual ≠ derived decomposition".

-- Ref: [ramis-sauloy-zhang-2013] https://arxiv.org/abs/0903.0853 (Thm 3.3.5, §5.5.2, Thm 5.5.7)
-- Ref: [manuscript] docs/audits/2026-08-08-c1-infinity-has-no-stokes-multiplier.md
-- Ref: [manuscript] docs/audits/2026-08-01-branch-selection-birkhoff-connection-matrix.md
