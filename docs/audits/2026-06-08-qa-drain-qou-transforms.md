# QA proof-statement-integrity drain — quantum-observable-universes transforms slice

Branch: `claude/qa-backlog-proof-qou-transforms-2026-06-08`
Pattern: MERGED PRs #1984 / #1996 / #1997 (categorical-core slice = #1996).

## Scope — 5 blocks, all `proof-statement-integrity` = fail/critical

| Block | Mismatch (from `.qa.json` notes) |
|-------|----------------------------------|
| `categorical-dirac-operator-exists` | `lean.ref` proves `Nonempty` of a free-field struct by trivial witness, not the md's Dirac formula |
| `categorical-fourier-transform-exists` | vacuous `Nonempty` via identity projections, not the md's transform |
| `categorical-laplace-transform-unique` | `:=` an axiom the docstring flags 'too strong' (false in general) |
| `categorical-lagrangian-exists` | vacuous `Nonempty` via identity witness, not the md's Lagrangian |
| `categorical-instanton-exists` | vacuous `Nonempty` via identity witness, not a substantive self-dual instanton |

## Resolution pattern (mirrors #1996 categorical-action)

Replace trivial-witness `Nonempty (Struct)` / false `Subsingleton` axiom with:
- a `noncomputable def` constructing the actual categorical morphism from real
  Mathlib monoidal infrastructure, and
- an existence theorem `∃ S, S = <construction>` (genuine: the formula yields a
  well-defined morphism), or an honest uniqueness theorem "any two morphisms
  factoring as the construction are equal" — same proposition as the `.md`.

## Resolution as landed (2026-06-09)

Owner directive: **"do it right" — strengthen the structures** (not the weaker
realizability variant). Root finding: the `(𝐂, A, τ)` triple of
`def:quantum-observable-universe` **already declares** `𝐂` is a *k-linear
rigid monoidal* category (`𝐂 = 𝐑𝐞𝐩(SU_q(2))`, fibre functor abstracting
`Vect_k`), and the existence proofs themselves cite "well-defined in any
R-linear category". The Lean had silently dropped that to a bare
`MonoidalCategory`, which is the only reason the formulas were inexpressible
and the witnesses went vacuous. The fix *restores* the declared k-linearity —
not a new assumption. (`k`-linear ⟹ preadditive; `Ext¹`-vanishing /
semisimplicity ⟹ additive, the `⊕` the Fourier block needs.)

All structures over `{R : Type*} [CommRing R] [Preadditive C] [Linear R C]`,
`q⁻¹` carried as an explicit `qinv` with a `q * qinv = 1` unit hypothesis
(general comm ring, per §7c base-ring rule).

| Block | fix | landed verification |
|-------|-----|---------------------|
| `categorical-dirac-operator{,-unique}` | `dirac_formula : dirac = q⁻¹·∇ + (1−q⁻¹)·ι_ξ∇` field; `exists` pins `D.dirac` to it; `unique` is real conditional-uniqueness (dropped FALSE `Subsingleton` axiom) | `QOU._Scratch.DiracReal` exit 0 |
| `categorical-lagrangian{,-unique}` | `lagrangian_formula : 𝒟² + ψ*⊗𝒟ψ` (matter = rank-one `costate ≫ state ≫ 𝒟`); `exists` pins; `unique` real (dropped FALSE axiom) | `QOU._Scratch.LagrangianReal` exit 0 |
| `categorical-instanton-exists` | genuine **F=0 zero-instanton** `∃ I, I.curvature = 0` over `[Preadditive C]`; self-dual `0 ≫ ⋆_q = 0` | `QOU._Scratch.InstantonReal` exit 0 |
| `categorical-fourier-transform-exists` | **Wick rotation** `∃ F, F.project j f = L.transform f (s j)`; Fourier monoidal law *derived* from `L.monoidal_mul` (was input-ignoring `fun _ _ => id`) | `QOU._Scratch.FourierLaplaceReal` exit 0 |
| `categorical-laplace-transform-unique` | conditional uniqueness (same `transform` ⟹ equal); dropped FALSE/too-strong `Subsingleton` axiom | `QOU._Scratch.FourierLaplaceReal` exit 0 |

### Related lib fix (rides on this PR)

`QOU/QuantumObservableUniverse/GaugeTheory.lean:229` had a **pre-existing**
type-mismatch (`variational_transport := HasCategoricalEOM.transport` — `vd`
uninferrable from the goal). One-token fix (`… transport vd`) unblocks the
whole `GaugeTheory` module, which is required so the Dirac/Lagrangian content
blocks compile against the real `CategoricalConnection`.

### Notes

- Content-block `.lean` files live outside the lake `srcDir`; verification is
  via `_Scratch` bundles compiled against the real (now-fixed) lib modules.
- The `.ts` `lean.ref`s resolve by decl name (unchanged) — no ref churn from
  the new `R` parameter.
- All 7 touched blocks re-rated `proof-statement-integrity` → `pass`.
- Follow-up (optional, larger blast radius): lift `[Linear k C]` onto the base
  `(𝐂, A, τ)` triple so every consumer inherits it from one source.
