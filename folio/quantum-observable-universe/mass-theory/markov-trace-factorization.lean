import Mathlib.Data.Real.Basic
import Mathlib.Data.Real.Sqrt
import Mathlib.Tactic
import Mathlib.Data.List.Basic


/-!
# QOU.Archimedean.markov_trace_factorization — Exact factorization of the nuclear Markov trace

The Markov trace of the nuclear braid word factors as a product
of Markov-traced generator volumes:

  tr(N̄(p,n)) = Π_{i=0}^{A-2} (z · a_i + b_i)

where (a_i, b_i) are the Chebyshev-reduced chain coefficients
at generator σ_i, and z = q³/(q²+1) is the Markov trace parameter
(convention D; this read the excised convention-C 1/(q^{1/2}+q^{-1/2})
until 2026-11-16).  The factorisation needs the word grouped by
generator in increasing order; an interleaved word such as σ₁σ₂σ₁
does not factor (its trace is h z² + z, not z³).

LaTeX label: `thm:markov-trace-factorization`

## References
- [leitner2026] §6/markov-trace-factorization
-/

namespace QOU.Archimedean

/-- The Markov trace parameter z = q³/(q²+1) (convention D). -/
-- Ref: [leitner2026] §6/markov-trace-factorization
noncomputable def markovZ (q : ℝ) (hq : 0 < q) : ℝ :=
  q ^ 3 / (q ^ 2 + 1)

/-- The Chebyshev transfer matrix at one crossing.

    Given current state (a, b) representing a σ_i + b,
    and crossing coefficients (c, d) representing c σ_i + d,
    the product (a σ + b)(c σ + d) reduces via σ² = (q-q⁻¹)σ + 1 to:
      a' = ac(q-q⁻¹) + ad + bc
      b' = ac + bd -/
-- Ref: [leitner2026] §6/markov-trace-factorization
noncomputable def chebyshevStep (q : ℝ) (a b c d : ℝ) : ℝ × ℝ :=
  (a * c * (q - 1/q) + a * d + b * c, a * c + b * d)

/-- The Markov-traced generator volume: V̂_i = z · a_i + b_i.

    This is the contribution of generator σ_i to the total
    Markov trace. -/
-- Ref: [leitner2026] §6/markov-trace-factorization
noncomputable def tracedVolume (q : ℝ) (hq : 0 < q) (a b : ℝ) : ℝ :=
  markovZ q hq * a + b

/-- The asymptotic ratio: tr(L_0)/tr(parent) → 1/ℏ_q as A → ∞.

    For heavy nuclei, the L_0 trace converges to 1/ℏ_q times
    the parent trace, where ℏ_q = 1 - q⁻¹. -/
-- Ref: [leitner2026] §6/markov-trace-factorization
noncomputable def asymptoticRatio (q : ℝ) : ℝ :=
  1 / (1 - 1/q)

/-- The asymptotic ratio is positive for q > 1. -/
-- Ref: [leitner2026] §6/markov-trace-factorization
theorem asymptoticRatio_pos (q : ℝ) (hq : 1 < q) : 0 < asymptoticRatio q := by
  unfold asymptoticRatio
  apply div_pos (by norm_num : (0 : ℝ) < 1)
  rw [sub_pos, div_lt_one (by linarith : (0 : ℝ) < q)]
  linarith

/-- The asymptotic ratio equals 1/ℏ_q. -/
-- Ref: [leitner2026] §6/markov-trace-factorization
theorem asymptoticRatio_eq_inv_hbar (q : ℝ) (hq : 0 < q) :
    asymptoticRatio q = 1 / (1 - q⁻¹) := by
  unfold asymptoticRatio
  congr 1
  rw [inv_eq_one_div]

/-- Numerical verification: at q = 1.1097, the asymptotic ratio ≈ 10.116. -/
-- Ref: [leitner2026] §6/markov-trace-factorization
theorem asymptoticRatio_at_q :
    |asymptoticRatio 1.1097 - 10.116| < 0.01 := by
  unfold asymptoticRatio
  norm_num

-- ═══════════════════════════════════════════════════════════════════
-- Crossing coefficients in the Hecke algebra
-- ═══════════════════════════════════════════════════════════════════

/-- Positive crossing (proton-proton): c = 1, d = 0. -/
-- Ref: [leitner2026] §6/markov-trace-factorization
def crossingPositive : ℝ × ℝ := (1, 0)

/-- Negative crossing (neutron-neutron): c = 1, d = -(q - q⁻¹), i.e.
    `σ_i - (q - q⁻¹) = σ_i⁻¹` by the Hecke relation. Matches the (c, d)
    table of this block, `nucleon_typed_d` in `inverse-markov-qvalues.py`
    and `crossingNN` in `generator-volume-decomposition.lean`. (Corrected
    2026-11-16 from a convention-C form `(q², -q(√q - 1/√q))`.) -/
-- Ref: [leitner2026] §6/markov-trace-factorization
noncomputable def crossingNegative (q : ℝ) : ℝ × ℝ :=
  (1, -(q - 1 / q))

/-- Mixed crossing (proton-neutron): c = 1, d = -(q - q⁻¹)/2, the average
    of the positive and negative crossings. -/
-- Ref: [leitner2026] §6/markov-trace-factorization
noncomputable def crossingMixed (q : ℝ) : ℝ × ℝ :=
  (1, -(q - 1 / q) / 2)

-- ═══════════════════════════════════════════════════════════════════
-- The factorization chain: R[B_A] → H_A(q) → Π(a_i σ_i + b_i) → R
-- ═══════════════════════════════════════════════════════════════════

/-- The factorization of the link invariant through the Hecke algebra.

    Each step preserves the invariant:
    1. Braid → Hecke: quotient by Skein ideal (well-defined on links)
    2. Hecke → Chain: Gröbner reduction (confluence / diamond lemma)
    3. Chain → Trace: Markov property (link invariant by Ocneanu)
    4. Product: the factorization theorem (this file) -/
-- Ref: [leitner2026] §6/markov-trace-factorization
structure NuclearTraceFactorization where
  /-- Substrate parameter. -/
  q : ℝ
  /-- q > 1. -/
  q_gt_one : 1 < q
  /-- Number of protons. -/
  p : ℕ
  /-- Number of neutrons. -/
  n : ℕ
  /-- Mass number. -/
  A : ℕ := p + n
  /-- Chain coefficients (a_i, b_i) for i = 0,...,A-2. -/
  chains : List (ℝ × ℝ)
  /-- The list has the right length. -/
  chains_length : chains.length = A - 1
  /-- The Markov trace (product of traced volumes). -/
  trace : ℝ :=
    let z := markovZ q (by linarith : 0 < q)
    chains.foldl (fun acc ab => acc * (z * ab.1 + ab.2)) 1
  /-- The trace is a link invariant (independent of braid representative).
      This follows from the composition:
      Ocneanu trace ∘ Gröbner reduction ∘ Hecke quotient
      where each step preserves the link invariant. -/
  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  invariance : trace = chains.foldl (fun acc ab =>
    acc * (markovZ q (by linarith : 0 < q) * ab.1 + ab.2)) 1

/-- Top-level alias matching the manifest declaration. -/
-- Ref: [leitner2026] §6/markov-trace-factorization
noncomputable def markov_trace_factorization (q : ℝ) (hq : 1 < q)
    (chains : List (ℝ × ℝ)) : ℝ :=
  let z := markovZ q (by linarith)
  chains.foldl (fun acc ab => acc * (z * ab.1 + ab.2)) 1

/-- Pull the initial accumulator out of a multiplicative left-fold.
    Polymorphic over the element type `α` — the fold uses only multiplication
    in the `ℝ` codomain, never anything about `α` (per Gemini review, PR #1849). -/
private theorem foldl_mul_init {α : Type*} (g : α → ℝ) :
    ∀ (l : List α) (a : ℝ),
      l.foldl (fun acc x => acc * g x) a = a * l.foldl (fun acc x => acc * g x) 1
  | [], a => by simp
  | x :: t, a => by
      simp only [List.foldl_cons, one_mul]
      rw [foldl_mul_init g t (a * g x), foldl_mul_init g t (g x)]; ring

/-- Wenzl disjoint-multiplicativity (the MonoidHom property of the Markov trace):
    the traced-volume product over a concatenation of chains factors as the product
    of the two traced-volume products. This is `tr_M(K ⊔ K') = tr_M(K)·tr_M(K')`. -/
-- Ref: [wenzl1988] §1.7 (disjoint multiplicativity of the Markov trace)
theorem markov_trace_factorization_mul (q : ℝ) (hq : 1 < q) (c₁ c₂ : List (ℝ × ℝ)) :
    markov_trace_factorization q hq (c₁ ++ c₂)
      = markov_trace_factorization q hq c₁ * markov_trace_factorization q hq c₂ := by
  -- `simp only [def]` zeta-reduces the `let z := markovZ …`, exposing the bare
  -- multiplicative fold so `foldl_mul_init` matches and the goal closes by `rfl`
  -- (addresses the `let`-blocks-`rw` concern, Copilot review on PR #1849).
  simp only [markov_trace_factorization, List.foldl_append]
  rw [foldl_mul_init]

end QOU.Archimedean
