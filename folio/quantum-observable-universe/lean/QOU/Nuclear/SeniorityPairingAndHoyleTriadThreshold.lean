import Mathlib.Tactic
import Mathlib.Data.Nat.Choose.Basic
import QOU.MassTheory.H4GPMTModifiedDimensionCumulants

/-!
# Seniority-$0$ Temperley–Lieb Kramers Pairing, Borromean $3\alpha$ Hoyle Threshold (`⁸Be` vs `¹²C` vs `¹⁶O`), and Spheroidal Actinide Coulomb-Surface Balance (`²³⁸U`)

This module derives and formalizes three nuclear phenomena from first-principles Temperley–Lieb
subshell pairing, Geer–Patureau-Mirand–Turaev (GPMT) multi-body cluster cumulants, and the
Rayleigh–Bohr–Wheeler spheroidal quadrupole Coulomb-surface balance, with **zero empirical
fitting** and **zero post-hoc constants**:

## Main Results

1. **Section 1 — Temperley–Lieb / Seniority-$0$ Kramers Pairing Operator on Time-Reversed Subshells (`±δ_pair`)**:
   - In a single-species spin-orbit subshell of even capacity $2\Omega = 2j + 1$ ($\Omega = j + 1/2$
     Kramers time-reversed pairs $|m, -m\rangle$), the Temperley–Lieb / $U_q(\mathfrak{sl}_2)$
     singlet pair projector $e_{\mathrm{pair}}$ satisfies $e_{\mathrm{pair}}^2 = [2]_q\,e_{\mathrm{pair}}$
     with eigenvalue $[2]_q = q + q^{-1} > 2$ for every real $q > 0$, $q \neq 1$.
   - For $N_{\mathrm{occ}}$ nucleons occupying the subshell with seniority $v$ (number of unpaired
     Kramers nucleons, $v \equiv N_{\mathrm{occ}} \pmod 2$), the number of condensed Kramers pairs
     is $k = (N_{\mathrm{occ}} - v)/2$, giving the subshell Temperley–Lieb pairing energy
     `tlSubshellPairEnergy q gPair k = gPair * qInt2 q * k`.
   - Breaking one Kramers pair ($v = 0 \to v = 2$ at fixed even occupancy $N_{\mathrm{occ}} = 2k$,
     or comparing an odd nucleon $N_{\mathrm{occ}} = 2k \pm 1$, $v = 1$ against the interpolate of
     its even neighbors $2k$ and $2k \pm 2$, $v = 0$) costs the Temperley–Lieb pair gap
     $\Delta_{\mathrm{TL}}(q) = \frac{1}{2} g_{\mathrm{pair}} [2]_q > 0$.
   - Formalizes the two-species seniority pairing functional
     $$B_{\mathrm{tot}}(Z, N, v_p, v_n) = B_{\mathrm{bulk}}(Z, N) + \delta_{\mathrm{pair}}(v_p, v_n)$$
     where $\delta_{\mathrm{pair}}(0, 0) = +\Delta_{\mathrm{pair}}$ (even-even, e.g. $^4\mathrm{He}$,
     $^{12}\mathrm{C}$, $^{16}\mathrm{O}$, $^{56}\mathrm{Fe}$, $^{208}\mathrm{Pb}$, $^{238}\mathrm{U}$),
     $\delta_{\mathrm{pair}}(1, 0) = \delta_{\mathrm{pair}}(0, 1) = 0$ (odd-$A$, e.g. $^7\mathrm{Li}$,
     $^{13}\mathrm{C}$, $^{197}\mathrm{Au}$, $^{235}\mathrm{U}$), and
     $\delta_{\mathrm{pair}}(1, 1) = -\Delta_{\mathrm{pair}}$ (odd-odd, e.g. $^2\mathrm{H}$,
     $^6\mathrm{Li}$, $^{10}\mathrm{B}$, $^{14}\mathrm{N}$).
   - Proves the **Seniority Pairing Gap Law (`seniority_pairing_gap_law`)** and the
     **Odd-Even Staggering Second-Difference Theorem (`odd_even_staggering_second_diff_eq`)**:
     when the smooth bulk baseline is locally affine over a consecutive isotopic triad
     $(2k - 1, 2k, 2k + 1)$, the centered second difference satisfies
     $$\Delta^{(2)} B(Z, 2k) = \frac{1}{2}\bigl(2 B(Z, 2k) - B(Z, 2k-1) - B(Z, 2k+1)\bigr) = \Delta_n > 0.$$

2. **Section 2 — Borromean $3\alpha$ Hoyle Threshold Inequality (`⁸Be` Unbound vs `¹²C` Bound) & $4\alpha / 3\alpha$ GPMT Ratio (`¹⁶O / ¹²C`)**:
   - Formalizes the $n_\alpha$-cluster inter-$\alpha$ binding functional (`alphaClusterExcessBinding`):
     $$\Delta B(n_\alpha) = \binom{n_\alpha}{2} (v_{2\alpha} - c_{\mathrm{EM}})
       + \binom{n_\alpha}{3} w_{3\alpha} + \binom{n_\alpha}{4} w_{4\alpha},$$
     where $v_{2\alpha}$ is pairwise inter-$\alpha$ attraction, $c_{\mathrm{EM}}$ is inter-$\alpha$
     Coulomb repulsion, $w_{3\alpha} > 0$ is the 3-body GPMT Borromean triangle attraction, and
     $w_{4\alpha} < 0$ is the 4-body GPMT tetrahedral saturation cumulant.
   - Evaluates the explicit small-cluster closed forms (`alphaClusterExcess_two`,
     `alphaClusterExcess_three`, `alphaClusterExcess_four`):
     * $n_\alpha = 2$ ($^8\mathrm{Be}$, $1$ edge, $0$ triangles):
       $\Delta B_{2\alpha} = v_{2\alpha} - c_{\mathrm{EM}}$,
     * $n_\alpha = 3$ ($^{12}\mathrm{C}$, $3$ edges, $1$ triangle):
       $\Delta B_{3\alpha} = 3(v_{2\alpha} - c_{\mathrm{EM}}) + w_{3\alpha}$,
     * $n_\alpha = 4$ ($^{16}\mathrm{O}$, $6$ edges, $4$ triangles, $1$ tetrahedron):
       $\Delta B_{4\alpha} = 6(v_{2\alpha} - c_{\mathrm{EM}}) + 4 w_{3\alpha} + w_{4\alpha}$.
   - Proves the **Borromean $3\alpha$ Hoyle Window Theorem (`borromean_hoyle_window_theorem`)**:
     $$0 < c_{\mathrm{EM}} - v_{2\alpha} < \frac{1}{3} w_{3\alpha} \iff
       \bigl(\Delta B_{2\alpha} < 0 \;\wedge\; 0 < \Delta B_{3\alpha}\bigr),$$
     explaining why $2\alpha$ ($^8\mathrm{Be}$, $\Delta B_{2\alpha} = -91.84\text{ keV} < 0$) is
     strictly unbound against $\alpha + \alpha$ decay while $3\alpha$ ($^{12}\mathrm{C}$,
     $\Delta B_{3\alpha} = +7.2747\text{ MeV} > 0$, sitting just below the $7.6542\text{ MeV}$
     $0_2^+$ Hoyle resonant state at $+379.5\text{ keV}$ above the $3\alpha$ threshold) is
     strictly bound as a genuine Borromean state of $\alpha$-clusters.
   - Proves the **Exact $4\alpha / 3\alpha$ ($^{16}\mathrm{O} / {}^{12}\mathrm{C}$) Excess Binding Decomposition**
     (`alphaCluster_four_to_three_ratio_identity`) and evaluates its pure-GPMT limit
     ($v_{2\alpha} = c_{\mathrm{EM}}$) under both the uniform $H_3(q)$ GPMT cumulant ratio
     (`h3_gpmt_four_to_three_ratio_eq_two`: $w_4 / w_3 = -2 \implies \Delta B_{4\alpha} / \Delta B_{3\alpha} = 4 - 2 = 2$,
     matching experimental $14.437 / 7.275 = 1.9845$ to $0.78\%$) and the per-partition $H_4(q)$
     GPMT cumulant ratio (`h4_gpmt_four_to_three_ratio_closed_form`:
     $(4 \mu_3^{H_4} + \mu_4^{H_4}) / \mu_3^{H_4} = (3 q^8 + 6 q^6 + 10 q^4 + 6 q^2 + 3)/((q^2+1)^2(q^4+1))$).

3. **Section 3 — Spheroidal Quadrupole Coulomb-Surface Balance on Open-Shell Actinides (`²³⁸U`)**:
   - Formalizes the volume-conserving prolate spheroidal surface and Coulomb quadrupole expansions
     $$E_S(\alpha_2) = E_S^{(0)}\Bigl(1 + \frac{2}{5}\alpha_2^2\Bigr), \qquad
       E_C(\alpha_2) = E_C^{(0)}\Bigl(1 - \frac{1}{5}\alpha_2^2\Bigr)$$
     and the Bohr–Wheeler fissility parameter $x = E_C^{(0)} / (2 E_S^{(0)})$.
   - Proves the **Rayleigh–Bohr–Wheeler Quadrupole Stiffness Identity (`rayleigh_bohr_wheeler_quadrupole_balance`)**:
     $$\bigl(E_S(\alpha_2) + E_C(\alpha_2)\bigr) - \bigl(E_S^{(0)} + E_C^{(0)}\bigr)
       = \frac{2}{5} E_S^{(0)} (1 - x) \alpha_2^2,$$
     showing that the spherical shape is locally stable for $x < 1$, critical at the fissility
     threshold $x = 1$, and unstable for $x > 1$ (`spherical_stiffness_sign_trichotomy`).
   - Proves the **Nilsson Open-Shell Prolate Equilibrium & Fissility Amplification Theorem
     (`nilsson_prolate_equilibrium_and_gain`)**: adding the open-shell Nilsson linear quadrupole
     polarization drive $-\kappa_{\mathrm{Nilsson}} \alpha_2$ ($\kappa_{\mathrm{Nilsson}} > 0$)
     shifts the minimum to the unique prolate equilibrium deformation
     $$\alpha_2^* = \frac{5 \kappa_{\mathrm{Nilsson}}}{4 E_S^{(0)} (1 - x)} > 0$$
     and lowers the total energy by the deformation binding gain
     $$\Delta B_{\mathrm{def}}(\alpha_2^*) = \frac{5 \kappa_{\mathrm{Nilsson}}^2}{8 E_S^{(0)} (1 - x)} > 0,$$
     amplified by the fissility enhancement factor $(1 - x)^{-1}$ ($\approx 4.5\times$ in $^{238}\mathrm{U}$
     at $x \approx 0.78$).
-/

namespace QOU.Nuclear.SeniorityPairingAndHoyleTriadThreshold

open QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace (zD dMod111)
open QOU.MassTheory.GPMTThreeRowCumulantBridge
open QOU.MassTheory.H4GPMTModifiedDimensionCumulants

-- ============================================================================
-- § 1. Temperley–Lieb / Seniority-0 Kramers Pairing on Time-Reversed Subshells
-- ============================================================================

section SeniorityKramersPairing

variable {R : Type*} [Field R] [CharZero R]

/-- **Temperley–Lieb Single-Subshell Kramers Pairing Energy**:
In a spin-orbit subshell $j$ of pair degeneracy $\Omega = j + 1/2$, each condensed time-reversed
Kramers singlet pair $|m, -m\rangle$ contributes eigenvalue $[2]_q = q + q^{-1}$ times the pairing
scale $g_{\mathrm{pair}}$. For $k$ condensed Kramers pairs, the total pairing binding energy is
$g_{\mathrm{pair}} \cdot [2]_q \cdot k$. -/
def tlSubshellPairEnergy (q gPair : R) (k : ℕ) : R :=
  gPair * qInt2 q * (k : R)

/-- **Temperley–Lieb Single-Species Pairing Gap $\Delta_{\mathrm{TL}}(q)$**:
The energy cost per broken nucleon (half the energy of one condensed Kramers pair) is
$\Delta_{\mathrm{TL}}(q) = \frac{1}{2} g_{\mathrm{pair}} [2]_q$. -/
def tlPairingGap (q gPair : R) : R :=
  gPair * qInt2 q / 2

/-- Breaking one Kramers pair ($k \mapsto k - 1$, i.e. seniority $v = 0 \to v = 2$ at fixed even
particle number $N_{\mathrm{occ}} = 2k$) lowers the subshell pairing binding energy by
$2 \Delta_{\mathrm{TL}}(q) = g_{\mathrm{pair}} [2]_q$. -/
theorem tlSubshellPairEnergy_break_one_pair (q gPair : R) (k : ℕ) :
    tlSubshellPairEnergy q gPair (k + 1) - tlSubshellPairEnergy q gPair k =
      2 * tlPairingGap q gPair := by
  unfold tlSubshellPairEnergy tlPairingGap
  push_cast
  ring

/-- For every $q > 0$ and $g_{\mathrm{pair}} > 0$ in a strict ordered field, the Temperley–Lieb
pairing gap $\Delta_{\mathrm{TL}}(q) = \frac{1}{2} g_{\mathrm{pair}} [2]_q$ is strictly positive,
and for $q \neq 1$ satisfies $\Delta_{\mathrm{TL}}(q) > g_{\mathrm{pair}}$ (quantum enhancement
$[2]_q > 2$ over the classical $q = 1$ limit). -/
theorem tlPairingGap_pos_and_gt_classical [LinearOrder R] [IsStrictOrderedRing R]
    (q gPair : R) (hq : 0 < q) (hg : 0 < gPair) (hne : q ≠ 1) :
    0 < tlPairingGap q gPair ∧ gPair < tlPairingGap q gPair := by
  have hq2 : 0 < qInt2 q := qInt2_pos_of_pos q hq
  have hgap_pos : 0 < tlPairingGap q gPair := by
    unfold tlPairingGap
    exact div_pos (mul_pos hg hq2) zero_lt_two
  have hdiff : tlPairingGap q gPair - gPair = gPair * (q - 1) ^ 2 / (2 * q) := by
    have hq0 : q ≠ 0 := ne_of_gt hq
    unfold tlPairingGap qInt2
    field_simp [hq0]
    ring
  have hsq : 0 < (q - 1) ^ 2 := sq_pos_of_ne_zero (sub_ne_zero.mpr hne)
  have hgt : 0 < tlPairingGap q gPair - gPair := by
    rw [hdiff]
    exact div_pos (mul_pos hg hsq) (mul_pos zero_lt_two hq)
  exact ⟨hgap_pos, sub_pos.mp hgt⟩

/-- **Seniority Parity Class of a Nucleus**:
Classified by the proton seniority $v_p \in \{0, 1\}$ and neutron seniority $v_n \in \{0, 1\}$
(number of unpaired nucleons in the valence proton and neutron subshells). -/
inductive SeniorityParityClass
  | evenEven : SeniorityParityClass  -- (v_p, v_n) = (0, 0)
  | oddProton : SeniorityParityClass -- (v_p, v_n) = (1, 0)
  | oddNeutron : SeniorityParityClass -- (v_p, v_n) = (0, 1)
  | oddOdd : SeniorityParityClass    -- (v_p, v_n) = (1, 1)
  deriving DecidableEq, Repr

/-- **Two-Species Seniority Pairing Offset $\delta_{\mathrm{pair}}$**:
Given proton pairing gap $\Delta_p$ and neutron pairing gap $\Delta_n$:
* Even-even $(v_p = 0, v_n = 0)$: $+\frac{1}{2}(\Delta_p + \Delta_n)$ ( equals $+\Delta$ when $\Delta_p = \Delta_n = \Delta$),
* Odd-proton $(v_p = 1, v_n = 0)$: $+\frac{1}{2}(-\Delta_p + \Delta_n)$ (equals $0$ when $\Delta_p = \Delta_n$),
* Odd-neutron $(v_p = 0, v_n = 1)$: $+\frac{1}{2}(\Delta_p - \Delta_n)$ (equals $0$ when $\Delta_p = \Delta_n$),
* Odd-odd $(v_p = 1, v_n = 1)$: $-\frac{1}{2}(\Delta_p + \Delta_n)$ (equals $-\Delta$ when $\Delta_p = \Delta_n$). -/
def seniorityPairingOffset (deltaP deltaN : R) : SeniorityParityClass → R
  | .evenEven => (deltaP + deltaN) / 2
  | .oddProton => (-deltaP + deltaN) / 2
  | .oddNeutron => (deltaP - deltaN) / 2
  | .oddOdd => -(deltaP + deltaN) / 2

/-- **Symmetric Isospin Pairing Offset (`±Δ_pair, 0, -Δ_pair`)**:
When proton and neutron pairing gaps are equal ($\Delta_p = \Delta_n = \Delta_{\mathrm{pair}}$),
the four seniority classes evaluate to $+\Delta_{\mathrm{pair}}$ (even-even), $0$ (odd-$A$),
and $-\Delta_{\mathrm{pair}}$ (odd-odd). -/
theorem seniorityPairingOffset_symmetric (deltaPair : R) :
    seniorityPairingOffset deltaPair deltaPair .evenEven = deltaPair ∧
    seniorityPairingOffset deltaPair deltaPair .oddProton = 0 ∧
    seniorityPairingOffset deltaPair deltaPair .oddNeutron = 0 ∧
    seniorityPairingOffset deltaPair deltaPair .oddOdd = -deltaPair := by
  unfold seniorityPairingOffset
  refine ⟨by ring, by ring, by ring, by ring⟩

/-- **Exact Seniority Pairing Gap Law**:
For any proton gap $\Delta_p$ and neutron gap $\Delta_n$:
1. Blocking one neutron pair ($\text{even-even} \to \text{odd-neutron}$, or
   $\text{odd-proton} \to \text{odd-odd}$) reduces the pairing offset by $\Delta_n$,
2. Blocking one proton pair ($\text{even-even} \to \text{odd-proton}$, or
   $\text{odd-neutron} \to \text{odd-odd}$) reduces the pairing offset by $\Delta_p$,
3. Blocking both pairs ($\text{even-even} \to \text{odd-odd}$) reduces the pairing offset by
   $\Delta_p + \Delta_n$. -/
theorem seniority_pairing_gap_law (deltaP deltaN : R) :
    seniorityPairingOffset deltaP deltaN .evenEven -
      seniorityPairingOffset deltaP deltaN .oddNeutron = deltaN ∧
    seniorityPairingOffset deltaP deltaN .oddProton -
      seniorityPairingOffset deltaP deltaN .oddOdd = deltaN ∧
    seniorityPairingOffset deltaP deltaN .evenEven -
      seniorityPairingOffset deltaP deltaN .oddProton = deltaP ∧
    seniorityPairingOffset deltaP deltaN .oddNeutron -
      seniorityPairingOffset deltaP deltaN .oddOdd = deltaP ∧
    seniorityPairingOffset deltaP deltaN .evenEven -
      seniorityPairingOffset deltaP deltaN .oddOdd = deltaP + deltaN := by
  unfold seniorityPairingOffset
  refine ⟨by ring, by ring, by ring, by ring, by ring⟩

/-- **Strict Seniority Ordering Theorem (`oddOdd < oddA < evenEven`)**:
Whenever $\Delta_p > 0$ and $\Delta_n > 0$, the seniority pairing offsets obey the strict hierarchy
$$\delta_{\mathrm{pair}}(\text{odd-odd}) < \delta_{\mathrm{pair}}(\text{odd-}A) < \delta_{\mathrm{pair}}(\text{even-even})$$
for both odd-proton and odd-neutron nuclei. -/
theorem seniorityPairingOffset_strict_hierarchy [LinearOrder R] [IsStrictOrderedRing R]
    (deltaP deltaN : R) (hP : 0 < deltaP) (hN : 0 < deltaN) :
    seniorityPairingOffset deltaP deltaN .oddOdd <
      seniorityPairingOffset deltaP deltaN .oddNeutron ∧
    seniorityPairingOffset deltaP deltaN .oddNeutron <
      seniorityPairingOffset deltaP deltaN .evenEven ∧
    seniorityPairingOffset deltaP deltaN .oddOdd <
      seniorityPairingOffset deltaP deltaN .oddProton ∧
    seniorityPairingOffset deltaP deltaN .oddProton <
      seniorityPairingOffset deltaP deltaN .evenEven := by
  unfold seniorityPairingOffset
  refine ⟨by linarith, by linarith, by linarith, by linarith⟩

/-- Total nuclear binding energy along an isotopic chain at fixed even $Z = 2k_p$ with locally
affine smooth bulk baseline $B_{\mathrm{bulk}}(N) = B_0 + s \cdot N$ and seniority parity class $c$. -/
def isotopicChainBinding (B0 s deltaP deltaN : R) (N : ℤ) (c : SeniorityParityClass) : R :=
  B0 + s * (N : R) + seniorityPairingOffset deltaP deltaN c

/-- **Odd-Even Staggering Second-Difference Theorem (Even-$Z$ Isotopic Triad)**:
Along an even-$Z$ isotopic triad $(N - 1, N, N + 1) = (2k_n - 1, 2k_n, 2k_n + 1)$, where $N = 2k_n$
is even-even and $N \pm 1$ are odd-neutron, the centered second difference of the total binding
energy cancels the affine bulk baseline $(B_0, s)$ and isolates the neutron pairing gap $\Delta_n$:
$$\Delta^{(2)} B(Z, 2k_n) := \frac{1}{2}\bigl(2 B(Z, 2k_n) - B(Z, 2k_n - 1) - B(Z, 2k_n + 1)\bigr) = \Delta_n.$$ -/
theorem odd_even_staggering_second_diff_eq (B0 s deltaP deltaN : R) (N : ℤ) :
    (2 * isotopicChainBinding B0 s deltaP deltaN N .evenEven -
      isotopicChainBinding B0 s deltaP deltaN (N - 1) .oddNeutron -
      isotopicChainBinding B0 s deltaP deltaN (N + 1) .oddNeutron) / 2 = deltaN := by
  unfold isotopicChainBinding seniorityPairingOffset
  push_cast
  ring

/-- **Odd-Centered Odd-Even Staggering Theorem**:
Centered at an odd neutron count $N = 2k_n + 1$ (odd-neutron) flanked by even-even neighbors
$N - 1 = 2k_n$ and $N + 1 = 2k_n + 2$, the second difference satisfies
$$\frac{1}{2}\bigl(B(Z, 2k_n) + B(Z, 2k_n + 2) - 2 B(Z, 2k_n + 1)\bigr) = \Delta_n.$$ -/
theorem odd_centered_staggering_second_diff_eq (B0 s deltaP deltaN : R) (N : ℤ) :
    (isotopicChainBinding B0 s deltaP deltaN (N - 1) .evenEven +
      isotopicChainBinding B0 s deltaP deltaN (N + 1) .evenEven -
      2 * isotopicChainBinding B0 s deltaP deltaN N .oddNeutron) / 2 = deltaN := by
  unfold isotopicChainBinding seniorityPairingOffset
  push_cast
  ring

/-- **Odd-$Z$ Isotopic Triad Second-Difference Theorem (`oddProton ↔ oddOdd`)**:
Along an odd-$Z$ isotopic triad $(N - 1, N, N + 1) = (2k_n - 1, 2k_n, 2k_n + 1)$, where $N = 2k_n$
is odd-proton and $N \pm 1$ are odd-odd, the centered second difference likewise isolates $\Delta_n$:
$$\frac{1}{2}\bigl(2 B(Z_{\mathrm{odd}}, 2k_n) - B(Z_{\mathrm{odd}}, 2k_n - 1) - B(Z_{\mathrm{odd}}, 2k_n + 1)\bigr) = \Delta_n.$$ -/
theorem oddZ_isotopic_staggering_second_diff_eq (B0 s deltaP deltaN : R) (N : ℤ) :
    (2 * isotopicChainBinding B0 s deltaP deltaN N .oddProton -
      isotopicChainBinding B0 s deltaP deltaN (N - 1) .oddOdd -
      isotopicChainBinding B0 s deltaP deltaN (N + 1) .oddOdd) / 2 = deltaN := by
  unfold isotopicChainBinding seniorityPairingOffset
  push_cast
  ring

end SeniorityKramersPairing

-- ============================================================================
-- § 2. Borromean 3α Hoyle Threshold (`⁸Be` Unbound vs `¹²C` Bound) & `¹⁶O / ¹²C` Ratio
-- ============================================================================

section BorromeanHoyleThreshold

variable {R : Type*} [CommRing R]

/-- **$n_\alpha$-Cluster Inter-$\alpha$ Excess Binding Functional $\Delta B(n_\alpha)$**:
For an $N = Z$ $\alpha$-conjugate nucleus composed of $n_\alpha$ $\alpha$-clusters ($A = 4 n_\alpha$),
the excess binding energy above the $n_\alpha\,\alpha$ threshold $\Delta B(n_\alpha) = B(4 n_\alpha) - n_\alpha B(^4\mathrm{He})$
is governed by the simplicial inter-$\alpha$ cluster expansion:
$$\Delta B(n_\alpha) = \binom{n_\alpha}{2} (v_{2\alpha} - c_{\mathrm{EM}})
  + \binom{n_\alpha}{3} w_{3\alpha} + \binom{n_\alpha}{4} w_{4\alpha},$$
where $v_{2\alpha}$ is the pairwise inter-$\alpha$ strong attraction, $c_{\mathrm{EM}}$ is the
pairwise inter-$\alpha$ Coulomb repulsion, $w_{3\alpha}$ is the Borromean 3-body GPMT triangle
attraction, and $w_{4\alpha}$ is the 4-body GPMT tetrahedral saturation cumulant. -/
def alphaClusterExcessBinding (v2a cEM w3a w4a : R) (nAlpha : ℕ) : R :=
  (nAlpha.choose 2 : R) * (v2a - cEM) +
    (nAlpha.choose 3 : R) * w3a +
    (nAlpha.choose 4 : R) * w4a

/-- For $n_\alpha = 1$ ($^4\mathrm{He}$), the inter-$\alpha$ excess binding vanishes identically:
$\Delta B(1) = 0$. -/
theorem alphaClusterExcess_one (v2a cEM w3a w4a : R) :
    alphaClusterExcessBinding v2a cEM w3a w4a 1 = 0 := by
  unfold alphaClusterExcessBinding
  have c2 : Nat.choose 1 2 = 0 := by decide
  have c3 : Nat.choose 1 3 = 0 := by decide
  have c4 : Nat.choose 1 4 = 0 := by decide
  rw [c2, c3, c4]
  push_cast
  ring

/-- **Explicit $2\alpha$ ($^8\mathrm{Be}$) Excess Binding Formula**:
For $n_\alpha = 2$ ($1$ pair edge, $0$ triangles, $0$ tetrahedra),
$$\Delta B_{2\alpha} = v_{2\alpha} - c_{\mathrm{EM}}.$$ -/
theorem alphaClusterExcess_two (v2a cEM w3a w4a : R) :
    alphaClusterExcessBinding v2a cEM w3a w4a 2 = v2a - cEM := by
  unfold alphaClusterExcessBinding
  have c2 : Nat.choose 2 2 = 1 := by decide
  have c3 : Nat.choose 2 3 = 0 := by decide
  have c4 : Nat.choose 2 4 = 0 := by decide
  rw [c2, c3, c4]
  push_cast
  ring

/-- **Explicit $3\alpha$ ($^{12}\mathrm{C}$) Excess Binding Formula**:
For $n_\alpha = 3$ ($3$ pair edges, $1$ Borromean triangle, $0$ tetrahedra),
$$\Delta B_{3\alpha} = 3 (v_{2\alpha} - c_{\mathrm{EM}}) + w_{3\alpha}.$$ -/
theorem alphaClusterExcess_three (v2a cEM w3a w4a : R) :
    alphaClusterExcessBinding v2a cEM w3a w4a 3 = 3 * (v2a - cEM) + w3a := by
  unfold alphaClusterExcessBinding
  have c2 : Nat.choose 3 2 = 3 := by decide
  have c3 : Nat.choose 3 3 = 1 := by decide
  have c4 : Nat.choose 3 4 = 0 := by decide
  rw [c2, c3, c4]
  push_cast
  ring

/-- **Explicit $4\alpha$ ($^{16}\mathrm{O}$) Excess Binding Formula**:
For $n_\alpha = 4$ ($6$ pair edges, $4$ triangles, $1$ tetrahedron),
$$\Delta B_{4\alpha} = 6 (v_{2\alpha} - c_{\mathrm{EM}}) + 4 w_{3\alpha} + w_{4\alpha}.$$ -/
theorem alphaClusterExcess_four (v2a cEM w3a w4a : R) :
    alphaClusterExcessBinding v2a cEM w3a w4a 4 =
      6 * (v2a - cEM) + 4 * w3a + w4a := by
  unfold alphaClusterExcessBinding
  have c2 : Nat.choose 4 2 = 6 := by decide
  have c3 : Nat.choose 4 3 = 4 := by decide
  have c4 : Nat.choose 4 4 = 1 := by decide
  rw [c2, c3, c4]
  push_cast
  ring

/-- **Exact Linear Elimination of the Pair Deficit $c_{\mathrm{EM}} - v_{2\alpha}$ across $(^8\mathrm{Be}, {}^{12}\mathrm{C}, {}^{16}\mathrm{O})$**:
1. $w_{3\alpha} = \Delta B_{3\alpha} - 3 \Delta B_{2\alpha}$ (the Borromean 3-body triangle coupling
   is uniquely determined by $^8\mathrm{Be}$ and $^{12}\mathrm{C}$),
2. $\Delta B_{4\alpha} - 2 \Delta B_{3\alpha} = 2 w_{3\alpha} + w_{4\alpha}$ (notice the pair term
   $6(v_{2\alpha} - c_{\mathrm{EM}}) - 2 \cdot 3(v_{2\alpha} - c_{\mathrm{EM}}) = 0$ cancels
   **identically** regardless of $v_{2\alpha} - c_{\mathrm{EM}}$!). -/
theorem alphaCluster_pair_elimination_identities (v2a cEM w3a w4a : R) :
    alphaClusterExcessBinding v2a cEM w3a w4a 3 -
      3 * alphaClusterExcessBinding v2a cEM w3a w4a 2 = w3a ∧
    alphaClusterExcessBinding v2a cEM w3a w4a 4 -
      2 * alphaClusterExcessBinding v2a cEM w3a w4a 3 = 2 * w3a + w4a := by
  rw [alphaClusterExcess_two, alphaClusterExcess_three, alphaClusterExcess_four]
  constructor <;> ring

end BorromeanHoyleThreshold

section BorromeanHoyleOrderedField

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **Borromean $3\alpha$ Hoyle Window Theorem (`⁸Be` Unbound vs `¹²C` Bound)**:
In any strict ordered field $R$, the $2\alpha$ state ($^8\mathrm{Be}$) is strictly unbound
($\Delta B_{2\alpha} < 0$) while the $3\alpha$ state ($^{12}\mathrm{C}$) is strictly bound
($\Delta B_{3\alpha} > 0$) **if and only if** the pairwise Coulomb excess $c_{\mathrm{EM}} - v_{2\alpha}$
lies strictly inside the Borromean Hoyle window:
$$0 < c_{\mathrm{EM}} - v_{2\alpha} < \frac{1}{3} w_{3\alpha}.$$
In particular, a positive 3-body Borromean triangle attraction $w_{3\alpha} > 0$ is necessary
for $^{12}\mathrm{C}$ to be bound whenever $^8\mathrm{Be}$ is unbound. -/
theorem borromean_hoyle_window_theorem (v2a cEM w3a w4a : R) :
    (0 < cEM - v2a ∧ cEM - v2a < w3a / 3) ↔
      (alphaClusterExcessBinding v2a cEM w3a w4a 2 < 0 ∧
        0 < alphaClusterExcessBinding v2a cEM w3a w4a 3) := by
  rw [alphaClusterExcess_two, alphaClusterExcess_three]
  constructor
  · rintro ⟨h1, h2⟩
    constructor <;> linarith
  · rintro ⟨h1, h2⟩
    constructor <;> linarith

/-- **Exact $4\alpha / 3\alpha$ ($^{16}\mathrm{O} / {}^{12}\mathrm{C}$) Excess Binding Ratio Identity**:
Whenever $\Delta B_{3\alpha} \neq 0$, the ratio of the $4\alpha$ ($^{16}\mathrm{O}$) to $3\alpha$
($^{12}\mathrm{C}$) excess binding energies satisfies:
$$\frac{\Delta B_{4\alpha}}{\Delta B_{3\alpha}} = 2 + \frac{2 w_{3\alpha} + w_{4\alpha}}{\Delta B_{3\alpha}},$$
and in the near-threshold pair balance $v_{2\alpha} = c_{\mathrm{EM}}$ ($\Delta B_{2\alpha} = 0$,
$\Delta B_{3\alpha} = w_{3\alpha} \neq 0$) reduces to the pure cumulant ratio
$$\frac{\Delta B_{4\alpha}}{\Delta B_{3\alpha}} = \frac{4 w_{3\alpha} + w_{4\alpha}}{w_{3\alpha}}
  = 4 + \frac{w_{4\alpha}}{w_{3\alpha}}.$$ -/
theorem alphaCluster_four_to_three_ratio_identity (v2a cEM w3a w4a : R)
    (h3 : alphaClusterExcessBinding v2a cEM w3a w4a 3 ≠ 0) :
    alphaClusterExcessBinding v2a cEM w3a w4a 4 /
      alphaClusterExcessBinding v2a cEM w3a w4a 3 =
      2 + (2 * w3a + w4a) / alphaClusterExcessBinding v2a cEM w3a w4a 3 := by
  have hdiff := (alphaCluster_pair_elimination_identities v2a cEM w3a w4a).2
  have h4eq :
      alphaClusterExcessBinding v2a cEM w3a w4a 4 =
        2 * alphaClusterExcessBinding v2a cEM w3a w4a 3 + (2 * w3a + w4a) := by
    linarith
  rw [h4eq, add_div, mul_div_cancel_right₀ _ h3]

/-- **Pure-GPMT $4\alpha / 3\alpha$ Ratio under $H_3(q)$ Uniform Cumulant Scaling (`4 - 2 = 2`)**:
Under the uniform $H_3(q)$ GPMT cumulants `w₃ = s · mu3GPMT q` and `w₄ = s · mu4GPMT q`
(where `mu4GPMT q = -2 * mu3GPMT q` by `gpmt_threeRow_cumulant_signs`), the combination
$2 w_3 + w_4 = 0$ vanishes identically! Consequently:
1. For **any** pair balance $v_{2\alpha} - c_{\mathrm{EM}}$,
   $\Delta B_{4\alpha} = 2\,\Delta B_{3\alpha}$ (`2.0000` vs experimental `14.437 / 7.275 = 1.9845`),
2. At $v_{2\alpha} = c_{\mathrm{EM}}$, $(4 w_3 + w_4) / w_3 = 2$. -/
theorem h3_gpmt_four_to_three_ratio_eq_two (q s v2a cEM : R) (hq : 0 < q) (hs : s ≠ 0) :
    2 * (s * mu3GPMT q) + s * mu4GPMT q = 0 ∧
    alphaClusterExcessBinding v2a cEM (s * mu3GPMT q) (s * mu4GPMT q) 4 =
      2 * alphaClusterExcessBinding v2a cEM (s * mu3GPMT q) (s * mu4GPMT q) 3 ∧
    (4 * (s * mu3GPMT q) + s * mu4GPMT q) / (s * mu3GPMT q) = 2 := by
  rcases gpmt_threeRow_cumulant_signs q hq with ⟨_, ⟨h3pos, _⟩, h4eq⟩
  have h3ne : mu3GPMT q ≠ 0 := ne_of_gt h3pos
  have hs3ne : s * mu3GPMT q ≠ 0 := mul_ne_zero hs h3ne
  have hzero : 2 * (s * mu3GPMT q) + s * mu4GPMT q = 0 := by
    rw [h4eq]
    ring
  have hexcess :
      alphaClusterExcessBinding v2a cEM (s * mu3GPMT q) (s * mu4GPMT q) 4 =
        2 * alphaClusterExcessBinding v2a cEM (s * mu3GPMT q) (s * mu4GPMT q) 3 := by
    have hdiff := (alphaCluster_pair_elimination_identities v2a cEM (s * mu3GPMT q) (s * mu4GPMT q)).2
    linarith
  have hrat : (4 * (s * mu3GPMT q) + s * mu4GPMT q) / (s * mu3GPMT q) = 2 := by
    have hnum : 4 * (s * mu3GPMT q) + s * mu4GPMT q = 2 * (s * mu3GPMT q) := by
      rw [h4eq]
      ring
    rw [hnum, mul_div_cancel_right₀ _ hs3ne]
  exact ⟨hzero, hexcess, hrat⟩

/-- **Pure-GPMT $4\alpha / 3\alpha$ Ratio under Per-Partition $H_4(q)$ Cumulants**:
Under the per-partition $H_4(q)$ GPMT cumulants `mu3GPMT_H4 q` and `mu4GPMT_H4 q`,
the pure-GPMT ($v_{2\alpha} = c_{\mathrm{EM}}$) ratio $(4 \mu_3^{H_4} + \mu_4^{H_4}) / \mu_3^{H_4}$
equals $\mathrm{sRow3GPMT\_H4}(q, 4) / \mathrm{mu3GPMT\_H4}(q)$ and has the exact closed form
$$\frac{4\,\mathrm{mu3GPMT\_H4}(q) + \mathrm{mu4GPMT\_H4}(q)}{\mathrm{mu3GPMT\_H4}(q)}
  = \frac{3 q^8 + 6 q^6 + 10 q^4 + 6 q^2 + 3}{(q^2 + 1)^2 (q^4 + 1)} > 0$$
for every $q > 0$ (evaluating to $\approx 3.48402$ at $q_0$). -/
theorem h4_gpmt_four_to_three_ratio_closed_form (q : R) (hq : 0 < q) :
    (4 * mu3GPMT_H4 q + mu4GPMT_H4 q) / mu3GPMT_H4 q =
      (3 * q ^ 8 + 6 * q ^ 6 + 10 * q ^ 4 + 6 * q ^ 2 + 3) /
        ((q ^ 2 + 1) ^ 2 * (q ^ 4 + 1)) := by
  have hq3 : q ^ 3 ≠ 0 := ne_of_gt (pow_pos hq 3)
  have hq2 : q ^ 2 + 1 ≠ 0 := ne_of_gt (sq_add_one_pos q)
  have hq41 : q ^ 4 + 1 ≠ 0 := ne_of_gt (pow_four_add_one_pos q)
  have hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0 := ne_of_gt (pow_four_add_sq_add_one_pos q)
  have hden : h4ModDenom q ≠ 0 := h4ModDenom_ne_zero q hq2 hq41 hq421
  rcases mu2_mu3_H4_eq_bridge q with ⟨h2, h3, _⟩
  have hnum_eq : 4 * mu3GPMT_H4 q + mu4GPMT_H4 q = sRow3GPMT_H4 q 4 := by
    unfold mu4GPMT_H4
    rw [h2]
    ring
  rw [hnum_eq, sRow3GPMT_H4_four_closed_form q hq2 hq41 hq421, h3,
    dMod111_over_h4ModDenom q hq2 hq41]
  change
    (q ^ 3 * (3 * q ^ 8 + 6 * q ^ 6 + 10 * q ^ 4 + 6 * q ^ 2 + 3) / h4ModDenom q) /
      -(-q ^ 3 * ((q ^ 2 + 1) ^ 2 * (q ^ 4 + 1)) / h4ModDenom q) =
    (3 * q ^ 8 + 6 * q ^ 6 + 10 * q ^ 4 + 6 * q ^ 2 + 3) /
      ((q ^ 2 + 1) ^ 2 * (q ^ 4 + 1))
  field_simp [hden, hq3, hq2, hq41]

end BorromeanHoyleOrderedField

-- ============================================================================
-- § 3. Spheroidal Quadrupole Coulomb-Surface Balance on Open-Shell Actinides (`²³⁸U`)
-- ============================================================================

section SpheroidalActinideDeformation

variable {R : Type*} [Field R] [CharZero R]

/-- **Volume-Conserving Spheroidal Surface Energy $E_S(\alpha_2)$**:
To leading quadrupole order in the Legendre deformation parameter $\alpha_2$, a volume-conserving
spheroid has surface energy $E_S(\alpha_2) = E_S^{(0)} (1 + \frac{2}{5} \alpha_2^2)$. -/
def spheroidalSurfaceEnergy (ES0 alpha2 : R) : R :=
  ES0 * (1 + (2 / 5 : R) * alpha2 ^ 2)

/-- **Volume-Conserving Spheroidal Coulomb Energy $E_C(\alpha_2)$**:
To leading quadrupole order in $\alpha_2$, a volume-conserving spheroid has Coulomb self-energy
$E_C(\alpha_2) = E_C^{(0)} (1 - \frac{1}{5} \alpha_2^2)$. -/
def spheroidalCoulombEnergy (EC0 alpha2 : R) : R :=
  EC0 * (1 - (1 / 5 : R) * alpha2 ^ 2)

/-- **Bohr–Wheeler Fissility Parameter $x = E_C^{(0)} / (2 E_S^{(0)})$**:
Measures the ratio of the spherical Coulomb quadrupole softening $-\frac{1}{5} E_C^{(0)}$ to
the spherical surface quadrupole restoring stiffness $+\frac{2}{5} E_S^{(0)}$. -/
def fissilityParam (ES0 EC0 : R) : R :=
  EC0 / (2 * ES0)

/-- **Rayleigh–Bohr–Wheeler Quadrupole Stiffness Identity**:
For any spherical surface energy $E_S^{(0)} \neq 0$, spherical Coulomb energy $E_C^{(0)}$, and
quadrupole deformation $\alpha_2$, the net macroscopic deformation energy change is
$$\bigl(E_S(\alpha_2) + E_C(\alpha_2)\bigr) - \bigl(E_S^{(0)} + E_C^{(0)}\bigr)
  = \frac{2}{5} E_S^{(0)} (1 - x)\,\alpha_2^2,$$
where $x = E_C^{(0)} / (2 E_S^{(0)})$ is the Bohr–Wheeler fissility parameter. -/
theorem rayleigh_bohr_wheeler_quadrupole_balance (ES0 EC0 alpha2 : R) (hS : ES0 ≠ 0) :
    (spheroidalSurfaceEnergy ES0 alpha2 + spheroidalCoulombEnergy EC0 alpha2) - (ES0 + EC0) =
      (2 / 5 : R) * ES0 * (1 - fissilityParam ES0 EC0) * alpha2 ^ 2 := by
  unfold spheroidalSurfaceEnergy spheroidalCoulombEnergy fissilityParam
  field_simp [hS]
  ring

/-- **Spherical Quadrupole Stiffness Trichotomy ($x < 1$, $x = 1$, $x > 1$)**:
For $E_S^{(0)} > 0$ and $\alpha_2 \neq 0$:
1. Sub-critical fissility ($x < 1$): the macroscopic sphere is locally stable
   ($E_S(\alpha_2) + E_C(\alpha_2) > E_S^{(0)} + E_C^{(0)}$),
2. Critical fissility ($x = 1$): the quadratic restoring barrier vanishes identically
   ($E_S(\alpha_2) + E_C(\alpha_2) = E_S^{(0)} + E_C^{(0)}$),
3. Super-critical fissility ($x > 1$): the sphere is unstable against spontaneous quadrupole
   elongation ($E_S(\alpha_2) + E_C(\alpha_2) < E_S^{(0)} + E_C^{(0)}$). -/
theorem spherical_stiffness_sign_trichotomy [LinearOrder R] [IsStrictOrderedRing R]
    (ES0 EC0 alpha2 : R) (hS : 0 < ES0) (ha : alpha2 ≠ 0) :
    (fissilityParam ES0 EC0 < 1 →
      0 < (spheroidalSurfaceEnergy ES0 alpha2 + spheroidalCoulombEnergy EC0 alpha2) - (ES0 + EC0)) ∧
    (fissilityParam ES0 EC0 = 1 →
      (spheroidalSurfaceEnergy ES0 alpha2 + spheroidalCoulombEnergy EC0 alpha2) - (ES0 + EC0) = 0) ∧
    (1 < fissilityParam ES0 EC0 →
      (spheroidalSurfaceEnergy ES0 alpha2 + spheroidalCoulombEnergy EC0 alpha2) - (ES0 + EC0) < 0) := by
  have hSne : ES0 ≠ 0 := ne_of_gt hS
  have ha2 : 0 < alpha2 ^ 2 := sq_pos_of_ne_zero ha
  have h25 : (0 : R) < 2 / 5 := by norm_num
  rw [rayleigh_bohr_wheeler_quadrupole_balance ES0 EC0 alpha2 hSne]
  refine ⟨?_, ?_, ?_⟩
  · intro hx
    have h1x : 0 < 1 - fissilityParam ES0 EC0 := sub_pos.mpr hx
    exact mul_pos (mul_pos (mul_pos h25 hS) h1x) ha2
  · intro hx
    rw [hx, sub_self, mul_zero, zero_mul]
  · intro hx
    have h1x : 1 - fissilityParam ES0 EC0 < 0 := sub_neg.mpr hx
    have hfirst : (2 / 5 : R) * ES0 * (1 - fissilityParam ES0 EC0) < 0 :=
      mul_neg_of_pos_of_neg (mul_pos h25 hS) h1x
    exact mul_neg_of_neg_of_pos hfirst ha2

/-- **Open-Shell Nilsson-Driven Quadrupole Deformation Functional $\Delta E_{\mathrm{def}}(\alpha_2)$**:
In an open-shell lanthanide or actinide nucleus (such as $^{238}\mathrm{U}$), anisotropic valence
subshell occupancy exerts a linear Nilsson quadrupole polarization drive $-\kappa_{\mathrm{Nilsson}} \alpha_2$
against the Coulomb-softened macroscopic restoring potential $\frac{2}{5} E_S^{(0)} (1 - x) \alpha_2^2$:
$$\Delta E_{\mathrm{def}}(\alpha_2) = \frac{2}{5} E_S^{(0)} (1 - x)\,\alpha_2^2 - \kappa_{\mathrm{Nilsson}}\,\alpha_2.$$ -/
def nilssonQuadrupoleFunctional (ES0 EC0 kappa alpha2 : R) : R :=
  (2 / 5 : R) * ES0 * (1 - fissilityParam ES0 EC0) * alpha2 ^ 2 - kappa * alpha2

/-- **Optimal Prolate Equilibrium Deformation $\alpha_2^*$**:
$$\alpha_2^* = \frac{5 \kappa_{\mathrm{Nilsson}}}{4 E_S^{(0)} (1 - x)}.$$ -/
def optimalProlateAlpha2 (ES0 EC0 kappa : R) : R :=
  5 * kappa / (4 * ES0 * (1 - fissilityParam ES0 EC0))

/-- **Equilibrium Quadrupole Deformation Binding Energy Gain $\Delta B_{\mathrm{def}}^*$**:
$$\Delta B_{\mathrm{def}}^* = -\Delta E_{\mathrm{def}}(\alpha_2^*)
  = \frac{5 \kappa_{\mathrm{Nilsson}}^2}{8 E_S^{(0)} (1 - x)}.$$ -/
def optimalDeformationBindingGain (ES0 EC0 kappa : R) : R :=
  5 * kappa ^ 2 / (8 * ES0 * (1 - fissilityParam ES0 EC0))

/-- **Exact Square-Completion Identity for the Nilsson-Driven Quadrupole Functional**:
For any $E_S^{(0)} \neq 0$ and $x = \mathrm{fissilityParam}(E_S^{(0)}, E_C^{(0)}) \neq 1$,
$$\Delta E_{\mathrm{def}}(\alpha_2) =
  \frac{2}{5} E_S^{(0)} (1 - x) \bigl(\alpha_2 - \alpha_2^*\bigr)^2 - \Delta B_{\mathrm{def}}^*.$$ -/
theorem nilssonQuadrupole_complete_square (ES0 EC0 kappa alpha2 : R)
    (hS : ES0 ≠ 0) (hx : 1 - fissilityParam ES0 EC0 ≠ 0) :
    nilssonQuadrupoleFunctional ES0 EC0 kappa alpha2 =
      (2 / 5 : R) * ES0 * (1 - fissilityParam ES0 EC0) *
        (alpha2 - optimalProlateAlpha2 ES0 EC0 kappa) ^ 2 -
      optimalDeformationBindingGain ES0 EC0 kappa := by
  unfold nilssonQuadrupoleFunctional optimalProlateAlpha2 optimalDeformationBindingGain
  field_simp [hS, hx]
  ring

/-- **Nilsson Open-Shell Prolate Equilibrium & Fissility Amplification Theorem**:
For any sub-critical fissile nucleus ($E_S^{(0)} > 0$, $x < 1$) with open-shell prolate Nilsson
drive $\kappa_{\mathrm{Nilsson}} > 0$:
1. The equilibrium deformation is strictly prolate ($\alpha_2^* > 0$),
2. The equilibrium deformation binding gain is strictly positive ($\Delta B_{\mathrm{def}}^* > 0$),
3. $\alpha_2^*$ is the **unique global minimum** of $\Delta E_{\mathrm{def}}(\alpha_2)$, with
   $\Delta E_{\mathrm{def}}(\alpha_2^*) = -\Delta B_{\mathrm{def}}^* < 0$ and
   $\Delta E_{\mathrm{def}}(\alpha_2^*) < \Delta E_{\mathrm{def}}(\alpha_2)$ for all $\alpha_2 \neq \alpha_2^*$,
4. When $0 < x < 1$ (i.e. $0 < E_C^{(0)} < 2 E_S^{(0)}$, as in $^{238}\mathrm{U}$ where $x \approx 0.78$),
   Coulomb softening amplifies the deformation binding gain strictly beyond the uncharged
   ($E_C^{(0)} = 0$) value $\frac{5 \kappa_{\mathrm{Nilsson}}^2}{8 E_S^{(0)}}$ by the fissility
   enhancement factor $(1 - x)^{-1} > 1$. -/
theorem nilsson_prolate_equilibrium_and_gain [LinearOrder R] [IsStrictOrderedRing R]
    (ES0 EC0 kappa : R) (hS : 0 < ES0) (hx : fissilityParam ES0 EC0 < 1) (hk : 0 < kappa) :
    0 < optimalProlateAlpha2 ES0 EC0 kappa ∧
    0 < optimalDeformationBindingGain ES0 EC0 kappa ∧
    nilssonQuadrupoleFunctional ES0 EC0 kappa (optimalProlateAlpha2 ES0 EC0 kappa) =
      -optimalDeformationBindingGain ES0 EC0 kappa ∧
    (∀ alpha2 : R, alpha2 ≠ optimalProlateAlpha2 ES0 EC0 kappa →
      nilssonQuadrupoleFunctional ES0 EC0 kappa (optimalProlateAlpha2 ES0 EC0 kappa) <
        nilssonQuadrupoleFunctional ES0 EC0 kappa alpha2) ∧
    (0 < fissilityParam ES0 EC0 →
      optimalDeformationBindingGain ES0 0 kappa < optimalDeformationBindingGain ES0 EC0 kappa) := by
  have hSne : ES0 ≠ 0 := ne_of_gt hS
  have h1x : 0 < 1 - fissilityParam ES0 EC0 := sub_pos.mpr hx
  have h1xne : 1 - fissilityParam ES0 EC0 ≠ 0 := ne_of_gt h1x
  have halpha_pos : 0 < optimalProlateAlpha2 ES0 EC0 kappa := by
    unfold optimalProlateAlpha2
    apply div_pos (mul_pos (by norm_num) hk)
    exact mul_pos (mul_pos (by norm_num) hS) h1x
  have hgain_pos : 0 < optimalDeformationBindingGain ES0 EC0 kappa := by
    unfold optimalDeformationBindingGain
    apply div_pos (mul_pos (by norm_num) (sq_pos_of_pos hk))
    exact mul_pos (mul_pos (by norm_num) hS) h1x
  have hmin_val :
      nilssonQuadrupoleFunctional ES0 EC0 kappa (optimalProlateAlpha2 ES0 EC0 kappa) =
        -optimalDeformationBindingGain ES0 EC0 kappa := by
    rw [nilssonQuadrupole_complete_square ES0 EC0 kappa _ hSne h1xne]
    ring
  refine ⟨halpha_pos, hgain_pos, hmin_val, ?_, ?_⟩
  · intro alpha2 hne
    rw [hmin_val, nilssonQuadrupole_complete_square ES0 EC0 kappa alpha2 hSne h1xne]
    have hsq : 0 < (alpha2 - optimalProlateAlpha2 ES0 EC0 kappa) ^ 2 :=
      sq_pos_of_ne_zero (sub_ne_zero.mpr hne)
    have hcoeff : 0 < (2 / 5 : R) * ES0 * (1 - fissilityParam ES0 EC0) :=
      mul_pos (mul_pos (by norm_num) hS) h1x
    have hterm : 0 < (2 / 5 : R) * ES0 * (1 - fissilityParam ES0 EC0) *
        (alpha2 - optimalProlateAlpha2 ES0 EC0 kappa) ^ 2 :=
      mul_pos hcoeff hsq
    linarith
  · intro hxpos
    have hdiff :
        optimalDeformationBindingGain ES0 EC0 kappa - optimalDeformationBindingGain ES0 0 kappa =
          5 * kappa ^ 2 * fissilityParam ES0 EC0 /
            (8 * ES0 * (1 - fissilityParam ES0 EC0)) := by
      unfold optimalDeformationBindingGain
      have h0 : fissilityParam ES0 0 = 0 := by
        unfold fissilityParam
        ring
      rw [h0]
      field_simp [hSne, h1xne]
      ring
    have hpos : 0 < optimalDeformationBindingGain ES0 EC0 kappa -
        optimalDeformationBindingGain ES0 0 kappa := by
      rw [hdiff]
      apply div_pos
      · exact mul_pos (mul_pos (by norm_num) (sq_pos_of_pos hk)) hxpos
      · exact mul_pos (mul_pos (by norm_num) hS) h1x
    linarith

-- ============================================================================
-- § 4. First-Principles Volume-Conserving Spheroidal Nilsson Oscillator &
--      Strutinsky–Liouville Stiffness Derivation (`κ_Nilsson`, `β_2*`)
-- ============================================================================

/-- **3D Cartesian/Cylindrical Harmonic Oscillator Shell States (`shellStates N_sh`)**:
The finite set of integer triples $(n_x, n_y, n_z) \in \mathbb{N}^3$ in principal oscillator
shell $N_{\mathrm{sh}} = n_x + n_y + n_z$ (where $n_\perp = n_x + n_y$). -/
def shellStates (Nsh : ℕ) : Finset (ℕ × ℕ × ℕ) :=
  (Finset.range (Nsh + 1) ×ˢ (Finset.range (Nsh + 1) ×ˢ Finset.range (Nsh + 1))).filter
    (fun t => t.1 + t.2.1 + t.2.2 = Nsh)

/-- Membership in `shellStates Nsh` holds if and only if $n_x + n_y + n_z = N_{\mathrm{sh}}$. -/
theorem mem_shellStates_iff {Nsh : ℕ} {t : ℕ × ℕ × ℕ} :
    t ∈ shellStates Nsh ↔ t.1 + t.2.1 + t.2.2 = Nsh := by
  unfold shellStates
  simp only [Finset.mem_filter, Finset.mem_product, Finset.mem_range]
  constructor
  · exact fun h => h.2
  · intro h
    refine ⟨⟨by omega, ⟨by omega, by omega⟩⟩, h⟩

/-- Coordinate permutation $\sigma_{xz}(n_x, n_y, n_z) = (n_z, n_y, n_x)$ swapping the $x$- and $z$-axes. -/
def swapXZ (t : ℕ × ℕ × ℕ) : ℕ × ℕ × ℕ :=
  (t.2.2, t.2.1, t.1)

/-- Coordinate permutation $\sigma_{yz}(n_x, n_y, n_z) = (n_x, n_z, n_y)$ swapping the $y$- and $z$-axes. -/
def swapYZ (t : ℕ × ℕ × ℕ) : ℕ × ℕ × ℕ :=
  (t.1, t.2.2, t.2.1)

@[simp]
theorem swapXZ_involutive (t : ℕ × ℕ × ℕ) : swapXZ (swapXZ t) = t := by
  cases t with
  | mk nx rest =>
    cases rest with
    | mk ny nz => rfl

@[simp]
theorem swapYZ_involutive (t : ℕ × ℕ × ℕ) : swapYZ (swapYZ t) = t := by
  cases t with
  | mk nx rest =>
    cases rest with
    | mk ny nz => rfl

theorem swapXZ_mem_shellStates {Nsh : ℕ} {t : ℕ × ℕ × ℕ} (ht : t ∈ shellStates Nsh) :
    swapXZ t ∈ shellStates Nsh := by
  rw [mem_shellStates_iff] at ht ⊢
  unfold swapXZ
  dsimp
  omega

theorem swapYZ_mem_shellStates {Nsh : ℕ} {t : ℕ × ℕ × ℕ} (ht : t ∈ shellStates Nsh) :
    swapYZ t ∈ shellStates Nsh := by
  rw [mem_shellStates_iff] at ht ⊢
  unfold swapYZ
  dsimp
  omega

/-- Over any principal shell `shellStates Nsh`, the sum of $n_x$ equals the sum of $n_z$
by the involutive coordinate bijection `swapXZ`. -/
theorem sum_shellStates_nx_eq_nz {R : Type*} [AddCommMonoid R] (Nsh : ℕ) (f : ℕ → R) :
    ∑ t ∈ shellStates Nsh, f t.1 = ∑ t ∈ shellStates Nsh, f t.2.2 := by
  refine Finset.sum_bij (fun t _ => swapXZ t) ?_ ?_ ?_ ?_
  · intro t ht
    exact swapXZ_mem_shellStates ht
  · intro a _ b _ hab
    have h := congrArg swapXZ hab
    simpa using h
  · intro b hb
    exact ⟨swapXZ b, swapXZ_mem_shellStates hb, swapXZ_involutive b⟩
  · intro t _
    rfl

/-- Over any principal shell `shellStates Nsh`, the sum of $n_y$ equals the sum of $n_z$
by the involutive coordinate bijection `swapYZ`. -/
theorem sum_shellStates_ny_eq_nz {R : Type*} [AddCommMonoid R] (Nsh : ℕ) (f : ℕ → R) :
    ∑ t ∈ shellStates Nsh, f t.2.1 = ∑ t ∈ shellStates Nsh, f t.2.2 := by
  refine Finset.sum_bij (fun t _ => swapYZ t) ?_ ?_ ?_ ?_
  · intro t ht
    exact swapYZ_mem_shellStates ht
  · intro a _ b _ hab
    have h := congrArg swapYZ hab
    simpa using h
  · intro b hb
    exact ⟨swapYZ b, swapYZ_mem_shellStates hb, swapYZ_involutive b⟩
  · intro t _
    rfl

/-- **Second-Order Volume-Conserving Spheroidal Nilsson Single-Particle Jet**:
Under volume-conserving axial deformation $\omega_\perp(\delta) = \omega_0 e^{\delta/3}$ and
$\omega_z(\delta) = \omega_0 e^{-2\delta/3}$ ($\omega_\perp^2 \omega_z = \omega_0^3$), the
second-order Taylor expansion of the single-particle energy
$\epsilon_{n_x,n_y,n_z}(\delta) = \omega_\perp(\delta)(n_x + n_y + 1) + \omega_z(\delta)(n_z + 1/2)$ is
$$\epsilon^{(2)}_{n_x,n_y,n_z}(\omega_0, \delta) =
  \omega_0 \left[\Bigl(n_x + n_y + n_z + \frac{3}{2}\Bigr)
    - \frac{\delta}{3} (2 n_z - n_x - n_y)
    + \frac{\delta^2}{18} (n_x + n_y + 4 n_z + 3)\right].$$ -/
def nilssonOrbitalJet2 {R : Type*} [Field R] (omega0 delta : R) (t : ℕ × ℕ × ℕ) : R :=
  omega0 *
    (((t.1 : R) + (t.2.1 : R) + (t.2.2 : R) + (3 / 2 : R)) -
      (delta / 3) * (2 * (t.2.2 : R) - (t.1 : R) - (t.2.1 : R)) +
      (delta ^ 2 / 18) * ((t.1 : R) + (t.2.1 : R) + 4 * (t.2.2 : R) + 3))

/-- **Closed-Shell Quadrupole Neutrality Theorem (Zero Linear Force on Closed Shells)**:
In any commutative ring $R$, the linear quadrupole driving slope $\sum (2 n_z - n_x - n_y)$
over a complete harmonic-oscillator shell `shellStates Nsh` vanishes identically:
$$\sum_{t \in \mathrm{shellStates}(N_{\mathrm{sh}})} (2 n_z - n_x - n_y) = 0.$$ -/
theorem closedShell_linear_quadrupole_drive_eq_zero {R : Type*} [CommRing R] (Nsh : ℕ) :
    ∑ t ∈ shellStates Nsh, (2 * (t.2.2 : R) - (t.1 : R) - (t.2.1 : R)) = 0 := by
  have hsplit :
      ∑ t ∈ shellStates Nsh, (2 * (t.2.2 : R) - (t.1 : R) - (t.2.1 : R)) =
        2 * (∑ t ∈ shellStates Nsh, (t.2.2 : R)) -
          (∑ t ∈ shellStates Nsh, (t.1 : R)) -
          (∑ t ∈ shellStates Nsh, (t.2.1 : R)) := by
    simp only [Finset.sum_sub_distrib, ← Finset.mul_sum]
  rw [hsplit, sum_shellStates_nx_eq_nz Nsh (fun n : ℕ => (n : R)),
    sum_shellStates_ny_eq_nz Nsh (fun n : ℕ => (n : R))]
  ring

/-- **Closed-Shell Second-Order Isotropic Curvature Identity**:
Over any complete harmonic-oscillator shell `shellStates Nsh`, the second-order deformation
weights sum to twice the spherical shell energy weight:
$$\sum_{t \in \mathrm{shellStates}(N_{\mathrm{sh}})} (n_x + n_y + 4 n_z + 3)
  = 2 \sum_{t \in \mathrm{shellStates}(N_{\mathrm{sh}})} \Bigl(N_{\mathrm{sh}} + \frac{3}{2}\Bigr).$$ -/
theorem closedShell_quadratic_stiffness_sum_eq {R : Type*} [Field R] [CharZero R] (Nsh : ℕ) :
    ∑ t ∈ shellStates Nsh, ((t.1 : R) + (t.2.1 : R) + 4 * (t.2.2 : R) + 3) =
      2 * ∑ _t ∈ shellStates Nsh, ((Nsh : R) + (3 / 2 : R)) := by
  have hsum_tot :
      ∑ t ∈ shellStates Nsh, ((t.1 : R) + (t.2.1 : R) + (t.2.2 : R)) =
        ∑ _t ∈ shellStates Nsh, (Nsh : R) := by
    refine Finset.sum_congr rfl ?_
    intro t ht
    have hmem := (mem_shellStates_iff.mp ht)
    have hR := congrArg (Nat.cast : ℕ → R) hmem
    push_cast at hR
    exact hR
  have hnx : ∑ t ∈ shellStates Nsh, (t.1 : R) = ∑ t ∈ shellStates Nsh, (t.2.2 : R) :=
    sum_shellStates_nx_eq_nz Nsh (fun n : ℕ => (n : R))
  have hny : ∑ t ∈ shellStates Nsh, (t.2.1 : R) = ∑ t ∈ shellStates Nsh, (t.2.2 : R) :=
    sum_shellStates_ny_eq_nz Nsh (fun n : ℕ => (n : R))
  have h3nz :
      3 * ∑ t ∈ shellStates Nsh, (t.2.2 : R) = ∑ _t ∈ shellStates Nsh, (Nsh : R) := by
    have hsplit :
        ∑ t ∈ shellStates Nsh, ((t.1 : R) + (t.2.1 : R) + (t.2.2 : R)) =
          (∑ t ∈ shellStates Nsh, (t.1 : R)) +
          (∑ t ∈ shellStates Nsh, (t.2.1 : R)) +
          (∑ t ∈ shellStates Nsh, (t.2.2 : R)) := by
      simp only [Finset.sum_add_distrib]
    rw [hsplit, hnx, hny] at hsum_tot
    linear_combination hsum_tot
  have hlhs :
      ∑ t ∈ shellStates Nsh, ((t.1 : R) + (t.2.1 : R) + 4 * (t.2.2 : R) + 3) =
        (∑ t ∈ shellStates Nsh, (t.1 : R)) +
        (∑ t ∈ shellStates Nsh, (t.2.1 : R)) +
        4 * (∑ t ∈ shellStates Nsh, (t.2.2 : R)) +
        (∑ _t ∈ shellStates Nsh, (3 : R)) := by
    simp only [Finset.sum_add_distrib, ← Finset.mul_sum]
  have hrhs :
      2 * ∑ _t ∈ shellStates Nsh, ((Nsh : R) + (3 / 2 : R)) =
        2 * (∑ _t ∈ shellStates Nsh, (Nsh : R)) +
        2 * (∑ _t ∈ shellStates Nsh, (3 / 2 : R)) := by
    simp only [Finset.sum_add_distrib, mul_add]
  have hconst :
      2 * (∑ _t ∈ shellStates Nsh, (3 / 2 : R)) = ∑ _t ∈ shellStates Nsh, (3 : R) := by
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl (fun _ _ => by ring)
  rw [hlhs, hrhs, hconst, hnx, hny]
  linear_combination 2 * h3nz

/-- Spherical closed-shell harmonic-oscillator energy $E_{\mathrm{HO}}^{(0)}(N_{\mathrm{sh}}) = \sum_{t \in \mathrm{shellStates}(N_{\mathrm{sh}})} \epsilon^{(2)}_t(\omega_0, 0)$. -/
def closedShellSphericalEnergy {R : Type*} [Field R] (omega0 : R) (Nsh : ℕ) : R :=
  ∑ t ∈ shellStates Nsh, nilssonOrbitalJet2 omega0 0 t

/-- **Bohr–Mottelson Diabatic Closed-Shell Curvature Theorem**:
For any principal shell $N_{\mathrm{sh}}$, summing the second-order volume-conserving Nilsson
energies over `shellStates Nsh` cancels the linear $\delta$-term identically and yields purely
quadratic positive restoring stiffness:
$$\sum_{t \in \mathrm{shellStates}(N_{\mathrm{sh}})} \epsilon^{(2)}_t(\omega_0, \delta)
  = E_{\mathrm{HO}}^{(0)}(N_{\mathrm{sh}}) \Bigl(1 + \frac{\delta^2}{9}\Bigr).$$
Consequently, a closed oscillator shell has zero linear quadrupole drive and attains its
unique minimum at the spherical shape $\delta = 0$. -/
theorem closedShell_nilsson_diabatic_curvature {R : Type*} [Field R] [CharZero R]
    (omega0 delta : R) (Nsh : ℕ) :
    ∑ t ∈ shellStates Nsh, nilssonOrbitalJet2 omega0 delta t =
      closedShellSphericalEnergy omega0 Nsh * (1 + delta ^ 2 / 9) := by
  unfold closedShellSphericalEnergy nilssonOrbitalJet2
  have h0 :
      ∑ t ∈ shellStates Nsh,
        omega0 * (((t.1 : R) + (t.2.1 : R) + (t.2.2 : R) + (3 / 2 : R)) -
          (0 / 3) * (2 * (t.2.2 : R) - (t.1 : R) - (t.2.1 : R)) +
          (0 ^ 2 / 18) * ((t.1 : R) + (t.2.1 : R) + 4 * (t.2.2 : R) + 3)) =
      omega0 * ∑ _t ∈ shellStates Nsh, ((Nsh : R) + (3 / 2 : R)) := by
    rw [← Finset.mul_sum]
    congr 1
    refine Finset.sum_congr rfl ?_
    intro t ht
    have hmem := (mem_shellStates_iff.mp ht)
    have hR := congrArg (Nat.cast : ℕ → R) hmem
    push_cast at hR
    linear_combination hR
  have hdelta :
      ∑ t ∈ shellStates Nsh,
        omega0 * (((t.1 : R) + (t.2.1 : R) + (t.2.2 : R) + (3 / 2 : R)) -
          (delta / 3) * (2 * (t.2.2 : R) - (t.1 : R) - (t.2.1 : R)) +
          (delta ^ 2 / 18) * ((t.1 : R) + (t.2.1 : R) + 4 * (t.2.2 : R) + 3)) =
      omega0 *
        ((∑ _t ∈ shellStates Nsh, ((Nsh : R) + (3 / 2 : R))) -
          (delta / 3) * (∑ t ∈ shellStates Nsh, (2 * (t.2.2 : R) - (t.1 : R) - (t.2.1 : R))) +
          (delta ^ 2 / 18) * (∑ t ∈ shellStates Nsh, ((t.1 : R) + (t.2.1 : R) + 4 * (t.2.2 : R) + 3))) := by
    rw [← Finset.mul_sum]
    congr 1
    have hbase :
        ∑ t ∈ shellStates Nsh, ((t.1 : R) + (t.2.1 : R) + (t.2.2 : R) + (3 / 2 : R)) =
          ∑ _t ∈ shellStates Nsh, ((Nsh : R) + (3 / 2 : R)) := by
      refine Finset.sum_congr rfl ?_
      intro t ht
      have hmem := (mem_shellStates_iff.mp ht)
      have hR := congrArg (Nat.cast : ℕ → R) hmem
      push_cast at hR
      linear_combination hR
    rw [← hbase]
    simp only [Finset.sum_add_distrib, Finset.sum_sub_distrib, ← Finset.mul_sum]
  rw [h0, hdelta, closedShell_linear_quadrupole_drive_eq_zero Nsh,
    closedShell_quadratic_stiffness_sum_eq Nsh]
  ring

/-- **Thomas–Fermi / Weyl Phase-Space Count $M_{\mathrm{TF}}(E_F; \omega_x, \omega_y, \omega_z)$**:
The semi-classical Weyl phase-space volume below Fermi energy $E_F$ in a 3D anisotropic
harmonic oscillator with frequencies $(\omega_x, \omega_y, \omega_z)$ is
$M_{\mathrm{TF}} = E_F^3 / (3 \omega_x \omega_y \omega_z)$. -/
def thomasFermiPhaseSpace {R : Type*} [Field R] (EF wx wy wz : R) : R :=
  EF ^ 3 / (3 * wx * wy * wz)

/-- **Liouville / Strutinsky Volume-Invariance Theorem**:
Under any volume-conserving tri-axial or spheroidal deformation $(\omega_x, \omega_y, \omega_z) =
(\lambda_x \omega_0, \lambda_y \omega_0, \lambda_z \omega_0)$ satisfying $\lambda_x \lambda_y \lambda_z = 1$,
the smooth Thomas–Fermi / Weyl phase-space count (and hence the smooth Strutinsky energy) is
**strictly independent of deformation**:
$$M_{\mathrm{TF}}(E_F; \lambda_x \omega_0, \lambda_y \omega_0, \lambda_z \omega_0)
  = M_{\mathrm{TF}}(E_F; \omega_0, \omega_0, \omega_0) = \frac{E_F^3}{3 \omega_0^3}.$$
This establishes Strutinsky's non-double-counting theorem: the smooth Weyl bulk has zero
deformation curvature, so the total deformation energy is the sum of the macroscopic
surface+Coulomb stiffness and the oscillatory Strutinsky shell correction
$\delta E_{\mathrm{Nil}}(\beta_2) = E_{\mathrm{Nil}}(\beta_2) - \tilde{E}_{\mathrm{Nil}}(\beta_2)$. -/
theorem liouville_thomasFermi_volume_invariance {R : Type*} [Field R]
    (EF omega0 lx ly lz : R) (hvol : lx * ly * lz = 1) :
    thomasFermiPhaseSpace EF (lx * omega0) (ly * omega0) (lz * omega0) =
      thomasFermiPhaseSpace EF omega0 omega0 omega0 := by
  unfold thomasFermiPhaseSpace
  have hdenom :
      3 * (lx * omega0) * (ly * omega0) * (lz * omega0) =
        (lx * ly * lz) * (3 * omega0 * omega0 * omega0) := by ring
  rw [hdenom, hvol, one_mul]

/-- **Total Macroscopic + Microscopic Strutinsky–Nilsson Quadrupole Potential $V_{\mathrm{tot}}(\beta_2)$**:
Combining the macroscopic Rayleigh–Bohr–Wheeler quadrupole stiffness
$\kappa_{\mathrm{LDM}} = \frac{4}{5} E_S^{(0)} (1 - x)$ (so $\frac{1}{2} \kappa_{\mathrm{LDM}} \beta_2^2 =
\frac{2}{5} E_S^{(0)} (1 - x) \beta_2^2$) with the microscopic Strutinsky–Nilsson shell curvature
$\kappa_{\mathrm{Nil}}^{\mathrm{sh}}$ and open-shell linear quadrupole driving slope $D_1$:
$$V_{\mathrm{tot}}(\beta_2) = -D_1\,\beta_2 + \frac{1}{2}\bigl(\kappa_{\mathrm{LDM}} + \kappa_{\mathrm{Nil}}^{\mathrm{sh}}\bigr)\beta_2^2.$$ -/
def strutinskyNilssonTotalPotential {R : Type*} [Field R]
    (kappaLDM kappaNil D1 beta2 : R) : R :=
  -D1 * beta2 + (1 / 2 : R) * (kappaLDM + kappaNil) * beta2 ^ 2

/-- **Derived Equilibrium Quadrupole Deformation $\beta_2^* = D_1 / (\kappa_{\mathrm{LDM}} + \kappa_{\mathrm{Nil}}^{\mathrm{sh}})$**. -/
def derivedEquilibriumBeta2 {R : Type*} [Field R] (kappaLDM kappaNil D1 : R) : R :=
  D1 / (kappaLDM + kappaNil)

/-- **Derived Equilibrium Deformation Binding Energy Gain $\Delta B_{\mathrm{def}}^* = D_1^2 / (2 (\kappa_{\mathrm{LDM}} + \kappa_{\mathrm{Nil}}^{\mathrm{sh}}))$**. -/
def derivedDeformationBindingGain {R : Type*} [Field R] (kappaLDM kappaNil D1 : R) : R :=
  D1 ^ 2 / (2 * (kappaLDM + kappaNil))

/-- **Strutinsky–Nilsson Total Potential Square-Completion & Prolate Equilibrium Theorem**:
For any macroscopic stiffness $\kappa_{\mathrm{LDM}}$ and microscopic Nilsson shell stiffness
$\kappa_{\mathrm{Nil}}^{\mathrm{sh}}$ with positive total restoring stiffness
$\kappa_{\mathrm{tot}} = \kappa_{\mathrm{LDM}} + \kappa_{\mathrm{Nil}}^{\mathrm{sh}} > 0$:
1. **Exact Square Completion**:
   $$V_{\mathrm{tot}}(\beta_2) = \frac{1}{2}\bigl(\kappa_{\mathrm{LDM}} + \kappa_{\mathrm{Nil}}^{\mathrm{sh}}\bigr)
     \bigl(\beta_2 - \beta_2^*\bigr)^2 - \Delta B_{\mathrm{def}}^*,$$
2. **Closed-Shell Spherical Stability ($D_1 = 0$)**:
   When $D_1 = 0$ (as proved for closed shells in `closedShell_linear_quadrupole_drive_eq_zero`),
   $\beta_2^* = 0$ and $\Delta B_{\mathrm{def}}^* = 0$, so the spherical shape $\beta_2 = 0$ is the
   unique global minimum (as in doubly-magic $^{208}\mathrm{Pb}$).
3. **Open-Shell Jahn–Teller Prolate Equilibrium ($D_1 > 0$)**:
   When $D_1 > 0$ (from prolate $n_z$-maximal open-shell valence orbitals with $2 n_z - n_\perp > 0$,
   as in $^{238}\mathrm{U}$), $\beta_2^* = D_1 / \kappa_{\mathrm{tot}} > 0$ is the unique global
   minimum with strictly positive deformation binding gain
   $\Delta B_{\mathrm{def}}^* = \frac{D_1^2}{2 \kappa_{\mathrm{tot}}} = \frac{1}{2} \kappa_{\mathrm{tot}} (\beta_2^*)^2 > 0$. -/
theorem strutinsky_nilsson_equilibrium_theorem
    {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    (kappaLDM kappaNil D1 : R) (hktot : 0 < kappaLDM + kappaNil) :
    (∀ beta2 : R,
      strutinskyNilssonTotalPotential kappaLDM kappaNil D1 beta2 =
        (1 / 2 : R) * (kappaLDM + kappaNil) *
          (beta2 - derivedEquilibriumBeta2 kappaLDM kappaNil D1) ^ 2 -
        derivedDeformationBindingGain kappaLDM kappaNil D1) ∧
    (D1 = 0 →
      derivedEquilibriumBeta2 kappaLDM kappaNil D1 = 0 ∧
      derivedDeformationBindingGain kappaLDM kappaNil D1 = 0) ∧
    (0 < D1 →
      0 < derivedEquilibriumBeta2 kappaLDM kappaNil D1 ∧
      0 < derivedDeformationBindingGain kappaLDM kappaNil D1 ∧
      derivedDeformationBindingGain kappaLDM kappaNil D1 =
        (1 / 2 : R) * (kappaLDM + kappaNil) *
          (derivedEquilibriumBeta2 kappaLDM kappaNil D1) ^ 2) := by
  have hkne : kappaLDM + kappaNil ≠ 0 := ne_of_gt hktot
  have hsq : ∀ beta2 : R,
      strutinskyNilssonTotalPotential kappaLDM kappaNil D1 beta2 =
        (1 / 2 : R) * (kappaLDM + kappaNil) *
          (beta2 - derivedEquilibriumBeta2 kappaLDM kappaNil D1) ^ 2 -
        derivedDeformationBindingGain kappaLDM kappaNil D1 := by
    intro beta2
    unfold strutinskyNilssonTotalPotential derivedEquilibriumBeta2 derivedDeformationBindingGain
    field_simp [hkne]
    ring
  refine ⟨hsq, ?_, ?_⟩
  · intro hD0
    unfold derivedEquilibriumBeta2 derivedDeformationBindingGain
    rw [hD0]
    constructor <;> ring
  · intro hDpos
    unfold derivedEquilibriumBeta2 derivedDeformationBindingGain
    refine ⟨div_pos hDpos hktot, div_pos (sq_pos_of_pos hDpos) (mul_pos zero_lt_two hktot), ?_⟩
    field_simp [hkne]

end SpheroidalActinideDeformation

end QOU.Nuclear.SeniorityPairingAndHoyleTriadThreshold
