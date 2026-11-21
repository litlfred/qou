# 2026-11-20 — 𝒩_sym = tr_F(e_sym^EW · e_H): what the trace algebra allows

Block: `conj:g-action-on-substrate`
(`folio/quantum-observable-universe/quantum-observable-universes/g-action-on-substrate.md`).
Owner ruling 2026-11-20: the host is left open until a structural derivation decides.
Lean: `QOU.QuantumObservableUniverses.NSymTraceAlgebra`
(`folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverses/NSymTraceAlgebra.lean`),
lean-direct exit 0 with `-DautoImplicit=false -s 65536`, no `sorry`, axioms
`[propext, Classical.choice, Quot.sound]` only. The 213.11 target was not used.

## Trace used

The corpus has no constructed pivotal trace of `Rep(SU_q(2))`. `tr_F` is modelled by
`CyclicTrace` (`HiggsVacuumResidual.lean`): additive, `K`-homogeneous and cyclic on a
`K`-linear category, `K` any field. Multiplicativity on `⊗` is a further hypothesis,
`MonoidalCyclicTrace`. `Matrix.trace` satisfies both (`Matrix.trace_kronecker`), but no
instance is built in Lean.

## The formula has two independent choices

`e_sym^EW · e_H` hides two separate choices.

**Choice 1: how `e_sym` and `e_H` combine.**

- *Composite* (`·` = `≫`, both endomorphisms of one object). `PointCopoint.tr_comp_proj`:
  `tr(f ≫ e_H) = t⁻¹ s · tr(𝟙_U)`, where `s` is the vacuum matrix element
  `ϱ ≫ f ≫ ϱ* = s • 𝟙`. The host dimension `tr(𝟙_X)` does not appear. If `f` is an
  idempotent that commutes with `e_H`, then `s ∈ {0, t}`
  (`PointCopoint.vacuum_coeff_dichotomy`). With the unit-normalised trace of (G-4),
  `tr(e_sym ≫ e_H) ∈ {0, 1}` (`VacuumPairing.tr_comp_proj_zero_or_one`). If the two
  idempotents sit on different summands of a biproduct, the composite is `0` and so is
  its trace (`onLeft_comp_onRight`, `tr_onLeft_comp_onRight`).
- *Tensor* (`·` = `⊗`, `e_sym ⊗ e_H` on `X ⊗ A^{(H)}`). `VacuumPairing.tr_tensor_proj`:
  `tr(f ⊗ e_H) = tr f`. The Higgs factor contributes `1`.

So, **proved, scope (b), invariant = cyclicity plus the rank-one factorisation of
`e_H` through `𝟙`:** under the composite reading, `tr_F(e_sym^EW · e_H)` is a vacuum
expectation value. For a commuting idempotent it is `0` or `1`, and it is never a sum or
product of host `q`-dimensions. A `q`-dimension-valued 𝒩_sym requires the tensor
reading, and then 𝒩_sym = `tr_F(e_sym^EW)`. Commutation is a hypothesis of the
dichotomy. Without it the value is still `t⁻¹ s`, a vacuum matrix element, but it need
not be `0` or `1`.

**Choice 2: the electroweak host.** Once the tensor reading is fixed,
𝒩_sym = `tr_F(e_sym^EW)`. Taking `e_sym^EW` to be the identity on each host, as (G-2)
does, gives:

- direct sum, as (G-1) states: `tr(𝟙(X ⊞ Y)) = tr 𝟙X + tr 𝟙Y` (`CyclicTrace.tr_id_biprod`,
  from cyclicity alone), so the value is `2[4]_q + [6]_q ≈ 14.607451551764766`;
- tensor product: `tr(𝟙(X ⊗ Y)) = tr 𝟙X · tr 𝟙Y` (`MonoidalCyclicTrace.tr_id_tensor`), so
  the value is `[4]_q²[6]_q ≈ 107.89152433518721`.

Here `[4]_{q₀} ≈ 4.1096824358`, `[6]_{q₀} ≈ 6.3880866802`, symmetric `[n]_q`,
`q₀ = 1.10997859564273904668`, mpmath at 50 dps.

The trace algebra does **not** decide Choice 2. Both rules hold for the same trace, and
which one applies depends on what object the electroweak host is. (G-1) states a direct
sum. The tensor rule needs a monoidal structure on the hosts that the corpus does not
supply.

## Verdict

Partial resolution.

- **Choice 1 is resolved.** Composition cannot give a `q`-dimension, so the formula is
  meaningful as a `q`-dimension only as `e_sym^EW ⊗ e_H`. The trace is then taken on
  `A^{EW} ⊗ A^{(H)}`, a tensor power of `A`, not on `A` as (G-1) has it. Also, (G-4)'s
  factor `1` then contributes nothing.
- **Choice 2 is not resolved.** It is a question about the host object, which the trace
  algebra cannot settle. Under (G-1) as stated, the value is `2[4]_q + [6]_q`.

The 213.11 target was not consulted.
