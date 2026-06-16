/-
Copyright (c) 2026 litlfred. All rights reserved.

# Markov trace on Hecke algebras — scaffold (2026-06-04)

This file scaffolds the Markov-trace infrastructure on Iwahori-Hecke
algebras `H_n(q)` needed for the Q_β residue A composite-operator
identification (paths B, C, D in
`docs/scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md`).

## What this provides

A type-level scaffold for:
- The Hecke algebra `H_n(q)` (axiomatised; Mathlib has only basic stub)
- The Markov trace `tr_M : H_n(q) → R` as a linear functional
- Class `MarkovTraceCompatibility` axiomatising the Markov properties:
  (M1) Linearity, (M2) Conjugation invariance, (M3) Markov reduction
       `tr_M(x · σ_{n-1}) = z · tr_M(x)` for `x ∈ H_{n-1}`

## Cross-refs

- `QBetaCategoricalPrecisionLadder.lean` (`τ_M(T_β)` is the canonical Q_β source)
- Audit: [`docs/scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md`](../../../../../docs/scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md)
- CLAUDE.md §"Hecke-Skein convention"
- [wenzl1988] doi:10.1007/BF01239526 (Markov trace on H_n(q))
-/

import Mathlib.Algebra.Algebra.Defs
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases

namespace QOU.Machinery

/-! ## Hecke algebra `H_n(q)` — abstract scaffold

The Iwahori-Hecke algebra is presented as a quotient of the braid
group algebra of `B_n` by the relation `(σ_i - q)(σ_i + q⁻¹) = 0`
(CLAUDE.md §7a Hecke-Skein convention). Mathlib has only a basic
stub; here we axiomatise the structure for downstream consumers. -/

/-- The **Iwahori-Hecke algebra** `H_n(q)` as an abstract type-class
over a commutative ring `R` and parameter `q : R`. The instance is
the open infrastructure work — Mathlib lacks `H_n(q)` for n ≥ 3. -/
class HeckeAlgebra (R : Type*) [CommRing R] (q : R) (n : ℕ) (H : Type*) [Ring H] [Algebra R H] : Prop where
  /-- Hecke algebra structure on `H` (opaque marker for the open
  infrastructure work; instance gates the categorical promotion). -/
  hecke_structure : True

/-! ## Markov trace as a linear functional -/

/-- A **Markov trace** on `H_n(q)` is a linear functional satisfying
the Markov reduction property.

**Opaque-marker scaffold (honest framing).** This class is a single
`True`-valued marker — it does NOT encode the Markov laws (linearity,
conjugation invariance, `tr (x · σ_{n-1}) = z · tr (x)`) as Lean
propositions, because doing so requires the full `HeckeAlgebra` module
structure that Mathlib lacks for `n ≥ 3`. Downstream code that needs
the actual laws must wait for the real development; this marker only
records the intent at the type-class layer (§3b-cond pattern). The
three laws are listed in the field docstring as documentation of what
the eventual instance must supply — they are NOT currently enforced. -/
class MarkovTrace (R H : Type*) [CommRing R] [Ring H] [Algebra R H]
    (tr : H → R) : Prop where
  /-- Opaque marker. The eventual real instance must supply: (M1)
  linearity (`tr` is `R`-linear), (M2) conjugation invariance
  (`tr (x·y) = tr (y·x)`), (M3) Markov reduction
  (`tr (x·σ_{n-1}) = z·tr (x)` for `x ∈ H_{n-1}`). None enforced yet. -/
  markov_properties : True

/-! ## Jones-Wenzl projector + Markov-trace evaluation -/

/-- The **Jones-Wenzl projector** `p_n ∈ H_n(q)` is the idempotent
projecting onto the (n)-irreducible component.

**Opaque-marker scaffold.** Single `True` marker; the real instance
must supply idempotence (`p·p = p`) and the strand-killing relation
(`p·σ_i = -q⁻¹·p` for `i < n-1`). Neither is enforced here — they are
documented as the eventual instance's obligations (§3b-cond). -/
class JonesWenzlProjector (R H : Type*) [CommRing R] [Ring H] [Algebra R H]
    (q : R) (n : ℕ) (p : H) : Prop where
  /-- Opaque marker. Eventual instance must supply idempotence and the
  strand-killing relation; neither enforced yet. -/
  jw_properties : True

/-! ## Conditional class: residue A as a Markov-trace residue

The Q_β residue A at `u_substrate` is conjecturally the Markov-trace
residue of a composite Wenzl × Demazure operator (path D). This is
captured as a conditional class. -/

/-- Conditional class for the residue A composite identification.
NEAR-MATCH tier; instance not constructed (requires upstream Wenzl,
Markov trace, and Demazure-crystal infrastructure to be in place).

The composite operator is `(Wenzl projector p_3) × (Demazure char χ_λ)`,
evaluated at proton-pinned q₀; the Markov-trace residue at the
`u_substrate` pole is conjecturally `A = c_3 (Hopf-Jones value) +
q-Pochhammer correction`. -/
class ResidueACompositeIdentification : Prop where
  /-- Composite Wenzl × Demazure operator has well-defined Markov-trace
  residue at `u_substrate` (opaque marker for the open derivation). -/
  composite_markov_residue : True

/-! ## Concrete `H₃(q)` Markov trace — the real structure

This realizes the `MarkovTrace` intent above for `n = 3` with an explicit
linear functional on the NF free module `Fin 6 → R`, replacing the
`True` marker with proved laws. The NF basis order is
`[γ, σ₀, σ₁, L₊, L₋, e⁻]`, identical to `gram.NF_BASIS`; the data mirror
`computations/.../gram.py` (`hm`, `TR_M`) and the
symbolic `pyhecke.trace_formal`. The mathematics is cross-verified in
Python against `gram.py` (randomized) and over ℚ(s) by
`tools/pyhecke/tests/test_trace_formal.py`. -/
namespace H3

variable {R : Type*} [CommRing R]

/-- Markov-Ocneanu-Wenzl weights on the GB-NF basis `[γ, σ₀, σ₁, L₊, L₋,
e⁻]` of `H₃(q)` (mirrors `gram.TR_M` / `trace_formal.TR_M_formal`):
`tr_M(e⁻) = h·z² + z` — the 2026-05-19 fix, NOT `z³`. `z` is the Markov
parameter, `h = q − q⁻¹`. -/
def TRM (z h : R) : Fin 6 → R := ![1, z, z, z ^ 2, z ^ 2, h * z ^ 2 + z]

/-- The **Markov trace** on the NF free module `Fin 6 → R`: the linear
functional `v ↦ ∑ᵢ vᵢ · TRMᵢ`. The real structure behind the `True`
marker. -/
def trM (z h : R) (v : Fin 6 → R) : R := ∑ i, v i * TRM z h i

/-- Right action of `σ₀` on the NF basis (mirrors `gram.hm(·,1,0,0)`). -/
def mulσ₀ (h : R) (v : Fin 6 → R) : Fin 6 → R :=
  ![v 1, v 0 + h * v 1, v 3, v 2 + h * v 3, v 5, v 4 + h * v 5]

/-- Right action of `σ₁` on the NF basis (mirrors `gram.hm(·,1,0,1)`). -/
def mulσ₁ (h : R) (v : Fin 6 → R) : Fin 6 → R :=
  ![v 2, v 4, v 0 + h * v 2, v 5, v 1 + h * v 4, v 3 + h * v 5]

/-- The **full algebra product** `u · v` on the NF free module of `H₃(q)`.

Each basis element `b_j` is the GB normal form of a generator word `W_j`,
and right-multiplication is an anti-homomorphism `R_{ab} = R_b ∘ R_a`, so
`u · b_j = R_{W_j}(u)` is the composite of `mulσ₀`/`mulσ₁` along `W_j`. By
right-linearity `u · v = ∑_j v_j · (u · b_j)`. The producing words (and
hence the composition order — note `b₃ = σ₁σ₀`, `b₄ = σ₀σ₁`) were pinned by
the symbolic preflight in `gram.py`'s `hm` convention, which also verified
`tr_M(u·v) = tr_M(v·u)` as an identity over `ℚ(z,h)`:

| `j` | basis `b_j` | word `W_j` | `u · b_j` |
|----|------------|-----------|-----------|
| 0 | `γ`  | `()`      | `u` |
| 1 | `σ₀` | `(0)`     | `mulσ₀ u` |
| 2 | `σ₁` | `(1)`     | `mulσ₁ u` |
| 3 | `L₊` | `(1,0)`   | `mulσ₀ (mulσ₁ u)` |
| 4 | `L₋` | `(0,1)`   | `mulσ₁ (mulσ₀ u)` |
| 5 | `e⁻` | `(0,1,0)` | `mulσ₀ (mulσ₁ (mulσ₀ u))` | -/
def mulNF (h : R) (u v : Fin 6 → R) : Fin 6 → R := fun i =>
    v 0 * u i
  + v 1 * mulσ₀ h u i
  + v 2 * mulσ₁ h u i
  + v 3 * mulσ₀ h (mulσ₁ h u) i
  + v 4 * mulσ₁ h (mulσ₀ h u) i
  + v 5 * mulσ₀ h (mulσ₁ h (mulσ₀ h u)) i

/-- **(M1) Linearity** — additivity. -/
theorem trM_add (z h : R) (u v : Fin 6 → R) :
    trM z h (u + v) = trM z h u + trM z h v := by
  simp only [trM, Pi.add_apply, add_mul, Finset.sum_add_distrib]

/-- **(M1) Linearity** — homogeneity. -/
theorem trM_smul (z h c : R) (v : Fin 6 → R) :
    trM z h (c • v) = c * trM z h v := by
  simp only [trM, Pi.smul_apply, smul_eq_mul, Finset.mul_sum]
  exact Finset.sum_congr rfl (fun i _ => by ring)

/-- **(M3) Hecke relation** as an operator identity: `σ₀² = h·σ₀ + 1`. -/
theorem mulσ₀_hecke (h : R) (v : Fin 6 → R) :
    mulσ₀ h (mulσ₀ h v) = h • mulσ₀ h v + v := by
  funext i
  fin_cases i <;>
    simp [mulσ₀, Pi.add_apply, Pi.smul_apply, smul_eq_mul] <;> ring

/-- **(M3) Markov reduction** `tr(x·σ₁) = z·tr(x)` for
`x ∈ H₂ = span{γ, σ₀}` (i.e. `v 2 = v 3 = v 4 = v 5 = 0`). The defining
Markov property at the `H₂ ↪ H₃` inclusion. -/
theorem trM_markov_σ₁ (z h : R) (v : Fin 6 → R)
    (h2 : v 2 = 0) (h3 : v 3 = 0) (h4 : v 4 = 0) (h5 : v 5 = 0) :
    trM z h (mulσ₁ h v) = z * trM z h v := by
  simp only [trM, mulσ₁, TRM, Fin.sum_univ_six, Matrix.cons_val, h2, h3, h4, h5]
  ring

/-- **(M2) Trace cyclicity** `tr_M(u · v) = tr_M(v · u)` — the defining
property of a *trace*, here for the full `H₃(q)` algebra product `mulNF`.
This is what makes `trM` an honest Markov **trace** (not merely a Markov-
reducible functional), and it is exactly the symmetry the `Ind_{H₃}^{H₄}`
Markov-stabilization analysis relies on. Verified over `ℚ(z,h)` by the
symbolic preflight before being formalized; the identity is a polynomial
in the entries of `u`, `v` and the parameters `z, h`, closed by `ring`
after the trace sum and the nested `mulσ` actions are unfolded. -/
theorem trM_cyclic (z h : R) (u v : Fin 6 → R) :
    trM z h (mulNF h u v) = trM z h (mulNF h v u) := by
  simp only [trM, mulNF, mulσ₀, mulσ₁, TRM, Fin.sum_univ_six,
    Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]
  ring

/-- The concrete n=3 trace is a **real** linear functional satisfying the
Markov **trace** laws — no longer a `True` marker. Bundles (M1) linearity,
(M2) cyclicity, and (M3) the Markov reduction; the bridge for discharging
`markov_trace_origin` once Step 4 names the residue-A element. -/
theorem markovTrace_realized (z h : R) :
    (∀ u v, trM z h (u + v) = trM z h u + trM z h v) ∧
    (∀ c v, trM z h (c • v) = c * trM z h v) ∧
    (∀ u v, trM z h (mulNF h u v) = trM z h (mulNF h v u)) ∧
    (∀ v : Fin 6 → R, v 2 = 0 → v 3 = 0 → v 4 = 0 → v 5 = 0 →
       trM z h (mulσ₁ h v) = z * trM z h v) :=
  ⟨trM_add z h, trM_smul z h, trM_cyclic z h, trM_markov_σ₁ z h⟩

end H3

end QOU.Machinery
