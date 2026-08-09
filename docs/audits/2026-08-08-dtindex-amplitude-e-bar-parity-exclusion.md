# The DT-invariant / 3d-index / graded-Euler route is BAR-PARITY excluded from supplying the A=3 amplitude `E` — scope-(b)

**Date:** 2026-08-08 · **Epic:** `qou-x631` · **Beans:** `qou-3dya` (Δ_λ keystone:
converge DT/Stokes onto amplitude `E`) / `qou-jqof` (the open keystone) ·
**Branch:** `claude/deltalambda-dt-index-amplitude-e-2026-08-08` ·
**Tier:** derivation-attempt / formalize-first (Lean, sorry-free) ·
**Scope:** (a) framing; the exclusion itself is **scope-(b)** (proved invariant: bar-parity);
nothing fitted; nothing wired; no anchor inverted; L2 unchanged.

- Lean: [`QOU/QBeta/DTIndexAmplitudeE.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/DTIndexAmplitudeE.lean)
  — sorry-free, `lean`-direct exit 0, 0 real sorries, no `native_decide` / trivial-true / axiom.
- Builds on (cited, not imported — QOU package unbuilt in-sandbox): `A3AntiSelfAdjointLift`
  (#4611; `amplitude_nonzero`/`amplitude_surjective`/`amplitude_injective`), `A3OffBlockDerivation`
  (#4595; `magnitudeFactor_le_one`, `offBlockNum_bar_odd`, `branching_graded_selfadjoint`),
  `BerezinianSelfAdjointCrossTerm` (self-adjoint ⇒ bar-even cross-term).

## The question

`A3AntiSelfAdjointLift` (#4611) bracketed the A=3 magnitude lift `r* = μ₃/c₃ ≈ 1.585 > 1` to
**exactly one free real DOF** — the anti-self-adjoint off-block amplitude `E := C + σ B`. Deriving
`E` from the substrate (never fitting to `r*`) is the open keystone `qou-jqof`. This note attacks
that keystone via the **DT-invariant / 3d-index / graded-Euler** substrate route:

> Is `E` a Behrend-signed Donaldson–Thomas count / 3d-index / graded Euler characteristic of a
> substrate-forced moduli — i.e. does the DT-index datum supply the numeric amplitude that hits `r*`?

## The answer: NO — the DT-index route is bar-parity excluded (scope-(b))

The exclusion is a **proved invariant (bar-parity)**, not a numerical near-miss:

| step | statement | Lean |
|---|---|---|
| DT-index is bar-EVEN | every Behrend count / graded-Euler χ ∈ ℤ; a ring-hom bar involution fixes `ℤ ↪ R` | `dtIndex_barEven` (`map_intCast`) |
| the amplitude is bar-ODD | the physical mass/C1 face has a **bar-even** cross-term `B·D⁻¹·C` (parity of `r*=μ₃/c₃`); with `B` bar-odd, `D` bar-even, this forces `C` bar-odd, hence `E=C+σB` bar-odd | `crossTermBarEven_imp_C_barOdd` → `amplitude_barOdd` |
| the two sectors meet only at 0 | `σx=x ∧ σx=−x ⇒ 2x=0 ⇒ x=0` (invariant: `char R ≠ 2`) | `barEven_barOdd_eq_zero` |
| **headline** | the nonzero amplitude `E` a lift forces is **NOT** any DT-index value `(d:R)`, `d:ℤ` | **`dtIndex_cannot_supply_amplitude`** |

**Reading.** The self-adjoint branching Schur complement (bar-EVEN sector) is a reduction `≤ 1`
(`A3OffBlockDerivation.magnitudeFactor_le_one`); the lift lives **entirely** in the bar-ODD
amplitude `E`. Any DT-invariant / 3d-index / graded-Euler datum is an **integer** — a
Behrend-weighted virtual point count, equivalently an alternating dimension sum
`χ = Σ_k (−1)^k dim(G)_k ∈ ℤ` — and every integer is bar-EVEN. **A bar-even integer cannot be a
nonzero bar-odd amplitude.** So the DT-index route, which is exactly the machinery producing
`Δ_λ = (−1)^{n(λ)}·dim V_λ`, the sandwich normalization `Σ_{λ⊢3}Δ_λ = −2`, and the Stokes count
`3` / `{3,4}`, **cannot supply `E`**.

## The bar-parity exclusion is already accepted corpus infrastructure

The "bar-even ∧ bar-odd ⇒ 0" filter is **not** invented here — it is established corpus
infrastructure: [`QOU/BraidKnot/BarParityInvariant.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/BarParityInvariant.lean)
(`barEven_barOdd_forces_zero`, bean `qou-ph2a` / `s5bb`) proves it at the **function** level
(`f(q⁻¹) = ±f(q)`, `q ↦ q⁻¹` concrete) and already applies it to exclude a bar-mixed μ-correction
on the amphichiral figure-8. This file is the **element / scalar** analog (`σ : R →+* R` on the
scalars in which the A=3 off-blocks `B, C, D, E` live). The genuinely new step is `dtIndex_barEven`:
a DT-index / graded-Euler value is an integer, hence bar-even, so it falls on the *excluded* side of
that already-accepted filter. That the same `ℤ/2` bar grading gates the μ-correction (#2584), the
Δ_λ chirality sign (`deltaSign = (-1)^{principal grading}`), and now the A=3 amplitude `E` is the
recurring structural theme BarParityInvariant already names.

## Why this is a genuine new contribution (not a re-proof)

- `A3OffBlockDerivation` proved the *self-adjoint branching* gives `≤ 1` (bar-even sector).
- `A3AntiSelfAdjointLift` proved `E` is the single free/unique DOF (affine bijection).
- **This file** proves the *DT-index route specifically* cannot be `E`'s source, by a bar-parity
  invariant — a route-scoped scope-(b) that no corpus file previously connected to the `E` framing
  (`amplitude` × `DT` grep on `docs/audits` + `content/**/QBeta` returned no prior `E`↔DT link).

## What it buys, and its honest limit

- **Buys (scope-(b)):** the integer DT/graded-Euler *count* is excluded from *being* `E` — a proved
  parity obstruction, cited invariant `char R ≠ 2` + `map_intCast`.
- **Does NOT claim:** that `E` is underivable. It **hands `E` back to the bar-ODD sector** — the
  resurgent Stokes / DM q-cubic prolongation symbol
  (`conj:qdifference-kernel-prolongation-symbol`), which is the ±i (π/2) resurgent phase, bar-ODD,
  the correct parity. This converges from a **fresh direction** with the Stokes route a sibling is
  on (bean `qou-jqof`): the DT attack *proves* the amplitude cannot be a DT count and points at
  Stokes as the only remaining home. Consistent with Horn-1 (PR #4540): the DT/Behrend **sign** is
  a real π-phase (bar-even), while the resurgent Stokes phase is ±i / π/2 (bar-odd) — `E` lives with
  the latter.
- **Consistent with** `amplitude_surjective` (some real `E` hits `r*`): that witness is a bar-odd
  geometric scalar, never a DT integer. No contradiction.

## Anti-fit / anti-laundering ledger

- **0 free parameters**; `r*`, `μ₃`, `c₃`, AME, CODATA, `q₀` never inverted; nothing chosen to hit a
  target. The DT integers (`−2`, `3`, `{3,4}`) appear only as the objects being *excluded*.
- **No conjecture class, no axiom** carrying `E`'s value — the file is a pure *limitative*
  (impossibility) result, so there is nothing to launder. §"Axiomatization is NOT a Proof" trivially
  respected.
- The one physical hypothesis is the **bar-EVEN parity of the mass-face cross-term** (an established
  parity datum, `BerezinianSelfAdjointCrossTerm`) — a *sub-hypothesis about the observable's parity*,
  not the conclusion; the theorem DERIVES `E`'s bar-oddness and then the exclusion.
- Formalize-first honoured: every claim is a sorry-free Lean statement. No `sorry`, no
  `True`-conclusion, no `native_decide`. Base ring generic `[Field R] [CharZero R]`; no `ℝ`.
- corpus-grep run before the "no prior E↔DT" declaration (docs/audits, content/, computations/,
  docs/coordination walked). "sorry-free ≠ derived" respected — this proves an *exclusion*, it does
  not close `qou-jqof`.

## Verdict

**Scope-(b), route-scoped exclusion.** The DT-invariant / 3d-index / graded-Euler route **cannot**
supply the A=3 anti-self-adjoint amplitude `E`: DT values are bar-even integers, `E` is bar-odd, and
the sectors meet only at zero. This does not close `r*` — it **removes the DT-index route from the
menu** and hands the keystone back to the bar-odd resurgent-Stokes sector (`qou-jqof`), converging
with the Stokes-route sibling from a different direction.

## Cross-references

- Amplitude `E` bracket (single DOF): [`A3AntiSelfAdjointLift.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/A3AntiSelfAdjointLift.lean) (#4611); ROUTE 2-c in [`option-e.md`](../coordination/option-e.md).
- Self-adjoint reduction `≤ 1`: [`A3OffBlockDerivation.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/A3OffBlockDerivation.lean) (#4595).
- DT = graded-Euler home (Δ_λ value): [`2026-08-01-deltalambda-dt-3dindex-graded-euler-unification.md`](2026-08-01-deltalambda-dt-3dindex-graded-euler-unification.md); DT moduli external: [`2026-08-01-deltalambda-dt-substrate-derivation.md`](2026-08-01-deltalambda-dt-substrate-derivation.md), [`2026-08-02-driver-14-character-variety-dt-moduli-constructibility.md`](2026-08-02-driver-14-character-variety-dt-moduli-constructibility.md).
- Stokes = DT bridge (bar-odd home for `E`): [`2026-08-02-stokes-dt-bridge-moduli-gap-unification.md`](2026-08-02-stokes-dt-bridge-moduli-gap-unification.md); `conj:qdifference-kernel-prolongation-symbol`.
- Horn-1 sign is real π-phase (bar-even), not ±i Stokes: PR #4540 `StokesPhaseSignChirality.lean`.
- AGENTS.md §"Axiomatization is NOT a Proof"; §"Before declaring refuted" ((a)/(b) scoping used); §"Strict Lean Discipline".
