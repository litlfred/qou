import QOU.Hecke.TauStructureConstants
import QOU.MathlibExt.TraceWeightsOfAlgEquiv
import Mathlib.LinearAlgebra.Matrix.Nondegenerate

/-!
# QOU.Hecke.TauSchurElement — the abstract Schur elements of `H_n(q)`, and they never vanish

Option 2 of the `qou-kwoa` fork, completed.  The **abstract** Schur element is
`s_λ = 1 / c_λ`, where `c_λ` is the weight of `τ` on the `λ`-block of a splitting
`H_n(q) ≅ ∏_λ M_{d_λ}(K)`.  That is their definition, not a formula; the
identification with Wenzl's hook-length product `schurElement Q X` is option 3
and is **not** here.

## The chain

1. `τ(T_v T_w) = δ_{w,v⁻¹} q^{ℓ(v)}` (`TauStructureConstants`) ⟹ the Gram
   determinant is `sign(inv) · ∏_v q^{ℓ(v)}`, **nonzero for every `q ≠ 0`**.
2. Hence `τ` is nondegenerate: `∀ y, τ(z y) = 0` forces `z = 0`
   (`tau_eq_zero_of_forall_mul` — a determinant argument in the `T_w` basis).
3. A vanishing block weight would put a whole block in the radical
   (`QOU.MathlibExt.exists_ne_zero_forall_mul_eq_zero_of_traceWeight_eq_zero`).
4. So **every** block weight is nonzero, and `s_λ = 1/c_λ` exists and is nonzero
   — at every rank and every `q ≠ 0`, for *any* splitting.

## What this is, and what it is not

It **is** the conclusion side of the Geck–Pfeiffer criterion, derived: the Schur
elements of `H_n(q)` do not vanish where the algebra splits.  Read
contrapositively it is the statement the arc has been aiming at — *a candidate
weight system with a zero is realised by no splitting*.

It is **not** the criterion itself.  `SchurElementCriterion` asserts the
converse implication (`all s_λ ≠ 0 ⟹ semisimple`), which is Tits deformation
and is not here; and it is stated with Wenzl's two-parameter `schurElement Q X`,
a different object from `s_λ` until the identification of option 3 is made.
`SchurElementCriterion` therefore still has **no instance**, and the
`heckeWedderburn` shortcut is still refused (see `WeightedTraceGram`).

Splittings are taken as a **hypothesis** `E` rather than produced here, so
nothing below depends on which `q` admit one; that is deliberate — the
statement is *"for any splitting, the weights are nonzero"*.

`Ref: [geckpfeiffer2000]` §7.2, §8.1 — attribution.
-/

namespace QOU.Hecke.TwBasis

open QOU.MathlibExt Matrix

variable (K : Type*) [Field K] (q : K) (n : ℕ)

/-! ### `τ` is nondegenerate -/

/-- **`τ` is nondegenerate**: an element killed by `τ(z · —)` is zero.

    The `T_w` coordinates of such a `z` are a left null vector of `tauGram`, and
    that determinant is nonzero by `tauGram_det_ne_zero`. -/
theorem tau_eq_zero_of_forall_mul (hq : q ≠ 0)
    {z : QOU.Hecke.IwahoriHecke K q n}
    (h : ∀ y : QOU.Hecke.IwahoriHecke K q n, tau K q n (z * y) = 0) : z = 0 := by
  classical
  have hvec : Matrix.vecMul (fun v => (basisTwOfField K q n).repr z v)
      (tauGram K q n) = 0 := by
    funext w
    have hz : ∑ v, (basisTwOfField K q n).repr z v • Tw K q n v = z := by
      have := Module.Basis.sum_repr (basisTwOfField K q n) z
      simpa [coe_basisTwOfField] using this
    have hexp : tau K q n (z * Tw K q n w)
        = ∑ v, (basisTwOfField K q n).repr z v * tauGram K q n v w := by
      conv_lhs => rw [← hz]
      rw [Finset.sum_mul, map_sum]
      exact Finset.sum_congr rfl fun v _ => by
        rw [smul_mul_assoc, map_smul, smul_eq_mul, tauGram_apply]
    have := h (Tw K q n w)
    rw [hexp] at this
    simpa [Matrix.vecMul, dotProduct] using this
  have hr := Matrix.eq_zero_of_vecMul_eq_zero (tauGram_det_ne_zero K q n hq) hvec
  have : (basisTwOfField K q n).repr z = 0 := by
    ext v
    exact congrFun hr v
  simpa using congrArg (basisTwOfField K q n).repr.symm this

/-! ### The abstract Schur elements -/

variable {K q n}
variable {ι : Type*} [Fintype ι] [DecidableEq ι]
variable {J : ι → Type*} [∀ i, Fintype (J i)] [∀ i, DecidableEq (J i)]

/-- **Every block weight of `τ` is nonzero**, for any splitting and any
    `q ≠ 0`.

    Contrapositive of the radical lemma: a zero weight would exhibit a nonzero
    element annihilated by `τ(· × —)`, and `τ` is nondegenerate. -/
theorem traceWeight_tau_ne_zero (hq : q ≠ 0)
    (E : QOU.Hecke.IwahoriHecke K q n ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (a : ∀ i, J i) (i : ι) :
    traceWeight E (tau K q n) a i ≠ 0 := by
  intro hc
  obtain ⟨z, hz, hzy⟩ :=
    exists_ne_zero_forall_mul_eq_zero_of_traceWeight_eq_zero E (tau K q n)
      (tau_mul_comm K q n) a hc
  exact hz (tau_eq_zero_of_forall_mul K q n hq hzy)

/-- **The abstract Schur element** of the block `i`, relative to a splitting:
    the reciprocal of `τ`'s weight there.

    This is the *definition* of the Schur element.  Identifying it with Wenzl's
    hook-length product `QOU.MathlibExt.schurElement Q X` is a separate theorem
    (option 3) and is not available here. -/
noncomputable def abstractSchurElement
    (E : QOU.Hecke.IwahoriHecke K q n ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (a : ∀ i, J i) (i : ι) : K :=
  (traceWeight E (tau K q n) a i)⁻¹

/-- **The abstract Schur elements never vanish**, at every rank and every
    `q ≠ 0`. -/
theorem abstractSchurElement_ne_zero (hq : q ≠ 0)
    (E : QOU.Hecke.IwahoriHecke K q n ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (a : ∀ i, J i) (i : ι) :
    abstractSchurElement E a i ≠ 0 :=
  inv_ne_zero (traceWeight_tau_ne_zero hq E a i)

omit [Fintype ι] in
/-- The weight is the reciprocal of the Schur element — the defining relation,
    in the direction one usually quotes. -/
theorem traceWeight_eq_inv_abstractSchurElement
    (E : QOU.Hecke.IwahoriHecke K q n ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (a : ∀ i, J i) (i : ι) :
    traceWeight E (tau K q n) a i = (abstractSchurElement E a i)⁻¹ := by
  rw [abstractSchurElement, inv_inv]

/-- **`τ` is the Schur-weighted character sum** — the identity the Schur
    elements are named for, `τ = Σ_λ (1 / s_λ) χ_λ`.

    No `q ≠ 0` hypothesis: `(c⁻¹)⁻¹ = c` holds in a field unconditionally, so
    this identity does not depend on the weights being nonzero — only the
    *interpretation* of `s_λ` as a Schur element does. -/
theorem tau_eq_weightedTrace_inv_abstractSchurElement
    (E : QOU.Hecke.IwahoriHecke K q n ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (a : ∀ i, J i) (x : QOU.Hecke.IwahoriHecke K q n) :
    tau K q n x
      = weightedTrace (fun i => (abstractSchurElement E a i)⁻¹) (E x) := by
  rw [eq_weightedTrace_of_algEquiv E (tau K q n) (tau_mul_comm K q n) a]
  simp only [weightedTrace]
  exact Finset.sum_congr rfl fun i _ => by
    rw [traceWeight_eq_inv_abstractSchurElement E a i]

omit [Fintype ι] in
/-- **The independence statement**: the Schur element does not depend on which
    diagonal matrix unit reads the weight. -/
theorem abstractSchurElement_indep
    (E : QOU.Hecke.IwahoriHecke K q n ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (a b : ∀ i, J i) (i : ι) :
    abstractSchurElement E a i = abstractSchurElement E b i := by
  rw [abstractSchurElement, abstractSchurElement,
    traceWeight_indep E (tau K q n) (tau_mul_comm K q n) a b i]

end QOU.Hecke.TwBasis
