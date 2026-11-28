import QOU.BringsSurface.BringRegularMap
import QOU.FluidDynamics.DECYekutieliStokes
import Mathlib.Data.Fintype.Perm
import Mathlib.Tactic.Group
import Mathlib.Tactic.Ring

/-!
# Non-Abelian Yekutieli Stokes Theorem on Bring's 24-Pentagon $(2,4,5)$ Tessellation

Resolves the explicit open formalisation target noted in
`QOU/FluidDynamics/DECYekutieliStokes.lean` (lines 41–45): constructs the complete
120-dart Cayley map of Bring's genus-4 Riemann surface ($V = 30, E = 60, F = 24,
\chi = -6, g = 4$), an explicit 29-edge primal spanning tree $T$ connecting all 30
vertices, and an explicit 24-kite Yekutieli surface traversal, and proves over an
**arbitrary non-abelian `[Group G]`** (`0 sorry`, zero `[Field]`, zero `field_simp`,
zero `Real.*`) that the ordered product of the 24 rooted pentagon kite holonomies
equals the genus-4 fundamental-polygon commutator product $\prod_{j=1}^4 [a_j, b_j]$.

## Physics & Geometry Literature Context

* **Bralić (1980)** (*Exact computation of loop averages in two-dimensional Yang–Mills
  theory*, Phys. Rev. D 22, 3090–3103, DOI `10.1103/PhysRevD.22.3090`) and
  **Yekutieli (2015)** (*Nonabelian Multiplicative Integration on Surfaces*, World
  Scientific, DOI `10.1142/9537`): non-abelian Wilson-loop Stokes theorem on a
  2-complex requires conjugating each plaquette holonomy along a rooted whisker (kite)
  and multiplying in surface-cut order.
* **Atiyah–Bott (1983)** (*The Yang–Mills equations over Riemann surfaces*, Phil. Trans.
  R. Soc. Lond. A 308, 523–615) and **Witten (1991)** (*On quantum gauge theories in two
  dimensions*, Commun. Math. Phys. 141, 153–209): on a closed orientable genus-$g$
  surface ($\partial \Sigma = \emptyset$), the total surface-ordered holonomy of a
  lattice gauge connection $U$ is the commutator relator $\prod_{j=1}^g [a_j, b_j] \in [G, G]$,
  which equals `1` if and only if $U$ defines a flat $G$-bundle, and projects to `0` in
  every abelianisation $G^{\mathrm{ab}}$.
* **Etnyre–Ghrist (2000)** (*Contact topology and hydrodynamics I: Beltrami fields and
  the Seifert conjecture*, Nonlinearity 13, 441–458) and **Moffatt (1969)** (*The degree
  of knottedness of tangled vortex lines*, J. Fluid Mech. 35, 117–129): contact Reeb
  flows are steady Beltrami Euler flows ($\mathrm{curl}\,u = \lambda u$) whose knotted
  vortex-tube circulation and helicity live on the holonomy / linking layer.

## Main Proved Theorems (`0 sorry`)

1. `dartEquiv` & `dartPerm_sigma`, `dartPerm_alpha`, `dartPerm_phi`: exact bijection
   `Fin 120 ≃ Equiv.Perm (Fin 5)` intertwining the 120-dart combinatorial map with
   `QOU.BringRegularMap.S` (order 4), `A` (order 2), and `A * S` (order 5), with
   $V = 30, E = 60, F = 24, \chi = -6, g = 4$ (`bring_cayley_euler`).
2. `bring_spanning_tree_verified`: explicit 29-edge spanning tree $T$ connecting the
   root vertex `v₀ = 0` to all 30 vertices.
3. `yekutieliKiteHol_eq_conj_treeKiteHol` & `kiteFace_bijective`: each of the 24
   Yekutieli kites visits a distinct pentagon of Bring's surface (`Fin 24 ≃ Fin 24`)
   and conjugates its $T$-rooted pentagon holonomy `treeKiteHol U f` by a closed
   handle-sheet frame loop at `v₀`.
4. **`bring_yekutieli_nonabelian_stokes`**: for *every* `[Group G]` and *every* edge
   connection `U : Fin 60 → G`,
   `((List.finRange 24).map (yekutieliKiteHol U)).prod = ∏_{j=0}^3 [handleHolA U j, handleHolB U j]`.
5. `bring_nonabelian_stokes_nonflat_perm3`: explicit `Perm (Fin 3)` gauge connection
   for which both sides evaluate to a nontrivial 3-cycle `≠ 1`, proving non-vacuity of
   the non-abelian genus-4 commutator obstruction.
6. `bringDECComplex2` & `bring_discrete_stokes_vort_sum_eq_zero`: exact cochain complex
   `d₁ ∘ d₀ = 0` over any `[CommRing R]` on Bring's $(30, 60, 24)$ map, and derivation
   of the abelian discrete Stokes theorem $\sum_{f=0}^{23} (d_1 v)_f = 0$ directly as the
   `Multiplicative R` specialisation of `bring_yekutieli_nonabelian_stokes`.
-/

set_option autoImplicit false

namespace QOU.FluidDynamics.BringTessellationNonAbelianStokes

open QOU.BringRegularMap
open QOU.MathlibExt.YekutieliIntegration
open QOU.FluidDynamics.DECYekutieli

/-! ## 1. Explicit 120-Dart Bring Cayley Map and `Perm (Fin 5)` Isomorphism -/

/-- Canonical Cayley-graph generator word (`false ↦ S`, `true ↦ A`) for each dart `d : Fin 120`
(balanced binary tree of depth 7 for $O(\log N)$ kernel WHNF reduction). -/
def dartWord (d : Fin 120) : List Bool :=
  if d.val < 60 then
    if d.val < 30 then
      if d.val < 15 then
        if d.val < 7 then
          if d.val < 3 then
            if d.val < 1 then
              []
            else
              if d.val < 2 then
                [false, true, false, true, false, false, true, false, true]
              else
                [false, true, false, false, true, false, true, false, true]
          else
            if d.val < 5 then
              if d.val < 4 then
                [false, true, false, false, false, true, false, true]
              else
                [false, false, false, true, false, true, false, false, false, true]
            else
              if d.val < 6 then
                [false, false, true, false, false, true, false, false, true]
              else
                [true, false, true, false, false, false, true]
        else
          if d.val < 11 then
            if d.val < 9 then
              if d.val < 8 then
                [true, false, false, true, false, false, true, false]
              else
                [true, false, false, false, true, false, true, false]
            else
              if d.val < 10 then
                [false]
              else
                [false, false, true, false, false, false, true, false, true]
          else
            if d.val < 13 then
              if d.val < 12 then
                [false, false, true, false, false, true, false, true, false, true]
              else
                [true, false, true, false, true, false, false, true]
            else
              if d.val < 14 then
                [true, false, false, false, true, false, true, false, false]
              else
                [true, false, false, true, false, false, true]
      else
        if d.val < 22 then
          if d.val < 18 then
            if d.val < 16 then
              [false, true, false, true, false, false, false, true]
            else
              if d.val < 17 then
                [false, false]
              else
                [false, true, false, false, false, true, false, true, false]
          else
            if d.val < 20 then
              if d.val < 19 then
                [false, false, false]
              else
                [true, false, true, false, false, true, false, true]
            else
              if d.val < 21 then
                [true, false, false, true, false, true, false, true]
              else
                [true, false, false, false, true, false, true]
        else
          if d.val < 26 then
            if d.val < 24 then
              if d.val < 23 then
                [false, false, true, false, true, false, false, false, true]
              else
                [false, true, false, false, true, false, false, true]
            else
              if d.val < 25 then
                [true]
              else
                [false, true, false, true, false, false, true, false]
          else
            if d.val < 28 then
              if d.val < 27 then
                [false, true, false, false, true, false, true, false]
              else
                [false, true, false, false, false, true, false]
            else
              if d.val < 29 then
                [false, false, false, true, false, true, false, false, false]
              else
                [false, false, true, false, false, true, false, false]
    else
      if d.val < 45 then
        if d.val < 37 then
          if d.val < 33 then
            if d.val < 31 then
              [false, true, false, false, false, true]
            else
              if d.val < 32 then
                [false, false, true, false, false, true, false]
              else
                [false, false, false, true, false, true, false]
          else
            if d.val < 35 then
              if d.val < 34 then
                [true, false]
              else
                [false, true, false, false, true, false, true, false, false, false]
            else
              if d.val < 36 then
                [false, true, false, true, false, false, true, false, false]
              else
                [false, true, false, true, false, false, true]
        else
          if d.val < 41 then
            if d.val < 39 then
              if d.val < 38 then
                [false, false, false, true, false, true, false, false]
              else
                [false, false, true, false, false, true]
            else
              if d.val < 40 then
                [false, true, false, false, true, false, true, false, false]
              else
                [true, false, false]
          else
            if d.val < 43 then
              if d.val < 42 then
                [false, true, false, false, false, true, false, false]
              else
                [true, false, false, false]
            else
              if d.val < 44 then
                [false, true, false, false, true, false, true]
              else
                [false, false, true, false, true, false, true]
      else
        if d.val < 52 then
          if d.val < 48 then
            if d.val < 46 then
              [false, false, false, true, false, true]
            else
              if d.val < 47 then
                [false, true, false, true, false, false, true, false, false, false]
              else
                [false, false, true, false, false, true, false, false, false]
          else
            if d.val < 50 then
              if d.val < 49 then
                [true, false, true, false, false, false]
              else
                [false, false, false, true, false, false, true, false, false]
            else
              if d.val < 51 then
                [false, false, true, false, true, false, false, true, false]
              else
                [false, true]
        else
          if d.val < 56 then
            if d.val < 54 then
              if d.val < 53 then
                [false, false, true, false, false, false, true, false]
              else
                [false, false, true, false, false, true, false, true, false]
            else
              if d.val < 55 then
                [false, true, false, false, false]
              else
                [false, false, true, false, false, true, false, true]
          else
            if d.val < 58 then
              if d.val < 57 then
                [false, false, false, true, false, true, false, true]
              else
                [true, false, true]
            else
              if d.val < 59 then
                [true, false, false, true, false, false, false, true, false]
              else
                [false, false, false, true, false, false, true, false, false, false]
  else
    if d.val < 90 then
      if d.val < 75 then
        if d.val < 67 then
          if d.val < 63 then
            if d.val < 61 then
              [false, false, false, true, false, false, true, false]
            else
              if d.val < 62 then
                [false, false, true, false, false, false, true]
              else
                [true, false, false, false, true, false, false, true, false]
          else
            if d.val < 65 then
              if d.val < 64 then
                [true, false, false, true, false, false, false, true]
              else
                [true, false, true, false]
            else
              if d.val < 66 then
                [false, true, false]
              else
                [true, false, true, false, false]
        else
          if d.val < 71 then
            if d.val < 69 then
              if d.val < 68 then
                [false, false, true, false, true, false, false, true]
              else
                [false, true, false, false]
            else
              if d.val < 70 then
                [false, false, true, false, false, false, true, false, false]
              else
                [false, false, false, true, false, false, true]
          else
            if d.val < 73 then
              if d.val < 72 then
                [true, false, false, false, true, false, false, true]
              else
                [true, false, true, false, true, false, false]
            else
              if d.val < 74 then
                [false, false, false, true, false, false, true, false, true, false]
              else
                [true, false, false, true, false, false]
      else
        if d.val < 82 then
          if d.val < 78 then
            if d.val < 76 then
              [false, true, false, true, false, false, false]
            else
              if d.val < 77 then
                [false, false, true]
              else
                [false, false, false, true, false, true, false, false, true, false]
          else
            if d.val < 80 then
              if d.val < 79 then
                [false, true, false, true, false, false]
              else
                [false, false, false, true, false, true, false, false, true]
            else
              if d.val < 81 then
                [false, false, true, false, false]
              else
                [true, false, true, false, true, false, false, false]
        else
          if d.val < 86 then
            if d.val < 84 then
              if d.val < 83 then
                [true, false, false, true]
              else
                [false, true, false, false, false, true, false, false, true]
            else
              if d.val < 85 then
                [false, false, false, true, false, false, true, false, true]
              else
                [false, false, true, false, false, false]
          else
            if d.val < 88 then
              if d.val < 87 then
                [false, true, false, false, true, false, false, false, true, false]
              else
                [true, false, false, true, false, false, false]
            else
              if d.val < 89 then
                [true, false, true, false, true]
              else
                [false, true, false, true]
    else
      if d.val < 105 then
        if d.val < 97 then
          if d.val < 93 then
            if d.val < 91 then
              [true, false, true, false, true, false]
            else
              if d.val < 92 then
                [true, false, false, true, false]
              else
                [false, true, false, true, false]
          else
            if d.val < 95 then
              if d.val < 94 then
                [false, false, true, false]
              else
                [false, true, false, false, false, true, false, false, true, false]
            else
              if d.val < 96 then
                [false, true, false, false, true, false, false, false, true]
              else
                [false, false, false, true]
        else
          if d.val < 101 then
            if d.val < 99 then
              if d.val < 98 then
                [true, false, true, false, false, true, false]
              else
                [true, false, false, true, false, true, false]
            else
              if d.val < 100 then
                [true, false, false, false, true, false]
              else
                [false, false, true, false, true, false, false, false]
          else
            if d.val < 103 then
              if d.val < 102 then
                [false, true, false, false, true, false, false]
              else
                [true, false, false, false, true]
            else
              if d.val < 104 then
                [false, true, false, false, true, false]
              else
                [false, false, true, false, true, false]
      else
        if d.val < 112 then
          if d.val < 108 then
            if d.val < 106 then
              [false, false, false, true, false]
            else
              if d.val < 107 then
                [true, false, false, true, false, true, false, false, false]
              else
                [true, false, true, false, false, true, false, false]
          else
            if d.val < 110 then
              if d.val < 109 then
                [true, false, true, false, false, true]
              else
                [false, false, true, false, true, false, false]
            else
              if d.val < 111 then
                [false, true, false, false, true]
              else
                [true, false, false, true, false, true, false, false]
        else
          if d.val < 116 then
            if d.val < 114 then
              if d.val < 113 then
                [false, false, false, true, false, false]
              else
                [true, false, false, false, true, false, false]
            else
              if d.val < 115 then
                [false, false, false, true, false, false, false]
              else
                [true, false, false, true, false, true]
          else
            if d.val < 118 then
              if d.val < 117 then
                [false, true, false, true, false, true]
              else
                [false, false, true, false, true]
            else
              if d.val < 119 then
                [true, false, true, false, false, true, false, false, false]
              else
                [false, true, false, false, true, false, false, false]

/-- Evaluation of a generator word in `S = (1 2 3 4)` and `A = (0 1)` inside `Perm (Fin 5)`. -/
def evalSAWord (w : List Bool) : Equiv.Perm (Fin 5) :=
  w.foldl (fun acc b => acc * (if b then A else S)) 1

/-- Permutation in `S₅` represented by dart `d : Fin 120`. -/
def dartPerm (d : Fin 120) : Equiv.Perm (Fin 5) :=
  evalSAWord (dartWord d)

/-- Underlying `Nat` table for `sigmaDart` (depth 7 binary tree). -/
def sigmaDartNat (n : Nat) : Nat :=
  if n < 60 then
    if n < 30 then
      if n < 15 then
        if n < 7 then
          if n < 3 then
            if n < 1 then
              9
            else
              if n < 2 then
                11
              else
                15
          else
            if n < 5 then
              if n < 4 then
                17
              else
                21
            else
              if n < 6 then
                23
              else
                3
        else
          if n < 11 then
            if n < 9 then
              if n < 8 then
                5
              else
                13
            else
              if n < 10 then
                16
              else
                19
          else
            if n < 13 then
              if n < 12 then
                22
              else
                1
            else
              if n < 14 then
                4
              else
                7
      else
        if n < 22 then
          if n < 18 then
            if n < 16 then
              10
            else
              if n < 17 then
                18
              else
                20
          else
            if n < 20 then
              if n < 19 then
                0
              else
                2
            else
              if n < 21 then
                6
              else
                8
        else
          if n < 26 then
            if n < 24 then
              if n < 23 then
                12
              else
                14
            else
              if n < 25 then
                33
              else
                35
          else
            if n < 28 then
              if n < 27 then
                39
              else
                41
            else
              if n < 29 then
                45
              else
                47
    else
      if n < 45 then
        if n < 37 then
          if n < 33 then
            if n < 31 then
              27
            else
              if n < 32 then
                29
              else
                37
          else
            if n < 35 then
              if n < 34 then
                40
              else
                43
            else
              if n < 36 then
                46
              else
                25
        else
          if n < 41 then
            if n < 39 then
              if n < 38 then
                28
              else
                31
            else
              if n < 40 then
                34
              else
                42
          else
            if n < 43 then
              if n < 42 then
                44
              else
                24
            else
              if n < 44 then
                26
              else
                30
      else
        if n < 52 then
          if n < 48 then
            if n < 46 then
              32
            else
              if n < 47 then
                36
              else
                38
          else
            if n < 50 then
              if n < 49 then
                57
              else
                59
            else
              if n < 51 then
                63
              else
                65
        else
          if n < 56 then
            if n < 54 then
              if n < 53 then
                69
              else
                71
            else
              if n < 55 then
                51
              else
                53
          else
            if n < 58 then
              if n < 57 then
                61
              else
                64
            else
              if n < 59 then
                67
              else
                70
  else
    if n < 90 then
      if n < 75 then
        if n < 67 then
          if n < 63 then
            if n < 61 then
              49
            else
              if n < 62 then
                52
              else
                55
          else
            if n < 65 then
              if n < 64 then
                58
              else
                66
            else
              if n < 66 then
                68
              else
                48
        else
          if n < 71 then
            if n < 69 then
              if n < 68 then
                50
              else
                54
            else
              if n < 70 then
                56
              else
                60
          else
            if n < 73 then
              if n < 72 then
                62
              else
                81
            else
              if n < 74 then
                83
              else
                87
      else
        if n < 82 then
          if n < 78 then
            if n < 76 then
              89
            else
              if n < 77 then
                93
              else
                95
          else
            if n < 80 then
              if n < 79 then
                75
              else
                77
            else
              if n < 81 then
                85
              else
                88
        else
          if n < 86 then
            if n < 84 then
              if n < 83 then
                91
              else
                94
            else
              if n < 85 then
                73
              else
                76
          else
            if n < 88 then
              if n < 87 then
                79
              else
                82
            else
              if n < 89 then
                90
              else
                92
    else
      if n < 105 then
        if n < 97 then
          if n < 93 then
            if n < 91 then
              72
            else
              if n < 92 then
                74
              else
                78
          else
            if n < 95 then
              if n < 94 then
                80
              else
                84
            else
              if n < 96 then
                86
              else
                105
        else
          if n < 101 then
            if n < 99 then
              if n < 98 then
                107
              else
                111
            else
              if n < 100 then
                113
              else
                117
          else
            if n < 103 then
              if n < 102 then
                119
              else
                99
            else
              if n < 104 then
                101
              else
                109
      else
        if n < 112 then
          if n < 108 then
            if n < 106 then
              112
            else
              if n < 107 then
                115
              else
                118
          else
            if n < 110 then
              if n < 109 then
                97
              else
                100
            else
              if n < 111 then
                103
              else
                106
        else
          if n < 116 then
            if n < 114 then
              if n < 113 then
                114
              else
                116
            else
              if n < 115 then
                96
              else
                98
          else
            if n < 118 then
              if n < 117 then
                102
              else
                104
            else
              if n < 119 then
                108
              else
                110

theorem sigmaDartNat_lt (d : Fin 120) : sigmaDartNat d.val < 120 := by
  revert d; decide

/-- Vertex rotation `σ` (`d ↦ d * S`, order 4) on `Fin 120`. -/
def sigmaDart (d : Fin 120) : Fin 120 := ⟨sigmaDartNat d.val, sigmaDartNat_lt d⟩

/-- Underlying `Nat` table for `alphaDart` (depth 7 binary tree). -/
def alphaDartNat (n : Nat) : Nat :=
  if n < 60 then
    if n < 30 then
      if n < 15 then
        if n < 7 then
          if n < 3 then
            if n < 1 then
              24
            else
              if n < 2 then
                25
              else
                26
          else
            if n < 5 then
              if n < 4 then
                27
              else
                28
            else
              if n < 6 then
                29
              else
                48
        else
          if n < 11 then
            if n < 9 then
              if n < 8 then
                49
              else
                50
            else
              if n < 10 then
                51
              else
                52
          else
            if n < 13 then
              if n < 12 then
                53
              else
                72
            else
              if n < 14 then
                73
              else
                74
      else
        if n < 22 then
          if n < 18 then
            if n < 16 then
              75
            else
              if n < 17 then
                76
              else
                77
          else
            if n < 20 then
              if n < 19 then
                96
              else
                97
            else
              if n < 21 then
                98
              else
                99
        else
          if n < 26 then
            if n < 24 then
              if n < 23 then
                100
              else
                101
            else
              if n < 25 then
                0
              else
                1
          else
            if n < 28 then
              if n < 27 then
                2
              else
                3
            else
              if n < 29 then
                4
              else
                5
    else
      if n < 45 then
        if n < 37 then
          if n < 33 then
            if n < 31 then
              54
            else
              if n < 32 then
                55
              else
                56
          else
            if n < 35 then
              if n < 34 then
                57
              else
                58
            else
              if n < 36 then
                59
              else
                78
        else
          if n < 41 then
            if n < 39 then
              if n < 38 then
                79
              else
                80
            else
              if n < 40 then
                81
              else
                82
          else
            if n < 43 then
              if n < 42 then
                83
              else
                102
            else
              if n < 44 then
                103
              else
                104
      else
        if n < 52 then
          if n < 48 then
            if n < 46 then
              105
            else
              if n < 47 then
                106
              else
                107
          else
            if n < 50 then
              if n < 49 then
                6
              else
                7
            else
              if n < 51 then
                8
              else
                9
        else
          if n < 56 then
            if n < 54 then
              if n < 53 then
                10
              else
                11
            else
              if n < 55 then
                30
              else
                31
          else
            if n < 58 then
              if n < 57 then
                32
              else
                33
            else
              if n < 59 then
                34
              else
                35
  else
    if n < 90 then
      if n < 75 then
        if n < 67 then
          if n < 63 then
            if n < 61 then
              84
            else
              if n < 62 then
                85
              else
                86
          else
            if n < 65 then
              if n < 64 then
                87
              else
                88
            else
              if n < 66 then
                89
              else
                108
        else
          if n < 71 then
            if n < 69 then
              if n < 68 then
                109
              else
                110
            else
              if n < 70 then
                111
              else
                112
          else
            if n < 73 then
              if n < 72 then
                113
              else
                12
            else
              if n < 74 then
                13
              else
                14
      else
        if n < 82 then
          if n < 78 then
            if n < 76 then
              15
            else
              if n < 77 then
                16
              else
                17
          else
            if n < 80 then
              if n < 79 then
                36
              else
                37
            else
              if n < 81 then
                38
              else
                39
        else
          if n < 86 then
            if n < 84 then
              if n < 83 then
                40
              else
                41
            else
              if n < 85 then
                60
              else
                61
          else
            if n < 88 then
              if n < 87 then
                62
              else
                63
            else
              if n < 89 then
                64
              else
                65
    else
      if n < 105 then
        if n < 97 then
          if n < 93 then
            if n < 91 then
              114
            else
              if n < 92 then
                115
              else
                116
          else
            if n < 95 then
              if n < 94 then
                117
              else
                118
            else
              if n < 96 then
                119
              else
                18
        else
          if n < 101 then
            if n < 99 then
              if n < 98 then
                19
              else
                20
            else
              if n < 100 then
                21
              else
                22
          else
            if n < 103 then
              if n < 102 then
                23
              else
                42
            else
              if n < 104 then
                43
              else
                44
      else
        if n < 112 then
          if n < 108 then
            if n < 106 then
              45
            else
              if n < 107 then
                46
              else
                47
          else
            if n < 110 then
              if n < 109 then
                66
              else
                67
            else
              if n < 111 then
                68
              else
                69
        else
          if n < 116 then
            if n < 114 then
              if n < 113 then
                70
              else
                71
            else
              if n < 115 then
                90
              else
                91
          else
            if n < 118 then
              if n < 117 then
                92
              else
                93
            else
              if n < 119 then
                94
              else
                95

theorem alphaDartNat_lt (d : Fin 120) : alphaDartNat d.val < 120 := by
  revert d; decide

/-- Edge involution `α` (`d ↦ d * A`, order 2) on `Fin 120`. -/
def alphaDart (d : Fin 120) : Fin 120 := ⟨alphaDartNat d.val, alphaDartNat_lt d⟩

/-- Face rotation `φ = σ ∘ α` (`d ↦ d * (A * S)`, order 5) on `Fin 120`. -/
def phiDart (d : Fin 120) : Fin 120 :=
  sigmaDart (alphaDart d)

/-- Lehmer-rank inverse mapping any permutation `p : Equiv.Perm (Fin 5)` back to `Fin 120`. -/
def permRank (p : Equiv.Perm (Fin 5)) : Fin 120 :=
  let a0 := (p 0).val
  let a1 := (p 1).val - (if p 0 < p 1 then 1 else 0)
  let a2 := (p 2).val - (if p 0 < p 2 then 1 else 0) - (if p 1 < p 2 then 1 else 0)
  let a3 := (p 3).val - (if p 0 < p 3 then 1 else 0) - (if p 1 < p 3 then 1 else 0) -
      (if p 2 < p 3 then 1 else 0)
  let r := a0 * 24 + a1 * 6 + a2 * 2 + a3
  if h : r < 120 then ⟨r, h⟩ else ⟨0, by decide⟩

/-- `permRank` is a left inverse to `dartPerm` across all 120 darts. -/
theorem permRank_dartPerm (d : Fin 120) : permRank (dartPerm d) = d := by
  have hall : (List.finRange 120).all (fun x => permRank (dartPerm x) == x) = true := by
    decide
  exact beq_iff_eq.1 ((List.all_eq_true.1 hall) d (List.mem_finRange d))

/-- `dartPerm` is a bijection `Fin 120 → Equiv.Perm (Fin 5)`. -/
theorem dartPerm_bijective : Function.Bijective dartPerm := by
  have hinj : Function.Injective dartPerm := Function.LeftInverse.injective permRank_dartPerm
  exact (Fintype.bijective_iff_injective_and_card dartPerm).2
    ⟨hinj, by rw [Fintype.card_fin, Fintype.card_perm]; rfl⟩

/-- Explicit equivalence `Fin 120 ≃ Equiv.Perm (Fin 5)` identifying the 120 darts with `S₅`. -/
noncomputable def dartEquiv : Fin 120 ≃ Equiv.Perm (Fin 5) :=
  Equiv.ofBijective dartPerm dartPerm_bijective

set_option maxRecDepth 4096 in
/-- `sigmaDart` intertwines right multiplication by `S = (1 2 3 4)` on `S₅`. -/
theorem dartPerm_sigma (d : Fin 120) : dartPerm (sigmaDart d) = dartPerm d * S := by
  have hall : (List.finRange 120).all (fun x =>
      (List.finRange 5).all (fun i => dartPerm (sigmaDart x) i == (dartPerm x * S) i)) = true := by
    decide
  ext i
  have hx := (List.all_eq_true.1 hall) d (List.mem_finRange d)
  have hi := (List.all_eq_true.1 hx) i (List.mem_finRange i)
  exact congrArg Fin.val (beq_iff_eq.1 hi)

/-- `alphaDart` intertwines right multiplication by `A = (0 1)` on `S₅`. -/
theorem dartPerm_alpha (d : Fin 120) : dartPerm (alphaDart d) = dartPerm d * A := by
  have hall : (List.finRange 120).all (fun x =>
      (List.finRange 5).all (fun i => dartPerm (alphaDart x) i == (dartPerm x * A) i)) = true := by
    decide
  ext i
  have hx := (List.all_eq_true.1 hall) d (List.mem_finRange d)
  have hi := (List.all_eq_true.1 hx) i (List.mem_finRange i)
  exact congrArg Fin.val (beq_iff_eq.1 hi)

/-- `phiDart` intertwines right multiplication by `A * S = (0 1 2 3 4)` on `S₅`. -/
theorem dartPerm_phi (d : Fin 120) : dartPerm (phiDart d) = dartPerm d * (A * S) := by
  rw [phiDart, dartPerm_sigma, dartPerm_alpha, mul_assoc]

/-! ## 2. Vertices (`30`), Edges (`60`), Pentagon Faces (`24`), and Spanning Tree `T` (`29`) -/

/-- Underlying `Nat` table for `vertOfDart`. -/
def vertOfDartNat (n : Nat) : Nat :=
  if n < 60 then
    if n < 30 then
      if n < 15 then
        if n < 7 then
          if n < 3 then
            if n < 1 then
              0
            else
              if n < 2 then
                1
              else
                2
          else
            if n < 5 then
              if n < 4 then
                3
              else
                4
            else
              if n < 6 then
                5
              else
                3
        else
          if n < 11 then
            if n < 9 then
              if n < 8 then
                5
              else
                4
            else
              if n < 10 then
                0
              else
                2
          else
            if n < 13 then
              if n < 12 then
                1
              else
                1
            else
              if n < 14 then
                4
              else
                5
      else
        if n < 22 then
          if n < 18 then
            if n < 16 then
              2
            else
              if n < 17 then
                0
              else
                3
          else
            if n < 20 then
              if n < 19 then
                0
              else
                2
            else
              if n < 21 then
                3
              else
                4
        else
          if n < 26 then
            if n < 24 then
              if n < 23 then
                1
              else
                5
            else
              if n < 25 then
                6
              else
                7
          else
            if n < 28 then
              if n < 27 then
                8
              else
                9
            else
              if n < 29 then
                10
              else
                11
    else
      if n < 45 then
        if n < 37 then
          if n < 33 then
            if n < 31 then
              9
            else
              if n < 32 then
                11
              else
                10
          else
            if n < 35 then
              if n < 34 then
                6
              else
                8
            else
              if n < 36 then
                7
              else
                7
        else
          if n < 41 then
            if n < 39 then
              if n < 38 then
                10
              else
                11
            else
              if n < 40 then
                8
              else
                6
          else
            if n < 43 then
              if n < 42 then
                9
              else
                6
            else
              if n < 44 then
                8
              else
                9
      else
        if n < 52 then
          if n < 48 then
            if n < 46 then
              10
            else
              if n < 47 then
                7
              else
                11
          else
            if n < 50 then
              if n < 49 then
                12
              else
                13
            else
              if n < 51 then
                14
              else
                15
        else
          if n < 56 then
            if n < 54 then
              if n < 53 then
                16
              else
                17
            else
              if n < 55 then
                15
              else
                17
          else
            if n < 58 then
              if n < 57 then
                16
              else
                12
            else
              if n < 59 then
                14
              else
                13
  else
    if n < 90 then
      if n < 75 then
        if n < 67 then
          if n < 63 then
            if n < 61 then
              13
            else
              if n < 62 then
                16
              else
                17
          else
            if n < 65 then
              if n < 64 then
                14
              else
                12
            else
              if n < 66 then
                15
              else
                12
        else
          if n < 71 then
            if n < 69 then
              if n < 68 then
                14
              else
                15
            else
              if n < 70 then
                16
              else
                13
          else
            if n < 73 then
              if n < 72 then
                17
              else
                18
            else
              if n < 74 then
                19
              else
                20
      else
        if n < 82 then
          if n < 78 then
            if n < 76 then
              21
            else
              if n < 77 then
                22
              else
                23
          else
            if n < 80 then
              if n < 79 then
                21
              else
                23
            else
              if n < 81 then
                22
              else
                18
        else
          if n < 86 then
            if n < 84 then
              if n < 83 then
                20
              else
                19
            else
              if n < 85 then
                19
              else
                22
          else
            if n < 88 then
              if n < 87 then
                23
              else
                20
            else
              if n < 89 then
                18
              else
                21
    else
      if n < 105 then
        if n < 97 then
          if n < 93 then
            if n < 91 then
              18
            else
              if n < 92 then
                20
              else
                21
          else
            if n < 95 then
              if n < 94 then
                22
              else
                19
            else
              if n < 96 then
                23
              else
                24
        else
          if n < 101 then
            if n < 99 then
              if n < 98 then
                25
              else
                26
            else
              if n < 100 then
                27
              else
                28
          else
            if n < 103 then
              if n < 102 then
                29
              else
                27
            else
              if n < 104 then
                29
              else
                28
      else
        if n < 112 then
          if n < 108 then
            if n < 106 then
              24
            else
              if n < 107 then
                26
              else
                25
          else
            if n < 110 then
              if n < 109 then
                25
              else
                28
            else
              if n < 111 then
                29
              else
                26
        else
          if n < 116 then
            if n < 114 then
              if n < 113 then
                24
              else
                27
            else
              if n < 115 then
                24
              else
                26
          else
            if n < 118 then
              if n < 117 then
                27
              else
                28
            else
              if n < 119 then
                25
              else
                29

theorem vertOfDartNat_lt (d : Fin 120) : vertOfDartNat d.val < 30 := by
  revert d; decide

/-- Vertex index (`Fin 30`) of each dart (`σ`-orbit). -/
def vertOfDart (d : Fin 120) : Fin 30 := ⟨vertOfDartNat d.val, vertOfDartNat_lt d⟩

/-- Underlying `Nat` table for `edgeIdxOfDart`. -/
def edgeIdxOfDartNat (n : Nat) : Nat :=
  if n < 60 then
    if n < 30 then
      if n < 15 then
        if n < 7 then
          if n < 3 then
            if n < 1 then
              0
            else
              if n < 2 then
                1
              else
                2
          else
            if n < 5 then
              if n < 4 then
                3
              else
                4
            else
              if n < 6 then
                5
              else
                6
        else
          if n < 11 then
            if n < 9 then
              if n < 8 then
                7
              else
                8
            else
              if n < 10 then
                9
              else
                10
          else
            if n < 13 then
              if n < 12 then
                11
              else
                12
            else
              if n < 14 then
                13
              else
                14
      else
        if n < 22 then
          if n < 18 then
            if n < 16 then
              15
            else
              if n < 17 then
                16
              else
                17
          else
            if n < 20 then
              if n < 19 then
                18
              else
                19
            else
              if n < 21 then
                20
              else
                21
        else
          if n < 26 then
            if n < 24 then
              if n < 23 then
                22
              else
                23
            else
              if n < 25 then
                0
              else
                1
          else
            if n < 28 then
              if n < 27 then
                2
              else
                3
            else
              if n < 29 then
                4
              else
                5
    else
      if n < 45 then
        if n < 37 then
          if n < 33 then
            if n < 31 then
              24
            else
              if n < 32 then
                25
              else
                26
          else
            if n < 35 then
              if n < 34 then
                27
              else
                28
            else
              if n < 36 then
                29
              else
                30
        else
          if n < 41 then
            if n < 39 then
              if n < 38 then
                31
              else
                32
            else
              if n < 40 then
                33
              else
                34
          else
            if n < 43 then
              if n < 42 then
                35
              else
                36
            else
              if n < 44 then
                37
              else
                38
      else
        if n < 52 then
          if n < 48 then
            if n < 46 then
              39
            else
              if n < 47 then
                40
              else
                41
          else
            if n < 50 then
              if n < 49 then
                6
              else
                7
            else
              if n < 51 then
                8
              else
                9
        else
          if n < 56 then
            if n < 54 then
              if n < 53 then
                10
              else
                11
            else
              if n < 55 then
                24
              else
                25
          else
            if n < 58 then
              if n < 57 then
                26
              else
                27
            else
              if n < 59 then
                28
              else
                29
  else
    if n < 90 then
      if n < 75 then
        if n < 67 then
          if n < 63 then
            if n < 61 then
              42
            else
              if n < 62 then
                43
              else
                44
          else
            if n < 65 then
              if n < 64 then
                45
              else
                46
            else
              if n < 66 then
                47
              else
                48
        else
          if n < 71 then
            if n < 69 then
              if n < 68 then
                49
              else
                50
            else
              if n < 70 then
                51
              else
                52
          else
            if n < 73 then
              if n < 72 then
                53
              else
                12
            else
              if n < 74 then
                13
              else
                14
      else
        if n < 82 then
          if n < 78 then
            if n < 76 then
              15
            else
              if n < 77 then
                16
              else
                17
          else
            if n < 80 then
              if n < 79 then
                30
              else
                31
            else
              if n < 81 then
                32
              else
                33
        else
          if n < 86 then
            if n < 84 then
              if n < 83 then
                34
              else
                35
            else
              if n < 85 then
                42
              else
                43
          else
            if n < 88 then
              if n < 87 then
                44
              else
                45
            else
              if n < 89 then
                46
              else
                47
    else
      if n < 105 then
        if n < 97 then
          if n < 93 then
            if n < 91 then
              54
            else
              if n < 92 then
                55
              else
                56
          else
            if n < 95 then
              if n < 94 then
                57
              else
                58
            else
              if n < 96 then
                59
              else
                18
        else
          if n < 101 then
            if n < 99 then
              if n < 98 then
                19
              else
                20
            else
              if n < 100 then
                21
              else
                22
          else
            if n < 103 then
              if n < 102 then
                23
              else
                36
            else
              if n < 104 then
                37
              else
                38
      else
        if n < 112 then
          if n < 108 then
            if n < 106 then
              39
            else
              if n < 107 then
                40
              else
                41
          else
            if n < 110 then
              if n < 109 then
                48
              else
                49
            else
              if n < 111 then
                50
              else
                51
        else
          if n < 116 then
            if n < 114 then
              if n < 113 then
                52
              else
                53
            else
              if n < 115 then
                54
              else
                55
          else
            if n < 118 then
              if n < 117 then
                56
              else
                57
            else
              if n < 119 then
                58
              else
                59

theorem edgeIdxOfDartNat_lt (d : Fin 120) : edgeIdxOfDartNat d.val < 60 := by
  revert d; decide

/-- Orientation bit of each dart (`true` on canonical edge representative, `false` on `α`-mate). -/
def edgeSignOfDart (n : Nat) : Bool :=
  if n < 60 then
    if n < 30 then
      if n < 15 then
        if n < 7 then
          if n < 3 then
            if n < 1 then
              true
            else
              if n < 2 then
                true
              else
                true
          else
            if n < 5 then
              if n < 4 then
                true
              else
                true
            else
              if n < 6 then
                true
              else
                true
        else
          if n < 11 then
            if n < 9 then
              if n < 8 then
                true
              else
                true
            else
              if n < 10 then
                true
              else
                true
          else
            if n < 13 then
              if n < 12 then
                true
              else
                true
            else
              if n < 14 then
                true
              else
                true
      else
        if n < 22 then
          if n < 18 then
            if n < 16 then
              true
            else
              if n < 17 then
                true
              else
                true
          else
            if n < 20 then
              if n < 19 then
                true
              else
                true
            else
              if n < 21 then
                true
              else
                true
        else
          if n < 26 then
            if n < 24 then
              if n < 23 then
                true
              else
                true
            else
              if n < 25 then
                false
              else
                false
          else
            if n < 28 then
              if n < 27 then
                false
              else
                false
            else
              if n < 29 then
                false
              else
                false
    else
      if n < 45 then
        if n < 37 then
          if n < 33 then
            if n < 31 then
              true
            else
              if n < 32 then
                true
              else
                true
          else
            if n < 35 then
              if n < 34 then
                true
              else
                true
            else
              if n < 36 then
                true
              else
                true
        else
          if n < 41 then
            if n < 39 then
              if n < 38 then
                true
              else
                true
            else
              if n < 40 then
                true
              else
                true
          else
            if n < 43 then
              if n < 42 then
                true
              else
                true
            else
              if n < 44 then
                true
              else
                true
      else
        if n < 52 then
          if n < 48 then
            if n < 46 then
              true
            else
              if n < 47 then
                true
              else
                true
          else
            if n < 50 then
              if n < 49 then
                false
              else
                false
            else
              if n < 51 then
                false
              else
                false
        else
          if n < 56 then
            if n < 54 then
              if n < 53 then
                false
              else
                false
            else
              if n < 55 then
                false
              else
                false
          else
            if n < 58 then
              if n < 57 then
                false
              else
                false
            else
              if n < 59 then
                false
              else
                false
  else
    if n < 90 then
      if n < 75 then
        if n < 67 then
          if n < 63 then
            if n < 61 then
              true
            else
              if n < 62 then
                true
              else
                true
          else
            if n < 65 then
              if n < 64 then
                true
              else
                true
            else
              if n < 66 then
                true
              else
                true
        else
          if n < 71 then
            if n < 69 then
              if n < 68 then
                true
              else
                true
            else
              if n < 70 then
                true
              else
                true
          else
            if n < 73 then
              if n < 72 then
                true
              else
                false
            else
              if n < 74 then
                false
              else
                false
      else
        if n < 82 then
          if n < 78 then
            if n < 76 then
              false
            else
              if n < 77 then
                false
              else
                false
          else
            if n < 80 then
              if n < 79 then
                false
              else
                false
            else
              if n < 81 then
                false
              else
                false
        else
          if n < 86 then
            if n < 84 then
              if n < 83 then
                false
              else
                false
            else
              if n < 85 then
                false
              else
                false
          else
            if n < 88 then
              if n < 87 then
                false
              else
                false
            else
              if n < 89 then
                false
              else
                false
    else
      if n < 105 then
        if n < 97 then
          if n < 93 then
            if n < 91 then
              true
            else
              if n < 92 then
                true
              else
                true
          else
            if n < 95 then
              if n < 94 then
                true
              else
                true
            else
              if n < 96 then
                true
              else
                false
        else
          if n < 101 then
            if n < 99 then
              if n < 98 then
                false
              else
                false
            else
              if n < 100 then
                false
              else
                false
          else
            if n < 103 then
              if n < 102 then
                false
              else
                false
            else
              if n < 104 then
                false
              else
                false
      else
        if n < 112 then
          if n < 108 then
            if n < 106 then
              false
            else
              if n < 107 then
                false
              else
                false
          else
            if n < 110 then
              if n < 109 then
                false
              else
                false
            else
              if n < 111 then
                false
              else
                false
        else
          if n < 116 then
            if n < 114 then
              if n < 113 then
                false
              else
                false
            else
              if n < 115 then
                false
              else
                false
          else
            if n < 118 then
              if n < 117 then
                false
              else
                false
            else
              if n < 119 then
                false
              else
                false

/-- Oriented edge `(e, s) : Fin 60 × Bool` of each dart (`α`-orbit). -/
def edgeOfDart (d : Fin 120) : Fin 60 × Bool :=
  (⟨edgeIdxOfDartNat d.val, edgeIdxOfDartNat_lt d⟩, edgeSignOfDart d.val)

/-- Underlying `Nat` table for `faceOfDart`. -/
def faceOfDartNat (n : Nat) : Nat :=
  if n < 60 then
    if n < 30 then
      if n < 15 then
        if n < 7 then
          if n < 3 then
            if n < 1 then
              0
            else
              if n < 2 then
                1
              else
                2
          else
            if n < 5 then
              if n < 4 then
                3
              else
                4
            else
              if n < 6 then
                5
              else
                6
        else
          if n < 11 then
            if n < 9 then
              if n < 8 then
                7
              else
                8
            else
              if n < 10 then
                9
              else
                10
          else
            if n < 13 then
              if n < 12 then
                11
              else
                12
            else
              if n < 14 then
                13
              else
                14
      else
        if n < 22 then
          if n < 18 then
            if n < 16 then
              15
            else
              if n < 17 then
                16
              else
                17
          else
            if n < 20 then
              if n < 19 then
                18
              else
                19
            else
              if n < 21 then
                20
              else
                21
        else
          if n < 26 then
            if n < 24 then
              if n < 23 then
                22
              else
                23
            else
              if n < 25 then
                9
              else
                11
          else
            if n < 28 then
              if n < 27 then
                15
              else
                17
            else
              if n < 29 then
                21
              else
                23
    else
      if n < 45 then
        if n < 37 then
          if n < 33 then
            if n < 31 then
              16
            else
              if n < 32 then
                22
              else
                18
          else
            if n < 35 then
              if n < 34 then
                0
              else
                12
            else
              if n < 36 then
                1
              else
                10
        else
          if n < 41 then
            if n < 39 then
              if n < 38 then
                20
              else
                19
            else
              if n < 40 then
                2
              else
                6
          else
            if n < 43 then
              if n < 42 then
                3
              else
                8
            else
              if n < 44 then
                14
              else
                13
      else
        if n < 52 then
          if n < 48 then
            if n < 46 then
              4
            else
              if n < 47 then
                7
              else
                5
          else
            if n < 50 then
              if n < 49 then
                3
              else
                5
            else
              if n < 51 then
                13
              else
                16
        else
          if n < 56 then
            if n < 54 then
              if n < 53 then
                19
              else
                22
            else
              if n < 55 then
                17
              else
                23
          else
            if n < 58 then
              if n < 57 then
                20
              else
                6
            else
              if n < 59 then
                14
              else
                7
  else
    if n < 90 then
      if n < 75 then
        if n < 67 then
          if n < 63 then
            if n < 61 then
              4
            else
              if n < 62 then
                18
              else
                21
          else
            if n < 65 then
              if n < 64 then
                8
              else
                0
            else
              if n < 66 then
                9
              else
                2
        else
          if n < 71 then
            if n < 69 then
              if n < 68 then
                12
              else
                15
            else
              if n < 70 then
                10
              else
                1
          else
            if n < 73 then
              if n < 72 then
                11
              else
                1
            else
              if n < 74 then
                4
              else
                7
      else
        if n < 82 then
          if n < 78 then
            if n < 76 then
              10
            else
              if n < 77 then
                18
              else
                20
          else
            if n < 80 then
              if n < 79 then
                11
              else
                21
            else
              if n < 81 then
                22
              else
                12
        else
          if n < 86 then
            if n < 84 then
              if n < 83 then
                8
              else
                13
            else
              if n < 85 then
                5
              else
                19
          else
            if n < 88 then
              if n < 87 then
                23
              else
                14
            else
              if n < 89 then
                2
              else
                15
    else
      if n < 105 then
        if n < 97 then
          if n < 93 then
            if n < 91 then
              0
            else
              if n < 92 then
                6
              else
                9
          else
            if n < 95 then
              if n < 94 then
                16
              else
                3
            else
              if n < 96 then
                17
              else
                0
        else
          if n < 101 then
            if n < 99 then
              if n < 98 then
                2
              else
                6
            else
              if n < 100 then
                8
              else
                12
          else
            if n < 103 then
              if n < 102 then
                14
              else
                9
            else
              if n < 104 then
                15
              else
                16
      else
        if n < 112 then
          if n < 108 then
            if n < 106 then
              18
            else
              if n < 107 then
                10
              else
                19
          else
            if n < 110 then
              if n < 109 then
                3
              else
                13
            else
              if n < 111 then
                17
              else
                20
        else
          if n < 116 then
            if n < 114 then
              if n < 113 then
                4
              else
                21
            else
              if n < 115 then
                1
              else
                7
          else
            if n < 118 then
              if n < 117 then
                11
              else
                22
            else
              if n < 119 then
                5
              else
                23

theorem faceOfDartNat_lt (d : Fin 120) : faceOfDartNat d.val < 24 := by
  revert d; decide

/-- Pentagon face index (`Fin 24`) of each dart (`φ`-orbit). -/
def faceOfDart (d : Fin 120) : Fin 24 := ⟨faceOfDartNat d.val, faceOfDartNat_lt d⟩

/-- Underlying `Nat` table for `edgeRepDart`. -/
def edgeRepDartNat (n : Nat) : Nat :=
  if n < 30 then
    if n < 15 then
      if n < 7 then
        if n < 3 then
          if n < 1 then
            0
          else
            if n < 2 then
              1
            else
              2
        else
          if n < 5 then
            if n < 4 then
              3
            else
              4
          else
            if n < 6 then
              5
            else
              6
      else
        if n < 11 then
          if n < 9 then
            if n < 8 then
              7
            else
              8
          else
            if n < 10 then
              9
            else
              10
        else
          if n < 13 then
            if n < 12 then
              11
            else
              12
          else
            if n < 14 then
              13
            else
              14
    else
      if n < 22 then
        if n < 18 then
          if n < 16 then
            15
          else
            if n < 17 then
              16
            else
              17
        else
          if n < 20 then
            if n < 19 then
              18
            else
              19
          else
            if n < 21 then
              20
            else
              21
      else
        if n < 26 then
          if n < 24 then
            if n < 23 then
              22
            else
              23
          else
            if n < 25 then
              30
            else
              31
        else
          if n < 28 then
            if n < 27 then
              32
            else
              33
          else
            if n < 29 then
              34
            else
              35
  else
    if n < 45 then
      if n < 37 then
        if n < 33 then
          if n < 31 then
            36
          else
            if n < 32 then
              37
            else
              38
        else
          if n < 35 then
            if n < 34 then
              39
            else
              40
          else
            if n < 36 then
              41
            else
              42
      else
        if n < 41 then
          if n < 39 then
            if n < 38 then
              43
            else
              44
          else
            if n < 40 then
              45
            else
              46
        else
          if n < 43 then
            if n < 42 then
              47
            else
              60
          else
            if n < 44 then
              61
            else
              62
    else
      if n < 52 then
        if n < 48 then
          if n < 46 then
            63
          else
            if n < 47 then
              64
            else
              65
        else
          if n < 50 then
            if n < 49 then
              66
            else
              67
          else
            if n < 51 then
              68
            else
              69
      else
        if n < 56 then
          if n < 54 then
            if n < 53 then
              70
            else
              71
          else
            if n < 55 then
              90
            else
              91
        else
          if n < 58 then
            if n < 57 then
              92
            else
              93
          else
            if n < 59 then
              94
            else
              95

theorem edgeRepDartNat_lt (e : Fin 60) : edgeRepDartNat e.val < 120 := by
  revert e; decide

/-- Canonical representative dart of each oriented edge `e : Fin 60` (`s = true`). -/
def edgeRepDart (e : Fin 60) : Fin 120 := ⟨edgeRepDartNat e.val, edgeRepDartNat_lt e⟩

/-- Underlying `Nat` table for `faceStartDart`. -/
def faceStartDartNat (n : Nat) : Nat :=
  if n < 12 then
    if n < 6 then
      if n < 3 then
        if n < 1 then
          0
        else
          if n < 2 then
            1
          else
            66
      else
        if n < 4 then
          108
        else
          if n < 5 then
            4
          else
            118
    else
      if n < 9 then
        if n < 7 then
          6
        else
          if n < 8 then
            46
          else
            63
      else
        if n < 10 then
          102
        else
          if n < 11 then
            69
          else
            11
  else
    if n < 18 then
      if n < 15 then
        if n < 13 then
          34
        else
          if n < 14 then
            50
          else
            43
      else
        if n < 16 then
          15
        else
          if n < 17 then
            30
          else
            95
    else
      if n < 21 then
        if n < 19 then
          61
        else
          if n < 20 then
            107
          else
            56
      else
        if n < 22 then
          79
        else
          if n < 23 then
            22
          else
            119

theorem faceStartDartNat_lt (f : Fin 24) : faceStartDartNat f.val < 120 := by
  revert f; decide

/-- Canonical starting dart of each pentagon face `f : Fin 24`. -/
def faceStartDart (f : Fin 24) : Fin 120 := ⟨faceStartDartNat f.val, faceStartDartNat_lt f⟩

/-- Exact combinatorial map incidences on `(Fin 30, Fin 60, Fin 24)` and Euler characteristic
`V - E + F = 30 - 60 + 24 = -6 = 2 - 2 * 4` (genus `g = 4`). -/
theorem bring_cayley_euler :
    (∀ d : Fin 120, vertOfDart (sigmaDart d) = vertOfDart d) ∧
    (∀ d : Fin 120, edgeOfDart (alphaDart d) = ((edgeOfDart d).1, !(edgeOfDart d).2)) ∧
    (∀ d : Fin 120, faceOfDart (phiDart d) = faceOfDart d) ∧
    (∀ f : Fin 24, faceOfDart (faceStartDart f) = f) ∧
    ((Fintype.card (Fin 30) : ℤ) - Fintype.card (Fin 60) + Fintype.card (Fin 24) = -6) ∧
    ((2 : ℤ) - 2 * 4 = -6) := by
  refine ⟨by decide, by decide, by decide, by decide, ?_, by norm_num⟩
  simp

/-- Tail vertex of an oriented edge `(e, s) : Fin 60 × Bool`. -/
def edgeTail (es : Fin 60 × Bool) : Fin 30 :=
  if es.2 then vertOfDart (edgeRepDart es.1) else vertOfDart (alphaDart (edgeRepDart es.1))

/-- Head vertex of an oriented edge `(e, s) : Fin 60 × Bool`. -/
def edgeHead (es : Fin 60 × Bool) : Fin 30 :=
  if es.2 then vertOfDart (alphaDart (edgeRepDart es.1)) else vertOfDart (edgeRepDart es.1)

/-- Decidable head-to-tail walk predicate on Bring's 1-skeleton from vertex `u` to `v`. -/
def isEdgeWalk : Fin 30 → Fin 30 → List (Fin 60 × Bool) → Bool
  | u, v, [] => u == v
  | u, v, es :: rest => (edgeTail es == u) && isEdgeWalk (edgeHead es) v rest

/-- The 5-edge positively oriented boundary cycle of pentagon `f : Fin 24`. -/
def pentagonCycle (f : Fin 24) : List (Fin 60 × Bool) :=
  let d0 := faceStartDart f
  let d1 := phiDart d0
  let d2 := phiDart d1
  let d3 := phiDart d2
  let d4 := phiDart d3
  [edgeOfDart d0, edgeOfDart d1, edgeOfDart d2, edgeOfDart d3, edgeOfDart d4]

/-- Base vertex of pentagon `f : Fin 24` (`vertOfDart (faceStartDart f)`). -/
def pentagonBaseVert (f : Fin 24) : Fin 30 :=
  vertOfDart (faceStartDart f)

/-- Every pentagon boundary `pentagonCycle f` is a closed 5-edge walk at `pentagonBaseVert f`. -/
theorem isClosedWalk_pentagonCycle (f : Fin 24) :
    (pentagonCycle f).length = 5 ∧
      isEdgeWalk (pentagonBaseVert f) (pentagonBaseVert f) (pentagonCycle f) = true := by
  revert f; decide

/-- Fast `Bool` membership predicate for the 29-edge primal spanning tree `T`. -/
def isBringTreeEdge (e : Fin 60) : Bool :=
  if e.val < 30 then
    if e.val < 15 then
      if e.val < 7 then
        if e.val < 3 then
          if e.val < 1 then
            true
          else
            if e.val < 2 then
              false
            else
              false
        else
          if e.val < 5 then
            if e.val < 4 then
              false
            else
              false
          else
            if e.val < 6 then
              false
            else
              true
      else
        if e.val < 11 then
          if e.val < 9 then
            if e.val < 8 then
              false
            else
              false
          else
            if e.val < 10 then
              true
            else
              false
        else
          if e.val < 13 then
            if e.val < 12 then
              false
            else
              false
          else
            if e.val < 14 then
              false
            else
              true
    else
      if e.val < 22 then
        if e.val < 18 then
          if e.val < 16 then
            true
          else
            if e.val < 17 then
              true
            else
              false
        else
          if e.val < 20 then
            if e.val < 19 then
              true
            else
              false
          else
            if e.val < 21 then
              false
            else
              true
      else
        if e.val < 26 then
          if e.val < 24 then
            if e.val < 23 then
              true
            else
              false
          else
            if e.val < 25 then
              true
            else
              false
        else
          if e.val < 28 then
            if e.val < 27 then
              false
            else
              true
          else
            if e.val < 29 then
              false
            else
              false
  else
    if e.val < 45 then
      if e.val < 37 then
        if e.val < 33 then
          if e.val < 31 then
            true
          else
            if e.val < 32 then
              false
            else
              true
        else
          if e.val < 35 then
            if e.val < 34 then
              false
            else
              true
          else
            if e.val < 36 then
              true
            else
              true
      else
        if e.val < 41 then
          if e.val < 39 then
            if e.val < 38 then
              true
            else
              false
          else
            if e.val < 40 then
              true
            else
              false
        else
          if e.val < 43 then
            if e.val < 42 then
              false
            else
              false
          else
            if e.val < 44 then
              true
            else
              false
    else
      if e.val < 52 then
        if e.val < 48 then
          if e.val < 46 then
            true
          else
            if e.val < 47 then
              false
            else
              true
        else
          if e.val < 50 then
            if e.val < 49 then
              true
            else
              false
          else
            if e.val < 51 then
              true
            else
              false
      else
        if e.val < 56 then
          if e.val < 54 then
            if e.val < 53 then
              true
            else
              true
          else
            if e.val < 55 then
              true
            else
              true
        else
          if e.val < 58 then
            if e.val < 57 then
              false
            else
              true
          else
            if e.val < 59 then
              false
            else
              true

/-- Explicit 29-edge primal spanning tree `T` of Bring's 1-skeleton. -/
def bringTreeEdges : Finset (Fin 60) :=
  Finset.univ.filter (fun e => isBringTreeEdge e = true)

/-- Unique reduced path in `bringTreeEdges` from root vertex `v₀ = 0` to `v : Fin 30`. -/
def treePath (v : Fin 30) : List (Fin 60 × Bool) :=
  if v.val < 15 then
    if v.val < 7 then
      if v.val < 3 then
        if v.val < 1 then
          []
        else
          if v.val < 2 then
            [(16, true), (57, true), (22, false)]
          else
            [(9, true), (47, true), (15, false)]
      else
        if v.val < 5 then
          if v.val < 4 then
            [(0, true), (27, true), (6, false)]
          else
            [(0, true), (36, true), (21, false)]
        else
          if v.val < 6 then
            [(0, true), (34, true), (14, false)]
          else
            [(0, true)]
    else
      if v.val < 11 then
        if v.val < 9 then
          if v.val < 8 then
            [(9, true), (47, true), (30, false)]
          else
            [(9, true), (50, true), (37, false)]
        else
          if v.val < 10 then
            [(9, true), (24, false)]
          else
            [(18, true), (39, false)]
      else
        if v.val < 13 then
          if v.val < 12 then
            [(16, true), (32, false)]
          else
            [(0, true), (27, true)]
        else
          if v.val < 14 then
            [(18, true), (52, false)]
          else
            [(0, true), (34, true), (45, false)]
  else
    if v.val < 22 then
      if v.val < 18 then
        if v.val < 16 then
          [(9, true)]
        else
          if v.val < 17 then
            [(16, true), (43, false)]
          else
            [(0, true), (36, true), (53, false)]
      else
        if v.val < 20 then
          if v.val < 19 then
            [(18, true), (54, false)]
          else
            [(9, true), (24, false), (35, true)]
        else
          if v.val < 21 then
            [(0, true), (34, true)]
          else
            [(9, true), (47, true)]
    else
      if v.val < 26 then
        if v.val < 24 then
          if v.val < 23 then
            [(16, true)]
          else
            [(9, true), (50, true), (59, false)]
        else
          if v.val < 25 then
            [(18, true)]
          else
            [(0, true), (27, true), (48, true)]
      else
        if v.val < 28 then
          if v.val < 27 then
            [(0, true), (34, true), (55, true)]
          else
            [(0, true), (36, true)]
        else
          if v.val < 29 then
            [(16, true), (57, true)]
          else
            [(9, true), (50, true)]

/-- `bringTreeEdges` has cardinality `29 = 30 - 1`, and `treePath v` is a valid walk
in `bringTreeEdges` from the base vertex `0` to every vertex `v : Fin 30`. -/
theorem bring_spanning_tree_verified :
    bringTreeEdges.card = 29 ∧
    (∀ v : Fin 30, isEdgeWalk 0 v (treePath v) = true) ∧
    (∀ v : Fin 30, ∀ es ∈ treePath v, es.1 ∈ bringTreeEdges) := by
  have hmem : ∀ v : Fin 30, (treePath v).all (fun es => isBringTreeEdge es.1) = true := by
    decide
  refine ⟨by decide, by decide, ?_⟩
  intro v es hes
  rw [bringTreeEdges, Finset.mem_filter]
  exact ⟨Finset.mem_univ _, (List.all_eq_true.1 (hmem v)) es hes⟩

/-! ## 3. Tail-Recursive Free-Group Path Calculus and Rooted Pentagon Kite Holonomies -/

/-- Reverse an oriented edge path by reversing order and flipping edge orientations. -/
def revEdgePath (w : List (Fin 60 × Bool)) : List (Fin 60 × Bool) :=
  (w.map (fun es => (es.1, !es.2))).reverse

/-- `faceHolonomy` of `revEdgePath w` is the exact group inverse `(faceHolonomy U w)⁻¹`. -/
theorem faceHolonomy_revEdgePath {G : Type*} [Group G] (U : Fin 60 → G)
    (w : List (Fin 60 × Bool)) :
    faceHolonomy U (revEdgePath w) = (faceHolonomy U w)⁻¹ := by
  unfold faceHolonomy revEdgePath
  rw [← holonomy_reverse_map_inv, List.map_reverse, List.map_map, List.map_map]
  apply congrArg holonomy
  apply congrArg List.reverse
  apply List.map_congr_left
  intro es _
  obtain ⟨e, b⟩ := es
  cases b <;> simp [edgeTransport]

/-- `faceHolonomy` is multiplicative under edge-path concatenation `w₁ ++ w₂`. -/
theorem faceHolonomy_append_edges {G : Type*} [Group G] (U : Fin 60 → G)
    (w₁ w₂ : List (Fin 60 × Bool)) :
    faceHolonomy U (w₁ ++ w₂) = faceHolonomy U w₁ * faceHolonomy U w₂ := by
  unfold faceHolonomy
  rw [List.map_append, holonomy_append]

/-- Tail-recursive stack push/pop step for free-group word reduction on `Fin 60 × Bool`
(constant $O(1)$ stack depth in kernel `decide`!). -/
def freeStepRev (stk : List (Fin 60 × Bool)) (es : Fin 60 × Bool) : List (Fin 60 × Bool) :=
  match stk with
  | [] => [es]
  | hd :: tl => if hd.1 == es.1 && hd.2 == !es.2 then tl else es :: hd :: tl

/-- Tail-recursive linear-time free-group word reduction cancelling adjacent inverse pairs. -/
def freeReduce (w : List (Fin 60 × Bool)) : List (Fin 60 × Bool) :=
  (w.foldl freeStepRev []).reverse

/-- Single stack step `freeStepRev` preserves `faceHolonomy U stk.reverse * edgeTransport U es`. -/
theorem faceHolonomy_freeStepRev {G : Type*} [Group G] (U : Fin 60 → G)
    (stk : List (Fin 60 × Bool)) (es : Fin 60 × Bool) :
    faceHolonomy U (freeStepRev stk es).reverse =
      faceHolonomy U stk.reverse * edgeTransport U es := by
  cases stk with
  | nil =>
    dsimp only [freeStepRev]
    unfold faceHolonomy
    simp [holonomy]
  | cons hd tl =>
    dsimp only [freeStepRev]
    cases h : (hd.1 == es.1 && hd.2 == !es.2)
    · simp only [Bool.false_eq_true, ↓reduceIte, List.reverse_cons, faceHolonomy_append_edges]
      unfold faceHolonomy
      simp [holonomy, mul_assoc]
    · simp only [↓reduceIte]
      simp only [Bool.and_eq_true, beq_iff_eq] at h
      rcases hd with ⟨e1, b1⟩
      rcases es with ⟨e2, b2⟩
      simp only at h
      rcases h with ⟨rfl, rfl⟩
      rw [List.reverse_cons, faceHolonomy_append_edges, mul_assoc]
      have hinv : faceHolonomy U [(e1, !b2)] * edgeTransport U (e1, b2) = 1 := by
        unfold faceHolonomy
        cases b2 <;> simp [holonomy, edgeTransport]
      rw [hinv, mul_one]

/-- Tail-recursive `foldl freeStepRev` invariant over any `[Group G]`. -/
theorem faceHolonomy_foldl_freeStepRev {G : Type*} [Group G] (U : Fin 60 → G)
    (w stk : List (Fin 60 × Bool)) :
    faceHolonomy U (w.foldl freeStepRev stk).reverse =
      faceHolonomy U stk.reverse * faceHolonomy U w := by
  induction w generalizing stk with
  | nil => simp [faceHolonomy, holonomy]
  | cons es tl ih =>
    unfold faceHolonomy
    rw [List.map_cons, holonomy_cons]
    change faceHolonomy U (tl.foldl freeStepRev (freeStepRev stk es)).reverse =
      faceHolonomy U stk.reverse * (edgeTransport U es * faceHolonomy U tl)
    rw [ih, faceHolonomy_freeStepRev, mul_assoc]

/-- Free-group reduction `freeReduce` preserves `faceHolonomy` identically over any `[Group G]`. -/
theorem faceHolonomy_freeReduce {G : Type*} [Group G] (U : Fin 60 → G)
    (w : List (Fin 60 × Bool)) :
    faceHolonomy U (freeReduce w) = faceHolonomy U w := by
  unfold freeReduce
  rw [faceHolonomy_foldl_freeStepRev]
  simp [faceHolonomy, holonomy]

/-- Spanning-tree parallel transport `treeHol U v : G` from base vertex `v₀ = 0` to `v`. -/
def treeHol {G : Type*} [Group G] (U : Fin 60 → G) (v : Fin 30) : G :=
  faceHolonomy U (treePath v)

/-- **Spanning-tree rooted pentagon kite holonomy** `treeKiteHol U f : G`:
pentagon `f`'s boundary holonomy conjugated along `treePath (pentagonBaseVert f)` to `v₀ = 0`. -/
def treeKiteHol {G : Type*} [Group G] (U : Fin 60 → G) (f : Fin 24) : G :=
  treeHol U (pentagonBaseVert f) * faceHolonomy U (pentagonCycle f) *
    (treeHol U (pentagonBaseVert f))⁻¹

/-! ## 4. Explicit 24-Kite Surface Traversal and Genus-4 Handle Loops -/

/-- Underlying `Nat` table for `kiteFace`. -/
def kiteFaceNat (n : Nat) : Nat :=
  if n < 12 then
    if n < 6 then
      if n < 3 then
        if n < 1 then
          3
        else
          if n < 2 then
            5
          else
            18
      else
        if n < 4 then
          17
        else
          if n < 5 then
            6
          else
            20
    else
      if n < 9 then
        if n < 7 then
          10
        else
          if n < 8 then
            19
          else
            15
      else
        if n < 10 then
          21
        else
          if n < 11 then
            23
          else
            14
  else
    if n < 18 then
      if n < 15 then
        if n < 13 then
          8
        else
          if n < 14 then
            4
          else
            16
      else
        if n < 16 then
          13
        else
          if n < 17 then
            22
          else
            9
    else
      if n < 21 then
        if n < 19 then
          11
        else
          if n < 20 then
            7
          else
            1
      else
        if n < 22 then
          12
        else
          if n < 23 then
            2
          else
            0

theorem kiteFaceNat_lt (k : Fin 24) : kiteFaceNat k.val < 24 := by
  revert k; decide

/-- Face ordering `kiteFace : Fin 24 → Fin 24` of the 24-pentagon Yekutieli kite traversal. -/
def kiteFace (k : Fin 24) : Fin 24 := ⟨kiteFaceNat k.val, kiteFaceNat_lt k⟩

/-- `kiteFace` is a bijection `Fin 24 → Fin 24`: every one of the 24 Bring pentagons
appears in the ordered surface product **exactly once**. -/
theorem kiteFace_bijective : Function.Bijective kiteFace := by
  refine (Fintype.bijective_iff_injective_and_card kiteFace).2 ⟨?_, rfl⟩
  decide

/-- Whisker path from `v₀ = 0` to `pentagonBaseVert (kiteFace k)` for the `k`-th kite. -/
def kiteWhisker (k : Fin 24) : List (Fin 60 × Bool) :=
  if k.val < 12 then
    if k.val < 6 then
      if k.val < 3 then
        if k.val < 1 then
          [(0, true), (27, true), (48, true)]
        else
          if k.val < 2 then
            [(0, true), (27, true), (48, true)]
          else
            [(0, true), (27, true), (48, true), (41, false), (32, true), (43, false)]
      else
        if k.val < 4 then
          [(0, true), (27, true), (48, true), (41, false), (32, true), (43, false), (26, false), (31, true)]
        else
          if k.val < 5 then
            [(0, true), (27, true), (48, true), (41, false), (32, true), (43, false), (26, false), (31, true), (17, false)]
          else
            [(0, true), (27, true), (48, true), (41, false), (32, true), (43, false)]
    else
      if k.val < 9 then
        if k.val < 7 then
          [(0, true), (27, true), (48, true), (41, false), (32, true), (43, false)]
        else
          if k.val < 8 then
            [(0, true), (27, true), (48, true)]
          else
            [(0, true), (27, true), (48, true), (19, false)]
      else
        if k.val < 10 then
          [(0, true), (27, true), (48, true), (19, false), (2, true), (37, true), (59, false)]
        else
          if k.val < 11 then
            [(0, true), (27, true), (48, true), (19, false), (2, true), (37, true)]
          else
            [(0, true), (27, true), (48, true), (19, false), (2, true)]
  else
    if k.val < 18 then
      if k.val < 15 then
        if k.val < 13 then
          [(0, true), (27, true), (48, true), (19, false), (2, true), (28, true)]
        else
          if k.val < 14 then
            [(0, true), (27, true), (48, true), (19, false), (2, true), (28, true), (8, false)]
          else
            [(0, true), (27, true), (48, true), (19, false), (2, true), (28, true), (8, false), (13, true), (35, false)]
      else
        if k.val < 16 then
          [(0, true), (27, true), (48, true), (19, false), (2, true), (28, true)]
        else
          if k.val < 17 then
            [(0, true), (27, true), (48, true), (19, false), (2, true), (28, true), (49, true), (22, false)]
          else
            [(0, true), (27, true), (48, true), (19, false), (2, true), (28, true), (49, true), (22, false), (11, true), (53, true)]
    else
      if k.val < 21 then
        if k.val < 19 then
          [(0, true), (27, true), (48, true), (19, false), (2, true), (28, true), (49, true), (22, false)]
        else
          if k.val < 20 then
            [(0, true), (27, true), (48, true), (19, false), (2, true), (28, true), (49, true), (22, false), (1, true)]
          else
            [(0, true), (27, true), (48, true), (19, false), (2, true), (28, true), (49, true), (22, false)]
      else
        if k.val < 22 then
          [(0, true), (27, true), (48, true), (19, false), (2, true)]
        else
          if k.val < 23 then
            [(0, true), (27, true)]
          else
            []

/-- Closed handle-sheet frame loop at `v₀ = 0` factoring `kiteWhisker k` through `treePath`. -/
def kiteSheetLoop (k : Fin 24) : List (Fin 60 × Bool) :=
  if k.val < 12 then
    if k.val < 6 then
      if k.val < 3 then
        if k.val < 1 then
          []
        else
          if k.val < 2 then
            []
          else
            [(0, true), (27, true), (48, true), (41, false), (32, true), (16, false)]
      else
        if k.val < 4 then
          [(0, true), (27, true), (48, true), (41, false), (32, true), (43, false), (26, false), (31, true), (59, true), (50, false), (9, false)]
        else
          if k.val < 5 then
            [(0, true), (27, true), (48, true), (41, false), (32, true), (43, false), (26, false), (31, true), (17, false), (6, true), (27, false), (0, false)]
          else
            [(0, true), (27, true), (48, true), (41, false), (32, true), (16, false)]
    else
      if k.val < 9 then
        if k.val < 7 then
          [(0, true), (27, true), (48, true), (41, false), (32, true), (16, false)]
        else
          if k.val < 8 then
            []
          else
            [(0, true), (27, true), (48, true), (19, false), (15, true), (47, false), (9, false)]
      else
        if k.val < 10 then
          [(0, true), (27, true), (48, true), (19, false), (2, true), (37, true), (50, false), (9, false)]
        else
          if k.val < 11 then
            [(0, true), (27, true), (48, true), (19, false), (2, true), (37, true), (50, false), (9, false)]
          else
            [(0, true), (27, true), (48, true), (19, false), (2, true), (37, true), (50, false), (9, false)]
  else
    if k.val < 18 then
      if k.val < 15 then
        if k.val < 13 then
          [(0, true), (27, true), (48, true), (19, false), (2, true), (28, true), (45, true), (34, false), (0, false)]
        else
          if k.val < 14 then
            [(0, true), (27, true), (48, true), (19, false), (2, true), (28, true), (8, false), (21, true), (36, false), (0, false)]
          else
            [(0, true), (27, true), (48, true), (19, false), (2, true), (28, true), (8, false), (13, true), (35, false), (24, true), (9, false)]
      else
        if k.val < 16 then
          [(0, true), (27, true), (48, true), (19, false), (2, true), (28, true), (45, true), (34, false), (0, false)]
        else
          if k.val < 17 then
            [(0, true), (27, true), (48, true), (19, false), (2, true), (28, true), (49, true), (57, false), (16, false)]
          else
            [(0, true), (27, true), (48, true), (19, false), (2, true), (28, true), (49, true), (22, false), (11, true), (53, true), (36, false), (0, false)]
    else
      if k.val < 21 then
        if k.val < 19 then
          [(0, true), (27, true), (48, true), (19, false), (2, true), (28, true), (49, true), (57, false), (16, false)]
        else
          if k.val < 20 then
            [(0, true), (27, true), (48, true), (19, false), (2, true), (28, true), (49, true), (22, false), (1, true), (30, true), (47, false), (9, false)]
          else
            [(0, true), (27, true), (48, true), (19, false), (2, true), (28, true), (49, true), (57, false), (16, false)]
      else
        if k.val < 22 then
          [(0, true), (27, true), (48, true), (19, false), (2, true), (37, true), (50, false), (9, false)]
        else
          if k.val < 23 then
            []
          else
            []

/-- Every `kiteWhisker k` is a walk from `0` to `pentagonBaseVert (kiteFace k)`, and
`kiteSheetLoop k` is a closed loop at `0` factoring `kiteWhisker k` through `treePath`. -/
theorem kiteWhisker_factorisation (k : Fin 24) :
    isEdgeWalk 0 (pentagonBaseVert (kiteFace k)) (kiteWhisker k) = true ∧
    isEdgeWalk 0 0 (kiteSheetLoop k) = true ∧
    freeReduce (kiteSheetLoop k ++ treePath (pentagonBaseVert (kiteFace k))) =
      freeReduce (kiteWhisker k) := by
  revert k; decide

/-- Full closed edge-loop of the `k`-th Yekutieli kite based at `v₀ = 0`. -/
def yekutieliKiteLoop (k : Fin 24) : List (Fin 60 × Bool) :=
  kiteWhisker k ++ pentagonCycle (kiteFace k) ++ revEdgePath (kiteWhisker k)

/-- **Rooted Yekutieli kite boundary holonomy** `yekutieliKiteHol U k : G` of the `k`-th
pentagon in the surface-cut ordering. -/
def yekutieliKiteHol {G : Type*} [Group G] (U : Fin 60 → G) (k : Fin 24) : G :=
  faceHolonomy U (kiteWhisker k) * faceHolonomy U (pentagonCycle (kiteFace k)) *
    (faceHolonomy U (kiteWhisker k))⁻¹

/-- `yekutieliKiteHol U k` equals `faceHolonomy U (yekutieliKiteLoop k)`. -/
theorem yekutieliKiteHol_eq_loop {G : Type*} [Group G] (U : Fin 60 → G) (k : Fin 24) :
    yekutieliKiteHol U k = faceHolonomy U (yekutieliKiteLoop k) := by
  unfold yekutieliKiteHol yekutieliKiteLoop
  rw [faceHolonomy_append_edges, faceHolonomy_append_edges, faceHolonomy_revEdgePath]

/-- **Sheet-frame relation to spanning-tree kite holonomy:** `yekutieliKiteHol U k` is
the conjugate of the spanning-tree rooted pentagon holonomy `treeKiteHol U (kiteFace k)`
by the closed `v₀`-loop holonomy `faceHolonomy U (kiteSheetLoop k)`. -/
theorem yekutieliKiteHol_eq_conj_treeKiteHol {G : Type*} [Group G] (U : Fin 60 → G)
    (k : Fin 24) :
    yekutieliKiteHol U k =
      faceHolonomy U (kiteSheetLoop k) * treeKiteHol U (kiteFace k) *
        (faceHolonomy U (kiteSheetLoop k))⁻¹ := by
  have hw : faceHolonomy U (kiteWhisker k) =
      faceHolonomy U (kiteSheetLoop k) * treeHol U (pentagonBaseVert (kiteFace k)) := by
    rw [← faceHolonomy_freeReduce U (kiteWhisker k), ← (kiteWhisker_factorisation k).2.2,
      faceHolonomy_freeReduce, faceHolonomy_append_edges, treeHol]
  unfold yekutieliKiteHol treeKiteHol
  rw [hw]
  group

/-- Explicit `a_j`-handle closed loops (`j : Fin 4`) at `v₀ = 0` on Bring's 1-skeleton. -/
def handleLoopA (j : Fin 4) : List (Fin 60 × Bool) :=
  if j.val < 2 then
    if j.val < 1 then
      [(0, true), (27, true), (6, false), (3, true), (24, true), (50, true), (59, false), (31, false), (39, true), (18, false), (16, true), (32, false), (5, false), (7, true), (52, true), (39, false), (4, false), (21, true), (36, false), (34, true), (14, false), (5, true), (25, true), (53, true), (21, false), (4, true), (31, true), (59, true), (50, false), (47, true), (30, false), (40, true), (55, false), (34, false), (0, false)]
    else
      [(0, true), (34, true), (55, true), (40, false), (30, true), (47, false), (9, false), (0, true), (36, true), (53, false), (25, false), (32, true), (16, false), (9, true), (50, true), (59, false), (31, false), (39, true), (18, false), (16, true), (32, false), (5, false), (14, true), (34, false), (0, false)]
  else
    if j.val < 3 then
      [(0, true), (34, true), (14, false), (5, true), (25, true), (53, true), (36, false), (0, false)]
    else
      [(0, true), (36, true), (53, false), (25, false), (32, true), (16, false)]

/-- Explicit `b_j`-handle closed loops (`j : Fin 4`) at `v₀ = 0` on Bring's 1-skeleton. -/
def handleLoopB (j : Fin 4) : List (Fin 60 × Bool) :=
  if j.val < 2 then
    if j.val < 1 then
      [(0, true), (34, true), (55, true), (40, false), (30, true), (47, false), (50, true), (59, false), (31, false), (4, false), (21, true), (53, false), (25, false), (5, false), (14, true), (34, false), (36, true), (21, false), (4, true), (39, true), (52, false), (7, false), (5, true), (32, true), (16, false), (18, true), (39, false), (31, true), (59, true), (50, false), (24, false), (35, true), (42, false), (52, true), (39, false), (4, false), (21, true), (36, false), (34, true), (14, false), (5, true), (25, true), (53, true), (21, false), (4, true), (31, true), (59, true), (50, false), (47, true), (30, false), (40, true), (55, false), (34, false), (0, false)]
    else
      [(0, true), (34, true), (14, false), (5, true), (32, true), (16, false), (18, true), (39, false), (31, true), (59, true), (50, false), (9, false), (16, true), (32, false), (25, true), (53, true), (36, false), (0, false), (9, true), (50, true), (59, false), (31, false), (4, false), (21, true), (53, false), (25, false), (5, false), (14, true), (34, false), (36, true), (21, false), (4, true), (39, true), (52, false), (7, false), (14, true), (34, false), (0, false)]
  else
    if j.val < 3 then
      [(0, true), (36, true), (53, false), (25, false), (32, true), (16, false), (18, true), (39, false), (31, true), (59, true), (50, false), (9, false), (16, true), (32, false), (25, true), (53, true), (36, false), (0, false), (9, true), (50, true), (59, false), (31, false), (4, false), (21, true), (36, false), (0, false)]
    else
      [(18, true), (39, false), (31, true), (59, true), (50, false), (9, false)]

/-- All eight fundamental-group generator loops `handleLoopA j`, `handleLoopB j` (`j : Fin 4`)
are genuine closed edge-walks starting and ending at `v₀ = 0` on Bring's 1-skeleton. -/
theorem isClosedWalk_handleLoops (j : Fin 4) :
    isEdgeWalk 0 0 (handleLoopA j) = true ∧ isEdgeWalk 0 0 (handleLoopB j) = true := by
  revert j; decide

/-- Holonomy `a_j ∈ G` along the `j`-th handle generator `handleLoopA j`. -/
def handleHolA {G : Type*} [Group G] (U : Fin 60 → G) (j : Fin 4) : G :=
  faceHolonomy U (handleLoopA j)

/-- Holonomy `b_j ∈ G` along the `j`-th handle generator `handleLoopB j`. -/
def handleHolB {G : Type*} [Group G] (U : Fin 60 → G) (j : Fin 4) : G :=
  faceHolonomy U (handleLoopB j)

/-- Group commutator `[a, b] = a * b * a⁻¹ * b⁻¹`. -/
def groupComm {G : Type*} [Group G] (a b : G) : G :=
  a * b * a⁻¹ * b⁻¹

/-- Edge-loop concatenation realising `[handleLoopA j, handleLoopB j]`. -/
def handleCommLoop (j : Fin 4) : List (Fin 60 × Bool) :=
  handleLoopA j ++ handleLoopB j ++ revEdgePath (handleLoopA j) ++ revEdgePath (handleLoopB j)

theorem faceHolonomy_handleCommLoop {G : Type*} [Group G] (U : Fin 60 → G) (j : Fin 4) :
    faceHolonomy U (handleCommLoop j) = groupComm (handleHolA U j) (handleHolB U j) := by
  unfold handleCommLoop groupComm handleHolA handleHolB
  simp only [faceHolonomy_append_edges, faceHolonomy_revEdgePath, mul_assoc]

/-! ## 5. Exact Non-Abelian Yekutieli Stokes Identity on $\Sigma_{\mathrm{Bring}}$ -/

set_option maxRecDepth 8192 in
/-- Master free-group surface-cut word equality on `Fin 60 × Bool`: the concatenation of
all 24 rooted pentagon kite loops freely reduces to the exact same reduced 58-edge word as
the concatenation of the 4 handle commutator loops. -/
theorem bring_freeReduce_kites_eq_commutators :
    freeReduce ((List.finRange 24).flatMap yekutieliKiteLoop) =
      freeReduce ((List.finRange 4).flatMap handleCommLoop) := by
  decide

/-- Helper: `faceHolonomy` of `l.flatMap f` equals the ordered list product `(l.map ...).prod`. -/
theorem faceHolonomy_flatMap {α G : Type*} [Group G] (U : Fin 60 → G)
    (l : List α) (f : α → List (Fin 60 × Bool)) :
    faceHolonomy U (l.flatMap f) = (l.map (fun x => faceHolonomy U (f x))).prod := by
  induction l with
  | nil => rfl
  | cons hd tl ih =>
    rw [List.flatMap_cons, faceHolonomy_append_edges, List.map_cons, List.prod_cons, ih]

/-- **THE GLOBAL NON-ABELIAN YEKUTIELI STOKES THEOREM ON BRING'S SURFACE.**

Over an **arbitrary non-abelian `[Group G]`** and for **any** edge connection
`U : Fin 60 → G` on the 60 edges of Bring's `{5, 4}` tessellation, the ordered product
of the 24 rooted pentagon kite holonomies equals the genus-4 fundamental-polygon
boundary commutator product $\prod_{j=0}^3 [a_j, b_j]$ in `G`:
$$\prod_{k=0}^{23} \mathrm{yekutieliKiteHol}(U, k) = [a_0, b_0] \cdot [a_1, b_1] \cdot [a_2, b_2] \cdot [a_3, b_3].$$
This discharges the exact formalisation target noted in `DECYekutieliStokes.lean` (lines 41–45). -/
theorem bring_yekutieli_nonabelian_stokes {G : Type*} [Group G] (U : Fin 60 → G) :
    ((List.finRange 24).map (yekutieliKiteHol U)).prod =
      groupComm (handleHolA U 0) (handleHolB U 0) *
      groupComm (handleHolA U 1) (handleHolB U 1) *
      groupComm (handleHolA U 2) (handleHolB U 2) *
      groupComm (handleHolA U 3) (handleHolB U 3) := by
  have hL : ((List.finRange 24).map (yekutieliKiteHol U)).prod =
      faceHolonomy U ((List.finRange 24).flatMap yekutieliKiteLoop) := by
    rw [faceHolonomy_flatMap]
    congr 2
    funext k
    exact yekutieliKiteHol_eq_loop U k
  have hR : faceHolonomy U ((List.finRange 4).flatMap handleCommLoop) =
      groupComm (handleHolA U 0) (handleHolB U 0) *
      groupComm (handleHolA U 1) (handleHolB U 1) *
      groupComm (handleHolA U 2) (handleHolB U 2) *
      groupComm (handleHolA U 3) (handleHolB U 3) := by
    rw [faceHolonomy_flatMap]
    have h4 : List.finRange 4 = [0, 1, 2, 3] := by decide
    rw [h4]
    simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, mul_one,
      faceHolonomy_handleCommLoop, mul_assoc]
  rw [hL, ← faceHolonomy_freeReduce U, bring_freeReduce_kites_eq_commutators,
    faceHolonomy_freeReduce U, hR]

/-- **Flat-bundle corollary:** whenever the 8 handle holonomies satisfy the surface
commutator relation $\prod_{j=0}^3 [a_j, b_j] = 1$ (in particular for any flat bundle on
closed $\Sigma_{\mathrm{Bring}}$), the ordered 24-pentagon kite product equals `1`. -/
theorem bring_yekutieli_stokes_of_flat_handles {G : Type*} [Group G] (U : Fin 60 → G)
    (hflat : groupComm (handleHolA U 0) (handleHolB U 0) *
      groupComm (handleHolA U 1) (handleHolB U 1) *
      groupComm (handleHolA U 2) (handleHolB U 2) *
      groupComm (handleHolA U 3) (handleHolB U 3) = 1) :
    ((List.finRange 24).map (yekutieliKiteHol U)).prod = 1 := by
  rw [bring_yekutieli_nonabelian_stokes, hflat]

/-- Explicit non-abelian `Perm (Fin 3)` lattice gauge connection on Bring's 60 edges
witnessing that the genus-4 commutator RHS is genuinely non-trivial on non-flat connections. -/
def nonflatConnS3 (e : Fin 60) : Equiv.Perm (Fin 3) :=
  if e.val = 3 then Equiv.swap 0 1
  else if e.val = 5 then Equiv.swap 1 2
  else 1

set_option maxRecDepth 8192 in
/-- **Non-vacuity witness (`Perm (Fin 3)`):** on `nonflatConnS3`, the ordered 24-pentagon
kite holonomy product and the 4-handle commutator product are equal and **strictly `≠ 1`**,
demonstrating the genuine non-abelian commutator obstruction on closed genus-4 $\Sigma_{\mathrm{Bring}}$. -/
theorem bring_nonabelian_stokes_nonflat_perm3 :
    ((List.finRange 24).map (yekutieliKiteHol nonflatConnS3)).prod ≠ 1 ∧
    groupComm (handleHolA nonflatConnS3 0) (handleHolB nonflatConnS3 0) *
      groupComm (handleHolA nonflatConnS3 1) (handleHolB nonflatConnS3 1) *
      groupComm (handleHolA nonflatConnS3 2) (handleHolB nonflatConnS3 2) *
      groupComm (handleHolA nonflatConnS3 3) (handleHolB nonflatConnS3 3) ≠ 1 := by
  have hne : groupComm (handleHolA nonflatConnS3 0) (handleHolB nonflatConnS3 0) *
      groupComm (handleHolA nonflatConnS3 1) (handleHolB nonflatConnS3 1) *
      groupComm (handleHolA nonflatConnS3 2) (handleHolB nonflatConnS3 2) *
      groupComm (handleHolA nonflatConnS3 3) (handleHolB nonflatConnS3 3) ≠ 1 := by
    intro heq
    have h0 : (groupComm (handleHolA nonflatConnS3 0) (handleHolB nonflatConnS3 0) *
      groupComm (handleHolA nonflatConnS3 1) (handleHolB nonflatConnS3 1) *
      groupComm (handleHolA nonflatConnS3 2) (handleHolB nonflatConnS3 2) *
      groupComm (handleHolA nonflatConnS3 3) (handleHolB nonflatConnS3 3)) (0 : Fin 3) = 0 := by
      rw [heq]; rfl
    revert h0; decide
  exact ⟨by rw [bring_yekutieli_nonabelian_stokes]; exact hne, hne⟩

/-! ## 6. Exact Abelian Specialisation (`Multiplicative R`) and DEC Cochain Stokes -/

section AbelianAndDEC

/-- In any commutative group `CommGroup G`, every kite conjugation cancels
(`yekutieliKiteHol U k = faceHolonomy U (pentagonCycle (kiteFace k))`) and every handle
commutator vanishes (`groupComm a b = 1`), so the product of all 24 pentagon face
holonomies equals `1`. -/
theorem bring_commGroup_stokes {G : Type*} [CommGroup G] (U : Fin 60 → G) :
    ∏ f : Fin 24, faceHolonomy U (pentagonCycle f) = 1 := by
  have hk : yekutieliKiteHol U = fun k => faceHolonomy U (pentagonCycle (kiteFace k)) := by
    funext k
    unfold yekutieliKiteHol
    rw [mul_comm (faceHolonomy U (kiteWhisker k)), mul_assoc, mul_inv_cancel, mul_one]
  have hcomm : ∀ a b : G, groupComm a b = 1 := by
    intro a b
    unfold groupComm
    rw [mul_comm a b, mul_assoc b a, mul_inv_cancel, mul_one, mul_inv_cancel]
  have hmain := bring_yekutieli_nonabelian_stokes U
  rw [hk] at hmain
  simp only [hcomm, mul_one] at hmain
  have hprod : (∏ k : Fin 24, faceHolonomy U (pentagonCycle (kiteFace k))) =
      ((List.finRange 24).map (fun k => faceHolonomy U (pentagonCycle (kiteFace k)))).prod := by
    rw [← Fin.prod_univ_def]
  let e := Equiv.ofBijective kiteFace kiteFace_bijective
  calc
    ∏ f : Fin 24, faceHolonomy U (pentagonCycle f)
        = ∏ k : Fin 24, faceHolonomy U (pentagonCycle (e k)) :=
          (Equiv.prod_comp e (fun f => faceHolonomy U (pentagonCycle f))).symm
    _ = ∏ k : Fin 24, faceHolonomy U (pentagonCycle (kiteFace k)) := rfl
    _ = ((List.finRange 24).map (fun k => faceHolonomy U (pentagonCycle (kiteFace k)))).prod := hprod
    _ = 1 := hmain

variable {R : Type*} [CommRing R]

/-- Coboundary `d₀ : C⁰ → C¹` (`Fin 60 × Fin 30`) on Bring's 1-skeleton over `[CommRing R]`. -/
def bringD0 : Matrix (Fin 60) (Fin 30) R :=
  fun e v =>
    (if edgeHead (e, true) = v then (1 : R) else 0) -
    (if edgeTail (e, true) = v then (1 : R) else 0)

/-- Coboundary `d₁ : C¹ → C²` (`Fin 24 × Fin 60`) read directly off `pentagonCycle` via `incid`. -/
def bringD1 : Matrix (Fin 24) (Fin 60) R :=
  fun f e => incid (pentagonCycle f) e

/-- For any oriented edge `es : Fin 60 × Bool` and vertex `v₀ : Fin 30`, the signed
coboundary value `signedVal (fun e => bringD0 e v₀) es` equals the oriented endpoint
difference `δ(edgeHead es, v₀) - δ(edgeTail es, v₀)`. -/
theorem signedVal_bringD0_eq (v₀ : Fin 30) (es : Fin 60 × Bool) :
    signedVal (fun e => bringD0 (R := R) e v₀) es =
      (if edgeHead es = v₀ then (1 : R) else 0) - (if edgeTail es = v₀ then (1 : R) else 0) := by
  rcases es with ⟨e, b⟩
  cases b <;> simp [signedVal, bringD0, edgeHead, edgeTail]

/-- Telescoping of `signedVal (fun e => bringD0 e v₀)` along any valid edge walk `w` from `u` to `v`. -/
theorem sum_signedVal_bringD0_walk (v₀ : Fin 30) :
    ∀ (w : List (Fin 60 × Bool)) (u v : Fin 30),
      isEdgeWalk u v w = true →
      (w.map (signedVal (fun e => bringD0 (R := R) e v₀))).sum =
        (if v = v₀ then (1 : R) else 0) - (if u = v₀ then (1 : R) else 0)
  | [], u, v, hw => by
    simp only [isEdgeWalk, beq_iff_eq] at hw
    subst hw
    simp
  | es :: rest, u, v, hw => by
    simp only [isEdgeWalk, Bool.and_eq_true, beq_iff_eq] at hw
    rcases hw with ⟨htu, hrest⟩
    rw [List.map_cons, List.sum_cons, signedVal_bringD0_eq,
      sum_signedVal_bringD0_walk v₀ rest (edgeHead es) v hrest, htu]
    ring

/-- **Exact cochain complex property `d₁ * d₀ = 0` over any `[CommRing R]`:**
on every pentagon `f : Fin 24`, `(d₁ d₀)_{f, v₀}` telescopes around the closed 5-edge
walk `pentagonCycle f` to `0`. -/
theorem bringD1_mul_bringD0 : (bringD1 (R := R)) * (bringD0 (R := R)) = 0 := by
  ext f v₀
  simp only [Matrix.mul_apply, Matrix.zero_apply, bringD1]
  rw [← sum_signedVal_eq (fun e => bringD0 (R := R) e v₀) (pentagonCycle f)]
  rw [sum_signedVal_bringD0_walk v₀ (pentagonCycle f) (pentagonBaseVert f)
    (pentagonBaseVert f) (isClosedWalk_pentagonCycle f).2]
  ring

/-- Concrete instantiation of `QOU.FluidDynamics.DEC.Complex2` on Bring's $(30, 60, 24)$
regular pentagon tessellation over any `[CommRing R]`. -/
def bringDECComplex2 : QOU.FluidDynamics.DEC.Complex2 R (Fin 30) (Fin 60) (Fin 24) where
  d0 := bringD0
  d1 := bringD1
  dd := bringD1_mul_bringD0

/-- **Abelian Specialisation (`G = Multiplicative R`) → Discrete DEC Stokes Theorem on $\Sigma_{\mathrm{Bring}}$:**
applying `bring_yekutieli_nonabelian_stokes` (`bring_commGroup_stokes`) to the abelian
connection `e ↦ Multiplicative.ofAdd (v e)` immediately yields
$$\sum_{f \in \mathrm{Fin}\,24} (\mathrm{bringDECComplex2.vort}\;v\;f) = 0$$
for every 1-cochain `v : Fin 60 → R` over any `[CommRing R]`. -/
theorem bring_discrete_stokes_vort_sum_eq_zero (v : Fin 60 → R) :
    ∑ f : Fin 24, (bringDECComplex2 (R := R)).vort v f = 0 := by
  have h := bring_commGroup_stokes (fun e => Multiplicative.ofAdd (v e))
  have hvort : ∀ f : Fin 24,
      faceHolonomy (fun e => Multiplicative.ofAdd (v e)) (pentagonCycle f) =
        Multiplicative.ofAdd ((bringDECComplex2 (R := R)).vort v f) := by
    intro f
    exact faceHolonomy_eq_vort (bringDECComplex2 (R := R)) pentagonCycle (fun _ _ => rfl) v f
  simp only [hvort] at h
  rw [← ofAdd_sum] at h
  exact Multiplicative.ofAdd.injective h

end AbelianAndDEC

end QOU.FluidDynamics.BringTessellationNonAbelianStokes
