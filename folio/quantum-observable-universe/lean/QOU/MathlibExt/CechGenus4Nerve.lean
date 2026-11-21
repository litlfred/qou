import Mathlib.Data.Fin.VecNotation
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Algebra.Module.BigOperators
import Mathlib.Tactic.Abel

/-!
# The nerve of a genus-4 triangulation: `H²` by the oriented face sum (route R3, step S1b)

A fixed closed oriented triangulated surface of genus 4: four 7-vertex tori glued
by connected sum along faces. 19 vertices, 75 edges, 50 faces, so
`χ = 19 − 75 + 50 = −6`. The data were generated and checked (simplicial, every
edge in exactly two faces, every vertex link a single cycle, consistently
oriented) by `computations/probes/genus4_connected_sum_triangulation.py`; the
facts used below are re-checked here by the kernel.

On one value per oriented face, `φ : Fin 50 → A` (any additive commutative
group `A`), this file proves the two halves of `H² ≅ A` for the
alternating complex:

## Results, all sorry-free

* `cert`: an integer certificate, checked by `decide +kernel`: for each face
  `g`, a signed path of edges in the dual graph to face `0` whose coboundary is
  `[g] − [0]`.
* `exists_cob_of_sum_zero`: if `Σ_f φ f = 0`, then `φ` is the coboundary of an
  antisymmetric function on pairs of vertices.
* `sum_cob_eq_zero`: conversely, the coboundary of any antisymmetric function on
  pairs has face sum `0` (each edge lies in two faces with opposite
  orientations).

So the face sum `φ ↦ Σ_f φ f` is well defined on classes and injective. It is
onto because `φ = [f₀]·g` has sum `g`.

## What this does NOT do

It is combinatorics only. It does not yet say that these faces are the nerve of
an open cover of a topological genus-4 surface (step S2), nor compare with the
colimit `Ȟ²` (steps S3–S4). Bean `qou-skn4`.

-- Ref: [leitner2026] lifting-and-descent, route R3, surface step S1
-/

namespace QOU.CentralExtension.Cech.Genus4

def fA : Fin 50 → Fin 19 := ![1, 2, 3, 4, 5, 6, 3, 4, 5, 6, 0, 1, 2, 1, 7, 0, 8, 9, 10, 0, 8, 9, 10, 3, 1, 1, 11, 7, 12, 13, 14, 7, 12, 13, 14, 10, 1, 1, 15, 11, 16, 17, 18, 11, 16, 17, 18, 14, 1, 15]

def fB : Fin 50 → Fin 19 := ![2, 3, 4, 5, 6, 0, 2, 3, 4, 5, 6, 0, 1, 7, 0, 8, 9, 10, 3, 7, 0, 8, 9, 10, 3, 11, 7, 12, 13, 14, 10, 11, 7, 12, 13, 14, 10, 15, 11, 16, 17, 18, 14, 15, 11, 16, 17, 18, 14, 1]

def fC : Fin 50 → Fin 19 := ![4, 5, 6, 0, 1, 2, 0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 3, 1, 7, 3, 1, 7, 0, 8, 9, 12, 13, 14, 10, 1, 11, 10, 1, 11, 7, 12, 13, 16, 17, 18, 14, 1, 15, 14, 1, 15, 11, 16, 17, 18]

def eA : Fin 75 → Fin 19 := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 12, 12, 13, 14, 14, 14, 14, 15, 15, 15, 16, 16, 17]

def eB : Fin 75 → Fin 19 := ![1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 3, 4, 5, 6, 4, 5, 6, 7, 8, 9, 10, 5, 6, 6, 8, 9, 10, 11, 12, 13, 14, 9, 10, 10, 11, 12, 13, 14, 12, 13, 14, 15, 16, 17, 18, 13, 14, 14, 15, 16, 17, 18, 16, 17, 18, 17, 18, 18]

def paths : Fin 50 → List (Fin 75 × ℤ) := ![[],
  [((29 : Fin 75), (-1 : ℤ)), ((28 : Fin 75), (-1 : ℤ))],
  [((31 : Fin 75), (1 : ℤ)), ((12 : Fin 75), (1 : ℤ))],
  [((38 : Fin 75), (1 : ℤ)), ((28 : Fin 75), (-1 : ℤ))],
  [((14 : Fin 75), (-1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((30 : Fin 75), (1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((1 : Fin 75), (-1 : ℤ)), ((30 : Fin 75), (1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((12 : Fin 75), (1 : ℤ))],
  [((28 : Fin 75), (-1 : ℤ))],
  [((40 : Fin 75), (-1 : ℤ)), ((14 : Fin 75), (-1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((5 : Fin 75), (1 : ℤ)), ((30 : Fin 75), (1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((13 : Fin 75), (-1 : ℤ)), ((14 : Fin 75), (-1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((10 : Fin 75), (-1 : ℤ))],
  [((16 : Fin 75), (-1 : ℤ)), ((0 : Fin 75), (1 : ℤ)), ((13 : Fin 75), (-1 : ℤ)), ((14 : Fin 75), (-1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((6 : Fin 75), (-1 : ℤ)), ((2 : Fin 75), (-1 : ℤ)), ((1 : Fin 75), (-1 : ℤ)), ((30 : Fin 75), (1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((7 : Fin 75), (1 : ℤ)), ((0 : Fin 75), (1 : ℤ)), ((13 : Fin 75), (-1 : ℤ)), ((14 : Fin 75), (-1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((36 : Fin 75), (-1 : ℤ)), ((11 : Fin 75), (1 : ℤ)), ((12 : Fin 75), (1 : ℤ))],
  [((17 : Fin 75), (1 : ℤ)), ((11 : Fin 75), (1 : ℤ)), ((12 : Fin 75), (1 : ℤ))],
  [((34 : Fin 75), (1 : ℤ)), ((2 : Fin 75), (-1 : ℤ)), ((1 : Fin 75), (-1 : ℤ)), ((30 : Fin 75), (1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((2 : Fin 75), (-1 : ℤ)), ((1 : Fin 75), (-1 : ℤ)), ((30 : Fin 75), (1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((0 : Fin 75), (1 : ℤ)), ((13 : Fin 75), (-1 : ℤ)), ((14 : Fin 75), (-1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((48 : Fin 75), (-1 : ℤ)), ((36 : Fin 75), (-1 : ℤ)), ((11 : Fin 75), (1 : ℤ)), ((12 : Fin 75), (1 : ℤ))],
  [((50 : Fin 75), (-1 : ℤ)), ((17 : Fin 75), (1 : ℤ)), ((11 : Fin 75), (1 : ℤ)), ((12 : Fin 75), (1 : ℤ))],
  [((35 : Fin 75), (-1 : ℤ)), ((36 : Fin 75), (-1 : ℤ)), ((11 : Fin 75), (1 : ℤ)), ((12 : Fin 75), (1 : ℤ))],
  [((11 : Fin 75), (1 : ℤ)), ((12 : Fin 75), (1 : ℤ))],
  [((20 : Fin 75), (-1 : ℤ)), ((15 : Fin 75), (-1 : ℤ)), ((16 : Fin 75), (-1 : ℤ)), ((0 : Fin 75), (1 : ℤ)), ((13 : Fin 75), (-1 : ℤ)), ((14 : Fin 75), (-1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((44 : Fin 75), (-1 : ℤ)), ((43 : Fin 75), (-1 : ℤ)), ((34 : Fin 75), (1 : ℤ)), ((2 : Fin 75), (-1 : ℤ)), ((1 : Fin 75), (-1 : ℤ)), ((30 : Fin 75), (1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((45 : Fin 75), (1 : ℤ)), ((15 : Fin 75), (-1 : ℤ)), ((16 : Fin 75), (-1 : ℤ)), ((0 : Fin 75), (1 : ℤ)), ((13 : Fin 75), (-1 : ℤ)), ((14 : Fin 75), (-1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((53 : Fin 75), (-1 : ℤ)), ((18 : Fin 75), (1 : ℤ)), ((17 : Fin 75), (1 : ℤ)), ((11 : Fin 75), (1 : ℤ)), ((12 : Fin 75), (1 : ℤ))],
  [((21 : Fin 75), (1 : ℤ)), ((18 : Fin 75), (1 : ℤ)), ((17 : Fin 75), (1 : ℤ)), ((11 : Fin 75), (1 : ℤ)), ((12 : Fin 75), (1 : ℤ))],
  [((51 : Fin 75), (1 : ℤ)), ((43 : Fin 75), (-1 : ℤ)), ((34 : Fin 75), (1 : ℤ)), ((2 : Fin 75), (-1 : ℤ)), ((1 : Fin 75), (-1 : ℤ)), ((30 : Fin 75), (1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((43 : Fin 75), (-1 : ℤ)), ((34 : Fin 75), (1 : ℤ)), ((2 : Fin 75), (-1 : ℤ)), ((1 : Fin 75), (-1 : ℤ)), ((30 : Fin 75), (1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((15 : Fin 75), (-1 : ℤ)), ((16 : Fin 75), (-1 : ℤ)), ((0 : Fin 75), (1 : ℤ)), ((13 : Fin 75), (-1 : ℤ)), ((14 : Fin 75), (-1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((62 : Fin 75), (-1 : ℤ)), ((53 : Fin 75), (-1 : ℤ)), ((18 : Fin 75), (1 : ℤ)), ((17 : Fin 75), (1 : ℤ)), ((11 : Fin 75), (1 : ℤ)), ((12 : Fin 75), (1 : ℤ))],
  [((64 : Fin 75), (-1 : ℤ)), ((21 : Fin 75), (1 : ℤ)), ((18 : Fin 75), (1 : ℤ)), ((17 : Fin 75), (1 : ℤ)), ((11 : Fin 75), (1 : ℤ)), ((12 : Fin 75), (1 : ℤ))],
  [((52 : Fin 75), (-1 : ℤ)), ((53 : Fin 75), (-1 : ℤ)), ((18 : Fin 75), (1 : ℤ)), ((17 : Fin 75), (1 : ℤ)), ((11 : Fin 75), (1 : ℤ)), ((12 : Fin 75), (1 : ℤ))],
  [((18 : Fin 75), (1 : ℤ)), ((17 : Fin 75), (1 : ℤ)), ((11 : Fin 75), (1 : ℤ)), ((12 : Fin 75), (1 : ℤ))],
  [((24 : Fin 75), (-1 : ℤ)), ((19 : Fin 75), (-1 : ℤ)), ((20 : Fin 75), (-1 : ℤ)), ((15 : Fin 75), (-1 : ℤ)), ((16 : Fin 75), (-1 : ℤ)), ((0 : Fin 75), (1 : ℤ)), ((13 : Fin 75), (-1 : ℤ)), ((14 : Fin 75), (-1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((58 : Fin 75), (-1 : ℤ)), ((57 : Fin 75), (-1 : ℤ)), ((51 : Fin 75), (1 : ℤ)), ((43 : Fin 75), (-1 : ℤ)), ((34 : Fin 75), (1 : ℤ)), ((2 : Fin 75), (-1 : ℤ)), ((1 : Fin 75), (-1 : ℤ)), ((30 : Fin 75), (1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((59 : Fin 75), (1 : ℤ)), ((19 : Fin 75), (-1 : ℤ)), ((20 : Fin 75), (-1 : ℤ)), ((15 : Fin 75), (-1 : ℤ)), ((16 : Fin 75), (-1 : ℤ)), ((0 : Fin 75), (1 : ℤ)), ((13 : Fin 75), (-1 : ℤ)), ((14 : Fin 75), (-1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((67 : Fin 75), (-1 : ℤ)), ((22 : Fin 75), (1 : ℤ)), ((21 : Fin 75), (1 : ℤ)), ((18 : Fin 75), (1 : ℤ)), ((17 : Fin 75), (1 : ℤ)), ((11 : Fin 75), (1 : ℤ)), ((12 : Fin 75), (1 : ℤ))],
  [((25 : Fin 75), (1 : ℤ)), ((22 : Fin 75), (1 : ℤ)), ((21 : Fin 75), (1 : ℤ)), ((18 : Fin 75), (1 : ℤ)), ((17 : Fin 75), (1 : ℤ)), ((11 : Fin 75), (1 : ℤ)), ((12 : Fin 75), (1 : ℤ))],
  [((65 : Fin 75), (1 : ℤ)), ((57 : Fin 75), (-1 : ℤ)), ((51 : Fin 75), (1 : ℤ)), ((43 : Fin 75), (-1 : ℤ)), ((34 : Fin 75), (1 : ℤ)), ((2 : Fin 75), (-1 : ℤ)), ((1 : Fin 75), (-1 : ℤ)), ((30 : Fin 75), (1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((57 : Fin 75), (-1 : ℤ)), ((51 : Fin 75), (1 : ℤ)), ((43 : Fin 75), (-1 : ℤ)), ((34 : Fin 75), (1 : ℤ)), ((2 : Fin 75), (-1 : ℤ)), ((1 : Fin 75), (-1 : ℤ)), ((30 : Fin 75), (1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((19 : Fin 75), (-1 : ℤ)), ((20 : Fin 75), (-1 : ℤ)), ((15 : Fin 75), (-1 : ℤ)), ((16 : Fin 75), (-1 : ℤ)), ((0 : Fin 75), (1 : ℤ)), ((13 : Fin 75), (-1 : ℤ)), ((14 : Fin 75), (-1 : ℤ)), ((10 : Fin 75), (-1 : ℤ))],
  [((72 : Fin 75), (-1 : ℤ)), ((67 : Fin 75), (-1 : ℤ)), ((22 : Fin 75), (1 : ℤ)), ((21 : Fin 75), (1 : ℤ)), ((18 : Fin 75), (1 : ℤ)), ((17 : Fin 75), (1 : ℤ)), ((11 : Fin 75), (1 : ℤ)), ((12 : Fin 75), (1 : ℤ))],
  [((74 : Fin 75), (-1 : ℤ)), ((25 : Fin 75), (1 : ℤ)), ((22 : Fin 75), (1 : ℤ)), ((21 : Fin 75), (1 : ℤ)), ((18 : Fin 75), (1 : ℤ)), ((17 : Fin 75), (1 : ℤ)), ((11 : Fin 75), (1 : ℤ)), ((12 : Fin 75), (1 : ℤ))],
  [((66 : Fin 75), (-1 : ℤ)), ((67 : Fin 75), (-1 : ℤ)), ((22 : Fin 75), (1 : ℤ)), ((21 : Fin 75), (1 : ℤ)), ((18 : Fin 75), (1 : ℤ)), ((17 : Fin 75), (1 : ℤ)), ((11 : Fin 75), (1 : ℤ)), ((12 : Fin 75), (1 : ℤ))],
  [((22 : Fin 75), (1 : ℤ)), ((21 : Fin 75), (1 : ℤ)), ((18 : Fin 75), (1 : ℤ)), ((17 : Fin 75), (1 : ℤ)), ((11 : Fin 75), (1 : ℤ)), ((12 : Fin 75), (1 : ℤ))],
  [((26 : Fin 75), (1 : ℤ)), ((25 : Fin 75), (1 : ℤ)), ((22 : Fin 75), (1 : ℤ)), ((21 : Fin 75), (1 : ℤ)), ((18 : Fin 75), (1 : ℤ)), ((17 : Fin 75), (1 : ℤ)), ((11 : Fin 75), (1 : ℤ)), ((12 : Fin 75), (1 : ℤ))]]

/-- Incidence of the ordered pair `(x, y)` with edge `e`: `+1` if it is the edge
as listed, `−1` if reversed, `0` otherwise. -/
def inc (x y : Fin 19) (e : Fin 75) : ℤ :=
  if x = eA e ∧ y = eB e then 1 else if y = eA e ∧ x = eB e then -1 else 0

/-- Coboundary matrix: incidence of face `f` with edge `e`. -/
def D (f : Fin 50) (e : Fin 75) : ℤ :=
  inc (fA f) (fB f) e + inc (fB f) (fC f) e - inc (fA f) (fC f) e

def colSum (f g : Fin 50) : ℤ := ((paths g).map (fun p => p.2 * D f p.1)).sum

/-- **The certificate.** Coboundary of path `g` is `[g] − [0]`. -/
theorem cert : ∀ f g : Fin 50,
    colSum f g = (if f = g then 1 else 0) - (if f = 0 then 1 else 0) := by
  decide +kernel

/-- Every edge lies in two faces with opposite orientations. -/
theorem colD : ∀ e : Fin 75, ∑ f, D f e = 0 := by decide +kernel

theorem edge_ne : ∀ e : Fin 75, eA e ≠ eB e := by decide +kernel

/-- Each side of each face is exactly one listed edge. -/
theorem side_sq : ∀ f : Fin 50, (∑ e, inc (fA f) (fB f) e ^ 2) = 1 ∧
    (∑ e, inc (fB f) (fC f) e ^ 2) = 1 ∧ (∑ e, inc (fA f) (fC f) e ^ 2) = 1 := by
  decide +kernel

theorem inc_swap (x y : Fin 19) (e : Fin 75) : inc y x e = - inc x y e := by
  have he := edge_ne e
  unfold inc
  by_cases h1 : x = eA e ∧ y = eB e
  · obtain ⟨rfl, rfl⟩ := h1; simp [he, Ne.symm he]
  · by_cases h2 : y = eA e ∧ x = eB e
    · obtain ⟨rfl, rfl⟩ := h2; simp [he, Ne.symm he]
    · simp [h1, h2]

variable {A : Type*} [AddCommGroup A]

/-- Coefficient of edge `e` in path `g`. -/
def pc (g : Fin 50) (e : Fin 75) : ℤ :=
  ((paths g).map (fun p => if p.1 = e then p.2 else 0)).sum

theorem sum_D_mul_pc (f g : Fin 50) : ∑ e, D f e * pc g e = colSum f g := by
  unfold pc colSum
  induction paths g with
  | nil => simp
  | cons p L ih =>
    simp only [List.map_cons, List.sum_cons, mul_add, Finset.sum_add_distrib, ih]
    congr 1
    simp [mul_comm]

/-- Edge values of the primitive. -/
def W (φ : Fin 50 → A) (e : Fin 75) : A := ∑ g, pc g e • φ g

/-- The primitive on pairs of vertices. -/
def prim (φ : Fin 50 → A) (x y : Fin 19) : A := ∑ e, inc x y e • W φ e

def cob (w : Fin 19 → Fin 19 → A) (i j k : Fin 19) : A := w i j + w j k - w i k

theorem prim_antisymm (φ : Fin 50 → A) (x y : Fin 19) : prim φ y x = - prim φ x y := by
  unfold prim
  rw [← Finset.sum_neg_distrib]
  refine Finset.sum_congr rfl fun e _ => ?_
  rw [inc_swap, neg_smul]

theorem cob_prim (φ : Fin 50 → A) (f : Fin 50) :
    cob (prim φ) (fA f) (fB f) (fC f) = ∑ e, D f e • W φ e := by
  unfold cob prim D
  simp only [add_smul, sub_smul, Finset.sum_add_distrib, Finset.sum_sub_distrib]

theorem sum_D_smul_W (φ : Fin 50 → A) (f : Fin 50) :
    ∑ e, D f e • W φ e = ∑ g, colSum f g • φ g := by
  unfold W
  simp only [Finset.smul_sum, smul_smul]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun g _ => ?_
  rw [← Finset.sum_smul, sum_D_mul_pc]

/-- **Injectivity.** A face function with sum zero is the coboundary of an
antisymmetric function on pairs. -/
theorem exists_cob_of_sum_zero (φ : Fin 50 → A) (h : ∑ f, φ f = 0) :
    ∃ w : Fin 19 → Fin 19 → A, (∀ x y, w y x = - w x y) ∧
      ∀ f, φ f = cob w (fA f) (fB f) (fC f) := by
  refine ⟨prim φ, prim_antisymm φ, fun f => ?_⟩
  rw [cob_prim, sum_D_smul_W]
  simp only [cert, sub_smul, ite_smul, one_smul, zero_smul, Finset.sum_sub_distrib,
    Finset.sum_ite_eq, Finset.mem_univ, if_true]
  by_cases hf : f = 0
  · subst hf; simp [h]
  · simp [hf]

theorem sum_inc_smul (u : Fin 19 → Fin 19 → A) (hu : ∀ x y, u y x = - u x y) (x y : Fin 19) :
    ∑ e, inc x y e • u (eA e) (eB e) = (∑ e, inc x y e ^ 2) • u x y := by
  rw [Finset.sum_smul]
  refine Finset.sum_congr rfl fun e _ => ?_
  unfold inc
  by_cases h1 : x = eA e ∧ y = eB e
  · simp [h1]
  · by_cases h2 : y = eA e ∧ x = eB e
    · obtain ⟨rfl, rfl⟩ := h2
      rw [hu (eA e) (eB e)]
      simp [h1]
    · simp [h1, h2]

/-- **Well-definedness.** The coboundary of an antisymmetric function on pairs has
face sum zero. -/
theorem sum_cob_eq_zero (u : Fin 19 → Fin 19 → A) (hu : ∀ x y, u y x = - u x y) :
    ∑ f, cob u (fA f) (fB f) (fC f) = 0 := by
  have hface : ∀ f, cob u (fA f) (fB f) (fC f) = ∑ e, D f e • u (eA e) (eB e) := by
    intro f
    obtain ⟨h1, h2, h3⟩ := side_sq f
    unfold cob D
    simp only [add_smul, sub_smul, Finset.sum_add_distrib, Finset.sum_sub_distrib,
      sum_inc_smul u hu, h1, h2, h3, one_smul]
  simp only [hface]
  rw [Finset.sum_comm]
  simp [← Finset.sum_smul, colD]

end QOU.CentralExtension.Cech.Genus4
