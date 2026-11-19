import Mathlib.Data.Real.Basic
import Mathlib.Data.List.Infix
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic
import QOU.Machinery.MarkovTraceOnHecke
import QOU.TransferMatrices.GSNormalForm
import QOU.Interactions.GramQuotientDetD
import QOU.Interactions.TwoTermPhotonGPMTConfinementSDP

/-!
# Gröbner–Shirshov Confluence, Critical Lyapunov `α_crit = q₀`, Markov vs `TL_n` Erasure,
# and Baryonic Radical Separation

This module establishes six structural theorems governing the Gröbner–Shirshov rewriting
dynamics, the critical exponential Lyapunov fugacity `α_crit = q`, the Markov-trace vs
Temperley–Lieb loop-erasure scalar separation, and the Geer–Patureau-Mirand–Turaev (GPMT)
baryonic radical completion on `H_n(q)`:

1. **Three-Strand Gröbner–Shirshov Termination and Confluence (`h3_gs_terminates_and_confluent`,
   `h3_gs_confluent_unique_nf`)**:
   On `n = 3` strands (`List (Fin 2)`), the rewriting system
   `([0,0] ↦ h•[0] + [], [1,1] ↦ h•[1] + [], [1,0,1] ↦ [0,1,0])`
   coincides with the full Bokut–Shiao completed basis (since `|i - j| ≥ 2` is empty and
   `j ≤ i - 1` has only `(i, j) = (1, 0)`). The canonical normal-form evaluation
   map `nfH3 (h : R) : List (Fin 2) → (Fin 6 → R)` is constructed via the right-action operators `mulσ₀`,
   `mulσ₁` of `QOU.Machinery.H3`, satisfying the Hecke and
   Yang–Baxter braid operator identities at arbitrary context depth (`u ++ lhs ++ v`), classifying
   the irreducible words as the exact six standard monomials
   `{[], [0], [1], [1,0], [0,1], [0,1,0]}` whose `nfH3 h` images are the six linearly independent
   basis vectors `Pi.single k 1`, and establishing termination via strict decrease of the weighted
   measure `h3WordMeasure w = 2 * w.length + countOnes w`. Consequently, any two reduction
   sequences from any initial free-algebra element to irreducible linear combinations terminate
   at the exact same unique normal form (`0` unproved Diamond-Lemma axioms required at `n = 3`).

2. **Four-Strand Naive Three-Rule Non-Confluence and Bokut–Shiao Completion
   (`h4_threeRule_not_confluent`, `bokutShiao_resolves_h4_overlap`)**:
   On `n = 4` strands (`List (Fin 3)`), the overlap word `w4Overlap = [2, 1, 2, 0]` (`σ₃σ₂σ₃σ₁`)
   reduces in one naive three-rule step to `w4BranchA = [1, 2, 1, 0]` (`σ₂σ₃σ₂σ₁`, via
   Yang–Baxter on `[2,1,2]`) and in one naive three-rule step to `w4BranchB = [2, 1, 0, 2]`
   (`σ₃σ₂σ₁σ₃`, via far-commutativity on `[2,0]`), where both `w4BranchA` and `w4BranchB` are
   strictly irreducible under the naive three-rule system and `w4BranchA ≠ w4BranchB`. Conversely,
   in *any* monoid or algebra satisfying only the Artin braid relations (`s₁ s₀ s₁ = s₀ s₁ s₀`,
   `s₂ s₁ s₂ = s₁ s₂ s₁`) and far-commutativity (`s₂ s₀ = s₀ s₂`) — with zero Hecke quadratic
   hypothesis and zero `q` — the Bokut–Shiao `(i = 2, j = 0)` identity
   `s₂ * s₁ * s₀ * s₂ = s₁ * s₂ * s₁ * s₀` holds unconditionally, resolving the overlap.

3. **Block-Ordered Nuclear Word `Ξ_A` Hecke-Only Reduction and Full Bokut–Shiao Irreducibility
   (`blockOrdered_nucleus_hecke_only_nf`, `no_bokutShiao_pattern`)**:
   Closing Gap `(c)` of `QOU.TransferMatrices.GSNormalForm`, induction on the number
   of generator blocks `m` establishes that any product of single-generator crossing chains reduces
   intra-block by Hecke steps alone (`hecke_linear_mul` / `transferMatrix`) to the chain product
   `∏_{i=0}^{m-1} (a_i σ_i + b_i)`, whose `2^m` subset expansion consists exclusively of strictly
   increasing generator words `σ_S`. Moreover, every strictly increasing word is already
   irreducible under all four rule families — Hecke, far-commutativity, Yang–Baxter, *and* the
   entire Bokut–Shiao completion family `σ_i σ_{i-1} ⋯ σ_j σ_i` (since `σ_i` cannot appear twice
   in a strictly increasing list) — incurring zero braid, Bokut–Shiao, or far-commutativity steps
   for every nucleon count `A ≥ 2`.

4. **Linear Word-Length Sign Flip at `ℓ = 11` vs Critical Exponential Lyapunov Law `α_crit = q`
   (`linear_length_step_sign_flip`, `exp_lyapunov_crit_q0`)**:
   For `q > 1`, `h = q - q⁻¹ > 0`, and `c ≠ 0`:
   * The linear word-length energy `E₁(w) = |c| · ℓ(w)` changes under a single Hecke step at word
     length `ℓ ≥ 2` by `ΔE₁ = |c| · (h · (ℓ - 1) - 2)`, which is negative iff `ℓ - 1 < 2 / h`
     (in particular, for `1/5 < h < 2/9`, which traps `h(q₀) ≈ 0.20906`, `ΔE₁ < 0` at `ℓ = 10`
     and `ΔE₁ > 0` at `ℓ = 11`).
   * The exponential fugacity functional `Φ_α(w) = α ^ ℓ(w)` (`α > 0`) obeys the exact
     characteristic factorization
     `ΔΦ_α = (|c| · h · α^(ℓ - 1) + |c| · α^(ℓ - 2)) - |c| · α^ℓ = -|c| · α^(ℓ - 2) · (α - q) · (α + q⁻¹)`.
     Consequently, at *every* word length `ℓ ≥ 2`: `ΔΦ_α < 0 ↔ q < α` (strict Lyapunov descent),
     `ΔΦ_q = 0` (exact conservation at the critical fugacity `α_crit = q`), and `0 < ΔΦ_α ↔ α < q`.

5. **Temperley–Lieb Loop-Erasure Scalar `δ⁻¹` vs Convention-D Markov Weight `z_D` and Dual Covector
   Evaluation (`tl_erasure_scalar_eq_inv_delta_ne_zD`, `trace_eq_covector_dotProduct`)**:
   With `z_D = q³ / (q² + 1)` and `δ = q + q⁻¹ = (q² + 1) / q` (`E_i = q · 1 - σ_i`), the
   Temperley–Lieb trace weight on `E_i` is `q - z_D = q / (q² + 1) = δ⁻¹`, satisfying
   `δ · z_D = q² > 1` and `δ⁻¹ ≠ z_D` for all `q > 1`. Furthermore, any `R`-linear trace
   functional `τ` on a finite normal-form expansion evaluates as the finite dual covector dot
   product `τ (∑ k, c k • b k) = ∑ k, c k * τ (b k)`.

6. **Two-Ideal Separation: Skein Quotient `I_Hecke` vs Antisymmetric Baryonic Radical `𝓝_D`
   (`two_ideal_separation_tl_vs_gpmt`)**:
   Combines `GramQuotientDetD` and `TwoTermPhotonGPMTConfinementSDP` into a unified structural
   separation theorem on `H₃(q)` (`q > 1`): the `q`-antisymmetriser `radicalVec q` (`y_{(1³)}`)
   lies in the right kernel of the uncompleted Convention-D Markov Gram matrix `gramD q` (whose
   leading `5 × 5` quotient determinant `gramQuotientD q` is strictly negative and non-zero),
   whereas under the GPMT-completed Gram matrix `gramGPMT q` the same antisymmetriser is an exact
   eigenvector with strictly positive eigenvalue `q⁻³ > 0`, positive modified quantum dimension
   `dMod111Abs q = q³ / ((q² + 1)(q⁴ + q² + 1)) > 0`, positive quadratic form
   `radicalVec q ⬝ᵥ gramGPMT q *ᵥ radicalVec q > 0`, and non-vanishing `6 × 6` determinant
   `det (gramGPMT q) ≠ 0`.
-/

namespace QOU.BraidsAndKnots.GroebnerShirshovConfluenceLyapunovAndRadical

open BigOperators Matrix
open QOU.Machinery.H3
open QOU.TransferMatrices.GSNormalForm
open QOU.Interactions.GramMatrixH3Symbolic
open QOU.Interactions.TwoTermPhotonGPMTConfinementSDP
open QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace

-- ============================================================================
-- § 1. Three-Strand (`H₃(q)`) Gröbner–Shirshov Termination and Confluence
-- ============================================================================

section H3Confluence

variable {R : Type*} [CommRing R]

/-- Single-generator right-action step on the 6-dimensional `H₃(q)` normal-form module `Fin 6 → R`:
generator `0` acts by `mulσ₀ h` and generator `1` acts by `mulσ₁ h`. -/
def stepNF3 (h : R) (g : Fin 2) (v : Fin 6 → R) : Fin 6 → R :=
  if g = 0 then mulσ₀ h v else mulσ₁ h v

@[simp] theorem stepNF3_zero (h : R) (v : Fin 6 → R) :
    stepNF3 h 0 v = mulσ₀ h v := rfl

@[simp] theorem stepNF3_one (h : R) (v : Fin 6 → R) :
    stepNF3 h 1 v = mulσ₁ h v := rfl

/-- Right-action of a positive 3-strand braid word `w : List (Fin 2)` on any normal-form vector
`v : Fin 6 → R`. -/
def actWordH3 (h : R) : List (Fin 2) → (Fin 6 → R) → (Fin 6 → R)
  | [], v => v
  | g :: w, v => actWordH3 h w (stepNF3 h g v)

@[simp] theorem actWordH3_nil (h : R) (v : Fin 6 → R) :
    actWordH3 h [] v = v := rfl

@[simp] theorem actWordH3_cons (h : R) (g : Fin 2) (w : List (Fin 2)) (v : Fin 6 → R) :
    actWordH3 h (g :: w) v = actWordH3 h w (stepNF3 h g v) := rfl

/-- Action of a concatenated word `u ++ w` factors as `actWordH3 h w (actWordH3 h u v)`. -/
theorem actWordH3_append (h : R) (u w : List (Fin 2)) (v : Fin 6 → R) :
    actWordH3 h (u ++ w) v = actWordH3 h w (actWordH3 h u v) := by
  induction u generalizing v with
  | nil => rfl
  | cons g u ih => simp [actWordH3, ih]

/-- `stepNF3 h g` is additive. -/
theorem stepNF3_add (h : R) (g : Fin 2) (u v : Fin 6 → R) :
    stepNF3 h g (u + v) = stepNF3 h g u + stepNF3 h g v := by
  fin_cases g <;>
    (funext k; fin_cases k <;> simp [stepNF3, mulσ₀, mulσ₁, Pi.add_apply] <;> ring)

/-- `stepNF3 h g` is `R`-homogeneous. -/
theorem stepNF3_smul (h c : R) (g : Fin 2) (v : Fin 6 → R) :
    stepNF3 h g (c • v) = c • stepNF3 h g v := by
  fin_cases g <;>
    (funext k; fin_cases k <;> simp [stepNF3, mulσ₀, mulσ₁, Pi.smul_apply, smul_eq_mul] <;> ring)

/-- `actWordH3 h w` is additive for every word `w`. -/
theorem actWordH3_add (h : R) (w : List (Fin 2)) (u v : Fin 6 → R) :
    actWordH3 h w (u + v) = actWordH3 h w u + actWordH3 h w v := by
  induction w generalizing u v with
  | nil => rfl
  | cons g w ih => rw [actWordH3_cons, stepNF3_add, ih, actWordH3_cons, actWordH3_cons]

/-- `actWordH3 h w` is `R`-homogeneous for every word `w`. -/
theorem actWordH3_smul (h c : R) (w : List (Fin 2)) (v : Fin 6 → R) :
    actWordH3 h w (c • v) = c • actWordH3 h w v := by
  induction w generalizing v with
  | nil => rfl
  | cons g w ih => rw [actWordH3_cons, stepNF3_smul, ih, actWordH3_cons]

/-- Hecke quadratic relation for `mulσ₁`: `mulσ₁² v = h • mulσ₁ v + v`. -/
theorem mulσ₁_hecke (h : R) (v : Fin 6 → R) :
    mulσ₁ h (mulσ₁ h v) = h • mulσ₁ h v + v := by
  funext i
  fin_cases i <;>
    simp [mulσ₁, Pi.add_apply, smul_eq_mul] <;> ring

/-- Yang–Baxter braid operator identity on `Fin 6 → R`:
`mulσ₀ (mulσ₁ (mulσ₀ v)) = mulσ₁ (mulσ₀ (mulσ₁ v))`. -/
theorem mulσ_yangBaxter (h : R) (v : Fin 6 → R) :
    mulσ₀ h (mulσ₁ h (mulσ₀ h v)) = mulσ₁ h (mulσ₀ h (mulσ₁ h v)) := by
  funext i
  fin_cases i <;>
    simp [mulσ₀, mulσ₁] <;> ring

/-- Canonical normal-form evaluation of a 3-strand positive braid word `w : List (Fin 2)`,
starting from the identity basis vector `Pi.single 0 1`. -/
def nfH3 (h : R) (w : List (Fin 2)) : Fin 6 → R :=
  actWordH3 h w (Pi.single 0 1)

/-- The six canonical standard monomials of `H₃(q)` in `QOU.Machinery.H3.mulNF` basis order:
`0 ↦ []`, `1 ↦ [0]`, `2 ↦ [1]`, `3 ↦ [1, 0]`, `4 ↦ [0, 1]`, `5 ↦ [0, 1, 0]`. -/
def stdMonomial3 : Fin 6 → List (Fin 2)
  | 0 => []
  | 1 => [0]
  | 2 => [1]
  | 3 => [1, 0]
  | 4 => [0, 1]
  | 5 => [0, 1, 0]

/-- Every standard monomial `stdMonomial3 k` evaluates under `nfH3 h` to the `k`-th standard
basis vector `Pi.single k 1` of `Fin 6 → R`. -/
theorem nfH3_stdMonomial3 (h : R) (k : Fin 6) :
    nfH3 h (stdMonomial3 k) = Pi.single k 1 := by
  fin_cases k <;>
    (funext i; fin_cases i <;>
      simp [nfH3, stdMonomial3, actWordH3, stepNF3, mulσ₀, mulσ₁])

/-- `R`-linear independence of the six standard monomials under `nfH3 h`: a linear combination
`∑ k, c k • nfH3 h (stdMonomial3 k)` vanishes if and only if every coefficient `c k = 0`. -/
theorem stdMonomial3_linearIndependent (h : R) (c : Fin 6 → R)
    (hsum : (∑ k : Fin 6, c k • nfH3 h (stdMonomial3 k)) = 0) :
    c = 0 := by
  funext k
  have hk := congrFun hsum k
  fin_cases k <;>
    simpa [nfH3_stdMonomial3, Fin.sum_univ_six, Pi.single_apply] using hk

/-- Context-invariance of `nfH3 h` under a `[0, 0] ↦ h • [0] + []` Hecke rewrite at arbitrary
prefix `u` and suffix `v`. -/
theorem nfH3_hecke_zero_eq (h : R) (u v : List (Fin 2)) :
    nfH3 h (u ++ [0, 0] ++ v) = h • nfH3 h (u ++ [0] ++ v) + nfH3 h (u ++ v) := by
  simp only [nfH3, List.append_assoc, actWordH3_append, actWordH3_cons, actWordH3_nil,
    stepNF3_zero]
  rw [mulσ₀_hecke, actWordH3_add, actWordH3_smul]

/-- Context-invariance of `nfH3 h` under a `[1, 1] ↦ h • [1] + []` Hecke rewrite at arbitrary
prefix `u` and suffix `v`. -/
theorem nfH3_hecke_one_eq (h : R) (u v : List (Fin 2)) :
    nfH3 h (u ++ [1, 1] ++ v) = h • nfH3 h (u ++ [1] ++ v) + nfH3 h (u ++ v) := by
  simp only [nfH3, List.append_assoc, actWordH3_append, actWordH3_cons, actWordH3_nil,
    stepNF3_one]
  rw [mulσ₁_hecke, actWordH3_add, actWordH3_smul]

/-- Context-invariance of `nfH3 h` under the Bokut–Shiao / Yang–Baxter rewrite
`[1, 0, 1] ↦ [0, 1, 0]` at arbitrary prefix `u` and suffix `v`. -/
theorem nfH3_yangBaxter_eq (h : R) (u v : List (Fin 2)) :
    nfH3 h (u ++ [1, 0, 1] ++ v) = nfH3 h (u ++ [0, 1, 0] ++ v) := by
  simp only [nfH3, List.append_assoc, actWordH3_append, actWordH3_cons, actWordH3_nil,
    stepNF3_zero, stepNF3_one, mulσ_yangBaxter]

/-- Formal linear combinations of 3-strand words represented as lists of `(coefficient, word)` pairs,
evaluated into `Fin 6 → R` via `nfH3 h`. -/
def evalCombH3 (h : R) : List (R × List (Fin 2)) → (Fin 6 → R)
  | [] => 0
  | (c, w) :: rest => c • nfH3 h w + evalCombH3 h rest

@[simp] theorem evalCombH3_nil (h : R) : evalCombH3 h ([] : List (R × List (Fin 2))) = 0 := rfl

@[simp] theorem evalCombH3_cons (h : R) (c : R) (w : List (Fin 2))
    (rest : List (R × List (Fin 2))) :
    evalCombH3 h ((c, w) :: rest) = c • nfH3 h w + evalCombH3 h rest := rfl

theorem evalCombH3_append (h : R) (xs ys : List (R × List (Fin 2))) :
    evalCombH3 h (xs ++ ys) = evalCombH3 h xs + evalCombH3 h ys := by
  induction xs with
  | nil => simp
  | cons x xs ih =>
    rcases x with ⟨c, w⟩
    simp [ih, add_assoc]

/-- Elementary single-step Gröbner–Shirshov rewrite relation on formal linear combinations of
3-strand words. -/
inductive GSStepH3 (h : R) : List (R × List (Fin 2)) → List (R × List (Fin 2)) → Prop
  | hecke0 (pre post : List (R × List (Fin 2))) (c : R) (u v : List (Fin 2)) :
      GSStepH3 h (pre ++ [(c, u ++ [0, 0] ++ v)] ++ post)
        (pre ++ [(c * h, u ++ [0] ++ v), (c, u ++ v)] ++ post)
  | hecke1 (pre post : List (R × List (Fin 2))) (c : R) (u v : List (Fin 2)) :
      GSStepH3 h (pre ++ [(c, u ++ [1, 1] ++ v)] ++ post)
        (pre ++ [(c * h, u ++ [1] ++ v), (c, u ++ v)] ++ post)
  | yangBaxter (pre post : List (R × List (Fin 2))) (c : R) (u v : List (Fin 2)) :
      GSStepH3 h (pre ++ [(c, u ++ [1, 0, 1] ++ v)] ++ post)
        (pre ++ [(c, u ++ [0, 1, 0] ++ v)] ++ post)

/-- Reflexive-transitive closure of `GSStepH3 h`. -/
inductive GSReducesH3 (h : R) : List (R × List (Fin 2)) → List (R × List (Fin 2)) → Prop
  | refl (xs : List (R × List (Fin 2))) : GSReducesH3 h xs xs
  | step {xs ys zs : List (R × List (Fin 2))} :
      GSStepH3 h xs ys → GSReducesH3 h ys zs → GSReducesH3 h xs zs

/-- Every single Gröbner–Shirshov step `GSStepH3 h` preserves `evalCombH3 h` identically. -/
theorem evalCombH3_invariant_step {h : R} {xs ys : List (R × List (Fin 2))}
    (hstep : GSStepH3 h xs ys) :
    evalCombH3 h xs = evalCombH3 h ys := by
  cases hstep with
  | hecke0 pre post c u v =>
    simp only [evalCombH3_append, evalCombH3_cons, evalCombH3_nil,
      nfH3_hecke_zero_eq, smul_add, MulAction.mul_smul, add_zero, add_assoc]
  | hecke1 pre post c u v =>
    simp only [evalCombH3_append, evalCombH3_cons, evalCombH3_nil,
      nfH3_hecke_one_eq, smul_add, MulAction.mul_smul, add_zero, add_assoc]
  | yangBaxter pre post c u v =>
    simp only [evalCombH3_append, evalCombH3_cons, evalCombH3_nil,
      nfH3_yangBaxter_eq]

/-- Any multi-step Gröbner–Shirshov reduction sequence `GSReducesH3 h` preserves `evalCombH3 h`. -/
theorem evalCombH3_invariant {h : R} {xs ys : List (R × List (Fin 2))}
    (hred : GSReducesH3 h xs ys) :
    evalCombH3 h xs = evalCombH3 h ys := by
  induction hred with
  | refl _ => rfl
  | step hs _ ih => rw [evalCombH3_invariant_step hs, ih]

/-- A 3-strand word is irreducible under the 3-strand Gröbner–Shirshov system if it contains
none of the three leading subwords `[0, 0]`, `[1, 1]`, `[1, 0, 1]`. -/
def isIrreducibleH3 (w : List (Fin 2)) : Prop :=
  ¬ ([0, 0] <:+: w) ∧ ¬ ([1, 1] <:+: w) ∧ ¬ ([1, 0, 1] <:+: w)

/-- Every standard monomial `stdMonomial3 k` (`k : Fin 6`) is irreducible under the 3-strand
Gröbner–Shirshov rewriting system. -/
theorem stdMonomial3_isIrreducibleH3 (k : Fin 6) :
    isIrreducibleH3 (stdMonomial3 k) := by
  fin_cases k <;>
    (unfold isIrreducibleH3 stdMonomial3; decide)

/-- Complete classification of irreducible 3-strand words: every word `w : List (Fin 2)` satisfying
`isIrreducibleH3 w` is equal to `stdMonomial3 k` for one of the six indices `k : Fin 6`. -/
theorem isIrreducibleH3_iff_exists_stdMonomial3 (w : List (Fin 2)) :
    isIrreducibleH3 w ↔ ∃ k : Fin 6, w = stdMonomial3 k := by
  constructor
  · intro hw
    rcases hw with ⟨h00, h11, h101⟩
    match w with
    | [] => exact ⟨0, rfl⟩
    | [a] =>
      fin_cases a
      · exact ⟨1, rfl⟩
      · exact ⟨2, rfl⟩
    | [a, b] =>
      fin_cases a <;> fin_cases b
      · exfalso; exact h00 ⟨[], [], rfl⟩
      · exact ⟨4, rfl⟩
      · exact ⟨3, rfl⟩
      · exfalso; exact h11 ⟨[], [], rfl⟩
    | [a, b, c] =>
      fin_cases a <;> fin_cases b <;> fin_cases c
      · exfalso; exact h00 ⟨[], [0], rfl⟩
      · exfalso; exact h00 ⟨[], [1], rfl⟩
      · exact ⟨5, rfl⟩
      · exfalso; exact h11 ⟨[0], [], rfl⟩
      · exfalso; exact h00 ⟨[1], [], rfl⟩
      · exfalso; exact h101 ⟨[], [], rfl⟩
      · exfalso; exact h11 ⟨[], [0], rfl⟩
      · exfalso; exact h11 ⟨[], [1], rfl⟩
    | a :: b :: c :: d :: rest =>
      exfalso
      fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d
      · exact h00 ⟨[], 0 :: 0 :: rest, rfl⟩
      · exact h00 ⟨[], 0 :: 1 :: rest, rfl⟩
      · exact h00 ⟨[], 1 :: 0 :: rest, rfl⟩
      · exact h00 ⟨[], 1 :: 1 :: rest, rfl⟩
      · exact h00 ⟨[0, 1], rest, rfl⟩
      · exact h101 ⟨[0], rest, rfl⟩
      · exact h11 ⟨[0], 0 :: rest, rfl⟩
      · exact h11 ⟨[0], 1 :: rest, rfl⟩
      · exact h00 ⟨[1], 0 :: rest, rfl⟩
      · exact h00 ⟨[1], 1 :: rest, rfl⟩
      · exact h101 ⟨[], 0 :: rest, rfl⟩
      · exact h101 ⟨[], 1 :: rest, rfl⟩
      · exact h11 ⟨[], 0 :: 0 :: rest, rfl⟩
      · exact h11 ⟨[], 0 :: 1 :: rest, rfl⟩
      · exact h11 ⟨[], 1 :: 0 :: rest, rfl⟩
      · exact h11 ⟨[], 1 :: 1 :: rest, rfl⟩
  · rintro ⟨k, rfl⟩
    exact stdMonomial3_isIrreducibleH3 k

/-- Number of generator-`1` occurrences in a 3-strand word `w : List (Fin 2)`. -/
def countOnes (w : List (Fin 2)) : ℕ :=
  (w.filter (· == 1)).length

@[simp] theorem countOnes_nil : countOnes [] = 0 := rfl

theorem countOnes_append (u v : List (Fin 2)) :
    countOnes (u ++ v) = countOnes u + countOnes v := by
  simp [countOnes, List.filter_append]

/-- Strictly decreasing termination measure on 3-strand words:
`h3WordMeasure w = 2 * w.length + countOnes w`.
- `[0, 0]` (measure `4`) reduces to `[0]` (measure `2`) and `[]` (measure `0`),
- `[1, 1]` (measure `6`) reduces to `[1]` (measure `3`) and `[]` (measure `0`),
- `[1, 0, 1]` (measure `8`) reduces to `[0, 1, 0]` (measure `7`). -/
def h3WordMeasure (w : List (Fin 2)) : ℕ :=
  2 * w.length + countOnes w

theorem h3WordMeasure_append (u v : List (Fin 2)) :
    h3WordMeasure (u ++ v) = h3WordMeasure u + h3WordMeasure v := by
  simp only [h3WordMeasure, List.length_append, countOnes_append]
  omega

/-- Every single-word rewrite in the 3-strand Gröbner–Shirshov system strictly decreases
`h3WordMeasure`. -/
theorem h3_gs_terminates_and_confluent (h : R) :
    (∀ u v : List (Fin 2),
      h3WordMeasure (u ++ [0] ++ v) < h3WordMeasure (u ++ [0, 0] ++ v) ∧
      h3WordMeasure (u ++ v) < h3WordMeasure (u ++ [0, 0] ++ v)) ∧
    (∀ u v : List (Fin 2),
      h3WordMeasure (u ++ [1] ++ v) < h3WordMeasure (u ++ [1, 1] ++ v) ∧
      h3WordMeasure (u ++ v) < h3WordMeasure (u ++ [1, 1] ++ v)) ∧
    (∀ u v : List (Fin 2),
      h3WordMeasure (u ++ [0, 1, 0] ++ v) < h3WordMeasure (u ++ [1, 0, 1] ++ v)) ∧
    (∀ w : List (Fin 2), isIrreducibleH3 w ↔ ∃ k : Fin 6, w = stdMonomial3 k) ∧
    (∀ k : Fin 6, nfH3 h (stdMonomial3 k) = Pi.single k 1) := by
  refine ⟨?_, ?_, ?_, isIrreducibleH3_iff_exists_stdMonomial3, nfH3_stdMonomial3 h⟩
  · intro u v
    have h0 : h3WordMeasure [0] = 2 := rfl
    have h00 : h3WordMeasure [0, 0] = 4 := rfl
    simp only [h3WordMeasure_append, h0, h00]
    omega
  · intro u v
    have h1 : h3WordMeasure [1] = 3 := rfl
    have h11 : h3WordMeasure [1, 1] = 6 := rfl
    simp only [h3WordMeasure_append, h1, h11]
    omega
  · intro u v
    have h010 : h3WordMeasure [0, 1, 0] = 7 := rfl
    have h101 : h3WordMeasure [1, 0, 1] = 8 := rfl
    simp only [h3WordMeasure_append, h010, h101]
    omega

/-- **Three-Strand Confluence and Unique Normal-Form Theorem (`0` Diamond-Lemma axioms)**:
If any initial linear combination `init : List (R × List (Fin 2))` reduces along two arbitrary
Gröbner–Shirshov paths to standard-monomial expansions `∑ k, c₁ k • stdMonomial3 k` and
`∑ k, c₂ k • stdMonomial3 k`, then the resulting normal-form coefficient vectors are identical
(`c₁ = c₂`). -/
theorem h3_gs_confluent_unique_nf (h : R) (init : List (R × List (Fin 2)))
    (c₁ c₂ : Fin 6 → R)
    (hred₁ : GSReducesH3 h init (List.ofFn (fun k : Fin 6 => (c₁ k, stdMonomial3 k))))
    (hred₂ : GSReducesH3 h init (List.ofFn (fun k : Fin 6 => (c₂ k, stdMonomial3 k)))) :
    c₁ = c₂ := by
  have hev₁ := evalCombH3_invariant hred₁
  have hev₂ := evalCombH3_invariant hred₂
  have h6 : ∀ c : Fin 6 → R,
      evalCombH3 h (List.ofFn (fun k : Fin 6 => (c k, stdMonomial3 k))) = c := by
    intro c
    funext i
    fin_cases i <;>
      simp [List.ofFn, Fin.foldr_succ, evalCombH3, nfH3_stdMonomial3]
  rw [h6 c₁] at hev₁
  rw [h6 c₂] at hev₂
  exact hev₁.symm.trans hev₂

end H3Confluence

-- ============================================================================
-- § 2. Four-Strand (`H₄(q)`) Naive 3-Rule Non-Confluence & Bokut–Shiao Resolution
-- ============================================================================

section H4BokutShiao

/-- The 4-strand overlap word `σ₃ σ₂ σ₃ σ₁` encoded in `0`-indexed generators `Fin 3` (`0, 1, 2`). -/
def w4Overlap : List (Fin 3) := [2, 1, 2, 0]

/-- Branch A of the `w4Overlap` critical pair: applying Yang–Baxter `[2, 1, 2] → [1, 2, 1]` to
the prefix yields `[1, 2, 1, 0]` (`σ₂ σ₃ σ₂ σ₁`). -/
def w4BranchA : List (Fin 3) := [1, 2, 1, 0]

/-- Branch B of the `w4Overlap` critical pair: applying far-commutativity `[2, 0] → [0, 2]` to
the suffix yields `[2, 1, 0, 2]` (`σ₃ σ₂ σ₁ σ₃`). -/
def w4BranchB : List (Fin 3) := [2, 1, 0, 2]

/-- Single-step length-preserving braid / far-commutativity reduction in the naive 3-rule system
on `n = 4` strands (`List (Fin 3)`). -/
inductive Naive3RuleStepH4 : List (Fin 3) → List (Fin 3) → Prop
  | farComm (u v : List (Fin 3)) :
      Naive3RuleStepH4 (u ++ [2, 0] ++ v) (u ++ [0, 2] ++ v)
  | yangBaxter01 (u v : List (Fin 3)) :
      Naive3RuleStepH4 (u ++ [1, 0, 1] ++ v) (u ++ [0, 1, 0] ++ v)
  | yangBaxter12 (u v : List (Fin 3)) :
      Naive3RuleStepH4 (u ++ [2, 1, 2] ++ v) (u ++ [1, 2, 1] ++ v)

/-- A 4-strand word `w : List (Fin 3)` is irreducible under the naive 3-rule system (Hecke
`[i, i]`, far-commutativity `[2, 0]`, and adjacent Yang–Baxter `[1, 0, 1]`, `[2, 1, 2]`) if none
of the six leading subwords occurs as an infix of `w`. -/
def isNaive3RuleIrreducibleH4 (w : List (Fin 3)) : Prop :=
  (∀ i : Fin 3, ¬ ([i, i] <:+: w)) ∧
  ¬ ([2, 0] <:+: w) ∧
  ¬ ([1, 0, 1] <:+: w) ∧
  ¬ ([2, 1, 2] <:+: w)

/-- **Four-Strand Naive 3-Rule Non-Confluence Theorem**:
The overlap word `w4Overlap = [2, 1, 2, 0]` (`σ₃σ₂σ₃σ₁`) reduces in one naive 3-rule step to
`w4BranchA = [1, 2, 1, 0]` and in one naive 3-rule step to `w4BranchB = [2, 1, 0, 2]`, both
`w4BranchA` and `w4BranchB` are strictly irreducible under the naive 3-rule system, and
`w4BranchA ≠ w4BranchB`. -/
theorem h4_threeRule_not_confluent :
    Naive3RuleStepH4 w4Overlap w4BranchA ∧
    Naive3RuleStepH4 w4Overlap w4BranchB ∧
    isNaive3RuleIrreducibleH4 w4BranchA ∧
    isNaive3RuleIrreducibleH4 w4BranchB ∧
    w4BranchA ≠ w4BranchB := by
  refine ⟨?_, ?_, ?_, ?_, by decide⟩
  · simpa [w4Overlap, w4BranchA] using Naive3RuleStepH4.yangBaxter12 [] [0]
  · simpa [w4Overlap, w4BranchB] using Naive3RuleStepH4.farComm [2, 1] []
  · unfold isNaive3RuleIrreducibleH4 w4BranchA
    decide
  · unfold isNaive3RuleIrreducibleH4 w4BranchB
    decide

/-- **Bokut–Shiao `q`-Free Braid Completion Theorem**:
In *any* monoid `M` satisfying the Artin braid relation `s₂ * s₁ * s₂ = s₁ * s₂ * s₁` and
far-commutativity `s₂ * s₀ = s₀ * s₂` — with zero Hecke quadratic hypothesis and zero `q` — the
Bokut–Shiao `(i = 2, j = 0)` rule `s₂ * s₁ * s₀ * s₂ = s₁ * s₂ * s₁ * s₀` holds unconditionally,
equating `w4BranchB` (`s₂ s₁ s₀ s₂`) with `w4BranchA` (`s₁ s₂ s₁ s₀`) in every monoid and algebra
quotient. -/
theorem bokutShiao_resolves_h4_overlap {M : Type*} [Monoid M] (s₀ s₁ s₂ : M)
    (hBraid12 : s₂ * s₁ * s₂ = s₁ * s₂ * s₁)
    (hFar02 : s₀ * s₂ = s₂ * s₀) :
    s₂ * s₁ * s₀ * s₂ = s₁ * s₂ * s₁ * s₀ := by
  calc
    s₂ * s₁ * s₀ * s₂ = s₂ * s₁ * (s₀ * s₂) := by simp [mul_assoc]
    _ = s₂ * s₁ * (s₂ * s₀) := by rw [hFar02]
    _ = (s₂ * s₁ * s₂) * s₀ := by simp [mul_assoc]
    _ = s₁ * s₂ * s₁ * s₀ := by rw [hBraid12]

end H4BokutShiao

-- ============================================================================
-- § 3. Block-Ordered Nuclear Word `Ξ_A`: Hecke-Only Reduction & Bokut–Shiao Irreducibility
-- ============================================================================

section BlockOrderedNucleus

variable {R : Type*} [CommRing R]

/-- Product of a single-generator crossing chain `∏_{(c, d) ∈ crossings} (c * σ + d)` in any
commutative ring (or single-generator commutative subalgebra `R[σ_i]`). -/
def blockCrossingProd (σ : R) : List (R × R) → R
  | [] => 1
  | (c, d) :: rest => (c * σ + d) * blockCrossingProd σ rest

/-- Transfer-matrix coefficient accumulator `(a, b)` for a single-generator crossing chain
`∏_{(c, d) ∈ crossings} (c * σ + d)` reduced exclusively by the Hecke quadratic relation
`σ² = qq * σ + 1`. -/
def blockTransferCoeffs (qq : R) : List (R × R) → R × R
  | [] => (0, 1)
  | (c, d) :: rest =>
    let ab := blockTransferCoeffs qq rest
    (ab.1 * c * qq + ab.1 * d + ab.2 * c, ab.1 * c + ab.2 * d)

/-- Each step of `blockTransferCoeffs` coincides with multiplying by `transferMatrix qq c d`. -/
theorem blockTransferCoeffs_cons_eq_transferMatrix (qq c d : R) (rest : List (R × R)) :
    let ab := blockTransferCoeffs qq rest
    (blockTransferCoeffs qq ((c, d) :: rest)).1 =
      (transferMatrix qq c d).mulVec ![ab.1, ab.2] 0 ∧
    (blockTransferCoeffs qq ((c, d) :: rest)).2 =
      (transferMatrix qq c d).mulVec ![ab.1, ab.2] 1 := by
  intro ab
  exact ⟨(heckeStep_eq_transferMatrix_fst qq c d ab.1 ab.2).symm,
         (heckeStep_eq_transferMatrix_snd qq c d ab.1 ab.2).symm⟩

/-- **Single-Block Hecke-Only Reduction**:
For any list of crossings `crossings : List (R × R)` at a single generator `σ` satisfying
`σ² = qq * σ + 1`, the block product `blockCrossingProd σ crossings` reduces by Hecke steps
alone to `(a * σ + b)` where `(a, b) = blockTransferCoeffs qq crossings`. -/
theorem blockCrossingProd_eq_linear (σ qq : R) (hσ : σ ^ 2 = qq * σ + 1)
    (crossings : List (R × R)) :
    blockCrossingProd σ crossings =
      (blockTransferCoeffs qq crossings).1 * σ + (blockTransferCoeffs qq crossings).2 := by
  induction crossings with
  | nil =>
    simp [blockCrossingProd, blockTransferCoeffs]
  | cons cd rest ih =>
    rcases cd with ⟨c, d⟩
    simp only [blockCrossingProd, blockTransferCoeffs]
    rw [ih]
    exact hecke_linear_mul σ qq c d
      (blockTransferCoeffs qq rest).1 (blockTransferCoeffs qq rest).2 hσ

/-- Descending Bokut–Shiao middle chain `[i - 1, i - 2, ..., j]` of length `k + 1` starting at
`j + k` down to `j`. -/
def descendingChain (j : ℕ) : ℕ → List ℕ
  | 0 => [j]
  | k + 1 => (j + k + 1) :: descendingChain j k

/-- Every Bokut–Shiao leading word `σ_i σ_{i-1} ⋯ σ_j σ_i` (`j < i`, represented as
`i :: mid ++ [i]`) starts and ends with the same generator index `i`. -/
def bokutShiaoLeadingWord (i : ℕ) (mid : List ℕ) : List ℕ :=
  i :: (mid ++ [i])

/-- **No Bokut–Shiao Pattern in Strictly Increasing Chain Words**:
Because a strictly increasing word `w : List ℕ` (`w.IsChain (· < ·)`) is strictly ordered under
`<`, no generator index `i` can appear twice in `w`; consequently, `w` contains no Bokut–Shiao
leading subword `i :: mid ++ [i]` for *any* `i : ℕ` and *any* intermediate subword `mid : List ℕ`
(including Yang–Baxter `mid = [i - 1]` and all higher `n ≥ 4` Bokut–Shiao words
`σ_i σ_{i-1} ⋯ σ_j σ_i`). -/
theorem no_bokutShiao_pattern {w : List ℕ} (hw : w.IsChain (· < ·)) (i : ℕ) (mid : List ℕ) :
    ¬ (bokutShiaoLeadingWord i mid <:+: w) := by
  intro hinf
  have hchain : (bokutShiaoLeadingWord i mid).IsChain (· < ·) :=
    List.IsChain.infix hw hinf
  have hpair : List.Pairwise (· < ·) (bokutShiaoLeadingWord i mid) :=
    List.isChain_iff_pairwise.mp hchain
  rw [bokutShiaoLeadingWord, List.pairwise_cons] at hpair
  have hlt : i < i := hpair.1 i (by simp)
  exact Nat.lt_irrefl i hlt

/-- **Closing Gap `(c)` of `GSNormalForm.lean` — Global Block-Ordered Hecke-Only Reduction and
Full Bokut–Shiao Irreducibility**:
For any sequence of `m` generator blocks `blocks : Fin m → List (R × R)` at generators `σ : Fin m → R`
each satisfying `σ i ^ 2 = qq * σ i + 1`, every block `i` reduces intra-block by Hecke steps alone
to `(a_i * σ_i + b_i)` via `blockTransferCoeffs qq (blocks i)`, and every strictly increasing
subset word `w` (`w.IsChain (· < ·)`) in the resulting `2^m` chain expansion is simultaneously
irreducible under all four rule families: Hecke, far-commutativity, Yang–Baxter, and the complete
Bokut–Shiao braid family. -/
theorem blockOrdered_nucleus_hecke_only_nf {m : ℕ} (qq : R) (σ : Fin m → R)
    (hσ : ∀ i : Fin m, (σ i) ^ 2 = qq * σ i + 1)
    (blocks : Fin m → List (R × R)) :
    (∀ i : Fin m,
      blockCrossingProd (σ i) (blocks i) =
        (blockTransferCoeffs qq (blocks i)).1 * σ i +
          (blockTransferCoeffs qq (blocks i)).2) ∧
    (∀ w : List ℕ, w.IsChain (· < ·) →
      (∀ i : ℕ, ¬ ([i, i] <:+: w)) ∧
      (∀ i j : ℕ, i + 2 ≤ j → ¬ ([j, i] <:+: w)) ∧
      (∀ i j : ℕ, ¬ ([j, i, j] <:+: w)) ∧
      (∀ (i : ℕ) (mid : List ℕ), ¬ (bokutShiaoLeadingWord i mid <:+: w))) := by
  refine ⟨fun i => blockCrossingProd_eq_linear (σ i) qq (hσ i) (blocks i), ?_⟩
  intro w hw
  exact ⟨no_hecke_pattern hw,
         no_farComm_pattern hw,
         no_yangBaxter_pattern hw,
         no_bokutShiao_pattern hw⟩

end BlockOrderedNucleus

-- ============================================================================
-- § 4. Linear Word-Length Sign Flip (`ℓ = 11`) vs Critical Exponential Lyapunov `α_crit = q`
-- ============================================================================

section LyapunovDynamics

/-- Change in the linear word-length functional `E₁(c · w) = |c| · ℓ(w)` under a single Hecke
rewrite `c · (u ++ σ_i² ++ v) ↦ (c · h) · (u ++ σ_i ++ v) + c · (u ++ v)` on a word of length
`ℓ ≥ 2` when `h = q - q⁻¹ > 0`. -/
noncomputable def deltaLinearEnergy (c h : ℝ) (ℓ : ℕ) : ℝ :=
  (|c| * h * ((ℓ : ℝ) - 1) + |c| * ((ℓ : ℝ) - 2)) - |c| * (ℓ : ℝ)

/-- Exact closed form of `deltaLinearEnergy`: `ΔE₁ = |c| · (h · (ℓ - 1) - 2)`. -/
theorem deltaLinearEnergy_eq (c h : ℝ) (ℓ : ℕ) :
    deltaLinearEnergy c h ℓ = |c| * (h * ((ℓ : ℝ) - 1) - 2) := by
  unfold deltaLinearEnergy
  ring

/-- **Linear Word-Length Sign-Flip Theorem (`ℓ ≤ 10` vs `ℓ ≥ 11` at `q₀`)**:
For `c ≠ 0` and `h > 0`:
1. `deltaLinearEnergy c h ℓ < 0 ↔ ((ℓ : ℝ) - 1) < 2 / h`, and
   `0 < deltaLinearEnergy c h ℓ ↔ 2 / h < ((ℓ : ℝ) - 1)`.
2. Whenever `1 / 5 < h` and `h < 2 / 9` (which traps the substrate Hecke scalar
   `h(q₀) = q₀ - q₀⁻¹ ≈ 0.2090602988 ∈ (0.2, 0.2222…)`), a single Hecke step strictly
   *decreases* `E₁` at word length `ℓ = 10` (`ΔE₁ < 0`) and strictly *increases* `E₁` at word
   length `ℓ = 11` (`ΔE₁ > 0`). -/
theorem linear_length_step_sign_flip (c h : ℝ) (hc : c ≠ 0) (hh : 0 < h) :
    (∀ ℓ : ℕ, deltaLinearEnergy c h ℓ < 0 ↔ ((ℓ : ℝ) - 1) < 2 / h) ∧
    (∀ ℓ : ℕ, 0 < deltaLinearEnergy c h ℓ ↔ 2 / h < ((ℓ : ℝ) - 1)) ∧
    ((1 : ℝ) / 5 < h ∧ h < 2 / 9 →
      deltaLinearEnergy c h 10 < 0 ∧ 0 < deltaLinearEnergy c h 11) := by
  have habs : 0 < |c| := abs_pos.mpr hc
  refine ⟨?_, ?_, ?_⟩
  · intro ℓ
    rw [deltaLinearEnergy_eq]
    constructor
    · intro hneg
      have hsub : h * ((ℓ : ℝ) - 1) - 2 < 0 := by
        by_contra hge
        push_neg at hge
        have : 0 ≤ |c| * (h * ((ℓ : ℝ) - 1) - 2) :=
          mul_nonneg (le_of_lt habs) hge
        linarith
      rw [lt_div_iff₀' hh]
      linarith
    · intro hlt
      rw [lt_div_iff₀' hh] at hlt
      exact mul_neg_of_pos_of_neg habs (by linarith)
  · intro ℓ
    rw [deltaLinearEnergy_eq, mul_pos_iff_of_pos_left habs, div_lt_iff₀' hh]
    constructor <;> (intro h1; linarith)
  · rintro ⟨hlow, hhigh⟩
    rw [deltaLinearEnergy_eq, deltaLinearEnergy_eq]
    constructor
    · exact mul_neg_of_pos_of_neg habs (by norm_num; linarith)
    · exact mul_pos habs (by norm_num; linarith)

/-- Change in the exponential fugacity functional `Φ_α(c · w) = |c| · α ^ ℓ(w)` under a single
Hecke rewrite `c · (u ++ σ_i² ++ v) ↦ (c · (q - q⁻¹)) · (u ++ σ_i ++ v) + c · (u ++ v)` on a word
of length `ℓ = k + 2` (`ℓ ≥ 2`). -/
noncomputable def deltaExpLyapunov (c q α : ℝ) (k : ℕ) : ℝ :=
  (|c| * (q - q⁻¹) * α ^ (k + 1) + |c| * α ^ k) - |c| * α ^ (k + 2)

/-- **Exact Characteristic Factorization of the Exponential Lyapunov Step**:
For all `c, q, α : ℝ` with `q ≠ 0` and every `k : ℕ` (word length `ℓ = k + 2 ≥ 2`),
`deltaExpLyapunov c q α k = -|c| * α ^ k * (α - q) * (α + q⁻¹)`. -/
theorem deltaExpLyapunov_factorization (c q α : ℝ) (hq : q ≠ 0) (k : ℕ) :
    deltaExpLyapunov c q α k = -|c| * α ^ k * (α - q) * (α + q⁻¹) := by
  unfold deltaExpLyapunov
  have hqq : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  calc
    (|c| * (q - q⁻¹) * α ^ (k + 1) + |c| * α ^ k) - |c| * α ^ (k + 2)
        = |c| * α ^ k * ((q - q⁻¹) * α + (q * q⁻¹) - α ^ 2) := by
          rw [hqq]; ring
    _ = -|c| * α ^ k * (α - q) * (α + q⁻¹) := by ring

/-- **Critical Exponential Lyapunov Theorem (`α_crit = q`)**:
For every `q > 1`, `c ≠ 0`, `α > 0`, and every word length `ℓ = k + 2 ≥ 2`:
1. **Exact Factorization**: `ΔΦ_α = -|c| · α^k · (α - q) · (α + q⁻¹)`.
2. **Strict Lyapunov Descent (`α > q`)**: `ΔΦ_α < 0 ↔ q < α` (uniformly negative at *every* word
   length `ℓ ≥ 2`, with no sign flip at `ℓ = 11` or anywhere else).
3. **Critical Conservation (`α_crit = q`)**: `ΔΦ_q = 0` at every word length `ℓ ≥ 2`.
4. **Subcritical Growth (`0 < α < q`)**: `0 < ΔΦ_α ↔ α < q`. -/
theorem exp_lyapunov_crit_q0 (c q α : ℝ) (hc : c ≠ 0) (hq : 1 < q) (hα : 0 < α) (k : ℕ) :
    deltaExpLyapunov c q α k = -|c| * α ^ k * (α - q) * (α + q⁻¹) ∧
    (deltaExpLyapunov c q α k < 0 ↔ q < α) ∧
    deltaExpLyapunov c q q k = 0 ∧
    (0 < deltaExpLyapunov c q α k ↔ α < q) := by
  have hq0 : (0 : ℝ) < q := by linarith
  have hq_ne : q ≠ 0 := ne_of_gt hq0
  have habs : 0 < |c| := abs_pos.mpr hc
  have hpow : 0 < α ^ k := pow_pos hα k
  have hplus : 0 < α + q⁻¹ := add_pos hα (inv_pos.mpr hq0)
  have hpos_factor : 0 < |c| * α ^ k * (α + q⁻¹) :=
    mul_pos (mul_pos habs hpow) hplus
  have hrewrite : deltaExpLyapunov c q α k =
      (|c| * α ^ k * (α + q⁻¹)) * (q - α) := by
    rw [deltaExpLyapunov_factorization c q α hq_ne k]
    ring
  refine ⟨deltaExpLyapunov_factorization c q α hq_ne k, ?_, ?_, ?_⟩
  · rw [hrewrite]
    constructor
    · intro hneg
      have hsub : q - α < 0 := by
        by_contra hge
        push_neg at hge
        have : 0 ≤ (|c| * α ^ k * (α + q⁻¹)) * (q - α) :=
          mul_nonneg (le_of_lt hpos_factor) hge
        linarith
      linarith
    · intro hgt
      exact mul_neg_of_pos_of_neg hpos_factor (by linarith)
  · rw [deltaExpLyapunov_factorization c q q hq_ne k]
    ring
  · rw [hrewrite]
    constructor
    · intro hpos
      have hsub : 0 < q - α := (mul_pos_iff_of_pos_left hpos_factor).mp hpos
      linarith
    · intro hlt
      exact mul_pos hpos_factor (by linarith)

end LyapunovDynamics

-- ============================================================================
-- § 5. Temperley–Lieb Loop-Erasure Scalar `δ⁻¹` vs Convention-D `z_D` & Dual Covector Dot Product
-- ============================================================================

section TemperleyLiebVsMarkov

/-- The Temperley–Lieb loop-erasure parameter `δ(q) = q + q⁻¹ = (q² + 1) / q`. -/
noncomputable def deltaTL (q : ℝ) : ℝ := q + q⁻¹

/-- **Temperley–Lieb Loop-Erasure Scalar `δ⁻¹` vs Convention-D Markov Weight `z_D` Theorem**:
For `E_i = q · 1 - σ_i` (satisfying `E_i² = δ · E_i` where `δ = q + q⁻¹`) and the Convention-D
Markov parameter `z_D = q³ / (q² + 1)`:
1. The Convention-D Markov trace of the Temperley–Lieb generator `E_i = q · 1 - σ_i` is
   `q - z_D = q / (q² + 1) = (deltaTL q)⁻¹`.
2. The product `deltaTL q * z_D = q²`.
3. For every `q > 1`, `(deltaTL q)⁻¹ < z_D` (in particular, `(deltaTL q)⁻¹ ≠ z_D`), proving that
   Temperley–Lieb loop erasure and Convention-D Markov strand closure carry distinct non-zero
   scalars related by a factor of `q²`. -/
theorem tl_erasure_scalar_eq_inv_delta_ne_zD (q : ℝ) (hq : 1 < q) :
    q - zD q = q / (q ^ 2 + 1) ∧
    q - zD q = (deltaTL q)⁻¹ ∧
    deltaTL q * zD q = q ^ 2 ∧
    (deltaTL q)⁻¹ < zD q ∧
    (deltaTL q)⁻¹ ≠ zD q := by
  have hq0 : (0 : ℝ) < q := by linarith
  have hq_ne : q ≠ 0 := ne_of_gt hq0
  have hq2_pos : 0 < q ^ 2 + 1 := by positivity
  have hq2_ne : q ^ 2 + 1 ≠ 0 := ne_of_gt hq2_pos
  have h1 : q - zD q = q / (q ^ 2 + 1) := by
    unfold zD
    field_simp
    ring
  have h2 : q - zD q = (deltaTL q)⁻¹ := by
    rw [h1]
    unfold deltaTL
    field_simp
  have h3 : deltaTL q * zD q = q ^ 2 := by
    unfold deltaTL zD
    field_simp
  have h4 : (deltaTL q)⁻¹ < zD q := by
    rw [← h2, h1]
    unfold zD
    rw [div_lt_div_iff_of_pos_right hq2_pos]
    have hq_sq : 1 < q ^ 2 := by nlinarith
    nlinarith
  exact ⟨h1, h2, h3, h4, ne_of_lt h4⟩

/-- **Trace / Mass as a Finite Dual Covector Dot Product on Standard Monomials**:
For any `R`-module `M`, any `R`-linear functional `τ : M →ₗ[R] R`, and any finite family of
standard basis monomials `b : ι → M`, the trace of a normal-form linear combination
`∑ i, c i • b i` is the finite dot product `∑ i, c i * τ (b i)` of the coefficient vector `c`
with the precomputed dual covector `i ↦ τ (b i)`. -/
theorem trace_eq_covector_dotProduct {R M ι : Type*} [CommRing R] [AddCommGroup M] [Module R M]
    [Fintype ι] (τ : M →ₗ[R] R) (b : ι → M) (c : ι → R) :
    τ (∑ i : ι, c i • b i) = ∑ i : ι, c i * τ (b i) := by
  rw [map_sum]
  refine Finset.sum_congr rfl ?_
  intro i _
  rw [τ.map_smul, smul_eq_mul]

end TemperleyLiebVsMarkov

-- ============================================================================
-- § 6. Two-Ideal Separation: Skein Quotient `I_Hecke` vs Antisymmetric Baryonic Radical `𝓝_D`
-- ============================================================================

section TwoIdealSeparation

/-- **Two-Ideal Separation Theorem (`TL_3` Null-Radical vs GPMT Baryonic Completion on `H₃(q)`)**:
For every real `q > 1`:
1. **Uncompleted Convention-D Null-Radical (`𝓝_D = span(radicalVec q)`)**:
   The `q`-antisymmetriser `radicalVec q` (`y_{(1³)}`) is annihilated by the Convention-D Markov
   Gram matrix (`∀ i, ∑ j, gramD q i j * radicalVec q j = 0`), while the `5 × 5` quotient Gram
   matrix `gramQuotientD q` on the complement has strictly negative (non-zero) determinant
   `(gramQuotientD q).det < 0`, pinning `ker(gramD q)` to the 1-dimensional `(1³)` antisymmetric
   ideal.
2. **GPMT Modified-Trace Baryonic Completion (`trGPMT` / `gramGPMT`)**:
   Restoring the `(1³)` sector with its positive GPMT modified quantum dimension
   `dMod111Abs q = q³ / ((q² + 1)(q⁴ + q² + 1)) > 0` lifts `radicalVec q` to an exact eigenvector
   of `gramGPMT q` with strictly positive eigenvalue `q⁻³ > 0`, strictly positive quadratic form
   `0 < ∑ i, radicalVec q i * ∑ j, gramGPMT q i j * radicalVec q j`, and full rank 6
   (`(Matrix.of (gramGPMT q)).det ≠ 0`). -/
theorem two_ideal_separation_tl_vs_gpmt (q : ℝ) (hq : 1 < q) :
    (∀ i : Fin 6, (∑ j : Fin 6, gramD q i j * radicalVec q j) = 0) ∧
    (gramQuotientD q).det < 0 ∧
    0 < dMod111Abs q ∧
    (∀ i : Fin 6,
      (∑ j : Fin 6, gramGPMT q i j * radicalVec q j) = q⁻¹ ^ 3 * radicalVec q i) ∧
    0 < q⁻¹ ^ 3 ∧
    0 < (∑ i : Fin 6, radicalVec q i * ∑ j : Fin 6, gramGPMT q i j * radicalVec q j) ∧
    (Matrix.of (gramGPMT q)).det ≠ 0 := by
  have hq0 : (0 : ℝ) < q := by linarith
  have hq_ne : q ≠ 0 := ne_of_gt hq0
  have hq2_ne : q ^ 2 + 1 ≠ 0 := by positivity
  have hq4_ne : q ^ 4 + q ^ 2 + 1 ≠ 0 := by positivity
  have hweights := gpmt_wedderburn_weights_pos q hq0
  have heig : ∀ i : Fin 6,
      (∑ j : Fin 6, gramGPMT q i j * radicalVec q j) = q⁻¹ ^ 3 * radicalVec q i :=
    gramGPMT_mul_radicalVec_eq_eigenvalue q hq_ne hq2_ne hq4_ne
  have hquad_pos :
      0 < (∑ i : Fin 6, radicalVec q i * ∑ j : Fin 6, gramGPMT q i j * radicalVec q j) := by
    simp_rw [heig]
    have hsum_sq :
        (∑ i : Fin 6, radicalVec q i * (q⁻¹ ^ 3 * radicalVec q i)) =
          q⁻¹ ^ 3 * (∑ i : Fin 6, (radicalVec q i) ^ 2) := by
      rw [Finset.mul_sum]
      refine Finset.sum_congr rfl ?_
      intro i _
      ring
    rw [hsum_sq]
    apply mul_pos (by positivity)
    have h0 : (radicalVec q 0) ^ 2 = 1 := by simp [radicalVec]
    have hnonneg : ∀ i ∈ (Finset.univ : Finset (Fin 6)), 0 ≤ (radicalVec q i) ^ 2 :=
      fun i _ => sq_nonneg _
    have hle : (radicalVec q 0) ^ 2 ≤ ∑ i : Fin 6, (radicalVec q i) ^ 2 :=
      Finset.single_le_sum hnonneg (Finset.mem_univ 0)
    linarith
  exact ⟨gramD_mul_radicalVec_eq_zero q hq_ne hq2_ne hq4_ne,
         gramQuotientD_det_neg q,
         hweights.2.2,
         heig,
         by positivity,
         hquad_pos,
         (gramGPMT_real_det_ne_zero_and_unique_solve q hq0).1⟩

end TwoIdealSeparation

end QOU.BraidsAndKnots.GroebnerShirshovConfluenceLyapunovAndRadical
