import QOU.Mass.KohnoWeighted
import QOU.Torsion.MassTraceMarkovClass

set_option autoImplicit false

/-!
# The mass identity on braid classes, Knizhnik–Zamolodchikov form

`QOU.Torsion.MassTraceMarkovClass.massClass` is the mass functional on braid classes (braids modulo
conjugation and positive or negative stabilisation). `QOU.Mass.KohnoWeighted.braidTrace_eq_kz`
writes the Markov trace of a braid as the site-weighted trace of the Hecke-factored
Knizhnik–Zamolodchikov holonomy representation. Combining the two, the mass of a braid class is the
framing-corrected site-weighted trace of the KZ holonomy of any of its representatives, at every
complex coupling `κ` with `q = e^{2πiκ}` not a root of unity.

`massClass_kz` is that statement; it adds no new trace identity.

## References

- Ref: [kohno1987] Monodromy representations of braid groups and Yang–Baxter equations.
-/

namespace QOU.Mass.KohnoWeightedClass

open QOU.IwahoriHecke.BraidGroup QOU.IwahoriHecke.JonesNormalisation QOU.IwahoriHecke.TensorEmbed
open QOU.Mass.KohnoWeighted QOU.Torsion.MassTraceMarkovClass QOU.IwahoriHecke.Balanced
open QOU.Mass.KohnoAssembly QOU.SchurWeyl QOU.Mass.KZHolonomy QOU.Mass.BraidHeckeFactor

/-- **The mass identity on braid classes, KZ form.** For a complex coupling `κ` with
`q = e^{2πiκ}` not a root of unity, the mass of the class of a braid `β` on `m+1` strands is the
framing-corrected site-weighted trace of the KZ holonomy representation `kzHeckeC` of `β`'s image
in the Hecke algebra. The left side depends only on the class, so the right side is the same for
every representative. -/
theorem massClass_kz (c κ : ℂ) (hκ : GenericParameter.NotRootOfUnity (qC κ))
    (w : Fin 2 → ℂ) (wi : ℂ) (hw : (1 + qC κ ^ 2) * wi = 1) (h0 : w 0 = 1)
    (h1 : w 1 = qC κ ^ 2) {m : ℕ} (β : BraidGroupN m) :
    massClass (qC κ) (qC κ)⁻¹ wi (mul_inv_cancel₀ (qC_ne_zero κ)) w hw h0 h1
        (QOU.MathlibExt.MarkovMoves.classOf artinTower ⟨m, β⟩)
      = ((strandFactor (qC κ) (qC κ)⁻¹ wi (mul_inv_cancel₀ (qC_ne_zero κ)) hw ^ (m + 1) : ℂˣ) : ℂ)
        * ((writheFactor (qC κ) (qC κ)⁻¹ (mul_inv_cancel₀ (qC_ne_zero κ))
            ^ braidWritheZ β : ℂˣ) : ℂ)
        * (wi ^ (m + 1) * (QOU.IwahoriHecke.QuantumTrace.siteWeight w *
            kzHeckeC m c κ ((JimboActionKernel.skeinCoxAEquiv (qC κ)
              (qC_ne_zero κ) m).symm
              ((heckeRep (coxA m) (mul_inv_cancel₀ (qC_ne_zero κ))
                coxA_symm β : (BalancedHecke (coxA m) (qC κ))ˣ) :
                BalancedHecke (coxA m) (qC κ)))).trace) := by
  rw [massClass_classOf, jonesFn, braidTrace_eq_kz c κ hκ w wi β]

/-- **Vanishing difference form of `massClass_kz` (`qou-37kk`).**
Under the hypotheses of `massClass_kz`, the difference between the left-hand and right-hand
sides of `massClass_kz` is zero. -/
theorem massClass_kz_sub_eq_zero (c κ : ℂ) (hκ : GenericParameter.NotRootOfUnity (qC κ))
    (w : Fin 2 → ℂ) (wi : ℂ) (hw : (1 + qC κ ^ 2) * wi = 1) (h0 : w 0 = 1)
    (h1 : w 1 = qC κ ^ 2) {m : ℕ} (β : BraidGroupN m) :
    massClass (qC κ) (qC κ)⁻¹ wi (mul_inv_cancel₀ (qC_ne_zero κ)) w hw h0 h1
        (QOU.MathlibExt.MarkovMoves.classOf artinTower ⟨m, β⟩)
      - ((strandFactor (qC κ) (qC κ)⁻¹ wi (mul_inv_cancel₀ (qC_ne_zero κ)) hw ^ (m + 1) : ℂˣ) : ℂ)
        * ((writheFactor (qC κ) (qC κ)⁻¹ (mul_inv_cancel₀ (qC_ne_zero κ))
            ^ braidWritheZ β : ℂˣ) : ℂ)
        * (wi ^ (m + 1) * (QOU.IwahoriHecke.QuantumTrace.siteWeight w *
            kzHeckeC m c κ ((JimboActionKernel.skeinCoxAEquiv (qC κ)
              (qC_ne_zero κ) m).symm
              ((heckeRep (coxA m) (mul_inv_cancel₀ (qC_ne_zero κ))
                coxA_symm β : (BalancedHecke (coxA m) (qC κ))ˣ) :
                BalancedHecke (coxA m) (qC κ)))).trace) = 0 :=
  sub_eq_zero.mpr (massClass_kz c κ hκ w wi hw h0 h1 β)

end QOU.Mass.KohnoWeightedClass
