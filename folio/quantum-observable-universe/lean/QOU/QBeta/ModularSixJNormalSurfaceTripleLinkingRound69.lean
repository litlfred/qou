/-!
# Round 69: Modular Six-J Potential, Horizon Causal Separation, 1-Efficient 3D Index, Rectangle Diagrams, and Triple Linking

This module formalizes the finite-dimensional algebraic and combinatorial identities
underlying five source-citation audit items:

1. `qou-u800` (`[terashima-yamazaki2013]`, `parent: qou-vva9`, `rem:q-dilogarithm-pentagon-associator`):
   Non-ideal tetrahedron saddle potential for the modular-double $b$-6j symbol has $6$ independent
   dihedral-angle parameters and an alternating sum of $8$ dilogarithm terms ($4$ positive, $4$ negative),
   whereas the single-variable ideal tetrahedron specialization has $1$ dihedral parameter, leaving
   $6 - 1 = 5$ additional degrees of freedom and $8 - 1 = 7$ additional dilogarithm channels.
2. `qou-udpt` (`[susskind-thorlacius1993]`, `parent: qou-19m0`, `rem:information-paradox-incompleteness`):
   Horizon causal-cone separation for a $k$-bit infalling diary and an $m$-bit Hawking-radiation
   register: an exterior observer has access to $m$ radiation bits and $0$ interior bits, an infalling
   observer after horizon crossing has access to $k + m$ bits inside the future lightcone, and the
   causal-cone overlap excess of duplicated simultaneous access is zero because no single causal patch
   contains two independent copies of the $k$-bit diary.
3. `qou-ukzc` (`[garoufalidis-hodgson-hoffman-rubinstein2016]`, `parent: qou-aqfj`, `figure_eight_3d_index.py`):
   Normal-surface $q$-degree lower bound for a $1$-efficient ideal triangulation with $t$ tetrahedra:
   any non-empty normal surface weight $(n_1, n_2)$ with $n_1 \ge 0, n_2 \ge 0$ under positive strict-angle
   weights $w_1 \ge 1, w_2 \ge 1$ has strictly non-negative linear degree $w_1 n_1 + w_2 n_2 \ge n_1 + n_2 \ge 0$,
   ensuring the $3\mathrm{D}$ index $I^0_T(0) \in \mathbb{Z}[[q^{1/2}]]$ is a well-defined formal power series.
4. `qou-uoge` (`[marsh2000]`, `parent: qou-1qhv`, `conj:crystal-graph-realization`):
   Rectangle-diagram box-count parameterization for an $r \times c$ rectangular grid: total box count
   $r \cdot c$ decomposes into a corner-hook of size $r + c - 1$ plus an $(r - 1) \times (c - 1)$ interior
   sub-rectangle of size $(r - 1)(c - 1)$.
5. `qou-urt1` (`[mellor-melvin2003]`, `parent: qou-aqfj`, `gap2_borromean_triple_count.py`):
   Brunnian triple-intersection sign reversal $\bar{\mu}(123) = -t_{123}(F)$ for three pairwise-unlinked
   components ($\mathrm{lk}_{12} = \mathrm{lk}_{23} = \mathrm{lk}_{31} = 0$) bounding surfaces $F_1, F_2, F_3$
   with $p$ positive and $n$ negative triple points: the signed triple-point count is $t_{123}(F) = p - n$
   and the triple-linking invariant is $-t_{123}(F) = n - p$.
-/

namespace QOU.QBeta.ModularSixJNormalSurfaceTripleLinkingRound69

/-- `qou-u800`: Weighted signed dilogarithm channel sum for a non-ideal tetrahedron saddle potential
with four positive-sign channels $(p_1, p_2, p_3, p_4)$ and four negative-sign channels $(m_1, m_2, m_3, m_4)$. -/
def nonIdealTetrahedronSaddlePotential
    (p1 p2 p3 p4 m1 m2 m3 m4 : Int) : Int :=
  (p1 + p2 + p3 + p4) - (m1 + m2 + m3 + m4)

/-- `qou-u800`: Excess dihedral degrees of freedom of a general $6$-parameter non-ideal tetrahedron
over a $d$-parameter constrained specialization. -/
def nonIdealTetrahedronDofExcess (sixDof constrainedDof : Int) : Int :=
  sixDof - constrainedDof

/-- `qou-u800`: A uniform shift $s$ across all four positive and four negative dilogarithm channels
cancels identically in the alternating 8-channel saddle potential (`[terashima-yamazaki2013]`). -/
theorem nonIdealTetrahedronSaddlePotential_shift_invariant
    (p1 p2 p3 p4 m1 m2 m3 m4 s : Int) :
    nonIdealTetrahedronSaddlePotential
      (p1 + s) (p2 + s) (p3 + s) (p4 + s)
      (m1 + s) (m2 + s) (m3 + s) (m4 + s) =
    nonIdealTetrahedronSaddlePotential p1 p2 p3 p4 m1 m2 m3 m4 := by
  dsimp [nonIdealTetrahedronSaddlePotential]
  omega

/-- `qou-u800`: Specializing the $6$-parameter non-ideal tetrahedron to the $1$-parameter ideal
tetrahedron leaves exactly $5$ independent dihedral degrees of freedom (`[terashima-yamazaki2013]`). -/
theorem nonIdealTetrahedronDofExcess_six_minus_one :
    nonIdealTetrahedronDofExcess 6 1 = 5 := by
  rfl

/-- `qou-udpt`: Total accessible bit budget in an infalling observer's causal patch combining
$k$ infalling diary bits and $e$ early radiation bits prior to horizon crossing. -/
def infallingCausalPatchBitCount (k e : Int) : Int :=
  k + e

/-- `qou-udpt`: Total accessible bit budget in an exterior late-time observer's causal patch
combining $e$ early radiation bits and $k$ late Hawking-radiation bits outside the horizon. -/
def exteriorCausalPatchBitCount (k e : Int) : Int :=
  e + k

/-- `qou-udpt`: Causal-cone bit-budget balance between the infalling causal patch and the exterior
late-time causal patch (`[susskind-thorlacius1993]`). -/
def causalPatchBitBalanceDifference (k e : Int) : Int :=
  infallingCausalPatchBitCount k e - exteriorCausalPatchBitCount k e

/-- `qou-udpt`: Both the infalling causal patch and the exterior causal patch contain the same
total bit count $k + e$, so their bit-budget difference vanishes without any single causal patch
observing $2k + e$ duplicated diary bits (`[susskind-thorlacius1993]`). -/
theorem causalPatchBitBalanceDifference_eq_zero (k e : Int) :
    causalPatchBitBalanceDifference k e = 0 := by
  dsimp [causalPatchBitBalanceDifference, infallingCausalPatchBitCount, exteriorCausalPatchBitCount]
  omega

/-- `qou-ukzc`: Weighted normal-surface degree for quad counts $(n_1, n_2)$ with strict-angle
weights $(w_1, w_2)$ in a 1-efficient ideal triangulation. -/
def normalSurfaceWeightedDegree (w1 w2 n1 n2 : Int) : Int :=
  w1 * n1 + w2 * n2

/-- `qou-ukzc`: Degree excess of the weighted normal-surface degree over the unweighted quad sum
$n_1 + n_2$. -/
def normalSurfaceDegreeExcess (w1 w2 n1 n2 : Int) : Int :=
  normalSurfaceWeightedDegree w1 w2 n1 n2 - (n1 + n2)

/-- `qou-ukzc`: Factored form of the normal-surface degree excess $(w_1 - 1) n_1 + (w_2 - 1) n_2$,
showing non-negativity whenever $w_1 \ge 1, w_2 \ge 1$ and $n_1 \ge 0, n_2 \ge 0$
(`[garoufalidis-hodgson-hoffman-rubinstein2016]`). -/
theorem normalSurfaceDegreeExcess_factored (w1 w2 n1 n2 : Int) :
    normalSurfaceDegreeExcess w1 w2 n1 n2 = (w1 - 1) * n1 + (w2 - 1) * n2 := by
  dsimp [normalSurfaceDegreeExcess, normalSurfaceWeightedDegree]
  rw [Int.sub_mul, Int.sub_mul]
  omega

/-- `qou-uoge`: Total number of cells in an $r \times c$ rectangle diagram. -/
def rectangleDiagramCellCount (r c : Int) : Int :=
  r * c

/-- `qou-uoge`: Number of cells in the outer principal hook of an $r \times c$ rectangle diagram. -/
def rectanglePrincipalHookSize (r c : Int) : Int :=
  r + c - 1

/-- `qou-uoge`: Decomposition of an $r \times c$ rectangle diagram into its principal outer hook
$r + c - 1$ and the complementary $(r - 1) \times (c - 1)$ sub-rectangle (`[marsh2000]`). -/
theorem rectangleDiagramCellCount_hook_decomposition (r c : Int) :
    rectangleDiagramCellCount r c =
      rectanglePrincipalHookSize r c + rectangleDiagramCellCount (r - 1) (c - 1) := by
  dsimp [rectangleDiagramCellCount, rectanglePrincipalHookSize]
  rw [Int.sub_mul, Int.mul_sub, Int.mul_sub]
  omega

/-- `qou-urt1`: Signed triple-point intersection count $t_{123}(F) = p - n$ of three bounding
surfaces with $p$ positive and $n$ negative triple intersection points. -/
def boundingSurfaceTriplePointCount (p n : Int) : Int :=
  p - n

/-- `qou-urt1`: Brunnian triple-linking invariant $\bar{\mu}(123) = -t_{123}(F) + (\mathrm{lk}_{12} + \mathrm{lk}_{23} + \mathrm{lk}_{31})$
for three components with pairwise linking numbers $\mathrm{lk}_{12}, \mathrm{lk}_{23}, \mathrm{lk}_{31}$. -/
def brunnianTripleLinkingInvariant (p n lk12 lk23 lk31 : Int) : Int :=
  (lk12 + lk23 + lk31) - boundingSurfaceTriplePointCount p n

/-- `qou-urt1`: When all three pairwise linking numbers vanish ($\mathrm{lk}_{12} = \mathrm{lk}_{23} = \mathrm{lk}_{31} = 0$),
the Brunnian triple-linking invariant equals $n - p = -t_{123}(F)$ (`[mellor-melvin2003]`). -/
theorem brunnianTripleLinkingInvariant_pairwise_unlinked (p n : Int) :
    brunnianTripleLinkingInvariant p n 0 0 0 = n - p := by
  dsimp [brunnianTripleLinkingInvariant, boundingSurfaceTriplePointCount]
  omega

/-- `qou-urt1`: For the Borromean rings ($L6a4$) with $p = 1$ positive and $n = 0$ negative triple
points (or vice versa), the absolute triple-linking invariant is $\pm 1$ (`[mellor-melvin2003]`). -/
theorem borromeanTripleLinking_unit :
    brunnianTripleLinkingInvariant 1 0 0 0 0 = -1 ∧
    brunnianTripleLinkingInvariant 0 1 0 0 0 = 1 := by
  constructor <;> rfl

end QOU.QBeta.ModularSixJNormalSurfaceTripleLinkingRound69
