import HeckeTemperleyLieb.TLRectangularHom
import HeckeTemperleyLieb.TLBraidedModular

/-!
# Braiding and modular data on the semisimplified Temperley–Lieb quotient

Bean `hkmt`. `TLBraidedModular` computes the `S`- and `T`-matrices from braiding on the
Jones–Wenzl projectors, using the trace on `TL` itself. `TLNegligibleQuotient` and
`TLRectangularHom` build the quotient `Q N` by negligible morphisms and its category. This file
moves the braiding and the modular data onto that quotient.

* `tauQ`: the trace descends to `Q N`. It is cyclic, and **nondegenerate** there
  (`tauQ_nondegenerate`): the quotient is exactly what makes the trace form nondegenerate.
* `crossingQ`, `crossingInvQ`: the positive-loop crossings `σᵢ = A·1 − A⁻¹ eᵢ` descend. They
  are invertible and satisfy the braid relations in `Q N`.
* `jw_mul_fullTwistQ`: the full twist acts on the image of `p_n` by `A^{n(n+1)}`.
* `cH_eq_tauQ`: every Hopf-link entry of the braid `S`-matrix is a quotient trace.
* `modular_data_quotient`: at a primitive `2(k+2)`-th root `ω²`, `δ = ω² + ω⁻²`:
  1. every simple idempotent of every `Q N` is equivalent to the vacuum or some `p_m`, `m < k`,
     with cups, and none of these is zero in the quotient;
  2. the `S`-matrix on those `k + 1` simples, computed from braiding and quotient traces, is
     `S_{ij} = [(i+1)(j+1)]`;
  3. it is invertible. Together with 1, this is the modularity condition for the quotient:
     the `S`-matrix on the **complete** list of simples is nondegenerate.

Not proved here: a monoidal structure on the quotient category (the tensor product of objects on
different strand counts) and a braiding as a natural isomorphism in Mathlib's
`BraidedCategory`. The braiding here is the action of the crossings on each `Q N`.

No empirical input; everything is over an arbitrary field.

-- Ref: [jones1983] Index for subfactors, §4.
-- Ref: [kirbymelvin1991] https://doi.org/10.1007/BF01239527
-- Ref: [leitner2026] the Temperley–Lieb chapter (bean `hkmt`).
-/

namespace QOU.HeckeTemperleyLieb.TLQuotientModular

open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov
open QOU.HeckeTemperleyLieb.TLPositiveLoop QOU.HeckeTemperleyLieb.TLHopfRow
open QOU.HeckeTemperleyLieb.TLRootOfUnity QOU.HeckeTemperleyLieb.TLVacuumRow
open QOU.HeckeTemperleyLieb.TLCable QOU.HeckeTemperleyLieb.TLSemisimpleQuotient
open QOU.HeckeTemperleyLieb.TLCupCap QOU.HeckeTemperleyLieb.TLNegligible
open QOU.HeckeTemperleyLieb.TLBraidedModular

/-! ## The trace on the quotient -/

section Trace

variable {K : Type*} [Field K] {δ ε : K} (T : MarkovTower δ ε)

theorem negl_tau {n : ℕ} {x : TLFin K δ n} (h : Negl T n x) : T.τ n x = 0 := by
  simpa using h 1

/-- **The trace on the quotient by negligibles.** -/
noncomputable def tauQ (n : ℕ) : Q T n → K :=
  Quotient.lift (fun x => T.τ n x) (fun x y h => by
    have h' : Negl T n (x - y) := h
    rw [← sub_eq_zero, ← map_sub]; exact negl_tau T h')

theorem tauQ_coe (n : ℕ) (x : TLFin K δ n) : tauQ T n (x : Q T n) = T.τ n x := rfl

theorem tauQ_comm (n : ℕ) (φ ψ : Q T n) : tauQ T n (φ * ψ) = tauQ T n (ψ * φ) := by
  obtain ⟨x, rfl⟩ := coe_surj T φ
  obtain ⟨y, rfl⟩ := coe_surj T ψ
  rw [← RingCon.coe_mul, ← RingCon.coe_mul, tauQ_coe, tauQ_coe, T.tr_comm]

/-- **The trace form on the quotient is nondegenerate**, on every number of strands. -/
theorem tauQ_nondegenerate (n : ℕ) (φ : Q T n) (h : ∀ ψ, tauQ T n (φ * ψ) = 0) : φ = 0 := by
  obtain ⟨x, rfl⟩ := coe_surj T φ
  rw [coe_eq_zero_iff]
  intro y
  have := h (y : Q T n)
  rwa [← RingCon.coe_mul, tauQ_coe] at this

end Trace

/-! ## The braiding on the quotient -/

section Braiding

variable {K : Type*} [Field K] {δ ε A : K} (T : MarkovTower δ ε) (hA : A ≠ 0)
  (hδ : δ = A ^ 2 + A⁻¹ ^ 2)

variable (A) in
/-- The crossing `σᵢ` in the quotient. -/
noncomputable def crossingQ {n : ℕ} (i : Fin n) : Q T n := (crossing δ A i : Q T n)

variable (A) in
/-- The inverse crossing in the quotient. -/
noncomputable def crossingInvQ {n : ℕ} (i : Fin n) : Q T n := (crossingInv δ A i : Q T n)

include hA hδ in
theorem crossingQ_mul_inv {n : ℕ} (i : Fin n) : crossingQ A T i * crossingInvQ A T i = 1 := by
  rw [crossingQ, crossingInvQ, ← RingCon.coe_mul, crossing_mul_crossingInv hA hδ,
    RingCon.coe_one]

include hA hδ in
theorem crossingInvQ_mul {n : ℕ} (i : Fin n) : crossingInvQ A T i * crossingQ A T i = 1 := by
  rw [crossingQ, crossingInvQ, ← RingCon.coe_mul, crossingInv_mul_crossing hA hδ,
    RingCon.coe_one]

include hA hδ in
/-- **The braid relation in the quotient.** -/
theorem crossingQ_braid {n : ℕ} {i j : Fin n} (h : i.val + 1 = j.val ∨ j.val + 1 = i.val) :
    crossingQ A T i * crossingQ A T j * crossingQ A T i =
      crossingQ A T j * crossingQ A T i * crossingQ A T j := by
  simp only [crossingQ, ← RingCon.coe_mul, crossing_braid hA hδ h]

theorem crossingQ_commute {n : ℕ} {i j : Fin n} (h : ¬ (i.val + 1 = j.val ∨ j.val + 1 = i.val)) :
    crossingQ A T i * crossingQ A T j = crossingQ A T j * crossingQ A T i := by
  simp only [crossingQ, ← RingCon.coe_mul, crossing_commute h]

/-- **The twist in the quotient.** The full twist acts on the image of `p_n` by `A^{n(n+1)}`. -/
theorem jw_mul_fullTwistQ {n : ℕ} (hS : JWSpec δ n) :
    (jw δ n : Q T n) * (fullTwist δ A n : Q T n) = A ^ (n * (n + 1)) • (jw δ n : Q T n) := by
  rw [← RingCon.coe_mul, jw_mul_fullTwist hS, coe_smul']

/-- **Every Hopf-link entry is a quotient trace.** -/
theorem cH_eq_tauQ (n m : ℕ) :
    cH A T n m = tauQ T (n + m + 1) ((wB δ n m * cable δ A n (m + 1) : TLFin K δ (n + m + 1)) :
      Q T (n + m + 1)) := rfl

end Braiding

/-! ## The modular data of the quotient -/

section Modular

variable {K : Type*} [Field K]

/-- **Modular data of the semisimplified Temperley–Lieb category at a root of unity.**
With `ζ = ω²` a primitive `2(k+2)`-th root and `δ = ζ + ζ⁻¹`: the simples of every quotient
`Q N` are the vacuum and `p_0, …, p_{k−1}` with cups, none of them zero; the braid `S`-matrix on
these `k + 1` simples is `[(i+1)(j+1)]`; and it is invertible. -/
theorem modular_data_quotient (ω : Kˣ) (k : ℕ) (hζ : IsPrimitiveRoot (ω ^ 2) (2 * (k + 2)))
    {ε : K} (T : MarkovTower (((ω ^ 2 : Kˣ) : K) + (((ω ^ 2)⁻¹ : Kˣ) : K)) ε)
    (hε : (((ω ^ 2 : Kˣ) : K) + (((ω ^ 2)⁻¹ : Kˣ) : K)) * ε = 1) :
    (∀ N (φ : Q T N), IsSimpleIdem K φ →
      ∃ s, StdLt (((ω ^ 2 : Kˣ) : K) + (((ω ^ 2)⁻¹ : Kˣ) : K)) k N s ∧
        MvN φ (s : Q T N) ∧ (s : Q T N) ≠ 0) ∧
    braidS (ω : K) T k = sMatrix (ω ^ 2) k ∧
    (braidS (ω : K) T k).det ≠ 0 :=
  ⟨fun N φ hφ => simple_mvn_stdLt_root k hζ T hε N φ hφ,
    braidS_eq_sMatrix ω k hζ T hε, braidS_det_ne_zero ω k hζ T hε⟩

end Modular

end QOU.HeckeTemperleyLieb.TLQuotientModular
