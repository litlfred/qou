import QOU.Hecke.TwMul
import QOU.MathlibExt.InvMonomialDet

/-!
# QOU.Hecke.TauSymmetrizing — the canonical trace `τ`, and its Gram determinant

Third brick of bean `qou-kwoa` (Option C: derive the Schur-element criterion
instead of citing it).  `QOU.MathlibExt.WeightedTraceGram` did the half of
Geck–Pfeiffer 7.2.6 that is pure linear algebra; this file starts the half that
is genuinely about `H_n(q)`.

`Ref: [geckpfeiffer2000]` Thm 7.2.6 and §8.1.  The citation stays: Geck and
Pfeiffer proved this, and formalising a piece of it does not change that.  What
changes is its *role* — for what is proved below it is attribution, and for the
identity left open (`tau_Tw_mul_Tw`, stated as a hypothesis rather than an
axiom) it remains load-bearing.

## `τ` is definable in one line, and that was the surprise

The docstring of `WeightedTraceGram` recorded that Mathlib has no
symmetric-algebra theory — true — and inferred that constructing `τ` would need
that theory built first.  **That inference was wrong.**  `τ` is the
`T_1`-coordinate in the `T_w` basis, and `QOU.Hecke.TwBasis.basisTwOfField`
already supplies the basis, so `τ` is `Module.Basis.coord`.  Its defining
property `τ(T_w) = δ_{w,1}` is then immediate.

What is *not* immediate — and is the whole content — is the structure-constant
identity

  `τ(T_v · T_w) = δ_{w, v⁻¹} · q^{ℓ(v)}`,

which says the Gram matrix of `(x, y) ↦ τ(x y)` is supported on the graph of
inversion.  This file states it as an explicit hypothesis and derives the
determinant from it; it does not assume it anywhere.

## What is proved

* `tau`, `tau_Tw`, `tau_one` — the functional and its defining property.
* `tau_Tw_mul_Tw_of_length_add` — the identity's **length-additive locus**,
  proved outright from `Tw_mul_Tw`: there `τ(T_v T_w) = δ_{wv, 1}`.
* `tauGram`, `tauGram_apply` — the Gram matrix.
* `tauGram_det_of_structure_constants` — **given** the identity,
  `det = sign(inv) · ∏_v q^{ℓ(v)}`.
* `tauGram_det_ne_zero_of_structure_constants` — hence nonzero for every
  `q ≠ 0`.

## What the last one does NOT say

`det(τ-Gram) ≠ 0` for all `q ≠ 0` is **not** semisimplicity of `H_n(q)`, which
is false at roots of unity.  It is the statement that `H_n(q)` is a *symmetric
Frobenius* algebra, which it is for every `q ≠ 0`.  The criterion needs both
this and the split decomposition: on a split semisimple `A ≅ ∏_λ M_{d_λ}(K)`,
`WeightedTraceGram.weightedGram_det_ne_zero_iff` says a weighted trace's Gram is
nondegenerate iff every weight is nonzero, and `τ`'s weights are `1/s_λ`.  So
the two together give **`s_λ = 0` for some `λ` ⟹ `H_n(q)` is not split
semisimple**.  The converse — the direction `SchurElementCriterion` is usually
wanted for — is a separate argument (Tits deformation) and is not here.

## The remaining induction, since it is now legible

`QOU.Hecke.TwBasis.σ_mul_Tw` is the **full** structure-constant table, up and
down cases together, so the induction is available in principle.  It does not
close on `ℓ(v)` alone: `τ(σ_i · z) = q · [T_{s_i}-coefficient of z]`, which is a
different coordinate.  Geck–Pfeiffer 8.1.1 instead inducts on `ℓ(v) + ℓ(w)`,
using a common descent `s` to write `T_v T_w = (q-1) T_{v s} T_w + q T_{v s}
T_{s w}` — both terms of smaller total length, so the recursion closes on `τ`
alone.  What that needs and this corpus does not yet have: the descent
decomposition in this file's handedness (`T_v T_w = T_{wv}`, not `T_{vw}`), and
the exchange fact supplying a common descent.  Tracked in bean `qou-kwoa`.
-/

namespace QOU.Hecke.TwBasis

open QOU.Hecke.SymmetricCoxeter

variable (K : Type*) [Field K] (q : K) (n : ℕ)

/-- **The canonical trace `τ`**: the `T_1`-coordinate in the `T_w` basis.

    This is the functional Geck–Pfeiffer characterise by `τ(T_w) = δ_{w,1}`; the
    characterisation is `tau_Tw` below.  That it is a *trace* — `τ(xy) = τ(yx)`
    — is the open half, and is nowhere assumed here. -/
noncomputable def tau : QOU.Hecke.IwahoriHecke K q n →ₗ[K] K :=
  (basisTwOfField K q n).coord 1

/-- **`τ(T_w) = δ_{w,1}`** — the defining property. -/
@[simp] theorem tau_Tw (w : Equiv.Perm (Fin (n + 1))) :
    tau K q n (Tw K q n w) = if w = 1 then 1 else 0 := by
  rw [tau, Module.Basis.coord_apply, ← coe_basisTwOfField K q n,
    Module.Basis.repr_self, Finsupp.single_apply]

/-- `τ(1) = 1`. -/
@[simp] theorem tau_one : tau K q n 1 = 1 := by
  rw [← Tw_one K q n, tau_Tw]; simp

/-- **The identity holds on the length-additive locus**, without assumption:
    where the lengths add, `T_v · T_w = T_{wv}` and `τ` reads off `δ_{wv,1}`.

    This is consistent with the conjectured `δ_{w,v⁻¹} q^{ℓ(v)}` rather than a
    proof of it: on this locus `w = v⁻¹` forces `ℓ(v) + ℓ(w) = ℓ(1) = 0`, so the
    `q`-power is `q^0 = 1`.  The locus therefore never sees the `q`-powers, which
    is exactly why the general identity needs the descent induction instead. -/
theorem tau_Tw_mul_Tw_of_length_add (v w : Equiv.Perm (Fin (n + 1)))
    (h : (permCoxeterSystem n).length (w * v)
        = (permCoxeterSystem n).length w + (permCoxeterSystem n).length v) :
    tau K q n (Tw K q n v * Tw K q n w) = if w * v = 1 then 1 else 0 := by
  rw [Tw_mul_Tw K q n v w h, tau_Tw]

/-- **The Gram matrix of `(x, y) ↦ τ(x y)` in the `T_w` basis.** -/
noncomputable def tauGram :
    Matrix (Equiv.Perm (Fin (n + 1))) (Equiv.Perm (Fin (n + 1))) K :=
  Matrix.of fun v w => tau K q n (Tw K q n v * Tw K q n w)

@[simp] theorem tauGram_apply (v w : Equiv.Perm (Fin (n + 1))) :
    tauGram K q n v w = tau K q n (Tw K q n v * Tw K q n w) := rfl

/-- **Given the structure-constant identity, the Gram determinant is a sign
    times a product of `q`-powers.**

    The hypothesis is Geck–Pfeiffer's `τ(T_v T_w) = δ_{w,v⁻¹} q^{ℓ(v)}`; it is a
    hypothesis, not an axiom, and the conclusion is a genuine implication.  Once
    the hypothesis is discharged the conclusion becomes unconditional with no
    change to this proof. -/
theorem tauGram_det_of_structure_constants
    (hsc : ∀ v w : Equiv.Perm (Fin (n + 1)),
      tau K q n (Tw K q n v * Tw K q n w)
        = if w = v⁻¹ then q ^ (permCoxeterSystem n).length v else 0) :
    (tauGram K q n).det
      = (Equiv.Perm.sign (Equiv.inv (Equiv.Perm (Fin (n + 1)))) : K)
          * ∏ v : Equiv.Perm (Fin (n + 1)), q ^ (permCoxeterSystem n).length v := by
  have hM : tauGram K q n
      = Matrix.of fun v w =>
          if w = v⁻¹ then q ^ (permCoxeterSystem n).length v else 0 := by
    ext v w; rw [tauGram_apply, hsc]; rfl
  rw [hM, QOU.MathlibExt.det_of_inv_monomial]

/-- **Hence `H_n(q)` is Frobenius for every `q ≠ 0`** — the `τ`-Gram is
    nondegenerate.  Note this is *not* semisimplicity, which fails at roots of
    unity; see the module docstring. -/
theorem tauGram_det_ne_zero_of_structure_constants (hq : q ≠ 0)
    (hsc : ∀ v w : Equiv.Perm (Fin (n + 1)),
      tau K q n (Tw K q n v * Tw K q n w)
        = if w = v⁻¹ then q ^ (permCoxeterSystem n).length v else 0) :
    (tauGram K q n).det ≠ 0 := by
  have hM : tauGram K q n
      = Matrix.of fun v w =>
          if w = v⁻¹ then q ^ (permCoxeterSystem n).length v else 0 := by
    ext v w; rw [tauGram_apply, hsc]; rfl
  rw [hM]
  exact QOU.MathlibExt.det_of_inv_monomial_ne_zero fun v => pow_ne_zero _ hq

end QOU.Hecke.TwBasis
