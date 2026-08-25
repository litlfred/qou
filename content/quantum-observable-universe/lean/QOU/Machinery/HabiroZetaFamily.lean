/-
# ζ-indexed families, archimedean layer — the structure the bracket inhabits

Completes the Lean half of bean qou-zt3h (T4 of the Habiro attack
plan). The GSWZ picture (arXiv:2412.04241, `library/arxiv-2412.04241v2/2412.04241v2.pdf`)
organizes a Habiro-module element as a family of fibres over the roots
of unity with arithmetic transition edges. The ARCHIMEDEAN layer of
that picture — the only layer visible to `ℂ`-analysis — carries exactly
one Galois edge, complex conjugation, and this file packages it:

* **`ZetaFamily`** — a global function on `ℂ` together with the
  conjugation-equivariance law. The single field is content-bearing
  (an equivariance equation, not a marker), and the structure is
  INHABITED by the categorical bracket (`bracketZetaFamily`), so the
  §3b-tax vacuity disciplines are satisfied by construction.
* **`ZetaFamily.bar_edge`** — the derived theorem: on the unit circle
  conjugation IS the bar involution `q ↦ q⁻¹`, so every `ZetaFamily`
  automatically satisfies the bar edge `F(z⁻¹) = conj (F z)` at EVERY
  unit-circle fibre — the family-level form of the ζ₄ bar edge that
  `rho_compat` realizes for the τ-assignment.
* **`ZetaFamily.conj_fixed_of_bar_fixed`** — bar-even values at
  unit-circle fibres are conjugation-fixed (real): the abstract form
  of the fibre-reality check exercised on the binding-tail data in
  `habiro_tail_membership_gate_probe.py`.
* **`bracketZetaFamily`** — the inhabitant: fibre values `0` at ζ₄
  (the monodromy-point modular zero) and `√2` at ζ₈ (the Q_β witness
  point), imported from the merged bracket-family facts.

Honest scope: the p-adic Frobenius edges (the genuinely arithmetic
transitions of GSWZ Def 1.1) are NOT representable in this archimedean
layer — they are implemented and verified compute-side
(`gswz_frobenius_teichmuller_probe.py`, `gswz_padic_dilog_modp_probe.py`).
This structure names what ℂ can see: one Galois edge and the fibre
values. The number-field family with Frobenius gluing remains open on
bean qou-9p9y.

HONESTY (STRICT): sorry-free, no axioms, no `decide`; the structure is
inhabited (no empty-carrier flag); nothing wired; `1/(8π)` stays
phase-4.

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Machinery.HabiroBracketFamily

namespace QOU.Machinery.CoxeterParabolic

open Complex

/-- A ζ-indexed family, archimedean layer: a global function on `ℂ`
carrying the conjugation-Galois equivariance law — the one Galois edge
visible to `ℂ`-analysis. -/
structure ZetaFamily where
  toFun : ℂ → ℂ
  conj_equivariant :
    ∀ z : ℂ, toFun ((starRingEnd ℂ) z) = (starRingEnd ℂ) (toFun z)

/-- **The bar edge at every unit-circle fibre**: on `|z| = 1`
conjugation is the bar involution `q ↦ q⁻¹`, so conjugation
equivariance forces `F(z⁻¹) = conj (F z)` — the family-level form of
the ζ₄ bar edge realized by `rho_compat` for the τ-assignment. -/
theorem ZetaFamily.bar_edge (F : ZetaFamily) {z : ℂ}
    (hz : Complex.normSq z = 1) :
    F.toFun z⁻¹ = (starRingEnd ℂ) (F.toFun z) := by
  rw [← F.conj_equivariant z, Complex.inv_def, hz]
  norm_num

/-- Bar-fixed values at bar-fixed fibres are real: if the family value
at a unit-circle point equals its value at the inverse point, the value
is fixed by conjugation. Concrete form of the fibre-reality check used
on the binding-tail data. -/
theorem conj_fixed_of_bar_fixed (F : ZetaFamily) {z : ℂ}
    (hz : Complex.normSq z = 1) (hfix : F.toFun z⁻¹ = F.toFun z) :
    (starRingEnd ℂ) (F.toFun z) = F.toFun z := by
  rw [← F.bar_edge hz, hfix]

/-- **The inhabitant**: the categorical bracket as a ζ-family. -/
noncomputable def bracketZetaFamily : ZetaFamily where
  toFun := bracketFamily
  conj_equivariant := bracketFamily_conj

/-- The inhabitant's ζ₄ fibre is the monodromy-point modular zero. -/
theorem bracketZetaFamily_zeta4 : bracketZetaFamily.toFun I = 0 := by
  show bracketFamily I = 0
  unfold bracketFamily
  rw [Complex.inv_I]
  ring

/-- The inhabitant's ζ₈ fibre is `√2` — the Q_β witness point. -/
theorem bracketZetaFamily_zeta8 :
    bracketZetaFamily.toFun (Complex.exp (Real.pi / 4 * I))
      = Real.sqrt 2 :=
  bracketFamily_zeta8_eq_sqrt2

end QOU.Machinery.CoxeterParabolic
