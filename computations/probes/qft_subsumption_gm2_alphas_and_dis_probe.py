#!/usr/bin/env python3
"""qft_subsumption_gm2_alphas_and_dis_probe.py — 80-dps Perturbative QFT Subsumption
Probe: 12-Digit Electron (g-2)_e Rb-vs-Cs Comparison, 2-Loop Running Strong Coupling
alpha_s(Q^2) Across Quark Thresholds, & Borromean Proton DIS Valence Mellin Moments
(Zero Fitting, Zero Float64).

Companion to Lean 4 formalization:
  `folio/quantum-observable-universe/lean/QOU/StandardModel/InfraredQFTSubsumptionAndPartonMoments.lean`
  (`namespace QOU.StandardModel.InfraredQFTSubsumptionAndPartonMoments`).

PURPOSE & STRICT ANTI-FITTING DISCIPLINE
----------------------------------------
Evaluates at 80 decimal places (95 working guard digits, zero float64 intermediates,
zero `math` module imports, zero fitted parameters, zero CODATA-proximity assertions)
the interface between QOU's discrete ultraviolet topological spectral invariants and
standard continuum 3+1D perturbative quantum field theory:

1. **Part 1 — 12-Digit Electron Anomalous Magnetic Moment `a_e = (g-2)_e / 2` &
   Rubidium-2020 vs. Cesium-2018 Comparison (With Explicit Pin/Branch Uniqueness Audit)**:
   - Evaluates the exact analytical mass-independent QED universal coefficients at 80 dps:
       * `C_1 = 1/2` (Schwinger 1948),
       * `C_2 = 197/144 + pi^2/12 - (pi^2/2) ln 2 + (3/4) zeta(3)`
         (`-0.32847896557919378458...`, Petermann 1957; Sommerfield 1957),
       * `C_3 = 28259/5184 + (17101/810) pi^2 - (298/9) pi^2 ln 2 + (139/18) zeta(3)`
         `+ (100/3)(Li_4(1/2) + (1/24) ln^4 2 - (pi^2/24) ln^2 2) - (239/2160) pi^4`
         `+ (83/72) pi^2 zeta(3) - (215/24) zeta(5)`
         (`+1.18124145658720000627...`, Laporta & Remiddi 1996),
     together with the 4-loop and 5-loop universal coefficients `C_4 = -1.912245764926445574`
     (Laporta 2017) and `C_5 = 6.599` (Aoyama, Kinoshita, Nio 2019; Volkov 5-loop alternative
     `C_5_volkov = 5.891` also recorded transparently), the exact 80-dps 2-loop heavy-lepton
     vacuum polarization `a_e^{(2,VP)}(m_e / m_mu) = A_2^{(2)}(r) (alpha/pi)^2` evaluated via
     the closed-form rational power-logarithmic series
     `A_2^{(2)}(r) = sum_{n>=1} r^{2n} [-(8n^3 + 4n^2 - 32n - 25)/((n+2)^2 (2n+1)^2 (2n+3)^2) - (2(n-1)/((n+2)(2n+1)(2n+3))) ln(1/r)]`
     (cross-checked to `< 10^{-85}` against the 1D Feynman/dispersion integral) at QOU's
     parameter-free derived ratio `m_mu / m_e = Vol(4_1) / hbar_q^2`, and the published
     higher-loop lepton (`-0.05687e-12`) plus hadronic/electroweak (`+1.709e-12`) shifts.
   - Evaluates `a_e(alpha)` across all four QOU parameter-free `alpha_EM^{-1}` branches
     (`form_B_schwinger_cubic`, `form_A_bring_quadratic`, `form_tree_plus_zero_mode`,
     `one_term_chern_simons`) and across all three substrate pins (`q_0` 1-term proton,
     `q_2t` 2-term Borromean proton, `q_muon` ideal CAL-2 muon), comparing transparently
     side-by-side against:
       * Harvard 2023 measurement (Fan et al., PRL 130, 071801):
         `a_e^{exp} = 0.00115965218059(13)`,
       * Rubidium 2020 recoil `alpha_{Rb}^{-1} = 137.035999206(11)` (`-0.3596e-12 = -2.77 sigma`),
       * Cesium 2018 recoil `alpha_{Cs}^{-1} = 137.035999046(27)` (`+0.9924e-12 = +7.63 sigma`),
       * CODATA 2022 registry `alpha_{CODATA}^{-1} = 137.035999177(21)` (`-0.1146e-12 = -0.88 sigma`),
     and verifies the Planck-scale UV dipole suppression `(m_e / E_{Pl})^2 = 1.7518e-45 << 1.3e-13`.
   - **Explicit Anti-Cherry-Picking Audit (Two Open First-Principles Gaps)**:
     At the 1-term proton pin `q_0`, `form_B_schwinger_cubic` yields `alpha_EM^{-1}(q_0) = 137.035999127`
     (`a_e = 0.001159652180898`, `+2.372 sigma` vs. Harvard 2023, strictly between Rb-2020 and Cs-2018),
     whereas at QOU's QED-subtracted 2-term Borromean proton pin `q_2t` (`+11.17 ppb` above `q_0`)
     and ideal CAL-2 muon pin `q_muon` (`+11.61 ppb` above `q_0`), `form_B_schwinger_cubic` shifts
     by `+76.34 ppb` to `137.036009588` (`-677.5 sigma` on `a_e`) and `137.036010003` (`-704.5 sigma`).
     Selecting `form_B_schwinger_cubic` at `q_0` over `{form_A, form_B} x {q_0, q_2t, q_muon}`
     would constitute post-hoc branch/pin selection until two structural derivations are closed:
       * *Gap 1 (Dyson Uniqueness of Form B vs. Form A)*: Deriving why the 1PI Bring-Schwinger
         photon Dyson equation uniquely carries the Habiro self-dressing factor `(1 - h^2 alpha)`
         (`1/alpha = T + alpha H (1 - h^2 alpha)`, Form B) rather than the bare 1-loop self-energy
         (`1/alpha = T + alpha H`, Form A, which sits at `-9.73 sigma` even at `q_0`).
       * *Gap 2 (The `+76.34 ppb` `q_0 -> q_2t` Pin Shift & Missing 2-Loop QED Photon VP Scale)*:
         Because `d(1/alpha)/dq = +843.64` on `T(q) = q[9]_q[10]_q + 2/(3 pi)`, subtracting the
         proton's `+0.220 keV` Borromean `V^3` QED self-energy (`q_0 -> q_2t`) shifts `1/alpha` by
         `+0.000010461` (`+76.34 ppb`), exposing an un-derived `-1.046e-5 = -1.939 (alpha/pi)^2`
         (2-loop Schwinger-Jost-Luttinger `(alpha/pi)^2` photon vacuum-polarization / Bloch-group
         `Delta_2`) offset at the QED-subtracted substrate pin `q_2t`.

2. **Part 2 — Running Strong Coupling `alpha_s(Q^2)` Across Quark Thresholds to `M_Z` and `1 TeV`**:
   - Verifies the exact 1-loop and 2-loop SU(3)_c beta coefficients
     `b_0(n_f) = 11 - (2/3) n_f` (`9, 25/3, 23/3, 7` for `n_f = 3, 4, 5, 6`) and
     `b_1(n_f) = 102 - (38/3) n_f` (`64, 154/3, 116/3, 26`).
   - Integrates the exact 2-loop renormalization-group equation
     `d alpha_s / d ln Q^2 = -(b_0 / (4 pi)) alpha_s^2 - (b_1 / (4 pi)^2) alpha_s^3`
     via the exact implicit transcendental invariant
     `F(alpha_s; n_f) = (4 pi)/(b_0 alpha_s) - (b_1 / b_0^2) ln((4 pi)/(b_0 alpha_s) + b_1 / b_0^2) = ln(Q^2 / Lambda^2)`
     with continuous threshold matching at `m_c = 1.27 GeV`, `m_b = 4.18 GeV`, `m_t = 172.69 GeV`.
   - Reports transparently without cherry-picking all four natural QOU hadronic scales
     (`(3/2) m_pi = 209.36 MeV`, `m_p hbar_q [2]_q = 186.94 MeV`,
     `m_p / (8 G_Cat) = 128.04 MeV`, `m_p / Vol(4_1)^2 = 227.71 MeV`) under both 3-flavour
     (`Lambda^{(3)}`) and 5-flavour (`Lambda^{(5)}`) threshold interpretations at
     `Q = 2 GeV`, `m_b = 4.18 GeV`, `M_Z = 91.1876 GeV`, and `1000 GeV`, alongside the
     inverse check from PDG `alpha_s(M_Z) = 0.1180(9)` (`Lambda_{MSbar}^{(5)} = 211.89 MeV`,
     `Lambda_{MSbar}^{(3)} = 356.95 MeV`). Note candidly that a physical hadronic scale at
     `mu ~ 200 MeV` lives in the `n_f = 3` regime where empirical `Lambda_{MSbar}^{(3)} = 356.95 MeV`
     (giving `alpha_s(M_Z) = 0.1075` if `(3/2) m_pi` is identified directly with `Lambda^{(3)}`),
     whereas `(3/2) m_pi = 209.36 MeV` matches `Lambda_{MSbar}^{(5)} = 211.89 MeV`
     (`alpha_s(M_Z) = 0.1178`) only if the topological scale enters as the effective 5-flavour
     MSbar invariant above the `m_c, m_b` thresholds.

3. **Part 3 — Non-Perturbative Borromean Proton Valence Mellin Moments & 1-Loop DGLAP Evolution**:
   - Verifies the exact rational 1-loop non-singlet Mellin anomalous dimensions
     `gamma_n^{NS} = (4/3)(4 H_n - 3 - 2/(n(n+1)))` (`0, 32/9, 50/9, 314/45` for `n = 1, 2, 3, 4`).
   - Evaluates the parameter-free 3-strand Borromean proton `[u, u, d] in H_3(q)` valence
     momentum ratios at the hadronic scale `mu_0 = m_p` from the Jucys-Murphy spectrum `(1, q^2, q^4)`:
       * Branch A (Symmetric/Palindromic `d` on middle strand `q^2`):
         `<x>_{u_v} / <x>_{d_v} = (1 + q^4)/q^2 = q^2 + q^{-2} = 2 + h^2 = 2.04370620... > 2` at `q_0`
         (`2.04370621...` at `q_2t`),
       * Branch B (Ordered Jucys-Murphy `u, u` on `(q^2, q^4)`, `d` on `1`):
         `<x>_{u_v} / <x>_{d_v} = q^2 (1 + q^2) = 2.75000570...` at `q_0` (`2.75000579...` at `q_2t`),
       * Branch C (Symmetrized `u`-Swap Midpoint of Branches A and B):
         `<x>_{u_v} / <x>_{d_v} = (1/2)(q^2 + q^{-2} + q^2 + q^4) = 2.39685595...` at `q_0`
         (`2.39685600...` at `q_2t`, compared transparently against empirical DIS CT18 / NNPDF4.0 `~2.35-2.42`),
     and evolves the valence and singlet `(q_Sigma, g)` momentum and higher Mellin moments
     (`n = 2, 3, 4`) from `mu_0 = m_p` to `Q^2 = 4 GeV^2` (JLab/HERA), `Q^2 = 100 GeV^2`,
     and `Q^2 = M_Z^2` (LHC) across four parameter-free initial valence carry fractions
     (`M_2^{val}(mu_0) = z_D = q^3/(q^2+1)`, `M_2^{val}(mu_0) = 1/[2]_q = q/(q^2+1)`,
     `M_2^{val}(mu_0) = 3/5`, and `M_2^{val}(mu_0) = 1`). Note candidly that under the
     pure-valence initial condition `M_2^{sea}(mu_0) = 0`, the branch `M_2^{val}(mu_0) = 1/[2]_q = 0.4973`
     matches empirical valence moments at `Q^2 = 4 GeV^2` (`<x>_{u_v} = 0.3197`, `<x>_{d_v} = 0.1334`,
     `<x>_{u_v - d_v} = 0.1863`) while over-assigning the remaining neutral fraction to gluons
     (`<x>_g(4 GeV^2) = 0.5167` vs. CT18/NNPDF `0.41-0.47`), whereas `M_2^{val}(mu_0) = z_D = 0.6127`
     matches `<x>_g(4 GeV^2) = 0.4179` because `z_D - 1/[2]_q = 0.1154` approximates the
     non-perturbative primordial quark sea at `mu_0 = m_p`.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ["QOU_OUTPUT_DPS"] = "80"

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

from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_P_MEV_VALIDATION,
    M_PI_PM_MEV_VALIDATION,
)
from meson_em_sinh_closed_form import alpha_em_inv_derived  # noqa: E402
from q_parameter import q_at, q_muon_at, q_two_term_borromean_at  # noqa: E402
from qou_substrate import codata as _codata  # noqa: E402
from witness_base import WitnessBuilder, q0_comparison  # noqa: E402


# ── Section 0: Exact Quantum-Integer & Figure-Eight Volume Helpers ───────────
def q_int(n: int, q: mp.mpf) -> mp.mpf:
    """Balanced quantum integer [n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
    return (q ** n - q ** (-n)) / (q - mp.mpf(1) / q)


def vol_4_1_at_95dps() -> mp.mpf:
    """Hyperbolic volume of the figure-eight knot complement Vol(4_1) = 2 Im Li_2(e^{i pi/3})."""
    with mp.workdps(95):
        return mp.mpf(2) * mp.clsin(2, mp.pi / mp.mpf(3))


# ── Section 1: 12-Digit Electron (g-2)_e / 2 & Alpha_EM Branch Evaluator ─────
def compute_universal_qed_gm2_coefficients() -> dict[str, mp.mpf]:
    """Compute exact 80-dps analytical mass-independent QED coefficients C_1, C_2, C_3
    and record the published 4-loop (Laporta 2017) and 5-loop (Aoyama-Kinoshita-Nio 2019
    and Volkov 2019/2024) universal coefficients.
    """
    with mp.workdps(95):
        pi = mp.pi
        ln2 = mp.log(2)
        z2 = (pi ** 2) / mp.mpf(6)
        z3 = mp.zeta(3)
        z5 = mp.zeta(5)
        li4_half = mp.polylog(4, mp.mpf(1) / mp.mpf(2))

        c1 = mp.mpf(1) / mp.mpf(2)

        # Petermann (1957) & Sommerfield (1957) 2-loop universal coefficient:
        c2 = (
            mp.mpf(197) / mp.mpf(144)
            + (pi ** 2) / mp.mpf(12)
            - (pi ** 2) * ln2 / mp.mpf(2)
            + mp.mpf(3) * z3 / mp.mpf(4)
        )
        # Equivalent zeta(2) representation check:
        c2_zeta_form = (
            mp.mpf(197) / mp.mpf(144)
            + z2 / mp.mpf(2)
            - mp.mpf(3) * z2 * ln2
            + mp.mpf(3) * z3 / mp.mpf(4)
        )

        # Laporta & Remiddi (1996, Phys. Lett. B 379, 283) 3-loop universal coefficient:
        a4_comb = li4_half + (ln2 ** 4) / mp.mpf(24) - (pi ** 2) * (ln2 ** 2) / mp.mpf(24)
        c3 = (
            mp.mpf(28259) / mp.mpf(5184)
            + mp.mpf(17101) * (pi ** 2) / mp.mpf(810)
            - mp.mpf(298) * (pi ** 2) * ln2 / mp.mpf(9)
            + mp.mpf(139) * z3 / mp.mpf(18)
            + mp.mpf(100) * a4_comb / mp.mpf(3)
            - mp.mpf(239) * (pi ** 4) / mp.mpf(2160)
            + mp.mpf(83) * (pi ** 2) * z3 / mp.mpf(72)
            - mp.mpf(215) * z5 / mp.mpf(24)
        )
        # Alternative zeta(2), zeta(4) representation check for C_3:
        z4 = (pi ** 4) / mp.mpf(90)
        c3_zeta_form = (
            mp.mpf(28259) / mp.mpf(5184)
            + mp.mpf(17101) * z2 / mp.mpf(135)
            - mp.mpf(596) * z2 * ln2 / mp.mpf(3)
            + mp.mpf(139) * z3 / mp.mpf(18)
            + mp.mpf(100) * (li4_half + (ln2 ** 4) / mp.mpf(24) - z2 * (ln2 ** 2) / mp.mpf(4)) / mp.mpf(3)
            - mp.mpf(239) * z4 / mp.mpf(24)
            + mp.mpf(83) * z2 * z3 / mp.mpf(12)
            - mp.mpf(215) * z5 / mp.mpf(24)
        )

        # Laporta (2017, Phys. Lett. B 772, 232) 4-loop universal coefficient:
        c4 = mp.mpf("-1.912245764926445574")
        # Aoyama, Kinoshita, Nio (2019, Atoms 7, 28) & Volkov (2019/2024) 5-loop universal coefficients:
        c5_akn = mp.mpf("6.599")
        c5_volkov = mp.mpf("5.891")

        return {
            "C1": c1,
            "C2": c2,
            "C2_zeta_form": c2_zeta_form,
            "C3": c3,
            "C3_zeta_form": c3_zeta_form,
            "C4_laporta2017": c4,
            "C5_akn2019": c5_akn,
            "C5_volkov2024": c5_volkov,
        }


def compute_qou_alpha_em_inv_branches(q: mp.mpf) -> dict[str, mp.mpf]:
    """Compute all four parameter-free QOU inverse fine-structure constant branches at q:
      1. `form_B_schwinger_cubic`: 1/alpha = T + alpha H (1 - h^2 alpha),
      2. `form_A_bring_quadratic`: 1/alpha = T + alpha H,
      3. `form_tree_plus_zero_mode`: T = q [9]_q [10]_q + 2 / (3 pi),
      4. `one_term_chern_simons`: Chern-Simons Gram-determinant tower `alpha_em_inv_derived(q)`.
    """
    with mp.workdps(95):
        pi = mp.pi
        h = q - mp.mpf(1) / q
        h2 = h ** 2
        T = q * q_int(9, q) * q_int(10, q) + mp.mpf(2) / (mp.mpf(3) * pi)
        H = q_int(2, q) / (mp.mpf(8) * pi)

        # Form A positive root of H alpha^2 + T alpha - 1 = 0:
        alpha_A = (-T + mp.sqrt(T * T + mp.mpf(4) * H)) / (mp.mpf(2) * H)
        quad_res_A = H * (alpha_A ** 2) + T * alpha_A - mp.mpf(1)

        # Form B positive root of -H h^2 alpha^3 + H alpha^2 + T alpha - 1 = 0 via 95-dps Newton:
        alpha_B = alpha_A
        for _ in range(40):
            f_val = -H * h2 * (alpha_B ** 3) + H * (alpha_B ** 2) + T * alpha_B - mp.mpf(1)
            fp_val = -mp.mpf(3) * H * h2 * (alpha_B ** 2) + mp.mpf(2) * H * alpha_B + T
            step = f_val / fp_val
            alpha_B -= step
            if abs(step) < mp.mpf("1e-90"):
                break
        cubic_res_B = -H * h2 * (alpha_B ** 3) + H * (alpha_B ** 2) + T * alpha_B - mp.mpf(1)

        alpha_inv_cs = alpha_em_inv_derived(q)

        return {
            "form_B_schwinger_cubic": mp.mpf(1) / alpha_B,
            "form_A_bring_quadratic": mp.mpf(1) / alpha_A,
            "form_tree_plus_zero_mode": T,
            "one_term_chern_simons": alpha_inv_cs,
            "alpha_B": alpha_B,
            "alpha_A": alpha_A,
            "cubic_residual_B": cubic_res_B,
            "quadratic_residual_A": quad_res_A,
        }


def a2_heavy_lepton_vp_series_exact(r_val: mp.mpf, n_max: int = 25) -> mp.mpf:
    """Exact 80-dps closed-form power-logarithmic series for the 2-loop heavy-lepton
    vacuum-polarization kernel A_2^{(2)}(r) (r = m_e / m_mu < 1; Elend 1966;
    Lautrup & de Rafael 1968; Passera 2004):
      A_2^{(2)}(r) = sum_{n>=1} r^{2n} [ c_n + d_n ln(1/r) ],
    where for all n >= 1:
      c_n = -(8 n^3 + 4 n^2 - 32 n - 25) / ((n + 2)^2 (2n + 1)^2 (2n + 3)^2),
      d_n = -2 (n - 1) / ((n + 2) (2n + 1) (2n + 3)).
    At n = 1, 2, 3:
      c_1 = 1/45,        d_1 = 0,
      c_2 = 9/19600,     d_2 = -1/70,
      c_3 = -131/99225,  d_3 = -4/315.
    For r ~ 1/206.768, r^2 ~ 2.34e-5, so n_max = 25 converges to > 115 decimal places.
    """
    with mp.workdps(95):
        log_inv_r = mp.log(mp.mpf(1) / r_val)
        r2 = r_val * r_val
        r2n = mp.mpf(1)
        tot = mp.mpf(0)
        for n in range(1, n_max + 1):
            r2n *= r2
            num_c = -(8 * (n ** 3) + 4 * (n ** 2) - 32 * n - 25)
            den_c = ((n + 2) ** 2) * ((2 * n + 1) ** 2) * ((2 * n + 3) ** 2)
            c_n = mp.mpf(num_c) / mp.mpf(den_c)
            d_n = -mp.mpf(2 * (n - 1)) / mp.mpf((n + 2) * (2 * n + 1) * (2 * n + 3))
            tot += r2n * (c_n + d_n * log_inv_r)
        return tot


def a2_heavy_lepton_vp_feynman_quad(r_val: mp.mpf) -> mp.mpf:
    """Direct 1D Feynman/dispersion integral for A_2^{(2)}(r):
      A_2^{(2)}(r) = int_0^1 dx (1 - x) J(4 (1 - x) / (r^2 x^2)),
    where J(B) = int_0^1 dv v^2 (1 - v^2 / 3) / (1 + B - v^2)
               = sum_{m>=0} [2 (2m + 6) / (3 (2m + 3) (2m + 5))] / (B + 1)^{m + 1}.
    Used to cross-verify `a2_heavy_lepton_vp_series_exact` at 80+ dps.
    """
    with mp.workdps(95):
        def j_kernel(b_val: mp.mpf) -> mp.mpf:
            if b_val < mp.mpf(10):
                s_val = mp.mpf(1) + b_val
                sq = mp.sqrt(s_val)
                return (
                    b_val / mp.mpf(3)
                    - mp.mpf(5) / mp.mpf(9)
                    + (sq * (mp.mpf(2) - b_val) / mp.mpf(3)) * mp.log((sq + mp.mpf(1)) / mp.sqrt(b_val))
                )
            inv_s = mp.mpf(1) / (b_val + mp.mpf(1))
            p = inv_s
            acc = mp.mpf(0)
            for m in range(75):
                term = p * mp.mpf(2 * (2 * m + 6)) / mp.mpf(3 * (2 * m + 3) * (2 * m + 5))
                acc += term
                if term < acc * mp.mpf("1e-93"):
                    break
                p *= inv_s
            return acc

        r2 = r_val * r_val
        return mp.quad(
            lambda x: (mp.mpf(1) - x) * j_kernel(mp.mpf(4) * (mp.mpf(1) - x) / (r2 * x * x))
            if x > mp.mpf(0)
            else mp.mpf(0),
            [mp.mpf(0), mp.mpf(1)],
        )


def evaluate_ae_from_alpha_inv(
    alpha_inv: mp.mpf,
    q_for_muon_vp: mp.mpf,
    vol41: mp.mpf,
    coeffs: dict[str, mp.mpf],
) -> dict[str, mp.mpf]:
    """Evaluate a_e = (g-2)_e / 2 at 80 dps from `alpha_inv` across three transparent tiers:
      - `a_e_universal_5loop`: pure mass-independent 5-loop QED series,
      - `a_e_qed_with_qou_muon_vp`: + exact 80-dps 2-loop muon vacuum polarization evaluated
        at QOU's derived `m_mu / m_e = Vol(4_1) / hbar_q^2`,
      - `a_e_full_sm`: + higher-loop heavy-lepton QED (`-0.05687e-12`) + hadronic & electroweak
        (`+1.709e-12`) shifts (also reporting the Volkov 5-loop variant).
    """
    with mp.workdps(95):
        pi = mp.pi
        alpha = mp.mpf(1) / alpha_inv
        x = alpha / pi

        c1 = coeffs["C1"]
        c2 = coeffs["C2"]
        c3 = coeffs["C3"]
        c4 = coeffs["C4_laporta2017"]
        c5_akn = coeffs["C5_akn2019"]
        c5_vol = coeffs["C5_volkov2024"]

        term1 = c1 * x
        term2 = c2 * (x ** 2)
        term3 = c3 * (x ** 3)
        term4 = c4 * (x ** 4)
        term5_akn = c5_akn * (x ** 5)
        term5_vol = c5_vol * (x ** 5)

        univ_5loop = term1 + term2 + term3 + term4 + term5_akn
        univ_5loop_volkov = term1 + term2 + term3 + term4 + term5_vol

        # QOU parameter-free muon-to-electron mass ratio m_mu / m_e = Vol(4_1) / hbar_q^2:
        hbar_q = (q_for_muon_vp - mp.mpf(1)) / q_for_muon_vp
        m_mu_over_m_e_qou = vol41 / (hbar_q ** 2)
        r_mu = mp.mpf(1) / m_mu_over_m_e_qou

        # Exact 80-dps 2-loop heavy-lepton vacuum-polarization kernel A_2^{(2)}(r_mu):
        a2_mu_coeff = a2_heavy_lepton_vp_series_exact(r_mu, 25)
        a_e_2loop_mu_vp = a2_mu_coeff * (x ** 2)

        # Published 3+4-loop heavy-lepton QED shift & hadronic + electroweak shift (Aoyama-Kinoshita-Nio 2019):
        delta_ae_higher_lepton = mp.mpf("-0.05687e-12")
        delta_ae_had_ew = mp.mpf("1.709e-12")

        qed_with_qou_mu_vp = univ_5loop + a_e_2loop_mu_vp
        full_sm = qed_with_qou_mu_vp + delta_ae_higher_lepton + delta_ae_had_ew
        full_sm_volkov = univ_5loop_volkov + a_e_2loop_mu_vp + delta_ae_higher_lepton + delta_ae_had_ew

        return {
            "alpha_inv": alpha_inv,
            "alpha_over_pi": x,
            "term1_schwinger": term1,
            "term2_2loop_univ": term2,
            "term3_3loop_univ": term3,
            "term4_4loop_univ": term4,
            "term5_5loop_akn": term5_akn,
            "a_e_universal_5loop": univ_5loop,
            "a_e_2loop_qou_muon_vp": a_e_2loop_mu_vp,
            "a_e_qed_with_qou_muon_vp": qed_with_qou_mu_vp,
            "a_e_full_sm": full_sm,
            "a_e_full_sm_volkov5loop": full_sm_volkov,
        }


# ── Section 2: 2-Loop QCD Running Strong Coupling alpha_s(Q^2) ───────────────
def b0_qcd(nf: int) -> mp.mpf:
    """1-loop SU(3)_c QCD beta coefficient b_0(n_f) = 11 - (2/3) n_f."""
    return mp.mpf(11) - mp.mpf(2 * nf) / mp.mpf(3)


def b1_qcd(nf: int) -> mp.mpf:
    """2-loop SU(3)_c QCD beta coefficient b_1(n_f) = 102 - (38/3) n_f."""
    return mp.mpf(102) - mp.mpf(38 * nf) / mp.mpf(3)


def F_rge_2loop(alpha_s: mp.mpf, nf: int) -> mp.mpf:
    """Exact integrated 2-loop RGE invariant:
      F(alpha_s; n_f) = (4 pi)/(b_0 alpha_s) - (b_1 / b_0^2) ln((4 pi)/(b_0 alpha_s) + b_1 / b_0^2)
                      = ln(Q^2 / Lambda^2).
    """
    with mp.workdps(95):
        b0 = b0_qcd(nf)
        b1 = b1_qcd(nf)
        u = (mp.mpf(4) * mp.pi) / (b0 * alpha_s)
        c = b1 / (b0 ** 2)
        return u - c * mp.log(u + c)


def solve_alpha_s_2loop(target_F: mp.mpf, nf: int) -> mp.mpf:
    """80-dps Newton solver for alpha_s > 0 satisfying F_rge_2loop(alpha_s, nf) = target_F."""
    with mp.workdps(95):
        b0 = b0_qcd(nf)
        b1 = b1_qcd(nf)
        c = b1 / (b0 ** 2)
        u = target_F + c * mp.log(max(target_F, mp.mpf(2)))
        for _ in range(45):
            f_val = u - c * mp.log(u + c) - target_F
            fp_val = mp.mpf(1) - c / (u + c)
            step = f_val / fp_val
            u -= step
            if abs(step) < mp.mpf("1e-88"):
                break
        return (mp.mpf(4) * mp.pi) / (b0 * u)


def build_alpha_s_profile_from_lambda3(
    lam3_gev: mp.mpf,
    m_c_gev: mp.mpf,
    m_b_gev: mp.mpf,
    m_t_gev: mp.mpf,
) -> dict[str, mp.mpf]:
    """Construct a continuously threshold-matched 2-loop and 1-loop QCD alpha_s(Q) profile
    from a 3-flavour scale `lam3_gev` across `m_c`, `m_b`, `m_t`.
    """
    with mp.workdps(95):
        # 2-loop threshold matching:
        F3_mc = mp.mpf(2) * mp.log(m_c_gev / lam3_gev)
        as_mc_2l = solve_alpha_s_2loop(F3_mc, 3)
        F4_mc = F_rge_2loop(as_mc_2l, 4)
        lam4_gev = m_c_gev * mp.exp(-F4_mc / mp.mpf(2))

        F4_mb = F4_mc + mp.mpf(2) * mp.log(m_b_gev / m_c_gev)
        as_mb_2l = solve_alpha_s_2loop(F4_mb, 4)
        F5_mb = F_rge_2loop(as_mb_2l, 5)
        lam5_gev = m_b_gev * mp.exp(-F5_mb / mp.mpf(2))

        F5_mt = F5_mb + mp.mpf(2) * mp.log(m_t_gev / m_b_gev)
        as_mt_2l = solve_alpha_s_2loop(F5_mt, 5)
        F6_mt = F_rge_2loop(as_mt_2l, 6)
        lam6_gev = m_t_gev * mp.exp(-F6_mt / mp.mpf(2))

        return {
            "lam3_gev": lam3_gev,
            "lam4_gev": lam4_gev,
            "lam5_gev": lam5_gev,
            "lam6_gev": lam6_gev,
            "F3_mc": F3_mc,
            "F4_mc": F4_mc,
            "F4_mb": F4_mb,
            "F5_mb": F5_mb,
            "F5_mt": F5_mt,
            "F6_mt": F6_mt,
            "as_mc_2l": as_mc_2l,
            "as_mb_2l": as_mb_2l,
            "as_mt_2l": as_mt_2l,
        }


def build_alpha_s_profile_from_lambda5(
    lam5_gev: mp.mpf,
    m_c_gev: mp.mpf,
    m_b_gev: mp.mpf,
    m_t_gev: mp.mpf,
) -> dict[str, mp.mpf]:
    """Construct a continuously threshold-matched 2-loop QCD alpha_s(Q) profile anchored by
    a 5-flavour scale `lam5_gev` and matched downward across `m_b` and `m_c` and upward across `m_t`.
    """
    with mp.workdps(95):
        F5_mb = mp.mpf(2) * mp.log(m_b_gev / lam5_gev)
        as_mb_2l = solve_alpha_s_2loop(F5_mb, 5)
        F4_mb = F_rge_2loop(as_mb_2l, 4)
        lam4_gev = m_b_gev * mp.exp(-F4_mb / mp.mpf(2))

        F4_mc = F4_mb + mp.mpf(2) * mp.log(m_c_gev / m_b_gev)
        as_mc_2l = solve_alpha_s_2loop(F4_mc, 4)
        F3_mc = F_rge_2loop(as_mc_2l, 3)
        lam3_gev = m_c_gev * mp.exp(-F3_mc / mp.mpf(2))

        F5_mt = F5_mb + mp.mpf(2) * mp.log(m_t_gev / m_b_gev)
        as_mt_2l = solve_alpha_s_2loop(F5_mt, 5)
        F6_mt = F_rge_2loop(as_mt_2l, 6)
        lam6_gev = m_t_gev * mp.exp(-F6_mt / mp.mpf(2))

        return {
            "lam3_gev": lam3_gev,
            "lam4_gev": lam4_gev,
            "lam5_gev": lam5_gev,
            "lam6_gev": lam6_gev,
            "F3_mc": F3_mc,
            "F4_mc": F4_mc,
            "F4_mb": F4_mb,
            "F5_mb": F5_mb,
            "F5_mt": F5_mt,
            "F6_mt": F6_mt,
            "as_mc_2l": as_mc_2l,
            "as_mb_2l": as_mb_2l,
            "as_mt_2l": as_mt_2l,
        }


def eval_alpha_s_at_Q(
    profile: dict[str, mp.mpf],
    Q_gev: mp.mpf,
    m_c_gev: mp.mpf,
    m_b_gev: mp.mpf,
    m_t_gev: mp.mpf,
) -> dict[str, mp.mpf]:
    """Evaluate 2-loop and 1-loop continuously matched alpha_s(Q) at scale `Q_gev`."""
    with mp.workdps(95):
        pi = mp.pi
        lam3 = profile["lam3_gev"]
        F3_mc = profile["F3_mc"]
        as_1l_mc = (mp.mpf(4) * pi) / (b0_qcd(3) * F3_mc)
        as_1l_mb = mp.mpf(1) / (
            mp.mpf(1) / as_1l_mc
            + (b0_qcd(4) / (mp.mpf(4) * pi)) * mp.mpf(2) * mp.log(m_b_gev / m_c_gev)
        )
        as_1l_mt = mp.mpf(1) / (
            mp.mpf(1) / as_1l_mb
            + (b0_qcd(5) / (mp.mpf(4) * pi)) * mp.mpf(2) * mp.log(m_t_gev / m_b_gev)
        )

        if Q_gev <= m_c_gev:
            Fq = mp.mpf(2) * mp.log(Q_gev / lam3)
            as_2l = solve_alpha_s_2loop(Fq, 3)
            as_1l = (mp.mpf(4) * pi) / (b0_qcd(3) * Fq)
            nf = 3
        elif Q_gev <= m_b_gev:
            Fq = profile["F4_mc"] + mp.mpf(2) * mp.log(Q_gev / m_c_gev)
            as_2l = solve_alpha_s_2loop(Fq, 4)
            as_1l = mp.mpf(1) / (
                mp.mpf(1) / as_1l_mc
                + (b0_qcd(4) / (mp.mpf(4) * pi)) * mp.mpf(2) * mp.log(Q_gev / m_c_gev)
            )
            nf = 4
        elif Q_gev <= m_t_gev:
            Fq = profile["F5_mb"] + mp.mpf(2) * mp.log(Q_gev / m_b_gev)
            as_2l = solve_alpha_s_2loop(Fq, 5)
            as_1l = mp.mpf(1) / (
                mp.mpf(1) / as_1l_mb
                + (b0_qcd(5) / (mp.mpf(4) * pi)) * mp.mpf(2) * mp.log(Q_gev / m_b_gev)
            )
            nf = 5
        else:
            Fq = profile["F6_mt"] + mp.mpf(2) * mp.log(Q_gev / m_t_gev)
            as_2l = solve_alpha_s_2loop(Fq, 6)
            as_1l = mp.mpf(1) / (
                mp.mpf(1) / as_1l_mt
                + (b0_qcd(6) / (mp.mpf(4) * pi)) * mp.mpf(2) * mp.log(Q_gev / m_t_gev)
            )
            nf = 6

        roundtrip_err = abs(F_rge_2loop(as_2l, nf) - Fq)
        return {
            "alpha_s_2loop": as_2l,
            "alpha_s_1loop": as_1l,
            "roundtrip_F_err": roundtrip_err,
        }


# ── Section 3: Non-Perturbative Borromean Proton Valence Mellin Moments & DGLAP ──
def gamma_ns_1loop(n: int) -> mp.mpf:
    """Exact 1-loop QCD non-singlet Mellin anomalous dimension:
      gamma_n^{NS} = C_F (4 H_n - 3 - 2 / (n (n+1))),  C_F = 4/3.
    """
    with mp.workdps(95):
        cf = mp.mpf(4) / mp.mpf(3)
        hn = sum(mp.mpf(1) / mp.mpf(k) for k in range(1, n + 1))
        return cf * (mp.mpf(4) * hn - mp.mpf(3) - mp.mpf(2) / mp.mpf(n * (n + 1)))


def singlet_anomalous_matrix_n2(nf: int) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    """1-loop QCD singlet n=2 (momentum sum-rule) anomalous-dimension matrix entries:
      Gamma_2(n_f) = [[gamma_qq, gamma_qg], [gamma_gq, gamma_gg]]
                   = [[32/9, -2 n_f / 3], [-32/9, 2 n_f / 3]].
    """
    with mp.workdps(95):
        g_qq = mp.mpf(32) / mp.mpf(9)
        g_gq = -mp.mpf(32) / mp.mpf(9)
        g_qg = -mp.mpf(2 * nf) / mp.mpf(3)
        g_gg = mp.mpf(2 * nf) / mp.mpf(3)
        return g_qq, g_qg, g_gq, g_gg


def evolve_dglap_interval(
    moments_in: dict[str, mp.mpf],
    as_low: mp.mpf,
    as_high: mp.mpf,
    nf: int,
) -> dict[str, mp.mpf]:
    """Evolve non-singlet valence Mellin moments (n = 1, 2, 3, 4) and singlet (Sigma, g)
    momentum fractions (n = 2) across a single flavour threshold interval [mu_low, mu_high]
    with active flavour count `nf`.
    """
    with mp.workdps(95):
        b0 = b0_qcd(nf)
        ratio = as_high / as_low

        out: dict[str, mp.mpf] = {}
        for n in (1, 2, 3, 4):
            g_ns = gamma_ns_1loop(n)
            fac = ratio ** (g_ns / (mp.mpf(2) * b0))
            out[f"M{n}_uv"] = moments_in[f"M{n}_uv"] * fac
            out[f"M{n}_dv"] = moments_in[f"M{n}_dv"] * fac
            out[f"M{n}_uv_minus_dv"] = moments_in[f"M{n}_uv_minus_dv"] * fac
            out[f"M{n}_val_total"] = moments_in[f"M{n}_val_total"] * fac

        # Singlet n=2 2x2 matrix exponential evolution on (Sigma = val + sea, g):
        g_qq, _g_qg, _g_gq, g_gg = singlet_anomalous_matrix_n2(nf)
        lam_plus = g_qq + g_gg  # (32 + 6 n_f) / 9
        e_sing = ratio ** (lam_plus / (mp.mpf(2) * b0))

        sigma_old = moments_in["M2_val_total"] + moments_in["M2_sea"]
        g_old = moments_in["M2_g"]
        total_mom = sigma_old + g_old

        sigma_eq = total_mom * (mp.mpf(3 * nf) / mp.mpf(16 + 3 * nf))
        g_eq = total_mom * (mp.mpf(16) / mp.mpf(16 + 3 * nf))

        sigma_new = sigma_eq + (sigma_old - sigma_eq) * e_sing
        g_new = g_eq + (g_old - g_eq) * e_sing
        sea_new = sigma_new - out["M2_val_total"]

        out["M2_Sigma"] = sigma_new
        out["M2_sea"] = sea_new
        out["M2_g"] = g_new
        out["M2_total_momentum"] = sigma_new + g_new
        out["uv_over_dv_ratio_M2"] = out["M2_uv"] / out["M2_dv"]
        return out


def compute_borromean_initial_moments(
    q: mp.mpf,
    m2_val_init: mp.mpf,
    branch_mode: str,
) -> dict[str, mp.mpf]:
    """Construct the initial Mellin moments at the hadronic scale mu_0 = m_p for the 3-strand
    Borromean proton [u, u, d] in H_3(q) with multiplicative Jucys-Murphy weights (1, q^2, q^4):
      - `palindromic_d_middle`: d on q^2, u_1, u_2 on (1, q^4) -> u_v/d_v = (1 + q^4)/q^2 = 2 + h^2,
      - `ordered_d_first`: d on 1, u_1, u_2 on (q^2, q^4) -> u_v/d_v = q^2 (1 + q^2),
      - `symmetrized_midpoint`: equal-weight coherent average of the two u-d strand assignments.
    """
    with mp.workdps(95):
        w_tot = mp.mpf(1) + (q ** 2) + (q ** 4)
        x1 = m2_val_init * mp.mpf(1) / w_tot
        x2 = m2_val_init * (q ** 2) / w_tot
        x3 = m2_val_init * (q ** 4) / w_tot

        def moments_for_assignment(d_x: mp.mpf, u1_x: mp.mpf, u2_x: mp.mpf) -> dict[str, mp.mpf]:
            m_dict: dict[str, mp.mpf] = {
                "M1_uv": mp.mpf(2),
                "M1_dv": mp.mpf(1),
                "M1_uv_minus_dv": mp.mpf(1),
                "M1_val_total": mp.mpf(3),
            }
            for n in (2, 3, 4):
                p = n - 1
                m_uv = (u1_x ** p) + (u2_x ** p)
                m_dv = d_x ** p
                m_dict[f"M{n}_uv"] = m_uv
                m_dict[f"M{n}_dv"] = m_dv
                m_dict[f"M{n}_uv_minus_dv"] = m_uv - m_dv
                m_dict[f"M{n}_val_total"] = m_uv + m_dv
            return m_dict

        m_pal = moments_for_assignment(x2, x1, x3)
        m_ord = moments_for_assignment(x1, x2, x3)

        if branch_mode == "palindromic_d_middle":
            res = dict(m_pal)
        elif branch_mode == "ordered_d_first":
            res = dict(m_ord)
        elif branch_mode == "symmetrized_midpoint":
            # For n=2, the ratio r_mid = (1/2)*(r_pal + r_ord) with M2_uv + M2_dv = m2_val_init;
            # for n >= 3, arithmetic midpoint of the two strand assignments:
            r_pal = (mp.mpf(1) + (q ** 4)) / (q ** 2)
            r_ord = (q ** 2) * (mp.mpf(1) + (q ** 2))
            r_mid = (r_pal + r_ord) / mp.mpf(2)
            res = {
                "M1_uv": mp.mpf(2),
                "M1_dv": mp.mpf(1),
                "M1_uv_minus_dv": mp.mpf(1),
                "M1_val_total": mp.mpf(3),
                "M2_dv": m2_val_init / (mp.mpf(1) + r_mid),
                "M2_uv": m2_val_init * r_mid / (mp.mpf(1) + r_mid),
                "M2_uv_minus_dv": m2_val_init * (r_mid - mp.mpf(1)) / (mp.mpf(1) + r_mid),
                "M2_val_total": m2_val_init,
            }
            for n in (3, 4):
                for k in ("uv", "dv", "uv_minus_dv", "val_total"):
                    res[f"M{n}_{k}"] = (m_pal[f"M{n}_{k}"] + m_ord[f"M{n}_{k}"]) / mp.mpf(2)
        else:
            raise ValueError(f"Unknown branch_mode: {branch_mode}")

        res["M2_sea"] = mp.mpf(0)
        res["M2_g"] = mp.mpf(1) - m2_val_init
        res["M2_Sigma"] = m2_val_init
        res["M2_total_momentum"] = mp.mpf(1)
        res["uv_over_dv_ratio_M2"] = res["M2_uv"] / res["M2_dv"]
        return res


def evolve_moments_to_scales(
    init_moments: dict[str, mp.mpf],
    as_profile: dict[str, mp.mpf],
    m_p_gev: mp.mpf,
    m_c_gev: mp.mpf,
    m_b_gev: mp.mpf,
    m_t_gev: mp.mpf,
    M_Z_gev: mp.mpf,
) -> dict[str, dict[str, mp.mpf]]:
    """Evolve initial nucleon Mellin moments from `mu_0 = m_p` across thresholds `m_c` and `m_b`
    to `Q^2 = 4 GeV^2` (`Q = 2 GeV`), `Q^2 = 100 GeV^2` (`Q = 10 GeV`), and `Q^2 = M_Z^2`.
    """
    with mp.workdps(95):
        as_mp = eval_alpha_s_at_Q(as_profile, m_p_gev, m_c_gev, m_b_gev, m_t_gev)["alpha_s_2loop"]
        as_mc = as_profile["as_mc_2l"]
        as_2gev = eval_alpha_s_at_Q(as_profile, mp.mpf(2), m_c_gev, m_b_gev, m_t_gev)["alpha_s_2loop"]
        as_mb = as_profile["as_mb_2l"]
        as_10gev = eval_alpha_s_at_Q(as_profile, mp.mpf(10), m_c_gev, m_b_gev, m_t_gev)["alpha_s_2loop"]
        as_mz = eval_alpha_s_at_Q(as_profile, M_Z_gev, m_c_gev, m_b_gev, m_t_gev)["alpha_s_2loop"]

        # Step 1: m_p -> m_c (n_f = 3)
        at_mc = evolve_dglap_interval(init_moments, as_mp, as_mc, 3)
        # Step 2: m_c -> 2 GeV (n_f = 4, Q^2 = 4 GeV^2)
        at_q2_4 = evolve_dglap_interval(at_mc, as_mc, as_2gev, 4)
        # Step 3: 2 GeV -> m_b (n_f = 4)
        at_mb = evolve_dglap_interval(at_q2_4, as_2gev, as_mb, 4)
        # Step 4: m_b -> 10 GeV (n_f = 5, Q^2 = 100 GeV^2)
        at_q2_100 = evolve_dglap_interval(at_mb, as_mb, as_10gev, 5)
        # Step 5: 10 GeV -> M_Z (n_f = 5, Q^2 = M_Z^2)
        at_q2_mz2 = evolve_dglap_interval(at_q2_100, as_10gev, as_mz, 5)

        return {
            "mu0_mp": init_moments,
            "Q2_4GeV2": at_q2_4,
            "Q2_100GeV2": at_q2_100,
            "Q2_MZ2": at_q2_mz2,
        }


# ── Main Execution & Witness Emission ────────────────────────────────────────
def main() -> int:
    with mp.workdps(95):
        q0_proton = q_at(95)
        q0_2term = q_two_term_borromean_at(95)
        q0_muon = q_muon_at(95)
        vol41 = vol_4_1_at_95dps()
        vol_bor = mp.mpf(8) * mp.catalan

        print("=" * 138)
        print("  80-dps Perturbative QFT Subsumption Probe: 12-Digit (g-2)_e, 2-Loop alpha_s(Q^2), & Borromean Proton DIS Moments")
        print("=" * 138)

        # ── Part 1: (g-2)_e & Rb-2020 vs Cs-2018 Smoking-Gun Comparison ──
        coeffs = compute_universal_qed_gm2_coefficients()
        ae_harvard_2023 = mp.mpf("0.00115965218059")
        ae_harvard_sigma = mp.mpf("0.00000000000013")

        alpha_inv_rb2020 = mp.mpf("137.035999206")
        alpha_inv_rb_sigma = mp.mpf("0.000000011")
        alpha_inv_cs2018 = mp.mpf("137.035999046")
        alpha_inv_cs_sigma = mp.mpf("0.000000027")
        _alpha_inv_reg = _codata.codata("inverse fine-structure constant")
        alpha_inv_codata2022 = mp.mpf(_alpha_inv_reg.value_str)
        alpha_inv_codata_sigma = mp.mpf(_alpha_inv_reg.uncertainty_str)

        ext_benchmarks: dict[str, dict[str, str]] = {}
        for ext_name, ainv_val, ainv_sig in (
            ("Rb_2020_recoil", alpha_inv_rb2020, alpha_inv_rb_sigma),
            ("Cs_2018_recoil", alpha_inv_cs2018, alpha_inv_cs_sigma),
            ("CODATA_2022_registry", alpha_inv_codata2022, alpha_inv_codata_sigma),
        ):
            ev = evaluate_ae_from_alpha_inv(ainv_val, q0_proton, vol41, coeffs)
            diff_sm = ev["a_e_full_sm"] - ae_harvard_2023
            ext_benchmarks[ext_name] = {
                "alpha_inv": fmt(ainv_val),
                "alpha_inv_uncertainty": fmt(ainv_sig),
                "a_e_universal_5loop": fmt(ev["a_e_universal_5loop"]),
                "a_e_qed_with_qou_muon_vp": fmt(ev["a_e_qed_with_qou_muon_vp"]),
                "a_e_full_sm": fmt(ev["a_e_full_sm"]),
                "a_e_full_sm_volkov5loop": fmt(ev["a_e_full_sm_volkov5loop"]),
                "residual_vs_harvard2023": fmt(diff_sm),
                "residual_in_1e12": fmt(diff_sm * (mp.mpf(10) ** 12)),
                "sigma_vs_harvard2023": fmt(diff_sm / ae_harvard_sigma),
            }

        pins = {
            "proton_1term": q0_proton,
            "proton_2term_borromean": q0_2term,
            "muon_ideal_cal2": q0_muon,
        }
        qou_gm2_table: dict[str, dict[str, dict[str, str]]] = {}
        max_cubic_res = mp.mpf(0)
        max_quad_res = mp.mpf(0)

        print("  1. Universal Analytical QED Coefficients (80 dps):")
        print(f"     C_1 (Schwinger 1948)          = {mp.nstr(coeffs['C1'], 25)}")
        print(f"     C_2 (Petermann-Sommerfield)   = {mp.nstr(coeffs['C2'], 25)}")
        print(f"     C_3 (Laporta-Remiddi 1996)    = {mp.nstr(coeffs['C3'], 25)}")
        print(f"     C_4 (Laporta 2017)            = {mp.nstr(coeffs['C4_laporta2017'], 20)}")
        print(f"     C_5 (AKN 2019 / Volkov 2024)  = {mp.nstr(coeffs['C5_akn2019'], 6)} / {mp.nstr(coeffs['C5_volkov2024'], 6)}")
        print("-" * 138)
        print("  2. 12-Digit Electron a_e = (g-2)_e / 2 Across QOU alpha_EM^-1 Branches vs. Harvard-2023, Rb-2020, & Cs-2018:")
        for ext_name, edata in ext_benchmarks.items():
            print(
                f"     [EXT] {ext_name:22s} | 1/a = {edata['alpha_inv'][:16]} | "
                f"a_e(SM) = {edata['a_e_full_sm'][:18]} | "
                f"Delta = {edata['residual_in_1e12'][:8]}e-12 ({edata['sigma_vs_harvard2023'][:6]} sigma)"
            )

        for pin_name, q_val in pins.items():
            br = compute_qou_alpha_em_inv_branches(q_val)
            max_cubic_res = max(max_cubic_res, abs(br["cubic_residual_B"]))
            max_quad_res = max(max_quad_res, abs(br["quadratic_residual_A"]))
            qou_gm2_table[pin_name] = {}
            for bname in (
                "form_B_schwinger_cubic",
                "form_A_bring_quadratic",
                "form_tree_plus_zero_mode",
                "one_term_chern_simons",
            ):
                ainv = br[bname]
                ev = evaluate_ae_from_alpha_inv(ainv, q_val, vol41, coeffs)
                diff_sm = ev["a_e_full_sm"] - ae_harvard_2023
                diff_rb_ppb = (ainv - alpha_inv_rb2020) / alpha_inv_rb2020 * (mp.mpf(10) ** 9)
                diff_cs_ppb = (ainv - alpha_inv_cs2018) / alpha_inv_cs2018 * (mp.mpf(10) ** 9)
                diff_codata_ppb = (ainv - alpha_inv_codata2022) / alpha_inv_codata2022 * (mp.mpf(10) ** 9)
                qou_gm2_table[pin_name][bname] = {
                    "alpha_inv": fmt(ainv),
                    "alpha_inv_vs_rb2020_ppb": fmt(diff_rb_ppb),
                    "alpha_inv_vs_cs2018_ppb": fmt(diff_cs_ppb),
                    "alpha_inv_vs_codata2022_ppb": fmt(diff_codata_ppb),
                    "a_e_universal_5loop": fmt(ev["a_e_universal_5loop"]),
                    "a_e_2loop_qou_muon_vp": fmt(ev["a_e_2loop_qou_muon_vp"]),
                    "a_e_qed_with_qou_muon_vp": fmt(ev["a_e_qed_with_qou_muon_vp"]),
                    "a_e_full_sm": fmt(ev["a_e_full_sm"]),
                    "a_e_full_sm_volkov5loop": fmt(ev["a_e_full_sm_volkov5loop"]),
                    "residual_vs_harvard2023": fmt(diff_sm),
                    "residual_in_1e12": fmt(diff_sm * (mp.mpf(10) ** 12)),
                    "sigma_vs_harvard2023": fmt(diff_sm / ae_harvard_sigma),
                }
                print(
                    f"     [{pin_name:22s}] {bname:24s} | 1/a = {mp.nstr(ainv, 14):16s} | "
                    f"a_e(SM) = {mp.nstr(ev['a_e_full_sm'], 16):18s} | "
                    f"Delta = {mp.nstr(diff_sm * (mp.mpf(10) ** 12), 6):9s}e-12 "
                    f"({mp.nstr(diff_sm / ae_harvard_sigma, 5):7s} sigma)"
                )

        # Cross-verify 2-loop heavy-lepton VP series against 1D Feynman/dispersion integral:
        r_mu_q0 = mp.mpf(1) / (vol41 / (((q0_proton - mp.mpf(1)) / q0_proton) ** 2))
        a2_series_q0 = a2_heavy_lepton_vp_series_exact(r_mu_q0, 25)
        a2_quad_q0 = a2_heavy_lepton_vp_feynman_quad(r_mu_q0)
        a2_vp_quad_err = abs(a2_series_q0 - a2_quad_q0)

        # Explicit Pin & Branch Uniqueness Audit (Preventing Post-Hoc Cherry-Picking):
        br_q0 = compute_qou_alpha_em_inv_branches(q0_proton)
        br_q2t = compute_qou_alpha_em_inv_branches(q0_2term)
        br_qmu = compute_qou_alpha_em_inv_branches(q0_muon)

        dq_step = mp.mpf("1e-30")
        d_alpha_inv_dq = (
            compute_qou_alpha_em_inv_branches(q0_proton + dq_step)["form_B_schwinger_cubic"]
            - compute_qou_alpha_em_inv_branches(q0_proton - dq_step)["form_B_schwinger_cubic"]
        ) / (mp.mpf(2) * dq_step)

        shift_q0_to_q2t_q_ppb = (q0_2term - q0_proton) / q0_proton * (mp.mpf(10) ** 9)
        shift_q0_to_qmu_q_ppb = (q0_muon - q0_proton) / q0_proton * (mp.mpf(10) ** 9)
        shift_q0_to_q2t_alpha_inv = br_q2t["form_B_schwinger_cubic"] - br_q0["form_B_schwinger_cubic"]
        shift_q0_to_q2t_alpha_inv_ppb = (
            shift_q0_to_q2t_alpha_inv / br_q0["form_B_schwinger_cubic"] * (mp.mpf(10) ** 9)
        )
        shift_q0_to_qmu_alpha_inv = br_qmu["form_B_schwinger_cubic"] - br_q0["form_B_schwinger_cubic"]
        shift_q0_to_qmu_alpha_inv_ppb = (
            shift_q0_to_qmu_alpha_inv / br_q0["form_B_schwinger_cubic"] * (mp.mpf(10) ** 9)
        )
        alpha_over_pi_q2t_sq = (br_q2t["alpha_B"] / mp.pi) ** 2
        shift_q0_to_q2t_in_units_of_alpha_over_pi_sq = (
            -shift_q0_to_q2t_alpha_inv / alpha_over_pi_q2t_sq
        )
        rel_shift_q0_to_q2t_in_units_of_alpha_over_pi_sq = -shift_q0_to_q2t_alpha_inv / (
            br_q2t["form_B_schwinger_cubic"] * alpha_over_pi_q2t_sq
        )
        shift_formA_minus_formB_alpha_inv = (
            br_q0["form_A_bring_quadratic"] - br_q0["form_B_schwinger_cubic"]
        )

        pin_and_branch_uniqueness_audit = {
            "d_alpha_inv_dq_at_q0": fmt(d_alpha_inv_dq),
            "shift_q0_to_q2t_q_ppb": fmt(shift_q0_to_q2t_q_ppb),
            "shift_q0_to_qmu_q_ppb": fmt(shift_q0_to_qmu_q_ppb),
            "shift_q0_to_q2t_alpha_inv": fmt(shift_q0_to_q2t_alpha_inv),
            "shift_q0_to_q2t_alpha_inv_ppb": fmt(shift_q0_to_q2t_alpha_inv_ppb),
            "shift_q0_to_qmu_alpha_inv": fmt(shift_q0_to_qmu_alpha_inv),
            "shift_q0_to_qmu_alpha_inv_ppb": fmt(shift_q0_to_qmu_alpha_inv_ppb),
            "shift_q0_to_q2t_in_units_of_alpha_over_pi_sq": fmt(
                shift_q0_to_q2t_in_units_of_alpha_over_pi_sq
            ),
            "rel_shift_q0_to_q2t_in_units_of_alpha_over_pi_sq": fmt(
                rel_shift_q0_to_q2t_in_units_of_alpha_over_pi_sq
            ),
            "shift_formA_minus_formB_alpha_inv_at_q0": fmt(shift_formA_minus_formB_alpha_inv),
            "a2_heavy_lepton_vp_series_vs_quad_err": fmt(a2_vp_quad_err),
            "open_gap_1_dyson_uniqueness_form_B_vs_form_A": (
                "OPEN: Must derive from the 1PI Bring-Schwinger photon Dyson equation why "
                "the Habiro self-dressing factor (1 - h^2 alpha) in Form B (1/alpha = T + "
                "alpha H (1 - h^2 alpha), +2.37 sigma at q_0) is uniquely required over the "
                "bare 1-loop self-energy Form A (1/alpha = T + alpha H, -9.73 sigma at q_0)."
            ),
            "open_gap_2_q0_vs_q2t_pin_shift_and_2loop_photon_vp": (
                "OPEN: Moving from the 1-term proton pin q_0 (which absorbs the proton +0.220 keV "
                "Borromean V^3 QED self-energy) to the QED-subtracted 2-term Borromean proton pin "
                "q_2t (+11.17 ppb in q) or ideal CAL-2 muon pin q_muon (+11.61 ppb in q) shifts "
                "1/alpha_EM by +0.000010461 (+76.34 ppb, -677.5 sigma on a_e), exposing an "
                "un-derived -1.939 (alpha/pi)^2 (2-loop Schwinger-Jost-Luttinger photon vacuum "
                "polarization / Bloch-group Delta_2) offset at the canonical QED-subtracted pin."
            ),
        }
        print(
            f"     [AUDIT: Pin/Branch Gaps] d(1/a)/dq = +{mp.nstr(d_alpha_inv_dq, 6)} | "
            f"Delta(1/a)[q_0 -> q_2t] = +{mp.nstr(shift_q0_to_q2t_alpha_inv, 6)} "
            f"(+{mp.nstr(shift_q0_to_q2t_alpha_inv_ppb, 5)} ppb = "
            f"{mp.nstr(-shift_q0_to_q2t_in_units_of_alpha_over_pi_sq, 5)}*(a/pi)^2; "
            f"a_e shifts from +2.37 sigma at q_0 to -677.5 sigma at q_2t / -704.5 sigma at q_muon)"
        )
        print(
            f"     [AUDIT: Form-A vs Form-B] Form-A - Form-B at q_0 = +{mp.nstr(shift_formA_minus_formB_alpha_inv, 6)} "
            f"(Form-A = -9.73 sigma vs Form-B = +2.37 sigma at q_0; Dyson uniqueness & 2-loop VP scale remain open)"
        )

        # Planck-scale UV dipole suppression bound (m_e / E_Pl)^2:
        e_planck_mev = mp.mpf("1.220890e22")
        uv_planck_dipole_bound = (M_E_MEV / e_planck_mev) ** 2

        # ── Part 2: 2-Loop Running Strong Coupling alpha_s(Q^2) ──
        m_c_gev = mp.mpf("1.27")
        m_b_gev = mp.mpf("4.18")
        m_t_gev = mp.mpf("172.69")
        M_Z_gev = mp.mpf("91.1876")
        m_p_gev = M_P_MEV_VALIDATION / mp.mpf(1000)
        m_pi_gev = M_PI_PM_MEV_VALIDATION / mp.mpf(1000)

        hbar_q0 = (q0_proton - mp.mpf(1)) / q0_proton
        q_int2_0 = q_int(2, q0_proton)

        candidate_lambda_scales_gev = {
            "three_halves_m_pi": mp.mpf(3) * m_pi_gev / mp.mpf(2),
            "mp_hbar_q_qInt2": m_p_gev * hbar_q0 * q_int2_0,
            "mp_over_vol_borromean": m_p_gev / vol_bor,
            "mp_over_vol41_sq": m_p_gev / (vol41 ** 2),
        }

        qcd_beta_table = {
            f"nf_{nf}": {
                "b0": fmt(b0_qcd(nf)),
                "b1": fmt(b1_qcd(nf)),
            }
            for nf in (3, 4, 5, 6)
        }

        print("-" * 138)
        print("  3. 2-Loop Running Strong Coupling alpha_s(Q^2) Across Thresholds (m_c=1.27, m_b=4.18, m_t=172.69 GeV):")
        alpha_s_as_lambda3_table: dict[str, dict[str, str]] = {}
        alpha_s_as_lambda5_table: dict[str, dict[str, str]] = {}
        max_rge_roundtrip_err = mp.mpf(0)
        max_threshold_match_err = mp.mpf(0)

        for sname, lam_gev in candidate_lambda_scales_gev.items():
            # Interpretation A: candidate scale = 3-flavour Lambda^{(3)}
            prof3 = build_alpha_s_profile_from_lambda3(lam_gev, m_c_gev, m_b_gev, m_t_gev)
            # Verify continuous matching at m_c, m_b, m_t:
            err_mc = abs(solve_alpha_s_2loop(prof3["F3_mc"], 3) - solve_alpha_s_2loop(prof3["F4_mc"], 4))
            err_mb = abs(solve_alpha_s_2loop(prof3["F4_mb"], 4) - solve_alpha_s_2loop(prof3["F5_mb"], 5))
            err_mt = abs(solve_alpha_s_2loop(prof3["F5_mt"], 5) - solve_alpha_s_2loop(prof3["F6_mt"], 6))
            max_threshold_match_err = max(max_threshold_match_err, err_mc, err_mb, err_mt)

            ev_2gev = eval_alpha_s_at_Q(prof3, mp.mpf(2), m_c_gev, m_b_gev, m_t_gev)
            ev_mb = eval_alpha_s_at_Q(prof3, m_b_gev, m_c_gev, m_b_gev, m_t_gev)
            ev_mz = eval_alpha_s_at_Q(prof3, M_Z_gev, m_c_gev, m_b_gev, m_t_gev)
            ev_1tev = eval_alpha_s_at_Q(prof3, mp.mpf(1000), m_c_gev, m_b_gev, m_t_gev)
            max_rge_roundtrip_err = max(
                max_rge_roundtrip_err,
                ev_2gev["roundtrip_F_err"],
                ev_mb["roundtrip_F_err"],
                ev_mz["roundtrip_F_err"],
                ev_1tev["roundtrip_F_err"],
            )
            alpha_s_as_lambda3_table[sname] = {
                "Lambda3_MeV": fmt(lam_gev * mp.mpf(1000)),
                "Lambda4_MeV": fmt(prof3["lam4_gev"] * mp.mpf(1000)),
                "Lambda5_MeV": fmt(prof3["lam5_gev"] * mp.mpf(1000)),
                "alpha_s_2loop_2GeV": fmt(ev_2gev["alpha_s_2loop"]),
                "alpha_s_2loop_mb": fmt(ev_mb["alpha_s_2loop"]),
                "alpha_s_2loop_MZ": fmt(ev_mz["alpha_s_2loop"]),
                "alpha_s_2loop_1TeV": fmt(ev_1tev["alpha_s_2loop"]),
                "alpha_s_1loop_MZ": fmt(ev_mz["alpha_s_1loop"]),
            }
            print(
                f"     [as Lambda^(3)] {sname:22s}: Lam3={mp.nstr(lam_gev*1000, 6):7s} MeV (Lam5={mp.nstr(prof3['lam5_gev']*1000, 6):7s} MeV) -> "
                f"as(2GeV)={mp.nstr(ev_2gev['alpha_s_2loop'], 6)}, as(mb)={mp.nstr(ev_mb['alpha_s_2loop'], 6)}, "
                f"as(MZ)={mp.nstr(ev_mz['alpha_s_2loop'], 6)}, as(1TeV)={mp.nstr(ev_1tev['alpha_s_2loop'], 6)}"
            )

            # Interpretation B: candidate scale = 5-flavour Lambda^{(5)}
            prof5 = build_alpha_s_profile_from_lambda5(lam_gev, m_c_gev, m_b_gev, m_t_gev)
            ev5_2gev = eval_alpha_s_at_Q(prof5, mp.mpf(2), m_c_gev, m_b_gev, m_t_gev)
            ev5_mb = eval_alpha_s_at_Q(prof5, m_b_gev, m_c_gev, m_b_gev, m_t_gev)
            ev5_mz = eval_alpha_s_at_Q(prof5, M_Z_gev, m_c_gev, m_b_gev, m_t_gev)
            ev5_1tev = eval_alpha_s_at_Q(prof5, mp.mpf(1000), m_c_gev, m_b_gev, m_t_gev)
            alpha_s_as_lambda5_table[sname] = {
                "Lambda5_MeV": fmt(lam_gev * mp.mpf(1000)),
                "Lambda4_MeV": fmt(prof5["lam4_gev"] * mp.mpf(1000)),
                "Lambda3_MeV": fmt(prof5["lam3_gev"] * mp.mpf(1000)),
                "alpha_s_2loop_2GeV": fmt(ev5_2gev["alpha_s_2loop"]),
                "alpha_s_2loop_mb": fmt(ev5_mb["alpha_s_2loop"]),
                "alpha_s_2loop_MZ": fmt(ev5_mz["alpha_s_2loop"]),
                "alpha_s_2loop_1TeV": fmt(ev5_1tev["alpha_s_2loop"]),
                "alpha_s_1loop_MZ": fmt(ev5_mz["alpha_s_1loop"]),
            }
            print(
                f"     [as Lambda^(5)] {sname:22s}: Lam5={mp.nstr(lam_gev*1000, 6):7s} MeV (Lam3={mp.nstr(prof5['lam3_gev']*1000, 6):7s} MeV) -> "
                f"as(2GeV)={mp.nstr(ev5_2gev['alpha_s_2loop'], 6)}, as(mb)={mp.nstr(ev5_mb['alpha_s_2loop'], 6)}, "
                f"as(MZ)={mp.nstr(ev5_mz['alpha_s_2loop'], 6)}, as(1TeV)={mp.nstr(ev5_1tev['alpha_s_2loop'], 6)}"
            )

        # Inverse PDG reference check: alpha_s(M_Z) = 0.1180(9)
        as_mz_pdg = mp.mpf("0.1180")
        F5_mz_pdg = F_rge_2loop(as_mz_pdg, 5)
        lam5_pdg_gev = M_Z_gev * mp.exp(-F5_mz_pdg / mp.mpf(2))
        prof_pdg = build_alpha_s_profile_from_lambda5(lam5_pdg_gev, m_c_gev, m_b_gev, m_t_gev)
        print(
            f"     [PDG inverse]   alpha_s(M_Z)=0.1180(9) -> "
            f"Lam5_MSbar={mp.nstr(lam5_pdg_gev*1000, 7)} MeV, "
            f"Lam4_MSbar={mp.nstr(prof_pdg['lam4_gev']*1000, 7)} MeV, "
            f"Lam3_MSbar={mp.nstr(prof_pdg['lam3_gev']*1000, 7)} MeV"
        )

        # ── Part 3: Borromean Proton Valence Mellin Moments & 1-Loop DGLAP Evolution ──
        print("-" * 138)
        print("  4. Borromean Proton [u, u, d] in H_3(q) Valence Mellin Moments & 1-Loop DGLAP Evolution:")
        anomalous_dims_ns = {
            f"n_{n}": fmt(gamma_ns_1loop(n)) for n in (1, 2, 3, 4)
        }

        # Evaluate valence momentum ratios across all 3 substrate pins:
        valence_ratios_by_pin: dict[str, dict[str, str]] = {}
        max_laurent_identity_err = mp.mpf(0)
        max_zD_q2_identity_err = mp.mpf(0)

        for pin_name, q_val in pins.items():
            h_val = q_val - mp.mpf(1) / q_val
            r_pal = (mp.mpf(1) + (q_val ** 4)) / (q_val ** 2)
            r_pal_alt = mp.mpf(2) + (h_val ** 2)
            max_laurent_identity_err = max(max_laurent_identity_err, abs(r_pal - r_pal_alt))

            r_ord = (q_val ** 2) * (mp.mpf(1) + (q_val ** 2))
            r_mid = (r_pal + r_ord) / mp.mpf(2)
            r_mid_alt = mp.mpf(1) + (h_val ** 2) / mp.mpf(2) + (q_val ** 2) * (mp.mpf(1) + (q_val ** 2)) / mp.mpf(2)
            max_laurent_identity_err = max(max_laurent_identity_err, abs(r_mid - r_mid_alt))

            zD_val = (q_val ** 3) / ((q_val ** 2) + mp.mpf(1))
            inv_qInt2_val = mp.mpf(1) / q_int(2, q_val)
            max_zD_q2_identity_err = max(max_zD_q2_identity_err, abs(zD_val / (q_val ** 2) - inv_qInt2_val))

            valence_ratios_by_pin[pin_name] = {
                "palindromic_d_middle_2_plus_h2": fmt(r_pal),
                "ordered_d_first_q2_1_plus_q2": fmt(r_ord),
                "symmetrized_u_swap_midpoint": fmt(r_mid),
                "z_D_markov_weight": fmt(zD_val),
                "inv_qInt2_weight": fmt(inv_qInt2_val),
            }

        print(
            f"     Jucys-Murphy <x>_{{u_v}} / <x>_{{d_v}} at q_0: "
            f"palindromic (2+h^2) = {valence_ratios_by_pin['proton_1term']['palindromic_d_middle_2_plus_h2'][:10]}, "
            f"ordered q^2(1+q^2) = {valence_ratios_by_pin['proton_1term']['ordered_d_first_q2_1_plus_q2'][:10]}, "
            f"symmetrized midpoint = {valence_ratios_by_pin['proton_1term']['symmetrized_u_swap_midpoint'][:10]}"
        )

        # Evolve from mu_0 = m_p across four initial valence carry fractions M_2^{val}(mu_0)
        # using the parameter-free (3/2) m_pi 5-flavour profile (and also recording the (3/2) m_pi 3-flavour profile):
        zD_0 = (q0_proton ** 3) / ((q0_proton ** 2) + mp.mpf(1))
        inv_q2_0 = mp.mpf(1) / q_int(2, q0_proton)
        init_carry_branches = {
            "convention_D_markov_zD": zD_0,
            "borromean_inv_qInt2": inv_q2_0,
            "classical_equipartition_3_5": mp.mpf(3) / mp.mpf(5),
            "pure_valence_constituent_1": mp.mpf(1),
        }

        prof_for_dglap = build_alpha_s_profile_from_lambda5(
            candidate_lambda_scales_gev["three_halves_m_pi"], m_c_gev, m_b_gev, m_t_gev
        )

        dglap_evolution_table: dict[str, dict[str, dict[str, dict[str, str]]]] = {}
        max_momentum_sum_err = mp.mpf(0)
        max_adler_sum_err = mp.mpf(0)
        max_ratio_rg_invariance_err = mp.mpf(0)

        for cname, m2v0 in init_carry_branches.items():
            dglap_evolution_table[cname] = {}
            for bmode in ("palindromic_d_middle", "ordered_d_first", "symmetrized_midpoint"):
                init_m = compute_borromean_initial_moments(q0_proton, m2v0, bmode)
                ev_scales = evolve_moments_to_scales(
                    init_m, prof_for_dglap, m_p_gev, m_c_gev, m_b_gev, m_t_gev, M_Z_gev
                )
                r0 = init_m["uv_over_dv_ratio_M2"]
                dglap_evolution_table[cname][bmode] = {}
                for sc_key, mdict in ev_scales.items():
                    max_momentum_sum_err = max(
                        max_momentum_sum_err, abs(mdict["M2_total_momentum"] - mp.mpf(1))
                    )
                    max_adler_sum_err = max(
                        max_adler_sum_err,
                        abs(mdict["M1_uv"] - mp.mpf(2)),
                        abs(mdict["M1_dv"] - mp.mpf(1)),
                        abs(mdict["M1_uv_minus_dv"] - mp.mpf(1)),
                    )
                    max_ratio_rg_invariance_err = max(
                        max_ratio_rg_invariance_err,
                        abs(mdict["uv_over_dv_ratio_M2"] - r0),
                    )
                    dglap_evolution_table[cname][bmode][sc_key] = {
                        k: fmt(v) for k, v in mdict.items()
                    }

            # Print summary row for symmetrized_midpoint at Q^2 = 4 GeV^2 and Q^2 = M_Z^2:
            m_q4 = dglap_evolution_table[cname]["symmetrized_midpoint"]["Q2_4GeV2"]
            m_mz = dglap_evolution_table[cname]["symmetrized_midpoint"]["Q2_MZ2"]
            print(
                f"     [{cname:26s} | midpoint] "
                f"Q^2=4GeV^2: <x>_uv={m_q4['M2_uv'][:7]}, <x>_dv={m_q4['M2_dv'][:7]}, "
                f"<x>_(uv-dv)={m_q4['M2_uv_minus_dv'][:7]}, <x>_g={m_q4['M2_g'][:7]} | "
                f"Q^2=MZ^2: <x>_val={m_mz['M2_val_total'][:7]}, <x>_sea={m_mz['M2_sea'][:7]}, <x>_g={m_mz['M2_g'][:7]}"
            )

        # Singlet matrix column-sum and Gross-Wilczek fixed-point eigenvector verification:
        max_singlet_col_sum_err = mp.mpf(0)
        max_gw_fixed_point_err = mp.mpf(0)
        for nf in (3, 4, 5, 6):
            g_qq, g_qg, g_gq, g_gg = singlet_anomalous_matrix_n2(nf)
            max_singlet_col_sum_err = max(
                max_singlet_col_sum_err, abs(g_qq + g_gq), abs(g_qg + g_gg)
            )
            sig_eq = mp.mpf(3 * nf) / mp.mpf(16 + 3 * nf)
            g_eq = mp.mpf(16) / mp.mpf(16 + 3 * nf)
            max_gw_fixed_point_err = max(
                max_gw_fixed_point_err,
                abs(g_qq * sig_eq + g_qg * g_eq),
                abs(g_gq * sig_eq + g_gg * g_eq),
                abs(sig_eq + g_eq - mp.mpf(1)),
            )

        # ── Build Witness JSON ───────────────────────────────────────────────
        wb = WitnessBuilder("qft-subsumption-gm2-alphas-and-dis", engine="mpmath")
        wb.set_description(
            "80-dps Perturbative QFT Subsumption Probe (Zero Fitting, Zero Float64): "
            "(1) 12-digit electron anomalous magnetic moment a_e = (g-2)_e/2 from exact "
            "analytical universal QED coefficients (C_1, C_2, C_3) + 4/5-loop QED + QOU-derived "
            "2-loop muon vacuum polarization across all four QOU alpha_EM^-1 branches vs. "
            "Harvard-2023, Rubidium-2020, and Cesium-2018; (2) 2-loop running strong coupling "
            "alpha_s(Q^2) with continuous threshold matching across m_c, m_b, m_t from all "
            "four QOU hadronic candidate scales; and (3) non-perturbative 3-strand Borromean "
            "proton [u,u,d] in H_3(q) valence Mellin moments evolved via 1-loop non-singlet "
            "and singlet (q_Sigma, g) 2x2 matrix DGLAP equations from mu_0 = m_p to Q^2 = 4 GeV^2, "
            "100 GeV^2, and M_Z^2."
        )

        # 5 Exact Mathematical / RGE / Anomalous-Dimension Assertions (Zero CODATA-proximity assertions)
        c2_consistency = abs(coeffs["C2"] - coeffs["C2_zeta_form"])
        c3_consistency = abs(coeffs["C3"] - coeffs["C3_zeta_form"])
        wb.add_assertion(
            name="qed_universal_c1_c2_c3_exact_analytical_and_fixed_point_identities",
            computed="1"
            if (
                abs(coeffs["C1"] - mp.mpf(1) / mp.mpf(2)) < mp.mpf("1e-75")
                and coeffs["C2"] < mp.mpf(0)
                and mp.mpf(1) < coeffs["C3"] < mp.mpf(2)
                and c2_consistency < mp.mpf("1e-75")
                and c3_consistency < mp.mpf("1e-75")
                and max_cubic_res < mp.mpf("1e-75")
                and max_quad_res < mp.mpf("1e-75")
                and a2_vp_quad_err < mp.mpf("1e-80")
            )
            else "0",
            expected="1",
            tolerance="0",
        )

        wb.add_assertion(
            name="qcd_beta_b0_b1_and_2loop_implicit_rge_roundtrip_exact",
            computed="1"
            if (
                abs(b0_qcd(3) - mp.mpf(9)) < mp.mpf("1e-75")
                and abs(b0_qcd(4) - mp.mpf(25) / mp.mpf(3)) < mp.mpf("1e-75")
                and abs(b0_qcd(5) - mp.mpf(23) / mp.mpf(3)) < mp.mpf("1e-75")
                and abs(b0_qcd(6) - mp.mpf(7)) < mp.mpf("1e-75")
                and abs(b1_qcd(3) - mp.mpf(64)) < mp.mpf("1e-75")
                and abs(b1_qcd(4) - mp.mpf(154) / mp.mpf(3)) < mp.mpf("1e-75")
                and abs(b1_qcd(5) - mp.mpf(116) / mp.mpf(3)) < mp.mpf("1e-75")
                and abs(b1_qcd(6) - mp.mpf(26)) < mp.mpf("1e-75")
                and max_rge_roundtrip_err < mp.mpf("1e-75")
                and max_threshold_match_err < mp.mpf("1e-75")
            )
            else "0",
            expected="1",
            tolerance="0",
        )

        wb.add_assertion(
            name="dglap_1loop_nonsinglet_anomalous_dimensions_and_adler_sum_rule",
            computed="1"
            if (
                abs(gamma_ns_1loop(1) - mp.mpf(0)) < mp.mpf("1e-75")
                and abs(gamma_ns_1loop(2) - mp.mpf(32) / mp.mpf(9)) < mp.mpf("1e-75")
                and abs(gamma_ns_1loop(3) - mp.mpf(50) / mp.mpf(9)) < mp.mpf("1e-75")
                and abs(gamma_ns_1loop(4) - mp.mpf(314) / mp.mpf(45)) < mp.mpf("1e-75")
                and gamma_ns_1loop(1) < gamma_ns_1loop(2) < gamma_ns_1loop(3) < gamma_ns_1loop(4)
                and max_adler_sum_err < mp.mpf("1e-75")
            )
            else "0",
            expected="1",
            tolerance="0",
        )

        wb.add_assertion(
            name="dglap_1loop_singlet_momentum_conservation_and_gross_wilczek_fixed_point",
            computed="1"
            if (
                max_singlet_col_sum_err == mp.mpf(0)
                and max_gw_fixed_point_err < mp.mpf("1e-75")
                and max_momentum_sum_err < mp.mpf("1e-75")
            )
            else "0",
            expected="1",
            tolerance="0",
        )

        wb.add_assertion(
            name="borromean_jucys_murphy_valence_ratio_algebraic_identities_and_rg_invariance",
            computed="1"
            if (
                max_laurent_identity_err < mp.mpf("1e-75")
                and max_zD_q2_identity_err < mp.mpf("1e-75")
                and max_ratio_rg_invariance_err < mp.mpf("1e-75")
            )
            else "0",
            expected="1",
            tolerance="0",
        )

        wb.add_data(
            "part1_electron_gm2_and_rb_vs_cs",
            {
                "universal_qed_coefficients": {
                    k: fmt(v) for k, v in coeffs.items()
                },
                "harvard_2023_experiment": {
                    "a_e_exp": fmt(ae_harvard_2023),
                    "a_e_sigma": fmt(ae_harvard_sigma),
                    "reference": "Fan et al. (2023), Phys. Rev. Lett. 130, 071801",
                },
                "planck_uv_dipole_bound": {
                    "m_e_over_E_Pl_sq": fmt(uv_planck_dipole_bound),
                    "ratio_to_harvard_sigma": fmt(uv_planck_dipole_bound / ae_harvard_sigma),
                },
                "external_alpha_benchmarks": ext_benchmarks,
                "qou_alpha_em_branches_by_pin": qou_gm2_table,
                "pin_and_branch_uniqueness_audit": pin_and_branch_uniqueness_audit,
            },
        )
        wb.add_data(
            "part2_qcd_alpha_s_running",
            {
                "beta_coefficients": qcd_beta_table,
                "quark_thresholds_GeV": {
                    "m_c_GeV": fmt(m_c_gev),
                    "m_b_GeV": fmt(m_b_gev),
                    "m_t_GeV": fmt(m_t_gev),
                    "M_Z_GeV": fmt(M_Z_gev),
                },
                "qou_candidates_as_Lambda3": alpha_s_as_lambda3_table,
                "qou_candidates_as_Lambda5": alpha_s_as_lambda5_table,
                "pdg_inverse_reference": {
                    "alpha_s_MZ_pdg": fmt(as_mz_pdg),
                    "alpha_s_MZ_pdg_sigma": fmt(mp.mpf("0.0009")),
                    "Lambda5_MSbar_MeV": fmt(lam5_pdg_gev * mp.mpf(1000)),
                    "Lambda4_MSbar_MeV": fmt(prof_pdg["lam4_gev"] * mp.mpf(1000)),
                    "Lambda3_MSbar_MeV": fmt(prof_pdg["lam3_gev"] * mp.mpf(1000)),
                },
            },
        )
        wb.add_data(
            "part3_borromean_proton_dis_moments",
            {
                "nonsinglet_1loop_anomalous_dimensions": anomalous_dims_ns,
                "jucys_murphy_valence_ratios_by_pin": valence_ratios_by_pin,
                "dglap_evolved_moments_by_initial_carry_and_branch": dglap_evolution_table,
                "empirical_dis_and_lattice_reference_window_Q2_4GeV2": {
                    "uv_over_dv_ratio_CT18_NNPDF40": "2.35 to 2.42",
                    "M2_uv_CT18_NNPDF40": "0.305 to 0.320",
                    "M2_dv_CT18_NNPDF40": "0.127 to 0.135",
                    "M2_uv_minus_dv_Lattice_DIS": "0.175 to 0.188",
                    "M2_gluon_CT18_NNPDF40": "0.410 to 0.470",
                },
            },
        )
        wb.add_data(
            "methodology_note",
            (
                "UV-to-IR Division of Labour & Candid Open-Gap Accounting: QOU provides discrete "
                "ultraviolet spectral boundary conditions at the hadronic/threshold scale "
                "(alpha_EM^-1, m_mu/m_e, m_pi, m_p, and the 3-strand Borromean Jucys-Murphy "
                "strand weights in H_3(q)), while standard continuum 3+1D QED Schwinger-Petermann-"
                "Laporta series, 2-loop QCD beta-function evolution, and 1-loop Altarelli-Parisi "
                "(DGLAP) anomalous dimensions govern infrared momentum-scale running. No parameter "
                "is fitted; all candidate branches and pins are reported side-by-side alongside "
                "three explicit structural open gaps: "
                "(1) In Part 1, while Form-B (1/alpha = T + alpha H (1 - h^2 alpha)) at the 1-term "
                "proton pin q_0 yields alpha_EM^-1 = 137.035999127 (+2.37 sigma vs. Harvard 2023 "
                "a_e, strictly between Rb-2020 and Cs-2018), moving to the QED-subtracted 2-term "
                "Borromean proton pin q_2t (+11.17 ppb in q) or ideal CAL-2 muon pin q_muon (+11.61 "
                "ppb in q) shifts 1/alpha_EM by +0.000010461 (+76.34 ppb, -677.5 sigma on a_e) due "
                "to the tree-level sensitivity d(1/alpha)/dq = +843.64, exposing an un-derived "
                "-1.939 (alpha/pi)^2 (2-loop Schwinger-Jost-Luttinger photon vacuum-polarization / "
                "Bloch-group Delta_2) offset at q_2t as well as the open Dyson uniqueness proof "
                "selecting Form-B over bare Form-A (-9.73 sigma at q_0). "
                "(2) In Part 2, a physical hadronic scale at mu ~ 200 MeV resides in the n_f = 3 "
                "regime where empirical Lambda_{MSbar}^{(3)} = 356.95 MeV (so identifying (3/2) m_pi "
                "= 209.36 MeV with Lambda^{(3)} yields alpha_s(M_Z) = 0.1075), whereas (3/2) m_pi "
                "matches Lambda_{MSbar}^{(5)} = 211.89 MeV (alpha_s(M_Z) = 0.1178, -0.24 sigma from "
                "PDG 0.1180(9)) only under the 5-flavour threshold-matched MSbar identification. "
                "(3) In Part 3, under the pure-valence boundary assumption M_2^{sea}(mu_0) = 0, "
                "the initial carry M_2^{val}(mu_0) = 1/[2]_q = 0.4973 reproduces empirical DIS/lattice "
                "valence moments at Q^2 = 4 GeV^2 (<x>_{u_v} = 0.3197, <x>_{d_v} = 0.1334, "
                "<x>_{u_v - d_v} = 0.1863) while over-assigning the remaining neutral momentum to "
                "gluons (<x>_g(4 GeV^2) = 0.5167 vs. empirical 0.41-0.47), whereas M_2^{val}(mu_0) "
                "= z_D = 0.6127 reproduces <x>_g(4 GeV^2) = 0.4179 because z_D - 1/[2]_q = 0.1154 "
                "proxies the non-perturbative primordial quark sea at mu_0 = m_p."
            ),
        )

        out_path = wb.save(
            q0_comparison(
                muon=q0_muon,
                proton=q0_proton,
                reason=(
                    "Evaluates 12-digit electron (g-2)_e across QOU alpha_EM^-1 branches, "
                    "2-loop QCD running alpha_s(Q^2), and Borromean proton DIS valence Mellin "
                    "moments across 1-term proton (q_0), 2-term Borromean proton (q_2t), and "
                    "ideal CAL-2 muon (q_muon) pins."
                ),
                dps=70,
            )
        )
        print(f"\n  Saved 80-dps witness -> {out_path}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
