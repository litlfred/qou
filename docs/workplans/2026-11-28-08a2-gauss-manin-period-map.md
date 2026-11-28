# Epic `08a2`: derive the Gauss–Manin period map Φ (Lean-first plan, 2026-11-28)

Owner tap 2026-11-28 ("Start 08a2 thread"). Branch `claude/gauss-manin-period-map-2026-11-28`.

## Target

`Φ : q ↦ H¹(E_{τ(q)}) ⊂ H¹(Bring)` (R2 / MOC). What it has to discharge on `main`:

* `QOU.MassTheory.EmPerLoopMeasureConditional.GermPeriodShare μ₁ a₀`: one field,
  `channelCount * μ₁ = a₀` with `channelCount = pairCount = 2`. No instance exists, and none
  is added unless derived. It gives `μ₁ = a₀/2`.
* `QOU.Archimedean.EmPerLoopMeasureConditionalReal.HeatKernelLeadingCoeff a₀` (`a₀ = 1/(4π)`,
  Clause A) is a separate analytic hypothesis.
* Formal-groups thread (#9935, #9944, #9946): `1/(8π) = (1/4)·‖2πi‖⁻¹`, and `2πi = ∮ dt/t` is
  the period of `𝔾ₘ` (`QOU.Transcendental.FormalGroups.GmPeriod`). So Φ has to supply a
  `(2πi)⁻¹` normalisation and a rational.

Standing constraints: no `sorry`, standard axioms only, no measured values in proofs, no
fitting, analytic material only under `QOU/Transcendental/`, roots of unity algebraic.

## What is already known (not re-derived here)

* `2026-08-02-moc-gauss-manin-not-derivable`: Φ does not follow from the `E⁴` model. The
  model fixes the codomain (`Jac(Bring) ~ E⁴`, `E` in class 50a, no CM, the X₀(5) isogeny),
  not the map.
* `2026-08-02-hodge-lift-bring-h1-model`: `ρ ↔` Hodge conjugation is automatic; the wall is
  the one existence field (MOC).
* `2026-08-29-alpha-em-germ-viability-live` (bean `qou-rrgk`): the germ curvature
  `F_q = [δq₁, δq₂]` has EM-singlet moment `m_F = −h/[2]_q`. The route is live, which is
  necessary, not sufficient.
* Owner ruling 2026-07-19: R2 is not proved and not canonized.

## A structural fact the plan has to respect

The Hecke anchor sits at `q₀ ≈ 1.11` (outside the unit disc), while the nome of Bring's
elliptic factor is `e^{2πiτ₀}` with `τ₀ = −½ + 0.18668i`, so `|nome| ≈ 0.31`. These are
diagnostics, used in no proof. They show that "the Hecke `q` *is* the Tate nome, evaluated
at `q₀`" cannot hold with `τ(q₀) = τ₀`; picking a power `nome = q^k` to make them agree would be
a fit. So the identification in M4 is a genuine definition, not a computation, and it is the
owner's call.

## Milestones

| | milestone | where | status |
|---|---|---|---|
| **M1** | Tate curve `E_q` over `ℤ[[q]]`: `c₄ = E₄`, `c₆ = −E₆`, `Δ = q + O(q²)`; cusp fibre is the nodal cubic, parametrised by `𝔾ₘ`, with `dx/(2y+x) ↦ dt/t` | `QOU/GaussManin/TateCurveCusp.lean` | **done, this PR** |
| **M2** | Algebraic Gauss–Manin connection on `H¹_dR` of a Weierstrass family over a differential ring: basis `ω = dx/(2y+a₁x+a₃)`, `η = xω`, connection matrix in `c₄, c₆, Δ` and the derivation; Picard–Fuchs. Pure algebra. | `QOU/GaussManin/` | next |
| **M2b** | On `E_q` with `θ = q d/dq`: the Ramanujan system (`θE₄ = (E₂E₄ − E₆)/3`, …) and `θΔ = E₂Δ`. Needs divisor-sum convolution identities; the hardest algebraic step. | `QOU/GaussManin/` | multi-week |
| **M3** | Formal group of `E_q` at the origin is `𝔾̂ₘ` (Tate parameter); link to `QOU.FormalGroups.multiplicative`. Vanishing-cycle period `= ∮ dt/t = 2πi` via `GmPeriod.gm_period`. Monodromy at `q = 0` is unipotent `[[1,1],[0,1]]` (Picard–Lefschetz), rank-2 weight filtration. | algebra in `QOU/GaussManin/`, the period in `QOU/Transcendental/` | after M1 |
| **M4** | The τ-functor: how the Hecke `q` maps to the period domain. Owner's decision (core definition). Candidates below. | — | **card to Carl** |
| **M5** | Given M4: build `GermPeriodShare` from Φ, i.e. show the two Hecke channels `e±` map to the two graded pieces of `H¹(E)` and the per-channel share of the period normalisation is equal. The rational must come out of the construction, not be chosen. | `QOU/GaussManin/`, `QOU/Transcendental/` | after M4 |
| **M6** | Assemble with Clause A: `μ₁ = 1/(8π)` as a theorem with only `HeatKernelLeadingCoeff` left as hypothesis. | `QOU/Transcendental/` | last |

## M4 candidates (for the owner)

1. **Keep Φ an open hypothesis; build M1–M3 and the germ route.** No core change. Research
   the germ-curvature route (`qou-rrgk`) for a `τ(q)` defined as the period ratio of the
   germ holonomy. Recommended now.
2. **Define the τ-functor as the Tate family over the formal Hecke parameter.** Φ becomes
   algebraic in `ℤ[[q]]` and M5 is in reach, but the normalisation `τ(q₀) = τ₀` is dropped
   and `E_q` at the anchor is not Bring's factor. Core-definition change.
3. **Define Φ by a modular parameter of `X₀(5)`** (the isogeny that `Jac(Bring)` carries),
   with the Hecke `q` entering through a Hauptmodul. Core-definition change, and the choice
   of Hauptmodul must be forced, not selected.
