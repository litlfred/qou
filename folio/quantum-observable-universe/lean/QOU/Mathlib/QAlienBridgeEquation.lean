/-
Copyright (c) 2026 litlfred. All rights reserved.

# The q-native bridge equation: the weight is multiplicative, and in general mixed

[`AlienBridgeEquation.lean`](AlienBridgeEquation.lean) carries Écalle's classical
bridge equation `⁅∂, Δ_ω⁆ = ω · Δ_ω`, whose weight shift is **additive**:
`∂`-eigenvalue `λ ↦ λ + ω`. That relation does not transfer to a q-difference
module, and the reason is structural rather than technical.

**The dichotomy is forced, not chosen.** The "ordinary operator" one conjugates
by is a *derivation* in the classical setting and an *automorphism* in the
q-setting (the dilation `σ_q : x ↦ qx`). Conjugating by a derivation is a
commutator and its eigenvalue shift is additive; conjugating by an automorphism
is `σ ∘ Δ ∘ σ⁻¹` and its eigenvalue shift is **multiplicative**:

| setting | ordinary operator | relation | eigenvalue shift |
|---|---|---|---|
| classical | derivation `∂` | `⁅∂, Δ_ω⁆ = ω·Δ_ω` | `λ ↦ λ + ω`  (additive) |
| q-difference | automorphism `σ` | `σ ∘ Δ_ω ∘ σ⁻¹ = c_ω·Δ_ω` | `λ ↦ c_ω·λ`  (multiplicative) |

`eulerSystem_weight_exp` below makes the link exact rather than analogical: on the
**same** family `Δ_n := tⁿ·E` over the **same** grading, the classical weight is
`n` and the q-weight is `cⁿ`. The two are not rival conventions — the
multiplicative weight is the multiplicative character `c^{(−)}` evaluated on the
additive one. The grading is the invariant; "additive vs multiplicative" only
records which operator you read it through.

**And in general it is neither, but both** — the matrix-representation picture.
The adjoint action of `σ` on the alien derivations need not be diagonalisable.
`QBridgeSystem` therefore carries a Jordan-style pair:

    σ ∘ Δ_ω ∘ σ⁻¹  =  weight ω · Δ_ω  +  unipotent ω

a semisimple part (the multiplicative character) plus a nilpotent correction.
This is exactly the Levi decomposition of the local q-difference Galois group —
a torus of characters `qⁿ` extended by a unipotent part that the q-logarithm
generates. Held: [vanderput2006] §5 (1) gives `Gal(M) = Hom(L, ℂ*) (× 𝔾_a)` for a
regular-singular module, the `𝔾_a` present exactly when the constant matrix is
not semisimple (the q-logarithm `ℓ`), and §5 (5) gives the split exact sequence
`1 → U_ξ → Gal(M) → Gal(gr M) → 1` with `U_ξ` unipotent — a semi-direct product,
the action of `Gal(gr M)` on `U_ξ` explicit. One caveat the docstring's phrase
hides: for an *irreducible* module of non-integral slope `t/n`, `n > 1`,
[vanderput2006] §5 (2) has `1 → 𝔾_m → Gal → (ℤ/n)² → 0` **not** split, so the
torus-by-unipotent picture is the regular-singular and slope-filtered shape,
not the shape inside a single ramified block.

**What the structure abstracts, and from where.** The `Δ_ω` are Ramis–Sauloy's
q-alien derivations [ramis-sauloy2006] Thm 3.5, `Δ̇_c(A) = Res_{d=c} log S_{d,a}(A)`,
valued in the Stokes Lie algebra `st(A)` and graded by level `δ = μ_j − μ_i`
(their eq. 16); Thm 3.6 makes them Lie-like ⊗-endomorphisms of the fibre functor,
which is the functoriality `Derivation R A A` encodes. The singular set `Ω` is
their `Σ_{A_0} ⊂ E_q`, points of the elliptic curve rather than sectors (Prop.
2.5 and eq. 6: the Stokes operator `S_{c,d} = (S_c)⁻¹ S_d` is the ambiguity
between two q-directions of summation). `QBridgeSystem.bridge` is the adjoint
action of the dilation on those `Δ̇_c`. Ramis–Sauloy supply the object; whether
their `Δ̇_c` satisfy `bridge` with any particular weight is bean `qou-vkg5`'s
open item 2, and this file does not claim it. `qweight_shift` computes the eigenvalue statement in that general
case: the semisimple part multiplies the eigenvalue, the unipotent part adds a
correction. `qweight_shift_of_semisimple` is the diagonal special case.

**Not claimed.** That C1 — or any analytic q-difference module — satisfies this
relation with particular weights. This says what a system carrying the q-bridge
looks like and what follows; exhibiting one from a resurgent q-series is
untouched. Bean `qou-vkg5`.

§7c: generic `{R A : Type*} [CommSemiring R] [CommRing A] [Algebra R A]`, no
ordering and no `ℝ`. Sorry-free.

-- Ref: [ecalle1981] Fonctions résurgentes, tome I
-- Ref: [ramis-sauloy-zhang2013] https://arxiv.org/abs/0903.0853
-- Ref: [ramis-sauloy2006] https://arxiv.org/abs/math/0611521 (Prop. 2.5, Thm 3.5–3.6: the q-alien derivations)
-- Ref: [vanderput2006] https://arxiv.org/abs/math/0612592 (§5 (1), (2), (5): the local q-difference Galois group)
-- Ref: [leitner2026] docs/audits/2026-08-08-rsz-c1-infinity-route-closed.md
-/
import Mathlib.RingTheory.Derivation.Basic
import Mathlib.Tactic
import QOU.Mathlib.AlienBridgeEquation

namespace QOU.Mathlib.QAlienBridge

open QOU.Mathlib.AlienBridge

variable {R A Ω : Type*} [CommSemiring R] [CommRing A] [Algebra R A]

/-! ### Conjugating a derivation by an algebra automorphism -/

/-- `σ ∘ D ∘ σ⁻¹` is again a derivation.  Mathlib has `Derivation` and
    `AlgEquiv` but does not provide this conjugation, which is the whole content
    of the q-side bridge relation: in the q-setting the "ordinary operator" is an
    automorphism, so the relation is a conjugation rather than a commutator. -/
noncomputable def conjDeriv (σ : A ≃ₐ[R] A) (D : Derivation R A A) :
    Derivation R A A where
  toLinearMap := σ.toLinearMap ∘ₗ (D.toLinearMap ∘ₗ σ.symm.toLinearMap)
  map_one_eq_zero' := by simp
  leibniz' := fun a b => by
    simp only [LinearMap.coe_comp, Function.comp_apply, AlgEquiv.toLinearMap_apply,
      Derivation.coeFn_coe, map_mul, D.leibniz, smul_eq_mul, map_add,
      AlgEquiv.apply_symm_apply]

@[simp]
theorem conjDeriv_apply (σ : A ≃ₐ[R] A) (D : Derivation R A A) (f : A) :
    conjDeriv σ D f = σ (D (σ.symm f)) := rfl

/-- Conjugation is `R`-linear in the derivation. -/
theorem conjDeriv_smul (σ : A ≃ₐ[R] A) (c : R) (D : Derivation R A A) :
    conjDeriv σ (c • D) = c • conjDeriv σ D := by
  ext f
  simp [Derivation.smul_apply]

/-! ### The q-bridge system -/

/-- A **q-native bridge system**: a dilation automorphism `σ`, a family of alien
    derivations `Δ_ω`, a **multiplicative** weight `c_ω`, a unipotent correction,
    and the relation

    `σ ∘ Δ_ω ∘ σ⁻¹ = c_ω · Δ_ω + N_ω`.

    The relation is a **field**, i.e. a hypothesis — nothing in the data
    determines it, and axiomatising it would not establish it (AGENTS.md
    §"Axiomatization is NOT a Proof").

    The `unipotent` field is what makes this the general "combined" form: the
    adjoint action of `σ` on the `Δ_ω` need not be diagonalisable, and the Levi
    decomposition of a local q-difference Galois group is precisely a torus of
    multiplicative characters extended by a unipotent part ([vanderput2006]
    §5 (1), (5); the `Δ_ω` themselves are [ramis-sauloy2006] Thm 3.5).  Setting
    `unipotent = 0` (`IsSemisimple`) recovers the pure multiplicative case. -/
structure QBridgeSystem (R A Ω : Type*) [CommSemiring R] [CommRing A]
    [Algebra R A] where
  /-- The dilation automorphism `σ` (classically `x ↦ qx`). -/
  dil : A ≃ₐ[R] A
  /-- The alien derivation at the singularity `ω`. -/
  alien : Ω → Derivation R A A
  /-- The **multiplicative** weight — the semisimple part of the adjoint action. -/
  weight : Ω → R
  /-- The nilpotent part of the adjoint action (zero in the diagonalisable case). -/
  unipotent : Ω → Derivation R A A
  /-- The q-bridge equation. -/
  bridge : ∀ (ω : Ω) (f : A),
    conjDeriv dil (alien ω) f = weight ω • alien ω f + unipotent ω f

namespace QBridgeSystem

/-- The adjoint action is diagonalisable — no unipotent part. -/
def IsSemisimple (S : QBridgeSystem R A Ω) : Prop := ∀ ω : Ω, S.unipotent ω = 0

/-- Solved form: `σ(Δ_ω(σ⁻¹ f)) = c_ω · Δ_ω f + N_ω f`. -/
theorem dil_alien_symm (S : QBridgeSystem R A Ω) (ω : Ω) (f : A) :
    S.dil (S.alien ω (S.dil.symm f)) = S.weight ω • S.alien ω f + S.unipotent ω f :=
  S.bridge ω f

/-- **The weight shift is MULTIPLICATIVE, with a unipotent correction.**

    If `f` is a `σ`-eigenvector of eigenvalue `λ` (a unit), then

    `σ(Δ_ω f) = (c_ω · λ) · Δ_ω f  +  λ · N_ω f`.

    This is the combined / matrix-representation form: the semisimple part
    **multiplies** the eigenvalue by `c_ω`, and the unipotent part contributes an
    additive correction — a Jordan block rather than a diagonal entry.  Contrast
    `AlienBridge.BridgeSystem.weight_shift`, where conjugating by a *derivation*
    gives `λ ↦ λ + ω`. -/
theorem qweight_shift (S : QBridgeSystem R A Ω) (ω : Ω) {lam : Rˣ} {f : A}
    (hf : S.dil f = (lam : R) • f) :
    S.dil (S.alien ω f)
      = (S.weight ω * (lam : R)) • S.alien ω f + (lam : R) • S.unipotent ω f := by
  have hsymm : S.dil.symm f = ((lam⁻¹ : Rˣ) : R) • f := by
    apply S.dil.injective
    rw [S.dil.apply_symm_apply, map_smul, hf, smul_smul, Units.inv_mul, one_smul]
  have hb := S.bridge ω f
  rw [conjDeriv_apply, hsymm, Derivation.map_smul, map_smul] at hb
  have h2 := congrArg (fun x : A => (lam : R) • x) hb
  simp only [smul_add, smul_smul] at h2
  rw [Units.mul_inv, one_smul] at h2
  rw [h2, mul_comm (S.weight ω) ((lam : R))]

/-- **The diagonal case: purely multiplicative.**  With no unipotent part the
    `σ`-eigenvalue is simply scaled by the weight: `λ ↦ c_ω · λ`. -/
theorem qweight_shift_of_semisimple (S : QBridgeSystem R A Ω)
    (hss : S.IsSemisimple) (ω : Ω) {lam : Rˣ} {f : A}
    (hf : S.dil f = (lam : R) • f) :
    S.dil (S.alien ω f) = (S.weight ω * (lam : R)) • S.alien ω f := by
  rw [S.qweight_shift ω hf, hss ω]
  simp

/-- **Weights MULTIPLY under composition** (diagonal case) — the q-analogue of
    `AlienBridge.BridgeSystem.weight_add_of_comp`, where they add.  So the `Δ_ω`
    generate an algebra graded by a *multiplicative* character group rather than
    by an additive one. -/
theorem qweight_mul_of_comp (S : QBridgeSystem R A Ω) (hss : S.IsSemisimple)
    (ω ω' : Ω) (f : A) :
    S.dil (S.alien ω (S.alien ω' (S.dil.symm f)))
      = (S.weight ω * S.weight ω') • S.alien ω (S.alien ω' f) := by
  have hb : ∀ (u : Ω) (g : A),
      S.dil (S.alien u (S.dil.symm g)) = S.weight u • S.alien u g := by
    intro u g
    have h := S.bridge u g
    rw [conjDeriv_apply, hss u] at h
    simpa using h
  rw [show S.alien ω' (S.dil.symm f)
      = S.dil.symm (S.dil (S.alien ω' (S.dil.symm f))) from
        (S.dil.symm_apply_apply _).symm,
    hb ω' f, map_smul, Derivation.map_smul, map_smul, hb ω (S.alien ω' f),
    smul_smul, mul_comm (S.weight ω') (S.weight ω)]

/-- **The hypothesis has teeth.**  If `σ` commutes with `Δ_ω` (the conjugation is
    trivial) and the system is semisimple, then every value of `Δ_ω` is fixed by
    scaling by `c_ω`.  So whenever `c_ω` fixes nothing but `0`, commutation forces
    `Δ_ω = 0`.

    Note the degenerate value is `c_ω = 1`, not `c_ω = 0` — the multiplicative
    counterpart of the classical `ω = 0` (`AlienBridge.ord_comm_of_weight_zero`),
    and a check that the weight really does sit in the relation multiplicatively.
    The hypothesis is phrased as "scaling by `c_ω` fixes only `0`" rather than
    "`c_ω − 1` acts injectively" so that it stays over a `CommSemiring`, where
    there is no subtraction. -/
theorem alien_eq_zero_of_dil_comm (S : QBridgeSystem R A Ω) (hss : S.IsSemisimple)
    (ω : Ω) (hcomm : ∀ g : A, conjDeriv S.dil (S.alien ω) g = S.alien ω g)
    (hw : ∀ x : A, S.weight ω • x = x → x = 0) (f : A) :
    S.alien ω f = 0 := by
  refine hw _ ?_
  have hb := S.bridge ω f
  rw [hss ω] at hb
  simp only [Derivation.zero_apply, add_zero] at hb
  rw [← hb, hcomm f]

end QBridgeSystem

/-! ### The q-Euler model, and the exact additive ↔ multiplicative link -/

/-- **The q-Euler bridge system.**  Given a dilation `σ` with `σ t = c · t` and a
    derivation `E` commuting with `σ` (the Euler / degree operator), the family
    `Δ_n := tⁿ·E` satisfies the q-bridge with **multiplicative** weight `cⁿ` and
    no unipotent part.

    The weight comes out multiplicative for a completely explicit reason: `σ` is
    an algebra map, so it passes through the product `tⁿ · E(−)` and multiplies
    by `σ(t)ⁿ = cⁿ`.  A derivation would instead have *differentiated* the
    product and produced `n` additively. -/
noncomputable def qEulerSystem (σ : A ≃ₐ[R] A) (E : Derivation R A A) {t : A} {c : R}
    (hσt : σ t = c • t) (hcomm : ∀ g : A, σ (E g) = E (σ g)) :
    QBridgeSystem R A ℕ where
  dil := σ
  alien n := t ^ n • E
  weight n := c ^ n
  unipotent _ := 0
  bridge := by
    intro n f
    simp only [conjDeriv_apply, Derivation.smul_apply, smul_eq_mul,
      Derivation.zero_apply, add_zero]
    rw [map_mul, map_pow, hσt, hcomm, σ.apply_symm_apply, smul_pow,
      smul_mul_assoc]

theorem qEulerSystem_isSemisimple (σ : A ≃ₐ[R] A) (E : Derivation R A A) {t : A}
    {c : R} (hσt : σ t = c • t) (hcomm : ∀ g : A, σ (E g) = E (σ g)) :
    (qEulerSystem σ E hσt hcomm).IsSemisimple := fun _ => rfl

/-- **The answer, stated as one theorem.**  Suppose the *same* `(A, E, t)` carries
    both structures — `E t = t` (so `AlienBridge.eulerSystem` applies) and
    `σ t = c·t` with `σ` commuting with `E` (so `qEulerSystem` applies).  Then:

    * the two systems have the **same alien family** `Δ_n = tⁿ·E`, indexed by the
      same `n`;
    * the classical weight is **`n`** — additive;
    * the q-weight is **`cⁿ`** — multiplicative.

    So additive and multiplicative are not rival conventions and not a modelling
    choice.  There is one grading, indexed by `n`; the classical weight *is* that
    index, and the q-weight is the multiplicative character `c^{(−)}` evaluated on
    it.  Which one you see is determined by whether the operator you conjugate by
    is a derivation (differentiates the product ⇒ `n` appears additively) or an
    automorphism (passes through the product ⇒ `cⁿ` appears multiplicatively).

    The general case is neither: `QBridgeSystem` carries a `unipotent` field, and
    `qweight_shift` shows the eigenvalue is then multiplied by the semisimple part
    *and* shifted by the nilpotent one — a Jordan block, the matrix-representation
    form.  Both models here are semisimple; a mixed example needs the q-logarithm,
    which is not built. -/
theorem euler_weight_additive_qweight_multiplicative
    (σ : A ≃ₐ[R] A) (E : Derivation R A A) {t : A} {c : R}
    (ht : E t = t) (hσt : σ t = c • t) (hcomm : ∀ g : A, σ (E g) = E (σ g))
    (n : ℕ) :
    (qEulerSystem σ E hσt hcomm).alien n
        = (AlienBridge.eulerSystem E ht).alien n
      ∧ (AlienBridge.eulerSystem E ht).weight n = (n : R)
      ∧ (qEulerSystem σ E hσt hcomm).weight n = c ^ n :=
  ⟨rfl, rfl, rfl⟩

/-! #### A concrete q-difference witness for the semisimple case

    `qEulerSystem` and the additive-vs-multiplicative theorem are so far
    hypothetical: no actual dilation has been exhibited.  This section supplies
    one — `R[X]` with the genuine q-dilation `X ↦ c·X` and the Euler operator
    `X·d/dX` — so that `euler_weight_additive_qweight_multiplicative` has a model
    in which *both* of its hypotheses hold simultaneously. -/

/-- The dilation automorphism `X ↦ c·X` of `R[X]`, for a unit `c`.  This is the
    algebraic q-dilation `σ_q`. -/
noncomputable def dilateAlgEquiv (R : Type*) [CommRing R] (c : Rˣ) :
    Polynomial R ≃ₐ[R] Polynomial R :=
  AlgEquiv.ofAlgHom
    (Polynomial.aeval (Polynomial.C (c : R) * Polynomial.X))
    (Polynomial.aeval (Polynomial.C ((c⁻¹ : Rˣ) : R) * Polynomial.X))
    (by
      apply Polynomial.algHom_ext
      simp only [AlgHom.coe_comp, Function.comp_apply, Polynomial.aeval_X,
        AlgHom.coe_id, id_eq, Polynomial.aeval_mul, Polynomial.aeval_C,
        Polynomial.algebraMap_eq]
      rw [← mul_assoc, ← Polynomial.C_mul, Units.inv_mul, map_one, one_mul])
    (by
      apply Polynomial.algHom_ext
      simp only [AlgHom.coe_comp, Function.comp_apply, Polynomial.aeval_X,
        AlgHom.coe_id, id_eq, Polynomial.aeval_mul, Polynomial.aeval_C,
        Polynomial.algebraMap_eq]
      rw [← mul_assoc, ← Polynomial.C_mul, Units.mul_inv, map_one, one_mul])

theorem dilateAlgEquiv_apply (R : Type*) [CommRing R] (c : Rˣ) (p : Polynomial R) :
    dilateAlgEquiv R c p = p.comp (Polynomial.C (c : R) * Polynomial.X) := rfl

/-- The **Euler operator** `X·d/dX` on `R[X]`. -/
noncomputable def polyEuler (R : Type*) [CommRing R] :
    Derivation R (Polynomial R) (Polynomial R) :=
  (Polynomial.X : Polynomial R) • AlienBridge.polyDerivation R

theorem polyEuler_apply (R : Type*) [CommRing R] (p : Polynomial R) :
    polyEuler R p = Polynomial.X * Polynomial.derivative p := rfl

/-- `X` is an Euler coordinate: `E X = X`.  Supplies `AlienBridge.eulerSystem`'s
    hypothesis. -/
theorem polyEuler_X (R : Type*) [CommRing R] :
    polyEuler R Polynomial.X = (Polynomial.X : Polynomial R) := by
  rw [polyEuler_apply, Polynomial.derivative_X, mul_one]

/-- The dilation scales `X` by `c`.  Supplies `qEulerSystem`'s first hypothesis. -/
theorem dilateAlgEquiv_X (R : Type*) [CommRing R] (c : Rˣ) :
    dilateAlgEquiv R c Polynomial.X = (c : R) • (Polynomial.X : Polynomial R) := by
  rw [dilateAlgEquiv_apply, Polynomial.X_comp, Polynomial.smul_eq_C_mul]

/-- The dilation commutes with the Euler operator — both are degree operators.
    Supplies `qEulerSystem`'s second hypothesis. -/
theorem dilate_comm_polyEuler (R : Type*) [CommRing R] (c : Rˣ) (p : Polynomial R) :
    dilateAlgEquiv R c (polyEuler R p) = polyEuler R (dilateAlgEquiv R c p) := by
  simp only [polyEuler_apply, dilateAlgEquiv_apply, Polynomial.mul_comp,
    Polynomial.X_comp, Polynomial.derivative_comp, Polynomial.derivative_mul,
    Polynomial.derivative_C, Polynomial.derivative_X, zero_mul, mul_one, zero_add]
  ring

/-- **The concrete q-difference bridge system**: `R[X]`, dilation `X ↦ c·X`,
    `Δ_n := Xⁿ·(X·d/dX)`, multiplicative weight `cⁿ`. -/
noncomputable def polyQEulerSystem (R : Type*) [CommRing R] (c : Rˣ) :
    QBridgeSystem R (Polynomial R) ℕ :=
  qEulerSystem (dilateAlgEquiv R c) (polyEuler R) (dilateAlgEquiv_X R c)
    (dilate_comm_polyEuler R c)

/-- **The additive-vs-multiplicative theorem, concretely witnessed.**  On `R[X]`
    the same family `Δ_n = Xⁿ·(X·d/dX)`, on the same index `n`, has classical
    weight `n` against the Euler *derivation* and q-weight `cⁿ` against the
    *dilation*.  Both hypotheses of
    `euler_weight_additive_qweight_multiplicative` hold here simultaneously, so
    that theorem is not vacuous. -/
theorem polyQEuler_weights (R : Type*) [CommRing R] (c : Rˣ) (n : ℕ) :
    (polyQEulerSystem R c).alien n
        = (AlienBridge.eulerSystem (polyEuler R) (polyEuler_X R)).alien n
      ∧ (AlienBridge.eulerSystem (polyEuler R) (polyEuler_X R)).weight n = (n : R)
      ∧ (polyQEulerSystem R c).weight n = (c : R) ^ n :=
  euler_weight_additive_qweight_multiplicative (dilateAlgEquiv R c) (polyEuler R)
    (polyEuler_X R) (dilateAlgEquiv_X R c) (dilate_comm_polyEuler R c) n

/-! ### A genuinely MIXED model — the unipotent block

    Both models above are semisimple, which would leave `QBridgeSystem`'s
    `unipotent` field untested and the "combined" case decorative.  This section
    exhibits a system where the semisimple part is trivial (`c = 1`) and the
    whole content is unipotent.

    The hypothesis `σ t = t + 1` is not invented for the purpose: it is the
    defining property of the **q-logarithm** `ℓ_q`, for which `σ_q ℓ_q = ℓ_q + 1`.
    In q-difference Galois theory `ℓ_q` generates exactly the unipotent part of
    the local Galois group, the part the torus of characters `qⁿ` is extended by.
    So this is the unipotent block, not a toy. -/

/-- **A mixed (non-semisimple) q-bridge system.**  With `σ t = t + 1` — the
    q-logarithm relation — and `σ ∘ D ∘ σ⁻¹ = D`, the single alien derivation
    `Δ := t·D` satisfies

    `σ ∘ Δ ∘ σ⁻¹ = 1 · Δ + D`,

    i.e. multiplicative weight `1` and unipotent part `D`.  The adjoint action is
    a Jordan block: it fixes the eigenvalue and adds a nilpotent shift. -/
noncomputable def unipotentSystem (σ : A ≃ₐ[R] A) (D : Derivation R A A) {t : A}
    (hσt : σ t = t + 1) (hcomm : ∀ g : A, σ (D (σ.symm g)) = D g) :
    QBridgeSystem R A Unit where
  dil := σ
  alien _ := t • D
  weight _ := 1
  unipotent _ := D
  bridge := by
    intro _ f
    simp only [conjDeriv_apply, Derivation.smul_apply, smul_eq_mul, one_smul]
    rw [map_mul, hσt, hcomm]
    ring

/-- **The mixed model really is mixed.**  Whenever `D ≠ 0` the system is not
    semisimple, so `QBridgeSystem`'s `unipotent` field is not decorative and
    `qweight_shift`'s correction term is not always zero. -/
theorem unipotentSystem_not_isSemisimple (σ : A ≃ₐ[R] A) (D : Derivation R A A)
    {t : A} (hσt : σ t = t + 1) (hcomm : ∀ g : A, σ (D (σ.symm g)) = D g)
    (hD : D ≠ 0) :
    ¬ (unipotentSystem σ D hσt hcomm).IsSemisimple := fun h => hD (h ())

/-! #### A concrete witness for the mixed model

    `R[X]` with the shift `X ↦ X + 1` and `D = d/dX`.  The shift is a genuine
    algebra automorphism, `d/dX` is shift-invariant, and `d/dX ≠ 0`, so the mixed
    system above is inhabited non-trivially. -/

/-- The shift automorphism `X ↦ X + 1` of `R[X]`. -/
noncomputable def shiftAlgEquiv (R : Type*) [CommRing R] :
    Polynomial R ≃ₐ[R] Polynomial R :=
  AlgEquiv.ofAlgHom
    (Polynomial.aeval (Polynomial.X + 1))
    (Polynomial.aeval (Polynomial.X - 1))
    (by apply Polynomial.algHom_ext; simp)
    (by apply Polynomial.algHom_ext; simp)

theorem shiftAlgEquiv_apply (R : Type*) [CommRing R] (p : Polynomial R) :
    shiftAlgEquiv R p = p.comp (Polynomial.X + 1) := rfl

@[simp]
theorem shiftAlgEquiv_X (R : Type*) [CommRing R] :
    shiftAlgEquiv R Polynomial.X = (Polynomial.X : Polynomial R) + 1 := by
  rw [shiftAlgEquiv_apply, Polynomial.X_comp]

/-- `d/dX` is invariant under the shift — the concrete form of `hcomm`. -/
theorem shift_conj_derivative (R : Type*) [CommRing R] (f : Polynomial R) :
    shiftAlgEquiv R (AlienBridge.polyDerivation R ((shiftAlgEquiv R).symm f))
      = AlienBridge.polyDerivation R f := by
  have hcomp : ∀ p : Polynomial R,
      shiftAlgEquiv R (Polynomial.derivative p)
        = Polynomial.derivative (shiftAlgEquiv R p) := by
    intro p
    rw [shiftAlgEquiv_apply, shiftAlgEquiv_apply, Polynomial.derivative_comp]
    simp
  show shiftAlgEquiv R (Polynomial.derivative _) = Polynomial.derivative f
  rw [hcomp, AlgEquiv.apply_symm_apply]

theorem polyDerivation_ne_zero (R : Type*) [CommRing R] [Nontrivial R] :
    AlienBridge.polyDerivation R ≠ 0 := by
  intro h
  have hX : AlienBridge.polyDerivation R Polynomial.X = 0 := by rw [h]; rfl
  have : (1 : Polynomial R) = 0 := by
    rw [← Polynomial.derivative_X (R := R)]; exact hX
  exact one_ne_zero this

/-- **The concrete mixed system.**  `R[X]`, the shift `X ↦ X + 1`, `Δ := X·d/dX`.
    Its adjoint action under the shift is `Δ ↦ Δ + d/dX`: weight `1`, unipotent
    part `d/dX`. -/
noncomputable def polyUnipotentSystem (R : Type*) [CommRing R] :
    QBridgeSystem R (Polynomial R) Unit :=
  unipotentSystem (shiftAlgEquiv R) (AlienBridge.polyDerivation R)
    (shiftAlgEquiv_X R) (shift_conj_derivative R)

/-- **The `unipotent` field is not decorative.**  A concrete system whose adjoint
    action is a genuine Jordan block: the semisimple weight is `1`, so
    `qweight_shift_of_semisimple` does not apply, and the correction term in
    `qweight_shift` is `d/dX ≠ 0`. -/
theorem polyUnipotentSystem_not_isSemisimple (R : Type*) [CommRing R]
    [Nontrivial R] : ¬ (polyUnipotentSystem R).IsSemisimple :=
  unipotentSystem_not_isSemisimple _ _ _ _ (polyDerivation_ne_zero R)

/-! ### The twist: why the index set must be `E_q`, proved rather than asserted

    `QBridgeSystem` above assumes `σ ∘ Δ_ω ∘ σ⁻¹` is a multiple of **`Δ_ω` itself**
    — the *same* index.  For q-difference equations that is an over-restriction,
    and the reason is geometric: the dilation acts on the Borel plane too, so it
    moves a singularity at `ω` to one at `qω`.  The honest general form carries a
    **shift** on the index set,

    `σ ∘ Δ_ω ∘ σ⁻¹  =  c_ω · Δ_{shift ω}  +  N_ω`,

    and `QBridgeSystem` is the `shift = id` case (`ofUntwisted` / `untwist`).

    Two facts make this precise, and both are theorems here rather than prose:

    * `shift_mul_eq_id_iff` — on a group of singularity locations with
      `shift ω = q·ω`, the shift is the identity **iff `q = 1`**.  So for a genuine
      dilation the untwisted form is simply unavailable on `ℂ*`.
    * `untwist` — the twist disappears exactly when the alien family is invariant
      under the shift, i.e. **constant along q-spirals**, i.e. factors through
      `ℂ*/q^ℤ = E_q`.

    Together: `E_q` is not a convenient choice of base, it is forced — it is
    precisely the quotient on which the bridge relation can be index-preserving.
    That is independent corroboration of the corpus's `E_q` framing, where the
    third singular site `x = q⁻²` was found to be the identity orbit `[q⁻²] = [1]`
    ([`2026-08-08-rsz-c1-infinity-route-closed.md`](../../../../../docs/audits/2026-08-08-rsz-c1-infinity-route-closed.md)).

    `conjDeriv_iterate` is the content of the twist when it is *not* removed:
    iterating the conjugation walks the orbit and **accumulates the product** of
    the weights along it. -/

/-- A **twisted** q-bridge system: like `QBridgeSystem`, but the conjugation may
    move the singularity index by `shift`. -/
structure TwistedQBridgeSystem (R A Ω : Type*) [CommSemiring R] [CommRing A]
    [Algebra R A] where
  /-- The dilation automorphism. -/
  dil : A ≃ₐ[R] A
  /-- The alien derivation at `ω`. -/
  alien : Ω → Derivation R A A
  /-- The multiplicative weight. -/
  weight : Ω → R
  /-- The induced motion of the singularity index (`ω ↦ qω` for a dilation). -/
  shift : Ω → Ω
  /-- The nilpotent part. -/
  unipotent : Ω → Derivation R A A
  /-- The twisted q-bridge equation. -/
  bridge : ∀ (ω : Ω) (f : A),
    conjDeriv dil (alien ω) f
      = weight ω • alien (shift ω) f + unipotent ω f

namespace TwistedQBridgeSystem

/-- No unipotent part. -/
def IsSemisimple (S : TwistedQBridgeSystem R A Ω) : Prop := ∀ ω : Ω, S.unipotent ω = 0

/-- The bridge at the level of derivations, in the semisimple case. -/
theorem bridge_deriv (S : TwistedQBridgeSystem R A Ω) (hss : S.IsSemisimple)
    (ω : Ω) :
    conjDeriv S.dil (S.alien ω) = S.weight ω • S.alien (S.shift ω) := by
  ext f
  have h := S.bridge ω f
  rw [hss ω] at h
  simpa using h

/-- **Weights accumulate along the orbit.**  Conjugating `n` times walks the index
    along `shift` and multiplies the weights encountered on the way:

    `σⁿ ∘ Δ_ω ∘ σ⁻ⁿ = (∏_{k<n} c_{shiftᵏ ω}) · Δ_{shiftⁿ ω}`.

    This is the content of the twist.  When `shift = id` it collapses to
    `c_ω ⁿ · Δ_ω`, recovering the untwisted picture; when `shift` is a genuine
    dilation of the Borel plane the index genuinely moves, and the product is over
    a whole q-spiral. -/
theorem conjDeriv_iterate (S : TwistedQBridgeSystem R A Ω) (hss : S.IsSemisimple)
    (ω : Ω) : ∀ n : ℕ,
    (conjDeriv S.dil)^[n] (S.alien ω)
      = (∏ k ∈ Finset.range n, S.weight (S.shift^[k] ω))
          • S.alien (S.shift^[n] ω) := by
  intro n
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Function.iterate_succ_apply', ih, conjDeriv_smul,
      S.bridge_deriv hss (S.shift^[n] ω), smul_smul, Finset.prod_range_succ,
      ← Function.iterate_succ_apply' S.shift n]

/-- **The twist vanishes exactly when the alien family is shift-invariant.**

    `hinv` says the family is constant along the orbit of `shift` — for the
    dilation, constant along q-spirals, i.e. factoring through `E_q = ℂ*/q^ℤ`.
    Under it the twisted system *is* an untwisted `QBridgeSystem`, with the same
    data. -/
def untwist (S : TwistedQBridgeSystem R A Ω)
    (hinv : ∀ ω : Ω, S.alien (S.shift ω) = S.alien ω) : QBridgeSystem R A Ω where
  dil := S.dil
  alien := S.alien
  weight := S.weight
  unipotent := S.unipotent
  bridge := fun ω f => by rw [S.bridge ω f, hinv ω]

end TwistedQBridgeSystem

/-- Every untwisted system is a twisted one with `shift = id`, so nothing proved
    about `QBridgeSystem` is lost. -/
def QBridgeSystem.toTwisted (S : QBridgeSystem R A Ω) :
    TwistedQBridgeSystem R A Ω where
  dil := S.dil
  alien := S.alien
  weight := S.weight
  shift := id
  unipotent := S.unipotent
  bridge := S.bridge

/-- **On `ℂ*` the twist is unavoidable.**  For singularity locations forming a
    group and `shift ω = q·ω`, the shift is the identity **iff `q = 1`**.  So for a
    genuine dilation (`q ≠ 1`) no untwisted `QBridgeSystem` on that index set
    exists, and one must pass to the spiral quotient.  This is the precise sense
    in which `E_q` is forced rather than chosen. -/
theorem shift_mul_eq_id_iff {G : Type*} [Group G] (q : G) :
    (fun ω : G => q * ω) = id ↔ q = 1 := by
  constructor
  · intro h
    simpa using congrFun h 1
  · intro h
    funext ω
    simp [h]

/-- **A prune: the monomial grading carries no q-bridge weight.**

    The dilation acts on the monomial `x^{n}` with eigenvalue `qⁿ`, and every
    `qⁿ` lies in `q^ℤ` — the *identity* class of `E_q = ℂ*/q^ℤ`.  So on the index
    set of monomial `σ`-eigenvalue **classes** there is only one class: the shift
    is trivially the identity, `untwist` applies for an empty reason, and no
    weight distinguishes anything.

    **Reading — scope-(a), a where-not-to-look result, not a computation.**
    Whatever q-bridge weight a q-difference module carries, it is not visible in
    the monomial grading of its formal solution.  For C1's `∞` side the weight
    would have to come from the *quadratic* factor certified by
    `deg_q(cₙ) = n²` (`QOU.QBeta.cCoeff_natDegree`), not from the powers of `x`.
    Nothing here says the weight is trivial, or that C1 has no weight; it says
    this particular grading cannot exhibit one. -/
theorem monomial_eigenvalue_mem_zpowers {G : Type*} [Group G] (q : G) (n : ℤ) :
    q ^ n ∈ Subgroup.zpowers q := Subgroup.mem_zpowers_iff.mpr ⟨n, rfl⟩

end QOU.Mathlib.QAlienBridge
