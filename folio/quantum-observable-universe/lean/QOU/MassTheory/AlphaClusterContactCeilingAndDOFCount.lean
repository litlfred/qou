/-
Copyright (c) 2026 QOU Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Alpha-Cluster Contact Ceiling, Prolate Sub-Max Contact Deficit, and Empirical Support Count

Formalizes two linked structural diagnostics in the alpha-cluster binding hierarchy:

1. **Cluster and Prolate Deviations Below Maximum Contact (`qou-3lsb` / `GAP-4`)**:
   - For $n_\alpha \ge 3$ alpha clusters in $\mathbb{R}^3$, the rigid sphere-packing
     maximum-contact count is $3 n_\alpha - 6$, while the complete-graph pair count
     is $\binom{n_\alpha}{2}$ (scaled by $2$: $n_\alpha(n_\alpha - 1)$).
   - Their scaled difference $n_\alpha(n_\alpha - 1) - 2(3 n_\alpha - 6)$ factors
     identically as $(n_\alpha - 3)(n_\alpha - 4)$, vanishing at $n_\alpha = 3$ ($^{12}\text{C}$)
     and $n_\alpha = 4$ ($^{16}\text{O}$) and becoming strictly positive at $n_\alpha \ge 5$.
   - At $^{20}\text{Ne}$ ($n_\alpha = 5$), the rigid maximum-contact count is $9$
     (strictly below $\binom{5}{2} = 10$), while the prolate $\alpha + {}^{16}\text{O}$
     configuration has $3 n_\alpha - 7 = 8$ contacts, a $1$-bond deficit below max-contact.

2. **Non-Closability of Empirical $b_{\alpha\alpha} \approx 2.41\text{ MeV}$ (`qou-ebs6`)**:
   - Because the complete-graph bond formula $\binom{n_\alpha}{2}$ is geometrically
     unrealizable in $\mathbb{R}^3$ for $n_\alpha \ge 5$, the complete-graph model's
     valid domain contains only $3$ nuclei: $^8\text{Be}$ ($n_\alpha = 2$),
     $^{12}\text{C}$ ($n_\alpha = 3$), and $^{16}\text{O}$ ($n_\alpha = 4$).
   - Excusing $^8\text{Be}$ ($b_{\alpha\alpha} \approx 0$) leaves only $2$ fitting points
     ($2425\text{ keV}$ at $^{12}\text{C}$ and $2406\text{ keV}$ at $^{16}\text{O}$, spread $19\text{ keV}$)
     for $1$ parameter $b_{\alpha\alpha}$, yielding $1$ residual degree of freedom and
     zero out-of-sample validation points outside the fitted pair.
-/

namespace QOU.MassTheory.AlphaClusterContactCeilingAndDOFCount

/-- Rigid 3D maximum-contact count $3 n_\alpha - 6$ for $n_\alpha \ge 3$ alpha clusters. -/
def maxAlphaContactsRigid3D (nAlpha : Int) : Int :=
  3 * nAlpha - 6

/-- Complete-graph alpha-pair count $\binom{n_\alpha}{2}$ scaled by $2$: $n_\alpha(n_\alpha - 1)$. -/
def completeAlphaPairsScaled2 (nAlpha : Int) : Int :=
  nAlpha * (nAlpha - 1)

/-- Prolate one-bond sub-max contact count $3 n_\alpha - 7$ (e.g. $^{20}\text{Ne} = \alpha + {}^{16}\text{O}$). -/
def prolateSubMaxContacts (nAlpha : Int) : Int :=
  3 * nAlpha - 7

/-- Excess of complete-graph pair count over rigid 3D max-contact count, scaled by $2$. -/
def completeMinusRigidContactExcessScaled2 (nAlpha : Int) : Int :=
  completeAlphaPairsScaled2 nAlpha - 2 * maxAlphaContactsRigid3D nAlpha

/-- Remaining degrees of freedom after subtracting excused points and fitted parameters. -/
def residualDegreesOfFreedom (totalValidPoints excusedPoints paramCount : Int) : Int :=
  totalValidPoints - excusedPoints - paramCount

/-- Exact algebraic factorization (`qou-3lsb`, `qou-ebs6`): the scaled excess of the
    complete-graph pair count over the rigid 3D max-contact count factors as
    $(n_\alpha - 3)(n_\alpha - 4)$. -/
theorem completeMinusRigidContactExcessScaled2_factored (nAlpha : Int) :
    completeMinusRigidContactExcessScaled2 nAlpha = (nAlpha - 3) * (nAlpha - 4) := by
  dsimp [completeMinusRigidContactExcessScaled2, completeAlphaPairsScaled2,
    maxAlphaContactsRigid3D]
  have h1 : (nAlpha - 3) * (nAlpha - 4) =
      nAlpha * (nAlpha - 4) - 3 * (nAlpha - 4) :=
    Int.sub_mul nAlpha 3 (nAlpha - 4)
  have h2 : nAlpha * (nAlpha - 4) = nAlpha * (nAlpha - 1) - 3 * nAlpha := by
    have ha : nAlpha - 4 = (nAlpha - 1) - 3 := by omega
    rw [ha, Int.mul_sub]
    have hb : nAlpha * 3 = 3 * nAlpha := Int.mul_comm nAlpha 3
    omega
  omega

/-- $^{20}\text{Ne}$ ($n_\alpha = 5$) prolate sub-max contact deficit and complete-graph
    overshoot (`qou-3lsb`): at $n_\alpha = 5$, the prolate $\alpha + {}^{16}\text{O}$
    contact count is $8$, one bond below the rigid max-contact ceiling $9$, while the
    complete-graph count ($10$, scaled by $2$ to $20$) strictly exceeds the rigid ceiling ($18$). -/
theorem ne20_prolate_sub_max_contact_and_halo_deficit
    (nAlpha : Int) (hn : nAlpha = 5) :
    prolateSubMaxContacts nAlpha = 8 ∧
      maxAlphaContactsRigid3D nAlpha = 9 ∧
      2 * maxAlphaContactsRigid3D nAlpha < completeAlphaPairsScaled2 nAlpha ∧
      maxAlphaContactsRigid3D nAlpha - prolateSubMaxContacts nAlpha = 1 := by
  dsimp [prolateSubMaxContacts, maxAlphaContactsRigid3D, completeAlphaPairsScaled2]
  have hp : 3 * nAlpha - 7 = 8 := by omega
  have hm : 3 * nAlpha - 6 = 9 := by omega
  have hlt : 2 * (3 * nAlpha - 6) < nAlpha * (nAlpha - 1) := by
    subst hn
    decide
  refine ⟨hp, hm, hlt, by omega⟩

/-- Empirical $b_{\alpha\alpha}$ degree-of-freedom accounting (`qou-ebs6`):
    in the $n_\alpha \le 4$ equilateral domain ($3$ valid nuclei: $^8\text{Be}, {}^{12}\text{C}, {}^{16}\text{O}$),
    excusing $^8\text{Be}$ ($1$ point) and fitting $1$ parameter $b_{\alpha\alpha}$
    leaves only $1$ residual degree of freedom between $^{12}\text{C}$ ($2425\text{ keV}$)
    and $^{16}\text{O}$ ($2406\text{ keV}$, spread $19\text{ keV}$), while at $n_\alpha = 5$
    the complete-graph excess $(5-3)(5-4) = 2 > 0$ breaks equilateral realizability. -/
theorem b_alpha_alpha_dof_and_equilateral_domain_bound
    (totalValid excused params bC12KeV bO16KeV : Int)
    (ht : totalValid = 3) (he : excused = 1) (hp : params = 1)
    (hc : bC12KeV = 2425) (ho : bO16KeV = 2406) :
    residualDegreesOfFreedom totalValid excused params = 1 ∧
      bC12KeV - bO16KeV = 19 ∧
      completeMinusRigidContactExcessScaled2 5 = 2 := by
  dsimp [residualDegreesOfFreedom, completeMinusRigidContactExcessScaled2,
    completeAlphaPairsScaled2, maxAlphaContactsRigid3D]
  have hdof : totalValid - excused - params = 1 := by omega
  have hsp : bC12KeV - bO16KeV = 19 := by omega
  refine ⟨hdof, hsp, rfl⟩

end QOU.MassTheory.AlphaClusterContactCeilingAndDOFCount
