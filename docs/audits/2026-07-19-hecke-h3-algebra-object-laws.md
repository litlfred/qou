# H₃(q) NF module certified as an algebra object — categorical source-category brick (2026-07-19)

**Bean:** `qou-hxct` (categorical tranche on the F1/F2 source-category gap).
**Lean:** [`QOU/Machinery/HeckeH3AlgebraLaws.lean`](../../content/quantum-observable-universe/lean/QOU/Machinery/HeckeH3AlgebraLaws.lean)
— sorry-free, `lean`-direct exit 0, no linter warnings. §7c-generic
(`[CommRing R]` throughout, no ℝ).

**Scope guard (STRICT):** no instance of `HeckeBraidedPresentation` or
`MarkovStabilization` is declared — those classes quantify `σ : ℕ → H` (the
H_∞ inductive limit) and no finite-level padding satisfies them (σᵢ := 1
forces `(q−q⁻¹)•1 = 0` via the quadratic; σᵢ := σ₁ violates far
commutation). The general-n classes stay OPEN. Nothing wired; `1/(8π)`
stays phase-4.

## What was missing

`QOU.Machinery.H3` carried the Markov-trace laws (M1 linearity, M2
cyclicity, M3 reduction) but **not** the facts making the NF module an
honest *algebra object*: no associativity, no unit laws, no bilinearity, no
braid relation, no σ₁ quadratic. Without these, nothing instance-level can
ever be built on the concrete rung — the whole F1/F2 source-category story
rested on an object not yet certified to be an algebra.

## What is now proved (all sorry-free)

| Layer | Theorems |
|---|---|
| **Presentation laws at n=3, completed** | `mulσ₁_hecke` (σ₁² = h·σ₁ + 1, partner of the existing `mulσ₀_hecke`); **`braid_operator`** (σ₀σ₁σ₀ = σ₁σ₀σ₁ — the Yang–Baxter / hexagon shadow, the F2 datum). All three `HeckeBraidedPresentation` field contents now realized concretely at n=3 (far commutation vacuous with two generators). |
| **Algebra-object laws** | `mulNF_add_left/right`, `mulNF_smul_left/right` (R-bilinearity); `mulNF_one_left/right` (unit γ = e₀, including `word_j(γ) = b_j`); **`mulNF_assoc`** (`(u·v)·w = u·(v·w)` — the load-bearing law, closed by `ring` per NF entry in ~14 s). |
| **H₂ ↪ H₃ stabilization rung** | `iota23_mul` (the inclusion is multiplicative — the rank-one Hecke quadratic maps to the NF product); **`trM_iota23_stabilizes`** (`trM(ι x) = trM₂ x`, weights (1, z)); `trM₂_cyclic`. Together with the existing `trM_markov_σ₁`, the complete concrete content of the n = 2→3 Tier-2 stabilization base case. |

## Why this is the right categorical brick

The τ-functor wall analysis (`TauFunctorReduction`, target spec) reduces
"construct τ" to: the general-n Markov trace, the `TauRhoHodgeLift`
instance, and the F1/F2 Hecke-category infrastructure. This file certifies
the **concrete algebra object** all three legs stand on: the n=3 rung is
now an associative unital R-algebra with a proved Markov trace and proved
braid relations — the first tier of the source category 𝐂 that exists as
verified mathematics rather than as class fields. Next mechanical steps it
unlocks (not done here): a `Ring`/`Algebra R` instance wrapper for the NF
module, the **first `MarkovTrace` class instance** (all fields already
proved), and the H₄ table via the confluent `gb_nf_reducer.rs` route
documented in `MarkovTraceOnHecke`.

## Plan state

```
F-construction (qou-a46k): T1–T4 merged; T5 brick #4050 (parameter-free target)
Source category (F1/F2):   n=3 algebra object CERTIFIED (this)
                           general-n presentation / stabilization  OPEN
TauRhoHodgeLift instance:  OPEN — THE wall
```
