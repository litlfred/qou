/-
Copyright (c) 2026 QOU Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Expansion Parameter Hierarchy Mismatch and Multiplet Mass Isoscalar Blindness

Formalizes two structural diagnostics in the nuclear expansion and body-order hierarchy:

1. **Expansion Parameter Hierarchy Mismatch (`qou-3wxk` / `A7`)**:
   - The framework's native expansion parameter $u = b \hbar_q^2 \approx 0.00852$
     ($852$ in units of $10^{-5}$) and the external chiral-EFT expansion ratio
     $Q / \Lambda_\chi \approx 0.33000$ ($33000$ in units of $10^{-5}$) differ by
     more than a factor of $38$ ($38 \times 852 = 32376 < 33000$, spread $32148 \times 10^{-5}$).
   - Importing external chiral power counting as a magnitude input therefore mixes
     two incommensurable expansion hierarchies; it can serve at most as a placement
     diagnostic.

2. **Isobaric Multiplet Mass Differences Are Blind to Isoscalar Extensive Terms (`qou-se8k` / `A5`)**:
   - For the cubic isobaric multiplet polynomial
     $M(T_3) = a + b T_3 + c T_3^2 + d T_3^3$, the second difference in $T_3$ at $d = 0$
     evaluates identically to $2 c$ and the third difference evaluates identically to $6 d$,
     regardless of the isoscalar coefficient $a$.
   - Consequently, isobaric multiplet rank bounds ($d / a \sim 10^{-7}$) constrain only
     charge-dependent isovector/isotensor/isovector-rank-3 channels and carry zero
     information about an isoscalar ($T_3$-independent) extensive binding term.
-/

namespace QOU.MassTheory.ExpansionParameterMismatchAndIMMEIsoscalarBlindness

/-- Native expansion parameter $u = b \hbar_q^2$ in units of $10^{-5}$. -/
def qouExpansionParamScaled100000 (uScaled : Int) : Int :=
  uScaled

/-- External chiral expansion ratio $Q / \Lambda_\chi$ in units of $10^{-5}$. -/
def chiralExpansionParamScaled100000 (qOverLambdaScaled : Int) : Int :=
  qOverLambdaScaled

/-- Spread between external chiral expansion ratio and native expansion parameter $u$. -/
def expansionHierarchySpreadScaled100000 (qOverLambdaScaled uScaled : Int) : Int :=
  chiralExpansionParamScaled100000 qOverLambdaScaled - qouExpansionParamScaled100000 uScaled

/-- Cubic isobaric multiplet mass polynomial $M(T_3) = a + b T_3 + c T_3^2 + d T_3^3$. -/
def immeMultipletMass (aIsoscalar bIsovector cIsotensor dCubic T3 : Int) : Int :=
  aIsoscalar + bIsovector * T3 + cIsotensor * (T3 * T3) + dCubic * (T3 * T3 * T3)

/-- Second central difference $M(1) - 2 M(0) + M(-1)$ isolating the quadratic isotensor coefficient. -/
def immeSecondDifferenceAtZero (aIsoscalar bIsovector cIsotensor dCubic : Int) : Int :=
  immeMultipletMass aIsoscalar bIsovector cIsotensor dCubic 1 -
    2 * immeMultipletMass aIsoscalar bIsovector cIsotensor dCubic 0 +
    immeMultipletMass aIsoscalar bIsovector cIsotensor dCubic (-1)

/-- Third difference $M(2) - 3 M(1) + 3 M(0) - M(-1)$ isolating the cubic rank-3 coefficient. -/
def immeThirdDifferenceAtZero (aIsoscalar bIsovector cIsotensor dCubic : Int) : Int :=
  immeMultipletMass aIsoscalar bIsovector cIsotensor dCubic 2 -
    3 * immeMultipletMass aIsoscalar bIsovector cIsotensor dCubic 1 +
    3 * immeMultipletMass aIsoscalar bIsovector cIsotensor dCubic 0 -
    immeMultipletMass aIsoscalar bIsovector cIsotensor dCubic (-1)

/-- Expansion hierarchy incommensurability (`qou-3wxk`): in units of $10^{-5}$,
    the native parameter $u = 852$ satisfies $38 u = 32376 < 33000 = Q/\Lambda_\chi$,
    with positive hierarchy spread $32148$. -/
theorem qou_vs_chiral_expansion_hierarchy_incommensurable
    (uScaled chiralScaled : Int)
    (hu : uScaled = 852) (hc : chiralScaled = 33000) :
    38 * uScaled < chiralScaled ∧
      expansionHierarchySpreadScaled100000 chiralScaled uScaled = 32148 ∧
      0 < expansionHierarchySpreadScaled100000 chiralScaled uScaled := by
  dsimp [expansionHierarchySpreadScaled100000, chiralExpansionParamScaled100000,
    qouExpansionParamScaled100000]
  have h1 : 38 * uScaled < chiralScaled := by omega
  have h2 : chiralScaled - uScaled = 32148 := by omega
  refine ⟨h1, h2, by omega⟩

/-- Multiplet mass differences annihilate the isoscalar extensive term (`qou-se8k`):
    for any two distinct isoscalar values $a_1, a_2$, the second difference at $T_3 = 0$
    equals $2 c$ and the third difference equals $6 d$, proving complete blindness of
    charge-dependent multiplet differences to the isoscalar term $a$. -/
theorem imme_differences_annihilate_isoscalar_extensive_term
    (a1 a2 b c d : Int) :
    immeSecondDifferenceAtZero a1 b c d = 2 * c ∧
      immeSecondDifferenceAtZero a2 b c d = 2 * c ∧
      immeThirdDifferenceAtZero a1 b c d = 6 * d ∧
      immeThirdDifferenceAtZero a2 b c d = 6 * d := by
  dsimp [immeSecondDifferenceAtZero, immeThirdDifferenceAtZero, immeMultipletMass]
  have hs1 : a1 + b * 1 + c * (1 * 1) + d * (1 * 1 * 1) -
      2 * (a1 + b * 0 + c * (0 * 0) + d * (0 * 0 * 0)) +
      (a1 + b * -1 + c * (-1 * -1) + d * (-1 * -1 * -1)) = 2 * c := by omega
  have hs2 : a2 + b * 1 + c * (1 * 1) + d * (1 * 1 * 1) -
      2 * (a2 + b * 0 + c * (0 * 0) + d * (0 * 0 * 0)) +
      (a2 + b * -1 + c * (-1 * -1) + d * (-1 * -1 * -1)) = 2 * c := by omega
  have ht1 : a1 + b * 2 + c * (2 * 2) + d * (2 * 2 * 2) -
      3 * (a1 + b * 1 + c * (1 * 1) + d * (1 * 1 * 1)) +
      3 * (a1 + b * 0 + c * (0 * 0) + d * (0 * 0 * 0)) -
      (a1 + b * -1 + c * (-1 * -1) + d * (-1 * -1 * -1)) = 6 * d := by omega
  have ht2 : a2 + b * 2 + c * (2 * 2) + d * (2 * 2 * 2) -
      3 * (a2 + b * 1 + c * (1 * 1) + d * (1 * 1 * 1)) +
      3 * (a2 + b * 0 + c * (0 * 0) + d * (0 * 0 * 0)) -
      (a2 + b * -1 + c * (-1 * -1) + d * (-1 * -1 * -1)) = 6 * d := by omega
  exact ⟨hs1, hs2, ht1, ht2⟩

end QOU.MassTheory.ExpansionParameterMismatchAndIMMEIsoscalarBlindness
