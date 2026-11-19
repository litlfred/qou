import QOU.Mass.BridgeADeligneGauge
import QOU.Mass.KohnoAssembly

/-!
# Bridge A, route B, on the KZ connection (mass-pipeline gap 3)

`BridgeADeligneGauge.gauge_of_conj_monodromy` is abstract: any two connections with conjugate
monodromy are algebraically gauge equivalent, given Deligne full faithfulness. Here it is applied
to the case Bridge A needs:

* the deck group is the braid group `B_{m+1}` (unordered configurations of `m + 1` points);
* the fibre is `V^{⊗(m+1)}`, `V = ℂ²`, i.e. matrices indexed by `Fin (m + 1) → Fin 2`;
* connection 1 is KZ, whose fundamental solution has the KZ braid monodromy
  `σ_j ↦ e^{2πiκc} · kzBraidRep(σ_j)` (the scalar is the trace-part shift by `c`);
* connection 2 is any connection (the Lagrangian one) whose monodromy is the Jimbo braiding
  `σ_j ↦ Ř_{j,j+1}(q)`, `q = qC κ`.

The conjugating constant `U` is not assumed: it is `KohnoAssembly.kz_conj_jimbo_complex_σ`
(Drinfeld–Kohno for `𝔤𝔩_2` fundamental, every `m`, `q` not a root of unity), extended from the
generators to the whole braid group by `intertwine_of_closure`.

## Hypotheses that remain, stated exactly

1. `DeligneFullyFaithful`, both directions (the uniqueness half of Riemann–Hilbert).
2. The two fundamental solutions exist on the chosen ring `S` with the stated monodromies on the
   generators. For KZ this is the content of `KZHolonomy` (transport along the generator paths);
   packaging it as a global `FundamentalSolution` over a ring of multivalued functions is not
   done here.
3. `S` is a nontrivial `ℂ`-algebra on which `B_{m+1}` acts fixing `ℂ`, and the derivations
   kill `ℂ`.

No hypothesis is placed on the Lagrangian connection beyond its monodromy.
-/

namespace QOU.Mass.BridgeADeligneKZ

open QOU.Mass.BridgeADeligneGauge QOU.Mass.KohnoAssembly QOU.Mass.KZHolonomy
open QOU.IwahoriHecke.TensorEmbed QOU.MathlibExt.Braid QOU.SchurWeyl
open Complex

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

variable {m : ℕ} {S : Type*} [CommRing S] [Nontrivial S] [Algebra ℂ S]
  [MulSemiringAction (BraidGroup m) S] {ι : Type*} {D : ι → Derivation ℤ S S}

/-- The Artin generators generate the braid group. -/
theorem closure_range_σ : Subgroup.closure (Set.range (σ (n := m))) = ⊤ :=
  PresentedGroup.closure_range_of _

/-- **Bridge A, route B, for `𝔤𝔩_2` fundamental.** A connection on `V^{⊗(m+1)}` whose monodromy
is the Jimbo braiding is algebraically gauge equivalent to KZ (shifted by `c`), given Deligne full
faithfulness. The gauge `g` is an invertible matrix over the algebraic ring `R`, with
`∂_j g = ω_L j · g − g · ω_KZ j`. -/
theorem lagrangian_gauge_to_KZ (c κ : ℂ) (hκ : GenericParameter.NotRootOfUnity (qC κ))
    (hDK : ∀ j (z : ℂ), D j (algebraMap ℂ S z) = 0)
    (hΓK : ∀ (γ : BraidGroup m) (z : ℂ), γ • algebraMap ℂ S z = algebraMap ℂ S z)
    (R : Type*) [CommRing R] [Algebra R S] (hinj : Function.Injective (algebraMap R S))
    {ωKZ ωL : ι → Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) S}
    (FKZ : FundamentalSolution (Γ := BraidGroup m) (K := ℂ) D ωKZ)
    (FL : FundamentalSolution (Γ := BraidGroup m) (K := ℂ) D ωL)
    (hKZ : ∀ j : Fin m, FKZ.M (σ j) =
      Complex.exp (2 * κ * (Real.pi * I) * c) • ((kzBraidRep permRep κ c (σ j) :
        (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ) :
        Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ))
    (hL : ∀ j : Fin m, FL.M (σ j) = strandBraid (qC κ) (qC κ)⁻¹ j)
    (hFF₁ : DeligneFullyFaithful D R (BraidGroup m) ωKZ ωL)
    (hFF₂ : DeligneFullyFaithful D R (BraidGroup m) ωL ωKZ) :
    ∃ g gInv : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) R,
      g * gInv = 1 ∧ gInv * g = 1 ∧
      ∀ j, (g.map (algebraMap R S)).map (D j)
        = ωL j * g.map (algebraMap R S) - g.map (algebraMap R S) * ωKZ j := by
  obtain ⟨U, hU⟩ := kz_conj_jimbo_complex_σ (m := m) c κ hκ
  have hinjK : Function.Injective (algebraMap ℂ S) := (algebraMap ℂ S).injective
  have hC : ∀ γ, FL.M γ * (U : Matrix _ _ ℂ) = (U : Matrix _ _ ℂ) * FKZ.M γ :=
    intertwine_of_closure hΓK hinjK FKZ FL _ closure_range_σ (by
      rintro _ ⟨j, rfl⟩
      rw [hL j, hKZ j]
      exact (hU j).symm)
  exact gauge_of_conj_monodromy hDK hΓK R hinj FKZ FL (U : Matrix _ _ ℂ)
    ((U⁻¹ : (Matrix _ _ ℂ)ˣ) : Matrix _ _ ℂ) U.mul_inv U.inv_mul hC hFF₁ hFF₂

end QOU.Mass.BridgeADeligneKZ
