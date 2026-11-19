#!/usr/bin/env python3
"""nuclear_spin_orbit_shells_and_symmetry_probe.py — 80-dps First-Principles
Higher-l Spin-Orbit Pauli Fiber (2j+1), Mayer-Jensen Magic Closures, Quadratic
Fermi/Pauli Symmetry Energy, and Microscopic Shell-Correction Probe
(Zero Fitting, Zero Float64).

Companion to Lean 4 formalization:
  `folio/quantum-observable-universe/lean/QOU/Nuclear/SpinOrbitShellClosureAndSymmetryEnergy.lean`
  (`namespace QOU.Nuclear.SpinOrbitShellClosureAndSymmetryEnergy`)
and its s-wave simplicial foundation:
  `folio/quantum-observable-universe/lean/QOU/Nuclear/AlphaSimplexCoordinationDerivation.lean`
  (`namespace QOU.Nuclear.AlphaSimplexCoordinationDerivation`).

PURPOSE & STRICT ANTI-FITTING DISCIPLINE
----------------------------------------
Evaluates at 80 decimal places (zero float64 intermediates, zero `math` module
imports, zero empirical parameters fit to AME2020) the graded orbital-spin-isospin
Pauli shell tower formalized in `SpinOrbitShellClosureAndSymmetryEnergy.lean`:

1. **Graded Spin-Orbit Subshell Capacities (`2j + 1`) & Mayer-Jensen Closures**:
   - Single-species spin-aligned subshell `j = l + 1/2`: `degPlus(l) = 2*l + 2`.
   - Single-species spin-antialigned subshell `j = l - 1/2`: `degMinus(l) = 2*l`.
   - 3D harmonic-oscillator shell degeneracy `oscShellDeg(N) = (N + 1)*(N + 2)` and
     exact cumulative closure `cumOscClosure(K) = (K + 1)*(K + 2)*(K + 3) / 3`
     (`2, 8, 20, 40, 70, 112, 168` for `K = 0..6`).
   - Exact Carbon-12 (`Z = N = 6`) spin-orbit subshell closure:
     `oscShellDeg(0) + degPlus(1) = 2 + 4 = 6` (`1s_{1/2}^2 1p_{3/2}^4`) before
     `degMinus(1) = 2` (`1p_{1/2}^2`) completes Oxygen-16 at `Z = N = 8`.
   - Universal Mayer-Jensen intruder formula (`K >= 2`):
     `M_K = (K + 1)*(K + 2)*(K + 3) / 3 + (2*K + 4) in {28, 50, 82, 126, 184}`
     for `K = 2, 3, 4, 5, 6`.

2. **Parameter-Free QOU Oscillator Spacing `hbar*omega_q(A)` & Spin-Orbit Splitting**:
   - Evaluates two parameter-free QOU Compton/Fermi oscillator scale candidates
     side-by-side without post-hoc selection:
     * **Candidate I (Compton/Fermi shell quantum `(E_0^{(0)} / hbar_q) / A^{1/3}`)**:
       `hbar*omega_q^{(I)}(A) = (E_0^{(0)}(q) / hbar_q) / A^{1/3} = (m_e / (q - 1)^2) / A^{1/3}`,
       where `E_0^{(0)} = m_e / (q*(q - 1)) ≈ 4.18598 MeV`, `hbar_q = (q - 1)/q ≈ 0.0990817`,
       and `E_osc^{(I)}(q_0) = E_0^{(0)} / hbar_q = 42.24777 MeV` (tower-resummed
       `E_0^{(inf)} / hbar_q = 42.66664 MeV`, matching the standard nuclear oscillator
       scale `41..43 MeV * A^{-1/3}` with zero free parameters).
     * **Candidate II (Tower-resummed & bare Hecke level-0 quanta `E_0^{(inf)} / A^{1/3}` and `E_0^{(0)} / A^{1/3}`)**:
       `hbar*omega_q^{(II,inf)}(A) = E_0^{(inf)}(q) / A^{1/3}` (`E_0^{(inf)} = E_0^{(0)} / (1 - hbar_q^2) = 4.22748 MeV`)
       and `hbar*omega_q^{(II,bare)}(A) = E_0^{(0)}(q) / A^{1/3}` (`E_0^{(0)} = 4.18598 MeV`).
   - Parameter-free spin-orbit coupling constant from the Hecke/Reeb commutator
     quantum `h = q - q^{-1}` and Convention-D Markov trace `z_D = q^3 / (q^2 + 1)`:
     `kappa_SO(q) = h * z_D / 2` (`= 0.06404437` at `q_0`), with:
     * **Pure spin-orbit shift (`l . s` only)**:
       `Delta_SO^{pure}(l, j) = -kappa_SO(q) * hbar*omega_q(A) * <2 l . s>`, where
       `<2 l . s> = +l` for `j = l + 1/2` (deg `2l + 2`) and `<2 l . s> = -(l + 1)`
       for `j = l - 1/2` (deg `2l`). Because `(2l + 2)*l - 2l*(l + 1) = 0`, the pure
       `l . s` shift vanishes identically on every spin-saturated `l`-shell
       (`4He`, `16O`, `40Ca`), while peaking positively on spin-unsaturated
       aligned closures (`12C [1p_{3/2}^4]`, `28Si [1d_{5/2}^6]`, `48Ca [1f_{7/2}^8]`,
       `56Ni`, `120Sn`, `132Sn`, `208Pb`, `238U`).
     * **Monotone Nilsson/Mayer-Jensen energy ordering (`l . s` + centrifugal `-kappa_SO^2 * l(l+1)/2`)**:
       `eps_SO(N_osc, l, j) = (N_osc + 3/2) - kappa_SO * <2 l . s> - kappa_SO^2 * l*(l + 1) / 2`,
       sorted monotonically in energy so that `Monotone eps` (`fermi_asymmetry_promotion_nonneg`)
       holds identically across all 184 single-particle states. Both the pure `l . s`
       stabilization and the Nilsson centrifugal-inclusive stabilization are recorded
       separately in the witness.

3. **Discrete Single-Particle Shell Filling, Quadratic Pauli Symmetry Energy
   `E_sym(Z, N) propto (N - Z)^2 / A`, and Smooth Weyl Shell Correction `delta E_Weyl(Z, N)`**:
   - Computes exact discrete single-particle level filling sums
     `E_fill(M) = sum_{i=1}^M eps_i` for protons (`M = Z`) and neutrons (`M = N`).
   - Extracts the exact discrete Pauli Fermi-asymmetry promotion penalty
     `E_sym^{disc}(Z, N) = E_fill(Z) + E_fill(N) - 2 * E_fill(A / 2)`
     (`pauliAsymmetryPenalty` in `SpinOrbitShellClosureAndSymmetryEnergy.lean`),
     together with the two parameter-free quadratic symmetry energy candidates
     `E_sym^{quad}(Z, N) = a_sym(q) * (N - Z)^2 / A`:
     * **Candidate 1 (Compton/Fermi shell scale)**:
       `a_sym^{(I)}(q_0) = (E_0^{(0)}(q_0) / hbar_q) * z_D = 25.88470 MeV`,
     * **Candidate 2 (Hecke level-0 scale)**:
       `a_sym^{(II)}(q_0) = E_0^{(inf)}(q_0) * z_D / (1 + hbar_q^2) = 2.56495 MeV`,
     evaluated side-by-side against the linear 3-tree excess deficits (`pauliBridge`
     and `pauliTriangle`) from `AlphaSimplexCoordinationDerivation.lean`.
   - Evaluates the exact smooth Weyl / Thomas-Fermi 3D harmonic-oscillator baseline
     `E_smooth(M) = (3/4) * M * u_Weyl + (1/16) * ((3*M)^{2/3} - 1)` where
     `u_Weyl = (3*M)^{1/3} + 1 / (3 * (3*M)^{1/3})` (centered at the shell-oscillation mean
     `+(1/16)*(u^2 - 1)` between the exact closed-shell sum `(3/4) * M * (K + 2)` and the
     open-shell midpoint excess `+(1/8)*(u^2 - 1)`), recording both
     `delta_Weyl_HO_shell_dimless = (E_smooth(Z) - E_fill^{HO}(Z)) + (E_smooth(N) - E_fill^{HO}(N))`
     (which oscillates around zero: positive at harmonic-oscillator closures `4He`, `16O`, `40Ca`
     and negative at mid-shells `12C`, `24Mg`, `28Si`, `56Ni`, `208Pb`) and
     `delta_Weyl_shell_dimless = (E_smooth(Z) - E_fill^{SO}(Z)) + (E_smooth(N) - E_fill^{SO}(N))`
     (which spin-orbit lowering flips from negative in pure HO to positive at `12C`, `28Si`,
     `48Ca`, `56Ni`, `132Sn`, and `208Pb`, while keeping mid-shell `24Mg` negative).

4. **Cross-Anchor (`proton` vs `muon`) + Two-Term (`q_2t`) Evaluation**:
   - Evaluates the substrate constants and binding residuals across both canonical
     pins (`proton` and `muon`) plus the parameter-free 2-term Borromean root `q_2t`,
     and stamps top-level `"q0Anchor": "comparison"` with `"q0Values"` and
     `"q0AnchorReason"`.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(ROOT / "substrate") not in sys.path:
    sys.path.insert(0, str(ROOT / "substrate"))

import _path_bridge  # noqa: F401, E402
from _precision import fmt, set_compute_dps  # noqa: E402
import mpmath as mp  # noqa: E402

set_compute_dps(80)

from codata_constants import M_E_MEV, _ame_entry, ame_binding_mev  # noqa: E402
from coulomb_energy import coulomb_energy_mev  # noqa: E402
from q_parameter import (  # noqa: E402
    Q_50_DIGIT_STR,
    Q_TWO_TERM_50_DIGIT_STR,
    q_at,
    q_muon_at,
    q_two_term_borromean_at,
)
from witness_base import WitnessBuilder, q0_comparison  # noqa: E402


# ── Exact Integer Functions Matching SpinOrbitShellClosureAndSymmetryEnergy.lean ──

def deg_plus(ell: int) -> int:
    """Single-species degeneracy 2j + 1 = 2*ell + 2 for j = ell + 1/2."""
    return 2 * ell + 2


def deg_minus(ell: int) -> int:
    """Single-species degeneracy 2j + 1 = 2*ell for j = ell - 1/2 (0 at ell = 0)."""
    return 2 * ell


def single_species_orbital_cap(ell: int) -> int:
    """2*(2*ell + 1)."""
    return 2 * (2 * ell + 1)


def total_orbital_spin_isospin_cap(ell: int) -> int:
    """4*(2*ell + 1)."""
    return 4 * (2 * ell + 1)


def osc_shell_deg(n_osc: int) -> int:
    """Single-species 3D isotropic harmonic-oscillator shell degeneracy (N+1)(N+2)."""
    return (n_osc + 1) * (n_osc + 2)


def cum_osc_closure(k_osc: int) -> int:
    """Cumulative single-species harmonic-oscillator closure (K+1)(K+2)(K+3)//3."""
    return ((k_osc + 1) * (k_osc + 2) * (k_osc + 3)) // 3


def mayer_jensen_magic(k_osc: int) -> int:
    """Universal Mayer-Jensen spin-orbit intruder magic number for K >= 2:
    M_K = cumOscClosure(K) + degPlus(K + 1) = (K+1)(K+2)(K+3)//3 + (2K + 4)."""
    return cum_osc_closure(k_osc) + deg_plus(k_osc + 1)


def f1_simplex(A: int) -> int:
    if A <= 1:
        return 0
    if A == 2:
        return 1
    return 3 * A - 6


def f2_simplex(A: int) -> int:
    if A <= 2:
        return 0
    return 3 * A - 8


def f3_simplex(A: int) -> int:
    if A <= 3:
        return 0
    return A - 3


# ── Spectroscopic Single-Particle Spin-Orbit Subshell Ordering ────────────────
# Each entry is (label, N_osc, n_radial, ell, two_j, aligned_plus, degeneracy).
# Ordered by Mayer-Jensen spin-orbit energy E(N_osc, ell, j) = (N_osc + 3/2) - kappa_SO * <2 l.s>
# so that for N_osc >= 3 the stretched state (n_r=0, ell=N_osc, j=N_osc+1/2) intrudes into
# the (N_osc - 1) major shell, producing cumulative closures:
#   2 (1s1/2), 6 (1p3/2), 8 (1p1/2), 14 (1d5/2), 16 (2s1/2), 20 (1d3/2),
#   28 (1f7/2), 50 (+2p3/2,1f5/2,2p1/2,1g9/2), 82 (+1g7/2,2d5/2,2d3/2,3s1/2,1h11/2),
#   126 (+1h9/2,2f7/2,2f5/2,3p3/2,3p1/2,1i13/2),
#   184 (+1i11/2,2g9/2,2g7/2,3d5/2,3d3/2,4s1/2,1j15/2).
SPECTROSCOPIC_SUBSHELLS: list[tuple[str, int, int, int, int, bool, int]] = [
    # Major shell K = 0 (closes at 2)
    ("1s_{1/2}", 0, 0, 0, 1, True, deg_plus(0)),     # cum = 2
    # Major shell K = 1 (subshell closure at 6 [12C], major closure at 8 [16O])
    ("1p_{3/2}", 1, 0, 1, 3, True, deg_plus(1)),     # cum = 6  (12C Z=N=6)
    ("1p_{1/2}", 1, 0, 1, 1, False, deg_minus(1)),   # cum = 8  (16O Z=N=8)
    # Major shell K = 2 (subshell closure at 14 [28Si], major closure at 20 [40Ca])
    ("1d_{5/2}", 2, 0, 2, 5, True, deg_plus(2)),     # cum = 14
    ("2s_{1/2}", 2, 1, 0, 1, True, deg_plus(0)),     # cum = 16
    ("1d_{3/2}", 2, 0, 2, 3, False, deg_minus(2)),   # cum = 20 (40Ca Z=N=20)
    # Intruder from N_osc = 3 into K = 2 -> Magic 28
    ("1f_{7/2}", 3, 0, 3, 7, True, deg_plus(3)),     # cum = 28 (48Ca N=28, 56Ni Z=N=28)
    # Remaining N_osc = 3 states + Intruder 1g_{9/2} from N_osc = 4 -> Magic 50
    ("2p_{3/2}", 3, 1, 1, 3, True, deg_plus(1)),     # cum = 32
    ("1f_{5/2}", 3, 0, 3, 5, False, deg_minus(3)),   # cum = 38
    ("2p_{1/2}", 3, 1, 1, 1, False, deg_minus(1)),   # cum = 40
    ("1g_{9/2}", 4, 0, 4, 9, True, deg_plus(4)),     # cum = 50 (120Sn Z=50)
    # Remaining N_osc = 4 states + Intruder 1h_{11/2} from N_osc = 5 -> Magic 82
    ("1g_{7/2}", 4, 0, 4, 7, False, deg_minus(4)),   # cum = 58
    ("2d_{5/2}", 4, 1, 2, 5, True, deg_plus(2)),     # cum = 64
    ("2d_{3/2}", 4, 1, 2, 3, False, deg_minus(2)),   # cum = 68
    ("3s_{1/2}", 4, 2, 0, 1, True, deg_plus(0)),     # cum = 70 (120Sn N=70 subshell)
    ("1h_{11/2}", 5, 0, 5, 11, True, deg_plus(5)),   # cum = 82 (208Pb Z=82)
    # Remaining N_osc = 5 states + Intruder 1i_{13/2} from N_osc = 6 -> Magic 126
    ("1h_{9/2}", 5, 0, 5, 9, False, deg_minus(5)),   # cum = 92 (238U Z=92 subshell)
    ("2f_{7/2}", 5, 1, 3, 7, True, deg_plus(3)),     # cum = 100
    ("2f_{5/2}", 5, 1, 3, 5, False, deg_minus(3)),   # cum = 106
    ("3p_{3/2}", 5, 2, 1, 3, True, deg_plus(1)),     # cum = 110
    ("3p_{1/2}", 5, 2, 1, 1, False, deg_minus(1)),   # cum = 112
    ("1i_{13/2}", 6, 0, 6, 13, True, deg_plus(6)),   # cum = 126 (208Pb N=126)
    # Remaining N_osc = 6 states + Intruder 1j_{15/2} from N_osc = 7 -> Magic 184
    ("1i_{11/2}", 6, 0, 6, 11, False, deg_minus(6)), # cum = 138
    ("2g_{9/2}", 6, 1, 4, 9, True, deg_plus(4)),     # cum = 148 (238U N=146 near closure)
    ("2g_{7/2}", 6, 1, 4, 7, False, deg_minus(4)),   # cum = 156
    ("3d_{5/2}", 6, 2, 2, 5, True, deg_plus(2)),     # cum = 162
    ("3d_{3/2}", 6, 2, 2, 3, False, deg_minus(2)),   # cum = 166
    ("4s_{1/2}", 6, 3, 0, 1, True, deg_plus(0)),     # cum = 168
    ("1j_{15/2}", 7, 0, 7, 15, True, deg_plus(7)),   # cum = 184
]

BENCHMARK_NUCLEI: list[tuple[str, int, int]] = [
    ("4He", 2, 2),
    ("12C", 6, 6),
    ("16O", 8, 8),
    ("24Mg", 12, 12),
    ("28Si", 14, 14),
    ("40Ca", 20, 20),
    ("48Ca", 20, 28),
    ("56Ni", 28, 28),
    ("56Fe", 26, 30),
    ("120Sn", 50, 70),
    ("132Sn", 50, 82),
    ("197Au", 79, 118),
    ("208Pb", 82, 126),
    ("238U", 92, 146),
]


def _ame_sigma_total_mev(Z: int, A: int) -> mp.mpf:
    with mp.workdps(80):
        entry = _ame_entry(Z, A)
        unc_kev = entry.get("binding_energy_per_A_unc_keV")
        if unc_kev is None:
            return mp.mpf(0)
        return mp.mpf(repr(unc_kev)) * mp.mpf(A) / mp.mpf(1000)


def _derive_constants_at_q(q_val: mp.mpf) -> dict[str, mp.mpf]:
    """Derive all parameter-free QOU nuclear shell, spin-orbit, symmetry, and
    simplicial constants at a given substrate modulus `q_val` at 80 dps."""
    with mp.workdps(80):
        q = mp.mpf(q_val)
        qi = mp.mpf(1) / q
        h = q - qi
        hbar_q = (q - mp.mpf(1)) / q
        tower_resum = mp.mpf(1) / (mp.mpf(1) - hbar_q ** 2)
        me = mp.mpf(str(M_E_MEV))

        # Bare level-0 and tower-resummed Hecke energy scales (MeV)
        e0_bare = me / (q * (q - mp.mpf(1)))
        e0_inf = e0_bare * tower_resum

        # Convention-D Markov trace z_D and achiral gg crossing trace z_gg
        z_d = (q ** 3) / (q ** 2 + mp.mpf(1))
        z_gg = z_d - h / mp.mpf(2)

        # 2-body bond energies (MeV)
        b2_log_d = e0_bare * mp.log(mp.mpf(1) / z_d)
        b2_log_gg = e0_bare * mp.log(mp.mpf(1) / z_gg)
        b2_log_gg_inf = e0_inf * mp.log(mp.mpf(1) / z_gg)

        # GPMT H_3 / H_4 modified-dimension cumulants
        q2_1 = q ** 2 + mp.mpf(1)
        q4_1 = q ** 4 + mp.mpf(1)
        q4_2_1 = q ** 4 + q ** 2 + mp.mpf(1)
        h4_denom = (q2_1 ** 3) * q4_1 * q4_2_1

        d_mod_111 = -(q ** 3) / (q2_1 * q4_2_1)
        d_mod_211 = -(q ** 3) * q4_2_1 / ((q2_1 ** 3) * q4_1)
        d_mod_1111 = (q ** 7) / h4_denom

        mu3_gpmt = -d_mod_111
        s_row3_h4_4 = -mp.mpf(3) * d_mod_211 + d_mod_1111
        mu4_gpmt_h4 = s_row3_h4_4 - mp.mpf(4) * mu3_gpmt

        w3_gpmt_bare = e0_bare * mu3_gpmt
        w4_gpmt_bare = e0_bare * mu4_gpmt_h4
        w3_gpmt_inf = e0_inf * mu3_gpmt
        w4_gpmt_inf = e0_inf * mu4_gpmt_h4

        # Parameter-free Spin-Orbit coupling constant kappa_SO(q) from Reeb/Hecke commutator h*z_D/2
        # Dimensionless ratio Delta_SO / (hbar*omega_q * (2*l + 1)) = kappa_SO(q)
        kappa_so = h * z_d / mp.mpf(2)

        # Two parameter-free QOU oscillator / Fermi energy scale candidates (MeV):
        # Candidate I (Compton/Fermi shell quantum E_0 / hbar_q = m_e / (q - 1)^2 ≈ 42.273 MeV):
        #   Since lambda_bar_q = lambda_bar_e / (q - 1)^2, the Compton shell energy quantum is
        #   E_osc^{(I)}(q) = E_0^{(0)}(q) / hbar_q = m_e / (q - 1)^2 (42.273 MeV bare, 42.692 MeV tower-resummed),
        #   matching the textbook 41..43 MeV * A^{-1/3} harmonic-oscillator constant with ZERO free parameters.
        e_osc_compton_bare = e0_bare / hbar_q
        e_osc_compton_inf = e0_inf / hbar_q

        # Parameter-free Pauli/Fermi quadratic symmetry energy coefficients a_sym(q) in E_sym = a_sym * (N - Z)^2 / A:
        # Candidate A (Compton/Fermi shell scale): a_sym^{(I)}(q) = (E_0^{(0)} / hbar_q) * z_D / 2 ≈ 12.950 MeV
        #   (or with full z_D weight: (E_0^{(0)} / hbar_q) * z_D ≈ 25.900 MeV)
        a_sym_cand1 = (e0_bare / hbar_q) * z_d
        # Candidate B (Bare Hecke level-0 scale): a_sym^{(II)}(q) = E_0^{(inf)} * z_D / (1 + hbar_q^2) ≈ 2.565 MeV
        a_sym_cand2 = e0_inf * z_d / (mp.mpf(1) + hbar_q ** 2)

        return {
            "q": q,
            "qi": qi,
            "h": h,
            "hbar_q": hbar_q,
            "tower_resum_factor": tower_resum,
            "m_e_MeV": me,
            "E0_bare_MeV": e0_bare,
            "E0_inf_MeV": e0_inf,
            "E_osc_compton_bare_MeV": e_osc_compton_bare,
            "E_osc_compton_inf_MeV": e_osc_compton_inf,
            "z_D": z_d,
            "z_gg": z_gg,
            "b2_log_D_MeV": b2_log_d,
            "b2_log_gg_bare_MeV": b2_log_gg,
            "b2_log_gg_inf_MeV": b2_log_gg_inf,
            "mu3GPMT_H4": mu3_gpmt,
            "mu4GPMT_H4": mu4_gpmt_h4,
            "w3_GPMT_bare_MeV": w3_gpmt_bare,
            "w4_GPMT_H4_bare_MeV": w4_gpmt_bare,
            "w3_GPMT_inf_MeV": w3_gpmt_inf,
            "w4_GPMT_H4_inf_MeV": w4_gpmt_inf,
            "kappa_SO": kappa_so,
            "a_sym_cand1_MeV": a_sym_cand1,
            "a_sym_cand2_MeV": a_sym_cand2,
            "vol_coeff_3tree_gg_bare_MeV": mp.mpf(3) * b2_log_gg + mp.mpf(3) * w3_gpmt_bare + w4_gpmt_bare,
            "bdry_deficit_3tree_gg_bare_MeV": mp.mpf(6) * b2_log_gg + mp.mpf(8) * w3_gpmt_bare + mp.mpf(3) * w4_gpmt_bare,
            "vol_coeff_3tree_gg_inf_MeV": mp.mpf(3) * b2_log_gg_inf + mp.mpf(3) * w3_gpmt_inf + w4_gpmt_inf,
            "bdry_deficit_3tree_gg_inf_MeV": mp.mpf(6) * b2_log_gg_inf + mp.mpf(8) * w3_gpmt_inf + mp.mpf(3) * w4_gpmt_inf,
            "pauli_bridge_linear_deficit_per_D_MeV": mp.mpf(2) * b2_log_gg + mp.mpf(3) * w3_gpmt_bare + w4_gpmt_bare,
            "pauli_triangle_linear_deficit_per_D_MeV": b2_log_gg + mp.mpf(2) * w3_gpmt_bare + w4_gpmt_bare,
        }


def _single_particle_dimensionless_levels(
    kappa_so: mp.mpf, max_states: int = 184
) -> list[tuple[str, int, int, int, mp.mpf, mp.mpf, mp.mpf]]:
    """Expand `SPECTROSCOPIC_SUBSHELLS` into individual single-particle states up to `max_states`,
    sorted in energy-monotone order so that `fermi_asymmetry_promotion_nonneg` (`Monotone eps`)
    holds identically.
    Returns a list of tuples `(label, N_osc, ell, two_j, eps_ho_dimless, eps_so_nilsson_dimless, pure_ls_shift_dimless)` where:
      * `eps_ho_dimless = N_osc + 3/2` (pure 3D harmonic oscillator in units of `hbar*omega_q`,
        sorted by `N_osc`),
      * `eps_so_nilsson_dimless = (N_osc + 3/2) - kappa_SO * <2 l . s> - kappa_SO^2 * ell*(ell+1)/2`
        (Nilsson/Mayer-Jensen spin-orbit + centrifugal `-l^2` flattening, sorted monotonically
        by `eps_so_nilsson_dimless`),
      * `pure_ls_shift_dimless = kappa_SO * <2 l . s>` in spectroscopic filling order
        (whose sum over a closed spin-orbit pair `(2l+2)*l + 2l*(-(l+1))` is identically `0`)."""
    with mp.workdps(80):
        raw_so: list[tuple[mp.mpf, str, int, int, int]] = []
        raw_ho: list[tuple[mp.mpf, str, int, int, int]] = []
        raw_pure_ls: list[mp.mpf] = []
        for label, n_osc, _n_rad, ell, two_j, aligned_plus, deg in SPECTROSCOPIC_SUBSHELLS:
            eps_ho = mp.mpf(n_osc) + mp.mpf(3) / mp.mpf(2)
            two_l_dot_s = mp.mpf(ell) if aligned_plus else -mp.mpf(ell + 1)
            pure_ls = kappa_so * two_l_dot_s
            eps_so = (
                eps_ho
                - pure_ls
                - (kappa_so ** 2) * mp.mpf(ell * (ell + 1)) / mp.mpf(2)
            )
            for _m in range(deg):
                raw_so.append((eps_so, label, n_osc, ell, two_j))
                raw_ho.append((eps_ho, label, n_osc, ell, two_j))
                raw_pure_ls.append(pure_ls)
        raw_so.sort(key=lambda x: x[0])
        raw_ho.sort(key=lambda x: x[0])
        states: list[tuple[str, int, int, int, mp.mpf, mp.mpf, mp.mpf]] = []
        for i in range(min(max_states, len(raw_so))):
            eps_so, label, n_osc, ell, two_j = raw_so[i]
            eps_ho = raw_ho[i][0]
            states.append((label, n_osc, ell, two_j, eps_ho, eps_so, raw_pure_ls[i]))
        return states


def _smooth_weyl_fill_dimless(m_count: int) -> mp.mpf:
    """Smooth Thomas-Fermi / Weyl cumulative single-species 3D harmonic-oscillator
    energy (in units of `hbar*omega_q`) for `M` fermions.
    At exact oscillator shell closure `K`, `M = (K + 1)(K + 2)(K + 3) / 3 = (u^3 - u) / 3`
    where `u = K + 2`, and the exact discrete sum of `(N + 3/2)(N + 1)(N + 2)` over `N = 0..K`
    is `(3/4) * M * u = (3/4) * M * (K + 2)`, whereas at the midpoint of major shell `K + 1`
    the discrete sum exceeds `(3/4) * M * u` by `+(1/8) * (u^2 - 1)`.
    Inverting `3*M = u^3 - u` via `u = (3*M)^{1/3} + 1 / (3 * (3*M)^{1/3})` and centering the
    Weyl polynomial at the shell-oscillation mean `+(1/16) * (u^2 - 1)` yields a zero-centered
    shell correction `delta_Weyl_HO = E_smooth(M) - E_fill^{HO}(M)` that is positive at closed
    shells (`+ (u^2 - 1)/16`) and negative at mid-shells (`- (u^2 - 1)/16`):
    `E_smooth(M) = (3/4) * M * u + (1/16) * (u^2 - 1)`."""
    with mp.workdps(80):
        if m_count <= 0:
            return mp.mpf(0)
        m_mp = mp.mpf(m_count)
        u_0 = (mp.mpf(3) * m_mp) ** (mp.mpf(1) / mp.mpf(3))
        u_weyl = u_0 + mp.mpf(1) / (mp.mpf(3) * u_0)
        return (mp.mpf(3) / mp.mpf(4)) * m_mp * u_weyl + (mp.mpf(1) / mp.mpf(16)) * (u_0 ** 2 - mp.mpf(1))


def _shell_filling_observables(
    c: dict[str, mp.mpf],
    states: list[tuple[str, int, int, int, mp.mpf, mp.mpf, mp.mpf]],
    Z: int,
    N: int,
) -> dict[str, mp.mpf]:
    """Compute exact 80-dps discrete single-particle shell-filling energies,
    discrete Pauli Fermi-asymmetry promotion penalty, pure `l . s` spin-orbit gain,
    Nilsson centrifugal-inclusive spin-orbit gain, and smooth Weyl shell corrections
    for `(Z, N)`."""
    with mp.workdps(80):
        A = Z + N
        a_third = mp.mpf(A) ** (mp.mpf(1) / mp.mpf(3))
        # Two parameter-free QOU oscillator spacing candidates (MeV):
        # Candidate I: Compton/Fermi shell quantum (E_0^{(0)} / hbar_q) / A^{1/3} = (m_e / (q - 1)^2) / A^{1/3} = 42.24777 / A^{1/3} MeV
        # Candidate II: Hecke level-0 quantum E_0^{(inf)} / A^{1/3} = 4.22748 / A^{1/3} MeV (and bare 4.18598 / A^{1/3} MeV)
        hbar_omega_compton = c["E_osc_compton_bare_MeV"] / a_third
        hbar_omega_inf = c["E0_inf_MeV"] / a_third
        hbar_omega_bare = c["E0_bare_MeV"] / a_third

        # Cumulative dimensionless sums
        e_fill_z_so = mp.fsum(s[5] for s in states[:Z])
        e_fill_n_so = mp.fsum(s[5] for s in states[:N])
        e_fill_z_ho = mp.fsum(s[4] for s in states[:Z])
        e_fill_n_ho = mp.fsum(s[4] for s in states[:N])

        # Pure l.s lowering gain (vanishes identically at spin-saturated 4He, 16O, 40Ca)
        pure_ls_gain_z = mp.fsum(s[6] for s in states[:Z])
        pure_ls_gain_n = mp.fsum(s[6] for s in states[:N])
        pure_ls_gain_total = pure_ls_gain_z + pure_ls_gain_n

        # Balanced midpoint reference (exact half-integer interpolation if A is odd)
        m_half_low = A // 2
        m_half_high = A - m_half_low
        e_fill_mid_so = (
            mp.fsum(s[5] for s in states[:m_half_low])
            + mp.fsum(s[5] for s in states[:m_half_high])
        )
        e_fill_mid_ho = (
            mp.fsum(s[4] for s in states[:m_half_low])
            + mp.fsum(s[4] for s in states[:m_half_high])
        )

        # Discrete Pauli Fermi-asymmetry promotion penalty (in units of hbar*omega_q and in MeV)
        pauli_asym_dimless_so = (e_fill_z_so + e_fill_n_so) - e_fill_mid_so
        pauli_asym_dimless_ho = (e_fill_z_ho + e_fill_n_ho) - e_fill_mid_ho
        pauli_asym_so_mev_inf = pauli_asym_dimless_so * hbar_omega_inf
        pauli_asym_so_mev_bare = pauli_asym_dimless_so * hbar_omega_bare

        # Nilsson (l.s + centrifugal l(l+1)) lowering gain relative to pure HO
        so_gain_dimless_z = e_fill_z_ho - e_fill_z_so
        so_gain_dimless_n = e_fill_n_ho - e_fill_n_so
        so_gain_total_dimless = so_gain_dimless_z + so_gain_dimless_n

        # Smooth Weyl baseline vs discrete HO and SO sums (dimensionless & MeV)
        e_smooth_z = _smooth_weyl_fill_dimless(Z)
        e_smooth_n = _smooth_weyl_fill_dimless(N)
        delta_weyl_ho_dimless = (e_smooth_z - e_fill_z_ho) + (e_smooth_n - e_fill_n_ho)
        delta_weyl_so_dimless = (e_smooth_z - e_fill_z_so) + (e_smooth_n - e_fill_n_so)

        # Direct spin-orbit closure stabilization (MeV)
        delta_so_binding_compton_mev = so_gain_total_dimless * hbar_omega_compton
        delta_so_binding_inf_mev = so_gain_total_dimless * hbar_omega_inf
        delta_so_binding_bare_mev = so_gain_total_dimless * hbar_omega_bare

        return {
            "hbar_omega_compton_MeV": hbar_omega_compton,
            "hbar_omega_inf_MeV": hbar_omega_inf,
            "hbar_omega_bare_MeV": hbar_omega_bare,
            "E_fill_Z_SO_dimless": e_fill_z_so,
            "E_fill_N_SO_dimless": e_fill_n_so,
            "E_fill_total_SO_dimless": e_fill_z_so + e_fill_n_so,
            "E_fill_total_HO_dimless": e_fill_z_ho + e_fill_n_ho,
            "pauli_asym_SO_dimless": pauli_asym_dimless_so,
            "pauli_asym_HO_dimless": pauli_asym_dimless_ho,
            "pauli_asym_SO_compton_MeV": pauli_asym_dimless_so * hbar_omega_compton,
            "pauli_asym_SO_inf_MeV": pauli_asym_so_mev_inf,
            "pauli_asym_SO_bare_MeV": pauli_asym_so_mev_bare,
            "pure_ls_gain_Z_dimless": pure_ls_gain_z,
            "pure_ls_gain_N_dimless": pure_ls_gain_n,
            "pure_ls_gain_total_dimless": pure_ls_gain_total,
            "pure_ls_binding_compton_MeV": pure_ls_gain_total * hbar_omega_compton,
            "pure_ls_binding_inf_MeV": pure_ls_gain_total * hbar_omega_inf,
            "spin_orbit_gain_Z_dimless": so_gain_dimless_z,
            "spin_orbit_gain_N_dimless": so_gain_dimless_n,
            "spin_orbit_gain_total_dimless": so_gain_total_dimless,
            "delta_SO_binding_compton_MeV": delta_so_binding_compton_mev,
            "delta_SO_binding_inf_MeV": delta_so_binding_inf_mev,
            "delta_SO_binding_bare_MeV": delta_so_binding_bare_mev,
            "delta_Weyl_HO_shell_dimless": delta_weyl_ho_dimless,
            "delta_Weyl_HO_shell_compton_MeV": delta_weyl_ho_dimless * hbar_omega_compton,
            "delta_Weyl_shell_dimless": delta_weyl_so_dimless,
            "delta_Weyl_shell_compton_MeV": delta_weyl_so_dimless * hbar_omega_compton,
            "delta_Weyl_shell_inf_MeV": delta_weyl_so_dimless * hbar_omega_inf,
        }


def _err_metrics(b_pred: mp.mpf, b_ame: mp.mpf, sigma_ame: mp.mpf) -> dict[str, str]:
    delta = b_pred - b_ame
    ppq = delta / b_ame
    err_sig = (delta / sigma_ame) if sigma_ame > mp.mpf(0) else mp.mpf(0)
    return {
        "B_pred_MeV": fmt(b_pred),
        "delta_MeV": fmt(delta),
        "err_ppQ": fmt(ppq),
        "err_pct": fmt(ppq * mp.mpf(100)),
        "err_sigma": fmt(err_sig),
    }


def main() -> int:
    set_compute_dps(80)

    # Read both canonical q0 pins (proton and muon) plus 2-term Borromean root q_2t at 80 dps
    q_proton = q_at(80)
    q_muon = q_muon_at(80)
    q_2t = q_two_term_borromean_at(80)

    c_proton = _derive_constants_at_q(q_proton)
    c_muon = _derive_constants_at_q(q_muon)
    c_2t = _derive_constants_at_q(q_2t)

    states_proton = _single_particle_dimensionless_levels(c_proton["kappa_SO"], max_states=184)
    states_2t = _single_particle_dimensionless_levels(c_2t["kappa_SO"], max_states=184)

    wb = WitnessBuilder("nuclear-spin-orbit-shells-and-symmetry", engine="mpmath")
    wb.set_description(
        "80-dps first-principles evaluation of higher-l spin-orbit Pauli fiber "
        "multiplicities (2j+1), 3D harmonic-oscillator cumulative closures, Carbon-12 "
        "(Z=N=6) 1p_{3/2} subshell closure, universal Mayer-Jensen magic closures "
        "M_K = (K+1)(K+2)(K+3)/3 + (2K+4) in {28, 50, 82, 126, 184}, quadratic "
        "Fermi/Pauli symmetry energy E_sym propto (N-Z)^2/A, and spin-orbit shell "
        "corrections across 14 benchmark nuclei (4He to 238U). Zero fitting, zero float64."
    )
    wb.set_content_block("prop:spin-orbit-magic-closures")

    # 1. Exact Combinatorial & Magic-Closure Verification Table
    osc_table = []
    running_sum = 0
    for k_osc in range(7):
        deg_k = osc_shell_deg(k_osc)
        running_sum += deg_k
        closed_k = cum_osc_closure(k_osc)
        mj_k = mayer_jensen_magic(k_osc) if k_osc >= 2 else closed_k
        osc_table.append({
            "K": k_osc,
            "oscShellDeg": deg_k,
            "running_sum": running_sum,
            "cumOscClosure_formula": closed_k,
            "intruder_ell": (k_osc + 1) if k_osc >= 2 else 0,
            "intruder_degPlus": deg_plus(k_osc + 1) if k_osc >= 2 else 0,
            "mayerJensenMagic": mj_k,
        })

    wb.add_data("harmonic_oscillator_and_mayer_jensen_table", osc_table)

    # Verify subshell cumulative closures in SPECTROSCOPIC_SUBSHELLS
    subshell_closures: list[dict[str, object]] = []
    cum_occ = 0
    for label, n_osc, n_rad, ell, two_j, aligned_plus, deg in SPECTROSCOPIC_SUBSHELLS:
        cum_occ += deg
        subshell_closures.append({
            "subshell": label,
            "N_osc": n_osc,
            "n_radial": n_rad,
            "ell": ell,
            "two_j": two_j,
            "spin_aligned": aligned_plus,
            "degeneracy_2j_plus_1": deg,
            "cumulative_occupancy": cum_occ,
        })
    wb.add_data("spectroscopic_subshell_ladder", subshell_closures)

    wb.add_data(
        "substrate_constants_by_anchor",
        {
            "proton_pin": {k: fmt(v) for k, v in c_proton.items()},
            "muon_pin": {k: fmt(v) for k, v in c_muon.items()},
            "two_term_borromean_q2t": {k: fmt(v) for k, v in c_2t.items()},
        },
    )

    print("==========================================================================================================================================")
    print("  80-dps Higher-l Spin-Orbit Pauli Shells (2j+1), Mayer-Jensen Magic Closures & Quadratic Symmetry Energy Probe (Zero Float64)")
    print("==========================================================================================================================================")
    print("  1. Exact Mayer-Jensen Closed-Form Magic Sequence M_K = (K+1)(K+2)(K+3)/3 + (2K+4):")
    print("     K=0..2 harmonic-oscillator closures: " + str([cum_osc_closure(k) for k in (0, 1, 2)]))
    print("     Carbon-12 1s_{1/2} + 1p_{3/2} subshell closure: oscShellDeg(0) + degPlus(1) = " + str(osc_shell_deg(0) + deg_plus(1)))
    print("     K=2..6 Mayer-Jensen intruder closures: " + str([mayer_jensen_magic(k) for k in (2, 3, 4, 5, 6)]))
    print("  2. Parameter-Free QOU Nuclear Scales (Proton Pin vs 2-Term Borromean q_2t):")
    print("     E_0^{(0)} (bare)       = " + mp.nstr(c_proton["E0_bare_MeV"], 10) + " MeV  |  E_0^{(inf)} (resummed) = " + mp.nstr(c_proton["E0_inf_MeV"], 10) + " MeV")
    print("     kappa_SO = h*z_D/2     = " + mp.nstr(c_proton["kappa_SO"], 10) + "      |  a_sym^{(I)}(q0)        = " + mp.nstr(c_proton["a_sym_cand1_MeV"], 10) + " MeV")
    print("     a_sym^{(II)}(q0)       = " + mp.nstr(c_proton["a_sym_cand2_MeV"], 10) + " MeV  |  3-tree vol (gg,inf)    = " + mp.nstr(c_proton["vol_coeff_3tree_gg_inf_MeV"], 10) + " MeV/A")
    print("------------------------------------------------------------------------------------------------------------------------------------------")
    hdr = (
        f"{'Nucl':<6} {'Z':>3} {'N':>3} {'A':>3} {'D':>3} | "
        f"{'hw_q':>7} {'dSO_MeV':>8} {'Esym_P1':>8} {'Esym_Q1':>8} | "
        f"{'B_AME':>9} {'B_3t_P1':>9} {'B_3t_P2':>9} {'B_3t+Q1':>9} {'B_inf+Q1+SO':>11} {'err%':>7}"
    )
    print(hdr)
    print("-" * len(hdr))

    benchmark_rows: list[dict[str, object]] = []
    for name, Z, N in BENCHMARK_NUCLEI:
        A = Z + N
        D = abs(N - Z)
        b_ame = ame_binding_mev(Z, A)
        sigma_ame = _ame_sigma_total_mev(Z, A)
        e_c = coulomb_energy_mev(Z, A)

        f1_3t, f2_3t, f3_3t = f1_simplex(A), f2_simplex(A), f3_simplex(A)

        # Un-obstructed 3-tree strong simplicial core (bare and tower-resummed, achiral gg bond)
        b_simp_3t_bare = (
            mp.mpf(f1_3t) * c_proton["b2_log_gg_bare_MeV"]
            + mp.mpf(f2_3t) * c_proton["w3_GPMT_bare_MeV"]
            + mp.mpf(f3_3t) * c_proton["w4_GPMT_H4_bare_MeV"]
        )
        b_simp_3t_inf = (
            mp.mpf(f1_3t) * c_proton["b2_log_gg_inf_MeV"]
            + mp.mpf(f2_3t) * c_proton["w3_GPMT_inf_MeV"]
            + mp.mpf(f3_3t) * c_proton["w4_GPMT_H4_inf_MeV"]
        )
        b_simp_3t_2t_inf = (
            mp.mpf(f1_3t) * c_2t["b2_log_gg_inf_MeV"]
            + mp.mpf(f2_3t) * c_2t["w3_GPMT_inf_MeV"]
            + mp.mpf(f3_3t) * c_2t["w4_GPMT_H4_inf_MeV"]
        )

        # Linear s-wave 3-tree Pauli symmetry deficits (from AlphaSimplexCoordinationDerivation.lean)
        e_sym_linear_p1 = c_proton["pauli_bridge_linear_deficit_per_D_MeV"] * mp.mpf(D)
        e_sym_linear_p2 = c_proton["pauli_triangle_linear_deficit_per_D_MeV"] * mp.mpf(D)

        # Quadratic Fermi/Pauli symmetry energies E_sym = a_sym * (N - Z)^2 / A:
        #   a_sym_cand1 = (E_0^{(0)} / hbar_q) * z_D ≈ 25.900 MeV (Compton/Fermi shell scale)
        #   a_sym_cand2 = E_0^{(inf)} * z_D / (1 + hbar_q^2) ≈ 2.565 MeV (Hecke level-0 scale)
        d_sq_over_a = mp.mpf(D * D) / mp.mpf(A)
        e_sym_quad_cand1 = c_proton["a_sym_cand1_MeV"] * d_sq_over_a
        e_sym_quad_cand2 = c_proton["a_sym_cand2_MeV"] * d_sq_over_a
        e_sym_quad_2t = c_2t["a_sym_cand2_MeV"] * d_sq_over_a

        # Discrete single-particle shell filling & spin-orbit stabilization
        sh_p = _shell_filling_observables(c_proton, states_proton, Z, N)
        sh_2t = _shell_filling_observables(c_2t, states_2t, Z, N)

        # Model branches (all parameter-free, evaluated side-by-side):
        # Branch 1: s-wave Pauli Regime A (linear degree-1 bridge deficit)
        b_pred_p1 = b_simp_3t_bare - e_sym_linear_p1 - e_c
        # Branch 2: s-wave Pauli Regime B (linear degree-2 mixed-isospin triangle deficit)
        b_pred_p2 = b_simp_3t_bare - e_sym_linear_p2 - e_c
        # Branch 3: Bare 3-tree + Quadratic Pauli Symmetry Cand 1 (Compton/Fermi a_sym = 25.885 MeV) + Compton SO Gain
        b_pred_bare_q1 = b_simp_3t_bare - e_sym_quad_cand1 + sh_p["delta_SO_binding_compton_MeV"] - e_c
        # Branch 4: Tower-resummed 3-tree (E_0^{(inf)}) + Quadratic Pauli Symmetry Cand 1 (Compton/Fermi a_sym = 25.885 MeV) + Compton SO Gain
        b_pred_inf_q1_so = b_simp_3t_inf - e_sym_quad_cand1 + sh_p["delta_SO_binding_compton_MeV"] - e_c
        # Branch 5: Bare 3-tree + Quadratic Pauli Symmetry Cand 2 (Hecke level-0 a_sym = 2.565 MeV) + SO Gain
        b_pred_bare_q2_so = b_simp_3t_bare - e_sym_quad_cand2 + sh_p["delta_SO_binding_bare_MeV"] - e_c
        # Branch 6: Tower-resummed 3-tree (E_0^{(inf)}) + Quadratic Pauli Symmetry Cand 2 (Hecke level-0 a_sym = 2.565 MeV) + SO Gain
        b_pred_inf_q2_so = b_simp_3t_inf - e_sym_quad_cand2 + sh_p["delta_SO_binding_inf_MeV"] - e_c
        # Branch 7: Bare 3-tree + Discrete Single-Particle Pauli Promotion Penalty + SO Gain
        b_pred_bare_disc_so = (
            b_simp_3t_bare - sh_p["pauli_asym_SO_bare_MeV"] + sh_p["delta_SO_binding_bare_MeV"] - e_c
        )
        # Branch 8: 2-Term Borromean q_2t Tower-resummed 3-tree + Quadratic Pauli Symmetry Cand 2 + SO Gain
        b_pred_2t_inf_q2_so = (
            b_simp_3t_2t_inf - e_sym_quad_2t + sh_2t["delta_SO_binding_inf_MeV"] - e_c
        )

        err_pct_inf = ((b_pred_inf_q2_so - b_ame) / b_ame) * mp.mpf(100)
        print(
            f"{name:<6} {Z:>3} {N:>3} {A:>3} {D:>3} | "
            f"{mp.nstr(sh_p['hbar_omega_compton_MeV'], 5):>7} "
            f"{mp.nstr(sh_p['delta_SO_binding_compton_MeV'], 5):>8} "
            f"{mp.nstr(e_sym_linear_p1, 6):>8} "
            f"{mp.nstr(e_sym_quad_cand2, 6):>8} | "
            f"{mp.nstr(b_ame, 6):>9} "
            f"{mp.nstr(b_pred_p1, 6):>9} "
            f"{mp.nstr(b_pred_p2, 6):>9} "
            f"{mp.nstr(b_pred_bare_q1, 6):>9} "
            f"{mp.nstr(b_pred_inf_q2_so, 6):>11} "
            f"{mp.nstr(err_pct_inf, 4):>7}%"
        )

        benchmark_rows.append({
            "nuclide": name,
            "Z": Z,
            "N": N,
            "A": A,
            "N_minus_Z": N - Z,
            "B_AME_MeV": fmt(b_ame),
            "sigma_AME_MeV": fmt(sigma_ame),
            "E_C_MeV": fmt(e_c),
            "symmetry_energies_MeV": {
                "linear_pauli_bridge_P1_MeV": fmt(e_sym_linear_p1),
                "linear_pauli_triangle_P2_MeV": fmt(e_sym_linear_p2),
                "quadratic_pauli_compton_cand1_MeV": fmt(e_sym_quad_cand1),
                "quadratic_pauli_hecke_cand2_MeV": fmt(e_sym_quad_cand2),
                "discrete_shell_pauli_promotion_compton_MeV": fmt(sh_p["pauli_asym_SO_compton_MeV"]),
                "discrete_shell_pauli_promotion_inf_MeV": fmt(sh_p["pauli_asym_SO_inf_MeV"]),
                "discrete_shell_pauli_promotion_bare_MeV": fmt(sh_p["pauli_asym_SO_bare_MeV"]),
                "quadratic_compton_cand1_vs_linear_P1_gain_MeV": fmt(e_sym_linear_p1 - e_sym_quad_cand1),
                "quadratic_compton_cand1_vs_linear_P2_gain_MeV": fmt(e_sym_linear_p2 - e_sym_quad_cand1),
                "quadratic_hecke_cand2_vs_linear_P1_gain_MeV": fmt(e_sym_linear_p1 - e_sym_quad_cand2),
                "quadratic_hecke_cand2_vs_linear_P2_gain_MeV": fmt(e_sym_linear_p2 - e_sym_quad_cand2),
            },
            "shell_and_spin_orbit_observables": {
                k: fmt(v) for k, v in sh_p.items()
            },
            "branches": {
                "pauli_bridge_linear_3tree_bare": _err_metrics(b_pred_p1, b_ame, sigma_ame),
                "pauli_triangle_linear_3tree_bare": _err_metrics(b_pred_p2, b_ame, sigma_ame),
                "quadratic_sym_compton_cand1_plus_SO_3tree_bare": _err_metrics(b_pred_bare_q1, b_ame, sigma_ame),
                "quadratic_sym_compton_cand1_plus_SO_3tree_tower_resummed": _err_metrics(b_pred_inf_q1_so, b_ame, sigma_ame),
                "quadratic_sym_hecke_cand2_plus_SO_3tree_bare": _err_metrics(b_pred_bare_q2_so, b_ame, sigma_ame),
                "quadratic_sym_hecke_cand2_plus_SO_3tree_tower_resummed": _err_metrics(b_pred_inf_q2_so, b_ame, sigma_ame),
                "discrete_pauli_shell_plus_SO_3tree_bare": _err_metrics(b_pred_bare_disc_so, b_ame, sigma_ame),
                "q2t_quadratic_sym_hecke_cand2_plus_SO_3tree_tower_resummed": _err_metrics(b_pred_2t_inf_q2_so, b_ame, sigma_ame),
            },
        })

    wb.add_data("benchmark_nuclei", benchmark_rows)

    # ── Formal Assertions Verifying Every Lean 4 Theorem in SpinOrbitShellClosureAndSymmetryEnergy.lean ──

    # 1. `degPlus_add_degMinus` and `totalOrbitalSpinIsospinCap_eq` across l = 0..10
    subshell_sum_ok = all(
        (deg_plus(ell) + deg_minus(ell) == single_species_orbital_cap(ell))
        and (2 * (deg_plus(ell) + deg_minus(ell)) == total_orbital_spin_isospin_cap(ell))
        and (deg_plus(ell) - deg_minus(ell) == 2)
        for ell in range(11)
    )
    wb.add_assertion(
        name="spin_orbit_subshell_degeneracy_identities_2j_plus_1_exact",
        computed="1" if subshell_sum_ok else "0",
        expected="1",
        tolerance="0",
    )

    # 2. `cumOscClosure_eq_sum` and `cumOscClosure_values` (2, 8, 20, 40, 70, 112, 168)
    osc_expected = [2, 8, 20, 40, 70, 112, 168]
    osc_sum_ok = all(
        cum_osc_closure(k) == sum(osc_shell_deg(n) for n in range(k + 1)) == osc_expected[k]
        for k in range(7)
    )
    wb.add_assertion(
        name="harmonic_oscillator_tetrahedral_closures_2_8_20_40_70_112_168_exact",
        computed="1" if osc_sum_ok else "0",
        expected="1",
        tolerance="0",
    )

    # 3. `carbon12_and_oxygen16_shell_closures` (1s_{1/2}^2 + 1p_{3/2}^4 = 6 -> 12C; + 1p_{1/2}^2 = 8 -> 16O)
    c12_o16_ok = (
        (osc_shell_deg(0) + deg_plus(1) == 6)
        and (2 * (osc_shell_deg(0) + deg_plus(1)) == 12)
        and (osc_shell_deg(0) + deg_plus(1) + deg_minus(1) == cum_osc_closure(1) == 8)
        and (2 * cum_osc_closure(1) == 16)
    )
    wb.add_assertion(
        name="carbon12_1p3half_subshell_closure_6_and_oxygen16_closure_8_exact",
        computed="1" if c12_o16_ok else "0",
        expected="1",
        tolerance="0",
    )

    # 4. `mayerJensenMagic_values` and `mayerJensenMagic_mul_three_closed_form`:
    #    M_K = (K+1)(K+2)(K+3)/3 + (2K+4) in {28, 50, 82, 126, 184} for K = 2, 3, 4, 5, 6
    mj_expected = {2: 28, 3: 50, 4: 82, 5: 126, 6: 184}
    mj_ok = all(
        (mayer_jensen_magic(k) == val)
        and (3 * mayer_jensen_magic(k) == (k + 2) * (k * k + 4 * k + 9))
        and (mayer_jensen_magic(k + 1) - mayer_jensen_magic(k) == osc_shell_deg(k + 1) + 2)
        for k, val in mj_expected.items()
    )
    wb.add_assertion(
        name="mayer_jensen_magic_closed_form_28_50_82_126_184_exact",
        computed="1" if mj_ok else "0",
        expected="1",
        tolerance="0",
    )

    # 5. `quadratic_pauli_symmetry_energy_exact` & `fermi_asymmetry_promotion_nonneg`
    #    Verify that discrete Pauli promotion penalty is 0 for all N=Z nuclei, >= 0 for all
    #    N != Z nuclei (`fermi_asymmetry_promotion_nonneg`), and strictly > 0 whenever N and Z
    #    occupy distinct Mayer-Jensen shells (`120Sn`, `132Sn`, `197Au`, `208Pb`, `238U`).
    pauli_nonneg_ok = True
    for row in benchmark_rows:
        p_asym_so = mp.mpf(str(row["shell_and_spin_orbit_observables"]["pauli_asym_SO_dimless"]))
        p_asym_ho = mp.mpf(str(row["shell_and_spin_orbit_observables"]["pauli_asym_HO_dimless"]))
        if row["N_minus_Z"] == 0:
            if abs(p_asym_so) > mp.mpf("1e-70") or abs(p_asym_ho) > mp.mpf("1e-70"):
                pauli_nonneg_ok = False
        else:
            if p_asym_so < mp.mpf(0) or p_asym_ho < mp.mpf(0):
                pauli_nonneg_ok = False
            if row["A"] >= 50 and p_asym_so <= mp.mpf(0):
                pauli_nonneg_ok = False
            if row["A"] >= 130 and p_asym_ho <= mp.mpf(0):
                pauli_nonneg_ok = False
    wb.add_assertion(
        name="discrete_pauli_fermi_asymmetry_nonneg_and_strictly_pos_across_shells",
        computed="1" if pauli_nonneg_ok else "0",
        expected="1",
        tolerance="0",
    )

    # 6. Verify exact algebraic theorem `quadratic_pauli_symmetry_in_N_sub_Z`:
    #    4 * pauliAsymmetryPenalty(eps0 + i*Delta, M, d) == (N - Z)^2 * Delta on 208Pb (M=104, d=22, N-Z=44)
    m_pb = 104
    d_pb = 22
    eps0_test = c_proton["E0_bare_MeV"]
    delta_test = c_proton["kappa_SO"]
    fill_plus = mp.fsum(eps0_test + mp.mpf(i) * delta_test for i in range(m_pb + d_pb))
    fill_minus = mp.fsum(eps0_test + mp.mpf(i) * delta_test for i in range(m_pb - d_pb))
    fill_mid = mp.fsum(eps0_test + mp.mpf(i) * delta_test for i in range(m_pb))
    pauli_pen = fill_plus + fill_minus - mp.mpf(2) * fill_mid
    quad_rhs = (mp.mpf(2 * d_pb) ** 2) * delta_test
    wb.add_assertion(
        name="quadratic_pauli_symmetry_theorem_4_mul_penalty_eq_N_sub_Z_sq_exact",
        computed=fmt(abs(mp.mpf(4) * pauli_pen - quad_rhs)),
        expected="0",
        tolerance="1e-68",
    )

    # 7. First-principles algebraic verification of pure spin-orbit (`l . s`) cancellation
    #    on spin-saturated harmonic-oscillator major closures (`4He [Z=N=2]`, `16O [Z=N=8]`,
    #    `40Ca [Z=N=20]`) vs strict positivity on spin-unsaturated subshell/intruder closures
    #    (`12C [Z=N=6, 1p_{3/2}^4]`, `28Si [Z=N=14, 1d_{5/2}^6]`, `48Ca [N=28, 1f_{7/2}^8]`,
    #    `56Ni [Z=N=28]`, `132Sn [Z=50, N=82]`, `208Pb [Z=82, N=126]`):
    #    By `(2l + 2)*l + 2l*(-(l + 1)) = 0`, every completed `(j = l + 1/2, j = l - 1/2)`
    #    partner pair has zero net pure `l . s` shift, whereas every Mayer-Jensen intruder
    #    closure `M_K = cumOscClosure(K) + degPlus(K + 1)` carries excess positive lowering
    #    `degPlus(K + 1) * (K + 1) * kappa_SO = (2K + 4)(K + 1) * kappa_SO > 0`.
    saturated_zero_ok = all(
        abs(mp.mpf(str(next(r for r in benchmark_rows if r["nuclide"] == nuc)["shell_and_spin_orbit_observables"]["pure_ls_gain_total_dimless"])))
        < mp.mpf("1e-70")
        for nuc in ("4He", "16O", "40Ca")
    )
    intruder_pos_ok = all(
        mp.mpf(str(next(r for r in benchmark_rows if r["nuclide"] == nuc)["shell_and_spin_orbit_observables"]["pure_ls_gain_total_dimless"]))
        > mp.mpf(0)
        for nuc in ("12C", "28Si", "48Ca", "56Ni", "120Sn", "132Sn", "208Pb", "238U")
    )
    wb.add_assertion(
        name="pure_spin_orbit_ls_shift_vanishes_on_saturated_4He_16O_40Ca_and_pos_on_intruder_closures",
        computed="1" if (saturated_zero_ok and intruder_pos_ok) else "0",
        expected="1",
        tolerance="0",
    )

    out_path = wb.save(
        q0_comparison(
            muon=q_muon,
            proton=q_proton,
            reason=(
                "Evaluates parameter-free QOU nuclear spin-orbit shell closures, "
                "oscillator spacings, and quadratic Pauli symmetry energies across "
                "both the proton and muon q0 pins (plus the 2-term Borromean root q_2t) "
                "to verify cross-anchor stability of the Mayer-Jensen and symmetry-energy "
                "closure hierarchy."
            ),
        )
    )
    print("\n  Saved 80-dps witness -> " + str(out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
