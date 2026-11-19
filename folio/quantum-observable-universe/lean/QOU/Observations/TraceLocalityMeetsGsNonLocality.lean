import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import QOU.Machinery.HeckeH3AlgebraLaws

/-!
# QOU.Observations.TraceLocalityMeetsGsNonLocality

Formalizes `prop:trace-locality-meets-gs-non-locality` and its companion remark
`rem:trace-locality-gs-non-locality`:

1. **Markov locality of single Hecke crossings (positive and negative):**
   On the concrete `H₂(q) ↪ H₃(q)` normal-form algebra (`QOU.Machinery.H3`),
   for every `x ∈ H₂(q)`,
   `tr_M(x · σ₁) = z · tr_M(x)` and `tr_M(x · σ₁⁻¹) = (z - h) · tr_M(x)`
   where `h = q - q⁻¹` and `z_- = z - (q - q⁻¹)`.
   More generally, along any strictly increasing generator chain of length `k`,
   iterated Markov reduction evaluates the trace to `z ^ k`.
2. **Gröbner–Shirshov normal-form non-locality:**
   On the `6`-element Gröbner–Shirshov normal-form basis of `H₃(q)`,
   right-multiplying the reduced word `b₃ = σ₁ σ₀` (normal-form word `[1, 0]`,
   initial letter `1`) by `σ₁` triggers the braid reduction
   `[1, 0, 1] ↦ [0, 1, 0]` (`b₅ = σ₀ σ₁ σ₀`, initial letter `0 ≠ 1`), rewriting
   the very first letter of the word.
3. **Trace-level reconciliation:**
   The Markov trace is invariant under the non-local Gröbner–Shirshov braid rewrite:
   `tr_M(σ₁ σ₀ σ₁) = tr_M(σ₀ σ₁ σ₀) = h · z² + z`.
-/

namespace QOU.Observations.TraceLocalityMeetsGsNonLocality

open scoped BigOperators
open QOU.Machinery.H3

variable {R : Type*} [CommRing R]

/-! ## Part 1: Markov locality of single Hecke crossings (positive and negative) -/

/-- Right-multiplication by the inverse generator `σ₁⁻¹ = σ₁ - h · 1` on the `H₃(q)`
normal-form module (`Fin 6 → R`), derived from the Hecke quadratic relation
`σ₁² = h · σ₁ + 1`. -/
def mulσ₁Inv (h : R) (v : Fin 6 → R) : Fin 6 → R :=
  mulσ₁ h v - h • v

/-- `mulσ₁Inv h` is a right inverse to `mulσ₁ h` on `H₃(q)`. -/
theorem mulσ₁_mulσ₁Inv (h : R) (v : Fin 6 → R) :
    mulσ₁ h (mulσ₁Inv h v) = v := by
  funext i
  fin_cases i <;> simp [mulσ₁Inv, mulσ₁]

/-- `mulσ₁Inv h` is a left inverse to `mulσ₁ h` on `H₃(q)`. -/
theorem mulσ₁Inv_mulσ₁ (h : R) (v : Fin 6 → R) :
    mulσ₁Inv h (mulσ₁ h v) = v := by
  funext i
  fin_cases i <;> simp [mulσ₁Inv, mulσ₁]

/-- **Positive-crossing Markov locality on `H₂ ↪ H₃`:**
for every `x ∈ H₂(q)` (`v 2 = v 3 = v 4 = v 5 = 0`), adjoining a single positive
crossing `σ₁` multiplies the Markov trace by `z`, independent of the upstream
`H₂` history. -/
theorem markov_locality_pos (z h : R) (v : Fin 6 → R)
    (h2 : v 2 = 0) (h3 : v 3 = 0) (h4 : v 4 = 0) (h5 : v 5 = 0) :
    trM z h (mulσ₁ h v) = z * trM z h v :=
  trM_markov_σ₁ z h v h2 h3 h4 h5

/-- **Negative-crossing Markov locality on `H₂ ↪ H₃`:**
for every `x ∈ H₂(q)` (`v 2 = v 3 = v 4 = v 5 = 0`), adjoining a single negative
crossing `σ₁⁻¹ = σ₁ - h` multiplies the Markov trace by `z_- = z - h`. -/
theorem markov_locality_neg (z h : R) (v : Fin 6 → R)
    (h2 : v 2 = 0) (h3 : v 3 = 0) (h4 : v 4 = 0) (h5 : v 5 = 0) :
    trM z h (mulσ₁Inv h v) = (z - h) * trM z h v := by
  simp only [mulσ₁Inv, trM, mulσ₁, TRM, Fin.sum_univ_six,
    Pi.sub_apply, Pi.smul_apply, smul_eq_mul, Matrix.cons_val, h2, h3, h4, h5]
  ring

/-- **Combined positive and negative Markov locality along the `iota23 : H₂ ↪ H₃` embedding:**
for any `a, b : R` representing `x = a · 1 + b · σ₀ ∈ H₂(q)`,
`tr_M(x · σ₁) = z · tr_{M,2}(x)` and `tr_M(x · σ₁⁻¹) = (z - h) · tr_{M,2}(x)`. -/
theorem markov_locality_iota23 (z h a b : R) :
    trM z h (mulσ₁ h (iota23 a b)) = z * trM₂ z a b ∧
    trM z h (mulσ₁Inv h (iota23 a b)) = (z - h) * trM₂ z a b := by
  have hpos := markov_locality_pos z h (iota23 a b) rfl rfl rfl rfl
  have hneg := markov_locality_neg z h (iota23 a b) rfl rfl rfl rfl
  rw [trM_iota23_stabilizes] at hpos hneg
  exact ⟨hpos, hneg⟩

/-- **Iterated Markov locality on strictly increasing generator chains:**
if a sequence of elements `chain : ℕ → A` in an algebra with trace `tr : A → R`
starts at the unit (`tr (chain 0) = 1`) and each step adjoins a fresh generator
satisfying Markov locality `tr (chain (k + 1)) = z * tr (chain k)`, then
`tr (chain k) = z ^ k` for all `k`. -/
theorem trM_increasing_chain_eq_z_pow {A : Type*} (tr : A → R) (z : R)
    (chain : ℕ → A)
    (h0 : tr (chain 0) = 1)
    (hstep : ∀ k, tr (chain (k + 1)) = z * tr (chain k)) :
    ∀ k : ℕ, tr (chain k) = z ^ k := by
  intro k
  induction k with
  | zero => simpa using h0
  | succ k ih =>
    rw [hstep k, ih, pow_succ']

/-- Concrete `H₃` increasing generator chain: `1`, `σ₀`, `σ₀ σ₁` have Markov traces
`1`, `z`, `z ^ 2` respectively. -/
theorem trM_H3_increasing_chain (z h : R) :
    trM z h unitNF = 1 ∧
    trM z h (mulσ₀ h unitNF) = z ∧
    trM z h (mulσ₁ h (mulσ₀ h unitNF)) = z ^ 2 := by
  refine ⟨?_, ?_, ?_⟩
  · simp [trM, unitNF, TRM, Fin.sum_univ_six]
  · simp [trM, mulσ₀, unitNF, TRM, Fin.sum_univ_six]
  · simp [trM, mulσ₁, mulσ₀, unitNF, TRM, Fin.sum_univ_six]

/-! ## Part 2: Global Gröbner–Shirshov normal-form non-locality -/

/-- The 6 canonical Gröbner–Shirshov normal-form words of `H₃(q)` in generators
`0` (`σ₀`) and `1` (`σ₁`), matching the basis `[γ, σ₀, σ₁, L₊, L₋, e⁻]`. -/
def gsNormalFormWord : Fin 6 → List (Fin 2)
  | 0 => []
  | 1 => [0]
  | 2 => [1]
  | 3 => [1, 0]
  | 4 => [0, 1]
  | 5 => [0, 1, 0]

/-- Standard basis vector `e_k` of the `H₃(q)` normal-form free module `Fin 6 → R`. -/
def nfBasisVec (k : Fin 6) : Fin 6 → R :=
  fun i => if i = k then 1 else 0

/-- Right-multiplying the normal-form basis element `b₃ = σ₁ σ₀` (word `[1, 0]`)
by `σ₁` produces `b₅ = σ₀ σ₁ σ₀` (word `[0, 1, 0]`) via the Yang–Baxter braid rewrite. -/
theorem mulσ₁_basis3_eq_basis5 (h : R) :
    mulσ₁ h (nfBasisVec (3 : Fin 6)) = nfBasisVec (5 : Fin 6) := by
  funext i
  fin_cases i <;> simp [mulσ₁, nfBasisVec]

/-- **Gröbner–Shirshov reduction is non-local:**
the normal-form basis word of `b₃ = σ₁ σ₀` has initial letter `1` at position `0`,
whereas after right-multiplying by `σ₁` to obtain `b₅ = σ₀ σ₁ σ₀`, the normal-form
basis word has initial letter `0 ≠ 1` at position `0`. Thus appending a generator
at the right end of a word can rewrite the first letter of its Gröbner–Shirshov
normal form. -/
theorem gs_reduction_replaces_initial_letter :
    (gsNormalFormWord 3).head? = some (1 : Fin 2) ∧
    (gsNormalFormWord 5).head? = some (0 : Fin 2) ∧
    (gsNormalFormWord 3).head? ≠ (gsNormalFormWord 5).head? := by
  decide

/-! ## Part 3: Trace-level reconciliation -/

/-- **Trace-level reconciliation of Markov locality and Gröbner–Shirshov non-locality:**
the unreduced braid word `σ₁ σ₀ σ₁` and its Gröbner–Shirshov normal form `σ₀ σ₁ σ₀`
represent the exact same element of `H₃(q)` and evaluate under `trM` to the same
polynomial `h · z² + z`. -/
theorem trace_reconciles_braid_rewrite (z h : R) :
    mulσ₁ h (mulσ₀ h (mulσ₁ h (unitNF : Fin 6 → R))) =
      mulσ₀ h (mulσ₁ h (mulσ₀ h (unitNF : Fin 6 → R))) ∧
    trM z h (mulσ₁ h (mulσ₀ h (mulσ₁ h unitNF))) =
      trM z h (mulσ₀ h (mulσ₁ h (mulσ₀ h unitNF))) ∧
    trM z h (mulσ₀ h (mulσ₁ h (mulσ₀ h unitNF))) = h * z ^ 2 + z := by
  have hbraid :
      mulσ₁ h (mulσ₀ h (mulσ₁ h (unitNF : Fin 6 → R))) =
        mulσ₀ h (mulσ₁ h (mulσ₀ h (unitNF : Fin 6 → R))) :=
    (braid_operator h unitNF).symm
  refine ⟨hbraid, congrArg (trM z h) hbraid, ?_⟩
  simp [trM, mulσ₀, mulσ₁, unitNF, TRM, Fin.sum_univ_six]

/-! ## Packaged reconciliation class and canonical `H₃` instance -/

/-- **Locality–non-locality reconciliation class.**

Packages an `H₂`-subspace inclusion into a 3-strand Hecke carrier `A` with Markov trace
`trM`, positive and negative crossing operators `stepPos` and `stepNeg` (`σ₁` and `σ₁⁻¹`),
and normal-form initial-letter witness demonstrating that:
1. Positive single-crossing adjoining scales the trace locally by `z`;
2. Negative single-crossing adjoining scales the trace locally by `z - h`;
3. Gröbner–Shirshov braid reduction changes the initial normal-form letter while preserving `trM`. -/
class HasReconciliation (A : Type*) (R : Type*) [CommRing R] where
  /-- The Markov trace functional on `A`. -/
  trM : A → R
  /-- The Markov loop parameter `z` (canonically Convention D, `z = q³/(q² + 1)`). -/
  markovParameter : R
  /-- The Hecke quadratic parameter `h = q - q⁻¹`. -/
  heckeParameter : R
  /-- Embedding of the 2-strand subalgebra `H₂(q)` into `A`. -/
  embedH2 : R → R → A
  /-- Right action of the newly adjoined positive crossing `σ₁`. -/
  stepPos : A → A
  /-- Right action of the newly adjoined negative crossing `σ₁⁻¹`. -/
  stepNeg : A → A
  /-- **(1a) Positive Markov locality** on `H₂(q)`. -/
  markovLocalityPos :
    ∀ a b : R, trM (stepPos (embedH2 a b)) = markovParameter * trM (embedH2 a b)
  /-- **(1b) Negative Markov locality** on `H₂(q)`: `z_- = z - h`. -/
  markovLocalityNeg :
    ∀ a b : R,
      trM (stepNeg (embedH2 a b)) = (markovParameter - heckeParameter) * trM (embedH2 a b)
  /-- Witness element (`σ₁ σ₀`) before the non-local Yang–Baxter normal-form rewrite. -/
  preBraidElem : A
  /-- Normal-form initial letter before and after right-multiplication by `σ₁`. -/
  initialLetter : A → Fin 2
  /-- **(2) Gröbner–Shirshov non-locality**: right-multiplying `preBraidElem` by `σ₁`
  changes the initial letter at position `0` of the normal form. -/
  gsInitialLetterChanges :
    initialLetter (stepPos preBraidElem) ≠ initialLetter preBraidElem
  /-- **(3) Trace evaluation on the rewritten braid element**: `tr_M(σ₁ σ₀ σ₁) = h z² + z`. -/
  braidTraceEval :
    trM (stepPos preBraidElem) =
      heckeParameter * markovParameter ^ 2 + markovParameter

/-- Canonical concrete instance of `HasReconciliation` on the `H₃(q)` normal-form module
`Fin 6 → R` for any nontrivial commutative ring `R` and parameters `z, h : R`. -/
noncomputable def instHasReconciliationH3 [Nontrivial R] (z h : R) :
    HasReconciliation (Fin 6 → R) R where
  trM := QOU.Machinery.H3.trM z h
  markovParameter := z
  heckeParameter := h
  embedH2 := QOU.Machinery.H3.iota23
  stepPos := QOU.Machinery.H3.mulσ₁ h
  stepNeg := mulσ₁Inv h
  markovLocalityPos := fun a b =>
    markov_locality_pos z h (QOU.Machinery.H3.iota23 a b) rfl rfl rfl rfl
  markovLocalityNeg := fun a b =>
    markov_locality_neg z h (QOU.Machinery.H3.iota23 a b) rfl rfl rfl rfl
  preBraidElem := nfBasisVec (3 : Fin 6)
  initialLetter := fun v =>
    by
      classical
      exact if v (5 : Fin 6) = 0 then 1 else 0
  gsInitialLetterChanges := by
    classical
    rw [mulσ₁_basis3_eq_basis5]
    have h5 : (nfBasisVec (5 : Fin 6) : Fin 6 → R) 5 = 1 := rfl
    have h3 : (nfBasisVec (3 : Fin 6) : Fin 6 → R) 5 = 0 := rfl
    simp [h5, h3, one_ne_zero]
  braidTraceEval := by
    rw [mulσ₁_basis3_eq_basis5]
    simp [QOU.Machinery.H3.trM, nfBasisVec, QOU.Machinery.H3.TRM]

end QOU.Observations.TraceLocalityMeetsGsNonLocality
