import QOU.Transcendental.MassTheory.BridgeAStokesNBody

/-!
# Bridge A, gap 4: two-body locality (P2) from regular singularity, and where Deligne enters

Workstream W7 of the L2 1-ppQ plan (gap 4 of the Stokes-to-Hecke bridge); bean `qou-x09k`.
Companion to `BridgeAStokesNBody`, which takes P1–P3 as hypotheses.

## 1. The triple-collision gap in P2 (`n ≥ 4`)

The written P2 argument (audit `qou-derivation-chain/bridge-a/a2-lagrangian-kz.md`, §P2) assumes

* (a) logarithmic poles along the diagonals (Saito's condition),
* (b) Reeb (Euler-dilation) invariance,
* (c) *regular residues*: the residue along `z_m = z_j` has no pole when a third point arrives.

From (a)–(c) the residues are constant (`LagrangianKZ.eval_const_of_dilation_invariant`). For
`n = 3`, (c) follows from translation invariance; for `n ≥ 4` it does not. Measured exactly
(rational arithmetic, `computations/bridge_a/p2_triple_collision_probe.py`): at `n = 4` the
scalar forms satisfying (a), (b), translation invariance and `ι_T ω = 0` form a 10-dimensional
space, of which the Arnold forms `Σ c_ij dlog(z_i − z_j)` are 6 dimensions. The 4 extra
directions have residues with poles at triple collisions: the probe's element with
`P₁ = −(z₁ − z₄)²` has residue `−(z₂ − z₄)/(z₂ − z₃)` along `z₁ = z₂`, with a pole at the
triple collision `z₁ = z₂ = z₃`. So (c) is a genuine extra condition on the class, not a
consequence of (a)–(b).

In the same probe, flatness removes the 4 extra directions in every case tried: closed scalar
forms, abelian twists `dη + λ ∧ η = 0` (generic and one resonant `λ`), and first-order flat
deformations of KZ on the 2-dimensional irreducible representation of `S₄` at
`κ ∈ {3/7, 1/3, 1/2, 1}` (the last three resonant). This is evidence that flatness implies (c).
It is not a proof (it is first order, one representation, `n = 4`), and it is not used below.

## 2. What replaces (c): log poles on the collision compactification (one cited input)

Write `Conf_n⁰ = Conf_n / translations ≅ ℂ^* × M_{0,n+1}` (scale `t = z₁ − z₂`, and the
projective class of the configuration). It has the normal-crossings compactification
`P¹ × M̄_{0,n+1}`, whose boundary divisors are: total collision (`t = 0`), points flying apart
(`t = ∞`), and one divisor for every sub-collision `S ⊆ {1, …, n}`, `|S| ≥ 2`. The triple
collisions are among these divisors.

**Cited theorem** (`ArnoldSpan` below). Every global logarithmic 1-form on
`P¹ × M̄_{0,n+1}` pulls back to `Conf_n` as a constant combination of the forms
`dlog(z_i − z_j)`. Proof outline, from the literature:

* global logarithmic forms on a smooth compactification with normal-crossings boundary are
  closed, and the space of global logarithmic 1-forms is `F¹H¹` of the open variety
  (Deligne, *Théorie de Hodge II*, §3.2);
* `H¹(Conf_n, ℂ)` is spanned by the classes of `dlog(z_i − z_j)`, which are logarithmic on the
  compactification (Arnold 1969), so `F¹H¹ = H¹` and the dlog forms already fill the space;
* on `P¹`, the only global logarithmic form with poles at `0, ∞` is `c·dt/t`, and
  `dt/t = dlog(z₁ − z₂)`.

What the citation asks of the Lagrangian connection is a **modelling input**, stated plainly:
*the trivialisation of P1 extends over `P¹ × M̄_{0,n+1}` with logarithmic poles along every
boundary divisor.* That is regular singularity at all collisions, including triple ones, and at
infinity. The corpus does not state it. It is the same regularity that Deligne's
Riemann–Hilbert correspondence needs, so P2 and the Riemann–Hilbert step now rest on one input
instead of two. Reeb invariance (b) is no longer assumed: it follows, because every form in the
span is dilation invariant.

## What is proved here (sorry-free, no new axiom)

* `nbody_of_components`: if every scalar component `φ ∘ Ω` (`φ` a linear functional) of an
  `A`-valued form lies in a class with the Arnold-span property, then `Ω` is an `n`-body form
  `nbodyForm M` with **constant** residues `M_ab ∈ A`. This holds for every `n`: the cited
  input is about scalar forms, and the vector-valued step is a basis expansion.
* `nbodyForm_congr_offDiag`, `nbodyForm_residue_unique`: the residues are determined by the
  form off the diagonal, so P3 can be imposed on them without ambiguity.
* `kz_of_regular_singular`: Arnold span on components plus P3 on the residues gives
  `Ω = kzForm ρ (β/2) (−α/β)` on `Conf_n`. This is P2 + P3 ⇒ KZ, with P2 replaced by the
  regularity input.
* `gauge_one_of_form_eq`: in the algebraic setting of `BridgeADeligneGauge`, if the two
  connection matrices are equal then `g = 1` is an algebraic gauge between them.

## Where Deligne full faithfulness is needed, and where it is not

On the route through P1–P3 the Lagrangian connection form **is** the KZ form
(`BridgeAStokes.nbodyForm_eq_kzForm`, and `kz_of_regular_singular` here), so the gauge to KZ is
the identity (`gauge_one_of_form_eq`). `DeligneFullyFaithful` is not used. It enters only on
route B (`BridgeADeligneGauge.gauge_of_conj_monodromy`), which assumes nothing about the form
and only that the monodromy is conjugate to KZ's.

On route B, a Lean proof of full faithfulness is not feasible with current Mathlib: it needs
moderate-growth estimates for flat sections near a normal-crossings divisor, the Riemann
extension theorem in several variables, and algebraicity of meromorphic functions on a
projective variety (GAGA). The statement to cite is Deligne, *Équations différentielles à
points singuliers réguliers*, LNM 163 (1970), Ch. II, Théorème 5.9: on a smooth complex
algebraic variety, `(E, ∇) ↦ E^∇` is an equivalence between algebraic vector bundles with
regular-singular integrable connection and local systems. Full faithfulness of that functor,
applied to `Hom(∇₁, ∇₂)`, is exactly `DeligneFullyFaithful`. Both connections must be
regular singular; for the Lagrangian one that is again the modelling input of §2.

No empirical number enters. `q`, `α`, `β` are free complex parameters.

-- Ref: [deligne1970] Deligne, Équations différentielles à points singuliers réguliers, LNM 163.
-- Ref: [deligne1971] Deligne, Théorie de Hodge II, Publ. Math. IHÉS 40 (1971), §3.2.
-- Ref: [arnold1969] Arnold, The cohomology ring of the colored braid group, Mat. Zametki 5.
-/

namespace QOU.Mass.BridgeAP2

open QOU.Mass.BridgeAStokes QOU.Mass.KZHolonomy

/-! ## Scalar Arnold forms and the cited span property -/

section Scalar

variable {n : ℕ}

/-- The scalar Arnold form with coefficients `c`, normalised as `nbodyForm`:
`u ↦ ½ Σ_{a,b} c_ab (u_a − u_b)/(z_a − z_b)`. -/
noncomputable def scalarArnold (c : Fin n → Fin n → ℂ) (z u : Fin n → ℂ) : ℂ :=
  ∑ a, ∑ b, c a b * ((2 : ℂ)⁻¹ * (z a - z b)⁻¹ * (u a - u b))

/-- **The cited input, as a property of a class of scalar forms.** Every form in `L` agrees on
`Conf_n` with a scalar Arnold form. For `L` = the global logarithmic 1-forms on
`P¹ × M̄_{0,n+1}`, pulled back to `Conf_n`, this is Deligne (Hodge II, §3.2) plus Arnold 1969.
It is a hypothesis here, never proved. -/
def ArnoldSpan (L : Set ((Fin n → ℂ) → (Fin n → ℂ) → ℂ)) : Prop :=
  ∀ φ ∈ L, ∃ c : Fin n → Fin n → ℂ, ∀ z, Function.Injective z → ∀ u, φ z u = scalarArnold c z u

/-- The Arnold forms themselves have the span property: the hypothesis is satisfiable. -/
theorem arnoldSpan_range :
    ArnoldSpan (Set.range (scalarArnold (n := n))) := by
  rintro _ ⟨c, rfl⟩
  exact ⟨c, fun _ _ _ => rfl⟩

end Scalar

/-! ## Vector-valued forms: constant residues from the scalar span -/

section Vector

variable {n : ℕ} {A : Type*} [NormedRing A] [NormedAlgebra ℂ A]

/-- **P2 from the scalar span, for every `n`.** If every scalar component of `Ω` lies in a
class with the Arnold-span property, then on `Conf_n` the form `Ω` is the `n`-body form with
constant residues `M_ab ∈ A`. -/
theorem nbody_of_components [FiniteDimensional ℂ A]
    {L : Set ((Fin n → ℂ) → (Fin n → ℂ) → ℂ)} (hL : ArnoldSpan L)
    (Ω : (Fin n → ℂ) → (Fin n → ℂ) → A)
    (hΩ : ∀ φ : Module.Dual ℂ A, (fun z u => φ (Ω z u)) ∈ L) :
    ∃ M : Fin n → Fin n → A, ∀ z, Function.Injective z → ∀ u, Ω z u = nbodyForm M z u := by
  classical
  let e := Module.finBasis ℂ A
  have hc : ∀ i, ∃ c : Fin n → Fin n → ℂ, ∀ z, Function.Injective z → ∀ u,
      e.coord i (Ω z u) = scalarArnold c z u := fun i => hL _ (hΩ (e.coord i))
  choose c hc using hc
  refine ⟨fun a b => ∑ i, c i a b • e i, fun z hz u => ?_⟩
  rw [nbodyForm_apply]
  conv_lhs => rw [← e.sum_repr (Ω z u)]
  have hcoord : ∀ i, e.repr (Ω z u) i = scalarArnold (c i) z u := fun i => by
    rw [← hc i z hz u]; rfl
  simp only [hcoord, scalarArnold, Finset.sum_smul, Finset.smul_sum, smul_smul]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun b _ => Finset.sum_congr rfl fun i _ => ?_
  rw [mul_comm]

/-- The diagonal residues of an `n`-body form do not matter: `(z_a − z_a)⁻¹ = 0`. -/
theorem nbodyForm_congr_offDiag {M N : Fin n → Fin n → A} (h : ∀ a b, a ≠ b → M a b = N a b)
    (z u : Fin n → ℂ) : nbodyForm M z u = nbodyForm N z u := by
  rw [nbodyForm_apply, nbodyForm_apply]
  refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ => ?_
  by_cases hab : a = b
  · subst hab; simp
  · rw [h a b hab]

/-- **The residues of an `n`-body form are determined by the form on `Conf_n`** (symmetric
residues). So "the residues of `Ω`" is well defined, and P3 can be imposed on them. -/
theorem nbodyForm_residue_unique {M N : Fin n → Fin n → A} (hM : ∀ a b, M a b = M b a)
    (hN : ∀ a b, N a b = N b a)
    (h : ∀ z : Fin n → ℂ, Function.Injective z → ∀ u, nbodyForm M z u = nbodyForm N z u) :
    ∀ a b, a ≠ b → M a b = N a b := by
  refine QOU.Mass.LagrangianKZ.arnoldCoeff_injective (K := ℂ) fun z hz m => ?_
  rw [← QOU.Mass.LagrangianKZ.arnoldForm_single, ← QOU.Mass.LagrangianKZ.arnoldForm_single,
    ← nbodyForm_eq_arnoldForm hM, ← nbodyForm_eq_arnoldForm hN]
  exact h z hz _

/-- **P2 (from regularity) + P3 ⇒ KZ.** If every scalar component of `Ω` is in an
Arnold-span class (the cited regularity input) and the off-diagonal residues are
`α + β·ρ(s_ab)` (P3), then `Ω` is the KZ form with `κ = β/2`, `c = −α/β` on `Conf_n`. -/
theorem kz_of_regular_singular [FiniteDimensional ℂ A] (ρ : Equiv.Perm (Fin n) →* A)
    {α β : ℂ} (hβ : β ≠ 0) {L : Set ((Fin n → ℂ) → (Fin n → ℂ) → ℂ)} (hL : ArnoldSpan L)
    (Ω : (Fin n → ℂ) → (Fin n → ℂ) → A)
    (hΩ : ∀ φ : Module.Dual ℂ A, (fun z u => φ (Ω z u)) ∈ L)
    (hP3 : ∀ M : Fin n → Fin n → A,
      (∀ z, Function.Injective z → ∀ u, Ω z u = nbodyForm M z u) →
        ∀ a b, a ≠ b → M a b = pairResid ρ α β a b) :
    ∀ z, Function.Injective z → ∀ u, Ω z u = kzForm ρ (β / 2) (-α / β) z u := by
  obtain ⟨M, hM⟩ := nbody_of_components hL Ω hΩ
  intro z hz u
  rw [hM z hz u, nbodyForm_congr_offDiag (hP3 M hM) z u, nbodyForm_eq_kzForm ρ hβ]

end Vector

/-! ## On the P1–P3 route the gauge to KZ is the identity: no Deligne -/

section Gauge

open QOU.Mass.BridgeADeligneGauge

variable {S : Type*} [CommRing S] {N : Type*} [Fintype N] [DecidableEq N] {ι : Type*}

/-- If the two connection matrices agree, `g = 1` is an algebraic gauge between them, over any
`R`. This is what P1–P3 give for the Lagrangian connection and KZ; `DeligneFullyFaithful` is
not needed on that route. -/
theorem gauge_one_of_form_eq (D : ι → Derivation ℤ S S) (R : Type*) [CommRing R] [Algebra R S]
    {ωKZ ωL : ι → Matrix N N S} (h : ωL = ωKZ) :
    ∃ g gInv : Matrix N N R, g * gInv = 1 ∧ gInv * g = 1 ∧
      ∀ j, (g.map (algebraMap R S)).map (D j)
        = ωL j * g.map (algebraMap R S) - g.map (algebraMap R S) * ωKZ j := by
  refine ⟨1, 1, Matrix.mul_one 1, Matrix.mul_one 1, fun j => ?_⟩
  rw [Matrix.map_one _ (map_zero _) (map_one _), map_one_der, Matrix.mul_one, Matrix.one_mul, h,
    sub_self]

end Gauge

end QOU.Mass.BridgeAP2
