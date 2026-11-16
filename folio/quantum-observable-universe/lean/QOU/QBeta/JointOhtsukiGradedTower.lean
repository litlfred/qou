/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Team

# Joint Graded Ohtsuki Tower over $(4_1, 5_2, \mathbb{B}_3)$ and Negative-Grade Annihilator Obstruction

Task: `qou-7jok` (under epic `qou-10v9` / `qou-avtq`, owner ruling `Q-10V9-4 = 1`).
Probe companion: `computations/qbeta/joint_ohtsuki_graded_tower_annihilator_probe.py`.
Witness companion: `computations/qbeta/joint-ohtsuki-graded-tower-annihilator.witness.json`.

## Mathematical Summary

For each hyperbolic knot/link complement $K \in \{4_1, 5_2, \mathbb{B}_3\}$, the finite-$b$
asymptotic complex-volume tower at the substrate parameter $2\pi b^2 = i t$ ($t = \ln q_0 \in \mathbb{R}$)
has the graded expansion
$$\mathfrak{V}_b(K) \;=\; \mathfrak{V}_0(K) \;+\; \sum_{n \ge 1} \kappa_n(K)\,(i t)^n,
  \qquad \mathfrak{V}_0(K) = \mathrm{Vol}_0(K) + i\,\mathrm{CS}_0(K).$$

This module formalizes the joint graded tower over $(4_1, 5_2, \mathbb{B}_3)$ and proves the two
structural blockers that exclude any non-trivial parameter-free negative-grade / low-grade
annihilator $(\alpha_{4_1}, \alpha_{5_2}, \alpha_{\mathbb{B}_3}) \neq (0, 0, 0)$:

1. **Grade-$0$ Complex-Volume Chirality Blocker (`complexVolume0_im_eq_zero_iff`,
   `jointGrade0Im_amphicheiral_pair`, `chiral_grade0_parity_blocker`):**
   While all positive Ohtsuki rungs $n \ge 1$ split cleanly by parity (`even_rung_im_zero` and
   `odd_rung_re_zero`, via `OhtsukiTowerBarParity`), the grade-$0$ base $\mathfrak{V}_0(K) = \mathrm{Vol}_0(K) + i\,\mathrm{CS}_0(K)$
   has $\mathrm{Im}\,\mathfrak{V}_0(K) = \mathrm{CS}_0(K)$. For the amphicheiral complements
   $4_1$ and $\mathbb{B}_3$, $\mathrm{CS}_0(4_1) = \mathrm{CS}_0(\mathbb{B}_3) = 0$; for the chiral
   knot $5_2$, $\mathrm{CS}_0(5_2) \neq 0$. Consequently, requiring the joint grade-$0$ imaginary
   part $\mathrm{Im}\sum_K \alpha_K \mathfrak{V}_0(K)$ to vanish (so that the bar-odd channel
   starts at grade $1$) forces $\alpha_{5_2} = 0$.

2. **Arithmetic Field Disjointness & Full-Rank Annihilator Obstruction
   (`fiveTwo_cubic_mod2_no_root`, `trace_field_discriminants_pairwise_distinct`,
   `amphicheiral_two_rung_annihilator_trivial`, `joint_three_complement_annihilator_trivial`,
   `single_rung_q_linear_indep_annihilator_trivial`):**
   - The three complements have invariant trace/shape fields of discriminants $-3$ ($\mathbb{Q}(\sqrt{-3})$
     for $4_1$), $-23$ (the non-arithmetic cubic field $K_{5_2} = \mathbb{Q}(y_0)/(y_0^3 - 2y_0^2 + 3y_0 - 1)$
     for $5_2$, whose defining cubic has no root in $\mathbb{F}_2$), and $-4$ ($\mathbb{Q}(i)$ for
     $\mathbb{B}_3$).
   - Over $\mathbb{R}$, combining the grade-$0$ chirality blocker ($\mathrm{CS}_0(5_2) \neq 0$)
     with a non-singular $2 \times 2$ grade matrix on the remaining amphicheiral pair $(4_1, \mathbb{B}_3)$
     forces $\alpha_{4_1} = \alpha_{5_2} = \alpha_{\mathbb{B}_3} = 0$.
   - Over $\mathbb{Q}$, $\mathbb{Q}$-linear independence of the algebraic prefactors $(1, \omega_{4_1}, \omega_{5_2})$
     forces $\alpha_{4_1} = \alpha_{5_2} = \alpha_{\mathbb{B}_3} = 0$ even at a single odd rung.

-- Ref: [ohtsuki-2016] Ohtsuki, Quantum Topol. 7 (2016), 669-735
-- Ref: [neumann-zagier-1985] Neumann & Zagier, Topology 24 (1985), 307-332
-- Ref: [manuscript] computations/qbeta/joint_ohtsuki_graded_tower_annihilator_probe.py
-/
import QOU.QBeta.OhtsukiTowerBarParity

namespace QOU.QBeta.JointOhtsukiGradedTower

open QOU.QBeta.OhtsukiTowerBarParity

/-! ## 1. Graded Complex-Volume Tower Datum and Rung Parity -/

/-- Graded asymptotic complex-volume tower datum for a hyperbolic knot/link complement $K$:
grade-$0$ hyperbolic volume `vol0` ($\mathrm{Vol}_0(K)$), grade-$0$ Chern–Simons invariant
`cs0` ($\mathrm{CS}_0(K)$), and higher Ohtsuki cumulant rungs `kappa n` ($\kappa_n(K)$ for $n \ge 1$). -/
structure GradedComplexVolumeTower where
  /-- Grade-$0$ real hyperbolic volume $\mathrm{Vol}_0(K)$. -/
  vol0 : ℝ
  /-- Grade-$0$ imaginary Chern–Simons invariant $\mathrm{CS}_0(K)$. -/
  cs0 : ℝ
  /-- Higher Ohtsuki / state-integral cumulant rungs $\kappa_n(K)$. -/
  kappa : ℕ → ℝ

/-- Grade-$0$ complex volume $\mathfrak{V}_0(K) = \mathrm{Vol}_0(K) + i\,\mathrm{CS}_0(K) \in \mathbb{C}$. -/
noncomputable def GradedComplexVolumeTower.complexVolume0 (T : GradedComplexVolumeTower) : ℂ :=
  (T.vol0 : ℂ) + Complex.I * (T.cs0 : ℂ)

/-- The $n$-th graded Ohtsuki rung $(i t)^n \cdot \kappa_n(K) \in \mathbb{C}$ evaluated at the imaginary
substrate parameter $2\pi b^2 = i t$ ($t = \ln q_0 \in \mathbb{R}$). -/
noncomputable def GradedComplexVolumeTower.rungAt (T : GradedComplexVolumeTower) (t : ℝ) (n : ℕ) : ℂ :=
  (Complex.I * (t : ℂ)) ^ n * (T.kappa n : ℂ)

/-- The real part of the grade-$0$ complex volume $\mathfrak{V}_0(K)$ is $\mathrm{Vol}_0(K)$. -/
theorem complexVolume0_re (T : GradedComplexVolumeTower) :
    (T.complexVolume0).re = T.vol0 := by
  simp [GradedComplexVolumeTower.complexVolume0]

/-- The imaginary part of the grade-$0$ complex volume $\mathfrak{V}_0(K)$ is $\mathrm{CS}_0(K)$. -/
theorem complexVolume0_im (T : GradedComplexVolumeTower) :
    (T.complexVolume0).im = T.cs0 := by
  simp [GradedComplexVolumeTower.complexVolume0]

/-- The grade-$0$ complex volume $\mathfrak{V}_0(K)$ is purely real iff $\mathrm{CS}_0(K) = 0$
(satisfied by amphicheiral complements $4_1, \mathbb{B}_3$ and violated by chiral $5_2$). -/
theorem complexVolume0_im_eq_zero_iff (T : GradedComplexVolumeTower) :
    (T.complexVolume0).im = 0 ↔ T.cs0 = 0 := by
  rw [complexVolume0_im]

/-- Every even Ohtsuki rung $n = 2m$ is purely real at $2\pi b^2 = i t$
(`(T.rungAt t (2 * m)).im = 0`), feeding only the bar-even $\mathrm{Re}\,\mathfrak{V}_b$ channel. -/
theorem even_rung_im_zero (T : GradedComplexVolumeTower) (t : ℝ) (m : ℕ) :
    (T.rungAt t (2 * m)).im = 0 :=
  even_rung_real t (T.kappa (2 * m)) m

/-- Every odd Ohtsuki rung $n = 2m + 1$ is purely imaginary at $2\pi b^2 = i t$
(`(T.rungAt t (2 * m + 1)).re = 0`), feeding only the bar-odd $\mathrm{Im}\,\mathfrak{V}_b$ channel. -/
theorem odd_rung_re_zero (T : GradedComplexVolumeTower) (t : ℝ) (m : ℕ) :
    (T.rungAt t (2 * m + 1)).re = 0 :=
  odd_rung_imaginary t (T.kappa (2 * m + 1)) m

/-- Explicit imaginary part of the grade-$1$ rung $(i t)^1 \cdot \kappa_1(K)$:
$\mathrm{Im}(\mathrm{rungAt}\,T\,t\,1) = T.\kappa(1) \cdot t$. -/
theorem rungAt_one_im (T : GradedComplexVolumeTower) (t : ℝ) :
    (T.rungAt t 1).im = T.kappa 1 * t := by
  unfold GradedComplexVolumeTower.rungAt
  simp [mul_comm]

/-- Explicit real part of the grade-$2$ rung $(i t)^2 \cdot \kappa_2(K)$:
$\mathrm{Re}(\mathrm{rungAt}\,T\,t\,2) = -T.\kappa(2) \cdot t^2$. -/
theorem rungAt_two_re (T : GradedComplexVolumeTower) (t : ℝ) :
    (T.rungAt t 2).re = -T.kappa 2 * t ^ 2 := by
  unfold GradedComplexVolumeTower.rungAt
  rw [imaginary_sub_sq, ← Complex.ofReal_mul, Complex.ofReal_re]
  ring

/-! ## 2. Blocker 1: Grade-$0$ Complex-Volume Chirality Mismatch -/

/-- Joint linear combination of a per-complement real invariant $f(K)$ across $(4_1, 5_2, \mathbb{B}_3)$
with weights $(\alpha_{4_1}, \alpha_{5_2}, \alpha_{\mathbb{B}_3})$. -/
def jointLinearComb (f41 f52 fB3 α41 α52 αB3 : ℝ) : ℝ :=
  α41 * f41 + α52 * f52 + αB3 * fB3

/-- Joint grade-$0$ imaginary part $\mathrm{Im}\sum_{K \in \{4_1, 5_2, \mathbb{B}_3\}} \alpha_K \mathfrak{V}_0(K)$. -/
def jointGrade0Im (T41 T52 TB3 : GradedComplexVolumeTower) (α41 α52 αB3 : ℝ) : ℝ :=
  jointLinearComb T41.cs0 T52.cs0 TB3.cs0 α41 α52 αB3

/-- Joint grade-$0$ real part $\mathrm{Re}\sum_{K \in \{4_1, 5_2, \mathbb{B}_3\}} \alpha_K \mathfrak{V}_0(K)$. -/
def jointGrade0Re (T41 T52 TB3 : GradedComplexVolumeTower) (α41 α52 αB3 : ℝ) : ℝ :=
  jointLinearComb T41.vol0 T52.vol0 TB3.vol0 α41 α52 αB3

/-- Joint grade-$n$ rung coefficient $\sum_{K \in \{4_1, 5_2, \mathbb{B}_3\}} \alpha_K \kappa_n(K)$. -/
def jointRungCoeff (T41 T52 TB3 : GradedComplexVolumeTower) (n : ℕ) (α41 α52 αB3 : ℝ) : ℝ :=
  jointLinearComb (T41.kappa n) (T52.kappa n) (TB3.kappa n) α41 α52 αB3

/-- When $4_1$ and $\mathbb{B}_3$ are amphicheiral ($\mathrm{CS}_0(4_1) = \mathrm{CS}_0(\mathbb{B}_3) = 0$),
the joint grade-$0$ imaginary part reduces to $\alpha_{5_2} \cdot \mathrm{CS}_0(5_2)$ alone. -/
theorem jointGrade0Im_amphicheiral_pair {T41 T52 TB3 : GradedComplexVolumeTower}
    (h41 : T41.cs0 = 0) (hB3 : TB3.cs0 = 0) (α41 α52 αB3 : ℝ) :
    jointGrade0Im T41 T52 TB3 α41 α52 αB3 = α52 * T52.cs0 := by
  unfold jointGrade0Im jointLinearComb
  rw [h41, hB3]
  ring

/-- **Blocker 1 — Chiral Grade-$0$ Parity Exclusion (`chiral_grade0_parity_blocker`):**
Because $4_1$ and $\mathbb{B}_3$ have $\mathrm{CS}_0 = 0$ (amphicheiral) while $5_2$ has
$\mathrm{CS}_0(5_2) \neq 0$ (chiral), the joint grade-$0$ imaginary part vanishes if and only if
$\alpha_{5_2} = 0$. Thus $5_2$ cannot participate in any real linear combination that preserves
zero grade-$0$ imaginary parity. -/
theorem chiral_grade0_parity_blocker {T41 T52 TB3 : GradedComplexVolumeTower}
    (h41 : T41.cs0 = 0) (hB3 : TB3.cs0 = 0) (h52 : T52.cs0 ≠ 0)
    (α41 α52 αB3 : ℝ) :
    jointGrade0Im T41 T52 TB3 α41 α52 αB3 = 0 ↔ α52 = 0 := by
  rw [jointGrade0Im_amphicheiral_pair h41 hB3]
  exact mul_eq_zero_iff_right h52

/-! ## 3. Blocker 2: Arithmetic Field Disjointness and Full-Rank Annihilator Obstruction -/

/-- The invariant trace/shape field discriminants of $(4_1, 5_2, \mathbb{B}_3)$ are
$(-3, -23, -4)$ respectively. -/
def disc41 : ℤ := -3
def disc52 : ℤ := -23
def discB3 : ℤ := -4

/-- The three field discriminants $(-3, -23, -4)$ are pairwise distinct integers. -/
theorem trace_field_discriminants_pairwise_distinct :
    disc41 ≠ disc52 ∧ disc41 ≠ discB3 ∧ disc52 ≠ discB3 := by
  decide

/-- The $5_2$ saddle cubic $y^3 - 2y^2 + 3y - 1$ (from `FiveTwoOhtsukiCriticalPoint`) has no root
in $\mathbb{Z}/2\mathbb{Z}$, certifying that it has no rational root and is irreducible of degree $3$
over $\mathbb{Q}$. -/
theorem fiveTwo_cubic_mod2_no_root :
    ∀ y : ZMod 2, y ^ 3 - 2 * y ^ 2 + 3 * y - 1 ≠ 0 := by
  decide

/-- Homogenized mod-$2$ irreducibility certificate: for every $(a, b) \in (\mathbb{Z}/2\mathbb{Z})^2 \setminus \{(0, 0)\}$,
$a^3 - 2a^2 b + 3ab^2 - b^3 = 1 \neq 0$ in $\mathbb{Z}/2\mathbb{Z}$. -/
theorem fiveTwo_homog_cubic_mod2_ne_zero :
    ∀ a b : ZMod 2, (a ≠ 0 ∨ b ≠ 0) → a ^ 3 - 2 * a ^ 2 * b + 3 * a * b ^ 2 - b ^ 3 ≠ 0 := by
  decide

/-- The figure-eight $4_1$ rational Ohtsuki prefactors $\kappa_1 / (\sqrt{3}\pi) = 11/108$ and
$\kappa_2 / \pi^2 = 2/27$ and the Borromean $\mathbb{B}_3$ rational prefactors $r_1 = 1/4$ and
$r_2 = 5/12$ satisfy strict non-proportionality. -/
def k1Rat41 : ℚ := 11 / 108
def k2Rat41 : ℚ := 2 / 27
def k1RatB3 : ℚ := 1 / 4
def k2RatB3 : ℚ := 5 / 12

/-- Exact non-vanishing of the rational $2 \times 2$ determinant
$k_{1,4_1}^{\mathrm{rat}} k_{2,\mathbb{B}_3}^{\mathrm{rat}} - k_{1,\mathbb{B}_3}^{\mathrm{rat}} k_{2,4_1}^{\mathrm{rat}} = \frac{31}{1296} \neq 0$. -/
theorem rational_rung12_det_ne_zero :
    k1Rat41 * k2RatB3 - k1RatB3 * k2Rat41 = 31 / 1296 ∧
    k1Rat41 * k2RatB3 - k1RatB3 * k2Rat41 ≠ 0 := by
  unfold k1Rat41 k2Rat41 k1RatB3 k2RatB3
  norm_num

/-- **Amphicheiral $2 \times 2$ Rung Annihilator Obstruction (`amphicheiral_two_rung_annihilator_trivial`):**
For any two grade observables $(u_{4_1}, u_{\mathbb{B}_3})$ and $(v_{4_1}, v_{\mathbb{B}_3})$ with
non-vanishing $2 \times 2$ determinant $u_{4_1} v_{\mathbb{B}_3} - u_{\mathbb{B}_3} v_{4_1} \neq 0$,
the only pair $(\alpha_{4_1}, \alpha_{\mathbb{B}_3}) \in \mathbb{R}^2$ annihilating both rungs is $(0, 0)$. -/
theorem amphicheiral_two_rung_annihilator_trivial {u41 uB3 v41 vB3 α41 αB3 : ℝ}
    (hdet : u41 * vB3 - uB3 * v41 ≠ 0)
    (hu : α41 * u41 + αB3 * uB3 = 0)
    (hv : α41 * v41 + αB3 * vB3 = 0) :
    α41 = 0 ∧ αB3 = 0 := by
  have hα41_mul : (u41 * vB3 - uB3 * v41) * α41 = 0 := by
    linear_combination vB3 * hu - uB3 * hv
  have hαB3_mul : (u41 * vB3 - uB3 * v41) * αB3 = 0 := by
    linear_combination -v41 * hu + u41 * hv
  exact ⟨(mul_eq_zero.mp hα41_mul).resolve_left hdet,
    (mul_eq_zero.mp hαB3_mul).resolve_left hdet⟩

/-- **Joint Three-Complement Annihilator Obstruction (`joint_three_complement_annihilator_trivial`):**
Let $(T_{4_1}, T_{5_2}, T_{\mathbb{B}_3})$ be graded complex-volume towers such that:
1. $4_1$ and $\mathbb{B}_3$ are amphicheiral ($T_{4_1}.\mathrm{cs}_0 = 0$, $T_{\mathbb{B}_3}.\mathrm{cs}_0 = 0$)
   and $5_2$ is chiral ($T_{5_2}.\mathrm{cs}_0 \neq 0$);
2. The $2 \times 2$ grade-$0$/grade-$1$ determinant on $(4_1, \mathbb{B}_3)$ is non-zero
   ($T_{4_1}.\mathrm{vol}_0 \cdot T_{\mathbb{B}_3}.\kappa(1) - T_{\mathbb{B}_3}.\mathrm{vol}_0 \cdot T_{4_1}.\kappa(1) \neq 0$).
Then the ONLY real triple $(\alpha_{4_1}, \alpha_{5_2}, \alpha_{\mathbb{B}_3}) \in \mathbb{R}^3$ that
simultaneously annihilates `jointGrade0Im`, `jointGrade0Re`, and `jointRungCoeff ... 1` is
$(\alpha_{4_1}, \alpha_{5_2}, \alpha_{\mathbb{B}_3}) = (0, 0, 0)$. -/
theorem joint_three_complement_annihilator_trivial
    {T41 T52 TB3 : GradedComplexVolumeTower} {α41 α52 αB3 : ℝ}
    (hcs41 : T41.cs0 = 0) (hcsB3 : TB3.cs0 = 0) (hcs52 : T52.cs0 ≠ 0)
    (hdet : T41.vol0 * TB3.kappa 1 - TB3.vol0 * T41.kappa 1 ≠ 0)
    (hg0_im : jointGrade0Im T41 T52 TB3 α41 α52 αB3 = 0)
    (hg0_re : jointGrade0Re T41 T52 TB3 α41 α52 αB3 = 0)
    (hg1 : jointRungCoeff T41 T52 TB3 1 α41 α52 αB3 = 0) :
    α41 = 0 ∧ α52 = 0 ∧ αB3 = 0 := by
  have hα52 : α52 = 0 :=
    (chiral_grade0_parity_blocker hcs41 hcsB3 hcs52 α41 α52 αB3).mp hg0_im
  have hu : α41 * T41.vol0 + αB3 * TB3.vol0 = 0 := by
    unfold jointGrade0Re jointLinearComb at hg0_re
    rw [hα52, zero_mul, add_zero] at hg0_re
    exact hg0_re
  have hv : α41 * T41.kappa 1 + αB3 * TB3.kappa 1 = 0 := by
    unfold jointRungCoeff jointLinearComb at hg1
    rw [hα52, zero_mul, add_zero] at hg1
    exact hg1
  obtain ⟨hα41, hαB3⟩ := amphicheiral_two_rung_annihilator_trivial hdet hu hv
  exact ⟨hα41, hα52, hαB3⟩

/-- **Single-Rung $\mathbb{Q}$-Linear Independence Annihilator Obstruction
(`single_rung_q_linear_indep_annihilator_trivial`):**
Suppose $(1, \omega_{4_1}, \omega_{5_2}) \in \mathbb{R}^3$ are $\mathbb{Q}$-linearly independent
(representing the algebraic prefactors in $\mathbb{Q}$, $\mathbb{Q}(\sqrt{3})$, and $K_{5_2}$),
the rational prefactors $r_{\mathbb{B}_3}, r_{4_1}, r_{5_2} \in \mathbb{Q}$ are non-zero, and
$\varpi \neq 0$ (representing $\pi^n$). Then any rational triple $(\alpha_{4_1}, \alpha_{5_2}, \alpha_{\mathbb{B}_3}) \in \mathbb{Q}^3$
annihilating the single rung
$((\alpha_{\mathbb{B}_3} r_{\mathbb{B}_3} : \mathbb{Q}) + (\alpha_{4_1} r_{4_1} : \mathbb{Q})\,\omega_{4_1} + (\alpha_{5_2} r_{5_2} : \mathbb{Q})\,\omega_{5_2}) \cdot \varpi = 0$
must satisfy $\alpha_{4_1} = 0 \wedge \alpha_{5_2} = 0 \wedge \alpha_{\mathbb{B}_3} = 0$. -/
theorem single_rung_q_linear_indep_annihilator_trivial
    {ω41 ω52 ϖ : ℝ} (hϖ : ϖ ≠ 0)
    (h_indep : ∀ cB3 c41 c52 : ℚ,
      (cB3 : ℝ) + (c41 : ℝ) * ω41 + (c52 : ℝ) * ω52 = 0 → cB3 = 0 ∧ c41 = 0 ∧ c52 = 0)
    {rB3 r41 r52 α41 α52 αB3 : ℚ}
    (hrB3 : rB3 ≠ 0) (hr41 : r41 ≠ 0) (hr52 : r52 ≠ 0)
    (h_ann : (((αB3 * rB3 : ℚ) : ℝ) + ((α41 * r41 : ℚ) : ℝ) * ω41 +
      ((α52 * r52 : ℚ) : ℝ) * ω52) * ϖ = 0) :
    α41 = 0 ∧ α52 = 0 ∧ αB3 = 0 := by
  have h_sum : ((αB3 * rB3 : ℚ) : ℝ) + ((α41 * r41 : ℚ) : ℝ) * ω41 +
      ((α52 * r52 : ℚ) : ℝ) * ω52 = 0 :=
    (mul_eq_zero.mp h_ann).resolve_right hϖ
  obtain ⟨hcB3, hc41, hc52⟩ := h_indep (αB3 * rB3) (α41 * r41) (α52 * r52) h_sum
  exact ⟨(mul_eq_zero.mp hc41).resolve_right hr41,
    (mul_eq_zero.mp hc52).resolve_right hr52,
    (mul_eq_zero.mp hcB3).resolve_right hrB3⟩

end QOU.QBeta.JointOhtsukiGradedTower
