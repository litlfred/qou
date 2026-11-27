import Mathlib.Data.Finset.Basic
import QOU.StandardModel.Photon
import BraidKnotOctonion.PieriSupport


/-!
# QOU.Photon.Pieri — Pieri rule shift for degree-one Hecke elements

The photon is `def:photon`, `QOU.Photon.photon`:
`γ(φ) = 𝟙 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹` (owner ruling, bean `qou-99qc`,
2026-11-18, confirmed 2026-11-20; the fourth term is the chiral vertex).
Multiplied against a state `β_m` supported on the partition `λ`, its support
is contained in `{λ}` (same level) or in the partitions containing `λ` with one
box more (next level). No box is ever removed. The
degree-one element `1 + Σ_i φ_i σ_i` of the earlier statement is the named
specialisation `φ₀₁ = 0` on one strand pair (photon-usage audit 2026-11-17, C10).

Step 1 of the narrative proof, for the four-term photon, is
`commute_photon_of_commute` below: anything commuting with `σ₀` and `σ₁`
(e.g. a central idempotent `e_λ`) commutes with the whole photon, including
its vertex term `σ₀σ₁⁻¹`. The `λ ± □` part (a photon reaching one further
strand) is `pieri_one_box_shift`, proved for every `m` and every partition
from the seminormal branching in `QOU.SchurWeyl.PieriSupport` (no `sorry`).

LaTeX label: `prop:pieri-photon-shift`

## References

- [fulton1997] Young Tableaux (Cambridge University Press, 1997),
  Chapter 2.
- [kassel1995] Quantum Groups (Springer GTM 155, 1995), Chapter XI.
- [leitner2026] braids-and-knots / pieri-photon-shift
-/

namespace QOU.Photon

/-- **The Pieri rule, general form.** Let `y ∈ H_m(q)` be supported on the
    `λ`-block (its seminormal representation vanishes on every other partition of
    `m`). For every `a ∈ H_{m+1}(q)` and every `μ ⊢ m + 1` that is not `λ` with one
    box added, the seminormal representation of `a · y` at `μ` vanishes. So the
    support of `a · y` lies in `{μ ⊃ λ, |μ| = |λ| + 1}`, the three-row shape
    included. This is case 2 of the content block before the restriction to
    `V_□^{⊗(n+1)}`; it holds for every `m` and every `λ`.

    Proved in `QOU/SchurWeyl/PieriSupport.lean` from the seminormal branching
    `compress_seminormalRep_heckeIncl`. It replaces the earlier statement over an
    abstract `PieriInterface`, whose sets were not tied to Young's lattice and so
    could not be proved (QA on #8888, 2026-11-21). Real field, `q ≠ 0` and not a
    root of unity: the seminormal machinery is stated over `ℝ` (§7c, archimedean
    side of the wall). -/
-- Ref: [fulton1997] Young Tableaux, Ch. 2
theorem pieri_one_box_shift {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : QOU.SchurWeyl.GenericParameter.NotRootOfUnity q)
    (m : ℕ) (lam : YoungDiagram) (y : QOU.SchurWeyl.Hecke ℝ q q⁻¹ m)
    (hy : QOU.SchurWeyl.SeminormalRep.SupportedOn hq0 hq2 m lam y)
    (a : QOU.SchurWeyl.Hecke ℝ q q⁻¹ (m + 1))
    (μ : YoungDiagram) (hN : μ.cells.card = m + 2)
    (hμ : ∀ (c : ℕ × ℕ) (hc : QOU.Mathlib.IsCornerCell μ c),
      QOU.Mathlib.eraseCorner μ c hc ≠ lam) :
    QOU.SchurWeyl.SeminormalRep.seminormalRep q hq0 hq2 (m + 1) hN
      (a * QOU.SchurWeyl.HeckeInclusion.heckeIncl ℝ q q⁻¹ m y) = 0 :=
  QOU.SchurWeyl.SeminormalRep.pieri_support hq0 hq2 m lam y hy a μ hN hμ

/-- **Step 1 for the four-term photon.** If `e` commutes with `σ₀` and with the
    unit `σ₁`, it commutes with every photon `γ(φ)`, the vertex term `σ₀σ₁⁻¹`
    included. With `e = e_λ` central this is the level-`n` containment
    `γ · (e_λ β) = e_λ (γ · β)`. Generic ring, no ordering (§7c). -/
-- Ref: [leitner2026] prop:pieri-photon-shift; def:photon
theorem commute_photon_of_commute {R A : Type*} [CommRing R] [Ring A] [Algebra R A]
    {e σ₀ : A} {σ₁ : Aˣ} (h0 : Commute e σ₀) (h1 : Commute e (σ₁ : A)) (c : Colour R) :
    Commute e (photon σ₀ σ₁ c) := by
  have hinv : Commute e (↑σ₁⁻¹ : A) := h1.units_inv_right
  have hv : Commute e (vertex σ₀ σ₁) := h0.mul_right hinv
  have hs : ∀ (r : R) {x : A}, Commute e x → Commute e (r • x) := fun r x hx => by
    rw [Algebra.smul_def]
    exact (Algebra.commute_algebraMap_right r e).mul_right hx
  unfold photon
  exact (((Commute.one_right e).add_right (hs _ h0)).add_right (hs _ h1)).add_right (hs _ hv)

end QOU.Photon
