import QOU.Machinery.HeckeH2Wedderburn
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
# QOU.Machinery.HeckeH2WedderburnReal — H₂(q) over ℝ is semisimple, unconditionally

Archimedean instantiation of `HeckeH2Wedderburn` (§7c split: this file
owns the `Real.sqrt` construction).  The Hecke quadratic
$x^2 = h\,x + 1$ has discriminant $h^2 + 4 > 0$ for **every** real
$h$, so the two roots $(h \pm \sqrt{h^2+4})/2$ (i.e. $q$ and
$-q^{-1}$) are always real and distinct:

* `wedderburnReal` — the explicit decomposition
  $H_2(q) \cong \mathbb{R} \times \mathbb{R}$ for every real $h$;
* `isSemisimpleRing_H2A_real` — **H₂(q) over ℝ is a semisimple ring
  for every $h$**, sorry-free.

This is the rank-2 slice of Wenzl semisimplicity [wenzl1988] with an
actual proof — the first inhabited rung behind the cited hypothesis
classes (`WenzlCriterion`, `SchurElementCriterion`), and *stronger*
than the genericity-conditional statement at this rank: the real
substrate line never meets the rank-2 degeneracy locus at all (the
first degeneration $[2]_q = 0$ requires complex $q$, a root of
unity).  Higher ranks ($n \geq 3$, where hook lengths $\geq 2$ bring
genuine root-of-unity loci) remain the open stage-2 frontier (bean
`qou-vndn`).

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457
-/

namespace QOU.Machinery.H3
namespace H2A

/-- The larger root $(h + \sqrt{h^2+4})/2$ of the Hecke quadratic
    (this is $q$ when $h = q - q^{-1}$, $q > 1$). -/
noncomputable def realRootPlus (h : ℝ) : ℝ := (h + Real.sqrt (h ^ 2 + 4)) / 2

/-- The smaller root $(h - \sqrt{h^2+4})/2$ (this is $-q^{-1}$). -/
noncomputable def realRootMinus (h : ℝ) : ℝ := (h - Real.sqrt (h ^ 2 + 4)) / 2

lemma sq_sqrt_disc (h : ℝ) : Real.sqrt (h ^ 2 + 4) ^ 2 = h ^ 2 + 4 :=
  Real.sq_sqrt (by positivity)

lemma sqrt_disc_pos (h : ℝ) : 0 < Real.sqrt (h ^ 2 + 4) :=
  Real.sqrt_pos.mpr (by positivity)

lemma realRootPlus_root (h : ℝ) :
    realRootPlus h * realRootPlus h = h * realRootPlus h + 1 := by
  unfold realRootPlus
  linear_combination sq_sqrt_disc h / 4

lemma realRootMinus_root (h : ℝ) :
    realRootMinus h * realRootMinus h = h * realRootMinus h + 1 := by
  unfold realRootMinus
  linear_combination sq_sqrt_disc h / 4

lemma realRoots_ne (h : ℝ) : realRootPlus h ≠ realRootMinus h := by
  unfold realRootPlus realRootMinus
  intro heq
  have hpos := sqrt_disc_pos h
  have : Real.sqrt (h ^ 2 + 4) = 0 := by linarith
  linarith

/-- **The unconditional real Wedderburn decomposition (sorry-free):**
    $H_2(q) \cong \mathbb{R} \times \mathbb{R}$ for every real $h$. -/
noncomputable def wedderburnReal (h : ℝ) : H2A ℝ h ≃ₐ[ℝ] ℝ × ℝ :=
  wedderburn (realRootPlus h) (realRootMinus h)
    (realRootPlus_root h) (realRootMinus_root h)
    (realRootPlus h - realRootMinus h)⁻¹
    (inv_mul_cancel₀ (sub_ne_zero.mpr (realRoots_ne h)))

/-- **H₂(q) over ℝ is semisimple for every $h$ (sorry-free).**  The
    rank-2 slice of Wenzl semisimplicity, proved rather than cited. -/
theorem isSemisimpleRing_H2A_real (h : ℝ) : IsSemisimpleRing (H2A ℝ h) :=
  isSemisimpleRing_of_roots _ _
    (realRootPlus_root h) (realRootMinus_root h) (realRoots_ne h)

end H2A
end QOU.Machinery.H3
