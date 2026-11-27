import Mathlib.RingTheory.PowerSeries.WellKnown
import Mathlib.Tactic.Module
import Mathlib.Tactic.NoncommRing

/-!
# The two-strand h-adic KZ R-matrix satisfies the Hecke quadratic, with no analysis

Bean `qou-5ufw` (constructive item 1.2), owner ruling 2026-11-27: the KZ route moves from
the analytic multiplicative integral to the formal `h`-adic connection. This file does the
two-strand case, which is the algebraic twin of `QOU.Mass.KZTwoStrandHecke` (that file
transports the KZ equation in a complete normed `ℂ`-algebra; this one uses no norm, no
limit and no `ℂ`).

* `heckeQuad_of_involution`: for an involution `s` in any algebra `B` over any commutative
  ring `S`, and scalars `c, d` with `c + d = q`, `c − d = q'`, the element
  `σ = d + c s` satisfies `(σ − q)(σ + q') = 0`. Nothing about `c, d` is assumed beyond
  those two equations.
* `qh = e^{h/2}` and `qhInv = e^{−h/2}` are formal power series over a characteristic-zero
  field `A`, and `qh_mul_qhInv` proves `qh · qhInv = 1` in `A⟦h⟧` from Mathlib's
  `exp_mul_exp_neg_eq_one`.
* `heckeQuad_hAdic`: with `c = cosh(h/2)`, `d = sinh(h/2)` (as formal series), the element
  `σ = sinh(h/2) + cosh(h/2) s = s·e^{h s/2}` satisfies `(σ − q)(σ + q⁻¹) = 0` over
  `A⟦h⟧`, with `q = e^{h/2}`. This is the Hecke relation of `H₂(q)` at `q = e^{h/2}`, the
  two-strand case of `R = e^{hΩ/2}` composed with the flip.

**Scope.** Two strands. For `n ≥ 3` the braid action needs a rational Drinfeld associator
`Φ ∈ ℚ⟨⟨t₁₂, t₂₃⟩⟩`; that is the next step of `qou-5ufw` and is not done here.

No numerical value of `q` or `h` appears.
-/

namespace QOU.HeckeTemperleyLieb.HAdicTwoStrandHecke

open PowerSeries

section Generic

variable {S B : Type*} [CommRing S] [Ring B] [Algebra S B]

/-- The two-strand operator `σ = d + c s`. -/
def sigmaH (c d : S) (s : B) : B := d • (1 : B) + c • s

/-- **Hecke quadratic from an involution, over any commutative ring.** -/
theorem heckeQuad_of_involution {s : B} (hs : s * s = 1) {c d q q' : S}
    (hq : c + d = q) (hq' : c - d = q') :
    (sigmaH c d s - q • (1 : B)) * (sigmaH c d s + q' • (1 : B)) = 0 := by
  subst hq hq'
  have h1 : sigmaH c d s - (c + d) • (1 : B) = c • (s - 1) := by
    unfold sigmaH; module
  have h2 : sigmaH c d s + (c - d) • (1 : B) = c • (s + 1) := by
    unfold sigmaH; module
  rw [h1, h2, smul_mul_smul_comm, show (s - 1) * (s + 1) = s * s - 1 by noncomm_ring, hs,
    sub_self, smul_zero]

end Generic

section HAdic

variable (A : Type*) [Field A] [CharZero A]

/-- `q = e^{h/2}` as a formal power series in `h`. -/
noncomputable def qh : PowerSeries A := rescale (2⁻¹ : A) (exp A)

/-- `q⁻¹ = e^{−h/2}` as a formal power series in `h`. -/
noncomputable def qhInv : PowerSeries A := rescale (2⁻¹ : A) (evalNegHom (exp A))

/-- `e^{h/2} · e^{−h/2} = 1` in `A⟦h⟧`. -/
theorem qh_mul_qhInv : qh A * qhInv A = 1 := by
  unfold qh qhInv
  rw [← map_mul, exp_mul_exp_neg_eq_one, map_one]

/-- `cosh(h/2)`. -/
noncomputable def coshH : PowerSeries A := (2⁻¹ : A) • (qh A + qhInv A)

/-- `sinh(h/2)`. -/
noncomputable def sinhH : PowerSeries A := (2⁻¹ : A) • (qh A - qhInv A)

theorem coshH_add_sinhH : coshH A + sinhH A = qh A := by
  unfold coshH sinhH; module

theorem coshH_sub_sinhH : coshH A - sinhH A = qhInv A := by
  unfold coshH sinhH; module

/-- **The two-strand h-adic Hecke relation.** For an involution `s` in an `A⟦h⟧`-algebra,
`σ = sinh(h/2) + cosh(h/2) s` satisfies `(σ − q)(σ + q⁻¹) = 0` with `q = e^{h/2}` and
`q · q⁻¹ = 1` (`qh_mul_qhInv`). -/
theorem heckeQuad_hAdic {B : Type*} [Ring B] [Algebra (PowerSeries A) B] {s : B}
    (hs : s * s = 1) :
    (sigmaH (coshH A) (sinhH A) s - qh A • (1 : B)) *
      (sigmaH (coshH A) (sinhH A) s + qhInv A • (1 : B)) = 0 :=
  heckeQuad_of_involution hs (coshH_add_sinhH A) (coshH_sub_sinhH A)

end HAdic

end QOU.HeckeTemperleyLieb.HAdicTwoStrandHecke
