import Mathlib.Tactic
import Mathlib.Data.Nat.Choose.Basic
import QOU.MassTheory.H4GPMTModifiedDimensionCumulants

/-!
# First-Principles 3D Tetrahedral $\alpha$-Simplex Nuclear Coordination & GPMT Simplicial Energy

This module derives and formalizes the 3-dimensional tetrahedral ($\alpha$-simplex) nuclear
coordination hierarchy from first-principles representation theory and simplicial combinatorics,
with **zero empirical fitting** and **zero liquid-drop geometric assumptions**.

## Main Results

1. **Section 1 — Spin-Isospin Pauli Exclusion & the $K_4$ $\alpha$-Simplex Ceiling**:
   - Nucleons carry 4 internal spin-isospin states `SpinIsospinState := Fin 2 × Fin 2`
     ($\{p\uparrow, p\downarrow, n\uparrow, n\downarrow\}$, `card_spinIsospinState : Fintype.card SpinIsospinState = 4`).
   - By Pauli antisymmetrization on a common symmetric spatial $s$-wave braid locus, any mutually
     bonded local $s$-wave clique $S$ must admit an injective spin-isospin assignment
     `c : S → SpinIsospinState`, forcing `Fintype.card S ≤ 4` (`pauli_clique_card_le_four`)
     and excluding $K_5$ (`pauli_no_k5_clique`, `colored_clique_card_le_four`).
   - At the saturation ceiling $|S| = 4$ (the $^4\mathrm{He}$ $\alpha$-particle, Wigner $SU(4)$
     $[1^4]$ singlet), the unique maximal clique is the complete 3-simplex $K_4$ with face vector
     $(f_0, f_1, f_2, f_3) = (\binom{4}{1}, \binom{4}{2}, \binom{4}{3}, \binom{4}{4}) = (4, 6, 4, 1)$
     (`alpha_simplex_f_vector`).

2. **Section 2 — Stacked 3-Simplex Complex (3-Tree $\mathcal{K}_A$) $f$-Vector & Topology**:
   - Imposing local simplicial face-gluing saturation (inductively attaching each nucleon $A \ge 3 \mapsto A+1$
     along a shared $K_3$ triangular face) uniquely determines the stacked 3-simplex $f$-vector:
     $$f_0(A) = A,\quad f_1(A) = 3A - 6,\quad f_2(A) = 3A - 8,\quad f_3(A) = A - 3 \quad (A \ge 3).$$
   - Proves exact agreement with the single-simplex binomial counts $(\binom{A}{1}, \binom{A}{2}, \binom{A}{3}, \binom{A}{4})$
     for all $1 \le A \le 4$ (`fVector_eq_choose_of_le_four`), contractible simplicial Euler
     characteristic $\chi(\mathcal{K}_A) = f_0 - f_1 + f_2 - f_3 = 1$ for all $A \ge 1$
     (`eulerChar_stackedSimplex_eq_one`), boundary-interior triangle split
     $f_2^{\mathrm{bdry}}(A) = 2A - 4$, $f_2^{\mathrm{int}}(A) = A - 4$ with closed boundary
     2-sphere Euler characteristic $\chi(\partial \mathcal{K}_A) = 2$
     (`boundary_interior_triangle_split`, `boundary_sphere_eulerChar_eq_two`), and the exact
     edge deficit relative to the complete graph $K_A$:
     $$\binom{A}{2} - f_1(A) = \binom{A - 3}{2} \quad \forall A \ge 3$$
     (`complete_sub_simplex_edges_eq_choose`).

3. **Section 3 — Pauli Bipyramid Obstruction & the Hierarchical $\alpha$-Cluster Complex $\mathcal{C}_A$**:
   - **Pauli Bipyramid Obstruction (`pauli_bipyramid_forced_collision`)**: When two $K_4$
     tetrahedra $T_1 = \{v_1, v_2, v_3, v_4\}$ and $T_2 = \{v_1, v_2, v_3, v_5\}$ share a
     common $K_3$ triangle $\{v_1, v_2, v_3\}$, any spin-isospin coloring into a 4-element
     state space that is injective on both $T_1$ and $T_2$ forces the two apex nucleons to
     carry the **exact same** spin-isospin state (`c4 = c5`), requiring an orthogonal higher
     spatial orbital shell across every shared triangular face.
   - Formalizes the companion parameter-free **hierarchical $\alpha$-cluster complex** $\mathcal{C}_A$
     ($N_\alpha = \lfloor A/4 \rfloor$ disjoint closed-shell $K_4$ $\alpha$-simplices plus
     remainder $r = A \bmod 4$, linked by a 3-tree of inter-cluster bridges), proving
     `totalAlphaClusterEdges (4 * N_\alpha) = 9 * N_\alpha - 6` for all $N_\alpha \ge 4$
     (`totalAlphaClusterEdges_four_mul`), i.e. $\frac{9}{4} A - 6 = 2.25 A - 6$ edges.

4. **Section 4 — Exact GPMT Simplicial Energy Functional, Linear Extensivity & Saturation**:
   - Proves that the simplicial strong binding functional
     $B_{\mathrm{simp}}(\mathcal{K}_A) = f_1(A) b_2 + f_2(A) w_3 + f_3(A) w_4$ is identically
     affine-linear in $A$ for all $A \ge 3$ (`stackedSimplex_energy_affine_in_A`):
     $$B_{\mathrm{simp}}(\mathcal{K}_A) = (3 b_2 + 3 w_3 + w_4) A - (6 b_2 + 8 w_3 + 3 w_4),$$
     eliminating the $O(A^2)$ pair blowup while tripling the 2-body coordination of the 1D chain.
   - Connects directly to the `H_3(q)` / `H_4(q)` GPMT modified-dimension cumulants
     `mu3GPMT_H4 q > 0` and `mu4GPMT_H4 q < 0` (`QOU.MassTheory.H4GPMTModifiedDimensionCumulants`),
     proving that for all $q > 0$, both the single-$\alpha$ higher-body GPMT energy
     $4 \mu_3 + \mu_4 = \mathrm{sRow3GPMT\_H4}(q, 4)$ (`gpmt_alpha_higher_body_eq_sRow3_and_pos`)
     and the 3-tree asymptotic per-nucleon higher-body GPMT coefficient
     $3 \mu_3 + \mu_4$ (`gpmt_threeTree_higher_body_vol_pos`) are strictly positive, and that
     an isospin-symmetric strong core makes the mirror-nucleus binding split purely
     electromagnetic (`simplicial_mirror_split_pure_coulomb`).
-/

namespace QOU.Nuclear.AlphaSimplexCoordinationDerivation

open QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace (zD dMod111)
open QOU.MassTheory.GPMTThreeRowCumulantBridge
open QOU.MassTheory.H4GPMTModifiedDimensionCumulants

-- ============================================================================
-- § 1. Spin-Isospin Pauli Exclusion & the K₄ α-Simplex Ceiling
-- ============================================================================

/-- The 4-element nucleon spin-isospin state space $\Sigma_{\mathrm{SU(4)}} = \mathrm{Fin}\ 2 \times \mathrm{Fin}\ 2$
($\text{spin } \{\uparrow, \downarrow\} \times \text{isospin } \{p, n\}$). -/
abbrev SpinIsospinState : Type := Fin 2 × Fin 2

/-- The nucleon spin-isospin fiber has cardinality $2 \times 2 = 4$. -/
theorem card_spinIsospinState : Fintype.card SpinIsospinState = 4 := by
  decide

/-- **Pauli Local $s$-Wave Clique Bound**:
Any finite set $S$ of nucleons sharing a common symmetric spatial $s$-wave locus must admit
an injective spin-isospin assignment `c : S → SpinIsospinState`, and therefore has
cardinality at most $4$. -/
theorem pauli_clique_card_le_four {S : Type*} [Fintype S]
    (c : S → SpinIsospinState) (hc : Function.Injective c) :
    Fintype.card S ≤ 4 := by
  have hle : Fintype.card S ≤ Fintype.card SpinIsospinState :=
    Fintype.card_le_of_injective c hc
  simpa [card_spinIsospinState] using hle

/-- **Pauli $K_5$-Exclusion Theorem**:
No clique of $5$ or more nucleons can admit an injective spin-isospin coloring into
`SpinIsospinState`. -/
theorem pauli_no_k5_clique {S : Type*} [Fintype S] (hS : 5 ≤ Fintype.card S) :
    ¬ ∃ c : S → SpinIsospinState, Function.Injective c := by
  rintro ⟨c, hc⟩
  have hle := pauli_clique_card_le_four c hc
  omega

/-- Finset-level Pauli clique bound: for any vertex type `V`, any spin-isospin assignment
`col : V → SpinIsospinState`, and any finite clique `C : Finset V` on which `col` takes
pairwise distinct values, `C.card ≤ 4`. -/
theorem colored_clique_card_le_four {V : Type*} [DecidableEq V]
    (col : V → SpinIsospinState) (C : Finset V)
    (hC : ∀ x ∈ C, ∀ y ∈ C, x ≠ y → col x ≠ col y) :
    C.card ≤ 4 := by
  have hinj : Set.InjOn col C := by
    intro x hx y hy hxy
    by_contra hne
    exact hC x hx y hy hne hxy
  have hcard : C.card = (C.image col).card := (Finset.card_image_of_injOn hinj).symm
  have hsub : (C.image col).card ≤ Fintype.card SpinIsospinState :=
    Finset.card_le_univ (C.image col)
  rw [← hcard, card_spinIsospinState] at hsub
  exact hsub

/-- **Pauli Same-Isospin Clique Bound (`≤ 2`)**:
Because each isospin species ($p$ or $n$, `τ : Fin 2`) has only $2$ spin states (`Fin 2`),
any local $s$-wave clique `S` in which every nucleon has the same isospin `τ` has cardinality
at most $2$. Consequently, no $s$-wave $K_3$ triangle can be formed by $3$ identical nucleons
($ppp$ trineutron/triproton exclusion), and every $K_4$ tetrahedron must have the balanced
$(2p, 2n)$ composition of an $\alpha$-particle. -/
theorem pauli_same_isospin_card_le_two {S : Type*} [Fintype S]
    (c : S → SpinIsospinState) (hc : Function.Injective c)
    (τ : Fin 2) (hτ : ∀ x : S, (c x).2 = τ) :
    Fintype.card S ≤ 2 := by
  have hinj1 : Function.Injective (fun x : S => (c x).1) := by
    intro x y hxy
    apply hc
    apply Prod.ext
    · exact hxy
    · rw [hτ x, hτ y]
  have hle : Fintype.card S ≤ Fintype.card (Fin 2) :=
    Fintype.card_le_of_injective (fun x : S => (c x).1) hinj1
  simpa using hle

/-- **Pauli Mono-Isospin Triangle ($K_3$) Exclusion**:
No 3-nucleon $s$-wave triangle (`Fintype.card S = 3`) can consist of 3 nucleons of the same
isospin species ($ppp$ or $nnn$). -/
theorem pauli_no_mono_isospin_triangle {S : Type*} [Fintype S]
    (hcard : Fintype.card S = 3)
    (c : S → SpinIsospinState) (hc : Function.Injective c) (τ : Fin 2) :
    ¬ (∀ x : S, (c x).2 = τ) := by
  intro hτ
  have hle := pauli_same_isospin_card_le_two c hc τ hτ
  omega

/-- In any local $s$-wave clique `S` with injective spin-isospin coloring `c : S → SpinIsospinState`,
at most $2$ vertices of `S` can have isospin `τ : Fin 2`. -/
theorem pauli_filter_isospin_card_le_two {S : Type*} [Fintype S] [DecidableEq S]
    (c : S → SpinIsospinState) (hc : Function.Injective c) (τ : Fin 2) :
    (Finset.univ.filter (fun x : S => (c x).2 = τ)).card ≤ 2 := by
  let Sub := {x : S // (c x).2 = τ}
  have hsub : Fintype.card Sub ≤ 2 :=
    pauli_same_isospin_card_le_two (fun u : Sub => c u.1)
      (fun u v huv => Subtype.ext (hc huv)) τ (fun u => u.2)
  simpa [Sub, Fintype.card_subtype] using hsub

/-- **Balanced $(2p, 2n)$ Isospin Composition of Every $s$-Wave $K_4$ Tetrahedron**:
In any 4-nucleon $s$-wave clique `S` (`Fintype.card S = 4`) with injective spin-isospin
coloring `c : S → SpinIsospinState`, there are **exactly $2$ protons** (`(c x).2 = 0`)
and **exactly $2$ neutrons** (`(c x).2 = 1`).
Consequently, once all minority-species nucleons are paired into $(2p, 2n)$ core cells,
excess majority-species nucleons cannot form any additional $s$-wave $K_4$ tetrahedra. -/
theorem pauli_k4_balanced_isospin {S : Type*} [Fintype S] [DecidableEq S]
    (hcard : Fintype.card S = 4)
    (c : S → SpinIsospinState) (hc : Function.Injective c) :
    (Finset.univ.filter (fun x : S => (c x).2 = 0)).card = 2 ∧
    (Finset.univ.filter (fun x : S => (c x).2 = 1)).card = 2 := by
  have h0 : (Finset.univ.filter (fun x : S => (c x).2 = 0)).card ≤ 2 :=
    pauli_filter_isospin_card_le_two c hc 0
  have h1 : (Finset.univ.filter (fun x : S => (c x).2 = 1)).card ≤ 2 :=
    pauli_filter_isospin_card_le_two c hc 1
  have hcompl :
      Finset.univ.filter (fun x : S => ¬ (c x).2 = 0) =
        Finset.univ.filter (fun x : S => (c x).2 = 1) := by
    ext x
    simp only [Finset.mem_filter, Finset.mem_univ, true_and]
    have hfin : (c x).2 = 0 ∨ (c x).2 = 1 :=
      (by decide : ∀ t : Fin 2, t = 0 ∨ t = 1) (c x).2
    rcases hfin with h | h <;> simp [h]
  have hsum :
      (Finset.univ.filter (fun x : S => (c x).2 = 0)).card +
        (Finset.univ.filter (fun x : S => (c x).2 = 1)).card = 4 := by
    rw [← hcompl, Finset.filter_card_add_filter_neg_card_eq_card, Finset.card_univ, hcard]
  omega

/-- Exterior-power dimension vanishing gate: the dimension $\binom{4}{k}$ of the $k$-nucleon
totally antisymmetric spin-isospin space $\Lambda^k(\mathbb{C}^4)$ vanishes if and only if $k > 4$. -/
theorem su4_exterior_dim_zero_iff (k : ℕ) :
    Nat.choose 4 k = 0 ↔ 4 < k :=
  Nat.choose_eq_zero_iff

/-- At the $A = 4$ saturation ceiling ($^4\mathrm{He}$ $\alpha$-particle), the non-empty
simplex face counts $(\binom{4}{1}, \binom{4}{2}, \binom{4}{3}, \binom{4}{4})$ of the
regular 3-simplex $K_4$ are $(4, 6, 4, 1)$, with reduced Euler characteristic
$4 - 6 + 4 - 1 = 1$. -/
theorem alpha_simplex_f_vector :
    (Nat.choose 4 1, Nat.choose 4 2, Nat.choose 4 3, Nat.choose 4 4) = (4, 6, 4, 1) ∧
    ((Nat.choose 4 1 : ℤ) - Nat.choose 4 2 + Nat.choose 4 3 - Nat.choose 4 4 = 1) := by
  decide

-- ============================================================================
-- § 2. Stacked 3-Simplex Complex (3-Tree K_A) f-Vector, Euler Char & Boundary
-- ============================================================================

/-- Number of vertices $f_0(A) = A$ of the $A$-nucleon stacked 3-simplex complex $\mathcal{K}_A$. -/
def f0Simplex (A : ℕ) : ℕ := A

/-- Number of 2-body edges $f_1(A)$ of the $A$-nucleon stacked 3-simplex complex $\mathcal{K}_A$:
$0$ for $A \le 1$, $1$ for $A = 2$ ($^2\mathrm{H}$), and $3A - 6$ for all $A \ge 3$. -/
def f1Simplex (A : ℕ) : ℕ :=
  if A ≤ 1 then 0 else if A = 2 then 1 else 3 * A - 6

/-- Number of 3-body triangular faces $f_2(A)$ of the $A$-nucleon stacked 3-simplex complex $\mathcal{K}_A$:
$0$ for $A \le 2$, and $3A - 8$ for all $A \ge 3$. -/
def f2Simplex (A : ℕ) : ℕ :=
  if A ≤ 2 then 0 else 3 * A - 8

/-- Number of 4-body tetrahedral cells $f_3(A)$ of the $A$-nucleon stacked 3-simplex complex $\mathcal{K}_A$:
$0$ for $A \le 3$, and $A - 3$ for all $A \ge 4$. -/
def f3Simplex (A : ℕ) : ℕ :=
  if A ≤ 3 then 0 else A - 3

/-- Exact $f$-vector values at $A = 1, 2, 3, 4$. -/
theorem fVector_low_A :
    (f0Simplex 1, f1Simplex 1, f2Simplex 1, f3Simplex 1) = (1, 0, 0, 0) ∧
    (f0Simplex 2, f1Simplex 2, f2Simplex 2, f3Simplex 2) = (2, 1, 0, 0) ∧
    (f0Simplex 3, f1Simplex 3, f2Simplex 3, f3Simplex 3) = (3, 3, 1, 0) ∧
    (f0Simplex 4, f1Simplex 4, f2Simplex 4, f3Simplex 4) = (4, 6, 4, 1) := by
  decide

/-- For all $A \in \{1, 2, 3, 4\}$, the stacked 3-simplex $f$-vector coincides identically
with the complete-simplex binomial face counts $(\binom{A}{1}, \binom{A}{2}, \binom{A}{3}, \binom{A}{4})$. -/
theorem fVector_eq_choose_of_le_four (A : ℕ) (h1 : 1 ≤ A) (h4 : A ≤ 4) :
    (f0Simplex A, f1Simplex A, f2Simplex A, f3Simplex A) =
      (A.choose 1, A.choose 2, A.choose 3, A.choose 4) := by
  interval_cases A <;> decide

/-- Closed forms of `(f0Simplex A, f1Simplex A, f2Simplex A, f3Simplex A)` for all $A \ge 3$. -/
theorem fVector_of_three_le {A : ℕ} (hA : 3 ≤ A) :
    f0Simplex A = A ∧
    f1Simplex A = 3 * A - 6 ∧
    f2Simplex A = 3 * A - 8 ∧
    f3Simplex A = A - 3 := by
  unfold f0Simplex f1Simplex f2Simplex f3Simplex
  have h1 : ¬ A ≤ 1 := by omega
  have h2 : ¬ A = 2 := by omega
  have h2' : ¬ A ≤ 2 := by omega
  refine ⟨rfl, by simp [h1, h2], by simp [h2'], ?_⟩
  by_cases h3 : A ≤ 3
  · have hA3 : A = 3 := by omega
    subst hA3
    rfl
  · simp [h3]

/-- Inductive face-gluing step: for every $A \ge 3$, attaching nucleon $A + 1$ to an existing
$K_3$ triangular face increments $(f_0, f_1, f_2, f_3)$ by $(1, 3, 3, 1)$. -/
theorem fVector_succ_of_three_le {A : ℕ} (hA : 3 ≤ A) :
    f0Simplex (A + 1) = f0Simplex A + 1 ∧
    f1Simplex (A + 1) = f1Simplex A + 3 ∧
    f2Simplex (A + 1) = f2Simplex A + 3 ∧
    f3Simplex (A + 1) = f3Simplex A + 1 := by
  have hA1 : 3 ≤ A + 1 := by omega
  rcases fVector_of_three_le hA with ⟨h0, h1, h2, h3⟩
  rcases fVector_of_three_le hA1 with ⟨h0', h1', h2', h3'⟩
  rw [h0, h1, h2, h3, h0', h1', h2', h3']
  omega

/-- **Contractibility / Simplicial Euler Characteristic Theorem**:
For every $A \ge 1$, the stacked 3-simplex complex $\mathcal{K}_A$ has Euler characteristic
$$\chi(\mathcal{K}_A) = f_0(A) - f_1(A) + f_2(A) - f_3(A) = 1.$$ -/
theorem eulerChar_stackedSimplex_eq_one {A : ℕ} (hA : 1 ≤ A) :
    (f0Simplex A : ℤ) - (f1Simplex A : ℤ) + (f2Simplex A : ℤ) - (f3Simplex A : ℤ) = 1 := by
  by_cases hA3 : 3 ≤ A
  · rcases fVector_of_three_le hA3 with ⟨h0, h1, h2, h3⟩
    rw [h0, h1, h2, h3]
    omega
  · interval_cases A <;> decide

/-- Number of interior shared triangular faces $f_2^{\mathrm{int}}(A) = A - 4$ in a stacked
3-simplex complex for $A \ge 4$. -/
def f2Interior (A : ℕ) : ℕ := A - 4

/-- Number of exposed boundary triangular faces $f_2^{\mathrm{bdry}}(A) = 2A - 4$ on the surface
$\partial \mathcal{K}_A$ of a stacked 3-simplex complex for $A \ge 4$. -/
def f2Boundary (A : ℕ) : ℕ := 2 * A - 4

/-- **Boundary–Interior Triangle Split & Double-Handshake Identity**:
For every $A \ge 4$:
1. $f_2^{\mathrm{bdry}}(A) + f_2^{\mathrm{int}}(A) = f_2(A) = 3A - 8$,
2. $4 f_3(A) = f_2^{\mathrm{bdry}}(A) + 2 f_2^{\mathrm{int}}(A)$ (each of the $A - 3$ tetrahedra
   has $4$ faces; interior faces are shared by $2$ tetrahedra and boundary faces by $1$). -/
theorem boundary_interior_triangle_split {A : ℕ} (hA : 4 ≤ A) :
    f2Boundary A + f2Interior A = f2Simplex A ∧
    4 * f3Simplex A = f2Boundary A + 2 * f2Interior A := by
  have hA3 : 3 ≤ A := by omega
  rcases fVector_of_three_le hA3 with ⟨_, _, h2, h3⟩
  unfold f2Boundary f2Interior
  rw [h2, h3]
  omega

/-- **Boundary 2-Sphere Euler Characteristic**:
For every $A \ge 4$, the boundary surface $\partial \mathcal{K}_A$ has $V_\partial = A$ vertices,
$E_\partial = 3A - 6$ edges, and $F_\partial = 2A - 4$ triangular faces, satisfying the
2-sphere Euler characteristic $V_\partial - E_\partial + F_\partial = 2$. -/
theorem boundary_sphere_eulerChar_eq_two {A : ℕ} (hA : 4 ≤ A) :
    (f0Simplex A : ℤ) - (f1Simplex A : ℤ) + (f2Boundary A : ℤ) = 2 := by
  have hA3 : 3 ≤ A := by omega
  rcases fVector_of_three_le hA3 with ⟨h0, h1, _, _⟩
  unfold f2Boundary
  rw [h0, h1]
  omega

/-- **Exact Edge Decomposition of Complete Graph $K_A$ vs Stacked 3-Simplex $\mathcal{K}_A$**:
For every $A \ge 3$,
$$\binom{A}{2} = f_1(A) + \binom{A - 3}{2} = (3A - 6) + \binom{A - 3}{2}.$$ -/
theorem complete_edges_eq_simplex_add_choose {A : ℕ} (hA : 3 ≤ A) :
    A.choose 2 = f1Simplex A + (A - 3).choose 2 := by
  induction A, hA using Nat.le_induction with
  | base => decide
  | succ k hk ih =>
    have h1 : (k + 1).choose 2 = k + k.choose 2 := by
      simpa using Nat.choose_succ_succ k 1
    have h2 : (k + 1 - 3).choose 2 = (k - 3) + (k - 3).choose 2 := by
      have hsub : k + 1 - 3 = (k - 3) + 1 := by omega
      rw [hsub]
      simpa using Nat.choose_succ_succ (k - 3) 1
    have hf1 : f1Simplex (k + 1) = f1Simplex k + 3 :=
      (fVector_succ_of_three_le hk).2.1
    rw [h1, h2, hf1, ih]
    omega

/-- **Exact Edge Deficit of Stacked 3-Simplex vs Complete Graph $K_A$**:
For every $A \ge 3$, the edge deficit between the complete graph $K_A$ ($\binom{A}{2}$ edges)
and the stacked 3-simplex complex $\mathcal{K}_A$ ($3A - 6$ edges) is $\binom{A - 3}{2}$:
$$\binom{A}{2} - (3A - 6) = \binom{A - 3}{2}.$$ -/
theorem complete_sub_simplex_edges_eq_choose {A : ℕ} (hA : 3 ≤ A) :
    A.choose 2 - f1Simplex A = (A - 3).choose 2 := by
  have h := complete_edges_eq_simplex_add_choose hA
  omega

/-- For every $A \ge 5$, the stacked 3-simplex complex has strictly fewer edges than the
complete graph $K_A$: $f_1(A) = 3A - 6 < \binom{A}{2}$. -/
theorem f1Simplex_lt_choose_two_of_five_le {A : ℕ} (hA : 5 ≤ A) :
    f1Simplex A < A.choose 2 := by
  have hA3 : 3 ≤ A := by omega
  have hdef := complete_sub_simplex_edges_eq_choose hA3
  have hpos : 0 < (A - 3).choose 2 := by
    apply Nat.choose_pos
    omega
  omega

/-- 1D linear chain bond count $E_{\mathrm{chain}}(A) = A - 1$. -/
def chainEdges (A : ℕ) : ℕ := A - 1

/-- For all $A \ge 3$, $f_1(A) = 3 \cdot E_{\mathrm{chain}}(A) - 3$, so the stacked 3-simplex
complex has asymptotically **3 times** the 2-body coordination of the 1D linear chain. -/
theorem f1Simplex_eq_three_mul_chain_sub_three {A : ℕ} (hA : 3 ≤ A) :
    f1Simplex A = 3 * chainEdges A - 3 := by
  rcases fVector_of_three_le hA with ⟨_, h1, _, _⟩
  unfold chainEdges
  rw [h1]
  omega

-- ============================================================================
-- § 3. Pauli Bipyramid Obstruction & the Hierarchical α-Cluster Complex C_A
-- ============================================================================

/-- **Pauli Bipyramid Obstruction Theorem**:
In any 4-element spin-isospin state space $\alpha$ (`Fintype.card α = 4`), if two $K_4$
tetrahedra $T_1 = (c_1, c_2, c_3, c_4)$ and $T_2 = (c_1, c_2, c_3, c_5)$ share a common
$K_3$ triangle $(c_1, c_2, c_3)$ and each tetrahedron is properly 4-colored (pairwise distinct
spin-isospin states), then the two apex nucleons are forced to carry the **exact same**
spin-isospin state: `c4 = c5`.
Consequently, face-sharing two $s$-wave $K_4$ $\alpha$-clusters without Pauli collision
requires an orthogonal spatial orbital excitation across the shared face. -/
theorem pauli_bipyramid_forced_collision {α : Type*} [Fintype α] [DecidableEq α]
    (hcard : Fintype.card α = 4)
    {c1 c2 c3 c4 c5 : α}
    (h12 : c1 ≠ c2) (h13 : c1 ≠ c3) (h23 : c2 ≠ c3)
    (h14 : c1 ≠ c4) (h24 : c2 ≠ c4) (h34 : c3 ≠ c4)
    (h15 : c1 ≠ c5) (h25 : c2 ≠ c5) (h35 : c3 ≠ c5) :
    c4 = c5 := by
  by_contra h45
  let S : Finset α := {c1, c2, c3, c4, c5}
  have h1 : c1 ∉ ({c2, c3, c4, c5} : Finset α) := by
    simp [h12, h13, h14, h15]
  have h2 : c2 ∉ ({c3, c4, c5} : Finset α) := by
    simp [h23, h24, h25]
  have h3 : c3 ∉ ({c4, c5} : Finset α) := by
    simp [h34, h35]
  have h4 : c4 ∉ ({c5} : Finset α) := by
    simp [h45]
  have hScard : S.card = 5 := by
    dsimp [S]
    rw [Finset.card_insert_of_notMem h1,
      Finset.card_insert_of_notMem h2,
      Finset.card_insert_of_notMem h3,
      Finset.card_insert_of_notMem h4,
      Finset.card_singleton]
  have hle : S.card ≤ Fintype.card α := Finset.card_le_univ S
  omega

/-- Number of intra-cluster 2-body edges in the hierarchical $\alpha$-cluster decomposition
$A = 4 N_\alpha + r$ ($N_\alpha = A / 4$ disjoint $K_4$ $\alpha$-tetrahedra with $6$ edges each,
plus $\binom{r}{2}$ edges in the remainder $r = A \bmod 4$ cluster). -/
def intraAlphaEdges (A : ℕ) : ℕ :=
  6 * (A / 4) + (A % 4).choose 2

/-- Number of intra-cluster 3-body triangles in the hierarchical $\alpha$-cluster decomposition
$A = 4 N_\alpha + r$. -/
def intraAlphaTriangles (A : ℕ) : ℕ :=
  4 * (A / 4) + (A % 4).choose 3

/-- Number of intra-cluster 4-body tetrahedra $N_\alpha = A / 4$ in the hierarchical
$\alpha$-cluster decomposition. -/
def intraAlphaTetrahedra (A : ℕ) : ℕ :=
  A / 4

/-- Total number of cluster nodes $N_{\mathrm{cl}}(A) = \lceil A / 4 \rceil$ in the hierarchical
$\alpha$-cluster complex. -/
def clusterNodeCount (A : ℕ) : ℕ :=
  A / 4 + if A % 4 = 0 then 0 else 1

/-- Number of inter-cluster 3-tree bridge bonds $f_1(N_{\mathrm{cl}}(A))$ connecting the
$N_{\mathrm{cl}}(A)$ clusters in 3D. -/
def interClusterEdges (A : ℕ) : ℕ :=
  f1Simplex (clusterNodeCount A)

/-- Total 2-body edge count $E_{\mathrm{cluster}}(A) = E_{\mathrm{intra}}(A) + E_{\mathrm{inter}}(A)$
of the hierarchical $\alpha$-cluster simplicial complex $\mathcal{C}_A$. -/
def totalAlphaClusterEdges (A : ℕ) : ℕ :=
  intraAlphaEdges A + interClusterEdges A

/-- Exact values of `totalAlphaClusterEdges` on benchmark nuclei
$^2\mathrm{H}, ^3\mathrm{H}/^3\mathrm{He}, ^4\mathrm{He}, ^{12}\mathrm{C}, ^{16}\mathrm{O}, ^{56}\mathrm{Fe}$. -/
theorem totalAlphaClusterEdges_benchmarks :
    totalAlphaClusterEdges 2 = 1 ∧
    totalAlphaClusterEdges 3 = 3 ∧
    totalAlphaClusterEdges 4 = 6 ∧
    totalAlphaClusterEdges 12 = 21 ∧
    totalAlphaClusterEdges 16 = 30 ∧
    totalAlphaClusterEdges 56 = 120 := by
  decide

/-- **Exact Linear Scaling Law of the Hierarchical $\alpha$-Cluster Complex**:
For every $\alpha$-conjugate nucleus $A = 4 N_\alpha$ with $N_\alpha \ge 3$ ($A \ge 12$),
$$E_{\mathrm{cluster}}(4 N_\alpha) = 6 N_\alpha + (3 N_\alpha - 6) = 9 N_\alpha - 6,$$
giving a per-nucleon bond density of $\frac{9}{4} - \frac{6}{A} = 2.25 - \frac{6}{A}$
(strictly intermediate between the 1D chain $1 - 1/A$ and the nucleon 3-tree $3 - 6/A$). -/
theorem totalAlphaClusterEdges_four_mul {Nα : ℕ} (hN : 3 ≤ Nα) :
    totalAlphaClusterEdges (4 * Nα) = 9 * Nα - 6 := by
  unfold totalAlphaClusterEdges intraAlphaEdges interClusterEdges clusterNodeCount
  have hdiv : 4 * Nα / 4 = Nα := Nat.mul_div_right Nα (by decide)
  have hmod : 4 * Nα % 4 = 0 := Nat.mul_mod_right 4 Nα
  rw [hdiv, hmod]
  change 6 * Nα + 0 + f1Simplex (Nα + 0) = 9 * Nα - 6
  rw [add_zero, add_zero]
  rcases fVector_of_three_le hN with ⟨_, h1, _, _⟩
  rw [h1]
  omega

/-- **Pauli Excess-Nucleon Simplicial Attachment Regime A (Degree-1 Peripheral Bridge)**:
On a balanced core of size $A_{\mathrm{core}} = 2 \min(Z, N)$ with $D = |N - Z|$ excess
majority-species nucleons, each excess nucleon attaching by a degree-1 peripheral bond adds
$+1$ vertex, $+1$ edge, $0$ triangles, and $0$ tetrahedra (respecting `pauli_k4_balanced_isospin`). -/
def pauliBridgeF0 (Acore D : ℕ) : ℕ := f0Simplex Acore + D
def pauliBridgeF1 (Acore D : ℕ) : ℕ := f1Simplex Acore + D
def pauliBridgeF2 (Acore : ℕ) : ℕ := f2Simplex Acore
def pauliBridgeF3 (Acore : ℕ) : ℕ := f3Simplex Acore

/-- **Pauli Excess-Nucleon Simplicial Attachment Regime B (Maximal Degree-2 Mixed-Isospin Triangle)**:
By `pauli_same_isospin_card_le_two`, an $s$-wave $K_3$ triangle cannot be mono-isospin $(n, n, n)$,
but **can** be mixed-isospin $(p, n\uparrow, n\downarrow)$ (2 majority + 1 minority nucleon).
Attaching each of the $D = |N - Z|$ excess nucleons along a $(p, n)$ core edge forms one
mixed-isospin $K_3$ triangle and zero $K_4$ tetrahedra, adding $+1$ vertex, $+2$ edges,
$+1$ triangle, and $0$ tetrahedra per excess nucleon. -/
def pauliTriangleF0 (Acore D : ℕ) : ℕ := f0Simplex Acore + D
def pauliTriangleF1 (Acore D : ℕ) : ℕ := f1Simplex Acore + 2 * D
def pauliTriangleF2 (Acore D : ℕ) : ℕ := f2Simplex Acore + D
def pauliTriangleF3 (Acore : ℕ) : ℕ := f3Simplex Acore

/-- **Contractibility of Both Pauli Excess-Attachment Complexes**:
For every $A_{\mathrm{core}} \ge 1$ and every excess count $D \in \mathbb{N}$, both the
degree-1 peripheral-bridge complex and the maximal degree-2 mixed-isospin-triangle complex
preserve the contractible simplicial Euler characteristic $\chi = 1$. -/
theorem eulerChar_pauliExcess_both_eq_one {Acore : ℕ} (hA : 1 ≤ Acore) (D : ℕ) :
    ((pauliBridgeF0 Acore D : ℤ) - (pauliBridgeF1 Acore D : ℤ) +
      (pauliBridgeF2 Acore : ℤ) - (pauliBridgeF3 Acore : ℤ) = 1) ∧
    ((pauliTriangleF0 Acore D : ℤ) - (pauliTriangleF1 Acore D : ℤ) +
      (pauliTriangleF2 Acore D : ℤ) - (pauliTriangleF3 Acore : ℤ) = 1) := by
  have hbase := eulerChar_stackedSimplex_eq_one hA
  unfold pauliBridgeF0 pauliBridgeF1 pauliBridgeF2 pauliBridgeF3
    pauliTriangleF0 pauliTriangleF1 pauliTriangleF2 pauliTriangleF3
  push_cast
  omega

-- ============================================================================
-- § 4. Exact GPMT Simplicial Energy Functional, Linear Extensivity & Saturation
-- ============================================================================

section SimplicialEnergyFunctional

variable {R : Type*} [CommRing R]

/-- General simplicial strong binding energy functional on an $f$-vector $(f_1, f_2, f_3)$
with 2-body edge bond weight $b_2$, 3-body triangle weight $w_3$, and 4-body tetrahedron
weight $w_4$:
$$B_{\mathrm{simp}}(b_2, w_3, w_4, f_1, f_2, f_3) = f_1 b_2 + f_2 w_3 + f_3 w_4.$$ -/
def simplicialBinding (b₂ w₃ w₄ : R) (f₁ f₂ f₃ : ℕ) : R :=
  (f₁ : R) * b₂ + (f₂ : R) * w₃ + (f₃ : R) * w₄

/-- Bulk volume binding coefficient per nucleon on the stacked 3-simplex complex $\mathcal{K}_A$:
$$c_{\mathrm{vol}}^{\mathrm{3tree}}(b_2, w_3, w_4) = 3 b_2 + 3 w_3 + w_4.$$ -/
def volumeCoeff3Tree (b₂ w₃ w₄ : R) : R :=
  3 * b₂ + 3 * w₃ + w₄

/-- Constant finite-size boundary deficit on the stacked 3-simplex complex $\mathcal{K}_A$:
$$c_0^{\mathrm{3tree}}(b_2, w_3, w_4) = 6 b_2 + 8 w_3 + 3 w_4.$$ -/
def boundaryDeficit3Tree (b₂ w₃ w₄ : R) : R :=
  6 * b₂ + 8 * w₃ + 3 * w₄

/-- **Linear Extensivity of the Stacked 3-Simplex Energy Functional**:
For every $A \ge 3$, the simplicial strong binding energy on $\mathcal{K}_A$ is identically
affine-linear in $A$:
$$B_{\mathrm{simp}}(\mathcal{K}_A) = (3 b_2 + 3 w_3 + w_4) A - (6 b_2 + 8 w_3 + 3 w_4).$$ -/
theorem stackedSimplex_energy_affine_in_A (b₂ w₃ w₄ : R) {A : ℕ} (hA : 3 ≤ A) :
    simplicialBinding b₂ w₃ w₄ (f1Simplex A) (f2Simplex A) (f3Simplex A) =
      volumeCoeff3Tree b₂ w₃ w₄ * (A : R) - boundaryDeficit3Tree b₂ w₃ w₄ := by
  rcases fVector_of_three_le hA with ⟨_, h1, h2, h3⟩
  unfold simplicialBinding volumeCoeff3Tree boundaryDeficit3Tree
  rw [h1, h2, h3]
  have h1le : 6 ≤ 3 * A := by omega
  have h2le : 8 ≤ 3 * A := by omega
  rw [Nat.cast_sub h1le, Nat.cast_sub h2le, Nat.cast_sub hA]
  push_cast
  ring

/-- **Linear Extensivity of the Hierarchical $\alpha$-Cluster Energy Functional**:
For every $N_\alpha \ge 3$ ($A = 4 N_\alpha \ge 12$), evaluating `simplicialBinding` on the
hierarchical $\alpha$-cluster counts
$(f_1 = 9 N_\alpha - 6, f_2 = 4 N_\alpha, f_3 = N_\alpha)$ is identically affine-linear in $N_\alpha$:
$$B_{\mathrm{simp}}(\mathcal{C}_{4 N_\alpha}) = (9 b_2 + 4 w_3 + w_4) N_\alpha - 6 b_2.$$ -/
theorem alphaCluster_energy_affine_in_Nalpha (b₂ w₃ w₄ : R) {Nα : ℕ} (hN : 3 ≤ Nα) :
    simplicialBinding b₂ w₃ w₄
        (totalAlphaClusterEdges (4 * Nα))
        (intraAlphaTriangles (4 * Nα))
        (intraAlphaTetrahedra (4 * Nα)) =
      (9 * b₂ + 4 * w₃ + w₄) * (Nα : R) - 6 * b₂ := by
  rw [totalAlphaClusterEdges_four_mul hN]
  unfold simplicialBinding intraAlphaTriangles intraAlphaTetrahedra
  have hdiv : 4 * Nα / 4 = Nα := Nat.mul_div_right Nα (by decide)
  have hmod : 4 * Nα % 4 = 0 := Nat.mul_mod_right 4 Nα
  rw [hdiv, hmod]
  have hle : 6 ≤ 9 * Nα := by omega
  have hc3 : (0 : ℕ).choose 3 = 0 := rfl
  rw [hc3, add_zero, Nat.cast_sub hle]
  push_cast
  ring

/-- **Isospin-Symmetric Strong Core Mirror Split Theorem**:
Because `simplicialBinding` depends only on the mass number $A = Z + N$ when the 2-body strong
bond weight $b_2$ is isospin-symmetric ($f_{pp}^{\mathrm{strong}} = f_{pn}^{\mathrm{strong}} = f_{nn}^{\mathrm{strong}} = z_D$),
for any mirror pair $(Z, N)$ and $(N, Z)$ with $A = Z + N$, the strong simplicial binding
cancels identically in the mirror difference:
$$(B_{\mathrm{simp}}(\mathcal{K}_A) - E_C(Z)) - (B_{\mathrm{simp}}(\mathcal{K}_A) - E_C(N)) = E_C(N) - E_C(Z).$$ -/
theorem simplicial_mirror_split_pure_coulomb (b₂ w₃ w₄ ecZ ecN : R) (A : ℕ) :
    (simplicialBinding b₂ w₃ w₄ (f1Simplex A) (f2Simplex A) (f3Simplex A) - ecZ) -
      (simplicialBinding b₂ w₃ w₄ (f1Simplex A) (f2Simplex A) (f3Simplex A) - ecN) =
      ecN - ecZ := by
  ring

/-- **Exact Pauli Symmetry-Energy Deficits for Degree-1 Bridge vs Degree-2 Triangle Attachment**:
For any balanced core size $A_{\mathrm{core}} \ge 3$ and excess nucleon count $D = |N - Z|$,
relative to the un-obstructed 3-tree $\mathcal{K}_{A_{\mathrm{core}} + D}$:
1. The degree-1 bridge complex (`pauliBridge`) has linear symmetry-energy deficit
   $(2 b_2 + 3 w_3 + w_4) \cdot D$,
2. The maximal Pauli-legal degree-2 mixed-isospin triangle complex (`pauliTriangle`) has
   linear symmetry-energy deficit $(b_2 + 2 w_3 + w_4) \cdot D$. -/
theorem pauliExcess_symmetry_deficits_eq (b₂ w₃ w₄ : R) {Acore : ℕ} (hA : 3 ≤ Acore) (D : ℕ) :
    simplicialBinding b₂ w₃ w₄
        (f1Simplex (Acore + D)) (f2Simplex (Acore + D)) (f3Simplex (Acore + D)) -
      simplicialBinding b₂ w₃ w₄
        (pauliBridgeF1 Acore D) (pauliBridgeF2 Acore) (pauliBridgeF3 Acore) =
      (2 * b₂ + 3 * w₃ + w₄) * (D : R) ∧
    simplicialBinding b₂ w₃ w₄
        (f1Simplex (Acore + D)) (f2Simplex (Acore + D)) (f3Simplex (Acore + D)) -
      simplicialBinding b₂ w₃ w₄
        (pauliTriangleF1 Acore D) (pauliTriangleF2 Acore D) (pauliTriangleF3 Acore) =
      (b₂ + 2 * w₃ + w₄) * (D : R) := by
  have hAD : 3 ≤ Acore + D := by omega
  rcases fVector_of_three_le hA with ⟨_, h1, h2, h3⟩
  rcases fVector_of_three_le hAD with ⟨_, h1D, h2D, h3D⟩
  unfold simplicialBinding pauliBridgeF1 pauliBridgeF2 pauliBridgeF3
    pauliTriangleF1 pauliTriangleF2 pauliTriangleF3
  rw [h1, h2, h3, h1D, h2D, h3D]
  have h1le : 6 ≤ 3 * Acore := by omega
  have h2le : 8 ≤ 3 * Acore := by omega
  have h1Dle : 6 ≤ 3 * (Acore + D) := by omega
  have h2Dle : 8 ≤ 3 * (Acore + D) := by omega
  push_cast
  rw [Nat.cast_sub h1le, Nat.cast_sub h2le, Nat.cast_sub hA,
    Nat.cast_sub h1Dle, Nat.cast_sub h2Dle, Nat.cast_sub hAD]
  push_cast
  constructor <;> ring

end SimplicialEnergyFunctional

section GPMTSimplicialBridge

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **Per- Nucleon Saturation Decomposition on $\mathcal{K}_A$**:
For every $A \ge 3$ in an ordered field $R$, the per-nucleon binding on $\mathcal{K}_A$ is
the constant bulk volume plateau `volumeCoeff3Tree b₂ w₃ w₄` minus the $O(1/A)$ surface deficit
`boundaryDeficit3Tree b₂ w₃ w₄ / A`. -/
theorem stackedSimplex_per_nucleon_eq (b₂ w₃ w₄ : R) {A : ℕ} (hA : 3 ≤ A) :
    simplicialBinding b₂ w₃ w₄ (f1Simplex A) (f2Simplex A) (f3Simplex A) / (A : R) =
      volumeCoeff3Tree b₂ w₃ w₄ - boundaryDeficit3Tree b₂ w₃ w₄ / (A : R) := by
  have hA0 : (A : R) ≠ 0 := Nat.cast_ne_zero.mpr (by omega)
  rw [stackedSimplex_energy_affine_in_A b₂ w₃ w₄ hA, sub_div, mul_div_cancel_right₀ _ hA0]

/-- **Exact GPMT Higher-Body Cancellation on the Single $\alpha$-Simplex $K_4$**:
On a single $\alpha$-tetrahedron $K_4$ ($f_2 = 4$ triangles, $f_3 = 1$ tetrahedron), the
per-partition GPMT 3-body and 4-body cumulants `mu3GPMT_H4 q` and `mu4GPMT_H4 q` satisfy
$$4 \cdot \mathrm{mu3GPMT\_H4}(q) + 1 \cdot \mathrm{mu4GPMT\_H4}(q) = \mathrm{sRow3GPMT\_H4}(q, 4) > 0$$
for all $q > 0$. -/
theorem gpmt_alpha_higher_body_eq_sRow3_and_pos (q : R) (hq : 0 < q) :
    4 * mu3GPMT_H4 q + 1 * mu4GPMT_H4 q = sRow3GPMT_H4 q 4 ∧
    0 < 4 * mu3GPMT_H4 q + 1 * mu4GPMT_H4 q := by
  rcases mu2_mu3_H4_eq_bridge q with ⟨h2, _, _⟩
  have hid : 4 * mu3GPMT_H4 q + 1 * mu4GPMT_H4 q = sRow3GPMT_H4 q 4 := by
    unfold mu4GPMT_H4
    rw [h2]
    ring
  refine ⟨hid, ?_⟩
  rw [hid]
  exact (sRow3GPMT_H4_four_both_terms_pos q hq).2.2

/-- **Strict Positivity of the 3-Tree Asymptotic Higher-Body GPMT Volume Coefficient**:
On the stacked 3-simplex complex $\mathcal{K}_A$ ($f_2 = 3A - 8$ triangles, $f_3 = A - 3$ tetrahedra),
the asymptotic per-nucleon higher-body GPMT coefficient is $3 \cdot \mathrm{mu3GPMT\_H4}(q) + \mathrm{mu4GPMT\_H4}(q)$,
which equals
$$\frac{2 q^3 ((q^4 + q^2 + 1)^2 + q^4)}{(q^2 + 1)^3 (q^4 + 1)(q^4 + q^2 + 1)} > 0$$
for every $q > 0$. -/
theorem gpmt_threeTree_higher_body_vol_pos (q : R) (hq : 0 < q) :
    3 * mu3GPMT_H4 q + mu4GPMT_H4 q =
      2 * q ^ 3 * ((q ^ 4 + q ^ 2 + 1) ^ 2 + q ^ 4) /
        ((q ^ 2 + 1) ^ 3 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1)) ∧
    0 < 3 * mu3GPMT_H4 q + mu4GPMT_H4 q := by
  have hq2 : q ^ 2 + 1 ≠ 0 := ne_of_gt (sq_add_one_pos q)
  have hq41 : q ^ 4 + 1 ≠ 0 := ne_of_gt (pow_four_add_one_pos q)
  have hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0 := ne_of_gt (pow_four_add_sq_add_one_pos q)
  have hden : h4ModDenom q ≠ 0 := h4ModDenom_ne_zero q hq2 hq41 hq421
  rcases mu2_mu3_H4_eq_bridge q with ⟨_, h3, _⟩
  have hclosed :
      3 * mu3GPMT_H4 q + mu4GPMT_H4 q =
        2 * q ^ 3 * ((q ^ 4 + q ^ 2 + 1) ^ 2 + q ^ 4) /
          ((q ^ 2 + 1) ^ 3 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1)) := by
    rw [h3, dMod111_over_h4ModDenom q hq2 hq41, mu4GPMT_H4_closed_form q hq2 hq41 hq421]
    change
      3 * -(-q ^ 3 * ((q ^ 2 + 1) ^ 2 * (q ^ 4 + 1)) / h4ModDenom q) +
        -q ^ 3 * (q ^ 8 + 2 * q ^ 6 - 2 * q ^ 4 + 2 * q ^ 2 + 1) / h4ModDenom q =
      2 * q ^ 3 * ((q ^ 4 + q ^ 2 + 1) ^ 2 + q ^ 4) / h4ModDenom q
    field_simp [hden]
    ring
  refine ⟨hclosed, ?_⟩
  rw [hclosed]
  apply div_pos
  · apply mul_pos (mul_pos zero_lt_two (pow_pos hq 3))
    have hsq : 0 ≤ (q ^ 4 + q ^ 2 + 1) ^ 2 := sq_nonneg (q ^ 4 + q ^ 2 + 1)
    have hq4 : 0 < q ^ 4 := pow_pos hq 4
    linarith
  · exact mul_pos
      (mul_pos (pow_pos (sq_add_one_pos q) 3) (pow_four_add_one_pos q))
      (pow_four_add_sq_add_one_pos q)

end GPMTSimplicialBridge

end QOU.Nuclear.AlphaSimplexCoordinationDerivation
