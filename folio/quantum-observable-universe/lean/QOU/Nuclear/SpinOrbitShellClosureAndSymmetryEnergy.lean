import Mathlib.Tactic
import QOU.Nuclear.AlphaSimplexCoordinationDerivation

/-!
# Higher-$\ell$ Spin–Orbit Pauli Fiber ($2j+1$), Mayer–Jensen Magic Closures, and Quadratic Pauli Symmetry Energy

This module extends the $\ell = 0$ 4-state nucleon spin-isospin Pauli fiber
`SpinIsospinState := Fin 2 × Fin 2` (`QOU.Nuclear.AlphaSimplexCoordinationDerivation`)
to the graded higher-$\ell$ orbital–spin–isospin shell tower, deriving the single-species
spin–orbit subshell capacities $2j + 1$, the 3D isotropic harmonic-oscillator shell
degeneracies $(N+1)(N+2)$ and cumulative closures $\frac{(K+1)(K+2)(K+3)}{3}$, the
Carbon-12 $1p_{3/2}$ subshell closure at $Z = N = 6$, the universal Mayer–Jensen magic
number closed form
$$M_K = \frac{(K+1)(K+2)(K+3)}{3} + (2K + 4) \in \{28, 50, 82, 126, 184\} \quad (K \in \{2, 3, 4, 5, 6\}),$$
and the discrete Pauli Fermi-asymmetry quadratic promotion law $\propto (N - Z)^2$.

## Main Results

1. **Section 1 — Graded Orbital–Spin–Isospin Pauli Fiber & Subshell Multiplicities ($2j+1$)**:
   - For each orbital angular momentum quantum number $\ell \in \mathbb{N}$, the spin-aligned
     subshell $j = \ell + \tfrac{1}{2}$ has single-species magnetic degeneracy
     `degPlus ℓ = 2 * ℓ + 2`, and the spin-antialigned subshell ($\ell \ge 1$,
     $j = \ell - \tfrac{1}{2}$) has single-species magnetic degeneracy `degMinus ℓ = 2 * ℓ`.
   - Proves exact finite-type cardinalities via `SpinAlignedSubshellState ℓ := Fin (2 * ℓ + 2)`
     and `SpinAntialignedSubshellState ℓ := Fin (2 * ℓ)`, the single-species orbital sum
     `degPlus ℓ + degMinus ℓ = 2 * (2 * ℓ + 1)` (`degPlus_add_degMinus`), the total
     4-component spin-isospin orbital shell capacity `totalOrbitalSpinIsospinCap ℓ = 4 * (2 * ℓ + 1)`
     (`totalOrbitalSpinIsospinCap_eq`), and the spin–orbit subshell splitting difference
     `degPlus ℓ - degMinus ℓ = 2` (`degPlus_sub_degMinus`).
   - Proves Pauli subshell clique bounds: any single-species nucleon configuration occupying
     the $j = \ell + \tfrac{1}{2}$ subshell has cardinality at most $2\ell + 2$
     (`pauli_spinAligned_subshell_card_le`), and any two-species ($p, n$) configuration
     occupying $j = \ell + \tfrac{1}{2}$ has cardinality at most $4\ell + 4$
     (`pauli_twoSpecies_spinAligned_card_le`).

2. **Section 2 — 3D Isotropic Harmonic-Oscillator Shell Degeneracies & Cumulative Closures**:
   - The $N$-th 3D harmonic-oscillator major shell ($N = 2n_r + \ell$) has single-species
     degeneracy `oscShellDeg N = (N + 1) * (N + 2)`.
   - Proves the exact closed-form tetrahedral summation identity (`sum_oscShellDeg_mul_three`
     and `cumOscClosure_eq_sum`):
     $$3 \sum_{N=0}^{K} (N + 1)(N + 2) = (K + 1)(K + 2)(K + 3), \qquad
       \mathrm{cumOscClosure}(K) = \frac{(K + 1)(K + 2)(K + 3)}{3}.$$
   - Evaluates the harmonic-oscillator cumulative closures at $K = 0, 1, 2, 3, 4, 5, 6$ to
     $(2, 8, 20, 40, 70, 112, 168)$ (`cumOscClosure_values`).

3. **Section 3 — Carbon-12 ($Z = N = 6$) Subshell Closure & Universal Mayer–Jensen Magic Numbers**:
   - **Carbon-12 Subshell Closure (`carbon12_subshell_closure` & `oxygen16_full_p_shell_closure`)**:
     Filling the $N = 0$ ($1s_{1/2}$) shell (`oscShellDeg 0 = 2`) together with the spin-aligned
     $1p_{3/2}$ subshell (`degPlus 1 = 4`) closes identically at
     `oscShellDeg 0 + degPlus 1 = 6` per species ($Z = N = 6$, $A = 12$, $^{12}\mathrm{C}$),
     before the spin-antialigned $1p_{1/2}$ partner (`degMinus 1 = 2`) completes the $N = 1$
     major shell at $2 + 4 + 2 = 8$ per species ($Z = N = 8$, $A = 16$, $^{16}\mathrm{O}$).
   - **Universal Mayer–Jensen Intruder Magic Number Formula (`mayerJensenMagic_values` &
     `mayerJensen_step_decomposition`)**:
     For every major shell index $K \ge 2$, spin–orbit coupling depresses the maximum-$j$
     intruder subshell ($\ell = K + 1$, $j = K + \tfrac{3}{2}$, degeneracy
     `degPlus (K + 1) = 2 * K + 4`) from oscillator shell $K + 1$ into major shell $K$,
     yielding the exact closed-form magic sequence:
     $$M_K = \mathrm{cumOscClosure}(K) + \mathrm{degPlus}(K + 1)
           = \frac{(K + 1)(K + 2)(K + 3)}{3} + (2K + 4),$$
     which evaluates at $K = 2, 3, 4, 5, 6$ to $(28, 50, 82, 126, 184)$ and satisfies the
     exact shell-gap recurrence $M_{K+1} - M_K = \mathrm{oscShellDeg}(K+1) + 2 = (K+2)(K+3) + 2$,
     explaining the Doubly-Magic closures of $^{40}\mathrm{Ca}$ ($20, 20$),
     $^{48}\mathrm{Ca}$ ($20, 28$), $^{56}\mathrm{Ni}$ ($28, 28$),
     $^{100}\mathrm{Sn}$ / $^{132}\mathrm{Sn}$ ($Z = 50$, $N \in \{50, 82\}$), and
     $^{208}\mathrm{Pb}$ ($Z = 82, N = 126$).

4. **Section 4 — Discrete Pauli Fermi-Asymmetry Quadratic Promotion Law $\propto (N - Z)^2$**:
   - Proves that for any non-decreasing single-particle level sequence $\varepsilon : \mathbb{N} \to R$
     over a linearly ordered commutative ring $R$, the cumulative Fermi filling energy
     `fermiFillEnergy ε M = ∑_{i < M} ε(i)` satisfies the discrete convexity (promotion)
     inequality (`fermi_asymmetry_promotion_nonneg`): for any balanced core $M$ and neutron-proton
     half-excess $d$ ($Z = M - d$, $N = M + d$, $A = 2M$, $N - Z = 2d$),
     $$\mathrm{fermiFillEnergy}(\varepsilon, M + d) + \mathrm{fermiFillEnergy}(\varepsilon, M - d)
       - 2\,\mathrm{fermiFillEnergy}(\varepsilon, M)
       = \sum_{k=0}^{d-1} \bigl(\varepsilon(M + k) - \varepsilon(M - d + k)\bigr) \ge 0,$$
     vanishing at $d = 0$ ($Z = N$).
   - Proves that under a uniform local level spacing $\Delta\varepsilon > 0$ (or inverse Fermi
     level density $1/g(E_F) = \hbar\omega_q / g_{\mathrm{shell}}$), each promotion step across
     offset $d$ shifts by $\varepsilon(M + k) - \varepsilon(M - d + k) = d \cdot \Delta\varepsilon$,
     yielding the exact quadratic Pauli symmetry energy (`quadratic_pauli_symmetry_energy_exact`
     and `quadratic_pauli_symmetry_in_N_sub_Z`):
     $$E_{\mathrm{sym}}^{\mathrm{Pauli}}(Z, N)
       = d^2 \Delta\varepsilon = \frac{(N - Z)^2}{4}\,\Delta\varepsilon
       = \frac{\hbar\omega_q}{4 g_{\mathrm{shell}}}(N - Z)^2.$$
-/

namespace QOU.Nuclear.SpinOrbitShellClosureAndSymmetryEnergy

open Finset

-- ============================================================================
-- § 1. Graded Orbital–Spin–Isospin Pauli Fiber & Subshell Multiplicities (2j+1)
-- ============================================================================

/-- Single-species magnetic degeneracy $2j + 1 = 2\ell + 2$ of the spin-aligned
subshell $j = \ell + \tfrac{1}{2}$ for orbital angular momentum $\ell \in \mathbb{N}$. -/
def degPlus (ℓ : ℕ) : ℕ := 2 * ℓ + 2

/-- Single-species magnetic degeneracy $2j + 1 = 2\ell$ of the spin-antialigned
subshell $j = \ell - \tfrac{1}{2}$ for orbital angular momentum $\ell \in \mathbb{N}$
(vanishing at $\ell = 0$, where only $j = \tfrac{1}{2}$ exists). -/
def degMinus (ℓ : ℕ) : ℕ := 2 * ℓ

/-- Single-species orbital shell capacity $2(2\ell + 1)$ summing both spin–orbit partners. -/
def singleSpeciesOrbitalCap (ℓ : ℕ) : ℕ := 2 * (2 * ℓ + 1)

/-- Full 4-component spin–isospin ($p/n \times \uparrow/\downarrow$) orbital shell capacity
$4(2\ell + 1)$ at orbital angular momentum $\ell$. -/
def totalOrbitalSpinIsospinCap (ℓ : ℕ) : ℕ := 4 * (2 * ℓ + 1)

/-- Finite state type of a single-species spin-aligned subshell $j = \ell + \tfrac{1}{2}$. -/
abbrev SpinAlignedSubshellState (ℓ : ℕ) : Type := Fin (degPlus ℓ)

/-- Finite state type of a single-species spin-antialigned subshell $j = \ell - \tfrac{1}{2}$. -/
abbrev SpinAntialignedSubshellState (ℓ : ℕ) : Type := Fin (degMinus ℓ)

/-- Finite state type of the two-species (isospin $\mathrm{Fin}\ 2 \times \text{magnetic } m_j$)
spin-aligned subshell $j = \ell + \tfrac{1}{2}$. -/
abbrev TwoSpeciesSpinAlignedState (ℓ : ℕ) : Type := Fin 2 × Fin (degPlus ℓ)

/-- At $\ell = 0$ ($s$-wave), `degPlus 0 = 2`, `degMinus 0 = 0`, and the two-species
$s_{1/2}$ fiber `TwoSpeciesSpinAlignedState 0 = Fin 2 × Fin 2` has exact cardinality $4$,
recovering `SpinIsospinState` from `AlphaSimplexCoordinationDerivation`. -/
theorem sWave_recover_four_state_pauli_fiber :
    degPlus 0 = 2 ∧ degMinus 0 = 0 ∧
    Fintype.card (TwoSpeciesSpinAlignedState 0) = 4 := by
  refine ⟨rfl, rfl, ?_⟩
  decide

/-- For every $\ell \in \mathbb{N}$, the spin-aligned and spin-antialigned subshell
degeneracies sum to the total single-species orbital capacity $2(2\ell + 1)$. -/
theorem degPlus_add_degMinus (ℓ : ℕ) :
    degPlus ℓ + degMinus ℓ = singleSpeciesOrbitalCap ℓ := by
  unfold degPlus degMinus singleSpeciesOrbitalCap
  omega

/-- For every $\ell \in \mathbb{N}$, the two-species spin–isospin capacity of orbital $\ell$
equals twice the single-species orbital capacity:
$2(\mathrm{degPlus}(\ell) + \mathrm{degMinus}(\ell)) = 4(2\ell + 1)$. -/
theorem totalOrbitalSpinIsospinCap_eq (ℓ : ℕ) :
    2 * (degPlus ℓ + degMinus ℓ) = totalOrbitalSpinIsospinCap ℓ := by
  unfold degPlus degMinus totalOrbitalSpinIsospinCap
  omega

/-- The magnetic multiplicity difference between the spin-aligned partner $j = \ell + \tfrac{1}{2}$
and the spin-antialigned partner $j = \ell - \tfrac{1}{2}$ is identically $2$ for every $\ell$. -/
theorem degPlus_sub_degMinus (ℓ : ℕ) :
    degPlus ℓ - degMinus ℓ = 2 := by
  unfold degPlus degMinus
  omega

/-- Concrete single-species spin-aligned subshell capacities $2j + 1 = 2\ell + 2$
for $s_{1/2}, p_{3/2}, d_{5/2}, f_{7/2}, g_{9/2}, h_{11/2}, i_{13/2}, j_{15/2}$
($\ell = 0, 1, 2, 3, 4, 5, 6, 7$). -/
theorem degPlus_spectroscopic_values :
    degPlus 0 = 2 ∧ degPlus 1 = 4 ∧ degPlus 2 = 6 ∧ degPlus 3 = 8 ∧
    degPlus 4 = 10 ∧ degPlus 5 = 12 ∧ degPlus 6 = 14 ∧ degPlus 7 = 16 := by
  decide

/-- **Pauli Exclusion Bound on a Single-Species Spin–Orbit Subshell ($j = \ell + 1/2$)**:
Any finite set $S$ of identical nucleons (all protons or all neutrons) occupying a common
radial–orbital spin-aligned subshell $(n_r, \ell, j = \ell + \tfrac{1}{2})$ must admit an
injective magnetic-state assignment `c : S → SpinAlignedSubshellState ℓ`, forcing
`|S| ≤ 2ℓ + 2`. -/
theorem pauli_spinAligned_subshell_card_le (ℓ : ℕ) {S : Type*} [Fintype S]
    (c : S → SpinAlignedSubshellState ℓ) (hc : Function.Injective c) :
    Fintype.card S ≤ 2 * ℓ + 2 := by
  have hle : Fintype.card S ≤ Fintype.card (SpinAlignedSubshellState ℓ) :=
    Fintype.card_le_of_injective c hc
  simpa [SpinAlignedSubshellState, degPlus] using hle

/-- **Pauli Exclusion Bound on a Two-Species Spin–Orbit Subshell ($j = \ell + 1/2$)**:
Any finite set $S$ of nucleons (protons and neutrons combined) occupying a common
radial–orbital spin-aligned subshell $(n_r, \ell, j = \ell + \tfrac{1}{2})$ must admit an
injective isospin–magnetic state assignment `c : S → TwoSpeciesSpinAlignedState ℓ`,
forcing `|S| ≤ 4ℓ + 4`. -/
theorem pauli_twoSpecies_spinAligned_card_le (ℓ : ℕ) {S : Type*} [Fintype S]
    (c : S → TwoSpeciesSpinAlignedState ℓ) (hc : Function.Injective c) :
    Fintype.card S ≤ 4 * ℓ + 4 := by
  have hle : Fintype.card S ≤ Fintype.card (TwoSpeciesSpinAlignedState ℓ) :=
    Fintype.card_le_of_injective c hc
  have hcard : Fintype.card (TwoSpeciesSpinAlignedState ℓ) = 4 * ℓ + 4 := by
    simp [TwoSpeciesSpinAlignedState, degPlus]
    omega
  omega

-- ============================================================================
-- § 2. 3D Isotropic Harmonic-Oscillator Shell Degeneracies & Cumulative Closures
-- ============================================================================

/-- Single-species degeneracy of the $N$-th 3D isotropic harmonic-oscillator major shell
($N = 2n_r + \ell \ge 0$), including spin $\tfrac{1}{2}$:
$$\mathrm{oscShellDeg}(N) = 2 \binom{N + 2}{2} = (N + 1)(N + 2).$$ -/
def oscShellDeg (N : ℕ) : ℕ := (N + 1) * (N + 2)

/-- Closed-form cumulative single-species nucleon count across harmonic-oscillator major
shells $0 \le N \le K$:
$$\mathrm{cumOscClosure}(K) = \frac{(K + 1)(K + 2)(K + 3)}{3}.$$ -/
def cumOscClosure (K : ℕ) : ℕ := (K + 1) * (K + 2) * (K + 3) / 3

/-- The $N$-th oscillator shell degeneracy equals twice the triangular number $\binom{N+2}{2}$. -/
theorem oscShellDeg_eq_two_mul_choose (N : ℕ) :
    oscShellDeg N = 2 * (N + 2).choose 2 := by
  unfold oscShellDeg
  rw [Nat.choose_two_right]
  have hsub : N + 2 - 1 = N + 1 := rfl
  rw [hsub]
  have hdiv : 2 ∣ (N + 2) * (N + 1) := by
    rcases Nat.even_or_odd (N + 1) with ⟨k, hk⟩ | ⟨k, hk⟩
    · refine ⟨(N + 2) * k, ?_⟩
      rw [hk]
      ring
    · refine ⟨(N + 1) * (k + 1), ?_⟩
      have hN2 : N + 2 = 2 * (k + 1) := by omega
      rw [hN2]
      ring
  have hmul : 2 * ((N + 2) * (N + 1) / 2) = (N + 2) * (N + 1) :=
    Nat.mul_div_cancel' hdiv
  rw [hmul, mul_comm]

/-- **Exact Tetrahedral Summation Identity for 3D Harmonic-Oscillator Shells**:
For every major shell cutoff $K \in \mathbb{N}$,
$$3 \sum_{N=0}^{K} (N + 1)(N + 2) = (K + 1)(K + 2)(K + 3).$$ -/
theorem sum_oscShellDeg_mul_three (K : ℕ) :
    3 * (∑ N ∈ range (K + 1), oscShellDeg N) = (K + 1) * (K + 2) * (K + 3) := by
  induction K with
  | zero =>
    simp [oscShellDeg]
  | succ k ih =>
    rw [sum_range_succ, mul_add, ih]
    unfold oscShellDeg
    ring

/-- The product $(K + 1)(K + 2)(K + 3)$ is divisible by $3$ for every $K \in \mathbb{N}$. -/
theorem three_dvd_cumOsc_numer (K : ℕ) :
    3 ∣ (K + 1) * (K + 2) * (K + 3) := by
  refine ⟨∑ N ∈ range (K + 1), oscShellDeg N, ?_⟩
  exact (sum_oscShellDeg_mul_three K).symm

/-- **Exact Cumulative Oscillator Closure Theorem**:
For every $K \in \mathbb{N}$, the cumulative single-species occupancy across major shells
$0 \le N \le K$ equals the closed form `cumOscClosure K = (K + 1)(K + 2)(K + 3) / 3`. -/
theorem cumOscClosure_eq_sum (K : ℕ) :
    cumOscClosure K = ∑ N ∈ range (K + 1), oscShellDeg N := by
  unfold cumOscClosure
  rw [← sum_oscShellDeg_mul_three K]
  exact Nat.mul_div_right _ (by decide)

/-- One-step recurrence for `cumOscClosure`: adding major shell $K + 1$ increments the
cumulative closure by `oscShellDeg (K + 1)`. -/
theorem cumOscClosure_succ (K : ℕ) :
    cumOscClosure (K + 1) = cumOscClosure K + oscShellDeg (K + 1) := by
  rw [cumOscClosure_eq_sum (K + 1), cumOscClosure_eq_sum K, sum_range_succ]

/-- Individual 3D harmonic-oscillator shell degeneracies for $N = 0, 1, 2, 3, 4, 5, 6$:
$(2, 6, 12, 20, 30, 42, 56)$. -/
theorem oscShellDeg_values :
    oscShellDeg 0 = 2 ∧ oscShellDeg 1 = 6 ∧ oscShellDeg 2 = 12 ∧
    oscShellDeg 3 = 20 ∧ oscShellDeg 4 = 30 ∧ oscShellDeg 5 = 42 ∧
    oscShellDeg 6 = 56 := by
  decide

/-- Cumulative 3D harmonic-oscillator closures for $K = 0, 1, 2, 3, 4, 5, 6$:
$(2, 8, 20, 40, 70, 112, 168)$.
Note that $K = 0, 1, 2$ yield the light magic numbers $\{2, 8, 20\}$, whereas for $K \ge 3$
the pure oscillator closures $\{40, 70, 112, 168\}$ are shifted to $\{28, 50, 82, 126, 184\}$
by the Mayer–Jensen spin–orbit intruder subshell. -/
theorem cumOscClosure_values :
    cumOscClosure 0 = 2 ∧ cumOscClosure 1 = 8 ∧ cumOscClosure 2 = 20 ∧
    cumOscClosure 3 = 40 ∧ cumOscClosure 4 = 70 ∧ cumOscClosure 5 = 112 ∧
    cumOscClosure 6 = 168 := by
  decide

-- ============================================================================
-- § 3. Carbon-12 (Z=N=6) Subshell Closure & Universal Mayer–Jensen Magic Numbers
-- ============================================================================

/-- **Decompositions of Major Shells $N = 1$ ($p$-shell) and $N = 2$ ($sd$-shell)**:
1. The $N = 1$ major shell (`oscShellDeg 1 = 6`) splits into the spin-aligned $1p_{3/2}$
   subshell (`degPlus 1 = 4`) and the spin-antialigned $1p_{1/2}$ subshell (`degMinus 1 = 2`).
2. The $N = 2$ major shell (`oscShellDeg 2 = 12`) splits into $1d_{5/2}$ (`degPlus 2 = 6`),
   $2s_{1/2}$ (`degPlus 0 = 2`), and $1d_{3/2}$ (`degMinus 2 = 4`). -/
theorem p_and_sd_shell_spin_orbit_splits :
    oscShellDeg 1 = degPlus 1 + degMinus 1 ∧
    oscShellDeg 2 = degPlus 2 + degPlus 0 + degMinus 2 := by
  decide

/-- **Carbon-12 ($Z = N = 6$) Spin–Orbit Subshell Closure & Oxygen-16 ($Z = N = 8$) Completion**:
1. Filling the $1s_{1/2}$ core (`oscShellDeg 0 = 2`) plus the lowered spin-aligned $1p_{3/2}$
   subshell (`degPlus 1 = 4`) closes at exact occupancy $2 + 4 = 6$ per species, yielding
   $Z = N = 6$, $A = 12$ ($^{12}\mathrm{C}$, the $3\alpha$ triangular/tetrahedral subshell closure).
2. Filling the spin-antialigned partner $1p_{1/2}$ (`degMinus 1 = 2`) completes the $N = 1$
   major shell at $6 + 2 = 8 = \mathrm{cumOscClosure}(1)$ per species, yielding the doubly-magic
   closure $Z = N = 8$, $A = 16$ ($^{16}\mathrm{O}$, $4\alpha$). -/
theorem carbon12_and_oxygen16_shell_closures :
    oscShellDeg 0 + degPlus 1 = 6 ∧
    2 * (oscShellDeg 0 + degPlus 1) = 12 ∧
    (oscShellDeg 0 + degPlus 1) + degMinus 1 = cumOscClosure 1 ∧
    cumOscClosure 1 = 8 ∧
    2 * cumOscClosure 1 = 16 := by
  decide

/-- **Silicon-28 ($Z = N = 14$) $1d_{5/2}$ Subshell Closure & Calcium-40 ($Z = N = 20$) Completion**:
1. Adding the lowered $1d_{5/2}$ subshell (`degPlus 2 = 6`) to the $^{16}\mathrm{O}$ core
   (`cumOscClosure 1 = 8`) yields the $Z = N = 14$ ($A = 28$, $^{28}\mathrm{Si}$) subshell closure.
2. Adding the remaining $2s_{1/2}$ (`degPlus 0 = 2`) and $1d_{3/2}$ (`degMinus 2 = 4`)
   subshells completes the $N = 2$ major shell at $14 + 2 + 4 = 20 = \mathrm{cumOscClosure}(2)$
   ($Z = N = 20$, $A = 40$, $^{40}\mathrm{Ca}$). -/
theorem silicon28_and_calcium40_shell_closures :
    cumOscClosure 1 + degPlus 2 = 14 ∧
    (cumOscClosure 1 + degPlus 2) + degPlus 0 + degMinus 2 = cumOscClosure 2 ∧
    cumOscClosure 2 = 20 ∧
    2 * cumOscClosure 2 = 40 := by
  decide

/-- **Universal Mayer–Jensen Spin–Orbit Intruder Magic Number Formula**:
For major shell index $K \ge 2$, the spin–orbit interaction depresses the stretched
($n_r = 0, \ell = K + 1, j = K + \tfrac{3}{2}$) intruder subshell of degeneracy
`degPlus (K + 1) = 2 * K + 4` from oscillator shell $K + 1$ down into oscillator shell $K$:
$$M_K = \mathrm{cumOscClosure}(K) + \mathrm{degPlus}(K + 1)
      = \frac{(K + 1)(K + 2)(K + 3)}{3} + (2K + 4).$$ -/
def mayerJensenMagic (K : ℕ) : ℕ :=
  cumOscClosure K + degPlus (K + 1)

/-- Explicit algebraic formula for `3 * mayerJensenMagic K`:
$$3 M_K = (K + 1)(K + 2)(K + 3) + 6(K + 2) = (K + 2)(K^2 + 4K + 9).$$ -/
theorem mayerJensenMagic_mul_three_closed_form (K : ℕ) :
    3 * mayerJensenMagic K = (K + 2) * (K ^ 2 + 4 * K + 9) := by
  unfold mayerJensenMagic degPlus
  rw [mul_add, cumOscClosure_eq_sum, sum_oscShellDeg_mul_three]
  ring

/-- **Exact Mayer–Jensen Magic Numbers $\{28, 50, 82, 126, 184\}$**:
Evaluating `mayerJensenMagic K` at $K = 2, 3, 4, 5, 6$ yields the exact empirical
spin–orbit nuclear magic numbers:
- $K = 2$ ($1f_{7/2}$ intruder, $\mathrm{degPlus}(3) = 8$): $20 + 8 = 28$ ($^{48}\mathrm{Ca}, ^{56}\mathrm{Ni}$),
- $K = 3$ ($1g_{9/2}$ intruder, $\mathrm{degPlus}(4) = 10$): $40 + 10 = 50$ ($^{100}\mathrm{Sn}, ^{120}\mathrm{Sn}, ^{132}\mathrm{Sn}$),
- $K = 4$ ($1h_{11/2}$ intruder, $\mathrm{degPlus}(5) = 12$): $70 + 12 = 82$ ($^{132}\mathrm{Sn}, ^{208}\mathrm{Pb}$),
- $K = 5$ ($1i_{13/2}$ intruder, $\mathrm{degPlus}(6) = 14$): $112 + 14 = 126$ ($^{208}\mathrm{Pb}$),
- $K = 6$ ($1j_{15/2}$ intruder, $\mathrm{degPlus}(7) = 16$): $168 + 16 = 184$ (superheavy neutron closure). -/
theorem mayerJensenMagic_values :
    mayerJensenMagic 2 = 28 ∧
    mayerJensenMagic 3 = 50 ∧
    mayerJensenMagic 4 = 82 ∧
    mayerJensenMagic 5 = 126 ∧
    mayerJensenMagic 6 = 184 := by
  decide

/-- **Exact Shell-to-Shell Step Decomposition of the Mayer–Jensen Magic Sequence**:
Between two consecutive spin–orbit magic closures $M_K$ and $M_{K+1}$, the occupied block
consists of the remaining states of oscillator shell $K + 1$ after its own intruder
`degPlus (K + 1)` was donated to $M_K$ (`oscShellDeg (K + 1) - degPlus (K + 1)`), together
with the new intruder `degPlus (K + 2)` from oscillator shell $K + 2$:
$$M_{K+1} - M_K = \bigl(\mathrm{oscShellDeg}(K+1) - \mathrm{degPlus}(K+1)\bigr) + \mathrm{degPlus}(K+2)
               = \mathrm{oscShellDeg}(K+1) + 2 = (K+2)(K+3) + 2.$$ -/
theorem mayerJensen_step_decomposition (K : ℕ) :
    degPlus (K + 1) ≤ oscShellDeg (K + 1) ∧
    mayerJensenMagic (K + 1) =
      mayerJensenMagic K + (oscShellDeg (K + 1) - degPlus (K + 1)) + degPlus (K + 2) ∧
    mayerJensenMagic (K + 1) - mayerJensenMagic K = oscShellDeg (K + 1) + 2 := by
  have hle : degPlus (K + 1) ≤ oscShellDeg (K + 1) := by
    unfold degPlus oscShellDeg
    nlinarith
  have hd : degPlus (K + 2) = degPlus (K + 1) + 2 := by
    unfold degPlus
    omega
  refine ⟨hle, ?_, ?_⟩
  · unfold mayerJensenMagic
    rw [cumOscClosure_succ K]
    change cumOscClosure K + oscShellDeg (K + 1) + degPlus (K + 2) =
      (cumOscClosure K + degPlus (K + 1)) + (oscShellDeg (K + 1) - degPlus (K + 1)) + degPlus (K + 2)
    omega
  · unfold mayerJensenMagic
    rw [cumOscClosure_succ K]
    change (cumOscClosure K + oscShellDeg (K + 1) + degPlus (K + 2)) -
      (cumOscClosure K + degPlus (K + 1)) = oscShellDeg (K + 1) + 2
    rw [hd]
    omega

/-- Complete unified nuclear magic number sequence combining the low-$\ell$ harmonic-oscillator
closures ($K = 0, 1, 2 \mapsto 2, 8, 20$), the $1p_{3/2}$ subshell closure ($6$), and the
Mayer–Jensen intruder closures ($K = 2, 3, 4, 5, 6 \mapsto 28, 50, 82, 126, 184$). -/
def unifiedNuclearMagicSeq : List ℕ :=
  [cumOscClosure 0, oscShellDeg 0 + degPlus 1, cumOscClosure 1, cumOscClosure 2,
   mayerJensenMagic 2, mayerJensenMagic 3, mayerJensenMagic 4, mayerJensenMagic 5,
   mayerJensenMagic 6]

/-- The unified magic and subshell sequence evaluates to `[2, 6, 8, 20, 28, 50, 82, 126, 184]`,
and its doubly-magic pairings recover $^{4}\mathrm{He}$ ($2+2=4$), $^{12}\mathrm{C}$ ($6+6=12$),
$^{16}\mathrm{O}$ ($8+8=16$), $^{40}\mathrm{Ca}$ ($20+20=40$), $^{48}\mathrm{Ca}$ ($20+28=48$),
$^{56}\mathrm{Ni}$ ($28+28=56$), $^{132}\mathrm{Sn}$ ($50+82=132$), and
$^{208}\mathrm{Pb}$ ($82+126=208$). -/
theorem unifiedNuclearMagicSeq_eq_and_doubly_magic_masses :
    unifiedNuclearMagicSeq = [2, 6, 8, 20, 28, 50, 82, 126, 184] ∧
    cumOscClosure 0 + cumOscClosure 0 = 4 ∧
    (oscShellDeg 0 + degPlus 1) + (oscShellDeg 0 + degPlus 1) = 12 ∧
    cumOscClosure 1 + cumOscClosure 1 = 16 ∧
    cumOscClosure 2 + cumOscClosure 2 = 40 ∧
    cumOscClosure 2 + mayerJensenMagic 2 = 48 ∧
    mayerJensenMagic 2 + mayerJensenMagic 2 = 56 ∧
    mayerJensenMagic 3 + mayerJensenMagic 4 = 132 ∧
    mayerJensenMagic 4 + mayerJensenMagic 5 = 208 := by
  decide

-- ============================================================================
-- § 4. Discrete Pauli Fermi-Asymmetry Quadratic Promotion Law ∝ (N - Z)²
-- ============================================================================

section PauliSymmetryEnergy

variable {R : Type*} [CommRing R]

/-- Cumulative single-species Fermi shell-filling kinetic/orbital energy for $M$ identical
nucleons occupying ordered single-particle levels $\varepsilon : \mathbb{N} \to R$:
$$\mathrm{fermiFillEnergy}(\varepsilon, M) = \sum_{i=0}^{M-1} \varepsilon(i).$$ -/
def fermiFillEnergy (ε : ℕ → R) (M : ℕ) : R :=
  ∑ i ∈ range M, ε i

/-- Discrete Pauli Fermi promotion penalty when shifting $d$ nucleons from proton states
$\{M - d, \dots, M - 1\}$ to neutron states $\{M, \dots, M + d - 1\}$ at fixed mass number
$A = 2M$ ($Z = M - d$, $N = M + d$, $N - Z = 2d$):
$$\Delta E_{\mathrm{Pauli}}(\varepsilon, M, d)
  = \mathrm{fermiFillEnergy}(\varepsilon, M + d) + \mathrm{fermiFillEnergy}(\varepsilon, M - d)
    - 2\,\mathrm{fermiFillEnergy}(\varepsilon, M).$$ -/
def pauliAsymmetryPenalty (ε : ℕ → R) (M d : ℕ) : R :=
  fermiFillEnergy ε (M + d) + fermiFillEnergy ε (M - d) - 2 * fermiFillEnergy ε M

/-- At balanced isospin $d = 0$ ($Z = N = M$), the Pauli Fermi-asymmetry penalty vanishes
identically for any single-particle spectrum $\varepsilon$. -/
theorem pauliAsymmetryPenalty_zero (ε : ℕ → R) (M : ℕ) :
    pauliAsymmetryPenalty ε M 0 = 0 := by
  unfold pauliAsymmetryPenalty
  simp
  ring

/-- **Exact Telescoping Sum Decomposition of the Discrete Pauli Asymmetry Penalty**:
For every balanced core occupancy $M$ and half-excess $d \le M$, transferring $d$ protons
into $d$ neutron orbitals above the Fermi surface $M$ yields the exact level-by-level
promotion sum:
$$\mathrm{pauliAsymmetryPenalty}(\varepsilon, M, d)
  = \sum_{k=0}^{d-1} \bigl(\varepsilon(M + k) - \varepsilon(M - d + k)\bigr).$$ -/
theorem pauliAsymmetryPenalty_eq_promotion_sum (ε : ℕ → R) {M d : ℕ} (hd : d ≤ M) :
    pauliAsymmetryPenalty ε M d =
      ∑ k ∈ range d, (ε (M + k) - ε (M - d + k)) := by
  unfold pauliAsymmetryPenalty fermiFillEnergy
  have h1 : ∑ i ∈ range (M + d), ε i =
      (∑ i ∈ range M, ε i) + ∑ k ∈ range d, ε (M + k) :=
    sum_range_add ε M d
  have hM : M = (M - d) + d := (Nat.sub_add_cancel hd).symm
  have h2 : ∑ i ∈ range M, ε i =
      (∑ i ∈ range (M - d), ε i) + ∑ k ∈ range d, ε (M - d + k) := by
    conv_lhs => rw [hM]
    exact sum_range_add ε (M - d) d
  rw [h1, h2, sum_sub_distrib]
  ring

/-- **Quadratic Pauli Fermi-Asymmetry Theorem under Uniform Level Spacing**:
When the single-particle spectrum has local level spacing $\Delta\varepsilon \in R$ across
the Fermi window ($\varepsilon(i) = \varepsilon_0 + i \cdot \Delta\varepsilon$), each promoted
pair at index $k \in \{0, \dots, d-1\}$ costs $\varepsilon(M + k) - \varepsilon(M - d + k) = d \cdot \Delta\varepsilon$,
so summing over the $d$ promoted nucleons produces the **exact quadratic law**:
$$\mathrm{pauliAsymmetryPenalty}(\varepsilon, M, d) = d^2 \cdot \Delta\varepsilon.$$ -/
theorem quadratic_pauli_symmetry_energy_exact (ε₀ Δε : R) {M d : ℕ} (hd : d ≤ M) :
    pauliAsymmetryPenalty (fun i => ε₀ + (i : R) * Δε) M d =
      (d : R) ^ 2 * Δε := by
  rw [pauliAsymmetryPenalty_eq_promotion_sum _ hd]
  have hterm : ∀ k ∈ range d,
      (ε₀ + ((M + k : ℕ) : R) * Δε) - (ε₀ + ((M - d + k : ℕ) : R) * Δε) =
        (d : R) * Δε := by
    intro k _
    rw [Nat.cast_add, Nat.cast_add, Nat.cast_sub hd]
    ring
  rw [sum_congr rfl hterm, sum_const, card_range, nsmul_eq_mul]
  ring

/-- **Quadratic Pauli Symmetry Energy in Terms of Neutron Excess $D = N - Z = 2d$**:
Writing $Z = M - d$ and $N = M + d$ so that $N - Z = 2d$, four times the discrete Pauli
asymmetry penalty equals $(N - Z)^2 \cdot \Delta\varepsilon$:
$$4\,\mathrm{pauliAsymmetryPenalty}(\varepsilon, M, d) = (N - Z)^2 \cdot \Delta\varepsilon.$$ -/
theorem quadratic_pauli_symmetry_in_N_sub_Z (ε₀ Δε : R) {M d : ℕ} (hd : d ≤ M) :
    4 * pauliAsymmetryPenalty (fun i => ε₀ + (i : R) * Δε) M d =
      (((M + d : ℕ) : R) - ((M - d : ℕ) : R)) ^ 2 * Δε := by
  rw [quadratic_pauli_symmetry_energy_exact ε₀ Δε hd]
  rw [Nat.cast_add, Nat.cast_sub hd]
  ring

end PauliSymmetryEnergy

section OrderedPauliSymmetryEnergy

variable {R : Type*} [CommRing R] [PartialOrder R] [IsOrderedRing R]

/-- **Non-Negativity of the Discrete Pauli Fermi-Asymmetry Promotion Penalty**:
For any non-decreasing single-particle spectrum `Monotone ε` over an ordered commutative
ring $R$ and any $d \le M$,
$$0 \le \mathrm{pauliAsymmetryPenalty}(\varepsilon, M, d).$$
Thus balanced isospin ($Z = N = M$, $d = 0$) is a global minimum of the two-species
Fermi shell-filling energy at fixed even mass number $A = 2M$. -/
theorem fermi_asymmetry_promotion_nonneg {ε : ℕ → R} (hmono : Monotone ε)
    {M d : ℕ} (hd : d ≤ M) :
    0 ≤ pauliAsymmetryPenalty ε M d := by
  rw [pauliAsymmetryPenalty_eq_promotion_sum ε hd]
  apply sum_nonneg
  intro k _
  have hle : M - d + k ≤ M + k := by omega
  exact sub_nonneg.mpr (hmono hle)

/-- **Strict Positivity of the Quadratic Pauli Symmetry Penalty for $d \ge 1$**:
When the local level spacing $\Delta\varepsilon > 0$ is strictly positive and $1 \le d \le M$,
the quadratic Pauli symmetry penalty $d^2 \Delta\varepsilon$ is strictly positive. -/
theorem quadratic_pauli_symmetry_pos {R : Type*} [CommRing R] [LinearOrder R]
    [IsStrictOrderedRing R] (ε₀ Δε : R) (hΔ : 0 < Δε) {M d : ℕ} (hd1 : 1 ≤ d) (hd : d ≤ M) :
    0 < pauliAsymmetryPenalty (fun i => ε₀ + (i : R) * Δε) M d := by
  rw [quadratic_pauli_symmetry_energy_exact ε₀ Δε hd]
  have hd_pos : (0 : R) < (d : R) := Nat.cast_pos.mpr (by omega)
  exact mul_pos (sq_pos_of_pos hd_pos) hΔ

end OrderedPauliSymmetryEnergy

end QOU.Nuclear.SpinOrbitShellClosureAndSymmetryEnergy
