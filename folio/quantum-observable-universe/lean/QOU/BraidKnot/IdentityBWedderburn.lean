import Mathlib.LinearAlgebra.Trace
import Mathlib.LinearAlgebra.Pi
import Mathlib.LinearAlgebra.FreeModule.Finite.Matrix
import Mathlib.Logic.Equiv.Fin.Basic
import Mathlib.Data.Fintype.Option
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.RingTheory.MatrixAlgebra
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.LinearAlgebra.Dimension.Constructions
import Mathlib.Algebra.Central.Defs
import Mathlib.RingTheory.SimpleModule.WedderburnArtin
import Mathlib.RingTheory.SimpleModule.IsAlgClosed
import Mathlib.RepresentationTheory.Maschke
import Mathlib.Data.Complex.Basic
import Mathlib.FieldTheory.IsAlgClosed.Basic
import QOU.BraidKnot.RegularRepTrace
import QOU.BraidKnot.IdentityBCentrality

/-!
# Identity (B) for `ℂ[Sₙ]` via Artin–Wedderburn — fully sorry-free

The keystone's second carried representation-theory input — the **Plancherel content-square
mean**

$$ \mathbb{E}_{\mathrm{Planch}}\Big[\textstyle\sum_{c\in\lambda} c(c)^2\Big]
   \;=\; \binom{n}{2}, \qquad\text{i.e.}\qquad
   \sum_{\lambda\vdash n} (f^\lambda)^2 \Big(\textstyle\sum_{c\in\lambda} c(c)^2\Big)
   \;=\; n!\,\binom{n}{2}, $$

is proved here for `ℂ[Sₙ]` **without any `sorry`**: the Wedderburn/Schur side is the generic
semisimple trace identity below, and the one classical input — centrality of the second
Jucys–Murphy power sum `C₂ = ∑ₖ Xₖ²` — is proved in `QOU.BraidKnot.IdentityBCentrality`
(Jucys' theorem: at the coefficient level `C₂ = binom(n,2)·1 + class-sum of 3-cycles`).

## What is proved sorry-free here

The entire Wedderburn/Schur "side 2" is discharged **without any Sₙ-specific Okounkov–Vershik
data** by the generic semisimple trace identity:

* `AbsTrace.trace_piMapEndo` — trace of a block-diagonal endomorphism of `∀ i, Mᵢ` is the sum of
  block traces (`Fintype.induction_empty_option`).
* `AbsTrace.trace_mulLeft_pi_matrix` — for a central element of `∏ᵢ Matₐᵢ(F)` whose `i`-th
  component is the scalar matrix `ωᵢ·1`, the regular-representation trace of `mulLeft` is
  `∑ᵢ dᵢ²·ωᵢ`.
* `AbsTrace.trace_mulLeft_central_eq_block_sum` — **the abstract discharge.** For a *central*
  `z` in a finite-dimensional semisimple algebra `A` over an algebraically closed field `F`,
  there are block data `(d, ω)` with `∑ dᵢ² = finrank_F A` and `trace_F(mulLeft z) = ∑ dᵢ²·ωᵢ`,
  via Mathlib's `IsSemisimpleRing.exists_algEquiv_pi_matrix_of_isAlgClosed` (Artin–Wedderburn) +
  `Matrix.center_eq_range` (concrete Schur) + the Pi-trace decomposition.

Specialising to `A = ℂ[Sₙ]` (semisimple by Maschke, alg-closed by `IsAlgClosed ℂ`) and
`z = C₂`, and reading the easy-side `trace(mulLeft C₂) = n!·binom(n,2)` off
`RegularRepTrace.trace_centralC2_eq_factorial_mul_choose_two`, gives:

* `identityB_via_wedderburn` — Identity (B) given the hypothesis `C₂ ∈ Set.center ℂ[Sₙ]`.
  The quadratic weighting and `∑ dᵢ² = n!` are *produced*, not assumed.
* `identityB_via_wedderburn_unconditional` — **fully sorry-free**: the centrality hypothesis is
  discharged by `IdentityBCentrality.centralC2_mem_center`. Axioms:
  `[propext, Classical.choice, Quot.sound]`.

## Why this is more atomic than the carried OV bundle

`RegularRepBlockTrace.identityB_conditional` carries the full `SnWedderburnSpectralData` bundle
(the *labelled* block decomposition: partition ↔ irreducible, `dim = #SYT`, JM-eigenvalue =
contents). Here the conditional form `identityB_via_wedderburn` assumes only the centrality of
`C₂` — the block structure, the quadratic dimension weighting, and `∑ dᵢ² = n!` are
*machine-derived* from Artin–Wedderburn — and the **unconditional** theorem carries no remaining
Sₙ-specific hypothesis: that centrality is proved in `IdentityBCentrality`.

No `native_decide`, no `: True`, no statement-weakening; the base ring is `ℂ` exactly where the
representation theory needs alg-closedness + characteristic zero.

Ref: [vershik-kerov1977] (Okounkov–Vershik / Jucys central elements).
-/

open scoped Classical BigOperators
namespace AbsTrace
universe u w
variable {R : Type u} [CommRing R]

noncomputable def piMapEndo {ι : Type*} {M : ι → Type*} [∀ i, AddCommGroup (M i)]
    [∀ i, Module R (M i)] (f : ∀ i, M i →ₗ[R] M i) : (∀ i, M i) →ₗ[R] (∀ i, M i) :=
  LinearMap.pi (fun i => f i ∘ₗ LinearMap.proj i)

@[simp] lemma piMapEndo_apply {ι : Type*} {M : ι → Type*} [∀ i, AddCommGroup (M i)]
    [∀ i, Module R (M i)] (f : ∀ i, M i →ₗ[R] M i) (x : ∀ i, M i) (i : ι) :
    piMapEndo f x i = f i (x i) := rfl

private lemma pcl_apply {ι κ : Type*} (e : κ ≃ ι) {M : ι → Type*}
    [∀ i, AddCommGroup (M i)] [∀ i, Module R (M i)] (g : ∀ j, M (e j)) (j : κ) :
    (LinearEquiv.piCongrLeft R M e) g (e j) = g j := by
  show (LinearEquiv.piCongrLeft' R M e.symm).symm g (e j) = g j
  rw [LinearEquiv.piCongrLeft'_symm_apply]
  exact Equiv.piCongrLeft'_symm_apply_apply M e.symm g j

private lemma pcl_symm_apply {ι κ : Type*} (e : κ ≃ ι) {M : ι → Type*}
    [∀ i, AddCommGroup (M i)] [∀ i, Module R (M i)] (x : ∀ i, M i) (j : κ) :
    (LinearEquiv.piCongrLeft R M e).symm x j = x (e j) := by
  show (LinearEquiv.piCongrLeft' R M e.symm) x j = x (e j)
  rw [LinearEquiv.piCongrLeft'_apply]; simp

lemma piMapEndo_option_conj {ι : Type*} {M : Option ι → Type*}
    [∀ i, AddCommGroup (M i)] [∀ i, Module R (M i)] (f : ∀ i, M i →ₗ[R] M i) :
    (LinearEquiv.piOptionEquivProd R).conj (piMapEndo f)
      = (f none).prodMap (piMapEndo (fun i => f (some i))) := by
  ext x i <;> · simp [LinearEquiv.conj_apply, piMapEndo, LinearEquiv.piOptionEquivProd]

lemma piMapEndo_congrLeft_conj {ι κ : Type*} (e : κ ≃ ι) {M : ι → Type*}
    [∀ i, AddCommGroup (M i)] [∀ i, Module R (M i)] (f : ∀ i, M i →ₗ[R] M i) :
    (LinearEquiv.piCongrLeft R M e).conj (piMapEndo (fun j => f (e j)))
      = piMapEndo f := by
  apply LinearMap.ext; intro x
  rw [LinearEquiv.conj_apply]; apply funext
  refine e.surjective.forall.2 (fun j => ?_)
  rw [LinearMap.comp_apply, LinearMap.comp_apply]
  simp only [LinearEquiv.coe_coe]
  rw [pcl_apply, piMapEndo_apply, pcl_symm_apply, piMapEndo_apply]

private lemma trace_option_step {ι : Type*} [Fintype ι] {M : Option ι → Type w}
    [∀ i, AddCommGroup (M i)] [∀ i, Module R (M i)]
    [∀ i, Module.Free R (M i)] [∀ i, Module.Finite R (M i)]
    (f : ∀ i, M i →ₗ[R] M i)
    (IH : LinearMap.trace R (∀ i : ι, M (some i)) (piMapEndo (fun i => f (some i)))
            = ∑ i : ι, LinearMap.trace R (M (some i)) (f (some i))) :
    LinearMap.trace R (∀ i, M i) (piMapEndo f)
      = ∑ i : Option ι, LinearMap.trace R (M i) (f i) := by
  rw [← LinearMap.trace_conj' (piMapEndo f) (LinearEquiv.piOptionEquivProd R),
      piMapEndo_option_conj, LinearMap.trace_prodMap', IH, Fintype.sum_option]

private def PiTraceProp (ι : Type*) [Fintype ι] : Prop :=
  ∀ (M : ι → Type w) [∀ i, AddCommGroup (M i)] [∀ i, Module R (M i)]
    [∀ i, Module.Free R (M i)] [∀ i, Module.Finite R (M i)] (f : ∀ i, M i →ₗ[R] M i),
    LinearMap.trace R (∀ i, M i) (piMapEndo f) = ∑ i, LinearMap.trace R (M i) (f i)

private lemma piTraceProp_all (ι : Type*) [Fintype ι] : PiTraceProp.{u, w} (R := R) ι := by
  refine Fintype.induction_empty_option
    (P := fun α _ => PiTraceProp.{u, w} (R := R) α) ?_ ?_ ?_ ι
  · intro α β instβ e IH M _ _ _ _ f
    haveI instα : Fintype α := Fintype.ofEquiv β e.symm
    rw [← piMapEndo_congrLeft_conj e f, LinearMap.trace_conj',
        IH (fun j => M (e j)) (fun j => f (e j))]
    -- ∑_{j:α} trace(M(e j))(f(e j)) = ∑_{i:β} trace(M i)(f i), reindex by e
    refine Finset.sum_nbij' e e.symm ?_ ?_ ?_ ?_ ?_ <;>
      simp [Equiv.symm_apply_apply, Equiv.apply_symm_apply]
  · show PiTraceProp.{u, w} (R := R) PEmpty
    intro M _ _ _ _ f
    rw [Finset.univ_eq_empty, Finset.sum_empty]
    rw [show piMapEndo f = 0 from Subsingleton.elim _ _, map_zero]
  · intro α _ IH M _ _ _ _ f
    exact trace_option_step f (IH (fun i => M (some i)) (fun i => f (some i)))

/-- **Pi-trace decomposition.** The trace of the block-diagonal endomorphism
`(x i) ↦ (f i (x i))` of `∀ i, M i` (finite-dimensional free `R`-modules) is the sum of
block traces. -/
theorem trace_piMapEndo {ι : Type*} [Fintype ι] {M : ι → Type w}
    [∀ i, AddCommGroup (M i)] [∀ i, Module R (M i)]
    [∀ i, Module.Free R (M i)] [∀ i, Module.Finite R (M i)]
    (f : ∀ i, M i →ₗ[R] M i) :
    LinearMap.trace R (∀ i, M i) (piMapEndo f) = ∑ i, LinearMap.trace R (M i) (f i) :=
  piTraceProp_all.{u, w} (R := R) ι M f


/-! ## Matrix-block ingredients -/

/-- Trace of left-multiplication by the scalar matrix `c•1` on `Mat_d(F)` (a `d²`-dim free module)
is `d²·c`. Proof: `mulLeft (c•1) = c • id`, `trace (c • id) = c · finrank = c·d²`. -/
theorem trace_mulLeft_scalar {F : Type*} [Field F] (d : ℕ) (c : F) :
    LinearMap.trace F (Matrix (Fin d) (Fin d) F)
        (LinearMap.mulLeft F (Matrix.scalar (Fin d) c)) = (d : F) ^ 2 * c := by
  have hms : Matrix.scalar (Fin d) c = c • (1 : Matrix (Fin d) (Fin d) F) := by
    rw [Matrix.smul_one_eq_diagonal]; ext i j; simp [Matrix.scalar, Matrix.diagonal]
  have hml : LinearMap.mulLeft F (c • (1 : Matrix (Fin d) (Fin d) F)) = c • LinearMap.id := by
    ext x; simp [LinearMap.mulLeft_apply]
  rw [hms, hml, map_smul, LinearMap.trace_id, smul_eq_mul, Module.finrank_matrix,
      Module.finrank_self, Fintype.card_fin]
  push_cast; ring

/-- Left-multiplication by an element of a finite product ring is the block-diagonal endo of the
componentwise left-multiplications. -/
theorem mulLeft_pi_eq_piMapEndo {ι : Type*} {F : Type*} [CommRing F] {A : ι → Type*}
    [∀ i, Ring (A i)] [∀ i, Algebra F (A i)] (z : ∀ i, A i) :
    LinearMap.mulLeft F z = piMapEndo (fun i => LinearMap.mulLeft F (z i)) := by
  ext x i; simp [piMapEndo, LinearMap.mulLeft_apply, Pi.mul_apply]

/-- A central element of a finite product ring is central componentwise. -/
theorem center_pi_componentwise {ι : Type*} {A : ι → Type*} [∀ i, Ring (A i)]
    (z : ∀ i, A i) (hz : z ∈ Set.center (∀ i, A i)) (i : ι) :
    z i ∈ Set.center (A i) := by
  rw [Semigroup.mem_center_iff] at hz ⊢
  intro a
  have h := congrFun (hz (Pi.single i a)) i
  simpa using h

/-! ## The abstract trace identity over a product of matrix algebras -/

/-- **Abstract trace identity (product-of-matrices form).** For a central element `z` of
`∏ᵢ Mat_{dᵢ}(F)` over a field `F`, the trace of left-multiplication by `z` on the regular
representation is `∑ᵢ dᵢ²·ωᵢ`, where `z i = Matrix.scalar (ω i)` is the scalar by which `z` acts on
block `i` (its centrality forces each component to be a scalar matrix — concrete Schur's lemma).

Pure linear algebra: `mulLeft z` is block-diagonal (`mulLeft_pi_eq_piMapEndo`); its trace splits as
the block sum (`trace_piMapEndo`); each block trace is `dᵢ²·ωᵢ` (`trace_mulLeft_scalar`). No
representation theory, no Wedderburn — this is the trace bookkeeping that the abstract decomposition
feeds into. -/
theorem trace_mulLeft_pi_matrix {ι : Type*} [Fintype ι] {F : Type*} [Field F]
    (d : ι → ℕ) (ω : ι → F) :
    LinearMap.trace F (∀ i, Matrix (Fin (d i)) (Fin (d i)) F)
        (LinearMap.mulLeft F (fun i => Matrix.scalar (Fin (d i)) (ω i)))
      = ∑ i, (d i : F) ^ 2 * ω i := by
  rw [mulLeft_pi_eq_piMapEndo, trace_piMapEndo]
  exact Finset.sum_congr rfl (fun i _ => trace_mulLeft_scalar (d i) (ω i))

/-! ## Wedderburn bridge: from a general semisimple algebra to the block sum -/

/-- `mulLeft` transported across an algebra equivalence is conjugation of `mulLeft`. -/
theorem mulLeft_algEquiv_conj {F A B : Type*} [CommRing F] [Ring A] [Ring B]
    [Algebra F A] [Algebra F B] (Φ : A ≃ₐ[F] B) (z : A) :
    LinearMap.mulLeft F (Φ z) = Φ.toLinearEquiv.conj (LinearMap.mulLeft F z) := by
  ext y; simp [LinearMap.mulLeft_apply, LinearEquiv.conj_apply]

/-- **Abstract trace identity, semisimple-algebra form (the abstract discharge).**
Let `A` be a finite-dimensional algebra over an algebraically closed field `F`, with `A` semisimple
(e.g. `A = F[G]` for a finite group with `|G|` invertible, by Maschke). For any **central** `z ∈ A`,
there is a finite family of block dimensions `d : Fin n → ℕ` and block scalars `ω : Fin n → F` with
* `∑ᵢ dᵢ² = finrank_F A`  (the Artin–Wedderburn sum-of-squares), and
* `trace_F(mulLeft z) = ∑ᵢ dᵢ²·ωᵢ`  (**Identity-(B) trace, side 2**, abstractly),

obtained from the Artin–Wedderburn isomorphism `A ≃ₐ[F] ∏ᵢ Mat_{dᵢ}(F)` (Mathlib's
`exists_algEquiv_pi_matrix_of_isAlgClosed`) by transporting `mulLeft z` (concrete Schur: `z`
central ⇒ each block component is a scalar matrix `Matrix.scalar (ωᵢ)`) and applying the Pi-trace
decomposition. **This needs no S_n-specific Okounkov–Vershik data** — it is the generic semisimple
trace identity. -/
theorem trace_mulLeft_central_eq_block_sum
    (F A : Type*) [Field F] [IsAlgClosed F] [Ring A] [Algebra F A]
    [IsSemisimpleRing A] [FiniteDimensional F A]
    (z : A) (hz : z ∈ Set.center A) :
    ∃ (n : ℕ) (d : Fin n → ℕ) (ω : Fin n → F),
      (∑ i, (d i : F) ^ 2 = (Module.finrank F A : F)) ∧
      LinearMap.trace F A (LinearMap.mulLeft F z) = ∑ i, (d i : F) ^ 2 * ω i := by
  obtain ⟨n, d, _, ⟨Φ⟩⟩ :=
    IsSemisimpleRing.exists_algEquiv_pi_matrix_of_isAlgClosed F A
  -- Φ : A ≃ₐ[F] ∀ i, Matrix (Fin (d i)) (Fin (d i)) F
  -- Φ z is central; each component is a scalar matrix
  have hΦz : Φ z ∈ Set.center (∀ i, Matrix (Fin (d i)) (Fin (d i)) F) :=
    (MulEquivClass.apply_mem_center_iff Φ).mpr hz
  -- choose ω i with (Φ z) i = scalar (ω i)
  have hscal : ∀ i, ∃ c, (Φ z) i = Matrix.scalar (Fin (d i)) c := by
    intro i
    have hi := center_pi_componentwise (Φ z) hΦz i
    rw [Matrix.center_eq_range] at hi
    obtain ⟨c, hc⟩ := hi
    exact ⟨c, hc.symm⟩
  choose ω hω using hscal
  refine ⟨n, d, ω, ?_, ?_⟩
  · -- ∑ dᵢ² = finrank A.  finrank A = finrank (∏ Mat) = ∑ dᵢ² via Φ
    have hfr : Module.finrank F A
        = Module.finrank F (∀ i, Matrix (Fin (d i)) (Fin (d i)) F) :=
      LinearEquiv.finrank_eq Φ.toLinearEquiv
    haveI : ∀ i, Module.Finite F (Matrix (Fin (d i)) (Fin (d i)) F) := fun i => inferInstance
    rw [hfr, Module.finrank_pi_fintype]
    push_cast
    refine Finset.sum_congr rfl (fun i _ => ?_)
    rw [Module.finrank_matrix, Module.finrank_self, Fintype.card_fin]
    push_cast; ring
  · -- trace identity.  Convert trace_A (mulLeft z) → trace_∏ (mulLeft (Φ z)) via the equiv,
    -- then read off the block scalars.
    have hΦeq : (fun i => Matrix.scalar (Fin (d i)) (ω i)) = Φ z := funext (fun i => (hω i).symm)
    rw [← LinearMap.trace_conj' (LinearMap.mulLeft F z) Φ.toLinearEquiv,
        ← mulLeft_algEquiv_conj Φ z, ← hΦeq, trace_mulLeft_pi_matrix]

end AbsTrace

/-! ## Specialisation to `ℂ[S_n]`: Identity (B) modulo only the centrality of `C₂`

The abstract `trace_mulLeft_central_eq_block_sum` discharges the **entire** Wedderburn/Schur side 2
without any S_n-specific Okounkov–Vershik input.  Specialising to `A = ℂ[S_n]` (semisimple by
Maschke, alg-closed by `IsAlgClosed ℂ`) and `z = C₂` yields Identity (B) — `∑ dᵢ²·ωᵢ = n!·binom(n,2)`
with `∑ dᵢ² = n!` — with the *single* residual hypothesis that `C₂ ∈ Set.center ℂ[S_n]`.

This is a **much smaller** input than the full `SnWedderburnSpectralData` bundle carried by
`RegularRepBlockTrace.identityB_conditional`: that bundle assumes the existence of the *labelled*
block decomposition (partition ↔ irreducible, `dim = #SYT`, JM-eigenvalue = contents).  Here ONLY
the centrality of `C₂` is assumed; the block structure, the quadratic dimension weighting, and the
sum-of-squares `∑ dᵢ² = n!` are all **produced** by Artin–Wedderburn + the Pi-trace decomposition. -/

open QOU.BraidKnot.RegularRepTrace (centralC2 trace_centralC2_eq_factorial_mul_choose_two) in
/-- **Identity (B) for `ℂ[S_n]`, conditional only on the centrality of `C₂`.** There exist block
dimensions `d : Fin N → ℕ` and block scalars `ω : Fin N → ℂ` with
`∑ dᵢ² = n!` (Artin–Wedderburn sum-of-squares) and `∑ dᵢ²·ωᵢ = n!·binom(n,2)` (**Identity (B)**),
the only hypothesis being that the Jucys–Murphy central element `C₂ = ∑_k X_k²` is central. The
quadratic weighting and `∑ dᵢ² = n!` are derived, not assumed; reading `ωᵢ = ∑_{c∈λᵢ} c(c)²` and
`dᵢ = #SYT(λᵢ)` (the two OV labelling bricks, out of scope) makes this the literal Plancherel
content-square mean. -/
theorem identityB_via_wedderburn (n : ℕ)
    (hcentral : centralC2 (R := ℂ) n ∈ Set.center (MonoidAlgebra ℂ (Equiv.Perm (Fin n)))) :
    ∃ (N : ℕ) (d : Fin N → ℕ) (ω : Fin N → ℂ),
      (∑ i, (d i : ℂ) ^ 2 = (n.factorial : ℂ)) ∧
      (∑ i, (d i : ℂ) ^ 2 * ω i = (n.factorial : ℂ) * (n.choose 2 : ℂ)) := by
  obtain ⟨N, d, ω, hsumsq, htrace⟩ :=
    AbsTrace.trace_mulLeft_central_eq_block_sum ℂ (MonoidAlgebra ℂ (Equiv.Perm (Fin n)))
      (centralC2 (R := ℂ) n) hcentral
  refine ⟨N, d, ω, ?_, ?_⟩
  · -- ∑ dᵢ² = finrank ℂ[S_n] = n!
    have hfr : Module.finrank ℂ (MonoidAlgebra ℂ (Equiv.Perm (Fin n))) = n.factorial := by
      show Module.finrank ℂ (Equiv.Perm (Fin n) →₀ ℂ) = n.factorial
      rw [Module.finrank_finsupp_self, Fintype.card_perm, Fintype.card_fin]
    rw [hsumsq, hfr]
  · -- ∑ dᵢ² ωᵢ = trace (mulLeft C₂) = n!·binom(n,2)
    rw [← htrace, trace_centralC2_eq_factorial_mul_choose_two]

/-- **Identity (B) for `ℂ[S_n]`, fully sorry-free.** Same conclusion as
`identityB_via_wedderburn`, with the centrality `C₂ ∈ Set.center ℂ[Sₙ]` discharged by
`IdentityBCentrality.centralC2_mem_center` (Jucys' theorem, machine-checked: the coefficient of
`C₂` is a class function — `binom(n,2)` at `1`, `1` at each 3-cycle, `0` elsewhere). Every link —
the Wedderburn block decomposition, the quadratic dimension weighting, `∑ dᵢ² = n!`, side-1
`trace = n!·binom`, the center-reduction machinery, and the 3-cycle count — is proved; axioms:
`[propext, Classical.choice, Quot.sound]`. -/
theorem identityB_via_wedderburn_unconditional (n : ℕ) :
    ∃ (N : ℕ) (d : Fin N → ℕ) (ω : Fin N → ℂ),
      (∑ i, (d i : ℂ) ^ 2 = (n.factorial : ℂ)) ∧
      (∑ i, (d i : ℂ) ^ 2 * ω i = (n.factorial : ℂ) * (n.choose 2 : ℂ)) :=
  identityB_via_wedderburn n (QOU.BraidKnot.IdentityBCentrality.centralC2_mem_center n)
