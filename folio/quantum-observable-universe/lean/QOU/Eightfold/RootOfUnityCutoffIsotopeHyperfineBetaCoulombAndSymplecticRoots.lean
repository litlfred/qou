/-
Copyright (c) 2026 QOU Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Root-of-Unity Cutoff vs Real Positive Monotonicity, Isotope Hyperfine Separation, Isobaric Beta-Decay Coulomb Shift, Form-Factor Slope Charge Radius, and Symplectic Root Decomposition

This module formalizes structural lemmas across five work items under `qou-8lxd`:

1. **`qou-qhrw` (Odd root-of-unity cutoff index vs real positive non-vanishing)**:
   For the odd root-of-unity family $q_n = e^{i\pi/(2n-1)}$ ($n \ge 2$), the half-period order
   $N(n) = 2n - 1$ satisfies $N(n) \ge 3$ and $N(n) \bmod 2 = 1$, where the balanced quantum
   numerator $q_n^N - q_n^{-N} = (-1) - (-1) = 0$ vanishes. By contrast, for any distinct positive
   integers $a \neq b$ representing a rational $q = a / b \neq 1$, the difference $a^{2m} - b^{2m} \neq 0$
   for $m = 1$ ($a^2 \neq b^2$), so a real positive $q \neq 1$ has no algebraic vanishing at $m = 1$.

2. **`qou-fu7d` (Elemental vs hyperfine-weighted isotopic observable separation in r-II stars)**:
   Given two isotopic mixtures $(Y_{\text{odd}}^{(1)}, Y_{\text{even}}^{(1)})$ and
   $(Y_{\text{odd}}^{(2)}, Y_{\text{even}}^{(2)})$ with identical total elemental abundance
   $Y_{\text{odd}}^{(1)} + Y_{\text{even}}^{(1)} = Y_{\text{odd}}^{(2)} + Y_{\text{even}}^{(2)}$,
   any elemental-only observable $O_{\text{elem}} = c \cdot (Y_{\text{odd}} + Y_{\text{even}})$
   takes identical values on both mixtures, whereas any hyperfine-weighted observable
   $O_{\text{hfs}} = w_{\text{odd}} Y_{\text{odd}} + w_{\text{even}} Y_{\text{even}}$ with
   $w_{\text{odd}} > w_{\text{even}}$ strictly separates $Y_{\text{odd}}^{(1)} < Y_{\text{odd}}^{(2)}$.

3. **`qou-ihtw` (Isobaric beta-decay Coulomb pair difference along the A=88 kilonova chain)**:
   Along an isobaric $\beta^-$-decay step $(Z, A) \to (Z+1, A)$, the proton-pair count
   $P(Z) = Z(Z - 1)$ increments by $P(Z+1) - P(Z) = (Z+1)Z - Z(Z-1) = 2Z$. Across the two-step
   $A = 88$ waiting-point chain ${}^{88}\text{Kr} (Z=36) \to {}^{88}\text{Rb} (Z=37) \to {}^{88}\text{Sr} (Z=38)$,
   the cumulative pair increment is $2 \cdot 36 + 2 \cdot 37 = 146 = 38 \cdot 37 - 36 \cdot 35$.

4. **`qou-jogb` (Form-factor slope normalization and He-3 binding-length error improvement)**:
   In the low-momentum expansion $6 (1 - G_E(Q^2)) = \langle r^2 \rangle Q^2$, differentiating/dividing
   by $Q^2$ recovers $-6 \cdot (\text{slope}) = \langle r^2 \rangle$. On the integer-scaled ${}^3\text{He}$
   radius comparison (scale $10^4\text{ fm}^{-1}$: measured $25382$, binding-length $23795$,
   naive $r_0 A^{1/3} = 17307$), the binding-length error $1587$ is more than $5\times$ smaller
   than the liquid-drop error $8075$ ($5 \times 1587 = 7935 < 8075$).

5. **`qou-atsd-t3` (Symplectic root system $C_m$ short/long root split and Lie algebra dimension)**:
   For rank $m \ge 1$, the root system $C_m$ has $2 m (m - 1)$ short roots and $2 m$ long roots,
   summing to $2 m^2$ total roots, and adding the $m$-dimensional Cartan subalgebra yields the full
   symplectic dimension $m + 2 m^2 = m (2 m + 1)$ (giving $\dim = 3$, $0$ short roots, and $2$ long roots at $m = 1$).
-/

namespace QOU.Eightfold.RootOfUnityCutoffIsotopeHyperfineBetaCoulombAndSymplecticRoots

/-! ## Section 1: Odd Root-of-Unity Cutoff Index vs Real Positive Non-Vanishing (`qou-qhrw`) -/

/-- Odd root-of-unity half-period cutoff index $N(n) = 2 n - 1$. -/
def oddRootCutoffIndex (n : Nat) : Nat :=
  2 * n - 1

/-- For every $n \ge 2$, the cutoff index $N(n) = 2 n - 1$ is at least $3$ and odd ($N(n) \bmod 2 = 1$),
    with $(N(2), N(3), N(4)) = (3, 5, 7)$. -/
theorem oddRootCutoffIndex_properties (n : Nat) (hN : 2 ≤ n) :
    3 ≤ oddRootCutoffIndex n ∧
    (oddRootCutoffIndex n) % 2 = 1 ∧
    oddRootCutoffIndex 2 = 3 ∧
    oddRootCutoffIndex 3 = 5 ∧
    oddRootCutoffIndex 4 = 7 := by
  dsimp [oddRootCutoffIndex]
  refine ⟨by omega, by omega, by decide, by decide, by decide⟩

/-- For any positive integers $a < b$, their squares are strictly ordered ($a^2 < b^2$), so the
    balanced numerator factor $b^2 - a^2$ is strictly positive (cannot vanish on real $0 < a < b$). -/
theorem real_positive_square_diff_pos (a b : Nat) (hLt : a < b) :
    a * a < b * b ∧ 0 < b * b - a * a := by
  have h1 : a * a ≤ a * b := Nat.mul_le_mul_left a (Nat.le_of_lt hLt)
  have h2 : a * b < b * b := Nat.mul_lt_mul_of_pos_right hLt (by omega)
  omega

/-! ## Section 2: Elemental vs Hyperfine-Weighted Isotopic Observable Separation (`qou-fu7d`) -/

/-- Elemental-only observable $O_{\text{elem}}(c, Y_{\text{odd}}, Y_{\text{even}}) = c \cdot (Y_{\text{odd}} + Y_{\text{even}})$. -/
def elementalObservable (c yOdd yEven : Int) : Int :=
  c * (yOdd + yEven)

/-- Hyperfine-weighted isotopic observable $O_{\text{hfs}}(w_{\text{odd}}, w_{\text{even}}, Y_{\text{odd}}, Y_{\text{even}})
    = w_{\text{odd}} Y_{\text{odd}} + w_{\text{even}} Y_{\text{even}}$. -/
def hyperfineObservable (wOdd wEven yOdd yEven : Int) : Int :=
  wOdd * yOdd + wEven * yEven

/-- Two isotopic mixtures with equal total abundance $Y_{\text{odd}}^{(1)} + Y_{\text{even}}^{(1)}
    = Y_{\text{odd}}^{(2)} + Y_{\text{even}}^{(2)}$ are indistinguishable by `elementalObservable`,
    whereas for $w_{\text{even}} < w_{\text{odd}}$ and $Y_{\text{odd}}^{(1)} < Y_{\text{odd}}^{(2)}$,
    `hyperfineObservable` strictly separates them. -/
theorem elemental_degenerate_but_hyperfine_separates
    (c wOdd wEven yOdd1 yEven1 yOdd2 yEven2 : Int)
    (hTot : yOdd1 + yEven1 = yOdd2 + yEven2)
    (hWeight : wEven < wOdd)
    (hIso : yOdd1 < yOdd2) :
    elementalObservable c yOdd1 yEven1 = elementalObservable c yOdd2 yEven2 ∧
    hyperfineObservable wOdd wEven yOdd1 yEven1 <
      hyperfineObservable wOdd wEven yOdd2 yEven2 := by
  constructor
  · dsimp [elementalObservable]
    rw [hTot]
  · dsimp [hyperfineObservable]
    have hEven : yEven1 - yEven2 = yOdd2 - yOdd1 := by omega
    have hDiffPos : 0 < (wOdd - wEven) * (yOdd2 - yOdd1) :=
      Int.mul_pos (by omega) (by omega)
    have hExpand :
        (wOdd * yOdd2 + wEven * yEven2) - (wOdd * yOdd1 + wEven * yEven1) =
          (wOdd - wEven) * (yOdd2 - yOdd1) := by
      calc (wOdd * yOdd2 + wEven * yEven2) - (wOdd * yOdd1 + wEven * yEven1)
        _ = wOdd * (yOdd2 - yOdd1) - wEven * (yEven1 - yEven2) := by
          rw [Int.mul_sub, Int.mul_sub]
          omega
        _ = wOdd * (yOdd2 - yOdd1) - wEven * (yOdd2 - yOdd1) := by rw [hEven]
        _ = (wOdd - wEven) * (yOdd2 - yOdd1) := by rw [Int.sub_mul]
    omega

/-! ## Section 3: Isobaric Beta-Decay Coulomb Pair Difference (`qou-ihtw`) -/

/-- Ordered proton-pair count $P(Z) = Z (Z - 1)$ governing the nuclear Coulomb numerator. -/
def orderedProtonPairs (z : Nat) : Nat :=
  z * (z - 1)

/-- Single-step $\beta^-$ increment: for every $Z \ge 1$, advancing $Z \to Z + 1$ increases
    `orderedProtonPairs` by exactly $2 Z$, and across the $A = 88$ kilonova chain
    $Z = 36 \to 37 \to 38$ the two-step increment is $2 \cdot 36 + 2 \cdot 37 = 146$. -/
theorem isobaric_beta_proton_pair_increment (z : Nat) (hZ : 1 ≤ z) :
    orderedProtonPairs (z + 1) - orderedProtonPairs z = 2 * z ∧
    orderedProtonPairs 38 - orderedProtonPairs 36 = 146 ∧
    2 * 36 + 2 * 37 = 146 := by
  dsimp [orderedProtonPairs]
  have hMul : (z + 1) * z = z * (z - 1) + 2 * z := by
    have hZPred : z = (z - 1) + 1 := by omega
    calc (z + 1) * z
      _ = z * z + 1 * z := Nat.add_mul z 1 z
      _ = z * ((z - 1) + 1) + z := by rw [← hZPred, Nat.one_mul]
      _ = z * (z - 1) + z * 1 + z := by rw [Nat.mul_add]
      _ = z * (z - 1) + 2 * z := by omega
  refine ⟨by omega, by decide, by decide⟩

/-! ## Section 4: Form-Factor Slope Normalization and He-3 Binding-Length Error (`qou-jogb`) -/

/-- Scaled first-order electric form-factor drop $6 (G_0 - G_1) = r_{\text{sq}} \cdot q_{\text{sq}}$. -/
def formFactorLinearDrop (rSq qSq : Int) : Int :=
  rSq * qSq

/-- Uniform-ball vs RMS squared-radius cross-multiplied relation $5 R_{\text{rms}}^2 - 3 R_{\text{unif}}^2$. -/
def uniformBallRmsResidual (rRmsSq rUnifSq : Int) : Int :=
  5 * rRmsSq - 3 * rUnifSq

/-- On the ${}^3\text{He}$ charge-radius comparison (in units of $10^{-4}\text{ fm}$:
    measured $25382$, binding-length $23795$, liquid-drop $17307$), the binding-length absolute
    residual $1587$ improves over the liquid-drop residual $8075$ by more than a factor of $5$. -/
theorem he3_binding_length_fivefold_improvement :
    (25382 - 23795 : Nat) = 1587 ∧
    (25382 - 17307 : Nat) = 8075 ∧
    5 * (25382 - 23795 : Nat) < (25382 - 17307 : Nat) ∧
    uniformBallRmsResidual 3 5 = 0 := by
  decide

/-! ## Section 5: Symplectic Root System $C_m$ Decomposition (`qou-atsd-t3`) -/

/-- Number of short roots $\pm e_i \pm e_j$ ($i < j$) in the root system $C_m$: $2 m (m - 1)$. -/
def symplecticShortRootCount (m : Nat) : Nat :=
  2 * m * (m - 1)

/-- Number of long roots $\pm 2 e_i$ in the root system $C_m$: $2 m$. -/
def symplecticLongRootCount (m : Nat) : Nat :=
  2 * m

/-- Total root count $2 m^2$ of the root system $C_m$. -/
def symplecticTotalRootCount (m : Nat) : Nat :=
  2 * m * m

/-- Total Lie algebra dimension $m (2 m + 1) = \text{rank} + |R(C_m)|$ of $\mathfrak{sp}(2m)$. -/
def symplecticLieDim (m : Nat) : Nat :=
  m * (2 * m + 1)

/-- For every rank $m \ge 1$, the short and long roots of $C_m$ sum to $2 m^2$, adding the
    $m$-dimensional torus gives $\dim \mathfrak{sp}(2m) = m (2 m + 1)$, and at $m = 1$
    there are $0$ short roots, $2$ long roots, and total dimension $3$. -/
theorem symplectic_root_and_dimension_identities (m : Nat) (hM : 1 ≤ m) :
    symplecticShortRootCount m + symplecticLongRootCount m = symplecticTotalRootCount m ∧
    m + symplecticTotalRootCount m = symplecticLieDim m ∧
    symplecticShortRootCount 1 = 0 ∧
    symplecticLongRootCount 1 = 2 ∧
    symplecticLieDim 1 = 3 ∧
    symplecticLieDim 2 = 10 ∧
    symplecticLieDim 3 = 21 := by
  dsimp [symplecticShortRootCount, symplecticLongRootCount, symplecticTotalRootCount, symplecticLieDim]
  have hRootSum : 2 * m * (m - 1) + 2 * m = 2 * m * m := by
    have hMPred : m = (m - 1) + 1 := by omega
    calc 2 * m * (m - 1) + 2 * m
      _ = 2 * m * (m - 1) + 2 * m * 1 := by omega
      _ = 2 * m * ((m - 1) + 1) := by rw [← Nat.mul_add]
      _ = 2 * m * m := by rw [← hMPred]
  have hDim : m + 2 * m * m = m * (2 * m + 1) := by
    calc m + 2 * m * m
      _ = m * 1 + m * (2 * m) := by
        rw [Nat.mul_one, Nat.mul_comm (2 * m) m]
      _ = m * (1 + 2 * m) := by rw [← Nat.mul_add]
      _ = m * (2 * m + 1) := by rw [Nat.add_comm 1 (2 * m)]
  refine ⟨hRootSum, hDim, by decide, by decide, by decide, by decide, by decide⟩

end QOU.Eightfold.RootOfUnityCutoffIsotopeHyperfineBetaCoulombAndSymplecticRoots
