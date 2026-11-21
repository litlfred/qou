import QOU.Hecke.Algebra
import Mathlib.Algebra.Module.LinearMap.Defs
import QOU.IwahoriHecke.JonesNormalForm

/-!
# Markov trace on `H_n(q)`

A *Markov trace* on the family `{H_n(q)}_{n ≥ 1}` is an `R`-linear
functional `tr_M : H_n(q) → R` satisfying:

  (M1) Normalisation:  `tr_M(1) = 1`
  (M2) Cyclicity:      `tr_M(x · y) = tr_M(y · x)` for all x, y
  (M3) Markov axiom:   `tr_M^{H_n}(x · σ_{n-1}) = z · tr_M^{H_{n-1}}(x)`
                        for `x ∈ H_{n-1}(q) ⊂ H_n(q)`

with Markov parameter `z = 1 / (q^{1/2} + q^{-1/2})`.

Existence + uniqueness up to scalar normalisation: Jones (1987),
Ocneanu (1986).

## References

- [thm:jones-markov-trace]
- [prop:markov-pair-z2]
-/

namespace QOU.Hecke

universe u

/--
Markov trace structure on `H_n(q)`. Encodes the three Markov axioms
plus the connection to the Markov parameter `z`.

For the chain `H_1 ⊂ H_2 ⊂ ...` the Markov axiom relates traces at
adjacent levels; we capture this via a parameterised family of
traces and a coherence condition.
-/
class MarkovTrace
    {R : Type u} (n : ℕ) (q : R) (A : Type u)
    [CommRing R] [Inv R] [Ring A] [Algebra R A] [HA : HeckeAlgebra R n q A] where
  /-- The trace as an R-linear map A → R. -/
  trace : A →ₗ[R] R
  /-- (M1) Normalisation: tr_M(1) = 1. -/
  normalised : trace 1 = 1
  /-- (M2) Cyclicity: trace(x · y) = trace(y · x). -/
  cyclic : ∀ x y : A, trace (x * y) = trace (y * x)
  /-- The Markov parameter z = 1/(q^{1/2} + q^{-1/2}). Stored as a
  field rather than a definition because q^{1/2} requires choosing
  a square root extension of R. -/
  z_param : R
  /-- (M3 / generator value) tr_M(σ_i) = z for every generator.
  This is the key consequence of the full Markov axiom
  `tr_M^{H_n}(x · σ_{n-1}) = z · tr_M^{H_{n-1}}(x)` applied at
  level n with x = 1 ∈ H_{n-1}. -/
  trace_gen : ∀ i : Generator n, trace (HA.embed i) = z_param
  /-- (M3 / pair product) tr_M(σ_i · σ_j) = z² when i < j.
  Follows from two consecutive Markov peels: σ_j is top-indexed,
  one peel gives z · tr_{n-1}(σ_i); σ_i lives in H_{n-1} so the
  second peel gives z · z. -/
  trace_prod_gen : ∀ (i j : Generator n), i.idx.val < j.idx.val →
      trace (HA.embed i * HA.embed j) = z_param * z_param

namespace MarkovTrace

variable {R : Type u} {n : ℕ} {q : R} {A : Type u}
  [CommRing R] [Inv R] [Ring A] [Algebra R A]
  [HA : HeckeAlgebra R n q A]
  [MT : MarkovTrace n q A]

/-- The Markov trace value of a Hecke generator: tr_M(σ_i) = z. -/
theorem trace_generator (i : Generator n) :
    MT.trace (HA.embed i) = MT.z_param := by
  -- Ref: [thm:jones-markov-trace]; tr_M(σ_i) = z by Markov axiom.
  exact MT.trace_gen i

/-- Pair-of-generators trace formula:
    tr_M(σ_i · σ_j) = z²  for i < j
[leitner2026] `prop:markov-pair-z2` — direct two-step Markov peel. -/
theorem trace_pair (i j : Generator n) (h : i.idx.val < j.idx.val) :
    MT.trace (HA.embed i * HA.embed j) = MT.z_param * MT.z_param := by
  -- Ref: [prop:markov-pair-z2]; follows from trace_prod_gen field.
  exact MT.trace_prod_gen i j h

/-- **Idempotent-sandwich collapse.** For an idempotent `e` (`e * e = e`),
    `tr_M(e · x · e) = tr_M(e · x)`.  Derived purely from the cyclicity axiom
    (M2) and idempotency: `tr(e·x·e) = tr(e·(e·x)) = tr((e·e)·x) = tr(e·x)`.

    This is the structural simplification behind the **Pauli-full-shell** case of
    the knot operator `F(τ, N)` in `cor:spectral-decomposition-qvalue`, whose
    numerator is `|tr_M(e_{(1³)} · τ · T_β · e_{(1³)})|` with `e_{(1³)}` the
    alternating Young idempotent: the outer `e` sandwich collapses, so the
    numerator equals `|tr_M(e_{(1³)} · τ · T_β)|`.  Bean `qou-xq3f`. -/
theorem trace_idempotent_sandwich (e x : A) (he : e * e = e) :
    MT.trace (e * x * e) = MT.trace (e * x) := by
  rw [MT.cyclic (e * x) e, ← mul_assoc, he]

/-- The mirror form: `tr_M(e · x · e) = tr_M(x · e)` for an idempotent `e`.
    Same derivation via cyclicity applied to the leading factor. -/
theorem trace_idempotent_sandwich' (e x : A) (he : e * e = e) :
    MT.trace (e * x * e) = MT.trace (x * e) := by
  rw [MT.cyclic (e * x) e, ← mul_assoc, he, MT.cyclic e x]

/-- **Trace of a generator times an inverse generator**:
    `tr_M(σ_i · σ_j⁻¹) = z² − (q − q⁻¹)·z` for `i < j`.

    The Hecke quadratic relation gives `σ_j⁻¹ = σ_j − (q − q⁻¹)·1`
    (`HeckeAlgebra.inv_formula`), so writing `σ_j⁻¹` in that form and using
    `R`-linearity of the trace:

      `tr_M(σ_i · (σ_j − (q−q⁻¹)·1))
        = tr_M(σ_i·σ_j) − (q−q⁻¹)·tr_M(σ_i)
        = z² − (q−q⁻¹)·z`

    by `trace_prod_gen` (`i < j`) and `trace_gen`.  This is the **denominator**
    `tr_M(T_β)` of the Pauli-full-shell knot operator `F(τ,N)` in
    `cor:spectral-decomposition-qvalue`, whose decay operator is
    `T_β = σ_0 · σ_1⁻¹` (`i = 0`, `j = 1`).  Bean `qou-xq3f`. -/
theorem trace_gen_mul_invGen (i j : Generator n) (h : i.idx.val < j.idx.val) :
    MT.trace (HA.embed i * (HA.embed j - (q - q⁻¹) • 1))
      = MT.z_param * MT.z_param - (q - q⁻¹) * MT.z_param := by
  rw [mul_sub, mul_smul_comm, mul_one, map_sub, map_smul,
      MT.trace_prod_gen i j h, MT.trace_gen i, smul_eq_mul]

end MarkovTrace

/-! ## Uniqueness of the Markov trace

**The class `MarkovTrace` alone does NOT determine the trace.** Until 2026-10-10 this
file carried `axiom markov_trace_unique_axiom`, asserting that two `MarkovTrace`
instances with equal `z_param` have equal `trace`. That statement is **false**, and
since it was an `axiom` it made the environment inconsistent. The class only pins
`tr(1)`, `tr(σᵢ)`, `tr(σᵢσⱼ)` (`i < j`) and cyclicity; on `H₄(q)` the cyclic traces
form a 5-dimensional space (one per partition of 4) and those conditions cut out only
four of the five directions. Explicit counterexample, on the tree's own `H₄(q)`:
`QOU.Hecke.MarkovTraceClassNotUnique.markov_trace_unique_axiom_false` (the trace
`4·tr_Z − 3·tr_{Z+1} − tr_{Z−1} + tr_{Z+2}` satisfies every field with `z_param = Z`
but gives `Z³ + 6` on `σ₀σ₁σ₂`, against `Z³` for the Ocneanu trace).

What IS true is uniqueness under the **cross-level Markov property** (M3),
`tr(x · σ_k) = z · tr(x)` for `x` in the subalgebra generated by `σ₀, …, σ_{k-1}`.
`MarkovTrace.IsMarkov` states it, and `markov_trace_unique` below proves uniqueness
from it, sorry-free, via the Jones normal form
(`QOU.IwahoriHecke.JonesNormalForm.markov_unique_of_adjoin_eq_top`).

The concrete traces satisfy (M3), for every Markov parameter `z`:
`QOU.Hecke.MarkovTraceIsMarkov.isMarkov_H2` / `isMarkov_H3A` / `isMarkov_H4A`
(`markovTraceH2`, `markovTraceH3A`, `markovTraceH4A`). So `markov_trace_unique` applies:
`markovTraceH4A_unique` says every (M3) trace on the tree's `H₄(q)` is the Ocneanu trace
at its own `z`, and `mixMarkov_not_isMarkov` shows the counterexample trace above fails
(M3). No `MarkovTrace` on `H_n(q)` is constructed for `n ≥ 5`. -/

section Uniqueness

open QOU.IwahoriHecke.JonesNormalForm

variable {R : Type u} {n : ℕ} {q : R} {A : Type u}
  [CommRing R] [Inv R] [Ring A] [Algebra R A] [HA : HeckeAlgebra R n q A]

/-- The generators as an `ℕ`-indexed family: `genSeq k = σ_k` for `k < n - 1`, and `0`
past the top (never used there). -/
noncomputable def genSeq (HA : HeckeAlgebra R n q A) : ℕ → A := fun k =>
  if h : k < n - 1 then HA.embed ⟨⟨k, h⟩⟩ else 0

theorem genSeq_of_lt (k : ℕ) (h : k < n - 1) : genSeq HA k = HA.embed ⟨⟨k, h⟩⟩ :=
  dif_pos h

theorem genSeq_image_Iio {k : ℕ} (hk : k ≤ n - 1) :
    genSeq HA '' Set.Iio k = HA.embed '' {j : Generator n | j.idx.val < k} := by
  ext x
  constructor
  · rintro ⟨i, hi, rfl⟩
    have hi' : i < n - 1 := lt_of_lt_of_le hi hk
    exact ⟨⟨⟨i, hi'⟩⟩, hi, (genSeq_of_lt i hi').symm⟩
  · rintro ⟨⟨⟨i, hi⟩⟩, hik, rfl⟩
    exact ⟨i, hik, genSeq_of_lt i hi⟩

/-- The class relations make `genSeq` a `HeckeFamily` with quadratic `σ² = (q − q⁻¹)σ + 1`. -/
theorem genSeq_heckeFamily : HeckeFamily (n - 1) (q - q⁻¹) (1 : R) (genSeq HA) where
  quad i hi := by
    rw [genSeq_of_lt i hi, one_smul]
    exact HA.quadratic _
  braid i hi := by
    rw [genSeq_of_lt i (by omega), genSeq_of_lt (i + 1) hi]
    exact HA.braid _ _ (Or.inl rfl)
  comm i j hij hj := by
    rw [genSeq_of_lt i (by omega), genSeq_of_lt j hj]
    refine HA.farCommute _ _ ⟨fun h => ?_, fun h => ?_⟩
    · have := congrArg (fun g : Generator n => g.idx.val) h
      simp at this; omega
    · rcases h with h | h <;> simp at h <;> omega

theorem genSeq_adjoin_eq_top : Algebra.adjoin R (genSeq HA '' Set.Iio (n - 1)) = ⊤ := by
  rw [genSeq_image_Iio le_rfl]
  have : {j : Generator n | j.idx.val < n - 1} = Set.univ :=
    Set.eq_univ_of_forall fun j => j.idx.isLt
  rw [this, Set.image_univ]
  exact HA.spans

/-- **The cross-level Markov property (M3)** for a `MarkovTrace`:
`tr(x · σ_i) = z · tr(x)` whenever `x` lies in the subalgebra generated by the
generators of index `< i`. This is the axiom the `MarkovTrace` class does not carry. -/
def MarkovTrace.IsMarkov (MT : MarkovTrace n q A) : Prop :=
  ∀ i : Generator n, ∀ x ∈ Algebra.adjoin R (HA.embed '' {j : Generator n | j.idx.val < i.idx.val}),
    MT.trace (x * HA.embed i) = MT.z_param * MT.trace x

theorem MarkovTrace.IsMarkov.genSeq {MT : MarkovTrace n q A} (h : MT.IsMarkov) :
    ∀ k, k < n - 1 → ∀ x ∈ Algebra.adjoin R (genSeq HA '' Set.Iio k),
      MT.trace (x * genSeq HA k) = MT.z_param * MT.trace x := by
  intro k hk x hx
  rw [genSeq_image_Iio hk.le] at hx
  rw [genSeq_of_lt k hk]
  exact h ⟨⟨k, hk⟩⟩ x hx

/-- **Uniqueness of the Markov trace (Ocneanu 1985; Jones 1987), sorry-free.**
Two `MarkovTrace`s on the same `HeckeAlgebra` with the same Markov parameter that both
satisfy the cross-level Markov property (M3) have the same trace.

The (M3) hypotheses are necessary, not decorative: without them the conclusion is false
(`QOU.Hecke.MarkovTraceClassNotUnique.markov_trace_unique_axiom_false`). -/
-- Ref: [jones1987] §4–5 (normal form, Markov trace)
theorem markov_trace_unique (MT₁ MT₂ : MarkovTrace n q A)
    (hz : MT₁.z_param = MT₂.z_param) (h₁ : MT₁.IsMarkov) (h₂ : MT₂.IsMarkov) :
    MT₁.trace = MT₂.trace := by
  have hm₂ := h₂.genSeq
  rw [← hz] at hm₂
  exact markov_unique_of_adjoin_eq_top genSeq_heckeFamily genSeq_adjoin_eq_top MT₁.z_param
    MT₁.trace MT₂.trace MT₁.normalised MT₁.cyclic h₁.genSeq MT₂.normalised MT₂.cyclic hm₂

end Uniqueness

end QOU.Hecke
