import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.Real.Pi.Bounds
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Tactic
import QOU.Nuclear.AlphaSimplexCoordinationDerivation

/-!
# Simplicial Discrete Proton-Pair Coulomb Functional & 3D FCC Packing Radius Transport

This module formalizes the discrete 3D simplicial proton-pair electrostatic functional and
Euclidean close-packing radius transport on nuclear vertex complexes (`qou-usft`, `qou-mumr`),
closing the continuum uniform-sphere assumptions of liquid-drop electrostatics with zero fitted
parameters.

## Main Results

1. **Section 1 — Discrete Pairwise Proton Electrostatic Functional (`discreteCoulombEnergy`)**:
   - Defines `discreteCoulombEnergy` on any finite nucleon vertex set `V` equipped with a
     zero-diagonal symmetric inverse-distance kernel `invDist : V → V → ℝ` and proton occupancy
     `isProton : V → Bool`:
     $$E_C^{\mathrm{disc}}(\alpha\hbar c, \mathrm{invDist}, p)
       = \frac{\alpha\hbar c}{2} \sum_{u \in V} \sum_{v \in V} p_u p_v\,\mathrm{invDist}(u, v).$$
   - Proves exact reduction to the off-diagonal ordered proton pairs `(protonFinset isProton).offDiag`
     (`discreteCoulombPairSum_eq_offDiag_sum`), exact vanishing for $Z \le 1$ (`¹n`, `¹H`, `²H`, `³H`;
     `discreteCoulomb_eq_zero_of_protonCount_le_one`), and non-negativity (`discreteCoulomb_nonneg`).

2. **Section 2 — Exact Regular-Simplex Identity ($A \le 4$: `³He`, `⁴He`) & Continuum Distortion**:
   - Proves `discreteCoulomb_regularSimplex_closed_form`: when distinct vertices sit at equal bond
     length $\ell_{\mathrm{bond}}$ (`uniformBondInvDist`), $E_C^{\mathrm{disc}}$ equals
     $$\frac{Z(Z - 1)}{2} \cdot \frac{\alpha\hbar c}{\ell_{\mathrm{bond}}}
       = \binom{Z}{2} \frac{\alpha\hbar c}{\ell_{\mathrm{bond}}},$$
     with **zero $3/5$ continuum-sphere factor** and **zero $A^{1/3}$ denominator**.
   - Connects directly to `AlphaSimplexCoordinationDerivation.pauli_k4_balanced_isospin`
     (`pauli_k4_forced_single_proton_bond`): every 4-nucleon $s$-wave $K_4$ $\alpha$-simplex has
     exact proton count $Z = 2$ and therefore **1 proton–proton bond**
     ($E_C^{\mathrm{disc}}(^4\mathrm{He}) = E_C^{\mathrm{disc}}(^3\mathrm{He}) = \alpha\hbar c / \ell_{\mathrm{bond}}$),
     whereas the continuum sphere formula $\frac{3}{5} \frac{Z(Z-1)\alpha\hbar c}{\ell_{\mathrm{bond}} A^{1/3}}$
     introduces artificial geometric distortion factors whose cubes are $\frac{72}{125}$ at $A = 3$
     and $\frac{54}{125}$ at $A = 4$ (`continuum_sphere_distortion_A3_and_A4`).

3. **Section 3 — Mirror-Nucleus Strong Cancellation & Discrete Coulomb Displacement Theorems**:
   - Proves the master graph-metric mirror difference identity (`discreteCoulomb_mirror_diff_vertexPotential`)
     for $\bar{p}_u = 1 - p_u$ on any symmetric inverse-distance complex:
     $$E_C^{\mathrm{disc}}(p) - E_C^{\mathrm{disc}}(\bar{p})
       = \frac{\alpha\hbar c}{2} \sum_{u \in V} (2 p_u - 1)\,\sigma(u),
       \qquad \sigma(u) = \sum_{v \in V} \mathrm{invDist}(u, v).$$
   - Specializes to constant-potential / vertex-transitive complexes
     (`discreteCoulomb_mirror_diff_of_const_potential`), the regular simplex
     (`discreteCoulomb_mirror_diff_regularSimplex`), isometric core + single valence nucleon
     configurations (`discreteCoulomb_mirror_diff_isometric_valence`), and the joint net binding
     mirror split with `AlphaSimplexCoordinationDerivation.simplicialBinding`
     (`joint_simplicial_net_mirror_split`).

4. **Section 4 — $N_\alpha$-Cluster & Carbon-12 ($3 \times K_4$, $Z = 6$) Proton-Pair Decomposition**:
   - Proves that $2 N_\alpha$ protons partitioned $(2, 2, \dots, 2)$ across $N_\alpha$ $\alpha$-simplices
     decompose the $\binom{2 N_\alpha}{2}$ unordered proton pairs into $N_\alpha$ intra-$\alpha$ pairs
     plus $4 \binom{N_\alpha}{2}$ inter-$\alpha$ pairs (`multiAlpha_proton_pair_split`), giving
     $3 + 12 = 15$ for $^{12}\mathrm{C}$ (`carbon12_three_alpha_pair_split`) and $4 + 24 = 28$ for
     $^{16}\mathrm{O}$ (`oxygen16_four_alpha_pair_split`).
   - Evaluates the full `16 N_\alpha^2`-term double sum `discreteCoulombEnergy` on `Fin Nα × Fin 4`
     (`discreteCoulomb_equilateral_alphaCluster_eval`, `carbon12_equilateral_three_alpha_coulomb`).

5. **Section 5 — 3D FCC/HCP Close-Packing Voronoi Cell & Packing Radius Transport**:
   - Proves the nearest-neighbor distance identity, Voronoi / rhombic-dodecahedral cell volume
     $V_{\mathrm{cell}} = \ell_{\mathrm{bond}}^3 / \sqrt{2}$, close-packing fraction
     $\eta_{\mathrm{FCC}} = \pi \sqrt{2} / 6$, exact volume balance for
     $R_{\mathrm{FCC}}(\ell_{\mathrm{bond}}, A) = \bigl(\frac{3}{4\pi\sqrt{2}}\bigr)^{1/3} \ell_{\mathrm{bond}} A^{1/3}$,
     the exact sixth-power polynomial identity
     $$(4\pi)^2 \cdot 2 \cdot R_{\mathrm{FCC}}(\ell_{\mathrm{bond}}, A)^6 = 9\,\ell_{\mathrm{bond}}^6\,A^2$$
     (`fcc_packing_radius_sixth_power_identity`), and the strict enclosure
     $0.55 < \bigl(\frac{3}{4\pi\sqrt{2}}\right)^{1/3} < 0.56$ (`fccPackingConst_bounds`).
-/

namespace QOU.Nuclear.SimplicialCoulombGraphMetricDerivation

open QOU.Nuclear.AlphaSimplexCoordinationDerivation

-- ============================================================================
-- § 1. Discrete Pairwise Proton Electrostatic Functional on Vertex Complexes
-- ============================================================================

/-- Real indicator $p_u \in \{0, 1\}$ of proton occupancy at vertex $u \in V$. -/
def protonIndicator {V : Type*} (isProton : V → Bool) (u : V) : ℝ :=
  if isProton u then 1 else 0

/-- Finite subset of proton-occupied vertices $\{u \in V \mid \mathrm{isProton}(u) = \mathrm{true}\}$. -/
def protonFinset {V : Type*} [Fintype V] (isProton : V → Bool) : Finset V :=
  Finset.univ.filter (fun u => isProton u = true)

/-- Total proton number $Z = |\{u \in V \mid \mathrm{isProton}(u) = \mathrm{true}\}|$. -/
def protonCount {V : Type*} [Fintype V] (isProton : V → Bool) : ℕ :=
  (protonFinset isProton).card

/-- Isospin-swapped mirror occupancy $\bar{p}(u) = \neg p(u)$ exchanging protons and neutrons. -/
def mirrorOccupancy {V : Type*} (isProton : V → Bool) (u : V) : Bool :=
  !isProton u

/-- Pointwise mirror indicator identity $\bar{p}_u = 1 - p_u$. -/
theorem protonIndicator_mirror {V : Type*} (isProton : V → Bool) (u : V) :
    protonIndicator (mirrorOccupancy isProton) u = 1 - protonIndicator isProton u := by
  unfold protonIndicator mirrorOccupancy
  cases isProton u <;> norm_num

/-- Each indicator value satisfies $0 \le p_u$. -/
theorem protonIndicator_nonneg {V : Type*} (isProton : V → Bool) (u : V) :
    0 ≤ protonIndicator isProton u := by
  unfold protonIndicator
  split_ifs <;> norm_num

/-- Summing `protonIndicator` over `V` yields `(protonCount isProton : ℝ)`. -/
theorem sum_protonIndicator_eq_protonCount {V : Type*} [Fintype V] (isProton : V → Bool) :
    (∑ u : V, protonIndicator isProton u) = (protonCount isProton : ℝ) := by
  unfold protonIndicator protonCount protonFinset
  rw [← Finset.sum_filter]
  simp

/-- Proton count plus mirror proton (neutron) count equals total mass number $A = |V|$. -/
theorem protonCount_add_mirrorCount_eq_card {V : Type*} [Fintype V] (isProton : V → Bool) :
    protonCount isProton + protonCount (mirrorOccupancy isProton) = Fintype.card V := by
  unfold protonCount protonFinset mirrorOccupancy
  have hcompl :
      Finset.univ.filter (fun u : V => (!isProton u) = true) =
        Finset.univ.filter (fun u : V => ¬ (isProton u = true)) := by
    ext u
    cases isProton u <;> simp
  rw [hcompl, Finset.filter_card_add_filter_neg_card_eq_card, Finset.card_univ]

/-- Ordered-pair inverse-distance sum $\sum_{u \in V} \sum_{v \in V} p_u p_v\,\mathrm{invDist}(u, v)$. -/
def discreteCoulombPairSum {V : Type*} [Fintype V]
    (invDist : V → V → ℝ) (isProton : V → Bool) : ℝ :=
  ∑ u : V, ∑ v : V, protonIndicator isProton u * protonIndicator isProton v * invDist u v

/-- Discrete pairwise proton electrostatic energy functional
$$E_C^{\mathrm{disc}}(\alpha\hbar c, \mathrm{invDist}, p)
  = \frac{\alpha\hbar c}{2} \sum_{u \in V} \sum_{v \in V} p_u p_v\,\mathrm{invDist}(u, v).$$ -/
noncomputable def discreteCoulombEnergy {V : Type*} [Fintype V]
    (alphaHbarC : ℝ) (invDist : V → V → ℝ) (isProton : V → Bool) : ℝ :=
  (alphaHbarC / 2) * discreteCoulombPairSum invDist isProton

/-- When `invDist` vanishes on the diagonal (`∀ u, invDist u u = 0`), the double sum restricts
identically to distinct ordered pairs `(u, v) ∈ (protonFinset isProton).offDiag`. -/
theorem discreteCoulombPairSum_eq_offDiag_sum {V : Type*} [Fintype V] [DecidableEq V]
    (invDist : V → V → ℝ) (hDiag : ∀ u : V, invDist u u = 0) (isProton : V → Bool) :
    discreteCoulombPairSum invDist isProton =
      ∑ x ∈ (protonFinset isProton).offDiag, invDist x.1 x.2 := by
  unfold discreteCoulombPairSum protonIndicator protonFinset
  have hfilter :
      (∑ u : V, ∑ v : V,
        (if isProton u then (1 : ℝ) else 0) * (if isProton v then (1 : ℝ) else 0) * invDist u v) =
      ∑ u ∈ Finset.univ.filter (fun u => isProton u = true),
        ∑ v ∈ Finset.univ.filter (fun v => isProton v = true), invDist u v := by
    rw [Finset.sum_filter]
    refine Finset.sum_congr rfl ?_
    intro u _
    by_cases hu : isProton u = true
    · simp only [hu, ↓reduceIte, one_mul]
      rw [Finset.sum_filter]
      refine Finset.sum_congr rfl ?_
      intro v _
      by_cases hv : isProton v = true <;> simp [hv]
    · simp [hu]
  rw [hfilter, ← Finset.sum_product']
  have hsub :
      (Finset.univ.filter (fun u : V => isProton u = true)).offDiag ⊆
        (Finset.univ.filter (fun u : V => isProton u = true)) ×ˢ
          (Finset.univ.filter (fun v : V => isProton v = true)) := by
    intro x hx
    rw [Finset.mem_product]
    exact ⟨(Finset.mem_offDiag.mp hx).1, (Finset.mem_offDiag.mp hx).2.1⟩
  symm
  refine Finset.sum_subset hsub ?_
  intro x hxprod hxnot
  rw [Finset.mem_product] at hxprod
  rw [Finset.mem_offDiag] at hxnot
  push_neg at hxnot
  have hxeq : x.1 = x.2 := hxnot hxprod.1 hxprod.2
  rw [hxeq, hDiag]

/-- Zero self-interaction for $Z \le 1$: any configuration with at most one proton
(`¹n`, `¹H`, `²H`, `³H`) has identically zero discrete electrostatic energy. -/
theorem discreteCoulomb_eq_zero_of_protonCount_le_one {V : Type*} [Fintype V] [DecidableEq V]
    (alphaHbarC : ℝ) (invDist : V → V → ℝ) (hDiag : ∀ u : V, invDist u u = 0)
    (isProton : V → Bool) (hZ : protonCount isProton ≤ 1) :
    discreteCoulombEnergy alphaHbarC invDist isProton = 0 := by
  unfold discreteCoulombEnergy
  rw [discreteCoulombPairSum_eq_offDiag_sum invDist hDiag isProton]
  have hemp : (protonFinset isProton).offDiag = ∅ := by
    rw [Finset.eq_empty_iff_forall_notMem]
    intro x hx
    rcases Finset.mem_offDiag.mp hx with ⟨hx1, hx2, hne⟩
    have hcard : (protonFinset isProton).card ≤ 1 := hZ
    exact hne (Finset.card_le_one.mp hcard x.1 hx1 x.2 hx2)
  rw [hemp, Finset.sum_empty, mul_zero]

/-- Non-negativity of `discreteCoulombEnergy` for non-negative coupling and inverse distances. -/
theorem discreteCoulomb_nonneg {V : Type*} [Fintype V]
    (alphaHbarC : ℝ) (hα : 0 ≤ alphaHbarC)
    (invDist : V → V → ℝ) (hInv : ∀ u v : V, 0 ≤ invDist u v)
    (isProton : V → Bool) :
    0 ≤ discreteCoulombEnergy alphaHbarC invDist isProton := by
  unfold discreteCoulombEnergy discreteCoulombPairSum
  apply mul_nonneg (by linarith)
  refine Finset.sum_nonneg ?_
  intro u _
  refine Finset.sum_nonneg ?_
  intro v _
  exact mul_nonneg
    (mul_nonneg (protonIndicator_nonneg isProton u) (protonIndicator_nonneg isProton v))
    (hInv u v)

-- ============================================================================
-- § 2. Regular-Simplex Identity (A ≤ 4: ³He, ⁴He) & Continuum 3/5 Distortion
-- ============================================================================

/-- Combinatorial identity $2 \binom{n}{2} = n(n - 1)$ in $\mathbb{N}$. -/
theorem two_mul_choose_two_nat (n : ℕ) : 2 * n.choose 2 = n * (n - 1) := by
  induction n with
  | zero => rfl
  | succ k ih =>
    have hc : (k + 1).choose 2 = k + k.choose 2 := by
      simpa using Nat.choose_succ_succ k 1
    rw [hc, Nat.mul_add, ih]
    cases k with
    | zero => rfl
    | succ m =>
      simp only [Nat.add_sub_cancel]
      ring

/-- Real-cast binomial identity $\binom{Z}{2} = Z(Z - 1)/2$ for all $Z \in \mathbb{N}$. -/
theorem choose_two_cast_real (Z : ℕ) :
    (Z.choose 2 : ℝ) = (Z : ℝ) * ((Z : ℝ) - 1) / 2 := by
  cases Z with
  | zero => norm_num
  | succ k =>
    have hnat := two_mul_choose_two_nat (k + 1)
    have hcast : (2 : ℝ) * ((k + 1).choose 2 : ℝ) = ((k + 1 : ℕ) : ℝ) * ((k : ℕ) : ℝ) := by
      exact_mod_cast hnat
    push_cast at hcast ⊢
    linarith

/-- Cardinality of `s.offDiag` equals $2 \binom{|s|}{2}$. -/
theorem offDiag_card_eq_two_mul_choose {V : Type*} [DecidableEq V] (s : Finset V) :
    s.offDiag.card = 2 * s.card.choose 2 := by
  rw [Finset.offDiag_card, two_mul_choose_two_nat]
  cases s.card with
  | zero => rfl
  | succ k =>
    have hmul : (k + 1) * (k + 1) = (k + 1) * k + (k + 1) := by ring
    rw [hmul, Nat.add_sub_cancel]
    simp only [Nat.add_sub_cancel]

/-- Uniform inverse-distance kernel on a regular simplex (`A ≤ 4`) of edge length `bondLen`:
`0` on the diagonal and `1 / bondLen` on all distinct vertex pairs `u ≠ v`. -/
noncomputable def uniformBondInvDist {V : Type*} [DecidableEq V] (bondLen : ℝ) (u v : V) : ℝ :=
  if u = v then 0 else 1 / bondLen

theorem uniformBondInvDist_diag {V : Type*} [DecidableEq V] (bondLen : ℝ) (u : V) :
    uniformBondInvDist bondLen u u = 0 := by
  simp [uniformBondInvDist]

theorem uniformBondInvDist_symm {V : Type*} [DecidableEq V] (bondLen : ℝ) (u v : V) :
    uniformBondInvDist bondLen u v = uniformBondInvDist bondLen v u := by
  unfold uniformBondInvDist
  by_cases h : u = v
  · subst h; rfl
  · have h' : v ≠ u := Ne.symm h
    rw [if_neg h, if_neg h']

/-- **Regular-Simplex Discrete Electrostatic Identity**:
When all distinct vertices sit at equal bond length `bondLen` (`uniformBondInvDist bondLen`),
the discrete proton electrostatic energy equals identically
$$\frac{Z(Z - 1)}{2} \cdot \frac{\alpha\hbar c}{\ell_{\mathrm{bond}}}
  = \binom{Z}{2} \frac{\alpha\hbar c}{\ell_{\mathrm{bond}}},$$
with **zero $3/5$ continuum-sphere factor** and **zero $A^{1/3}$ scaling**. -/
theorem discreteCoulomb_regularSimplex_closed_form
    {V : Type*} [Fintype V] [DecidableEq V]
    (alphaHbarC bondLen : ℝ) (isProton : V → Bool) :
    discreteCoulombEnergy alphaHbarC (uniformBondInvDist bondLen) isProton =
      ((protonCount isProton : ℝ) * ((protonCount isProton : ℝ) - 1) / 2) *
        (alphaHbarC / bondLen) ∧
    discreteCoulombEnergy alphaHbarC (uniformBondInvDist bondLen) isProton =
      ((protonCount isProton).choose 2 : ℝ) * (alphaHbarC / bondLen) := by
  have hoff :
      discreteCoulombPairSum (uniformBondInvDist bondLen) isProton =
        ((protonFinset isProton).offDiag.card : ℝ) * (1 / bondLen) := by
    rw [discreteCoulombPairSum_eq_offDiag_sum (uniformBondInvDist bondLen)
      (uniformBondInvDist_diag bondLen) isProton]
    have hconst :
        ∀ x ∈ (protonFinset isProton).offDiag,
          uniformBondInvDist bondLen x.1 x.2 = 1 / bondLen := by
      intro x hx
      have hne : x.1 ≠ x.2 := (Finset.mem_offDiag.mp hx).2.2
      simp [uniformBondInvDist, hne]
    rw [Finset.sum_congr rfl hconst, Finset.sum_const, nsmul_eq_mul]
  have hcard : ((protonFinset isProton).offDiag.card : ℝ) =
      2 * ((protonCount isProton).choose 2 : ℝ) := by
    unfold protonCount
    exact_mod_cast offDiag_card_eq_two_mul_choose (protonFinset isProton)
  have hbin :
      discreteCoulombEnergy alphaHbarC (uniformBondInvDist bondLen) isProton =
        ((protonCount isProton).choose 2 : ℝ) * (alphaHbarC / bondLen) := by
    unfold discreteCoulombEnergy
    rw [hoff, hcard]
    ring
  refine ⟨?_, hbin⟩
  rw [hbin, choose_two_cast_real]

/-- **Single Proton–Proton Bond Identity for $Z = 2$ (`³He`, `⁴He`)**:
For any simplex with $Z = 2$ protons, there is $\binom{2}{2} = 1$ proton–proton bond, so
$E_C^{\mathrm{disc}} = \alpha\hbar c / \ell_{\mathrm{bond}}$. -/
theorem he3_and_he4_single_proton_bond_identity
    {V : Type*} [Fintype V] [DecidableEq V]
    (alphaHbarC bondLen : ℝ) (isProton : V → Bool) (hZ : protonCount isProton = 2) :
    discreteCoulombEnergy alphaHbarC (uniformBondInvDist bondLen) isProton =
      alphaHbarC / bondLen := by
  rw [(discreteCoulomb_regularSimplex_closed_form alphaHbarC bondLen isProton).2, hZ]
  norm_num

/-- **Pauli $K_4$ $\alpha$-Simplex Forced Single Proton–Proton Bond**:
Combining `AlphaSimplexCoordinationDerivation.pauli_k4_balanced_isospin` with
`discreteCoulomb_regularSimplex_closed_form`: on any 4-nucleon $s$-wave clique `V`
(`Fintype.card V = 4`) with injective `SpinIsospinState` coloring `c : V → SpinIsospinState`,
the proton occupancy `fun u => decide ((c u).2 = 0)` has `protonCount = 2` and exact single-bond
electrostatic energy $\alpha\hbar c / \ell_{\mathrm{bond}}$. -/
theorem pauli_k4_forced_single_proton_bond
    {V : Type*} [Fintype V] [DecidableEq V]
    (hcard : Fintype.card V = 4)
    (c : V → SpinIsospinState) (hc : Function.Injective c)
    (alphaHbarC bondLen : ℝ) :
    protonCount (fun u : V => decide ((c u).2 = 0)) = 2 ∧
    discreteCoulombEnergy alphaHbarC (uniformBondInvDist bondLen)
        (fun u : V => decide ((c u).2 = 0)) =
      alphaHbarC / bondLen := by
  have hk4 := (pauli_k4_balanced_isospin hcard c hc).1
  have hp : protonCount (fun u : V => decide ((c u).2 = 0)) = 2 := by
    unfold protonCount protonFinset
    simpa using hk4
  exact ⟨hp, he3_and_he4_single_proton_bond_identity alphaHbarC bondLen _ hp⟩

/-- Continuum uniform-ball electrostatic formula
$$E_C^{\mathrm{sphere}}(\alpha\hbar c, r_0, Z, A)
  = \frac{3}{5} \frac{Z(Z - 1)\,\alpha\hbar c}{r_0\,A^{1/3}}.$$ -/
noncomputable def continuumSphereCoulomb (alphaHbarC r0 : ℝ) (Z A : ℕ) : ℝ :=
  (3 / 5) * (Z : ℝ) * ((Z : ℝ) - 1) * alphaHbarC / (r0 * (A : ℝ) ^ ((1 : ℝ) / 3))

/-- Helper: $((A : \mathbb{R})^{1/3})^3 = A$ for $A \in \mathbb{N}$. -/
theorem natCast_rpow_one_third_pow_three (A : ℕ) :
    ((A : ℝ) ^ ((1 : ℝ) / 3)) ^ 3 = (A : ℝ) := by
  have hnonneg : (0 : ℝ) ≤ (A : ℝ) := Nat.cast_nonneg A
  rw [← Real.rpow_natCast ((A : ℝ) ^ ((1 : ℝ) / 3)) 3, ← Real.rpow_mul hnonneg]
  norm_num

/-- **Continuum Uniform-Sphere Geometric Distortion Theorem at $A = 3$ and $A = 4$**:
For $Z = 2$ (`³He` at $A = 3$ and `⁴He` at $A = 4$) with $r_0 = \ell_{\mathrm{bond}} > 0$ and
$\alpha\hbar c > 0$, the ratio $E_C^{\mathrm{sphere}} / E_C^{\mathrm{disc}}$ equals
$\frac{6}{5 \cdot A^{1/3}}$, whose exact cube is $\frac{72}{125} < 1$ at $A = 3$
($\approx 0.83203^3$) and $\frac{54}{125} < 1$ at $A = 4$ ($\approx 0.75595^3$). -/
theorem continuum_sphere_distortion_A3_and_A4
    {V : Type*} [Fintype V] [DecidableEq V]
    (alphaHbarC bondLen : ℝ) (hα : 0 < alphaHbarC) (hb : 0 < bondLen)
    (isProton : V → Bool) (hZ : protonCount isProton = 2) :
    (continuumSphereCoulomb alphaHbarC bondLen 2 3 /
        discreteCoulombEnergy alphaHbarC (uniformBondInvDist bondLen) isProton) ^ 3 = 72 / 125 ∧
    (continuumSphereCoulomb alphaHbarC bondLen 2 4 /
        discreteCoulombEnergy alphaHbarC (uniformBondInvDist bondLen) isProton) ^ 3 = 54 / 125 ∧
    (72 / 125 : ℝ) < 1 ∧ (54 / 125 : ℝ) < 1 := by
  rw [he3_and_he4_single_proton_bond_identity alphaHbarC bondLen isProton hZ]
  unfold continuumSphereCoulomb
  push_cast
  have hα0 : alphaHbarC ≠ 0 := ne_of_gt hα
  have hb0 : bondLen ≠ 0 := ne_of_gt hb
  have h3pow : ((3 : ℝ) ^ ((1 : ℝ) / 3)) ^ 3 = (3 : ℝ) := by
    simpa using natCast_rpow_one_third_pow_three 3
  have h4pow : ((4 : ℝ) ^ ((1 : ℝ) / 3)) ^ 3 = (4 : ℝ) := by
    simpa using natCast_rpow_one_third_pow_three 4
  have h3ne : ((3 : ℝ) ^ ((1 : ℝ) / 3)) ≠ 0 := by positivity
  have h4ne : ((4 : ℝ) ^ ((1 : ℝ) / 3)) ≠ 0 := by positivity
  refine ⟨?_, ?_, by norm_num, by norm_num⟩
  · have hrat3 :
        (3 / 5 * (2 : ℝ) * ((2 : ℝ) - 1) * alphaHbarC /
          (bondLen * (3 : ℝ) ^ ((1 : ℝ) / 3))) / (alphaHbarC / bondLen) =
        (6 / 5) / ((3 : ℝ) ^ ((1 : ℝ) / 3)) := by
      field_simp [hα0, hb0, h3ne]
      ring
    rw [hrat3, div_pow, h3pow]
    norm_num
  · have hrat4 :
        (3 / 5 * (2 : ℝ) * ((2 : ℝ) - 1) * alphaHbarC /
          (bondLen * (4 : ℝ) ^ ((1 : ℝ) / 3))) / (alphaHbarC / bondLen) =
        (6 / 5) / ((4 : ℝ) ^ ((1 : ℝ) / 3)) := by
      field_simp [hα0, hb0, h4ne]
      ring
    rw [hrat4, div_pow, h4pow]
    norm_num

-- ============================================================================
-- § 3. Mirror-Nucleus Strong Cancellation & Discrete Coulomb Displacement
-- ============================================================================

/-- Electrostatic inverse-distance vertex potential $\sigma(u) = \sum_{v \in V} \mathrm{invDist}(u, v)$. -/
def vertexPotential {V : Type*} [Fintype V] (invDist : V → V → ℝ) (u : V) : ℝ :=
  ∑ v : V, invDist u v

/-- **Master Graph-Metric Mirror Electrostatic Difference Theorem**:
For any symmetric inverse-distance kernel `invDist` (`invDist u v = invDist v u`) and any
proton occupancy `isProton : V → Bool` with mirror occupancy `mirrorOccupancy isProton`,
$$E_C^{\mathrm{disc}}(p) - E_C^{\mathrm{disc}}(\bar{p})
  = \frac{\alpha\hbar c}{2} \sum_{u \in V} (2 p_u - 1)\,\sigma(u).$$ -/
theorem discreteCoulomb_mirror_diff_vertexPotential {V : Type*} [Fintype V]
    (alphaHbarC : ℝ) (invDist : V → V → ℝ) (hSymm : ∀ u v : V, invDist u v = invDist v u)
    (isProton : V → Bool) :
    discreteCoulombEnergy alphaHbarC invDist isProton -
      discreteCoulombEnergy alphaHbarC invDist (mirrorOccupancy isProton) =
    (alphaHbarC / 2) *
      ∑ u : V, (2 * protonIndicator isProton u - 1) * vertexPotential invDist u := by
  unfold discreteCoulombEnergy discreteCoulombPairSum vertexPotential
  rw [← mul_sub]
  congr 1
  rw [← Finset.sum_sub_distrib]
  have hterm :
      (∑ x : V,
        ((∑ v : V, protonIndicator isProton x * protonIndicator isProton v * invDist x v) -
         (∑ v : V, protonIndicator (mirrorOccupancy isProton) x *
            protonIndicator (mirrorOccupancy isProton) v * invDist x v))) =
      ∑ u : V, ∑ v : V,
        (protonIndicator isProton u + protonIndicator isProton v - 1) * invDist u v := by
    refine Finset.sum_congr rfl ?_
    intro u _
    rw [← Finset.sum_sub_distrib]
    refine Finset.sum_congr rfl ?_
    intro v _
    rw [protonIndicator_mirror, protonIndicator_mirror]
    ring
  rw [hterm]
  have hsplit :
      (∑ u : V, ∑ v : V,
        (protonIndicator isProton u + protonIndicator isProton v - 1) * invDist u v) =
      (∑ u : V, ∑ v : V, protonIndicator isProton u * invDist u v) +
      (∑ u : V, ∑ v : V, protonIndicator isProton v * invDist u v) -
      (∑ u : V, ∑ v : V, invDist u v) := by
    simp only [sub_mul, add_mul, one_mul, Finset.sum_sub_distrib, Finset.sum_add_distrib]
  rw [hsplit]
  have hswap :
      (∑ u : V, ∑ v : V, protonIndicator isProton v * invDist u v) =
      (∑ u : V, ∑ v : V, protonIndicator isProton u * invDist u v) := by
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl ?_
    intro v _
    refine Finset.sum_congr rfl ?_
    intro u _
    rw [hSymm u v]
  rw [hswap]
  have hpull :
      ∀ u : V,
        (∑ v : V, protonIndicator isProton u * invDist u v) =
          protonIndicator isProton u * ∑ v : V, invDist u v := by
    intro u
    rw [Finset.mul_sum]
  simp only [hpull]
  rw [← Finset.sum_add_distrib, ← Finset.sum_sub_distrib]
  refine Finset.sum_congr rfl ?_
  intro u _
  ring

/-- **Constant-Potential (Vertex-Transitive) Mirror Electrostatic Difference**:
If every vertex of `(V, invDist)` has equal electrostatic potential `vertexPotential invDist u = σ₀`,
then with $Z = \mathrm{protonCount}\;p$ and $N = \mathrm{protonCount}\;\bar{p}$,
$$E_C^{\mathrm{disc}}(p) - E_C^{\mathrm{disc}}(\bar{p})
  = \frac{\alpha\hbar c}{2}\,((Z : \mathbb{R}) - (N : \mathbb{R}))\,\sigma_0.$$ -/
theorem discreteCoulomb_mirror_diff_of_const_potential {V : Type*} [Fintype V]
    (alphaHbarC σ₀ : ℝ) (invDist : V → V → ℝ) (hSymm : ∀ u v : V, invDist u v = invDist v u)
    (hConst : ∀ u : V, vertexPotential invDist u = σ₀) (isProton : V → Bool) :
    discreteCoulombEnergy alphaHbarC invDist isProton -
      discreteCoulombEnergy alphaHbarC invDist (mirrorOccupancy isProton) =
    (alphaHbarC / 2) *
      ((protonCount isProton : ℝ) - (protonCount (mirrorOccupancy isProton) : ℝ)) * σ₀ := by
  rw [discreteCoulomb_mirror_diff_vertexPotential alphaHbarC invDist hSymm isProton]
  have hsum :
      (∑ u : V, (2 * protonIndicator isProton u - 1) * vertexPotential invDist u) =
      ((2 * ∑ u : V, protonIndicator isProton u) - (Fintype.card V : ℝ)) * σ₀ := by
    simp only [hConst, sub_mul, Finset.sum_sub_distrib, one_mul, Finset.sum_const,
      Finset.card_univ, nsmul_eq_mul]
    have h2 :
        (∑ x : V, 2 * protonIndicator isProton x * σ₀) =
          2 * (∑ x : V, protonIndicator isProton x) * σ₀ := by
      calc
        (∑ x : V, 2 * protonIndicator isProton x * σ₀) =
            ∑ x : V, (2 * σ₀) * protonIndicator isProton x := by
          refine Finset.sum_congr rfl ?_
          intro x _; ring
        _ = (2 * σ₀) * ∑ x : V, protonIndicator isProton x := by rw [← Finset.mul_sum]
        _ = 2 * (∑ x : V, protonIndicator isProton x) * σ₀ := by ring
    rw [h2]
  rw [hsum, sum_protonIndicator_eq_protonCount]
  have hcard : (Fintype.card V : ℝ) =
      (protonCount isProton : ℝ) + (protonCount (mirrorOccupancy isProton) : ℝ) := by
    exact_mod_cast (protonCount_add_mirrorCount_eq_card isProton).symm
  rw [hcard]
  ring

/-- **Regular-Simplex Mirror Electrostatic Difference**:
On a non-empty regular simplex (`1 ≤ Fintype.card V`) of bond length `bondLen`,
$$E_C^{\mathrm{disc}}(p) - E_C^{\mathrm{disc}}(\bar{p})
  = \frac{(Z - N)(A - 1)}{2} \cdot \frac{\alpha\hbar c}{\ell_{\mathrm{bond}}}
  = \frac{Z(Z - 1) - N(N - 1)}{2} \cdot \frac{\alpha\hbar c}{\ell_{\mathrm{bond}}}.$$ -/
theorem discreteCoulomb_mirror_diff_regularSimplex {V : Type*} [Fintype V] [DecidableEq V]
    (hV : 1 ≤ Fintype.card V) (alphaHbarC bondLen : ℝ) (isProton : V → Bool) :
    discreteCoulombEnergy alphaHbarC (uniformBondInvDist bondLen) isProton -
      discreteCoulombEnergy alphaHbarC (uniformBondInvDist bondLen) (mirrorOccupancy isProton) =
    (((protonCount isProton : ℝ) - (protonCount (mirrorOccupancy isProton) : ℝ)) *
      ((Fintype.card V : ℝ) - 1) / 2) * (alphaHbarC / bondLen) ∧
    discreteCoulombEnergy alphaHbarC (uniformBondInvDist bondLen) isProton -
      discreteCoulombEnergy alphaHbarC (uniformBondInvDist bondLen) (mirrorOccupancy isProton) =
    (((protonCount isProton : ℝ) * ((protonCount isProton : ℝ) - 1) -
      (protonCount (mirrorOccupancy isProton) : ℝ) *
        ((protonCount (mirrorOccupancy isProton) : ℝ) - 1)) / 2) * (alphaHbarC / bondLen) := by
  have hz1 := (discreteCoulomb_regularSimplex_closed_form alphaHbarC bondLen isProton).1
  have hz2 :=
    (discreteCoulomb_regularSimplex_closed_form alphaHbarC bondLen (mirrorOccupancy isProton)).1
  have hcard : (Fintype.card V : ℝ) =
      (protonCount isProton : ℝ) + (protonCount (mirrorOccupancy isProton) : ℝ) := by
    exact_mod_cast (protonCount_add_mirrorCount_eq_card isProton).symm
  have _ := hV
  rw [hz1, hz2]
  refine ⟨?_, by ring⟩
  rw [hcard]
  ring

/-- **Isometric Core + Valence Nucleon Mirror Displacement Theorem**:
On a general (not necessarily vertex-transitive) nuclear complex `(V, invDist)` where a distance
automorphism `π : V ≃ V` fixes a single valence nucleon site `vStar` (`isProton vStar = true`)
and swaps the core proton and neutron sites (`∀ u ≠ vStar, mirrorOccupancy isProton (π u) = isProton u`),
the core–core proton repulsion cancels identically across the mirror pair, leaving purely the
electrostatic potential of the valence proton in the field of the core protons:
$$E_C^{\mathrm{disc}}(p) - E_C^{\mathrm{disc}}(\bar{p})
  = \alpha\hbar c \sum_{u \in V} p_u\,\mathrm{invDist}(v_\star, u).$$ -/
theorem discreteCoulomb_mirror_diff_isometric_valence {V : Type*} [Fintype V] [DecidableEq V]
    (alphaHbarC : ℝ) (invDist : V → V → ℝ)
    (hDiag : ∀ u : V, invDist u u = 0)
    (hSymm : ∀ u v : V, invDist u v = invDist v u)
    (isProton : V → Bool) (vStar : V) (hvStar : isProton vStar = true)
    (π : V ≃ V) (hπStar : π vStar = vStar)
    (hπIso : ∀ u v : V, invDist (π u) (π v) = invDist u v)
    (hπCore : ∀ u : V, u ≠ vStar → mirrorOccupancy isProton (π u) = isProton u) :
    discreteCoulombEnergy alphaHbarC invDist isProton -
      discreteCoulombEnergy alphaHbarC invDist (mirrorOccupancy isProton) =
    alphaHbarC * ∑ u : V, protonIndicator isProton u * invDist vStar u := by
  let coreInd : V → ℝ := fun u => if u = vStar then 0 else protonIndicator isProton u
  have hp_decomp : ∀ u : V,
      protonIndicator isProton u = coreInd u + (if u = vStar then 1 else 0) := by
    intro u
    dsimp [coreInd]
    by_cases h : u = vStar
    · rw [h]; simp [protonIndicator, hvStar]
    · simp [h]
  have hmir_star : mirrorOccupancy isProton vStar = false := by
    simp [mirrorOccupancy, hvStar]
  have hmir_eq : ∀ u : V,
      protonIndicator (mirrorOccupancy isProton) (π u) = coreInd u := by
    intro u
    dsimp [coreInd]
    by_cases h : u = vStar
    · rw [h]; simp [hπStar, protonIndicator, hmir_star]
    · unfold protonIndicator
      rw [hπCore u h, if_neg h]
  have hmir_sum :
      discreteCoulombPairSum invDist (mirrorOccupancy isProton) =
        ∑ u : V, ∑ v : V, coreInd u * coreInd v * invDist u v := by
    unfold discreteCoulombPairSum
    rw [← Equiv.sum_comp π]
    refine Finset.sum_congr rfl ?_
    intro u _
    rw [← Equiv.sum_comp π]
    refine Finset.sum_congr rfl ?_
    intro v _
    rw [hmir_eq u, hmir_eq v, hπIso u v]
  have hp_sum :
      discreteCoulombPairSum invDist isProton =
        (∑ u : V, ∑ v : V, coreInd u * coreInd v * invDist u v) +
        2 * ∑ u : V, coreInd u * invDist vStar u := by
    unfold discreteCoulombPairSum
    have hexp :
        (∑ u : V, ∑ v : V, protonIndicator isProton u * protonIndicator isProton v * invDist u v) =
        (∑ u : V, ∑ v : V, coreInd u * coreInd v * invDist u v) +
        (∑ u : V, ∑ v : V, coreInd u * (if v = vStar then (1 : ℝ) else 0) * invDist u v) +
        (∑ u : V, ∑ v : V, (if u = vStar then (1 : ℝ) else 0) * coreInd v * invDist u v) +
        (∑ u : V, ∑ v : V,
          (if u = vStar then (1 : ℝ) else 0) * (if v = vStar then (1 : ℝ) else 0) * invDist u v) := by
      simp only [hp_decomp]
      have hring : ∀ u v : V,
          (coreInd u + (if u = vStar then (1 : ℝ) else 0)) *
            (coreInd v + (if v = vStar then (1 : ℝ) else 0)) * invDist u v =
          coreInd u * coreInd v * invDist u v +
            coreInd u * (if v = vStar then (1 : ℝ) else 0) * invDist u v +
            (if u = vStar then (1 : ℝ) else 0) * coreInd v * invDist u v +
            (if u = vStar then (1 : ℝ) else 0) * (if v = vStar then (1 : ℝ) else 0) * invDist u v := by
        intro u v; ring
      simp only [hring, Finset.sum_add_distrib]
    rw [hexp]
    have hs1 :
        (∑ u : V, ∑ v : V, coreInd u * (if v = vStar then (1 : ℝ) else 0) * invDist u v) =
        ∑ u : V, coreInd u * invDist vStar u := by
      refine Finset.sum_congr rfl ?_
      intro u _
      have inner :
          (∑ v : V, coreInd u * (if v = vStar then (1 : ℝ) else 0) * invDist u v) =
          ∑ v : V, if v = vStar then coreInd u * invDist u v else 0 := by
        refine Finset.sum_congr rfl ?_
        intro v _; split_ifs <;> ring
      rw [inner, Finset.sum_ite_eq' Finset.univ vStar]
      simp [hSymm u vStar]
    have hs2 :
        (∑ u : V, ∑ v : V, (if u = vStar then (1 : ℝ) else 0) * coreInd v * invDist u v) =
        ∑ v : V, coreInd v * invDist vStar v := by
      rw [Finset.sum_comm]
      refine Finset.sum_congr rfl ?_
      intro v _
      have inner :
          (∑ u : V, (if u = vStar then (1 : ℝ) else 0) * coreInd v * invDist u v) =
          ∑ u : V, if u = vStar then coreInd v * invDist u v else 0 := by
        refine Finset.sum_congr rfl ?_
        intro u _; split_ifs <;> ring
      rw [inner, Finset.sum_ite_eq' Finset.univ vStar]
      simp
    have hs3 :
        (∑ u : V, ∑ v : V,
          (if u = vStar then (1 : ℝ) else 0) * (if v = vStar then (1 : ℝ) else 0) * invDist u v) = 0 := by
      refine Finset.sum_eq_zero ?_
      intro u _
      refine Finset.sum_eq_zero ?_
      intro v _
      by_cases hu : u = vStar
      · by_cases hv : v = vStar
        · rw [if_pos hu, if_pos hv, hu, hv, hDiag vStar, mul_zero]
        · rw [if_neg hv, mul_zero, zero_mul]
      · rw [if_neg hu, zero_mul, zero_mul]
    rw [hs1, hs2, hs3]
    ring
  have hcore_eq_full :
      (∑ u : V, coreInd u * invDist vStar u) =
      ∑ u : V, protonIndicator isProton u * invDist vStar u := by
    refine Finset.sum_congr rfl ?_
    intro u _
    dsimp [coreInd]
    by_cases hu : u = vStar
    · rw [if_pos hu, hu, hDiag vStar, zero_mul, mul_zero]
    · rw [if_neg hu]
  unfold discreteCoulombEnergy
  rw [hp_sum, hmir_sum, hcore_eq_full]
  ring

/-- **Joint Strong Simplicial + Discrete Coulomb Mirror Split**:
Combining `AlphaSimplexCoordinationDerivation.simplicialBinding` (charge-symmetric strong core)
with `discreteCoulombEnergy`, the net binding split between a mirror pair $(p, \bar{p})$ on an
$A$-vertex complex equals the discrete electrostatic difference identically:
$$(B_{\mathrm{simp}}(\mathcal{K}_A) - E_C^{\mathrm{disc}}(\bar{p}))
  - (B_{\mathrm{simp}}(\mathcal{K}_A) - E_C^{\mathrm{disc}}(p))
  = E_C^{\mathrm{disc}}(p) - E_C^{\mathrm{disc}}(\bar{p}).$$ -/
theorem joint_simplicial_net_mirror_split {V : Type*} [Fintype V]
    (b₂ w₃ w₄ alphaHbarC : ℝ) (invDist : V → V → ℝ) (isProton : V → Bool) :
    (simplicialBinding b₂ w₃ w₄
        (f1Simplex (Fintype.card V)) (f2Simplex (Fintype.card V)) (f3Simplex (Fintype.card V)) -
      discreteCoulombEnergy alphaHbarC invDist (mirrorOccupancy isProton)) -
    (simplicialBinding b₂ w₃ w₄
        (f1Simplex (Fintype.card V)) (f2Simplex (Fintype.card V)) (f3Simplex (Fintype.card V)) -
      discreteCoulombEnergy alphaHbarC invDist isProton) =
    discreteCoulombEnergy alphaHbarC invDist isProton -
      discreteCoulombEnergy alphaHbarC invDist (mirrorOccupancy isProton) := by
  ring

-- ============================================================================
-- § 4. N_α-Cluster & Carbon-12 (Z = 6, 3 × K₄) Proton-Pair Decomposition
-- ============================================================================

/-- **General $N_\alpha$-Cluster Proton-Pair Decomposition**:
When $Z = 2 N_\alpha$ protons are partitioned $(2, 2, \dots, 2)$ across $N_\alpha$ $\alpha$-tetrahedra,
the $\binom{2 N_\alpha}{2}$ unordered proton pairs split into $N_\alpha \cdot \binom{2}{2} = N_\alpha$
intra-$\alpha$ pairs plus $4 \binom{N_\alpha}{2}$ inter-$\alpha$ pairs:
$$\binom{2 N_\alpha}{2} = N_\alpha + 4 \binom{N_\alpha}{2}.$$ -/
theorem multiAlpha_proton_pair_split (Nα : ℕ) :
    (2 * Nα).choose 2 = Nα * (2 : ℕ).choose 2 + 4 * Nα.choose 2 := by
  have hc2 : (2 : ℕ).choose 2 = 1 := by decide
  rw [hc2, Nat.mul_one]
  induction Nα with
  | zero => decide
  | succ k ih =>
    have hstep2 : (2 * (k + 1)).choose 2 = (2 * k + 1) + 2 * k + (2 * k).choose 2 := by
      have hmul : 2 * (k + 1) = (2 * k + 1) + 1 := by ring
      rw [hmul]
      have ha : ((2 * k + 1) + 1).choose 2 = (2 * k + 1) + (2 * k + 1).choose 2 := by
        simpa using Nat.choose_succ_succ (2 * k + 1) 1
      have hb : (2 * k + 1).choose 2 = 2 * k + (2 * k).choose 2 := by
        simpa using Nat.choose_succ_succ (2 * k) 1
      rw [ha, hb]
      ring
    have hstep1 : (k + 1).choose 2 = k + k.choose 2 := by
      simpa using Nat.choose_succ_succ k 1
    rw [hstep2, hstep1, ih]
    ring

/-- **Carbon-12 ($Z = 6, 3 \times K_4$) Proton-Pair Decomposition**:
$6$ protons partitioned $2 + 2 + 2$ across $3$ $\alpha$-tetrahedra yield $\binom{6}{2} = 15$
total proton pairs: **3 intra-$\alpha$ pairs** + **12 inter-$\alpha$ pairs** ($3 + 12 = 15$). -/
theorem carbon12_three_alpha_pair_split :
    (6 : ℕ).choose 2 = 15 ∧
    3 * (2 : ℕ).choose 2 = 3 ∧
    4 * (3 : ℕ).choose 2 = 12 ∧
    3 * (2 : ℕ).choose 2 + 4 * (3 : ℕ).choose 2 = (6 : ℕ).choose 2 := by
  decide

/-- **Oxygen-16 ($Z = 8, 4 \times K_4$) Proton-Pair Decomposition**:
$8$ protons partitioned $2 + 2 + 2 + 2$ across $4$ tetrahedral $\alpha$-clusters yield
$\binom{8}{2} = 28$ total proton pairs: **4 intra-$\alpha$ pairs** + **24 inter-$\alpha$ pairs**
($4 + 24 = 28$). -/
theorem oxygen16_four_alpha_pair_split :
    (8 : ℕ).choose 2 = 28 ∧
    4 * (2 : ℕ).choose 2 = 4 ∧
    4 * (4 : ℕ).choose 2 = 24 ∧
    4 * (2 : ℕ).choose 2 + 4 * (4 : ℕ).choose 2 = (8 : ℕ).choose 2 := by
  decide

/-- Two-scale inverse-distance kernel on the $N_\alpha$-cluster vertex space `Fin Nα × Fin 4`,
with intra-$\alpha$ inverse bond length `1 / intraBond` for distinct vertices in the same
$\alpha$-tetrahedron and effective inter-$\alpha$ inverse distance `1 / interDist` between
vertices in distinct $\alpha$-tetrahedra. -/
noncomputable def alphaClusterInvDist (Nα : ℕ) (intraBond interDist : ℝ)
    (u v : Fin Nα × Fin 4) : ℝ :=
  if u = v then 0
  else if u.1 = v.1 then 1 / intraBond
  else 1 / interDist

theorem alphaClusterInvDist_diag (Nα : ℕ) (intraBond interDist : ℝ) (u : Fin Nα × Fin 4) :
    alphaClusterInvDist Nα intraBond interDist u u = 0 := by
  simp [alphaClusterInvDist]

theorem alphaClusterInvDist_symm (Nα : ℕ) (intraBond interDist : ℝ) (u v : Fin Nα × Fin 4) :
    alphaClusterInvDist Nα intraBond interDist u v =
      alphaClusterInvDist Nα intraBond interDist v u := by
  unfold alphaClusterInvDist
  by_cases huv : u = v
  · subst huv; rfl
  · have hvu : v ≠ u := Ne.symm huv
    by_cases hc : u.1 = v.1
    · have hc' : v.1 = u.1 := hc.symm
      rw [if_neg huv, if_neg hvu, if_pos hc, if_pos hc']
    · have hc' : v.1 ≠ u.1 := Ne.symm hc
      rw [if_neg huv, if_neg hvu, if_neg hc, if_neg hc']

/-- **Exact $N_\alpha$-Cluster Discrete Electrostatic Sum Evaluation**:
For any $N_\alpha$-cluster nucleus `Fin Nα × Fin 4` in which each $\alpha$-tetrahedron has
balanced `(2p, 2n)` proton occupancy (`∀ c : Fin Nα, (Finset.univ.filter (fun i => isProton (c, i) = true)).card = 2`),
evaluating `discreteCoulombEnergy` over all $(4 N_\alpha)^2$ vertex pairs yields identically:
$$E_C^{\mathrm{disc}} = \alpha\hbar c \left(\frac{N_\alpha}{\ell_{\mathrm{intra}}}
  + \frac{4 \binom{N_\alpha}{2}}{d_{\mathrm{inter}}}\right).$$ -/
theorem discreteCoulomb_equilateral_alphaCluster_eval
    (Nα : ℕ) (alphaHbarC intraBond interDist : ℝ)
    (isProton : Fin Nα × Fin 4 → Bool)
    (hBal : ∀ c : Fin Nα,
      (Finset.univ.filter (fun i : Fin 4 => isProton (c, i) = true)).card = 2) :
    discreteCoulombEnergy alphaHbarC (alphaClusterInvDist Nα intraBond interDist) isProton =
      alphaHbarC * ((Nα : ℝ) / intraBond + (4 * Nα.choose 2 : ℝ) / interDist) := by
  have hslice_sum : ∀ c : Fin Nα,
      (∑ i : Fin 4, protonIndicator isProton (c, i)) = 2 := by
    intro c
    have hs := sum_protonIndicator_eq_protonCount (fun i : Fin 4 => isProton (c, i))
    unfold protonCount protonFinset at hs
    change (∑ i : Fin 4, protonIndicator (fun i : Fin 4 => isProton (c, i)) i) = 2
    rw [hs, hBal c]
    norm_num
  have hintra_c : ∀ c : Fin Nα,
      (∑ i : Fin 4, ∑ j : Fin 4,
        protonIndicator isProton (c, i) * protonIndicator isProton (c, j) *
          alphaClusterInvDist Nα intraBond interDist (c, i) (c, j)) =
      2 / intraBond := by
    intro c
    have hker : ∀ i j : Fin 4,
        alphaClusterInvDist Nα intraBond interDist (c, i) (c, j) =
          uniformBondInvDist intraBond i j := by
      intro i j
      unfold alphaClusterInvDist uniformBondInvDist
      by_cases hij : i = j
      · subst hij; simp
      · have hne : (c, i) ≠ (c, j) := fun h => hij (Prod.mk.inj h).2
        simp [hij, hne]
    simp only [hker]
    change discreteCoulombPairSum (uniformBondInvDist intraBond) (fun i => isProton (c, i)) =
      2 / intraBond
    rw [discreteCoulombPairSum_eq_offDiag_sum (uniformBondInvDist intraBond)
      (uniformBondInvDist_diag intraBond)]
    have hconst :
        ∀ x ∈ (protonFinset (fun i : Fin 4 => isProton (c, i))).offDiag,
          uniformBondInvDist intraBond x.1 x.2 = 1 / intraBond := by
      intro x hx
      have hne : x.1 ≠ x.2 := (Finset.mem_offDiag.mp hx).2.2
      simp [uniformBondInvDist, hne]
    rw [Finset.sum_congr rfl hconst, Finset.sum_const, nsmul_eq_mul,
      offDiag_card_eq_two_mul_choose]
    unfold protonFinset
    rw [hBal c]
    norm_num
    ring
  have hinter_c : ∀ c₁ c₂ : Fin Nα, c₁ ≠ c₂ →
      (∑ i : Fin 4, ∑ j : Fin 4,
        protonIndicator isProton (c₁, i) * protonIndicator isProton (c₂, j) *
          alphaClusterInvDist Nα intraBond interDist (c₁, i) (c₂, j)) =
      4 / interDist := by
    intro c₁ c₂ hne
    have hker : ∀ i j : Fin 4,
        alphaClusterInvDist Nα intraBond interDist (c₁, i) (c₂, j) = 1 / interDist := by
      intro i j
      unfold alphaClusterInvDist
      have hpne : (c₁, i) ≠ (c₂, j) := fun h => hne (Prod.mk.inj h).1
      rw [if_neg hpne, if_neg hne]
    simp only [hker]
    have hinner : ∀ i : Fin 4,
        (∑ j : Fin 4,
          protonIndicator isProton (c₁, i) * protonIndicator isProton (c₂, j) * (1 / interDist)) =
        protonIndicator isProton (c₁, i) *
          ((∑ j : Fin 4, protonIndicator isProton (c₂, j)) * (1 / interDist)) := by
      intro i
      rw [Finset.sum_mul, Finset.mul_sum]
      refine Finset.sum_congr rfl ?_
      intro j _
      ring
    simp only [hinner, ← Finset.sum_mul]
    rw [hslice_sum c₁, hslice_sum c₂]
    ring
  unfold discreteCoulombEnergy discreteCoulombPairSum
  rw [Fintype.sum_prod_type]
  have houter :
      (∑ c₁ : Fin Nα, ∑ i : Fin 4, ∑ v : Fin Nα × Fin 4,
        protonIndicator isProton (c₁, i) * protonIndicator isProton v *
          alphaClusterInvDist Nα intraBond interDist (c₁, i) v) =
      ∑ c₁ : Fin Nα, ∑ c₂ : Fin Nα, ∑ i : Fin 4, ∑ j : Fin 4,
        protonIndicator isProton (c₁, i) * protonIndicator isProton (c₂, j) *
          alphaClusterInvDist Nα intraBond interDist (c₁, i) (c₂, j) := by
    refine Finset.sum_congr rfl ?_
    intro c₁ _
    simp only [Fintype.sum_prod_type]
    rw [Finset.sum_comm]
  rw [houter]
  have hrow : ∀ c₁ : Fin Nα,
      (∑ c₂ : Fin Nα, ∑ i : Fin 4, ∑ j : Fin 4,
        protonIndicator isProton (c₁, i) * protonIndicator isProton (c₂, j) *
          alphaClusterInvDist Nα intraBond interDist (c₁, i) (c₂, j)) =
      (2 / intraBond) + (((Nα - 1 : ℕ) : ℝ) * (4 / interDist)) := by
    intro c₁
    rw [← Finset.add_sum_erase Finset.univ _ (Finset.mem_univ c₁), hintra_c c₁]
    congr 1
    have herase :
        ∀ c₂ ∈ Finset.univ.erase c₁,
          (∑ i : Fin 4, ∑ j : Fin 4,
            protonIndicator isProton (c₁, i) * protonIndicator isProton (c₂, j) *
              alphaClusterInvDist Nα intraBond interDist (c₁, i) (c₂, j)) =
          4 / interDist := by
      intro c₂ hc₂
      exact hinter_c c₁ c₂ (Ne.symm (Finset.ne_of_mem_erase hc₂))
    rw [Finset.sum_congr rfl herase, Finset.sum_const,
      Finset.card_erase_of_mem (Finset.mem_univ c₁), Finset.card_univ, Fintype.card_fin,
      nsmul_eq_mul]
  simp only [hrow, Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
  have hprod_nat : (Nα : ℝ) * ((Nα - 1 : ℕ) : ℝ) = 2 * (Nα.choose 2 : ℝ) := by
    have hnat := (two_mul_choose_two_nat Nα).symm
    exact_mod_cast hnat
  calc
    alphaHbarC / 2 * ((Nα : ℝ) * (2 / intraBond + ((Nα - 1 : ℕ) : ℝ) * (4 / interDist)))
      = alphaHbarC * ((Nα : ℝ) / intraBond +
          ((Nα : ℝ) * ((Nα - 1 : ℕ) : ℝ)) * (2 / interDist)) := by ring
    _ = alphaHbarC * ((Nα : ℝ) / intraBond + (2 * (Nα.choose 2 : ℝ)) * (2 / interDist)) := by
      rw [hprod_nat]
    _ = alphaHbarC * ((Nα : ℝ) / intraBond + (4 * Nα.choose 2 : ℝ) / interDist) := by
      ring

/-- **Carbon-12 ($3 \times K_4$, `Fin 3 × Fin 4`) Equilateral 3-$\alpha$ Electrostatic Formula**:
For any balanced `(2p, 2n)` occupancy on each of the $3$ $\alpha$-tetrahedra of $^{12}\mathrm{C}$,
$$E_C^{\mathrm{disc}}(^{12}\mathrm{C})
  = \alpha\hbar c \left(\frac{3}{\ell_{\mathrm{intra}}} + \frac{12}{d_{\mathrm{inter}}}\right).$$ -/
theorem carbon12_equilateral_three_alpha_coulomb
    (alphaHbarC intraBond interDist : ℝ)
    (isProton : Fin 3 × Fin 4 → Bool)
    (hBal : ∀ c : Fin 3,
      (Finset.univ.filter (fun i : Fin 4 => isProton (c, i) = true)).card = 2) :
    discreteCoulombEnergy alphaHbarC (alphaClusterInvDist 3 intraBond interDist) isProton =
      alphaHbarC * (3 / intraBond + 12 / interDist) := by
  rw [discreteCoulomb_equilateral_alphaCluster_eval 3 alphaHbarC intraBond interDist isProton hBal]
  have hc : (3 : ℕ).choose 2 = 3 := by decide
  rw [hc]
  norm_num

-- ============================================================================
-- § 5. 3D FCC/HCP Close-Packing Voronoi Volume & Packing Radius Transport
-- ============================================================================

/-- Conventional FCC cubic unit-cell edge $a_{\mathrm{FCC}} = \sqrt{2}\,\ell_{\mathrm{bond}}$
for nearest-neighbor bond spacing $\ell_{\mathrm{bond}}$. -/
noncomputable def fccCubicEdge (bondLen : ℝ) : ℝ :=
  Real.sqrt 2 * bondLen

/-- Volume $V_{\mathrm{cell}} = \ell_{\mathrm{bond}}^3 / \sqrt{2}$ of each interior Voronoi
(rhombic-dodecahedral) cell in 3D FCC / HCP close packing. -/
noncomputable def fccVoronoiCellVolume (bondLen : ℝ) : ℝ :=
  bondLen ^ 3 / Real.sqrt 2

/-- Dimensionless 3D FCC/HCP close-packing radius constant
$$c_{\mathrm{FCC}} = \left(\frac{3}{4\pi\sqrt{2}}\right)^{1/3} \approx 0.5526695.$$ -/
noncomputable def fccPackingConst : ℝ :=
  (3 / (4 * Real.pi * Real.sqrt 2)) ^ ((1 : ℝ) / 3)

/-- Euclidean equivalent packing radius $R_{\mathrm{FCC}}(\ell_{\mathrm{bond}}, A)$ of $A$
close-packed nucleons of nearest-neighbor bond spacing $\ell_{\mathrm{bond}}$:
$$R_{\mathrm{FCC}}(\ell_{\mathrm{bond}}, A)
  = \left(\frac{3}{4\pi\sqrt{2}}\right)^{1/3} \ell_{\mathrm{bond}}\,A^{1/3}.$$ -/
noncomputable def fccPackingRadius (bondLen : ℝ) (A : ℕ) : ℝ :=
  fccPackingConst * bondLen * (A : ℝ) ^ ((1 : ℝ) / 3)

/-- Nearest-neighbor vector $(a_{\mathrm{FCC}}/2, a_{\mathrm{FCC}}/2, 0)$ in the conventional FCC
cube has squared Euclidean length $\ell_{\mathrm{bond}}^2$. -/
theorem fcc_nearest_neighbor_norm_sq (bondLen : ℝ) :
    (fccCubicEdge bondLen / 2) ^ 2 + (fccCubicEdge bondLen / 2) ^ 2 + (0 : ℝ) ^ 2 =
      bondLen ^ 2 := by
  unfold fccCubicEdge
  have hs2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  calc
    (Real.sqrt 2 * bondLen / 2) ^ 2 + (Real.sqrt 2 * bondLen / 2) ^ 2 + 0 ^ 2
      = (Real.sqrt 2 ^ 2) * bondLen ^ 2 / 2 := by ring
    _ = bondLen ^ 2 := by rw [hs2]; ring

/-- Dividing the conventional FCC cube volume $a_{\mathrm{FCC}}^3 = (\sqrt{2}\,\ell_{\mathrm{bond}})^3$
among its $4$ lattice sites yields the Voronoi cell volume $\ell_{\mathrm{bond}}^3 / \sqrt{2}$. -/
theorem fcc_voronoi_volume_from_conventional_cube (bondLen : ℝ) :
    (fccCubicEdge bondLen) ^ 3 / 4 = fccVoronoiCellVolume bondLen := by
  unfold fccCubicEdge fccVoronoiCellVolume
  have hs2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have hs4 : Real.sqrt 2 ^ 4 = 4 := by
    calc
      Real.sqrt 2 ^ 4 = (Real.sqrt 2 ^ 2) ^ 2 := by ring
      _ = 4 := by rw [hs2]; norm_num
  have hsne : Real.sqrt 2 ≠ 0 := ne_of_gt (Real.sqrt_pos.mpr (by norm_num))
  field_simp [hsne]
  rw [hs4]
  ring

/-- **3D Close-Packing Sphere Fraction Identity**:
Touching spheres of radius $\ell_{\mathrm{bond}} / 2$ occupy fraction
$\eta_{\mathrm{FCC}} = \frac{\pi \sqrt{2}}{6}$ of each Voronoi cell ($\eta_{\mathrm{FCC}}^2 = \pi^2 / 18$). -/
theorem fcc_sphere_packing_fraction_eq (bondLen : ℝ) (hb : bondLen ≠ 0) :
    ((4 / 3) * Real.pi * (bondLen / 2) ^ 3) / fccVoronoiCellVolume bondLen =
      Real.pi * Real.sqrt 2 / 6 ∧
    (((4 / 3) * Real.pi * (bondLen / 2) ^ 3) / fccVoronoiCellVolume bondLen) ^ 2 =
      Real.pi ^ 2 / 18 := by
  unfold fccVoronoiCellVolume
  have hsne : Real.sqrt 2 ≠ 0 := ne_of_gt (Real.sqrt_pos.mpr (by norm_num))
  have hs2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have h1 :
      ((4 / 3) * Real.pi * (bondLen / 2) ^ 3) / (bondLen ^ 3 / Real.sqrt 2) =
        Real.pi * Real.sqrt 2 / 6 := by
    field_simp [hb, hsne]
    ring
  refine ⟨h1, ?_⟩
  rw [h1]
  calc
    (Real.pi * Real.sqrt 2 / 6) ^ 2 = Real.pi ^ 2 * (Real.sqrt 2 ^ 2) / 36 := by ring
    _ = Real.pi ^ 2 / 18 := by rw [hs2]; ring

/-- Cube of `fccPackingConst` equals $3 / (4 \pi \sqrt{2})$. -/
theorem fccPackingConst_pow_three :
    fccPackingConst ^ 3 = 3 / (4 * Real.pi * Real.sqrt 2) := by
  unfold fccPackingConst
  have hbase : 0 ≤ 3 / (4 * Real.pi * Real.sqrt 2) := by
    apply div_nonneg (by norm_num)
    exact mul_nonneg (mul_nonneg (by norm_num) (le_of_lt Real.pi_pos)) (Real.sqrt_nonneg 2)
  rw [← Real.rpow_natCast _ 3, ← Real.rpow_mul hbase]
  norm_num

/-- **3D FCC Volume Balance Identity**:
For every `bondLen` and every nucleon count `A : ℕ`, the Euclidean ball of radius
`fccPackingRadius bondLen A` has exact volume $A \cdot V_{\mathrm{cell}}$:
$$\frac{4}{3} \pi R_{\mathrm{FCC}}(\ell_{\mathrm{bond}}, A)^3
  = A \cdot \frac{\ell_{\mathrm{bond}}^3}{\sqrt{2}}.$$ -/
theorem fcc_packing_radius_cubed_volume_conservation (bondLen : ℝ) (A : ℕ) :
    (4 / 3) * Real.pi * (fccPackingRadius bondLen A) ^ 3 =
      (A : ℝ) * fccVoronoiCellVolume bondLen := by
  unfold fccPackingRadius fccVoronoiCellVolume
  have hpi : Real.pi ≠ 0 := ne_of_gt Real.pi_pos
  have hsne : Real.sqrt 2 ≠ 0 := ne_of_gt (Real.sqrt_pos.mpr (by norm_num))
  calc
    (4 / 3) * Real.pi * (fccPackingConst * bondLen * (A : ℝ) ^ ((1 : ℝ) / 3)) ^ 3
      = (4 / 3) * Real.pi * fccPackingConst ^ 3 * bondLen ^ 3 *
          (((A : ℝ) ^ ((1 : ℝ) / 3)) ^ 3) := by ring
    _ = (4 / 3) * Real.pi * (3 / (4 * Real.pi * Real.sqrt 2)) * bondLen ^ 3 * (A : ℝ) := by
      rw [fccPackingConst_pow_three, natCast_rpow_one_third_pow_three]
    _ = (A : ℝ) * (bondLen ^ 3 / Real.sqrt 2) := by
      field_simp [hpi, hsne]

/-- **Exact Sixth-Power Polynomial Identity for the 3D FCC Packing Radius**:
For every `bondLen : ℝ` and every mass number `A : ℕ`,
$$(4\pi)^2 \cdot 2 \cdot R_{\mathrm{FCC}}(\ell_{\mathrm{bond}}, A)^6
  = 9\,\ell_{\mathrm{bond}}^6\,A^2.$$ -/
theorem fcc_packing_radius_sixth_power_identity (bondLen : ℝ) (A : ℕ) :
    (4 * Real.pi) ^ 2 * 2 * (fccPackingRadius bondLen A) ^ 6 =
      9 * bondLen ^ 6 * (A : ℝ) ^ 2 := by
  have hvol := fcc_packing_radius_cubed_volume_conservation bondLen A
  unfold fccVoronoiCellVolume at hvol
  have hsne : Real.sqrt 2 ≠ 0 := ne_of_gt (Real.sqrt_pos.mpr (by norm_num))
  have hs2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have hlin :
      4 * Real.pi * Real.sqrt 2 * (fccPackingRadius bondLen A) ^ 3 =
        3 * bondLen ^ 3 * (A : ℝ) := by
    have hmul := congrArg (fun x => 3 * Real.sqrt 2 * x) hvol
    dsimp at hmul
    field_simp [hsne] at hmul
    linarith
  have hsq := congrArg (fun x => x ^ 2) hlin
  dsimp at hsq
  calc
    (4 * Real.pi) ^ 2 * 2 * (fccPackingRadius bondLen A) ^ 6
      = (4 * Real.pi) ^ 2 * (Real.sqrt 2 ^ 2) * (fccPackingRadius bondLen A) ^ 6 := by
        rw [hs2]
    _ = (4 * Real.pi * Real.sqrt 2 * (fccPackingRadius bondLen A) ^ 3) ^ 2 := by ring
    _ = (3 * bondLen ^ 3 * (A : ℝ)) ^ 2 := hsq
    _ = 9 * bondLen ^ 6 * (A : ℝ) ^ 2 := by ring

/-- Algebraic sixth-power corollary from any radius `R` satisfying volume conservation
$\frac{4}{3}\pi R^3 = A \cdot (\ell_{\mathrm{bond}}^3 / \sqrt{2})$. -/
theorem fcc_sixth_power_of_volume_balance {R bondLen : ℝ} {A : ℕ}
    (hvol : (4 / 3) * Real.pi * R ^ 3 = (A : ℝ) * (bondLen ^ 3 / Real.sqrt 2)) :
    (4 * Real.pi) ^ 2 * 2 * R ^ 6 = 9 * bondLen ^ 6 * (A : ℝ) ^ 2 := by
  have hsne : Real.sqrt 2 ≠ 0 := ne_of_gt (Real.sqrt_pos.mpr (by norm_num))
  have hs2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have hlin : 4 * Real.pi * Real.sqrt 2 * R ^ 3 = 3 * bondLen ^ 3 * (A : ℝ) := by
    have hmul := congrArg (fun x => 3 * Real.sqrt 2 * x) hvol
    dsimp at hmul
    field_simp [hsne] at hmul
    linarith
  have hsq := congrArg (fun x => x ^ 2) hlin
  dsimp at hsq
  calc
    (4 * Real.pi) ^ 2 * 2 * R ^ 6
      = (4 * Real.pi * Real.sqrt 2 * R ^ 3) ^ 2 := by
        calc
          (4 * Real.pi) ^ 2 * 2 * R ^ 6 = (4 * Real.pi) ^ 2 * (Real.sqrt 2 ^ 2) * R ^ 6 := by
            rw [hs2]
          _ = (4 * Real.pi * Real.sqrt 2 * R ^ 3) ^ 2 := by ring
    _ = (3 * bondLen ^ 3 * (A : ℝ)) ^ 2 := hsq
    _ = 9 * bondLen ^ 6 * (A : ℝ) ^ 2 := by ring

/-- **Strict Numerical Enclosure of the Dimensionless FCC Packing Constant**:
$$0.55 = \frac{11}{20} < c_{\mathrm{FCC}} = \left(\frac{3}{4\pi\sqrt{2}}\right)^{1/3} < \frac{14}{25} = 0.56.$$ -/
theorem fccPackingConst_bounds :
    (11 / 20 : ℝ) < fccPackingConst ∧ fccPackingConst < (14 / 25 : ℝ) := by
  have hc_pos : 0 < fccPackingConst := by
    unfold fccPackingConst
    apply Real.rpow_pos_of_pos
    apply div_pos (by norm_num)
    exact mul_pos (mul_pos (by norm_num) Real.pi_pos) (Real.sqrt_pos.mpr (by norm_num))
  have hc6 : (4 * Real.pi) ^ 2 * 2 * fccPackingConst ^ 6 = 9 := by
    have h1 := fcc_packing_radius_sixth_power_identity 1 1
    unfold fccPackingRadius at h1
    norm_num at h1
    linarith
  have hpi_lo : (3.1415 : ℝ) < Real.pi := Real.pi_gt_d4
  have hpi_hi : Real.pi < (3.1416 : ℝ) := Real.pi_lt_d4
  have hpi_pos : 0 < Real.pi := Real.pi_pos
  have hlo6 : (11 / 20 : ℝ) ^ 6 < fccPackingConst ^ 6 := by
    have hprod : (4 * Real.pi) ^ 2 * 2 * (11 / 20 : ℝ) ^ 6 < 9 := by
      have hsq : Real.pi ^ 2 < (3.1416 : ℝ) ^ 2 := by nlinarith
      nlinarith
    have hfac_pos : 0 < (4 * Real.pi) ^ 2 * 2 := by positivity
    nlinarith
  have hhi6 : fccPackingConst ^ 6 < (14 / 25 : ℝ) ^ 6 := by
    have hprod : 9 < (4 * Real.pi) ^ 2 * 2 * (14 / 25 : ℝ) ^ 6 := by
      have hsq : (3.1415 : ℝ) ^ 2 < Real.pi ^ 2 := by nlinarith
      nlinarith
    have hfac_pos : 0 < (4 * Real.pi) ^ 2 * 2 := by positivity
    nlinarith
  refine ⟨?_, ?_⟩
  · by_contra hle
    push_neg at hle
    have hp : fccPackingConst ^ 6 ≤ (11 / 20 : ℝ) ^ 6 :=
      pow_le_pow_left₀ (le_of_lt hc_pos) hle 6
    linarith
  · by_contra hge
    push_neg at hge
    have hp : (14 / 25 : ℝ) ^ 6 ≤ fccPackingConst ^ 6 :=
      pow_le_pow_left₀ (by norm_num) hge 6
    linarith

end QOU.Nuclear.SimplicialCoulombGraphMetricDerivation
