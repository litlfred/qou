import Mathlib.Data.Fin.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Data.Finset.Card
import Mathlib.Data.Fintype.Basic
import Mathlib.Data.Fintype.Prod
import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Matrix.Mul
import Mathlib.Data.Real.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import QOU.Braiding.JimboGl3Singlet

set_option autoImplicit false

/-!
# Tetrahedral `K_4` Colour-Flux Ring Exchange & Nucleon-Cluster Wigner Majorana Space-Exchange (`A = 2, 3, 4`)

Formalizes Option 1B (`beans` `qou-3kkz`), building on `ConfinementLayerTower` (`#9212`) and
`ColourReconnectionStokesAssembly` (`#9221`), with `0 sorry`, `0 axiom`, zero empirical literals,
and `AGENTS.md §7c` base-ring generality:

## §1. Complete-Graph `K_A` Simplex, Hamiltonian 4-Cycle & Tait 3-Matching Combinatorics
- Constructive `Finset` definitions on `Fin A` for unoriented and oriented 2-body edges, 3-body
  triangles, and 4-body Hamiltonian 4-cycles, proving exact counts across `A = 1, 2, 3, 4`:
  - Unoriented edges `e₂(A) = C(A, 2) ∈ {0, 1, 3, 6}` (oriented `{0, 2, 6, 12}`),
  - Unoriented triangles `f₃(A) = C(A, 3) ∈ {0, 0, 1, 4}` (oriented `{0, 0, 2, 8}`),
  - Unoriented Hamiltonian 4-cycles `c₄(A) = 3 C(A, 4) ∈ {0, 0, 0, 3}` (oriented `{0, 0, 0, 6}`),
  - Tetrahedral 2-skeleton Euler characteristic `V - E + F = 4 - 6 + 4 = 2`,
  - Canonical Tait 3-edge-colouring bijection `k4HalfEdgeToQuark` pairing all 12 valence quarks
    of `⁴He` (`4 × 3`) 1-to-1 with the 12 half-edges of `K_4` without quark reuse.

## §2. Wigner `SU(4)` Spin-Isospin `[1^A]_{στ}` & Majorana Space-Exchange `P_{ab}^x = +1`
- Over any `[CommRing R]`, integer Pauli tensor swap identity `4 P_{ab}^{στ} = (2 P_{ab}^σ)(2 P_{ab}^τ)`
  on `NucSpinIso := Fin 2 × Fin 2` (`(I + σ·σ)(I + τ·τ)` without needing `√-1`),
- Constructive nonvanishing spin-isospin antisymmetric `[1^A]_{στ}` states for `A = 2, 3, 4`
  (`dim C(4, A) ∈ {6, 4, 1}`), proving Fermi–Dirac Majorana space-exchange `P_{ab}^x = -P_{ab}^{στ}`
  acts as `+1` on every nucleon pair `a ≠ b`, yielding exact pair sum `∑_{a < b} P_{ab}^x = C(A, 2)`
  (`1, 3, 6`), and proving exact `s`-shell Pauli closure at `A = 5` (`Λ⁵(Fin 4 → R) = 0`).

## §3. Exact `9q` & `12q` Cyclic Colour-Reconnection Traces over `[CommRing R]` & `[Field K]`
- Division-free over `[CommRing R]` (for any `q, qinv : R` with `q * qinv = 1`, bridged by `rfl` to
  `QOU.Braiding.JimboGl3Singlet.eps` and `R` over `[Field K]`):
  1. `nineQuark_R34_R67_and_cyclic_overlap_ring` & `nineQuark_R34_R67_overlap_field`: exact
     `3⁹ = 19,683`-term 9-quark 2-interface overlap `⟨ε_q^{⊗ 3} | Ř_{3,4} Ř_{6,7} | ε_q^{⊗ 3}⟩ /
     ‖ε_q‖⁶ = (q³ / [3]_q)²` and single-quark-per-cluster cyclic 3-cycle overlap;
  2. `twelveQuark_R34_R67_R910_overlap_ring` & `_field`: exact `3¹² = 531,441`-term 12-quark
     3-interface overlap `(q³ / [3]_q)³`;
  3. `clusterStepMat_rankOne_and_ringTraces`: exact rank-1 decomposition
     `M(q) + q⁻³ I₃ = [q, q⁻¹, q⁻³]ᵀ [1, 1, 1]` of the `3 × 3` cluster step matrix;
  4. `closedPlaquette_nine_and_twelve_overlap_ring` & `closedPlaquette_connected_cumulants_field`:
     exact closed 3-interface triangular plaquette overlap `(q⁹ [2]_q³ - 8) / ([2]_q³ [3]_q³)`
     (connected `8_c` cumulant `-8 / ([2]_q³ [3]_q³)`) and closed 4-interface tetrahedral ring
     overlap `(q¹² [2]_q⁴ + 8) / ([2]_q⁴ [3]_q⁴)` (connected `8_c` cumulant `+8 / ([2]_q⁴ [3]_q⁴)`).

## §4 & §5. Deuteron Preservation (`A = 2`), Higher-Plaquette Lowering & 3D Jacobi Hall–Post Bound
- Over `[CommRing R]`, 3-body and 4-body simplex counts vanish at `A = 2`, leaving deuteron binding
  identically invariant under arbitrary 3-body and 4-body cyclic couplings; over any strict ordered
  field (and specialized to `ℝ`), both cyclic 3-body and 4-body Bloch–Horowitz channels and 3D
  relative Jacobi `(A - 1)` kinetic factorization (`Hall–Post` bound) strictly enhance binding
  beyond pairwise `C(A, 2)` Majorana additivity.

-- Ref: [wigner1937] https://doi.org/10.1103/PhysRev.51.106
-- Ref: [hall-post1967] https://doi.org/10.1088/0370-1328/90/2/309
-- Ref: [jimbo1986] https://doi.org/10.1007/BF00704588
-- Ref: [kogut-susskind1975] https://doi.org/10.1103/PhysRevD.11.395
-- Ref: [bloch-horowitz1958] https://doi.org/10.1016/0029-5582(58)90136-6
-/

namespace QOU.Nuclear.TetrahedralFluxRingAndMajoranaCluster

open scoped BigOperators Matrix
open Matrix
open QOU.Braiding.JimboGl3Singlet

/-! ## §1. Complete-Graph `K_A` Simplex, Hamiltonian 4-Cycle & Tait 3-Matching Combinatorics -/

section CompleteGraphSimplices

/-- Unoriented 2-body edges of `K_A`, canonically represented by `(i, j) ∈ Fin A × Fin A` with `i < j`. -/
def kAEdges (A : ℕ) : Finset (Fin A × Fin A) :=
  Finset.univ.filter fun e => e.1 < e.2

/-- Oriented 2-body edges of `K_A`, represented by `(i, j)` with `i ≠ j`. -/
def kAOrientedEdges (A : ℕ) : Finset (Fin A × Fin A) :=
  Finset.univ.filter fun e => e.1 ≠ e.2

/-- Unoriented 3-body triangular faces of `K_A`, canonically represented by `i < j < k`. -/
def kATriangles (A : ℕ) : Finset (Fin A × Fin A × Fin A) :=
  Finset.univ.filter fun t => t.1 < t.2.1 ∧ t.2.1 < t.2.2

/-- Oriented 3-cycles on `K_A` modulo cyclic shift, canonically rooted at minimum vertex `i < j, k`
with `j ≠ k` (`i → j → k → i`). -/
def kAOrientedTriangles (A : ℕ) : Finset (Fin A × Fin A × Fin A) :=
  Finset.univ.filter fun t => t.1 < t.2.1 ∧ t.1 < t.2.2 ∧ t.2.1 ≠ t.2.2

/-- Oriented 4-cycles on 4-vertex subsets of `K_A` modulo cyclic shift, canonically rooted at the
minimum vertex `a < b, c, d` with `b, c, d` pairwise distinct (`a → b → c → d → a`). -/
def kAOrientedFourCycles (A : ℕ) : Finset (Fin A × Fin A × Fin A × Fin A) :=
  Finset.univ.filter fun q =>
    q.1 < q.2.1 ∧ q.1 < q.2.2.1 ∧ q.1 < q.2.2.2 ∧
      q.2.1 ≠ q.2.2.1 ∧ q.2.1 ≠ q.2.2.2 ∧ q.2.2.1 ≠ q.2.2.2

/-- Unoriented 4-cycles on 4-vertex subsets of `K_A` (modulo cyclic shift and reversal
`a-b-c-d-a ~ a-d-c-b-a`), canonically selected by `a < b, c, d`, `b < d`, and `c ≠ b, d`. -/
def kAFourCycles (A : ℕ) : Finset (Fin A × Fin A × Fin A × Fin A) :=
  Finset.univ.filter fun q =>
    q.1 < q.2.1 ∧ q.1 < q.2.2.1 ∧ q.1 < q.2.2.2 ∧
      q.2.1 < q.2.2.2 ∧ q.2.2.1 ≠ q.2.1 ∧ q.2.2.1 ≠ q.2.2.2

/-- **Exact `K_A` simplex and Hamiltonian cycle counts across `A = 1, 2, 3, 4`:**
- Unoriented edges `C(A, 2) = [0, 1, 3, 6]`; oriented edges `[0, 2, 6, 12]`;
- Unoriented triangles `C(A, 3) = [0, 0, 1, 4]`; oriented 3-cycles `[0, 0, 2, 8]`;
- Unoriented 4-cycles `3 C(A, 4) = [0, 0, 0, 3]`; oriented 4-cycles `[0, 0, 0, 6]`. -/
theorem kA_simplex_and_cycle_counts :
    ([kAEdges 1 |>.card, kAEdges 2 |>.card, kAEdges 3 |>.card, kAEdges 4 |>.card] =
      [0, 1, 3, 6]) ∧
    ([kAOrientedEdges 1 |>.card, kAOrientedEdges 2 |>.card,
        kAOrientedEdges 3 |>.card, kAOrientedEdges 4 |>.card] =
      [0, 2, 6, 12]) ∧
    ([kATriangles 1 |>.card, kATriangles 2 |>.card,
        kATriangles 3 |>.card, kATriangles 4 |>.card] =
      [0, 0, 1, 4]) ∧
    ([kAOrientedTriangles 1 |>.card, kAOrientedTriangles 2 |>.card,
        kAOrientedTriangles 3 |>.card, kAOrientedTriangles 4 |>.card] =
      [0, 0, 2, 8]) ∧
    ([kAFourCycles 1 |>.card, kAFourCycles 2 |>.card,
        kAFourCycles 3 |>.card, kAFourCycles 4 |>.card] =
      [0, 0, 0, 3]) ∧
    ([kAOrientedFourCycles 1 |>.card, kAOrientedFourCycles 2 |>.card,
        kAOrientedFourCycles 3 |>.card, kAOrientedFourCycles 4 |>.card] =
      [0, 0, 0, 6]) := by
  decide

/-- Explicit census of the 3 unoriented Hamiltonian 4-cycles on `K_4`:
`(0, 1, 2, 3)`, `(0, 1, 3, 2)`, and `(0, 2, 1, 3)`. -/
theorem k4_hamiltonian_four_cycles_explicit :
    kAFourCycles 4 = {(0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3)} := by
  decide

/-- **Tetrahedral boundary Euler characteristic (`∂Δ³ ≅ S²`) and 3-simplex Euler characteristic (`Δ³`):**
`V - E + F = 4 - 6 + 4 = 2` and `V - E + F - C_3 = 4 - 6 + 4 - 1 = 1`, while each of the `6` edges
bounds `2` triangles and each of the `3` Hamiltonian 4-cycles uses `4` of the `6` edges. -/
theorem k4_tetrahedral_euler_and_incidence :
    (4 : ℤ) - (kAEdges 4).card + (kATriangles 4).card = 2 ∧
    (4 : ℤ) - (kAEdges 4).card + (kATriangles 4).card - 1 = 1 ∧
    2 * (kAEdges 4).card = 3 * (kATriangles 4).card ∧
    (kAEdges 4).card = 2 * (kAFourCycles 4).card := by
  decide

/-- Cleared polynomial simplex-count identities over any `[CommRing R]`. -/
theorem simplex_polynomial_identities {R : Type*} [CommRing R] (a : R) :
    a * (a - 1) + 2 * a = a ^ 2 + a ∧
    (a - 2) * (a * (a - 1)) = a ^ 3 - 3 * a ^ 2 + 2 * a ∧
    3 * (a * (a - 1) * (a - 2) * (a - 3)) =
      3 * a ^ 4 - 18 * a ^ 3 + 33 * a ^ 2 - 18 * a := by
  refine ⟨by ring, by ring, by ring⟩

/-- Canonical Tait 3-edge-colouring `(Fin 3)` of the 6 unoriented edges `(u < v)` of `K_4`:
- Colour `0`: `{(0, 1), (2, 3)}`
- Colour `1`: `{(0, 2), (1, 3)}`
- Colour `2`: `{(0, 3), (1, 2)}`. -/
def k4TaitEdgeColour (u v : Fin 4) : Fin 3 :=
  if (u = 0 ∧ v = 1) ∨ (u = 1 ∧ v = 0) ∨ (u = 2 ∧ v = 3) ∨ (u = 3 ∧ v = 2) then 0
  else if (u = 0 ∧ v = 2) ∨ (u = 2 ∧ v = 0) ∨ (u = 1 ∧ v = 3) ∨ (u = 3 ∧ v = 1) then 1
  else 2

/-- Canonical valence-quark index `q ∈ Fin 12` assigned to directed half-edge `(u, v)` (`u ≠ v`)
of `K_4`: maps `(0,1) ↔ (2,3)`, `(1,2) ↔ (5,6)`, `(2,3) ↔ (8,9)` (all three chain interfaces are
zero-transport adjacent generators) and pairs `(0,2) ↔ (1,7)`, `(1,3) ↔ (4,10)`, `(0,3) ↔ (0,11)`. -/
def k4HalfEdgeToQuark (e : { p : Fin 4 × Fin 4 // p.1 ≠ p.2 }) : Fin 12 :=
  ⟨3 * e.1.1.val +
      (if e.1.1.val % 2 = 0 then 2 - (k4TaitEdgeColour e.1.1 e.1.2).val
       else (k4TaitEdgeColour e.1.1 e.1.2).val),
    by
      have hu : e.1.1.val < 4 := e.1.1.isLt
      have hm : (k4TaitEdgeColour e.1.1 e.1.2).val < 3 := (k4TaitEdgeColour e.1.1 e.1.2).isLt
      split_ifs <;> omega⟩

/-- **Exact `12q ↔ 12` half-edge Tait bijection on `K_4` & `K_5` valence obstruction:**
1. `k4TaitEdgeColour` is symmetric and a proper 3-edge-colouring at every vertex of `K_4`;
2. `k4HalfEdgeToQuark` maps the `12` oriented half-edges of `K_4` onto all `12` quarks in `Fin 12`
   with exact image cardinality `12` (zero quark reuse across all 6 tetrahedral bonds);
3. For `K_5` (`A = 5`), vertex degree is `4 > 3 = N_c`, so no proper 3-edge-colouring exists. -/
theorem k4_tait_bijection_and_k5_obstruction :
    (∀ u v : Fin 4, k4TaitEdgeColour u v = k4TaitEdgeColour v u) ∧
    (∀ u v w : Fin 4, u ≠ v → u ≠ w → v ≠ w →
      k4TaitEdgeColour u v ≠ k4TaitEdgeColour u w) ∧
    (Finset.univ.image k4HalfEdgeToQuark).card = 12 ∧
    ¬ ∃ col : Fin 5 → Fin 5 → Fin 3,
        ∀ v w : Fin 5, (0 : Fin 5) ≠ v → (0 : Fin 5) ≠ w → v ≠ w → col 0 v ≠ col 0 w := by
  refine ⟨by decide, by decide, by decide, ?_⟩
  rintro ⟨col, hcol⟩
  let f : Fin 4 → Fin 3 := fun i => col 0 i.succ
  have hinj : Function.Injective f := by
    intro i j hij
    by_contra hne
    have hsucc_ne : i.succ ≠ j.succ := fun hs => hne (Fin.succ_injective _ hs)
    exact hcol i.succ j.succ (Fin.succ_ne_zero i).symm (Fin.succ_ne_zero j).symm hsucc_ne hij
  have hcard := Fintype.card_le_of_injective f hinj
  norm_num at hcard

end CompleteGraphSimplices

/-! ## §2. Wigner `SU(4)` Spin-Isospin `[1^A]_{στ}` & Majorana Space-Exchange `P_{ab}^x = +1` -/

section WignerMajoranaCluster

/-- Single-nucleon 4-component spin-isospin index `(spin, isospin) ∈ Fin 2 × Fin 2`. -/
abbrev NucSpinIso := Fin 2 × Fin 2

/-- Integer bilinear Pauli dot-product `I + σ₁·σ₂` on `Fin 2` over any `[CommRing R]`. -/
def pauliOneAddDot {R : Type*} [CommRing R] (v : Fin 2 → Fin 2 → R) : Fin 2 → Fin 2 → R :=
  fun s₁ s₂ =>
    v s₁ s₂ +
    v (1 - s₁) (1 - s₂) +
    -(if s₁ = 0 then (1 : R) else -1) * (if s₂ = 0 then (1 : R) else -1) * v (1 - s₁) (1 - s₂) +
    (if s₁ = 0 then (1 : R) else -1) * (if s₂ = 0 then (1 : R) else -1) * v s₁ s₂

/-- **Division-free Pauli spin-exchange theorem over `[CommRing R]`:**
`(I + σ₁·σ₂) v (s₁, s₂) = 2 * v (s₂, s₁)`. -/
theorem pauliOneAddDot_eq_two_swap {R : Type*} [CommRing R]
    (v : Fin 2 → Fin 2 → R) (s₁ s₂ : Fin 2) :
    pauliOneAddDot v s₁ s₂ = 2 * v s₂ s₁ := by
  fin_cases s₁ <;> fin_cases s₂ <;> simp [pauliOneAddDot] <;> ring

/-- Four times the two-nucleon spin-isospin exchange `(I + σ₁·σ₂)(I + τ₁·τ₂)` on `NucSpinIso`. -/
def fourSpinIsoExchange {R : Type*} [CommRing R]
    (Ψ : NucSpinIso → NucSpinIso → R) : NucSpinIso → NucSpinIso → R :=
  fun x₁ x₂ =>
    pauliOneAddDot (fun s₁ s₂ => pauliOneAddDot (fun t₁ t₂ => Ψ (s₁, t₁) (s₂, t₂)) x₁.2 x₂.2)
      x₁.1 x₂.1

/-- **Exact Wigner `SU(4)` spin-isospin swap identity over `[CommRing R]`:**
`(I + σ₁·σ₂)(I + τ₁·τ₂) Ψ (x₁, x₂) = 4 * Ψ (x₂, x₁)`. -/
theorem fourSpinIsoExchange_eq_four_swap {R : Type*} [CommRing R]
    (Ψ : NucSpinIso → NucSpinIso → R) (x₁ x₂ : NucSpinIso) :
    fourSpinIsoExchange Ψ x₁ x₂ = 4 * Ψ x₂ x₁ := by
  rcases x₁ with ⟨s₁, t₁⟩
  rcases x₂ with ⟨s₂, t₂⟩
  simp only [fourSpinIsoExchange, pauliOneAddDot_eq_two_swap]
  ring

/-- Swap nucleon slots `a` and `b` in an `A`-nucleon spin-isospin tensor `Ψ : (Fin A → NucSpinIso) → R`. -/
def swapNucleonSpinIso {A : ℕ} {R : Type*} (a b : Fin A)
    (Ψ : (Fin A → NucSpinIso) → R) : (Fin A → NucSpinIso) → R :=
  fun cfg => Ψ (cfg ∘ Equiv.swap a b)

/-- Predicate that `Ψ : (Fin A → NucSpinIso) → R` lies in the spin-isospin antisymmetric Wigner
representation `[1^A]_{στ}`: swapping any distinct nucleons `a ≠ b` negates `Ψ`. -/
def IsSpinIsoAntisym {A : ℕ} {R : Type*} [CommRing R]
    (Ψ : (Fin A → NucSpinIso) → R) : Prop :=
  ∀ a b : Fin A, a ≠ b → swapNucleonSpinIso a b Ψ = -Ψ

/-- Under nucleon Fermi–Dirac total antisymmetry `P_{ab}^x (swapNucleonSpinIso a b Ψ) = -Ψ`,
the induced Majorana space-exchange action on `Ψ` is `-swapNucleonSpinIso a b Ψ`. -/
def majoranaOnSpinIso {A : ℕ} {R : Type*} [CommRing R] (a b : Fin A)
    (Ψ : (Fin A → NucSpinIso) → R) : (Fin A → NucSpinIso) → R :=
  -swapNucleonSpinIso a b Ψ

/-- **Majorana `+1` Space-Exchange Theorem (`majorana_eq_id_and_pair_sum_on_antisym`):**
Over any `[CommRing R]`, for **every** `A`-nucleon state `Ψ` in `[1^A]_{στ}`:
1. Every distinct nucleon pair `a ≠ b` has Majorana space-exchange eigenvalue `+1`;
2. Summing `majoranaOnSpinIso e.1 e.2 Ψ` over all `C(A, 2)` unoriented edges `e ∈ kAEdges A`
   equals `(kAEdges A).card • Ψ` (`1 • Ψ` at `A = 2`, `3 • Ψ` at `A = 3`, `6 • Ψ` at `A = 4`). -/
theorem majorana_eq_id_and_pair_sum_on_antisym {A : ℕ} {R : Type*} [CommRing R]
    {Ψ : (Fin A → NucSpinIso) → R} (hanti : IsSpinIsoAntisym Ψ) :
    (∀ a b : Fin A, a ≠ b → majoranaOnSpinIso a b Ψ = Ψ) ∧
    (∑ e ∈ kAEdges A, majoranaOnSpinIso e.1 e.2 Ψ) = (kAEdges A).card • Ψ := by
  have hpair : ∀ a b : Fin A, a ≠ b → majoranaOnSpinIso a b Ψ = Ψ := by
    intro a b hne
    unfold majoranaOnSpinIso
    rw [hanti a b hne, neg_neg]
  refine ⟨hpair, ?_⟩
  calc (∑ e ∈ kAEdges A, majoranaOnSpinIso e.1 e.2 Ψ)
      = ∑ _e ∈ kAEdges A, Ψ := by
          refine Finset.sum_congr rfl fun e he => ?_
          simp only [kAEdges, Finset.mem_filter, Finset.mem_univ, true_and] at he
          exact hpair e.1 e.2 (ne_of_lt he)
    _ = (kAEdges A).card • Ψ := Finset.sum_const Ψ

/-- Canonical ordering `0..3` of `NucSpinIso = Fin 2 × Fin 2` (`2 * s + t`). -/
def nucIdx (x : NucSpinIso) : Fin 4 :=
  ⟨2 * x.1.val + x.2.val, by
    have hs := x.1.isLt
    have ht := x.2.isLt
    omega⟩

/-- Sign-carrying Levi-Civita / Slater determinant generator on `Fin A → Fin 4` via inversion parity. -/
def slaterSign {A : ℕ} {R : Type*} [CommRing R] (f : Fin A → Fin 4) : R :=
  ∏ e ∈ kAEdges A,
    if f e.1 = f e.2 then 0
    else if f e.1 < f e.2 then (1 : R) else -1

/-- Canonical `[1^A]_{στ}` Slater spin-isospin state on `Fin A → NucSpinIso`. -/
def wignerAntisymState (A : ℕ) (R : Type*) [CommRing R] : (Fin A → NucSpinIso) → R :=
  fun cfg => slaterSign (fun i => nucIdx (cfg i))

private theorem slaterSign_eq_intCast {A : ℕ} {R : Type*} [CommRing R] (g : Fin A → Fin 4) :
    (slaterSign g : R) = ((slaterSign g : ℤ) : R) := by
  unfold slaterSign
  push_cast
  refine Finset.prod_congr rfl fun _ _ => ?_
  split_ifs <;> simp

private theorem slaterSign_swap_Z2 (v0 v1 : Fin 4) (a b : Fin 2) (hne : a ≠ b) :
    slaterSign (R := ℤ) (![v0, v1] ∘ Equiv.swap a b) = -slaterSign (R := ℤ) ![v0, v1] := by
  revert v0 v1 a b hne
  decide

private theorem slaterSign_swap_Z3 (v0 v1 v2 : Fin 4) (a b : Fin 3) (hne : a ≠ b) :
    slaterSign (R := ℤ) (![v0, v1, v2] ∘ Equiv.swap a b) = -slaterSign (R := ℤ) ![v0, v1, v2] := by
  revert v0 v1 v2 a b hne
  decide

private theorem slaterSign_swap_Z4 (v0 v1 v2 v3 : Fin 4) (a b : Fin 4) (hne : a ≠ b) :
    slaterSign (R := ℤ) (![v0, v1, v2, v3] ∘ Equiv.swap a b) =
      -slaterSign (R := ℤ) ![v0, v1, v2, v3] := by
  revert v0 v1 v2 v3 a b hne
  decide

/-- **Non-vacuity & `s`-shell closure of `[1^A]_{στ}` (`wignerAntisym_nonvacuous_A234_and_pauli_A5`):**
1. Over any `[CommRing R]`, `wignerAntisymState A R` satisfies `IsSpinIsoAntisym` for `A = 2, 3, 4`
   and evaluates to `1` on the canonical ground configuration;
2. The `SU(4)` exterior dimensions `[C(4,1), C(4,2), C(4,3), C(4,4), C(4,5)] = [4, 6, 4, 1, 0]`;
3. **Mass-5 Pauli closure (`A = 5`):** Over any `[CommRing R]` where `(2 : R)` is regular
   (`2 * r = 0 → r = 0`), **every** `5`-nucleon state satisfying `IsSpinIsoAntisym` is identically `0`! -/
theorem wignerAntisym_nonvacuous_A234_and_pauli_A5 :
    ([Nat.choose 4 1, Nat.choose 4 2, Nat.choose 4 3, Nat.choose 4 4, Nat.choose 4 5] =
      [4, 6, 4, 1, 0]) ∧
    (∀ {R : Type*} [CommRing R],
      IsSpinIsoAntisym (wignerAntisymState 2 R) ∧
      wignerAntisymState 2 R ![(0, 0), (0, 1)] = 1) ∧
    (∀ {R : Type*} [CommRing R],
      IsSpinIsoAntisym (wignerAntisymState 3 R) ∧
      wignerAntisymState 3 R ![(0, 0), (0, 1), (1, 0)] = 1) ∧
    (∀ {R : Type*} [CommRing R],
      IsSpinIsoAntisym (wignerAntisymState 4 R) ∧
      wignerAntisymState 4 R ![(0, 0), (0, 1), (1, 0), (1, 1)] = 1) ∧
    (∀ {R : Type*} [CommRing R], (∀ r : R, 2 * r = 0 → r = 0) →
      ∀ Ψ : (Fin 5 → NucSpinIso) → R, IsSpinIsoAntisym Ψ → Ψ = 0) := by
  refine ⟨by decide, ?_, ?_, ?_, ?_⟩
  · intro R _
    refine ⟨fun a b hne => ?_, ?_⟩
    · funext cfg
      simp only [swapNucleonSpinIso, Pi.neg_apply, wignerAntisymState, Function.comp_apply]
      rw [slaterSign_eq_intCast (R := R) (fun i => nucIdx (cfg (Equiv.swap a b i))),
        slaterSign_eq_intCast (R := R) (fun i => nucIdx (cfg i)), ← Int.cast_neg]
      congr 1
      have hg : (fun i : Fin 2 => nucIdx (cfg i)) = ![nucIdx (cfg 0), nucIdx (cfg 1)] := by
        funext i; fin_cases i <;> rfl
      have hgs : (fun i : Fin 2 => nucIdx (cfg (Equiv.swap a b i))) =
          ![nucIdx (cfg 0), nucIdx (cfg 1)] ∘ Equiv.swap a b := by
        funext i; rw [Function.comp_apply, ← hg]
      rw [hgs, hg]
      exact slaterSign_swap_Z2 (nucIdx (cfg 0)) (nucIdx (cfg 1)) a b hne
    · unfold wignerAntisymState
      rw [slaterSign_eq_intCast (R := R)]
      have hz : slaterSign (R := ℤ) (fun i : Fin 2 => nucIdx (![(0, 0), (0, 1)] i)) = 1 := by decide
      rw [hz, Int.cast_one]
  · intro R _
    refine ⟨fun a b hne => ?_, ?_⟩
    · funext cfg
      simp only [swapNucleonSpinIso, Pi.neg_apply, wignerAntisymState, Function.comp_apply]
      rw [slaterSign_eq_intCast (R := R) (fun i => nucIdx (cfg (Equiv.swap a b i))),
        slaterSign_eq_intCast (R := R) (fun i => nucIdx (cfg i)), ← Int.cast_neg]
      congr 1
      have hg : (fun i : Fin 3 => nucIdx (cfg i)) =
          ![nucIdx (cfg 0), nucIdx (cfg 1), nucIdx (cfg 2)] := by
        funext i; fin_cases i <;> rfl
      have hgs : (fun i : Fin 3 => nucIdx (cfg (Equiv.swap a b i))) =
          ![nucIdx (cfg 0), nucIdx (cfg 1), nucIdx (cfg 2)] ∘ Equiv.swap a b := by
        funext i; rw [Function.comp_apply, ← hg]
      rw [hgs, hg]
      exact slaterSign_swap_Z3 (nucIdx (cfg 0)) (nucIdx (cfg 1)) (nucIdx (cfg 2)) a b hne
    · unfold wignerAntisymState
      rw [slaterSign_eq_intCast (R := R)]
      have hz : slaterSign (R := ℤ) (fun i : Fin 3 => nucIdx (![(0, 0), (0, 1), (1, 0)] i)) = 1 := by
        decide
      rw [hz, Int.cast_one]
  · intro R _
    refine ⟨fun a b hne => ?_, ?_⟩
    · funext cfg
      simp only [swapNucleonSpinIso, Pi.neg_apply, wignerAntisymState, Function.comp_apply]
      rw [slaterSign_eq_intCast (R := R) (fun i => nucIdx (cfg (Equiv.swap a b i))),
        slaterSign_eq_intCast (R := R) (fun i => nucIdx (cfg i)), ← Int.cast_neg]
      congr 1
      have hg : (fun i : Fin 4 => nucIdx (cfg i)) =
          ![nucIdx (cfg 0), nucIdx (cfg 1), nucIdx (cfg 2), nucIdx (cfg 3)] := by
        funext i; fin_cases i <;> rfl
      have hgs : (fun i : Fin 4 => nucIdx (cfg (Equiv.swap a b i))) =
          ![nucIdx (cfg 0), nucIdx (cfg 1), nucIdx (cfg 2), nucIdx (cfg 3)] ∘ Equiv.swap a b := by
        funext i; rw [Function.comp_apply, ← hg]
      rw [hgs, hg]
      exact slaterSign_swap_Z4
        (nucIdx (cfg 0)) (nucIdx (cfg 1)) (nucIdx (cfg 2)) (nucIdx (cfg 3)) a b hne
    · unfold wignerAntisymState
      rw [slaterSign_eq_intCast (R := R)]
      have hz :
          slaterSign (R := ℤ) (fun i : Fin 4 => nucIdx (![(0, 0), (0, 1), (1, 0), (1, 1)] i)) = 1 := by
        decide
      rw [hz, Int.cast_one]
  · intro R _ h2reg Ψ hanti
    funext cfg
    have hnot_inj : ¬ Function.Injective cfg := by
      intro hinj
      have hle := Fintype.card_le_of_injective cfg hinj
      norm_num at hle
    simp only [Function.Injective, not_forall] at hnot_inj
    obtain ⟨a, b, hab_eq, hab_ne⟩ := hnot_inj
    have hswap_cfg : cfg ∘ Equiv.swap a b = cfg := by
      funext i
      simp only [Function.comp_apply]
      by_cases hia : i = a
      · subst hia; simp [hab_eq]
      · by_cases hib : i = b
        · subst hib; simp [hab_eq]
        · rw [Equiv.swap_apply_of_ne_of_ne hia hib]
    have hanti_ab := congr_fun (hanti a b hab_ne) cfg
    simp only [swapNucleonSpinIso, Pi.neg_apply, hswap_cfg] at hanti_ab
    exact h2reg (Ψ cfg) (by linear_combination hanti_ab)

end WignerMajoranaCluster

/-! ## §3. Exact `9q` & `12q` Colour-Reconnection Overlaps over `[CommRing R]` & `[Field K]` -/

section MultiClusterColourReconnection

/-- Three-quark cluster colour configuration `(a, b, c) ∈ Fin 3 × Fin 3 × Fin 3`. -/
abbrev Cl3 := Fin 3 × Fin 3 × Fin 3

/-- Division-free `q`-antisymmetric 3-quark colour singlet over any `[CommRing R]`. -/
def epsRing {R : Type*} [CommRing R] (qinv : R) (a b c : Fin 3) : R :=
  if a = 0 ∧ b = 1 ∧ c = 2 then 1
  else if a = 0 ∧ b = 2 ∧ c = 1 then -qinv
  else if a = 1 ∧ b = 0 ∧ c = 2 then -qinv
  else if a = 1 ∧ b = 2 ∧ c = 0 then qinv ^ 2
  else if a = 2 ∧ b = 0 ∧ c = 1 then qinv ^ 2
  else if a = 2 ∧ b = 1 ∧ c = 0 then -qinv ^ 3
  else 0

/-- Tuple wrapper of `epsRing` on `Cl3 = Fin 3 × Fin 3 × Fin 3`. -/
def epsCl {R : Type*} [CommRing R] (qinv : R) (u : Cl3) : R :=
  epsRing qinv u.1 u.2.1 u.2.2

/-- Division-free Jimbo `U_q(𝔰𝔩₃)` braiding operator on `Fin 3 → Fin 3 → R` over any `[CommRing R]`. -/
def jR {R : Type*} [CommRing R] (q qinv : R) (v : Fin 3 → Fin 3 → R) : Fin 3 → Fin 3 → R :=
  fun a b => if a = b then q * v a a else v b a + (if b < a then (q - qinv) * v a b else 0)

/-- Matrix kernel `jRMat q qinv c a c' a'` of `jR`. -/
def jRMat {R : Type*} [CommRing R] (q qinv : R) (c a c' a' : Fin 3) : R :=
  if c = a then (if c' = c ∧ a' = c then q else 0)
  else (if c' = a ∧ a' = c then 1 else 0) +
       (if a < c ∧ c' = c ∧ a' = a then q - qinv else 0)

/-- **Exact definitional bridges (`rfl`) to `QOU.Braiding.JimboGl3Singlet` over `[Field K]`.** -/
theorem epsRing_and_jR_eq_jimbo {K : Type*} [Field K] (q : K) :
    epsRing q⁻¹ = eps q ∧ jR q q⁻¹ = R q :=
  ⟨rfl, rfl⟩

theorem jR_eq_sum_jRMat {R : Type*} [CommRing R] (q qinv : R)
    (v : Fin 3 → Fin 3 → R) (c a : Fin 3) :
    jR q qinv v c a = ∑ c' : Fin 3, ∑ a' : Fin 3, jRMat q qinv c a c' a' * v c' a' := by
  fin_cases c <;> fin_cases a <;> simp [jR, jRMat, Fin.sum_univ_three]

/-- Norm-squared `(1 + qinv²)(1 + qinv² + qinv⁴)` of `epsRing qinv` over `[CommRing R]`. -/
def epsNormSqRing {R : Type*} [CommRing R] (qinv : R) : R :=
  ∑ u : Cl3, epsCl qinv u * epsCl qinv u

/-- Partial right norm-squared of `epsRing qinv` fixing 3rd quark `c`. -/
def epsRightSqRing {R : Type*} [CommRing R] (qinv : R) (c : Fin 3) : R :=
  ∑ a : Fin 3, ∑ b : Fin 3, epsRing qinv a b c * epsRing qinv a b c

/-- Partial left norm-squared of `epsRing qinv` fixing 1st quark `a`. -/
def epsLeftSqRing {R : Type*} [CommRing R] (qinv : R) (a : Fin 3) : R :=
  ∑ b : Fin 3, ∑ c : Fin 3, epsRing qinv a b c * epsRing qinv a b c

/-- Spectator-quark contraction `∑_b epsRing qinv a b c * epsRing qinv a' b c'`. -/
def clSpectatorW {R : Type*} [CommRing R] (qinv : R) (a c a' c' : Fin 3) : R :=
  ∑ b : Fin 3, epsRing qinv a b c * epsRing qinv a' b c'

theorem epsNormSqRing_closed_form {R : Type*} [CommRing R] (q qinv : R) (hq : q * qinv = 1) :
    epsNormSqRing qinv = (1 + qinv ^ 2) * (1 + qinv ^ 2 + qinv ^ 4) ∧
    (∑ c : Fin 3, epsRightSqRing qinv c) = epsNormSqRing qinv ∧
    (∑ a : Fin 3, epsLeftSqRing qinv a) = epsNormSqRing qinv ∧
    q ^ 3 * epsNormSqRing qinv = (q + qinv) * (q ^ 2 + 1 + qinv ^ 2) ∧
    (q ^ 2 + 1 + qinv ^ 2) * (q * (1 + qinv ^ 2)) = q ^ 3 * epsNormSqRing qinv := by
  have hn : epsNormSqRing qinv = (1 + qinv ^ 2) * (1 + qinv ^ 2 + qinv ^ 4) := by
    simp [epsNormSqRing, epsCl, epsRing, Fintype.sum_prod_type, Fin.sum_univ_three]
    ring
  have hr : (∑ c : Fin 3, epsRightSqRing qinv c) = (1 + qinv ^ 2) * (1 + qinv ^ 2 + qinv ^ 4) := by
    simp [epsRightSqRing, epsRing, Fin.sum_univ_three]
    ring
  have hl : (∑ a : Fin 3, epsLeftSqRing qinv a) = (1 + qinv ^ 2) * (1 + qinv ^ 2 + qinv ^ 4) := by
    simp [epsLeftSqRing, epsRing, Fin.sum_univ_three]
    ring
  have hf1 : q * (1 + qinv ^ 2) = q + qinv := by
    linear_combination qinv * hq
  have hf2 : q ^ 2 * (1 + qinv ^ 2 + qinv ^ 4) = q ^ 2 + 1 + qinv ^ 2 := by
    linear_combination (q * qinv + 1 + q * qinv ^ 3 + qinv ^ 2) * hq
  have hprod : q ^ 3 * epsNormSqRing qinv = (q + qinv) * (q ^ 2 + 1 + qinv ^ 2) := by
    rw [hn]
    calc q ^ 3 * ((1 + qinv ^ 2) * (1 + qinv ^ 2 + qinv ^ 4))
        = (q * (1 + qinv ^ 2)) * (q ^ 2 * (1 + qinv ^ 2 + qinv ^ 4)) := by ring
      _ = (q + qinv) * (q ^ 2 + 1 + qinv ^ 2) := by rw [hf1, hf2]
  have hscale : (q ^ 2 + 1 + qinv ^ 2) * (q * (1 + qinv ^ 2)) = q ^ 3 * epsNormSqRing qinv := by
    rw [hf1, hprod, mul_comm]
  exact ⟨hn, hr.trans hn.symm, hl.trans hn.symm, hprod, hscale⟩

private theorem epsRight_orthog_ring {R : Type*} [CommRing R] (qinv : R) {c c' : Fin 3}
    (hne : c ≠ c') :
    (∑ a : Fin 3, ∑ b : Fin 3, epsRing qinv a b c * epsRing qinv a b c') = 0 := by
  fin_cases c <;> fin_cases c' <;> try contradiction
  all_goals simp [epsRing, Fin.sum_univ_three]

private theorem epsLeft_orthog_ring {R : Type*} [CommRing R] (qinv : R) {a a' : Fin 3}
    (hne : a ≠ a') :
    (∑ b : Fin 3, ∑ c : Fin 3, epsRing qinv a b c * epsRing qinv a' b c) = 0 := by
  fin_cases a <;> fin_cases a' <;> try contradiction
  all_goals simp [epsRing, Fin.sum_univ_three]

/-- **Universal Schur Leaf-Pruning Identity over `[CommRing R]`:**
Contracting a cluster's right quark `c` against `jRMat q qinv c d c' d'` kills `d' ≠ d`
and yields the `d`-independent scalar `q * (1 + qinv²)` for **every** `d : Fin 3`. -/
theorem schur_right_leaf_prune {R : Type*} [CommRing R] (q qinv : R) (hq : q * qinv = 1)
    (d d' : Fin 3) :
    (∑ a : Fin 3, ∑ b : Fin 3, ∑ c : Fin 3, ∑ c' : Fin 3,
      epsRing qinv a b c * epsRing qinv a b c' * jRMat q qinv c d c' d') =
    if d = d' then q * (1 + qinv ^ 2) else 0 := by
  have hswap_sum : ∀ c c' : Fin 3,
      (∑ a : Fin 3, ∑ b : Fin 3,
        epsRing qinv a b c * epsRing qinv a b c' * jRMat q qinv c d c' d') =
      if c = c' then epsRightSqRing qinv c * jRMat q qinv c d c d' else 0 := by
    intro c c'
    simp_rw [← Finset.sum_mul]
    by_cases hcc : c = c'
    · subst hcc; simp [epsRightSqRing]
    · simp [hcc, epsRight_orthog_ring qinv hcc]
  have hcomm :
      (∑ a : Fin 3, ∑ b : Fin 3, ∑ c : Fin 3, ∑ c' : Fin 3,
        epsRing qinv a b c * epsRing qinv a b c' * jRMat q qinv c d c' d') =
      ∑ c : Fin 3, ∑ c' : Fin 3, ∑ a : Fin 3, ∑ b : Fin 3,
        epsRing qinv a b c * epsRing qinv a b c' * jRMat q qinv c d c' d' := by
    calc _ = ∑ a : Fin 3, ∑ c : Fin 3, ∑ b : Fin 3, ∑ c' : Fin 3, _ :=
            Finset.sum_congr rfl fun _ _ => Finset.sum_comm
      _ = ∑ c : Fin 3, ∑ a : Fin 3, ∑ b : Fin 3, ∑ c' : Fin 3, _ := Finset.sum_comm
      _ = ∑ c : Fin 3, ∑ a : Fin 3, ∑ c' : Fin 3, ∑ b : Fin 3, _ :=
            Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => Finset.sum_comm
      _ = ∑ c : Fin 3, ∑ c' : Fin 3, ∑ a : Fin 3, ∑ b : Fin 3, _ :=
            Finset.sum_congr rfl fun _ _ => Finset.sum_comm
  rw [hcomm]
  simp_rw [hswap_sum]
  fin_cases d <;> fin_cases d' <;>
    simp [epsRightSqRing, epsRing, jRMat, Fin.sum_univ_three]
  · linear_combination (qinv ^ 3 + qinv + qinv ^ 5 + qinv ^ 3) * hq
  · linear_combination (qinv + qinv ^ 3) * hq
  · ring

/-- Dual left-leaf Schur pruning: contracting a cluster's first quark `a` against `jRMat c a c' a'`
yields `q * (1 + qinv²)` when `c = c'` and `0` otherwise. -/
theorem schur_left_leaf_prune {R : Type*} [CommRing R] (q qinv : R) (hq : q * qinv = 1)
    (c c' : Fin 3) :
    (∑ a : Fin 3, ∑ b : Fin 3, ∑ f : Fin 3, ∑ a' : Fin 3,
      epsRing qinv a b f * epsRing qinv a' b f * jRMat q qinv c a c' a') =
    if c = c' then q * (1 + qinv ^ 2) else 0 := by
  have hswap_sum : ∀ a a' : Fin 3,
      (∑ b : Fin 3, ∑ f : Fin 3,
        epsRing qinv a b f * epsRing qinv a' b f * jRMat q qinv c a c' a') =
      if a = a' then epsLeftSqRing qinv a * jRMat q qinv c a c' a else 0 := by
    intro a a'
    simp_rw [← Finset.sum_mul]
    by_cases haa : a = a'
    · subst haa; simp [epsLeftSqRing]
    · simp [haa, epsLeft_orthog_ring qinv haa]
  have hcomm :
      (∑ a : Fin 3, ∑ b : Fin 3, ∑ f : Fin 3, ∑ a' : Fin 3,
        epsRing qinv a b f * epsRing qinv a' b f * jRMat q qinv c a c' a') =
      ∑ a : Fin 3, ∑ a' : Fin 3, ∑ b : Fin 3, ∑ f : Fin 3,
        epsRing qinv a b f * epsRing qinv a' b f * jRMat q qinv c a c' a' := by
    calc _ = ∑ a : Fin 3, ∑ b : Fin 3, ∑ a' : Fin 3, ∑ f : Fin 3, _ :=
            Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => Finset.sum_comm
      _ = ∑ a : Fin 3, ∑ a' : Fin 3, ∑ b : Fin 3, ∑ f : Fin 3, _ :=
            Finset.sum_congr rfl fun _ _ => Finset.sum_comm
  rw [hcomm]
  simp_rw [hswap_sum]
  fin_cases c <;> fin_cases c' <;>
    simp [epsLeftSqRing, epsRing, jRMat, Fin.sum_univ_three]
  · ring
  · linear_combination (qinv + qinv ^ 3) * hq
  · linear_combination (qinv ^ 3 + qinv + qinv ^ 5 + qinv ^ 3) * hq

private theorem sum_factor_two {ι₁ ι₂ R : Type*} [Fintype ι₁] [Fintype ι₂] [CommRing R]
    (c : R) (f : ι₁ → R) (g : ι₂ → R) :
    (∑ x : ι₁, ∑ y : ι₂, c * f x * g y) = c * (∑ x : ι₁, f x) * (∑ y : ι₂, g y) := by
  simp_rw [← Finset.mul_sum]
  rw [← Finset.sum_mul, ← Finset.mul_sum, mul_assoc]

/-! ### §3a. Open 2-Interface `9q` (`Ř_{3,4} Ř_{6,7}`), Cyclic 3-Quark `9q`, and 3-Interface `12q` Overlaps -/

/-- Factorized `9q` three-nucleon singlet `ε_q^{⊗ 3}` on `Cl3 × Cl3 × Cl3` (`3⁹ = 19,683` components). -/
def eps9Cl {R : Type*} [CommRing R] (qinv : R) (u₁ u₂ u₃ : Cl3) : R :=
  epsCl qinv u₁ * epsCl qinv u₂ * epsCl qinv u₃

/-- Action of `Ř_{3,4}(q) Ř_{6,7}(q)` (1-indexed quark interfaces `(3,4)` and `(6,7)`) on `9q` tensors. -/
def R34_R67_nine {R : Type*} [CommRing R] (q qinv : R)
    (W : Cl3 → Cl3 → Cl3 → R) : Cl3 → Cl3 → Cl3 → R :=
  fun u₁ u₂ u₃ =>
    jR q qinv (fun c₁' a₂' =>
      jR q qinv (fun c₂' a₃' =>
        W (u₁.1, u₁.2.1, c₁') (a₂', u₂.2.1, c₂') (a₃', u₃.2.1, u₃.2.2)) u₂.2.2 u₃.1) u₁.2.2 u₂.1

/-- Action of the single-quark-per-cluster cyclic 3-cycle `Ř_{3,6}(q) Ř_{6,9}(q)` on `9q` tensors. -/
def cyclic3Quark_nine {R : Type*} [CommRing R] (q qinv : R)
    (W : Cl3 → Cl3 → Cl3 → R) : Cl3 → Cl3 → Cl3 → R :=
  fun u₁ u₂ u₃ =>
    jR q qinv (fun c₁' x =>
      jR q qinv (fun c₂' c₃' =>
        W (u₁.1, u₁.2.1, c₁') (u₂.1, u₂.2.1, c₂') (u₃.1, u₃.2.1, c₃')) x u₃.2.2) u₁.2.2 u₂.2.2

/-- Factorized `12q` four-nucleon singlet `ε_q^{⊗ 4}` on `Cl3⁴` (`3¹² = 531,441` components). -/
def eps12Cl {R : Type*} [CommRing R] (qinv : R) (u₁ u₂ u₃ u₄ : Cl3) : R :=
  epsCl qinv u₁ * epsCl qinv u₂ * epsCl qinv u₃ * epsCl qinv u₄

/-- Action of `Ř_{3,4}(q) Ř_{6,7}(q) Ř_{9,10}(q)` on `12q` tensors. -/
def R34_R67_R910_twelve {R : Type*} [CommRing R] (q qinv : R)
    (W : Cl3 → Cl3 → Cl3 → Cl3 → R) : Cl3 → Cl3 → Cl3 → Cl3 → R :=
  fun u₁ u₂ u₃ u₄ =>
    jR q qinv (fun c₁' a₂' =>
      jR q qinv (fun c₂' a₃' =>
        jR q qinv (fun c₃' a₄' =>
          W (u₁.1, u₁.2.1, c₁') (a₂', u₂.2.1, c₂') (a₃', u₃.2.1, c₃') (a₄', u₄.2.1, u₄.2.2))
          u₃.2.2 u₄.1) u₂.2.2 u₃.1) u₁.2.2 u₂.1

/-- **Exact `9q` `Ř_{3,4} Ř_{6,7}` and cyclic 3-quark overlaps over `[CommRing R]`:**
1. `⟨ε_q^{⊗ 3} | Ř_{3,4} Ř_{6,7} | ε_q^{⊗ 3}⟩ = q² (1 + qinv²)² · epsNormSqRing qinv`;
2. Cleared `[3]_q²` form:
   `(q² + 1 + qinv²)² · ⟨ε_q^{⊗ 3} | Ř_{3,4} Ř_{6,7} | ε_q^{⊗ 3}⟩ = (q³)² · (epsNormSqRing qinv)³`;
3. Single-quark-per-cluster cyclic 3-cycle `⟨ε_q^{⊗ 3} | Ř_{3,6} Ř_{6,9} | ε_q^{⊗ 3}⟩` satisfies the
   exact same `(q³ / [3]_q)² · ‖ε_q‖⁶` identity! -/
theorem nineQuark_R34_R67_and_cyclic_overlap_ring {R : Type*} [CommRing R]
    (q qinv : R) (hq : q * qinv = 1) :
    (∑ u₁ : Cl3, ∑ u₂ : Cl3, ∑ u₃ : Cl3,
        eps9Cl qinv u₁ u₂ u₃ * R34_R67_nine q qinv (eps9Cl qinv) u₁ u₂ u₃) =
      (q * (1 + qinv ^ 2)) ^ 2 * epsNormSqRing qinv ∧
    (q ^ 2 + 1 + qinv ^ 2) ^ 2 *
        (∑ u₁ : Cl3, ∑ u₂ : Cl3, ∑ u₃ : Cl3,
          eps9Cl qinv u₁ u₂ u₃ * R34_R67_nine q qinv (eps9Cl qinv) u₁ u₂ u₃) =
      (q ^ 3) ^ 2 * epsNormSqRing qinv ^ 3 ∧
    (q ^ 2 + 1 + qinv ^ 2) ^ 2 *
        (∑ u₁ : Cl3, ∑ u₂ : Cl3, ∑ u₃ : Cl3,
          eps9Cl qinv u₁ u₂ u₃ * cyclic3Quark_nine q qinv (eps9Cl qinv) u₁ u₂ u₃) =
      (q ^ 3) ^ 2 * epsNormSqRing qinv ^ 3 := by
  have hscale := (epsNormSqRing_closed_form q qinv hq).2.2.2.2
  have hraw : (∑ u₁ : Cl3, ∑ u₂ : Cl3, ∑ u₃ : Cl3,
        eps9Cl qinv u₁ u₂ u₃ * R34_R67_nine q qinv (eps9Cl qinv) u₁ u₂ u₃) =
      (q * (1 + qinv ^ 2)) ^ 2 * epsNormSqRing qinv := by
    have hstep : ∀ u₂ : Cl3,
        (∑ u₁ : Cl3, ∑ u₃ : Cl3,
          eps9Cl qinv u₁ u₂ u₃ * R34_R67_nine q qinv (eps9Cl qinv) u₁ u₂ u₃) =
        (q * (1 + qinv ^ 2)) ^ 2 * (epsCl qinv u₂ * epsCl qinv u₂) := by
      rintro ⟨a₂, b₂, c₂⟩
      simp only [eps9Cl, R34_R67_nine, jR_eq_sum_jRMat, epsCl]
      have hexp : ∀ u₁ u₃ : Cl3,
          (epsRing qinv u₁.1 u₁.2.1 u₁.2.2 * epsRing qinv a₂ b₂ c₂ *
              epsRing qinv u₃.1 u₃.2.1 u₃.2.2) *
            (∑ c₁' : Fin 3, ∑ a₂' : Fin 3, jRMat q qinv u₁.2.2 a₂ c₁' a₂' *
              ∑ c₂' : Fin 3, ∑ a₃' : Fin 3, jRMat q qinv c₂ u₃.1 c₂' a₃' *
                (epsRing qinv u₁.1 u₁.2.1 c₁' * epsRing qinv a₂' b₂ c₂' *
                  epsRing qinv a₃' u₃.2.1 u₃.2.2)) =
          ∑ a₂' : Fin 3, ∑ c₂' : Fin 3,
            (epsRing qinv a₂ b₂ c₂ * epsRing qinv a₂' b₂ c₂') *
            (∑ c₁' : Fin 3, epsRing qinv u₁.1 u₁.2.1 u₁.2.2 * epsRing qinv u₁.1 u₁.2.1 c₁' *
              jRMat q qinv u₁.2.2 a₂ c₁' a₂') *
            (∑ a₃' : Fin 3, epsRing qinv u₃.1 u₃.2.1 u₃.2.2 * epsRing qinv a₃' u₃.2.1 u₃.2.2 *
              jRMat q qinv c₂ u₃.1 c₂' a₃') := by
        intro u₁ u₃
        simp only [Fin.sum_univ_three]
        ring
      simp_rw [hexp]
      calc _ = ∑ u₁ : Cl3, ∑ a₂' : Fin 3, ∑ c₂' : Fin 3, ∑ u₃ : Cl3,
              (epsRing qinv a₂ b₂ c₂ * epsRing qinv a₂' b₂ c₂') *
              (∑ c₁' : Fin 3, epsRing qinv u₁.1 u₁.2.1 u₁.2.2 * epsRing qinv u₁.1 u₁.2.1 c₁' *
                jRMat q qinv u₁.2.2 a₂ c₁' a₂') *
              (∑ a₃' : Fin 3, epsRing qinv u₃.1 u₃.2.1 u₃.2.2 * epsRing qinv a₃' u₃.2.1 u₃.2.2 *
                jRMat q qinv c₂ u₃.1 c₂' a₃') := by
              refine Finset.sum_congr rfl fun u₁ _ => ?_
              rw [Finset.sum_comm]
              refine Finset.sum_congr rfl fun a₂' _ => Finset.sum_comm
        _ = ∑ a₂' : Fin 3, ∑ c₂' : Fin 3,
              (epsRing qinv a₂ b₂ c₂ * epsRing qinv a₂' b₂ c₂') *
              (∑ u₁ : Cl3, ∑ c₁' : Fin 3,
                epsRing qinv u₁.1 u₁.2.1 u₁.2.2 * epsRing qinv u₁.1 u₁.2.1 c₁' *
                jRMat q qinv u₁.2.2 a₂ c₁' a₂') *
              (∑ u₃ : Cl3, ∑ a₃' : Fin 3,
                epsRing qinv u₃.1 u₃.2.1 u₃.2.2 * epsRing qinv a₃' u₃.2.1 u₃.2.2 *
                jRMat q qinv c₂ u₃.1 c₂' a₃') := by
              rw [Finset.sum_comm]
              refine Finset.sum_congr rfl fun a₂' _ => ?_
              rw [Finset.sum_comm]
              refine Finset.sum_congr rfl fun c₂' _ => ?_
              exact sum_factor_two _ _ _
        _ = (q * (1 + qinv ^ 2)) ^ 2 * (epsRing qinv a₂ b₂ c₂ * epsRing qinv a₂ b₂ c₂) := by
              have hu1 : ∀ a₂' : Fin 3,
                  (∑ u₁ : Cl3, ∑ c₁' : Fin 3,
                    epsRing qinv u₁.1 u₁.2.1 u₁.2.2 * epsRing qinv u₁.1 u₁.2.1 c₁' *
                    jRMat q qinv u₁.2.2 a₂ c₁' a₂') =
                  if a₂ = a₂' then q * (1 + qinv ^ 2) else 0 := by
                intro a₂'
                simp only [Fintype.sum_prod_type]
                exact schur_right_leaf_prune q qinv hq a₂ a₂'
              have hu3 : ∀ c₂' : Fin 3,
                  (∑ u₃ : Cl3, ∑ a₃' : Fin 3,
                    epsRing qinv u₃.1 u₃.2.1 u₃.2.2 * epsRing qinv a₃' u₃.2.1 u₃.2.2 *
                    jRMat q qinv c₂ u₃.1 c₂' a₃') =
                  if c₂ = c₂' then q * (1 + qinv ^ 2) else 0 := by
                intro c₂'
                simp only [Fintype.sum_prod_type]
                exact schur_left_leaf_prune q qinv hq c₂ c₂'
              simp_rw [hu1, hu3]
              fin_cases a₂ <;> fin_cases c₂ <;> simp <;> ring
    calc (∑ u₁ : Cl3, ∑ u₂ : Cl3, ∑ u₃ : Cl3,
            eps9Cl qinv u₁ u₂ u₃ * R34_R67_nine q qinv (eps9Cl qinv) u₁ u₂ u₃)
        = ∑ u₂ : Cl3, ∑ u₁ : Cl3, ∑ u₃ : Cl3,
            eps9Cl qinv u₁ u₂ u₃ * R34_R67_nine q qinv (eps9Cl qinv) u₁ u₂ u₃ := Finset.sum_comm
      _ = ∑ u₂ : Cl3, (q * (1 + qinv ^ 2)) ^ 2 * (epsCl qinv u₂ * epsCl qinv u₂) :=
            Finset.sum_congr rfl fun u₂ _ => hstep u₂
      _ = (q * (1 + qinv ^ 2)) ^ 2 * epsNormSqRing qinv := by
            rw [← Finset.mul_sum]; rfl
  have hcleared : (q ^ 2 + 1 + qinv ^ 2) ^ 2 *
        (∑ u₁ : Cl3, ∑ u₂ : Cl3, ∑ u₃ : Cl3,
          eps9Cl qinv u₁ u₂ u₃ * R34_R67_nine q qinv (eps9Cl qinv) u₁ u₂ u₃) =
      (q ^ 3) ^ 2 * epsNormSqRing qinv ^ 3 := by
    rw [hraw]
    calc (q ^ 2 + 1 + qinv ^ 2) ^ 2 * ((q * (1 + qinv ^ 2)) ^ 2 * epsNormSqRing qinv)
        = ((q ^ 2 + 1 + qinv ^ 2) * (q * (1 + qinv ^ 2))) ^ 2 * epsNormSqRing qinv := by ring
      _ = (q ^ 3 * epsNormSqRing qinv) ^ 2 * epsNormSqRing qinv := by rw [hscale]
      _ = (q ^ 3) ^ 2 * epsNormSqRing qinv ^ 3 := by ring
  refine ⟨hraw, hcleared, ?_⟩
  have hcyc_raw : (∑ u₁ : Cl3, ∑ u₂ : Cl3, ∑ u₃ : Cl3,
        eps9Cl qinv u₁ u₂ u₃ * cyclic3Quark_nine q qinv (eps9Cl qinv) u₁ u₂ u₃) =
      (q * (1 + qinv ^ 2)) ^ 2 * epsNormSqRing qinv := by
    have hstep_cyc : ∀ u₃ : Cl3,
        (∑ u₁ : Cl3, ∑ u₂ : Cl3,
          eps9Cl qinv u₁ u₂ u₃ * cyclic3Quark_nine q qinv (eps9Cl qinv) u₁ u₂ u₃) =
        ∑ c₃' : Fin 3, (q * (1 + qinv ^ 2)) ^ 2 *
          (if u₃.2.2 = c₃' then epsCl qinv u₃ * epsRing qinv u₃.1 u₃.2.1 c₃' else 0) := by
      intro u₃
      simp only [eps9Cl, cyclic3Quark_nine, jR_eq_sum_jRMat, epsCl]
      have hexp : ∀ u₁ u₂ : Cl3,
          (epsRing qinv u₁.1 u₁.2.1 u₁.2.2 * epsRing qinv u₂.1 u₂.2.1 u₂.2.2 *
              epsRing qinv u₃.1 u₃.2.1 u₃.2.2) *
            (∑ c₁' : Fin 3, ∑ x : Fin 3, jRMat q qinv u₁.2.2 u₂.2.2 c₁' x *
              ∑ c₂' : Fin 3, ∑ c₃' : Fin 3, jRMat q qinv x u₃.2.2 c₂' c₃' *
                (epsRing qinv u₁.1 u₁.2.1 c₁' * epsRing qinv u₂.1 u₂.2.1 c₂' *
                  epsRing qinv u₃.1 u₃.2.1 c₃')) =
          ∑ x : Fin 3,
            (∑ c₂' : Fin 3, ∑ c₃' : Fin 3,
              (epsRing qinv u₂.1 u₂.2.1 u₂.2.2 * epsRing qinv u₂.1 u₂.2.1 c₂' *
                jRMat q qinv x u₃.2.2 c₂' c₃') *
              (epsRing qinv u₃.1 u₃.2.1 u₃.2.2 * epsRing qinv u₃.1 u₃.2.1 c₃')) *
            (∑ c₁' : Fin 3, epsRing qinv u₁.1 u₁.2.1 u₁.2.2 * epsRing qinv u₁.1 u₁.2.1 c₁' *
              jRMat q qinv u₁.2.2 u₂.2.2 c₁' x) := by
        intro u₁ u₂
        simp only [Fin.sum_univ_three]
        ring
      simp_rw [hexp]
      rw [Finset.sum_comm]
      have hu2_step : ∀ u₂ : Cl3,
          (∑ u₁ : Cl3, ∑ x : Fin 3,
            (∑ c₂' : Fin 3, ∑ c₃' : Fin 3,
              (epsRing qinv u₂.1 u₂.2.1 u₂.2.2 * epsRing qinv u₂.1 u₂.2.1 c₂' *
                jRMat q qinv x u₃.2.2 c₂' c₃') *
              (epsRing qinv u₃.1 u₃.2.1 u₃.2.2 * epsRing qinv u₃.1 u₃.2.1 c₃')) *
            (∑ c₁' : Fin 3, epsRing qinv u₁.1 u₁.2.1 u₁.2.2 * epsRing qinv u₁.1 u₁.2.1 c₁' *
              jRMat q qinv u₁.2.2 u₂.2.2 c₁' x)) =
          ∑ c₃' : Fin 3, (q * (1 + qinv ^ 2)) *
            (epsRing qinv u₃.1 u₃.2.1 u₃.2.2 * epsRing qinv u₃.1 u₃.2.1 c₃') *
            (∑ c₂' : Fin 3, epsRing qinv u₂.1 u₂.2.1 u₂.2.2 * epsRing qinv u₂.1 u₂.2.1 c₂' *
              jRMat q qinv u₂.2.2 u₃.2.2 c₂' c₃') := by
        intro u₂
        rw [Finset.sum_comm]
        simp_rw [← Finset.mul_sum]
        have hu1_prune : ∀ x : Fin 3,
            (∑ u₁ : Cl3, ∑ c₁' : Fin 3,
              epsRing qinv u₁.1 u₁.2.1 u₁.2.2 * epsRing qinv u₁.1 u₁.2.1 c₁' *
              jRMat q qinv u₁.2.2 u₂.2.2 c₁' x) =
            if u₂.2.2 = x then q * (1 + qinv ^ 2) else 0 := by
          intro x
          simp only [Fintype.sum_prod_type]
          exact schur_right_leaf_prune q qinv hq u₂.2.2 x
        simp_rw [hu1_prune]
        rcases u₂ with ⟨a₂, b₂, c₂⟩
        fin_cases c₂ <;> simp [Fin.sum_univ_three] <;> ring
      simp_rw [hu2_step]
      rw [Finset.sum_comm]
      refine Finset.sum_congr rfl fun c₃' _ => ?_
      simp_rw [← Finset.mul_sum]
      have hu2_prune : (∑ u₂ : Cl3, ∑ c₂' : Fin 3,
            epsRing qinv u₂.1 u₂.2.1 u₂.2.2 * epsRing qinv u₂.1 u₂.2.1 c₂' *
              jRMat q qinv u₂.2.2 u₃.2.2 c₂' c₃') =
          if u₃.2.2 = c₃' then q * (1 + qinv ^ 2) else 0 := by
        simp only [Fintype.sum_prod_type]
        exact schur_right_leaf_prune q qinv hq u₃.2.2 c₃'
      rw [hu2_prune]
      split_ifs <;> ring
    calc (∑ u₁ : Cl3, ∑ u₂ : Cl3, ∑ u₃ : Cl3,
            eps9Cl qinv u₁ u₂ u₃ * cyclic3Quark_nine q qinv (eps9Cl qinv) u₁ u₂ u₃)
        = ∑ u₁ : Cl3, ∑ u₃ : Cl3, ∑ u₂ : Cl3,
            eps9Cl qinv u₁ u₂ u₃ * cyclic3Quark_nine q qinv (eps9Cl qinv) u₁ u₂ u₃ :=
            Finset.sum_congr rfl fun _ _ => Finset.sum_comm
      _ = ∑ u₃ : Cl3, ∑ u₁ : Cl3, ∑ u₂ : Cl3,
            eps9Cl qinv u₁ u₂ u₃ * cyclic3Quark_nine q qinv (eps9Cl qinv) u₁ u₂ u₃ := Finset.sum_comm
      _ = ∑ u₃ : Cl3, ∑ c₃' : Fin 3, (q * (1 + qinv ^ 2)) ^ 2 *
            (if u₃.2.2 = c₃' then epsCl qinv u₃ * epsRing qinv u₃.1 u₃.2.1 c₃' else 0) :=
            Finset.sum_congr rfl fun u₃ _ => hstep_cyc u₃
      _ = (q * (1 + qinv ^ 2)) ^ 2 * epsNormSqRing qinv := by
            have hcollapse : ∀ u₃ : Cl3,
                (∑ c₃' : Fin 3, (q * (1 + qinv ^ 2)) ^ 2 *
                  (if u₃.2.2 = c₃' then epsCl qinv u₃ * epsRing qinv u₃.1 u₃.2.1 c₃' else 0)) =
                (q * (1 + qinv ^ 2)) ^ 2 * (epsCl qinv u₃ * epsCl qinv u₃) := by
              rintro ⟨a₃, b₃, c₃⟩
              fin_cases c₃ <;> simp [epsCl]
            simp_rw [hcollapse, ← Finset.mul_sum]
            rfl
  rw [hcyc_raw]
  calc (q ^ 2 + 1 + qinv ^ 2) ^ 2 * ((q * (1 + qinv ^ 2)) ^ 2 * epsNormSqRing qinv)
      = ((q ^ 2 + 1 + qinv ^ 2) * (q * (1 + qinv ^ 2))) ^ 2 * epsNormSqRing qinv := by ring
    _ = (q ^ 3 * epsNormSqRing qinv) ^ 2 * epsNormSqRing qinv := by rw [hscale]
    _ = (q ^ 3) ^ 2 * epsNormSqRing qinv ^ 3 := by ring

/-- `[Field K]` specialization of `nineQuark_R34_R67_and_cyclic_overlap_ring` (`JimboGl3Singlet`). -/
theorem nineQuark_R34_R67_overlap_field {K : Type*} [Field K]
    (q : K) (hq : q ≠ 0) (hq3 : q ^ 2 + 1 + q⁻¹ ^ 2 ≠ 0) :
    (∑ u₁ : Cl3, ∑ u₂ : Cl3, ∑ u₃ : Cl3,
        eps9Cl q⁻¹ u₁ u₂ u₃ * R34_R67_nine q q⁻¹ (eps9Cl q⁻¹) u₁ u₂ u₃) =
      (q ^ 3 / (q ^ 2 + 1 + q⁻¹ ^ 2)) ^ 2 * epsNormSqRing q⁻¹ ^ 3 := by
  have hcl := (nineQuark_R34_R67_and_cyclic_overlap_ring q q⁻¹ (mul_inv_cancel₀ hq)).2.1
  have hsq : (q ^ 2 + 1 + q⁻¹ ^ 2) ^ 2 ≠ 0 := pow_ne_zero 2 hq3
  apply mul_left_cancel₀ hsq
  rw [hcl, div_pow, ← mul_assoc, mul_div_cancel₀ _ hsq]

private theorem pull_fourth_interface {α R : Type*} [Fintype α] [CommRing R]
    (E E₄ : R) (j₁ j₂ j₃ : α → α → R) (k₁ : α → R) (k₂ k₃ : α → α → R) (k₄ : α → R) :
    (E * E₄) *
      (∑ c₁' : α, ∑ a₂' : α, j₁ c₁' a₂' *
        ∑ c₂' : α, ∑ a₃' : α, j₂ c₂' a₃' *
          ∑ c₃' : α, ∑ a₄' : α, j₃ c₃' a₄' * (k₁ c₁' * k₂ a₂' c₂' * k₃ a₃' c₃' * k₄ a₄')) =
    ∑ c₃' : α,
      (E * (∑ c₁' : α, ∑ a₂' : α, j₁ c₁' a₂' *
        ∑ c₂' : α, ∑ a₃' : α, j₂ c₂' a₃' * (k₁ c₁' * k₂ a₂' c₂' * k₃ a₃' c₃'))) *
      (∑ a₄' : α, E₄ * k₄ a₄' * j₃ c₃' a₄') := by
  let S₄ : α → R := fun c₃' => ∑ a₄' : α, E₄ * k₄ a₄' * j₃ c₃' a₄'
  have hin : ∀ c₁' a₂' c₂' a₃' : α,
      E₄ * (∑ c₃' : α, ∑ a₄' : α, j₃ c₃' a₄' * (k₁ c₁' * k₂ a₂' c₂' * k₃ a₃' c₃' * k₄ a₄')) =
      ∑ c₃' : α, (k₁ c₁' * k₂ a₂' c₂' * k₃ a₃' c₃') * S₄ c₃' := by
    intro c₁' a₂' c₂' a₃'
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun c₃' _ => ?_
    dsimp only [S₄]
    rw [Finset.mul_sum, Finset.mul_sum]
    refine Finset.sum_congr rfl fun a₄' _ => by ring
  have hE4 :
      E₄ * (∑ c₁' : α, ∑ a₂' : α, j₁ c₁' a₂' *
        ∑ c₂' : α, ∑ a₃' : α, j₂ c₂' a₃' *
          ∑ c₃' : α, ∑ a₄' : α, j₃ c₃' a₄' * (k₁ c₁' * k₂ a₂' c₂' * k₃ a₃' c₃' * k₄ a₄')) =
      ∑ c₁' : α, ∑ a₂' : α, j₁ c₁' a₂' *
        ∑ c₂' : α, ∑ a₃' : α, j₂ c₂' a₃' *
          ∑ c₃' : α, (k₁ c₁' * k₂ a₂' c₂' * k₃ a₃' c₃') * S₄ c₃' := by
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun c₁' _ => ?_
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun a₂' _ => ?_
    rw [← mul_assoc, mul_comm E₄, mul_assoc]
    congr 1
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun c₂' _ => ?_
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun a₃' _ => ?_
    rw [← mul_assoc, mul_comm E₄, mul_assoc, hin]
  rw [mul_assoc E E₄, hE4]
  change _ = ∑ c₃' : α,
    (E * (∑ c₁' : α, ∑ a₂' : α, j₁ c₁' a₂' *
      ∑ c₂' : α, ∑ a₃' : α, j₂ c₂' a₃' * (k₁ c₁' * k₂ a₂' c₂' * k₃ a₃' c₃'))) * S₄ c₃'
  simp_rw [Finset.mul_sum, Finset.sum_mul]
  conv_lhs => enter [2, c₁', 2, a₂', 2, c₂']; rw [Finset.sum_comm]
  conv_lhs => enter [2, c₁', 2, a₂']; rw [Finset.sum_comm]
  conv_lhs => enter [2, c₁']; rw [Finset.sum_comm]
  conv_lhs => rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun c₃' _ => Finset.sum_congr rfl fun c₁' _ =>
    Finset.sum_congr rfl fun a₂' _ => Finset.sum_congr rfl fun c₂' _ =>
      Finset.sum_congr rfl fun a₃' _ => by ring

/-- **Exact `12q` `Ř_{3,4} Ř_{6,7} Ř_{9,10}` overlap over `[CommRing R]`:**
`(q² + 1 + qinv²)³ · ⟨ε_q^{⊗ 4} | Ř_{3,4} Ř_{6,7} Ř_{9,10} | ε_q^{⊗ 4}⟩ = (q³)³ · (epsNormSqRing qinv)⁴`. -/
theorem twelveQuark_R34_R67_R910_overlap_ring {R : Type*} [CommRing R]
    (q qinv : R) (hq : q * qinv = 1) :
    (∑ u₁ : Cl3, ∑ u₂ : Cl3, ∑ u₃ : Cl3, ∑ u₄ : Cl3,
        eps12Cl qinv u₁ u₂ u₃ u₄ * R34_R67_R910_twelve q qinv (eps12Cl qinv) u₁ u₂ u₃ u₄) =
      (q * (1 + qinv ^ 2)) ^ 3 * epsNormSqRing qinv ∧
    (q ^ 2 + 1 + qinv ^ 2) ^ 3 *
        (∑ u₁ : Cl3, ∑ u₂ : Cl3, ∑ u₃ : Cl3, ∑ u₄ : Cl3,
          eps12Cl qinv u₁ u₂ u₃ u₄ * R34_R67_R910_twelve q qinv (eps12Cl qinv) u₁ u₂ u₃ u₄) =
      (q ^ 3) ^ 3 * epsNormSqRing qinv ^ 4 := by
  have hscale := (epsNormSqRing_closed_form q qinv hq).2.2.2.2
  have hred4 : ∀ u₁ u₂ u₃ : Cl3,
      (∑ u₄ : Cl3,
        eps12Cl qinv u₁ u₂ u₃ u₄ * R34_R67_R910_twelve q qinv (eps12Cl qinv) u₁ u₂ u₃ u₄) =
      (q * (1 + qinv ^ 2)) *
        (eps9Cl qinv u₁ u₂ u₃ * R34_R67_nine q qinv (eps9Cl qinv) u₁ u₂ u₃) := by
    intro u₁ u₂ u₃
    simp only [eps12Cl, eps9Cl, R34_R67_R910_twelve, R34_R67_nine, jR_eq_sum_jRMat, epsCl]
    let F : Fin 3 → R := fun c₃' =>
      (epsRing qinv u₁.1 u₁.2.1 u₁.2.2 * epsRing qinv u₂.1 u₂.2.1 u₂.2.2 *
          epsRing qinv u₃.1 u₃.2.1 u₃.2.2) *
        (∑ c₁' : Fin 3, ∑ a₂' : Fin 3, jRMat q qinv u₁.2.2 u₂.1 c₁' a₂' *
          ∑ c₂' : Fin 3, ∑ a₃' : Fin 3, jRMat q qinv u₂.2.2 u₃.1 c₂' a₃' *
            (epsRing qinv u₁.1 u₁.2.1 c₁' * epsRing qinv a₂' u₂.2.1 c₂' *
              epsRing qinv a₃' u₃.2.1 c₃'))
    have hinner : ∀ u₄ : Cl3,
        (epsRing qinv u₁.1 u₁.2.1 u₁.2.2 * epsRing qinv u₂.1 u₂.2.1 u₂.2.2 *
            epsRing qinv u₃.1 u₃.2.1 u₃.2.2 * epsRing qinv u₄.1 u₄.2.1 u₄.2.2) *
          (∑ c₁' : Fin 3, ∑ a₂' : Fin 3, jRMat q qinv u₁.2.2 u₂.1 c₁' a₂' *
            ∑ c₂' : Fin 3, ∑ a₃' : Fin 3, jRMat q qinv u₂.2.2 u₃.1 c₂' a₃' *
              ∑ c₃' : Fin 3, ∑ a₄' : Fin 3, jRMat q qinv u₃.2.2 u₄.1 c₃' a₄' *
                (epsRing qinv u₁.1 u₁.2.1 c₁' * epsRing qinv a₂' u₂.2.1 c₂' *
                  epsRing qinv a₃' u₃.2.1 c₃' * epsRing qinv a₄' u₄.2.1 u₄.2.2)) =
        ∑ c₃' : Fin 3, F c₃' *
          (∑ a₄' : Fin 3, epsRing qinv u₄.1 u₄.2.1 u₄.2.2 * epsRing qinv a₄' u₄.2.1 u₄.2.2 *
            jRMat q qinv u₃.2.2 u₄.1 c₃' a₄') := by
      intro u₄
      exact pull_fourth_interface
        (epsRing qinv u₁.1 u₁.2.1 u₁.2.2 * epsRing qinv u₂.1 u₂.2.1 u₂.2.2 *
          epsRing qinv u₃.1 u₃.2.1 u₃.2.2)
        (epsRing qinv u₄.1 u₄.2.1 u₄.2.2)
        (jRMat q qinv u₁.2.2 u₂.1) (jRMat q qinv u₂.2.2 u₃.1) (jRMat q qinv u₃.2.2 u₄.1)
        (fun c₁' => epsRing qinv u₁.1 u₁.2.1 c₁')
        (fun a₂' c₂' => epsRing qinv a₂' u₂.2.1 c₂')
        (fun a₃' c₃' => epsRing qinv a₃' u₃.2.1 c₃')
        (fun a₄' => epsRing qinv a₄' u₄.2.1 u₄.2.2)
    simp_rw [hinner]
    rw [Finset.sum_comm]
    have hu4_prune : ∀ c₃' : Fin 3,
        (∑ u₄ : Cl3, ∑ a₄' : Fin 3,
          epsRing qinv u₄.1 u₄.2.1 u₄.2.2 * epsRing qinv a₄' u₄.2.1 u₄.2.2 *
          jRMat q qinv u₃.2.2 u₄.1 c₃' a₄') =
        if u₃.2.2 = c₃' then q * (1 + qinv ^ 2) else 0 := by
      intro c₃'
      simp only [Fintype.sum_prod_type]
      exact schur_left_leaf_prune q qinv hq u₃.2.2 c₃'
    simp_rw [← Finset.mul_sum, hu4_prune]
    rcases u₃ with ⟨a₃, b₃, c₃⟩
    have hsel : ∀ (G : Fin 3 → R) (c : Fin 3),
        (∑ c₃' : Fin 3, G c₃' * (if c = c₃' then q * (1 + qinv ^ 2) else 0)) =
        (q * (1 + qinv ^ 2)) * G c := by
      intro G c
      fin_cases c <;> simp <;> ring
    exact hsel F c₃
  have hraw9 := (nineQuark_R34_R67_and_cyclic_overlap_ring q qinv hq).1
  have hraw12 : (∑ u₁ : Cl3, ∑ u₂ : Cl3, ∑ u₃ : Cl3, ∑ u₄ : Cl3,
        eps12Cl qinv u₁ u₂ u₃ u₄ * R34_R67_R910_twelve q qinv (eps12Cl qinv) u₁ u₂ u₃ u₄) =
      (q * (1 + qinv ^ 2)) ^ 3 * epsNormSqRing qinv := by
    simp_rw [hred4, ← Finset.mul_sum]
    rw [hraw9]
    ring
  refine ⟨hraw12, ?_⟩
  rw [hraw12]
  calc (q ^ 2 + 1 + qinv ^ 2) ^ 3 * ((q * (1 + qinv ^ 2)) ^ 3 * epsNormSqRing qinv)
      = ((q ^ 2 + 1 + qinv ^ 2) * (q * (1 + qinv ^ 2))) ^ 3 * epsNormSqRing qinv := by ring
    _ = (q ^ 3 * epsNormSqRing qinv) ^ 3 * epsNormSqRing qinv := by rw [hscale]
    _ = (q ^ 3) ^ 3 * epsNormSqRing qinv ^ 4 := by ring

/-- `[Field K]` specialization of `twelveQuark_R34_R67_R910_overlap_ring`. -/
theorem twelveQuark_R34_R67_R910_overlap_field {K : Type*} [Field K]
    (q : K) (hq : q ≠ 0) (hq3 : q ^ 2 + 1 + q⁻¹ ^ 2 ≠ 0) :
    (∑ u₁ : Cl3, ∑ u₂ : Cl3, ∑ u₃ : Cl3, ∑ u₄ : Cl3,
        eps12Cl q⁻¹ u₁ u₂ u₃ u₄ * R34_R67_R910_twelve q q⁻¹ (eps12Cl q⁻¹) u₁ u₂ u₃ u₄) =
      (q ^ 3 / (q ^ 2 + 1 + q⁻¹ ^ 2)) ^ 3 * epsNormSqRing q⁻¹ ^ 4 := by
  have hcl := (twelveQuark_R34_R67_R910_overlap_ring q q⁻¹ (mul_inv_cancel₀ hq)).2
  have hcb : (q ^ 2 + 1 + q⁻¹ ^ 2) ^ 3 ≠ 0 := pow_ne_zero 3 hq3
  apply mul_left_cancel₀ hcb
  rw [hcl, div_pow, ← mul_assoc, mul_div_cancel₀ _ hcb]

/-! ### §3b. Closed `9q` Triangular Plaquette (`Ř_{3,4} Ř_{6,7} Ř_{9,1}`) & Closed `12q` Tetrahedral Ring (`Ř_{3,4} Ř_{6,7} Ř_{9,10} Ř_{12,1}`) -/

/-- Closed 3-interface triangular plaquette `Ř_{3,4}(q) Ř_{6,7}(q) Ř_{9,1}(q)` on `9q` tensors. -/
def closedTriangle_nine {R : Type*} [CommRing R] (q qinv : R)
    (W : Cl3 → Cl3 → Cl3 → R) : Cl3 → Cl3 → Cl3 → R :=
  fun u₁ u₂ u₃ =>
    jR q qinv (fun c₁' a₂' =>
      jR q qinv (fun c₂' a₃' =>
        jR q qinv (fun c₃' a₁' =>
          W (a₁', u₁.2.1, c₁') (a₂', u₂.2.1, c₂') (a₃', u₃.2.1, c₃'))
          u₃.2.2 u₁.1) u₂.2.2 u₃.1) u₁.2.2 u₂.1

/-- Closed 4-interface tetrahedral Hamiltonian ring `Ř_{3,4}(q) Ř_{6,7}(q) Ř_{9,10}(q) Ř_{12,1}(q)`
on `12q` tensors. -/
def closedRing_twelve {R : Type*} [CommRing R] (q qinv : R)
    (W : Cl3 → Cl3 → Cl3 → Cl3 → R) : Cl3 → Cl3 → Cl3 → Cl3 → R :=
  fun u₁ u₂ u₃ u₄ =>
    jR q qinv (fun c₁' a₂' =>
      jR q qinv (fun c₂' a₃' =>
        jR q qinv (fun c₃' a₄' =>
          jR q qinv (fun c₄' a₁' =>
            W (a₁', u₁.2.1, c₁') (a₂', u₂.2.1, c₂') (a₃', u₃.2.1, c₃') (a₄', u₄.2.1, c₄'))
            u₄.2.2 u₁.1) u₃.2.2 u₄.1) u₂.2.2 u₃.1) u₁.2.2 u₂.1

/-- The exact `3 × 3` stay-branch cluster transfer matrix `M(q)`. -/
def clusterStepMat {R : Type*} [CommRing R] (q qinv : R) : Matrix (Fin 3) (Fin 3) R :=
  Matrix.of ![![q - qinv ^ 3, q, q],
              ![qinv, qinv - qinv ^ 3, qinv],
              ![qinv ^ 3, qinv ^ 3, 0]]

/-- Exact `(Fin 3 × Fin 3) × (Fin 3 × Fin 3)` (`9 × 9`) pair-channel transfer matrix encoding one
3-quark cluster + interface `jR` step around any closed `k`-cluster colour-flux ring. -/
def ringPairTransfer {R : Type*} [CommRing R] (q qinv : R) :
    Matrix (Fin 3 × Fin 3) (Fin 3 × Fin 3) R :=
  fun p₁ p₂ =>
    ∑ c : Fin 3, ∑ c' : Fin 3,
      clSpectatorW qinv p₁.1 c p₁.2 c' * jRMat q qinv c p₂.1 c' p₂.2

/-- Exact closed form of spectator contraction `clSpectatorW` (`81` tiny cases, eliminating `b : Fin 3`). -/
private theorem clSpectatorW_eval {R : Type*} [CommRing R] (qinv : R) (a c a' c' : Fin 3) :
    clSpectatorW qinv a c a' c' =
      if a = c then 0
      else if a' = a ∧ c' = c then
        (if a = 0 ∧ c = 2 then 1
         else if (a = 0 ∧ c = 1) ∨ (a = 1 ∧ c = 2) then qinv ^ 2
         else if (a = 1 ∧ c = 0) ∨ (a = 2 ∧ c = 1) then qinv ^ 4
         else qinv ^ 6)
      else if a' = c ∧ c' = a then -qinv ^ 3
      else 0 := by
  fin_cases a <;> fin_cases c <;> fin_cases a' <;> fin_cases c' <;>
    simp [clSpectatorW, epsRing] <;> ring

private def ringBlockGen {R : Type*} [CommRing R]
    (A : Matrix (Fin 3) (Fin 3) R) (x : R) : Matrix (Fin 3 × Fin 3) (Fin 3 × Fin 3) R :=
  fun p₁ p₂ =>
    if p₁.1 = p₁.2 then
      if p₂.1 = p₂.2 then A p₁.1 p₂.1 else 0
    else if p₂.1 = p₁.1 ∧ p₂.2 = p₁.2 then x else 0

private theorem qinv_pow_mul_q {R : Type*} [CommRing R] (q qinv : R) (hq : q * qinv = 1) :
    qinv ^ 2 * q = qinv ∧ qinv ^ 4 * q = qinv ^ 3 ∧ qinv ^ 6 * q = qinv ^ 5 := by
  refine ⟨?_, ?_, ?_⟩
  · calc qinv ^ 2 * q = qinv * (q * qinv) := by ring
      _ = qinv := by rw [hq, mul_one]
  · calc qinv ^ 4 * q = qinv ^ 3 * (q * qinv) := by ring
      _ = qinv ^ 3 := by rw [hq, mul_one]
  · calc qinv ^ 6 * q = qinv ^ 5 * (q * qinv) := by ring
      _ = qinv ^ 5 := by rw [hq, mul_one]

private theorem ringPairTransfer_row0 {R : Type*} [CommRing R]
    (q qinv : R) (hq : q * qinv = 1) (a₁' a₂ a₂' : Fin 3) :
    ringPairTransfer q qinv (0, a₁') (a₂, a₂') =
      ringBlockGen (clusterStepMat q qinv) (-qinv ^ 3) (0, a₁') (a₂, a₂') := by
  obtain ⟨hq2, _, _⟩ := qinv_pow_mul_q q qinv hq
  rw [ringPairTransfer]
  simp_rw [clSpectatorW_eval]
  fin_cases a₁' <;> simp only [Fin.sum_univ_three]
  all_goals
    fin_cases a₂ <;> fin_cases a₂' <;>
      simp [ringBlockGen, jRMat, clusterStepMat, mul_sub] <;>
      (try rw [hq2]) <;> ring

private theorem ringPairTransfer_row1 {R : Type*} [CommRing R]
    (q qinv : R) (hq : q * qinv = 1) (a₁' a₂ a₂' : Fin 3) :
    ringPairTransfer q qinv (1, a₁') (a₂, a₂') =
      ringBlockGen (clusterStepMat q qinv) (-qinv ^ 3) (1, a₁') (a₂, a₂') := by
  obtain ⟨hq2, hq4, _⟩ := qinv_pow_mul_q q qinv hq
  rw [ringPairTransfer]
  simp_rw [clSpectatorW_eval]
  fin_cases a₁' <;> simp only [Fin.sum_univ_three]
  all_goals
    fin_cases a₂ <;> fin_cases a₂' <;>
      simp [ringBlockGen, jRMat, clusterStepMat, mul_sub] <;>
      (try rw [hq2]) <;> (try rw [hq4]) <;> ring

private theorem ringPairTransfer_row2 {R : Type*} [CommRing R]
    (q qinv : R) (hq : q * qinv = 1) (a₁' a₂ a₂' : Fin 3) :
    ringPairTransfer q qinv (2, a₁') (a₂, a₂') =
      ringBlockGen (clusterStepMat q qinv) (-qinv ^ 3) (2, a₁') (a₂, a₂') := by
  obtain ⟨_, hq4, hq6⟩ := qinv_pow_mul_q q qinv hq
  rw [ringPairTransfer]
  simp_rw [clSpectatorW_eval]
  fin_cases a₁' <;> simp only [Fin.sum_univ_three]
  all_goals
    fin_cases a₂ <;> fin_cases a₂' <;>
      simp [ringBlockGen, jRMat, clusterStepMat, mul_sub] <;>
      (try rw [hq4]) <;> (try rw [hq6]) <;> ring

private theorem ringPairTransfer_eq_block {R : Type*} [CommRing R]
    (q qinv : R) (hq : q * qinv = 1) :
    ringPairTransfer q qinv = ringBlockGen (clusterStepMat q qinv) (-qinv ^ 3) := by
  ext ⟨a₁, a₁'⟩ ⟨a₂, a₂'⟩
  fin_cases a₁
  · exact ringPairTransfer_row0 q qinv hq a₁' a₂ a₂'
  · exact ringPairTransfer_row1 q qinv hq a₁' a₂ a₂'
  · exact ringPairTransfer_row2 q qinv hq a₁' a₂ a₂'

private theorem block9_mul {R : Type*} [CommRing R]
    (A B : Matrix (Fin 3) (Fin 3) R) (x y : R) :
    ringBlockGen A x * ringBlockGen B y = ringBlockGen (A * B) (x * y) := by
  ext ⟨a₁, a₁'⟩ ⟨a₂, a₂'⟩
  simp only [Matrix.mul_apply, Fintype.sum_prod_type]
  fin_cases a₁ <;> fin_cases a₁' <;> fin_cases a₂ <;> fin_cases a₂' <;>
    simp [ringBlockGen, Matrix.mul_apply, Fin.sum_univ_three]

/-- **Rank-1 Decomposition of `clusterStepMat` & Exact Block Structure of `ringPairTransfer`:**
Over any `[CommRing R]` with `q * qinv = 1`:
1. `clusterStepMat q qinv + qinv³ • 1 = vecMulVec ![q, qinv, qinv³] ![1, 1, 1]` (rank 1);
2. `Tr(ringPairTransfer³) = (q + qinv)³ - 8 · qinv⁹` and
   `Tr(ringPairTransfer⁴) = (q + qinv)⁴ + 8 · qinv¹²`. -/
theorem clusterStepMat_rankOne_and_ringTraces {R : Type*} [CommRing R]
    (q qinv : R) (hq : q * qinv = 1) :
    clusterStepMat q qinv + qinv ^ 3 • (1 : Matrix (Fin 3) (Fin 3) R) =
      Matrix.vecMulVec ![q, qinv, qinv ^ 3] ![1, 1, 1] ∧
    Matrix.trace (ringPairTransfer q qinv ^ 3) = (q + qinv) ^ 3 - 8 * qinv ^ 9 ∧
    Matrix.trace (ringPairTransfer q qinv ^ 4) = (q + qinv) ^ 4 + 8 * qinv ^ 12 := by
  have hrk1 : clusterStepMat q qinv + qinv ^ 3 • (1 : Matrix (Fin 3) (Fin 3) R) =
      Matrix.vecMulVec ![q, qinv, qinv ^ 3] ![1, 1, 1] := by
    ext i j
    fin_cases i <;> fin_cases j <;> simp [clusterStepMat, Matrix.vecMulVec]
  let T0 := ringBlockGen (clusterStepMat q qinv) (-qinv ^ 3)
  have hT_eq : ringPairTransfer q qinv = T0 := ringPairTransfer_eq_block q qinv hq
  let R1 : Matrix (Fin 3) (Fin 3) R := Matrix.vecMulVec ![q, qinv, qinv ^ 3] ![1, 1, 1]
  let d : R := qinv ^ 3
  let s : R := q + qinv + qinv ^ 3
  have hM : clusterStepMat q qinv = (1 : R) • R1 + (-d) • (1 : Matrix (Fin 3) (Fin 3) R) := by
    ext i j
    fin_cases i <;> fin_cases j <;> simp [clusterStepMat, R1, d] <;> ring
  have hstep : ∀ a b : R,
      (a • R1 + b • (1 : Matrix (Fin 3) (Fin 3) R)) * clusterStepMat q qinv =
      (a * s - a * d + b) • R1 + (-b * d) • (1 : Matrix (Fin 3) (Fin 3) R) := by
    intro a b
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp [clusterStepMat, R1, d, s, Matrix.mul_apply, Fin.sum_univ_three] <;>
      ring
  have hM2 : clusterStepMat q qinv ^ 2 =
      ((1 : R) * s - (1 : R) * d + (-d)) • R1 + (-(-d) * d) • (1 : Matrix (Fin 3) (Fin 3) R) := by
    calc clusterStepMat q qinv ^ 2
        = ((1 : R) • R1 + (-d) • (1 : Matrix (Fin 3) (Fin 3) R)) * clusterStepMat q qinv := by
            rw [sq]; nth_rw 1 [hM]
      _ = _ := hstep 1 (-d)
  have hM3 : clusterStepMat q qinv ^ 3 =
      (((1 : R) * s - (1 : R) * d + (-d)) * s -
        ((1 : R) * s - (1 : R) * d + (-d)) * d + (-(-d) * d)) • R1 +
      (-(-(-d) * d) * d) • (1 : Matrix (Fin 3) (Fin 3) R) := by
    rw [pow_succ, hM2]
    exact hstep _ _
  have hM4 : clusterStepMat q qinv ^ 4 =
      ((((1 : R) * s - (1 : R) * d + (-d)) * s -
        ((1 : R) * s - (1 : R) * d + (-d)) * d + (-(-d) * d)) * s -
       (((1 : R) * s - (1 : R) * d + (-d)) * s -
        ((1 : R) * s - (1 : R) * d + (-d)) * d + (-(-d) * d)) * d +
       (-(-(-d) * d) * d)) • R1 +
      (-(-(-(-d) * d) * d) * d) • (1 : Matrix (Fin 3) (Fin 3) R) := by
    rw [pow_succ, hM3]
    exact hstep _ _
  have htr_lin : ∀ a b : R,
      Matrix.trace (a • R1 + b • (1 : Matrix (Fin 3) (Fin 3) R)) = a * s + 3 * b := by
    intro a b
    simp [Matrix.trace, Matrix.diag, R1, s, Fin.sum_univ_three]
    ring
  have htrM3 : Matrix.trace (clusterStepMat q qinv ^ 3) = (q + qinv) ^ 3 - 2 * qinv ^ 9 := by
    rw [hM3, htr_lin]
    dsimp only [s, d]; ring
  have htrM4 : Matrix.trace (clusterStepMat q qinv ^ 4) = (q + qinv) ^ 4 + 2 * qinv ^ 12 := by
    rw [hM4, htr_lin]
    dsimp only [s, d]; ring
  have hblock_pow : ∀ n : ℕ,
      T0 ^ (n + 1) = ringBlockGen (clusterStepMat q qinv ^ (n + 1)) ((-qinv ^ 3) ^ (n + 1)) := by
    intro n
    induction n with
    | zero => simp [T0]
    | succ k ih =>
      rw [pow_succ T0 (k + 1), ih, pow_succ (clusterStepMat q qinv) (k + 1),
        pow_succ (-qinv ^ 3) (k + 1)]
      exact block9_mul _ _ _ _
  have htr_block : ∀ (M : Matrix (Fin 3) (Fin 3) R) (z : R),
      Matrix.trace (ringBlockGen M z) = Matrix.trace M + 6 * z := by
    intro M z
    simp [ringBlockGen, Matrix.trace, Matrix.diag, Fintype.sum_prod_type, Fin.sum_univ_three]
    ring
  rw [hT_eq]
  refine ⟨hrk1, ?_, ?_⟩
  · rw [hblock_pow 2, htr_block, htrM3]; ring
  · rw [hblock_pow 3, htr_block, htrM4]; ring

/-- Single-cluster ket-interface kernel `∑_{c'} jRMat c a_next c' a_next' * epsRing a_in' b c'`. -/
private def ketEdge {R : Type*} [CommRing R] (q qinv : R)
    (u : Cl3) (a_next a_in' a_next' : Fin 3) : R :=
  ∑ c' : Fin 3, jRMat q qinv u.2.2 a_next c' a_next' * epsRing qinv a_in' u.2.1 c'

private theorem sum_bc_ketEdge {R : Type*} [CommRing R] (q qinv : R)
    (a a_next a' a_next' : Fin 3) :
    (∑ bc : Fin 3 × Fin 3,
      epsCl qinv (a, bc.1, bc.2) * ketEdge q qinv (a, bc.1, bc.2) a_next a' a_next') =
    ringPairTransfer q qinv (a, a') (a_next, a_next') := by
  simp only [epsCl, ketEdge, ringPairTransfer, clSpectatorW, Fintype.sum_prod_type,
    Fin.sum_univ_three]
  ring

private theorem closedTriangle_ket_expand {R : Type*} [CommRing R] (q qinv : R)
    (u₁ u₂ u₃ : Cl3) :
    closedTriangle_nine q qinv (eps9Cl qinv) u₁ u₂ u₃ =
      ∑ p : Fin 3 × Fin 3 × Fin 3,
        ketEdge q qinv u₁ u₂.1 p.1 p.2.1 *
        ketEdge q qinv u₂ u₃.1 p.2.1 p.2.2 *
        ketEdge q qinv u₃ u₁.1 p.2.2 p.1 := by
  simp only [closedTriangle_nine, eps9Cl, epsCl, jR_eq_sum_jRMat, Fintype.sum_prod_type]
  have hs3 : ∀ c₁' a₂' c₂' a₃' : Fin 3,
      (∑ c₃' : Fin 3, ∑ a₁' : Fin 3, jRMat q qinv u₃.2.2 u₁.1 c₃' a₁' *
        (epsRing qinv a₁' u₁.2.1 c₁' * epsRing qinv a₂' u₂.2.1 c₂' *
          epsRing qinv a₃' u₃.2.1 c₃')) =
      ∑ a₁' : Fin 3, epsRing qinv a₁' u₁.2.1 c₁' * epsRing qinv a₂' u₂.2.1 c₂' *
        ketEdge q qinv u₃ u₁.1 a₃' a₁' := by
    intro _ _ _ _
    simp only [ketEdge, Fin.sum_univ_three]; ring
  simp_rw [hs3]
  have hs2 : ∀ c₁' a₂' : Fin 3,
      (∑ c₂' : Fin 3, ∑ a₃' : Fin 3, jRMat q qinv u₂.2.2 u₃.1 c₂' a₃' *
        ∑ a₁' : Fin 3, epsRing qinv a₁' u₁.2.1 c₁' * epsRing qinv a₂' u₂.2.1 c₂' *
          ketEdge q qinv u₃ u₁.1 a₃' a₁') =
      ∑ a₃' : Fin 3, ∑ a₁' : Fin 3, epsRing qinv a₁' u₁.2.1 c₁' *
        ketEdge q qinv u₂ u₃.1 a₂' a₃' * ketEdge q qinv u₃ u₁.1 a₃' a₁' := by
    intro _ _
    simp only [ketEdge, Fin.sum_univ_three]; ring
  simp_rw [hs2]
  -- Unfold `ketEdge` ONLY on `u₁` (`5` Fin 3 variables = 243 atomic terms)
  conv_rhs =>
    arg 2; ext a₁'; arg 2; ext a₂'; arg 2; ext a₃'
    rw [show ketEdge q qinv u₁ u₂.1 a₁' a₂' =
      ∑ c₁' : Fin 3, jRMat q qinv u₁.2.2 u₂.1 c₁' a₂' * epsRing qinv a₁' u₁.2.1 c₁' from rfl]
  simp only [Fin.sum_univ_three]; ring

private theorem closedRing_ket_expand {R : Type*} [CommRing R] (q qinv : R)
    (u₁ u₂ u₃ u₄ : Cl3) :
    closedRing_twelve q qinv (eps12Cl qinv) u₁ u₂ u₃ u₄ =
      ∑ p : Fin 3 × Fin 3 × Fin 3 × Fin 3,
        ketEdge q qinv u₁ u₂.1 p.1 p.2.1 *
        ketEdge q qinv u₂ u₃.1 p.2.1 p.2.2.1 *
        ketEdge q qinv u₃ u₄.1 p.2.2.1 p.2.2.2 *
        ketEdge q qinv u₄ u₁.1 p.2.2.2 p.1 := by
  simp only [closedRing_twelve, eps12Cl, epsCl, jR_eq_sum_jRMat, Fintype.sum_prod_type]
  have hs4 : ∀ c₁' a₂' c₂' a₃' c₃' a₄' : Fin 3,
      (∑ c₄' : Fin 3, ∑ a₁' : Fin 3, jRMat q qinv u₄.2.2 u₁.1 c₄' a₁' *
        (epsRing qinv a₁' u₁.2.1 c₁' * epsRing qinv a₂' u₂.2.1 c₂' *
          epsRing qinv a₃' u₃.2.1 c₃' * epsRing qinv a₄' u₄.2.1 c₄')) =
      ∑ a₁' : Fin 3, epsRing qinv a₁' u₁.2.1 c₁' * epsRing qinv a₂' u₂.2.1 c₂' *
        epsRing qinv a₃' u₃.2.1 c₃' * ketEdge q qinv u₄ u₁.1 a₄' a₁' := by
    intro _ _ _ _ _ _
    simp only [ketEdge, Fin.sum_univ_three]; ring
  simp_rw [hs4]
  have hs3 : ∀ c₁' a₂' c₂' a₃' : Fin 3,
      (∑ c₃' : Fin 3, ∑ a₄' : Fin 3, jRMat q qinv u₃.2.2 u₄.1 c₃' a₄' *
        ∑ a₁' : Fin 3, epsRing qinv a₁' u₁.2.1 c₁' * epsRing qinv a₂' u₂.2.1 c₂' *
          epsRing qinv a₃' u₃.2.1 c₃' * ketEdge q qinv u₄ u₁.1 a₄' a₁') =
      ∑ a₄' : Fin 3, ∑ a₁' : Fin 3, epsRing qinv a₁' u₁.2.1 c₁' * epsRing qinv a₂' u₂.2.1 c₂' *
        (ketEdge q qinv u₃ u₄.1 a₃' a₄' * ketEdge q qinv u₄ u₁.1 a₄' a₁') := by
    intro _ _ _ _
    simp only [ketEdge, Fin.sum_univ_three]; ring
  simp_rw [hs3]
  have hs2 : ∀ c₁' a₂' : Fin 3,
      (∑ c₂' : Fin 3, ∑ a₃' : Fin 3, jRMat q qinv u₂.2.2 u₃.1 c₂' a₃' *
        ∑ a₄' : Fin 3, ∑ a₁' : Fin 3, epsRing qinv a₁' u₁.2.1 c₁' * epsRing qinv a₂' u₂.2.1 c₂' *
          (ketEdge q qinv u₃ u₄.1 a₃' a₄' * ketEdge q qinv u₄ u₁.1 a₄' a₁')) =
      ∑ a₃' : Fin 3, ∑ a₄' : Fin 3, ∑ a₁' : Fin 3, epsRing qinv a₁' u₁.2.1 c₁' *
        (ketEdge q qinv u₂ u₃.1 a₂' a₃' * ketEdge q qinv u₃ u₄.1 a₃' a₄' *
          ketEdge q qinv u₄ u₁.1 a₄' a₁') := by
    intro _ _
    simp only [ketEdge, Fin.sum_univ_three]; ring
  simp_rw [hs2]
  -- Pack `(a₃', a₄')` so `u₁` step only has 4 Fin 3 indices (`c₁', a₂', a₁', a₃'`) if needed, or 5 (`243` terms):
  let K234 : Fin 3 → Fin 3 → R := fun a₁' a₂' =>
    ∑ a₃' : Fin 3, ∑ a₄' : Fin 3,
      ketEdge q qinv u₂ u₃.1 a₂' a₃' * ketEdge q qinv u₃ u₄.1 a₃' a₄' *
        ketEdge q qinv u₄ u₁.1 a₄' a₁'
  have hwrapL : ∀ c₁' a₂' : Fin 3,
      (∑ a₃' : Fin 3, ∑ a₄' : Fin 3, ∑ a₁' : Fin 3, epsRing qinv a₁' u₁.2.1 c₁' *
        (ketEdge q qinv u₂ u₃.1 a₂' a₃' * ketEdge q qinv u₃ u₄.1 a₃' a₄' *
          ketEdge q qinv u₄ u₁.1 a₄' a₁')) =
      ∑ a₁' : Fin 3, epsRing qinv a₁' u₁.2.1 c₁' * K234 a₁' a₂' := by
    intro _ _
    dsimp only [K234]
    simp only [Fin.sum_univ_three]; ring
  have hwrapR : ∀ a₁' a₂' : Fin 3,
      (∑ a₃' : Fin 3, ∑ a₄' : Fin 3,
        ketEdge q qinv u₁ u₂.1 a₁' a₂' * ketEdge q qinv u₂ u₃.1 a₂' a₃' *
          ketEdge q qinv u₃ u₄.1 a₃' a₄' * ketEdge q qinv u₄ u₁.1 a₄' a₁') =
      ketEdge q qinv u₁ u₂.1 a₁' a₂' * K234 a₁' a₂' := by
    intro _ _
    dsimp only [K234]
    simp only [Fin.sum_univ_three]; ring
  simp_rw [hwrapL, hwrapR]
  conv_rhs =>
    arg 2; ext a₁'; arg 2; ext a₂'
    rw [show ketEdge q qinv u₁ u₂.1 a₁' a₂' =
      ∑ c₁' : Fin 3, jRMat q qinv u₁.2.2 u₂.1 c₁' a₂' * epsRing qinv a₁' u₁.2.1 c₁' from rfl]
  simp only [Fin.sum_univ_three]; ring

private theorem mul_two_sums {α β R : Type*} [Fintype α] [Fintype β] [CommRing R]
    (f : α → R) (g : β → R) :
    (∑ a : α, f a) * (∑ b : β, g b) = ∑ a : α, ∑ b : β, f a * g b := by
  rw [Finset.sum_mul]
  simp_rw [Finset.mul_sum]

private theorem factor_prod_three {β γ R : Type*} [Fintype β] [Fintype γ] [CommRing R]
    (f₁ f₂ f₃ : β → R) (g₁ g₂ g₃ : β → γ → R) :
    (∑ x₁ : β, ∑ x₂ : β, ∑ x₃ : β,
      (f₁ x₁ * f₂ x₂ * f₃ x₃) * ∑ p : γ, g₁ x₁ p * g₂ x₂ p * g₃ x₃ p) =
    ∑ p : γ,
      (∑ x₁ : β, f₁ x₁ * g₁ x₁ p) *
      (∑ x₂ : β, f₂ x₂ * g₂ x₂ p) *
      (∑ x₃ : β, f₃ x₃ * g₃ x₃ p) := by
  have hp : ∀ p : γ,
      (∑ x₁ : β, f₁ x₁ * g₁ x₁ p) * (∑ x₂ : β, f₂ x₂ * g₂ x₂ p) * (∑ x₃ : β, f₃ x₃ * g₃ x₃ p) =
      ∑ x₁ : β, ∑ x₂ : β, ∑ x₃ : β,
        (f₁ x₁ * f₂ x₂ * f₃ x₃) * (g₁ x₁ p * g₂ x₂ p * g₃ x₃ p) := by
    intro p
    rw [mul_two_sums, Finset.sum_mul]
    refine Finset.sum_congr rfl fun x₁ _ => ?_
    rw [Finset.sum_mul]
    refine Finset.sum_congr rfl fun x₂ _ => ?_
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun x₃ _ => by ring
  simp_rw [hp, Finset.mul_sum]
  calc _ = ∑ x₁ : β, ∑ x₂ : β, ∑ p : γ, ∑ x₃ : β, _ :=
          Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => Finset.sum_comm
    _ = ∑ x₁ : β, ∑ p : γ, ∑ x₂ : β, ∑ x₃ : β, _ :=
          Finset.sum_congr rfl fun _ _ => Finset.sum_comm
    _ = _ := Finset.sum_comm

private theorem factor_prod_four {β γ R : Type*} [Fintype β] [Fintype γ] [CommRing R]
    (f₁ f₂ f₃ f₄ : β → R) (g₁ g₂ g₃ g₄ : β → γ → R) :
    (∑ x₁ : β, ∑ x₂ : β, ∑ x₃ : β, ∑ x₄ : β,
      (f₁ x₁ * f₂ x₂ * f₃ x₃ * f₄ x₄) *
        ∑ p : γ, g₁ x₁ p * g₂ x₂ p * g₃ x₃ p * g₄ x₄ p) =
    ∑ p : γ,
      (∑ x₁ : β, f₁ x₁ * g₁ x₁ p) *
      (∑ x₂ : β, f₂ x₂ * g₂ x₂ p) *
      (∑ x₃ : β, f₃ x₃ * g₃ x₃ p) *
      (∑ x₄ : β, f₄ x₄ * g₄ x₄ p) := by
  have hp : ∀ p : γ,
      (∑ x₁ : β, f₁ x₁ * g₁ x₁ p) * (∑ x₂ : β, f₂ x₂ * g₂ x₂ p) *
        (∑ x₃ : β, f₃ x₃ * g₃ x₃ p) * (∑ x₄ : β, f₄ x₄ * g₄ x₄ p) =
      ∑ x₁ : β, ∑ x₂ : β, ∑ x₃ : β, ∑ x₄ : β,
        (f₁ x₁ * f₂ x₂ * f₃ x₃ * f₄ x₄) * (g₁ x₁ p * g₂ x₂ p * g₃ x₃ p * g₄ x₄ p) := by
    intro p
    rw [mul_two_sums, Finset.sum_mul]
    have h23 : ∀ x₁ : β,
        (∑ x₂ : β, (f₁ x₁ * g₁ x₁ p) * (f₂ x₂ * g₂ x₂ p)) * (∑ x₃ : β, f₃ x₃ * g₃ x₃ p) =
        ∑ x₂ : β, ∑ x₃ : β, (f₁ x₁ * g₁ x₁ p) * (f₂ x₂ * g₂ x₂ p) * (f₃ x₃ * g₃ x₃ p) := by
      intro x₁
      rw [Finset.sum_mul]
      refine Finset.sum_congr rfl fun x₂ _ => Finset.mul_sum ..
    simp_rw [h23]
    rw [Finset.sum_mul]
    refine Finset.sum_congr rfl fun x₁ _ => ?_
    rw [Finset.sum_mul]
    refine Finset.sum_congr rfl fun x₂ _ => ?_
    rw [Finset.sum_mul]
    refine Finset.sum_congr rfl fun x₃ _ => ?_
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun x₄ _ => by ring
  simp_rw [hp, Finset.mul_sum]
  calc _ = ∑ x₁ : β, ∑ x₂ : β, ∑ x₃ : β, ∑ p : γ, ∑ x₄ : β, _ :=
          Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ =>
            Finset.sum_congr rfl fun _ _ => Finset.sum_comm
    _ = ∑ x₁ : β, ∑ x₂ : β, ∑ p : γ, ∑ x₃ : β, ∑ x₄ : β, _ :=
          Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => Finset.sum_comm
    _ = ∑ x₁ : β, ∑ p : γ, ∑ x₂ : β, ∑ x₃ : β, ∑ x₄ : β, _ :=
          Finset.sum_congr rfl fun _ _ => Finset.sum_comm
    _ = _ := Finset.sum_comm

private theorem closedTriangle_nine_eq_trace {R : Type*} [CommRing R] (q qinv : R) :
    (∑ u₁ : Cl3, ∑ u₂ : Cl3, ∑ u₃ : Cl3,
        eps9Cl qinv u₁ u₂ u₃ * closedTriangle_nine q qinv (eps9Cl qinv) u₁ u₂ u₃) =
      Matrix.trace (ringPairTransfer q qinv ^ 3) := by
  simp_rw [closedTriangle_ket_expand, eps9Cl]
  -- Split ONLY the three outer `Cl3` sums (`u₁, u₂, u₃`) without touching `∑ p`!
  conv_lhs =>
    rw [Fintype.sum_prod_type]
    arg 2; ext a₁; arg 2; ext bc₁
    rw [Fintype.sum_prod_type]
    arg 2; ext a₂; arg 2; ext bc₂
    rw [Fintype.sum_prod_type]
  have hcomm :
      (∑ a₁ : Fin 3, ∑ bc₁ : Fin 3 × Fin 3, ∑ a₂ : Fin 3, ∑ bc₂ : Fin 3 × Fin 3,
        ∑ a₃ : Fin 3, ∑ bc₃ : Fin 3 × Fin 3,
          (epsCl qinv (a₁, bc₁) * epsCl qinv (a₂, bc₂) * epsCl qinv (a₃, bc₃)) *
          ∑ p : Fin 3 × Fin 3 × Fin 3,
            ketEdge q qinv (a₁, bc₁) a₂ p.1 p.2.1 *
            ketEdge q qinv (a₂, bc₂) a₃ p.2.1 p.2.2 *
            ketEdge q qinv (a₃, bc₃) a₁ p.2.2 p.1) =
      ∑ a₁ : Fin 3, ∑ a₂ : Fin 3, ∑ a₃ : Fin 3,
        ∑ bc₁ : Fin 3 × Fin 3, ∑ bc₂ : Fin 3 × Fin 3, ∑ bc₃ : Fin 3 × Fin 3,
          (epsCl qinv (a₁, bc₁) * epsCl qinv (a₂, bc₂) * epsCl qinv (a₃, bc₃)) *
          ∑ p : Fin 3 × Fin 3 × Fin 3,
            ketEdge q qinv (a₁, bc₁) a₂ p.1 p.2.1 *
            ketEdge q qinv (a₂, bc₂) a₃ p.2.1 p.2.2 *
            ketEdge q qinv (a₃, bc₃) a₁ p.2.2 p.1 := by
    refine Finset.sum_congr rfl fun a₁ _ => ?_
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl fun a₂ _ => ?_
    calc _ = ∑ bc₁ : Fin 3 × Fin 3, ∑ a₃ : Fin 3, ∑ bc₂ : Fin 3 × Fin 3,
            ∑ bc₃ : Fin 3 × Fin 3, _ := Finset.sum_congr rfl fun _ _ => Finset.sum_comm
      _ = _ := Finset.sum_comm
  rw [hcomm]
  have hstep : ∀ a₁ a₂ a₃ : Fin 3,
      (∑ bc₁ : Fin 3 × Fin 3, ∑ bc₂ : Fin 3 × Fin 3, ∑ bc₃ : Fin 3 × Fin 3,
        (epsCl qinv (a₁, bc₁) * epsCl qinv (a₂, bc₂) * epsCl qinv (a₃, bc₃)) *
        ∑ p : Fin 3 × Fin 3 × Fin 3,
          ketEdge q qinv (a₁, bc₁) a₂ p.1 p.2.1 *
          ketEdge q qinv (a₂, bc₂) a₃ p.2.1 p.2.2 *
          ketEdge q qinv (a₃, bc₃) a₁ p.2.2 p.1) =
      ∑ p : Fin 3 × Fin 3 × Fin 3,
        ringPairTransfer q qinv (a₁, p.1) (a₂, p.2.1) *
        ringPairTransfer q qinv (a₂, p.2.1) (a₃, p.2.2) *
        ringPairTransfer q qinv (a₃, p.2.2) (a₁, p.1) := by
    intro a₁ a₂ a₃
    rw [factor_prod_three]
    refine Finset.sum_congr rfl fun p _ => ?_
    rw [sum_bc_ketEdge, sum_bc_ketEdge, sum_bc_ketEdge]
  simp_rw [hstep]
  simp only [Matrix.trace, Matrix.diag, pow_succ', pow_zero, Matrix.mul_one, Matrix.mul_apply,
    Fintype.sum_prod_type]
  calc (∑ a₁ : Fin 3, ∑ a₂ : Fin 3, ∑ a₃ : Fin 3, ∑ a₁' : Fin 3, ∑ a₂' : Fin 3, ∑ a₃' : Fin 3,
          ringPairTransfer q qinv (a₁, a₁') (a₂, a₂') *
          ringPairTransfer q qinv (a₂, a₂') (a₃, a₃') *
          ringPairTransfer q qinv (a₃, a₃') (a₁, a₁'))
      = ∑ a₁ : Fin 3, ∑ a₁' : Fin 3, ∑ a₂ : Fin 3, ∑ a₂' : Fin 3, ∑ a₃ : Fin 3, ∑ a₃' : Fin 3,
          ringPairTransfer q qinv (a₁, a₁') (a₂, a₂') *
          (ringPairTransfer q qinv (a₂, a₂') (a₃, a₃') *
           ringPairTransfer q qinv (a₃, a₃') (a₁, a₁')) := by
          refine Finset.sum_congr rfl fun a₁ _ => ?_
          calc _ = ∑ a₂ : Fin 3, ∑ a₁' : Fin 3, ∑ a₃ : Fin 3, ∑ a₂' : Fin 3, ∑ a₃' : Fin 3, _ :=
                  Finset.sum_congr rfl fun _ _ => Finset.sum_comm
            _ = ∑ a₁' : Fin 3, ∑ a₂ : Fin 3, ∑ a₃ : Fin 3, ∑ a₂' : Fin 3, ∑ a₃' : Fin 3, _ :=
                  Finset.sum_comm
            _ = _ := by
                  refine Finset.sum_congr rfl fun a₁' _ => Finset.sum_congr rfl fun a₂ _ => ?_
                  rw [Finset.sum_comm]
                  refine Finset.sum_congr rfl fun a₂' _ => Finset.sum_congr rfl fun a₃ _ =>
                    Finset.sum_congr rfl fun a₃' _ => ?_
                  ring
    _ = _ := by
          refine Finset.sum_congr rfl fun a₁ _ => Finset.sum_congr rfl fun a₁' _ => ?_
          simp_rw [← Finset.mul_sum]

private theorem closedRing_twelve_eq_trace {R : Type*} [CommRing R] (q qinv : R) :
    (∑ u₁ : Cl3, ∑ u₂ : Cl3, ∑ u₃ : Cl3, ∑ u₄ : Cl3,
        eps12Cl qinv u₁ u₂ u₃ u₄ * closedRing_twelve q qinv (eps12Cl qinv) u₁ u₂ u₃ u₄) =
      Matrix.trace (ringPairTransfer q qinv ^ 4) := by
  simp_rw [closedRing_ket_expand, eps12Cl]
  conv_lhs =>
    rw [Fintype.sum_prod_type]
    arg 2; ext a₁; arg 2; ext bc₁
    rw [Fintype.sum_prod_type]
    arg 2; ext a₂; arg 2; ext bc₂
    rw [Fintype.sum_prod_type]
    arg 2; ext a₃; arg 2; ext bc₃
    rw [Fintype.sum_prod_type]
  have hcomm :
      (∑ a₁ : Fin 3, ∑ bc₁ : Fin 3 × Fin 3, ∑ a₂ : Fin 3, ∑ bc₂ : Fin 3 × Fin 3,
        ∑ a₃ : Fin 3, ∑ bc₃ : Fin 3 × Fin 3, ∑ a₄ : Fin 3, ∑ bc₄ : Fin 3 × Fin 3,
          (epsCl qinv (a₁, bc₁) * epsCl qinv (a₂, bc₂) *
            epsCl qinv (a₃, bc₃) * epsCl qinv (a₄, bc₄)) *
          ∑ p : Fin 3 × Fin 3 × Fin 3 × Fin 3,
            ketEdge q qinv (a₁, bc₁) a₂ p.1 p.2.1 *
            ketEdge q qinv (a₂, bc₂) a₃ p.2.1 p.2.2.1 *
            ketEdge q qinv (a₃, bc₃) a₄ p.2.2.1 p.2.2.2 *
            ketEdge q qinv (a₄, bc₄) a₁ p.2.2.2 p.1) =
      ∑ a₁ : Fin 3, ∑ a₂ : Fin 3, ∑ a₃ : Fin 3, ∑ a₄ : Fin 3,
        ∑ bc₁ : Fin 3 × Fin 3, ∑ bc₂ : Fin 3 × Fin 3,
        ∑ bc₃ : Fin 3 × Fin 3, ∑ bc₄ : Fin 3 × Fin 3,
          (epsCl qinv (a₁, bc₁) * epsCl qinv (a₂, bc₂) *
            epsCl qinv (a₃, bc₃) * epsCl qinv (a₄, bc₄)) *
          ∑ p : Fin 3 × Fin 3 × Fin 3 × Fin 3,
            ketEdge q qinv (a₁, bc₁) a₂ p.1 p.2.1 *
            ketEdge q qinv (a₂, bc₂) a₃ p.2.1 p.2.2.1 *
            ketEdge q qinv (a₃, bc₃) a₄ p.2.2.1 p.2.2.2 *
            ketEdge q qinv (a₄, bc₄) a₁ p.2.2.2 p.1 := by
    refine Finset.sum_congr rfl fun a₁ _ => ?_
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl fun a₂ _ => ?_
    calc _ = ∑ bc₁ : Fin 3 × Fin 3, ∑ a₃ : Fin 3, ∑ bc₂ : Fin 3 × Fin 3,
            ∑ bc₃ : Fin 3 × Fin 3, ∑ a₄ : Fin 3, ∑ bc₄ : Fin 3 × Fin 3, _ :=
            Finset.sum_congr rfl fun _ _ => Finset.sum_comm
      _ = ∑ a₃ : Fin 3, ∑ bc₁ : Fin 3 × Fin 3, ∑ bc₂ : Fin 3 × Fin 3,
            ∑ bc₃ : Fin 3 × Fin 3, ∑ a₄ : Fin 3, ∑ bc₄ : Fin 3 × Fin 3, _ := Finset.sum_comm
      _ = _ := by
            refine Finset.sum_congr rfl fun a₃ _ => ?_
            calc _ = ∑ bc₁ : Fin 3 × Fin 3, ∑ bc₂ : Fin 3 × Fin 3, ∑ a₄ : Fin 3,
                    ∑ bc₃ : Fin 3 × Fin 3, ∑ bc₄ : Fin 3 × Fin 3, _ :=
                    Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => Finset.sum_comm
              _ = ∑ bc₁ : Fin 3 × Fin 3, ∑ a₄ : Fin 3, ∑ bc₂ : Fin 3 × Fin 3,
                    ∑ bc₃ : Fin 3 × Fin 3, ∑ bc₄ : Fin 3 × Fin 3, _ :=
                    Finset.sum_congr rfl fun _ _ => Finset.sum_comm
              _ = _ := Finset.sum_comm
  rw [hcomm]
  have hstep : ∀ a₁ a₂ a₃ a₄ : Fin 3,
      (∑ bc₁ : Fin 3 × Fin 3, ∑ bc₂ : Fin 3 × Fin 3,
        ∑ bc₃ : Fin 3 × Fin 3, ∑ bc₄ : Fin 3 × Fin 3,
          (epsCl qinv (a₁, bc₁) * epsCl qinv (a₂, bc₂) *
            epsCl qinv (a₃, bc₃) * epsCl qinv (a₄, bc₄)) *
          ∑ p : Fin 3 × Fin 3 × Fin 3 × Fin 3,
            ketEdge q qinv (a₁, bc₁) a₂ p.1 p.2.1 *
            ketEdge q qinv (a₂, bc₂) a₃ p.2.1 p.2.2.1 *
            ketEdge q qinv (a₃, bc₃) a₄ p.2.2.1 p.2.2.2 *
            ketEdge q qinv (a₄, bc₄) a₁ p.2.2.2 p.1) =
      ∑ p : Fin 3 × Fin 3 × Fin 3 × Fin 3,
        ringPairTransfer q qinv (a₁, p.1) (a₂, p.2.1) *
        ringPairTransfer q qinv (a₂, p.2.1) (a₃, p.2.2.1) *
        ringPairTransfer q qinv (a₃, p.2.2.1) (a₄, p.2.2.2) *
        ringPairTransfer q qinv (a₄, p.2.2.2) (a₁, p.1) := by
    intro a₁ a₂ a₃ a₄
    rw [factor_prod_four]
    refine Finset.sum_congr rfl fun p _ => ?_
    rw [sum_bc_ketEdge, sum_bc_ketEdge, sum_bc_ketEdge, sum_bc_ketEdge]
  simp_rw [hstep]
  simp only [Matrix.trace, Matrix.diag, pow_succ', pow_zero, Matrix.mul_one, Matrix.mul_apply,
    Fintype.sum_prod_type]
  calc (∑ a₁ : Fin 3, ∑ a₂ : Fin 3, ∑ a₃ : Fin 3, ∑ a₄ : Fin 3,
          ∑ a₁' : Fin 3, ∑ a₂' : Fin 3, ∑ a₃' : Fin 3, ∑ a₄' : Fin 3,
            ringPairTransfer q qinv (a₁, a₁') (a₂, a₂') *
            ringPairTransfer q qinv (a₂, a₂') (a₃, a₃') *
            ringPairTransfer q qinv (a₃, a₃') (a₄, a₄') *
            ringPairTransfer q qinv (a₄, a₄') (a₁, a₁'))
      = ∑ a₁ : Fin 3, ∑ a₁' : Fin 3, ∑ a₂ : Fin 3, ∑ a₂' : Fin 3,
          ∑ a₃ : Fin 3, ∑ a₃' : Fin 3, ∑ a₄ : Fin 3, ∑ a₄' : Fin 3,
            ringPairTransfer q qinv (a₁, a₁') (a₂, a₂') *
            (ringPairTransfer q qinv (a₂, a₂') (a₃, a₃') *
             (ringPairTransfer q qinv (a₃, a₃') (a₄, a₄') *
              ringPairTransfer q qinv (a₄, a₄') (a₁, a₁'))) := by
          refine Finset.sum_congr rfl fun a₁ _ => ?_
          calc _ = ∑ a₂ : Fin 3, ∑ a₃ : Fin 3, ∑ a₁' : Fin 3, ∑ a₄ : Fin 3,
                  ∑ a₂' : Fin 3, ∑ a₃' : Fin 3, ∑ a₄' : Fin 3, _ :=
                  Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => Finset.sum_comm
            _ = ∑ a₂ : Fin 3, ∑ a₁' : Fin 3, ∑ a₃ : Fin 3, ∑ a₄ : Fin 3,
                  ∑ a₂' : Fin 3, ∑ a₃' : Fin 3, ∑ a₄' : Fin 3, _ :=
                  Finset.sum_congr rfl fun _ _ => Finset.sum_comm
            _ = ∑ a₁' : Fin 3, ∑ a₂ : Fin 3, ∑ a₃ : Fin 3, ∑ a₄ : Fin 3,
                  ∑ a₂' : Fin 3, ∑ a₃' : Fin 3, ∑ a₄' : Fin 3, _ := Finset.sum_comm
            _ = _ := by
                  refine Finset.sum_congr rfl fun a₁' _ => Finset.sum_congr rfl fun a₂ _ => ?_
                  calc _ = ∑ a₃ : Fin 3, ∑ a₂' : Fin 3, ∑ a₄ : Fin 3,
                          ∑ a₃' : Fin 3, ∑ a₄' : Fin 3, _ :=
                          Finset.sum_congr rfl fun _ _ => Finset.sum_comm
                    _ = ∑ a₂' : Fin 3, ∑ a₃ : Fin 3, ∑ a₄ : Fin 3,
                          ∑ a₃' : Fin 3, ∑ a₄' : Fin 3, _ := Finset.sum_comm
                    _ = _ := by
                          refine Finset.sum_congr rfl fun a₂' _ =>
                            Finset.sum_congr rfl fun a₃ _ => ?_
                          rw [Finset.sum_comm]
                          refine Finset.sum_congr rfl fun a₃' _ =>
                            Finset.sum_congr rfl fun a₄ _ =>
                              Finset.sum_congr rfl fun a₄' _ => ?_
                          ring
    _ = _ := by
          refine Finset.sum_congr rfl fun a₁ _ => Finset.sum_congr rfl fun a₁' _ => ?_
          simp_rw [← Finset.mul_sum]

/-- **Exact Closed `9q` Triangular Plaquette & Closed `12q` Tetrahedral Ring Overlaps (`[CommRing R]`):**
Over any `[CommRing R]` with `q * qinv = 1`:
1. `⟨ε_q^{⊗ 3} | Ř_{3,4} Ř_{6,7} Ř_{9,1} | ε_q^{⊗ 3}⟩ = (q + qinv)³ - 8 · qinv⁹`, and cleared of
   denominators:
   `[2]_q³ [3]_q³ · ⟨ε_q^{⊗ 3} | Ř_{3,4} Ř_{6,7} Ř_{9,1} | ε_q^{⊗ 3}⟩ = (q⁹ [2]_q³ - 8) · ‖ε_q‖⁶`;
2. `⟨ε_q^{⊗ 4} | Ř_{3,4} Ř_{6,7} Ř_{9,10} Ř_{12,1} | ε_q^{⊗ 4}⟩ = (q + qinv)⁴ + 8 · qinv¹²`, and
   cleared of denominators:
   `[2]_q⁴ [3]_q⁴ · ⟨ε_q^{⊗ 4} | Ř_{3,4} Ř_{6,7} Ř_{9,10} Ř_{12,1} | ε_q^{⊗ 4}⟩ = (q¹² [2]_q⁴ + 8) · ‖ε_q‖⁸`. -/
theorem closedPlaquette_nine_and_twelve_overlap_ring {R : Type*} [CommRing R]
    (q qinv : R) (hq : q * qinv = 1) :
    let q2 := q + qinv
    let q3 := q ^ 2 + 1 + qinv ^ 2
    ((∑ u₁ : Cl3, ∑ u₂ : Cl3, ∑ u₃ : Cl3,
        eps9Cl qinv u₁ u₂ u₃ * closedTriangle_nine q qinv (eps9Cl qinv) u₁ u₂ u₃) =
      q2 ^ 3 - 8 * qinv ^ 9) ∧
    (q2 ^ 3 * q3 ^ 3 *
        (∑ u₁ : Cl3, ∑ u₂ : Cl3, ∑ u₃ : Cl3,
          eps9Cl qinv u₁ u₂ u₃ * closedTriangle_nine q qinv (eps9Cl qinv) u₁ u₂ u₃) =
      (q ^ 9 * q2 ^ 3 - 8) * epsNormSqRing qinv ^ 3) ∧
    ((∑ u₁ : Cl3, ∑ u₂ : Cl3, ∑ u₃ : Cl3, ∑ u₄ : Cl3,
        eps12Cl qinv u₁ u₂ u₃ u₄ * closedRing_twelve q qinv (eps12Cl qinv) u₁ u₂ u₃ u₄) =
      q2 ^ 4 + 8 * qinv ^ 12) ∧
    (q2 ^ 4 * q3 ^ 4 *
        (∑ u₁ : Cl3, ∑ u₂ : Cl3, ∑ u₃ : Cl3, ∑ u₄ : Cl3,
          eps12Cl qinv u₁ u₂ u₃ u₄ * closedRing_twelve q qinv (eps12Cl qinv) u₁ u₂ u₃ u₄) =
      (q ^ 12 * q2 ^ 4 + 8) * epsNormSqRing qinv ^ 4) := by
  dsimp only
  have htr := clusterStepMat_rankOne_and_ringTraces q qinv hq
  have hn := (epsNormSqRing_closed_form q qinv hq).2.2.2.1
  have h9 : (∑ u₁ : Cl3, ∑ u₂ : Cl3, ∑ u₃ : Cl3,
        eps9Cl qinv u₁ u₂ u₃ * closedTriangle_nine q qinv (eps9Cl qinv) u₁ u₂ u₃) =
      (q + qinv) ^ 3 - 8 * qinv ^ 9 :=
    (closedTriangle_nine_eq_trace q qinv).trans htr.2.1
  have h12 : (∑ u₁ : Cl3, ∑ u₂ : Cl3, ∑ u₃ : Cl3, ∑ u₄ : Cl3,
        eps12Cl qinv u₁ u₂ u₃ u₄ * closedRing_twelve q qinv (eps12Cl qinv) u₁ u₂ u₃ u₄) =
      (q + qinv) ^ 4 + 8 * qinv ^ 12 :=
    (closedRing_twelve_eq_trace q qinv).trans htr.2.2
  have hq3 : q ^ 3 * qinv ^ 3 = 1 := by linear_combination (q ^ 2 * qinv ^ 2 + q * qinv + 1) * hq
  have hq9 : q ^ 9 * qinv ^ 9 = 1 := by
    linear_combination (q ^ 6 * qinv ^ 6 + q ^ 3 * qinv ^ 3 + 1) * hq3
  have hq12 : q ^ 12 * qinv ^ 12 = 1 := by
    linear_combination (q ^ 9 * qinv ^ 9 + q ^ 6 * qinv ^ 6 + q ^ 3 * qinv ^ 3 + 1) * hq3
  refine ⟨h9, ?_, h12, ?_⟩
  · rw [h9]
    have hprod3 : (q + qinv) ^ 3 * (q ^ 2 + 1 + qinv ^ 2) ^ 3 =
        q ^ 9 * epsNormSqRing qinv ^ 3 := by
      calc (q + qinv) ^ 3 * (q ^ 2 + 1 + qinv ^ 2) ^ 3
          = ((q + qinv) * (q ^ 2 + 1 + qinv ^ 2)) ^ 3 := by ring
        _ = (q ^ 3 * epsNormSqRing qinv) ^ 3 := by rw [← hn]
        _ = q ^ 9 * epsNormSqRing qinv ^ 3 := by ring
    calc (q + qinv) ^ 3 * (q ^ 2 + 1 + qinv ^ 2) ^ 3 * ((q + qinv) ^ 3 - 8 * qinv ^ 9)
        = (q ^ 9 * epsNormSqRing qinv ^ 3) * ((q + qinv) ^ 3 - 8 * qinv ^ 9) := by rw [hprod3]
      _ = (q ^ 9 * (q + qinv) ^ 3 - 8 * (q ^ 9 * qinv ^ 9)) * epsNormSqRing qinv ^ 3 := by ring
      _ = (q ^ 9 * (q + qinv) ^ 3 - 8) * epsNormSqRing qinv ^ 3 := by rw [hq9]; ring
  · rw [h12]
    have hprod4 : (q + qinv) ^ 4 * (q ^ 2 + 1 + qinv ^ 2) ^ 4 =
        q ^ 12 * epsNormSqRing qinv ^ 4 := by
      calc (q + qinv) ^ 4 * (q ^ 2 + 1 + qinv ^ 2) ^ 4
          = ((q + qinv) * (q ^ 2 + 1 + qinv ^ 2)) ^ 4 := by ring
        _ = (q ^ 3 * epsNormSqRing qinv) ^ 4 := by rw [← hn]
        _ = q ^ 12 * epsNormSqRing qinv ^ 4 := by ring
    calc (q + qinv) ^ 4 * (q ^ 2 + 1 + qinv ^ 2) ^ 4 * ((q + qinv) ^ 4 + 8 * qinv ^ 12)
        = (q ^ 12 * epsNormSqRing qinv ^ 4) * ((q + qinv) ^ 4 + 8 * qinv ^ 12) := by rw [hprod4]
      _ = (q ^ 12 * (q + qinv) ^ 4 + 8 * (q ^ 12 * qinv ^ 12)) * epsNormSqRing qinv ^ 4 := by ring
      _ = (q ^ 12 * (q + qinv) ^ 4 + 8) * epsNormSqRing qinv ^ 4 := by rw [hq12]; ring

/-- **Connected Colour-Octet Cumulant Ratios (`N_c² - 1 = 8`) over `[Field K]`:**
Subtracting the disconnected singlet tree background `(q³ / [3]_q)^k` from the normalized closed
`k`-cluster plaquette overlap isolates the pure `8_c` gluon-ring holonomy:
- `t₃^△(q) - (q³ / [3]_q)³ = -8 / ([2]_q³ [3]_q³)` (`k = 3`),
- `t₄^□(q) - (q³ / [3]_q)⁴ = +8 / ([2]_q⁴ [3]_q⁴)` (`k = 4`). -/
theorem closedPlaquette_connected_cumulants_field {K : Type*} [Field K]
    (q : K) (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hq3 : q ^ 2 + 1 + q⁻¹ ^ 2 ≠ 0) :
    let q2 := q + q⁻¹
    let q3 := q ^ 2 + 1 + q⁻¹ ^ 2
    ((q ^ 9 * q2 ^ 3 - 8) / (q2 ^ 3 * q3 ^ 3) - (q ^ 3 / q3) ^ 3 =
      -8 / (q2 ^ 3 * q3 ^ 3)) ∧
    ((q ^ 12 * q2 ^ 4 + 8) / (q2 ^ 4 * q3 ^ 4) - (q ^ 3 / q3) ^ 4 =
      8 / (q2 ^ 4 * q3 ^ 4)) := by
  have _ := hq
  -- Prove over general `q2 ≠ 0, q3 ≠ 0` so `field_simp` never expands `q + q⁻¹` or `q² + 1 + q⁻²`!
  have hgen : ∀ (a b : K), a ≠ 0 → b ≠ 0 →
      ((q ^ 9 * a ^ 3 - 8) / (a ^ 3 * b ^ 3) - (q ^ 3 / b) ^ 3 = -8 / (a ^ 3 * b ^ 3)) ∧
      ((q ^ 12 * a ^ 4 + 8) / (a ^ 4 * b ^ 4) - (q ^ 3 / b) ^ 4 = 8 / (a ^ 4 * b ^ 4)) := by
    intro a b ha hb
    refine ⟨by field_simp [ha, hb]; ring, by field_simp [ha, hb]; ring⟩
  exact hgen (q + q⁻¹) (q ^ 2 + 1 + q⁻¹ ^ 2) hq2 hq3

end MultiClusterColourReconnection

/-! ## §4. Deuteron Preservation (`A = 2`) & Higher-Plaquette Binding Enhancement (`§7c`) -/

section SimplexBindingHierarchy

/-- Simplex-resolved nuclear cluster binding functional on `K_A`:
`B(A) = C(A, 2) · b₂ + C(A, 3) · b₃ + c₄(A) · b₄`. -/
def kASimplexBinding {R : Type*} [CommRing R] (A : ℕ) (b₂ b₃ b₄ : R) : R :=
  ((kAEdges A).card : R) * b₂ + ((kATriangles A).card : R) * b₃ + ((kAFourCycles A).card : R) * b₄

/-- **Exact Deuteron Invariance & Simplex Decomposition across `A = 2, 3, 4` over `[CommRing R]`:**
1. At `A = 2` (`²H`), `kASimplexBinding 2 b₂ b₃ b₄ = b₂` identically for **all** `b₃, b₄ : R`;
2. At `A = 3` (`³H / ³He`), `kASimplexBinding 3 b₂ b₃ b₄ = 3 b₂ + b₃` (independent of `b₄`);
3. At `A = 4` (`⁴He`), `kASimplexBinding 4 b₂ b₃ b₄ = 6 b₂ + 4 b₃ + 3 b₄`. -/
theorem kASimplexBinding_deuteron_invariance_and_light_nuclei {R : Type*} [CommRing R]
    (b₂ b₃ b₄ : R) :
    kASimplexBinding 2 b₂ b₃ b₄ = b₂ ∧
    kASimplexBinding 3 b₂ b₃ b₄ = 3 * b₂ + b₃ ∧
    kASimplexBinding 4 b₂ b₃ b₄ = 6 * b₂ + 4 * b₃ + 3 * b₄ := by
  have hc2e : (kAEdges 2).card = 1 := by decide
  have hc2t : (kATriangles 2).card = 0 := by decide
  have hc2q : (kAFourCycles 2).card = 0 := by decide
  have hc3e : (kAEdges 3).card = 3 := by decide
  have hc3t : (kATriangles 3).card = 1 := by decide
  have hc3q : (kAFourCycles 3).card = 0 := by decide
  have hc4e : (kAEdges 4).card = 6 := by decide
  have hc4t : (kATriangles 4).card = 4 := by decide
  have hc4q : (kAFourCycles 4).card = 3 := by decide
  unfold kASimplexBinding
  refine ⟨?_, ?_, ?_⟩
  · rw [hc2e, hc2t, hc2q]; push_cast; ring
  · rw [hc3e, hc3t, hc3q]; push_cast; ring
  · rw [hc4e, hc4t, hc4q]; push_cast; ring

/-- Second-order Bloch–Horowitz simplex binding `C(A,2) (v₂²/(2 Δ₈)) + C(A,3) (v₃²/(3 Δ₈)) + c₄(A) (v₄²/(4 Δ₈))`
with `k · Δ₈` adiabatic gap for simultaneous `k`-cluster `8_c^{⊗ k}` colour excitation. -/
def kABlochHorowitzBinding {K : Type*} [Field K] (A : ℕ) (Δ₈ v₂ v₃ v₄ : K) : K :=
  kASimplexBinding A (v₂ ^ 2 / (2 * Δ₈)) (v₃ ^ 2 / (3 * Δ₈)) (v₄ ^ 2 / (4 * Δ₈))

/-- **Strict Super-Pairwise Binding Enhancement from Cyclic `3`- and `4`-Body Plaquettes (`§7c`):**
Over any `[Field K] [LinearOrder K] [IsStrictOrderedRing K]`, if `0 < Δ₈`, `v₂ ≠ 0`, `v₃ ≠ 0`, `v₄ ≠ 0`:
1. `kABlochHorowitzBinding 2 Δ₈ v₂ v₃ v₄ = v₂² / (2 Δ₈) > 0` (deuteron untouched);
2. `3 * kABlochHorowitzBinding 2 Δ₈ v₂ v₃ v₄ < kABlochHorowitzBinding 3 Δ₈ v₂ v₃ v₄`;
3. `6 * kABlochHorowitzBinding 2 Δ₈ v₂ v₃ v₄ + 4 * (v₃ ^ 2 / (3 * Δ₈)) < kABlochHorowitzBinding 4 Δ₈ v₂ v₃ v₄`. -/
theorem kABlochHorowitz_super_pairwise_enhancement
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (Δ₈ v₂ v₃ v₄ : K) (hΔ : 0 < Δ₈) (hv₂ : v₂ ≠ 0) (hv₃ : v₃ ≠ 0) (hv₄ : v₄ ≠ 0) :
    0 < kABlochHorowitzBinding 2 Δ₈ v₂ v₃ v₄ ∧
    kABlochHorowitzBinding 2 Δ₈ v₂ v₃ v₄ = v₂ ^ 2 / (2 * Δ₈) ∧
    3 * kABlochHorowitzBinding 2 Δ₈ v₂ v₃ v₄ < kABlochHorowitzBinding 3 Δ₈ v₂ v₃ v₄ ∧
    6 * kABlochHorowitzBinding 2 Δ₈ v₂ v₃ v₄ + 4 * (v₃ ^ 2 / (3 * Δ₈)) <
      kABlochHorowitzBinding 4 Δ₈ v₂ v₃ v₄ := by
  have hd := kASimplexBinding_deuteron_invariance_and_light_nuclei
    (v₂ ^ 2 / (2 * Δ₈)) (v₃ ^ 2 / (3 * Δ₈)) (v₄ ^ 2 / (4 * Δ₈))
  unfold kABlochHorowitzBinding
  rw [hd.1, hd.2.1, hd.2.2]
  have hb2 : 0 < v₂ ^ 2 / (2 * Δ₈) := div_pos (sq_pos_of_ne_zero hv₂) (by positivity)
  have hb3 : 0 < v₃ ^ 2 / (3 * Δ₈) := div_pos (sq_pos_of_ne_zero hv₃) (by positivity)
  have hb4 : 0 < v₄ ^ 2 / (4 * Δ₈) := div_pos (sq_pos_of_ne_zero hv₄) (by positivity)
  exact ⟨hb2, rfl, by linarith, by linarith⟩

/-- Archimedean `ℝ` specialization of `kABlochHorowitz_super_pairwise_enhancement` (`§7c` `_real` bridge). -/
theorem kABlochHorowitz_super_pairwise_enhancement_real
    (Δ₈ v₂ v₃ v₄ : ℝ) (hΔ : 0 < Δ₈) (hv₂ : v₂ ≠ 0) (hv₃ : v₃ ≠ 0) (hv₄ : v₄ ≠ 0) :
    0 < kABlochHorowitzBinding 2 Δ₈ v₂ v₃ v₄ ∧
    kABlochHorowitzBinding 2 Δ₈ v₂ v₃ v₄ = v₂ ^ 2 / (2 * Δ₈) ∧
    3 * kABlochHorowitzBinding 2 Δ₈ v₂ v₃ v₄ < kABlochHorowitzBinding 3 Δ₈ v₂ v₃ v₄ ∧
    6 * kABlochHorowitzBinding 2 Δ₈ v₂ v₃ v₄ + 4 * (v₃ ^ 2 / (3 * Δ₈)) <
      kABlochHorowitzBinding 4 Δ₈ v₂ v₃ v₄ :=
  kABlochHorowitz_super_pairwise_enhancement (K := ℝ) Δ₈ v₂ v₃ v₄ hΔ hv₂ hv₃ hv₄

/-! ## §5. 3D Jacobi `(A - 1)` Kinetic Factorization & Hall–Post Super-Pairwise Bound (`§7c`) -/

/-- Relative 3D Jacobi total energy `(A - 1) · t_kin - C(A, 2) · u_pair` for `A` nucleons with
`A - 1` relative kinetic modes of energy `t_kin` and `C(A, 2)` Wigner-symmetric pairs of attraction `u_pair`. -/
def jacobiClusterEnergy {R : Type*} [CommRing R] (A : ℕ) (t_kin u_pair : R) : R :=
  ((A - 1 : ℕ) : R) * t_kin - ((kAEdges A).card : R) * u_pair

/-- **Exact `(A - 1)` Jacobi Mode Factorization & Hall–Post Super-Pairwise Identity (`[CommRing R]`):**
Over any `[CommRing R]`:
1. Twice `jacobiClusterEnergy A t_kin u_pair` factors out `(A - 1)` across `A = 2, 3, 4`:
   `2 · E_Jac(A) = (A - 1) · (2 t_kin - A · u_pair)`;
2. **Hall–Post decomposition:** writing `u_pair = t_kin + b₂` (`-E_Jac(2) = b₂`), the net binding
   `-jacobiClusterEnergy A t_kin (t_kin + b₂)` equals `b₂` (`A = 2`), `3 b₂ + t_kin` (`A = 3`), and
   `6 b₂ + 3 t_kin` (`A = 4`). -/
theorem jacobi_mode_factorization_and_hall_post_ring {R : Type*} [CommRing R]
    (t_kin u_pair b₂ : R) :
    (2 * jacobiClusterEnergy 2 t_kin u_pair = 1 * (2 * t_kin - 2 * u_pair) ∧
      2 * jacobiClusterEnergy 3 t_kin u_pair = 2 * (2 * t_kin - 3 * u_pair) ∧
      2 * jacobiClusterEnergy 4 t_kin u_pair = 3 * (2 * t_kin - 4 * u_pair)) ∧
    (-jacobiClusterEnergy 2 t_kin (t_kin + b₂) = b₂ ∧
      -jacobiClusterEnergy 3 t_kin (t_kin + b₂) = 3 * b₂ + t_kin ∧
      -jacobiClusterEnergy 4 t_kin (t_kin + b₂) = 6 * b₂ + 3 * t_kin) := by
  have hc2 : (kAEdges 2).card = 1 := by decide
  have hc3 : (kAEdges 3).card = 3 := by decide
  have hc4 : (kAEdges 4).card = 6 := by decide
  unfold jacobiClusterEnergy
  refine ⟨⟨?_, ?_, ?_⟩, ⟨?_, ?_, ?_⟩⟩
  · rw [hc2]; push_cast; ring
  · rw [hc3]; push_cast; ring
  · rw [hc4]; push_cast; ring
  · rw [hc2]; push_cast; ring
  · rw [hc3]; push_cast; ring
  · rw [hc4]; push_cast; ring

/-- **Strict Hall–Post & Variational Compression Super-Pairwise Inequality (`§7c`):**
Over any `[CommRing K] [LinearOrder K] [IsStrictOrderedRing K]`, if `0 < t₂` and `0 < b₂`, then
for any variational trial energy `E_var4 ≤ jacobiClusterEnergy 4 t₂ (t₂ + b₂)`:
`6 * b₂ + 3 * t₂ ≤ -E_var4 ∧ 6 * b₂ < -E_var4`. -/
theorem hall_post_variational_exceeds_six_deuterons
    {K : Type*} [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    (t₂ b₂ E_var4 : K) (ht : 0 < t₂) (hb : 0 < b₂)
    (hvar : E_var4 ≤ jacobiClusterEnergy 4 t₂ (t₂ + b₂)) :
    6 * b₂ + 3 * t₂ ≤ -E_var4 ∧ 6 * b₂ < -E_var4 := by
  have hhp := (jacobi_mode_factorization_and_hall_post_ring t₂ (t₂ + b₂) b₂).2.2.2
  have _ := hb
  constructor <;> linarith

/-- Archimedean `ℝ` specialization of `hall_post_variational_exceeds_six_deuterons` (`§7c` `_real` bridge). -/
theorem hall_post_variational_exceeds_six_deuterons_real
    (t₂ b₂ E_var4 : ℝ) (ht : 0 < t₂) (hb : 0 < b₂)
    (hvar : E_var4 ≤ jacobiClusterEnergy 4 t₂ (t₂ + b₂)) :
    6 * b₂ + 3 * t₂ ≤ -E_var4 ∧ 6 * b₂ < -E_var4 :=
  hall_post_variational_exceeds_six_deuterons (K := ℝ) t₂ b₂ E_var4 ht hb hvar

end SimplexBindingHierarchy

end QOU.Nuclear.TetrahedralFluxRingAndMajoranaCluster
