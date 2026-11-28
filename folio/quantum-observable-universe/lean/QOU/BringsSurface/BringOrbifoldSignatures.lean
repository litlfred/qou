import QOU.BringsSurface.BringSymmetryQuotientGenus
import QOU.BringsSurface.BringHarmonicTypes

/-!
# Orbifold signatures of the symmetry quotients of Bring's surface

Bean `qou-u81q` (owner card 2026-11-28, "Both": with the exact discrete sunset). For every
conjugacy class of subgroups `H ≤ S₅` (19 classes, `SymmetryQuotientGenus.subgroupClasses`) this
file records the orbifold `B/H` and the non-orientable orbifold `B/(H × ⟨c⟩)`, where `c` is the
central reflection (complex conjugation, `BringReflectionParity.lean`). So the 14 quotients used to
recover the parity types (`parity_types_from_quotient_spectra`) are rows `9, 13, 14, 15, 16, 17,
18` of each table.

## Signatures

`B/H` (orientable, no boundary). Genus from `quotient_genus_table`; cone points:

| `H` | `B/H` | `H` | `B/H` |
|---|---|---|---|
| `1` | `(4; −)` | `S₃` | `(0; 2,2,2,2,2,2)` |
| `⟨(01)(23)⟩` | `(2; 2,2)` | `S₃` twisted | `(1; 2,2)` |
| `⟨(01)⟩` | `(1; 2⁶)` | `D₄` | `(0; 2,2,2,2,4)` |
| `C₃` | `(2; −)` | `D₅` | `(0; 2,2,5,5)` |
| `⟨(01),(23)⟩` | `(0; 2⁷)` | `S₃ × S₂` | `(0; 2,2,2,2,2)` |
| `V₄` | `(1; 2,2,2)` | `A₄` | `(1; 2)` |
| `C₄` | `(1; 4,4)` | `F₂₀` | `(0; 4,4,5)` |
| `C₅` | `(0; 5,5,5,5)` | `S₄` | `(0; 2,2,2,4)` |
| `C₆` | `(1; 2,2)` | `A₅` | `(0; 2,5,5)` |
| | | `S₅` | `(0; 2,4,5)` |

`B/(H × ⟨c⟩)`: see `sigRefl`. Every quotient with boundary has exactly one boundary curve, which
is a chain of mirrors. For example `B/(S₅ × c)` is the `(2,4,5)` triangle (a disc with corner
reflectors `2,4,5`), `B/(A₅ × c)` a disc with corners `2,5,5`, `B/(A₄ × c)` a Möbius band with one
corner `2`, `B/c` the closed surface with five cross-caps, and `B/(C₃ × c)`, `B/(C₅ × c)` closed
non-orientable surfaces (three cross-caps; one cross-cap with cones `5,5`).

## What is proved

* `cone_orders_derived`: the cone points of every `B/H` follow from the class distribution of `H`
  and the fixed-cell counts (`chiC0`, `chiC1`, `chiC2` of `BringHarmonicTypes`). A cell's
  stabiliser is cyclic: `C₄` (a conjugate of `⟨S⟩`) at a vertex, `C₂` (a transposition, which
  reverses the edge) at an edge, `C₅` at a face. If `n_d` cells have an `H`-stabiliser of order
  `d`, they form `d n_d / |H|` cone points of order `d`, and `n_d` is a sum of fixed-point counts
  over the elements of `H` (Burnside). All counts are integers (`cone_counts_integral`).
* `genus_agrees`: the underlying surfaces have the genera of `quotient_genus_table`.
* `orbifold_rh_orient`, `orbifold_rh_refl`: the orbifold Euler characteristic is `−6/|H|` and
  `−3/|H|` respectively, `χ(X) − Σ (1 − 1/m) − ½ Σ (1 − 1/n) = χ(B)/|K|`, for all 38 rows.
* `boundary_iff_reflection`: `B/(H × c)` has a mirror exactly when `H` contains a transposition or
  a double transposition, the only `g` for which `(g, c)` fixes a point (`rev_vertex_count`,
  `rev_edge_counts`).
* `underlying_surfaces`: each underlying surface is a valid compact surface: `2 − χ − b` is even
  and nonnegative when orientable, positive when not.

## Inputs, cited

The two tables are computed by `computations/probes/bring_orbifold_signatures_probe.py`, which
builds the `(2,4,5)` barycentric triangulation (240 triangles, on which `S₅ × C₂` acts simply
transitively) and takes the quotient complex: orbits of cells, stabilisers, mirror edges,
2-colouring for orientability. The `B/(H × c)` table is data checked here for consistency, not
derived in Lean. Burnside's lemma and the orbifold Euler characteristic (Thurston) are cited.
No empirical value enters.

-- Ref: [thurston1980] W. P. Thurston, *The Geometry and Topology of Three-Manifolds*, ch. 13.
-/

namespace QOU.Brings.OrbifoldSignatures

open QOU.Brings.HarmonicTypes QOU.Brings.SymmetryQuotientGenus

/-- `B/H` for the 19 classes, in the order of `subgroupClasses`: (χ of the underlying surface,
orientable, boundary components, cone orders, corner-reflector orders). From the probe. -/
def sigOrient : List (ℤ × Bool × ℕ × List ℕ × List ℕ) :=
  [(-6, true, 0, [], []),  -- 1
    (-2, true, 0, [2, 2], []),  -- <(01)(23)>
    (0, true, 0, [2, 2, 2, 2, 2, 2], []),  -- <(01)>
    (-2, true, 0, [], []),  -- C3
    (2, true, 0, [2, 2, 2, 2, 2, 2, 2], []),  -- <(01),(23)>
    (0, true, 0, [2, 2, 2], []),  -- V4
    (0, true, 0, [4, 4], []),  -- C4
    (2, true, 0, [5, 5, 5, 5], []),  -- C5
    (0, true, 0, [2, 2], []),  -- C6
    (2, true, 0, [2, 2, 2, 2, 2, 2], []),  -- S3
    (0, true, 0, [2, 2], []),  -- S3tw
    (2, true, 0, [2, 2, 2, 2, 4], []),  -- D4
    (2, true, 0, [2, 2, 5, 5], []),  -- D5
    (2, true, 0, [2, 2, 2, 2, 2], []),  -- S3xS2
    (0, true, 0, [2], []),  -- A4
    (2, true, 0, [4, 4, 5], []),  -- F20
    (2, true, 0, [2, 2, 2, 4], []),  -- S4
    (2, true, 0, [2, 5, 5], []),  -- A5
    (2, true, 0, [2, 4, 5], [])]  -- S5

/-- `B/(H × ⟨c⟩)` for the 19 classes, same format. From the probe. -/
def sigRefl : List (ℤ × Bool × ℕ × List ℕ × List ℕ) :=
  [(-3, false, 0, [], []),  -- 1 × c
    (-1, false, 1, [2], []),  -- <(01)(23)> × c
    (0, false, 1, [2, 2, 2], []),  -- <(01)> × c
    (-1, false, 0, [], []),  -- C3 × c
    (1, true, 1, [2, 2], [2, 2, 2]),  -- <(01),(23)> × c
    (0, false, 1, [], [2, 2, 2]),  -- V4 × c
    (0, false, 1, [4], []),  -- C4 × c
    (1, false, 0, [5, 5], []),  -- C5 × c
    (0, false, 1, [2], []),  -- C6 × c
    (1, true, 1, [2, 2, 2], []),  -- S3 × c
    (0, false, 1, [2], []),  -- S3tw × c
    (1, true, 1, [2], [2, 2, 4]),  -- D4 × c
    (1, true, 1, [2], [5, 5]),  -- D5 × c
    (1, true, 1, [2], [2, 2, 2]),  -- S3xS2 × c
    (0, false, 1, [], [2]),  -- A4 × c
    (1, true, 1, [4], [5]),  -- F20 × c
    (1, true, 1, [2], [2, 4]),  -- S4 × c
    (1, true, 1, [], [2, 5, 5]),  -- A5 × c
    (1, true, 1, [], [2, 4, 5])]  -- S5 × c

/-! ## The orientable quotients: cone points from fixed-point counts -/

/-- Cells with stabiliser exactly of order `d`, from fixed-point counts over `H` (class
distribution `k`): `n₄ = k₄·fix(4-cycle)/2` (each `C₄` has two generators), `n₂^V =
k_{(22)}·fix_V((22)) − n₄` (each `C₄` contains one double transposition), `n₂^E =
k_{(2)}·|chiC1 (2)|` (a transposition reverses each edge it fixes), `n₅ = k₅·fix(5-cycle)/4`. -/
def cellCounts (k : Fin 7 → ℤ) : ℤ × ℤ × ℤ × ℤ :=
  let n4 := k 5 * chiC0 5 / 2
  (k 2 * chiC0 2 - n4, n4, k 1 * (-chiC1 1), k 6 * chiC2 6 / 4)

/-- Cone points: `d n_d / |H|` of order `d`. -/
def coneOrders (o : ℕ) (k : Fin 7 → ℤ) : List ℕ :=
  let n := cellCounts k
  List.replicate (2 * n.1 / o + 2 * n.2.2.1 / o).toNat 2 ++ List.replicate (4 * n.2.1 / o).toNat 4 ++
    List.replicate (5 * n.2.2.2 / o).toNat 5

theorem cone_counts_integral :
    subgroupClasses.all (fun p => let n := cellCounts p.2
      decide ((p.1 : ℤ) ∣ 2 * n.1 ∧ (p.1 : ℤ) ∣ 2 * n.2.2.1 ∧ (p.1 : ℤ) ∣ 4 * n.2.1 ∧
        (p.1 : ℤ) ∣ 5 * n.2.2.2 ∧ 2 ∣ p.2 5 * chiC0 5 ∧ 4 ∣ p.2 6 * chiC2 6)) = true := by
  decide

/-- **The cone points of every `B/H`, derived.** -/
theorem cone_orders_derived :
    subgroupClasses.map (fun p => coneOrders p.1 p.2) = sigOrient.map (·.2.2.2.1) := by
  decide

/-- The underlying surfaces of `B/H` are closed, orientable, of the genera in
`quotient_genus_table`: `|H| (2 − χ) = 2 fixedSum`. -/
theorem genus_agrees :
    (List.zipWith (fun p s => decide ((p.1 : ℤ) * (2 - s.1) = 2 * fixedSum p.2 ∧ s.2.1 = true ∧
      s.2.2.1 = 0 ∧ s.2.2.2.2 = [])) subgroupClasses sigOrient).all id = true := by
  decide

/-- `20 (1 − 1/m)` for `m = 2, 4, 5`. -/
def w20 (m : ℕ) : ℤ := 20 - 20 / (m : ℤ)

/-- **Orbifold Riemann–Hurwitz for `B/H`**: `|H| · 20 χ^orb = 20 χ(B) = −120`. -/
theorem orbifold_rh_orient :
    (List.zipWith (fun p s => decide ((p.1 : ℤ) * (20 * s.1 - (s.2.2.2.1.map w20).sum) = -120))
      subgroupClasses sigOrient).all id = true := by
  decide

/-- **Orbifold Euler characteristic for `B/(H × c)`**: `2|H| · χ^orb = χ(B) = −6`, with corner
reflectors counted half: `|H| (40 χ − 2 Σ_cones w − Σ_corners w) = −120`. -/
theorem orbifold_rh_refl :
    (List.zipWith (fun p s => decide ((p.1 : ℤ) *
      (40 * s.1 - 2 * (s.2.2.2.1.map w20).sum - (s.2.2.2.2.map w20).sum) = -120))
      subgroupClasses sigRefl).all id = true := by
  decide

/-- **A mirror occurs exactly when `H` has a transposition or a double transposition.** -/
theorem boundary_iff_reflection :
    (List.zipWith (fun p s => decide ((0 < s.2.2.1) ↔ (0 < p.2 1 + p.2 2))) subgroupClasses
      sigRefl).all id = true := by
  decide

/-- **Valid underlying surfaces.** With `h = 2 − χ − b`: orientable needs `h` even and `≥ 0`
(`h = 2g`), non-orientable needs `h ≥ 1` (`h` cross-caps). -/
theorem underlying_surfaces :
    ((sigOrient ++ sigRefl).all fun s => let h := 2 - s.1 - (s.2.2.1 : ℤ)
      if s.2.1 then decide (0 ≤ h ∧ 2 ∣ h) else decide (1 ≤ h)) = true := by
  decide

/-- `B/(S₅ × c)` is the `(2,4,5)` triangle: a disc (`χ = 1`, one boundary curve) with corner
reflectors `2, 4, 5` and no cone point. -/
theorem full_quotient_is_triangle : sigRefl.getLast? = some (1, true, 1, [], [2, 4, 5]) := by
  decide

end QOU.Brings.OrbifoldSignatures
