#!/usr/bin/env python3
"""truncation_level_vs_accuracy_sweep_probe.py — 80-dps Parameter-Free Measurement
of Truncation Level vs Experimental Accuracy (sigma_exp & ppQ) Across All QOU Towers
and Heavy-Nuclide (56Fe, 208Pb, 238U) Error Decomposition.

Measures at 80-dps mpmath precision (zero float64 intermediates, zero fitted
parameters) how increasing the truncation level changes accuracy relative to
experimental uncertainty sigma_exp (|err| / sigma_exp < 1.0 => strictly inside
experimental accuracy) and uniform ppQ = 10^{-15} across six QOU towers:

  Tower T0 — Energy Unit Geometric Tower E_0^(M) = (m_e / (q(q-1))) * sum_{m=0}^M hbar_q^{2m}:
             M = 0..8 vs exact closed form E_0^(inf) = m_e / ((q-1)^2 (q+1)).
  Tower T1 — Meson m_K / m_pi EM Logarithm Level L = 0..8 vs closed form 1 + ln(1 + hbar_q):
             crosses inside 1 sigma_exp at L = 0 and reaches 0.00195 sigma_exp (51.48 ppb).
  Tower T2 — Gauge Fixed-Point Loop Level L = 0..4 (Electroweak VEV v, G_F, and 1/alpha_EM):
             v and G_F cross strictly inside 1 sigma_exp at L = 3 (-0.115 sigma_exp) and
             settle at -0.114 sigma_exp (-29.37 ppb) at L = 4; 1/alpha_EM improves from
             10^7 sigma_exp (L=0) -> 200,000 sigma_exp (L=1) -> 6.48 sigma_exp (L=2) ->
             2.38 sigma_exp (L=3), sizing the missing L=4 two-loop O(alpha^2) term.
  Tower T3 — Q_beta & Neutron Mass m_n Habiro-Kashiwara + Mirror-Projected Phase + 2-Term QED:
             sweeps N = 0, 1, 2, 2+2tQED (with both unprojected alpha_D and mirror-covariant
             alpha_D^proj = alpha_D - h^2/4) and computes the exact u^N = (b hbar_q^2)^N
             truncation envelope for N = 3, 4, 5, 6 vs sigma_exp(Q_beta) and sigma_exp(m_n).
  Tower T4 — General-K GPMT Modified Quantum Dimensions on H_K(q) (K = 3..8):
             verifies the universal Ocneanu/Wenzl content-hook formula for w_lambda(q, z)
             and its exact z = z_D derivative d_D(S^lambda), revealing the simple-zero
             stratum for 3 <= K <= 7 and the onset of the second-order zero at cell (4,2)
             for K = 8 (partition (2,2,2,2)).
  Tower T5 — Nuclide Mass & Binding Sweep (2H..238U), Deuteron (2H) Level Sweep,
             Heavy-Nuclide (56Fe, 208Pb, 238U) Error Decomposition, and Exact 4x4 Hankel
             Determinant Identity for 4-Row SU(4) q-Plancherel Normalization Z_{3A}^{(4)}(q_0)
             evaluated for all nuclides up to 238U (n = 714 strands).

Run:
    python3 computations/probes/truncation_level_vs_accuracy_sweep_probe.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def comb(n: int, k: int) -> int:
    """Exact pure-integer binomial coefficient C(n, k) without importing math."""
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    num = 1
    den = 1
    for i in range(1, k + 1):
        num *= n - k + i
        den *= i
    return num // den

THIS = Path(__file__).resolve()
COMPUTE_DIR = THIS.parent.parent
sys.path.insert(0, str(COMPUTE_DIR))
sys.path.insert(0, str(COMPUTE_DIR / "substrate"))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402
from mpmath import mpf  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_P_MEV_VALIDATION,
    M_P_MEV_VALIDATION_ERR,
    M_N_MEV_VALIDATION,
    M_N_MEV_VALIDATION_ERR,
    Q_BETA_MEV,
    Q_BETA_MEV_ERR,
    M_K_PM_MEV_VALIDATION,
    M_PI_PM_MEV_VALIDATION,
)
from qou_substrate import codata as _codata  # noqa: E402
from meson_em_sinh_closed_form import alpha_em_inv_derived  # noqa: E402
from _li_2_q_util import li_2_q  # noqa: E402
from coulomb_energy import coulomb_energy_mev  # noqa: E402
from canonical_mass import (  # noqa: E402
    proton_neutron_mass_mev,
    neutron_mass_two_term_mev,
    np_qed_splitting_borromean_conn_mev,
    gpmt_dmod_111,
    gpmt_dmod_211,
    gpmt_dmod_1111,
)

set_compute_dps(80)


def q_bal(k: int, q: mpf) -> mpf:
    """Balanced quantum integer [k]_q = (q^k - q^{-k}) / (q - q^{-1})."""
    if k == 0:
        return mpf(0)
    return (q ** k - q ** (-k)) / (q - mpf(1) / q)


def q2_int(m: int, q: mpf) -> mpf:
    """Gaussian q^2-integer [m]_{q^2} = (q^{2m} - 1) / (q^2 - 1) for any integer m."""
    if m == 0:
        return mpf(0)
    return (q ** (2 * m) - mpf(1)) / (q ** 2 - mpf(1))


def partitions_of(n: int, max_part: int | None = None) -> list[tuple[int, ...]]:
    """All integer partitions of n in non-increasing order."""
    if max_part is None or max_part > n:
        max_part = n
    if n == 0:
        return [()]
    res: list[tuple[int, ...]] = []
    for first in range(max_part, 0, -1):
        for tail in partitions_of(n - first, first):
            res.append((first,) + tail)
    return res


def hook_lengths(lam: tuple[int, ...]) -> list[int]:
    """Hook lengths h(i, j) for all boxes (i, j) in Young diagram lam."""
    conj = []
    if lam:
        for j in range(lam[0]):
            conj.append(sum(1 for r in lam if r > j))
    hooks: list[int] = []
    for i, row_len in enumerate(lam):
        for j in range(row_len):
            hooks.append((row_len - j - 1) + (conj[j] - i - 1) + 1)
    return hooks


def specht_dim(lam: tuple[int, ...]) -> int:
    """Classical Specht dimension f^lambda = |lambda|! / prod h(box)."""
    n = sum(lam)
    num = 1
    for k in range(2, n + 1):
        num *= k
    den = 1
    for h in hook_lengths(lam):
        den *= h
    return num // den


def gpmt_zero_order_and_dmod_D(lam: tuple[int, ...], q: mpf) -> tuple[int, mpf]:
    """Return (zero_order_at_zD, first_order_dMod_at_zD) for any partition lam.

    At z_D = q^3 / (q^2 + 1), G_c(q, z_D) = [c + 2]_{q^2} / [2]_{q^2}, which vanishes
    if and only if c = j - i = -2 (cells (3,1), (4,2), (5,3), ...).
    - If zero_order == 0 (l(lam) <= 2): returns (0, w_lam(q, z_D)).
    - If zero_order == 1 (unique c = -2 cell (3,1)): returns (1, dw_lam/dz |_{z=z_D})
      via the exact algebraic product formula (zero numerical differentiation).
    - If zero_order >= 2 (e.g. (2,2,2,2) containing both (3,1) and (4,2)):
      dw_lam/dz |_{z=z_D} = 0 identically; returns (zero_order, mpf(0)).
    """
    K = sum(lam)
    cells = [(i, j, j - i) for i, r in enumerate(lam, start=1) for j in range(1, r + 1)]
    zero_cells = [cell for cell in cells if cell[2] == -2]
    z_ord = len(zero_cells)
    n_lam = sum(i * part for i, part in enumerate(lam))
    den = mpf(1)
    for h in hook_lengths(lam):
        den *= q2_int(h, q)
    two_q2 = q2_int(2, q)

    if z_ord == 0:
        prod_c = mpf(1)
        for _, _, c in cells:
            prod_c *= q2_int(c + 2, q) / two_q2
        return 0, (q ** (2 * n_lam)) * prod_c / den

    if z_ord == 1:
        prod_other = mpf(1)
        for _, _, c in cells:
            if c != -2:
                prod_other *= q2_int(c + 2, q)
        dmod = -(q ** (2 * n_lam - 3)) * prod_other / ((two_q2 ** (K - 2)) * den)
        return 1, dmod

    return z_ord, mpf(0)


def ground_state_su4_partition(Z: int, N: int, S_twice: int) -> tuple[int, ...]:
    """Canonical 4-row SU(4) spin-isospin ground-state partition of 3A quarks."""
    Nu = 2 * Z + N
    Nd = Z + 2 * N
    valid: list[tuple[int, ...]] = []
    for u_up in range(Nu + 1):
        u_dn = Nu - u_up
        for d_up in range(Nd + 1):
            d_dn = Nd - d_up
            if abs((u_up + d_up) - (u_dn + d_dn)) == S_twice:
                p = tuple(sorted([u_up, u_dn, d_up, d_dn], reverse=True))
                p = tuple(x for x in p if x > 0)
                if p not in valid:
                    valid.append(p)
    valid.sort(key=lambda p: (p[0], p))
    return valid[0]


def frobenius_plancherel_Z_bounded_rows(
    n: int, max_rows: int, q_int_tbl: list[mpf], q_fact_tbl: list[mpf]
) -> mpf:
    """Direct bounded-row q-Plancherel partition sum Z_n^{(r)}(q) = sum_{lam |- n, l(lam)<=r} W_lam(q)
    via the Frobenius shifted-part identity:
      prod_{box in lam} [h(box)]_q = (prod_{i=1}^r [l_i]_q!) / (prod_{1<=i<j<=r} [l_i - l_j]_q).
    """
    r = max_rows
    n_fact_q = q_fact_tbl[n]

    if r == 2:
        total = mpf(0)
        for lam2 in range(n // 2 + 1):
            lam1 = n - lam2
            l1, l2 = lam1 + 1, lam2
            vand_sq = q_int_tbl[l1 - l2] ** 2
            den_sq = (q_fact_tbl[l1] * q_fact_tbl[l2]) ** 2
            total += n_fact_q * vand_sq / den_sq
        return total

    if r == 3:
        total = mpf(0)
        for lam3 in range(n // 3 + 1):
            rem2 = n - 3 * lam3
            for d2 in range(rem2 // 2 + 1):
                lam2 = lam3 + d2
                lam1 = n - lam2 - lam3
                l1, l2, l3 = lam1 + 2, lam2 + 1, lam3
                vand = q_int_tbl[l1 - l2] * q_int_tbl[l1 - l3] * q_int_tbl[l2 - l3]
                den = q_fact_tbl[l1] * q_fact_tbl[l2] * q_fact_tbl[l3]
                total += n_fact_q * (vand / den) ** 2
        return total

    if r == 4:
        total = mpf(0)
        for lam4 in range(n // 4 + 1):
            rem3 = n - 4 * lam4
            for d3 in range(rem3 // 3 + 1):
                lam3 = lam4 + d3
                rem2 = rem3 - 3 * d3
                for d2 in range(rem2 // 2 + 1):
                    lam2 = lam3 + d2
                    lam1 = n - lam2 - lam3 - lam4
                    l1, l2, l3, l4 = lam1 + 3, lam2 + 2, lam3 + 1, lam4
                    vand = (
                        q_int_tbl[l1 - l2]
                        * q_int_tbl[l1 - l3]
                        * q_int_tbl[l1 - l4]
                        * q_int_tbl[l2 - l3]
                        * q_int_tbl[l2 - l4]
                        * q_int_tbl[l3 - l4]
                    )
                    den = q_fact_tbl[l1] * q_fact_tbl[l2] * q_fact_tbl[l3] * q_fact_tbl[l4]
                    total += n_fact_q * (vand / den) ** 2
        return total

    raise ValueError(f"Unsupported max_rows={max_rows}")


class Hankel4RowPlancherelEvaluator:
    """Exact polynomial-time O(N^2) evaluator for the 4-row SU(4) q-Plancherel
    normalization sum Z_n^{(4)}(q) via the Andréief / Cauchy-Binet 4x4 Hankel determinant:

      Z_n^{(4)}(q) = ([n]_q! / (q - q^{-1})^{12}) * [z^{n+6}] det_{0 <= j,k <= 3} (F_{j+k}(z; q)),

    where F_m(z; q) = sum_{l >= 0} (q^{(2m - 6) l} / ([l]_q!)^2) z^l for m = 0..6.
    """

    def __init__(self, n_max: int, q0: mpf, q_fact_tbl: list[mpf]) -> None:
        self.n_max = n_max
        self.N_max = n_max + 6
        self.q0 = q0
        self.h0 = q0 - mpf(1) / q0
        self.q_fact_tbl = q_fact_tbl

        N = self.N_max
        inv_fact_sq = [mpf(1) / (q_fact_tbl[l] ** 2) for l in range(N + 1)]
        F: list[list[mpf]] = [[mpf(0)] * (N + 1) for _ in range(7)]
        for m in range(7):
            alpha = 2 * m - 6
            q_alpha = q0 ** alpha
            p = mpf(1)
            Fm = F[m]
            for l in range(N + 1):
                Fm[l] = p * inv_fact_sq[l]
                p *= q_alpha

        self.pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
        self.comp = {
            (0, 1): (2, 3),
            (0, 2): (1, 3),
            (0, 3): (1, 2),
            (1, 2): (0, 3),
            (1, 3): (0, 2),
            (2, 3): (0, 1),
        }
        self.signs = {
            (0, 1): 1,
            (0, 2): -1,
            (0, 3): 1,
            (1, 2): 1,
            (1, 3): -1,
            (2, 3): 1,
        }

        needed: set[tuple[int, int]] = set()
        for a, b in self.pairs:
            for r, s in [(a, b + 1), (b, a + 1), (a + 2, b + 3), (b + 2, a + 3)]:
                needed.add((min(r, s), max(r, s)))

        # Since F_m[l] ~ q^{-l^2}, terms in F_r[i] * F_s[j] with |i - j| > 230
        # are suppressed by q^{-(i-j)^2/2} < q^{-26450} < 10^{-99} (identically zero at 80 dps).
        BAND = 235
        self.prods: dict[tuple[int, int], list[mpf]] = {}
        for r, s in sorted(needed):
            A = F[r]
            B = F[s]
            out = [mpf(0)] * (N + 1)
            for i in range(N + 1):
                ai = A[i]
                j_lo = max(0, i - BAND)
                j_hi = min(N - i, i + BAND)
                for j in range(j_lo, j_hi + 1):
                    out[i + j] += ai * B[j]
            self.prods[(r, s)] = out

    def eval_Z4(self, n: int) -> mpf:
        N = n + 6
        coeff_N = mpf(0)
        for a, b in self.pairs:
            c, d = self.comp[(a, b)]
            sgn = self.signs[(a, b)]
            P01_pos = self.prods[(min(a, b + 1), max(a, b + 1))]
            P01_neg = self.prods[(min(b, a + 1), max(b, a + 1))]
            P23_pos = self.prods[(min(c + 2, d + 3), max(c + 2, d + 3))]
            P23_neg = self.prods[(min(d + 2, c + 3), max(d + 2, c + 3))]
            dot = mpf(0)
            for k in range(N + 1):
                m01 = P01_pos[k] - P01_neg[k]
                m23 = P23_pos[N - k] - P23_neg[N - k]
                dot += m01 * m23
            if sgn == 1:
                coeff_N += dot
            else:
                coeff_N -= dot
        return self.q_fact_tbl[n] * coeff_N / (self.h0 ** 12)


def frobenius_W_lambda(
    lam: tuple[int, ...], q_int_tbl: list[mpf], q_fact_tbl: list[mpf]
) -> mpf:
    """Exact W_lambda(q) = [n]_q! / prod [h]_q^2 via Frobenius shifted parts for l(lam) <= 4."""
    n = sum(lam)
    padded = list(lam) + [0] * (4 - len(lam))
    l1, l2, l3, l4 = padded[0] + 3, padded[1] + 2, padded[2] + 1, padded[3]
    vand = (
        q_int_tbl[l1 - l2]
        * q_int_tbl[l1 - l3]
        * q_int_tbl[l1 - l4]
        * q_int_tbl[l2 - l3]
        * q_int_tbl[l2 - l4]
        * q_int_tbl[l3 - l4]
    )
    den = q_fact_tbl[l1] * q_fact_tbl[l2] * q_fact_tbl[l3] * q_fact_tbl[l4]
    return q_fact_tbl[n] * (vand / den) ** 2


def load_ame_nuclides() -> dict[tuple[int, int], dict[str, mpf]]:
    """Load AME2020 binding and atomic mass entries as exact mpmath numbers."""
    u_mev = mpf(_codata.codata("atomic mass constant energy equivalent in MeV").value_str)
    d = json.loads((COMPUTE_DIR / "data" / "ame2020.json").read_text())
    entries = d["entries"] if isinstance(d, dict) and "entries" in d else d
    rows = entries.values() if isinstance(entries, dict) else entries
    out: dict[tuple[int, int], dict[str, mpf]] = {}
    for r in rows:
        b_kev = r.get("binding_energy_total_keV")
        amu = r.get("atomic_mass_micro_u")
        if b_kev is None or amu is None:
            continue
        Z = int(r["Z"])
        A = int(r["A"])
        unc_b_per_a = mpf(str(r.get("binding_energy_per_A_unc_keV") or "0"))
        unc_amu = mpf(str(r.get("atomic_mass_unc_micro_u") or "0"))
        out[(Z, A)] = {
            "B_AME_MeV": mpf(str(b_kev)) / mpf(1000),
            "sigma_B_MeV": unc_b_per_a * mpf(A) / mpf(1000),
            "M_atom_AME_MeV": mpf(str(amu)) * mpf("1e-6") * u_mev,
            "sigma_M_MeV": unc_amu * mpf("1e-6") * u_mev,
        }
    return out


def electron_binding_mev_mp(Z: int, alpha_em: mpf, m_e: mpf) -> mpf:
    """Derived bare-Z hydrogenic electron shell binding in MeV (pure mpmath)."""
    ry_mev = (alpha_em ** 2) * m_e / mpf(2)
    total = mpf(0)
    n = 1
    left = Z
    while left > 0:
        k = min(2 * n * n, left)
        total += mpf(k * Z * Z) * ry_mev / mpf(n * n)
        left -= k
        n += 1
    return total


def main() -> int:
    q0 = mpf(Q_50_DIGIT_STR)
    qi = mpf(1) / q0
    h0 = q0 - qi
    hbar_q = (q0 - mpf(1)) / q0
    m_e = mpf(str(M_E_MEV))
    pi = mp.pi

    wb = WitnessBuilder("truncation-level-vs-accuracy-sweep", engine="mpmath")
    wb.set_description(
        "80-dps parameter-free measurement of truncation level vs experimental accuracy "
        "(sigma_exp multiples and ppQ = 1e-15) across all six QOU truncation towers "
        "(E_0 geometric tower, meson m_K/m_pi log tower, gauge fixed-point loop tower on "
        "v/G_F and 1/alpha_EM, Q_beta & m_n Habiro-Kashiwara + mirror-projected D-phase + "
        "2-term QED tower, general-K GPMT modified quantum dimensions K=3..8, and heavy "
        "nuclide 56Fe/208Pb/238U error decomposition with exact 4x4 Hankel determinant "
        "4-row SU(4) q-Plancherel normalization Z_{3A}^{(4)}(q_0))."
    )

    # =========================================================================
    # TOWER T0: E_0^(M) = (m_e / (q(q-1))) * sum_{m=0}^M hbar_q^{2m}
    # =========================================================================
    E0_base = m_e / (q0 * (q0 - mpf(1)))
    E0_exact = (m_e * q0) / ((q0 - mpf(1)) * (mpf(2) * q0 - mpf(1)))
    t0_rows = []
    for M in range(9):
        E0_M = E0_base * sum(hbar_q ** (2 * m) for m in range(M + 1))
        rel_ppq = (E0_M - E0_exact) / E0_exact * mpf("1e15")
        t0_rows.append({
            "level_M": M,
            "E0_M_MeV": fmt(E0_M),
            "trunc_err_ppQ": fmt(rel_ppq),
        })
    wb.add_assertion(
        name="T0_E0_geometric_closed_form_identity",
        computed=fmt(E0_base / (mpf(1) - hbar_q ** 2)),
        expected=fmt(E0_exact),
        tolerance="1e-65",
        source="E_0^(0) / (1 - hbar_q^2) == m_e * q / ((q-1)(2q-1))",
    )

    # =========================================================================
    # TOWER T1: Meson m_K / m_pi Logarithm Level L = 0..8, inf
    # =========================================================================
    alpha_inv_cs = alpha_em_inv_derived(q0, order=None)
    alpha_cs = mpf(1) / alpha_inv_cs
    r_kpi_exp = mpf(str(M_K_PM_MEV_VALIDATION)) / mpf(str(M_PI_PM_MEV_VALIDATION))
    r_kpi_sig = r_kpi_exp * mp.sqrt(
        (mpf("0.013") / mpf(str(M_K_PM_MEV_VALIDATION))) ** 2
        + (mpf("0.00018") / mpf(str(M_PI_PM_MEV_VALIDATION))) ** 2
    )
    sigma_kpi_ppq = r_kpi_sig / r_kpi_exp * mpf("1e15")
    base_kpi_sq = q_bal(3, q0) * q_bal(4, q0)

    t1_rows = []
    for L in [0, 1, 2, 3, 4, 5, 6, 7, 8, "inf"]:
        if L == "inf":
            em_factor = mpf(1) + mp.log(mpf(1) + hbar_q)
        else:
            em_factor = mpf(1) + sum(
                (mpf(-1) ** (k - 1)) * (hbar_q ** k) / mpf(k) for k in range(1, int(L) + 1)
            )
        r_pred = mp.sqrt(base_kpi_sq + (alpha_cs / pi) * em_factor)
        err_ppq = (r_pred - r_kpi_exp) / r_kpi_exp * mpf("1e15")
        err_sig = (r_pred - r_kpi_exp) / r_kpi_sig
        t1_rows.append({
            "level_L": str(L),
            "mK_over_mpi_pred": fmt(r_pred),
            "err_ppQ": fmt(err_ppq),
            "abs_err_over_sigma_exp": fmt(abs(err_sig)),
            "inside_1sigma_exp": bool(abs(err_sig) < mpf(1)),
        })

    # =========================================================================
    # TOWER T2: Gauge Fixed-Point Loop Level L = 0..4 (v / G_F and 1/alpha_EM)
    # =========================================================================
    m_p_gev = mpf(str(M_P_MEV_VALIDATION)) / mpf(1000)
    G_F_exp = mpf("1.1663787e-5")
    G_F_sig = mpf("0.0000006e-5")
    v_exp = mpf(1) / mp.sqrt(mp.sqrt(mpf(2)) * G_F_exp)
    v_sig = v_exp * G_F_sig / (mpf(2) * G_F_exp)
    sigma_v_ppq = v_sig / v_exp * mpf("1e15")

    q2_0 = q_bal(2, q0)
    H_hab = q2_0 / (mpf(8) * pi)
    N_v_L0 = q0 * q_bal(4, q0) * q_bal(6, q0) * q_bal(8, q0)
    N_v_L1 = N_v_L0 * (q2_0 / mpf(2))
    T_EW = N_v_L1 + mpf(1) / pi  # L = 2 (+ Bring zero-mode 1/pi)
    a_v_L3 = mp.findroot(lambda a: -H_hab * a ** 2 + T_EW * a - mpf(1), mpf(1) / T_EW)
    N_v_L3 = mpf(1) / a_v_L3
    a_v_L4 = mp.findroot(
        lambda a: (hbar_q ** 2) * H_hab * a ** 3 - H_hab * a ** 2 + T_EW * a - mpf(1),
        mpf(1) / T_EW,
    )
    N_v_L4 = mpf(1) / a_v_L4

    t2_ew_rows = []
    for lbl, Nv in [
        ("L0_bare_tree", N_v_L0),
        ("L1_qdim_dressed", N_v_L1),
        ("L2_plus_Bring_1_over_pi", T_EW),
        ("L3_1loop_quadratic_FP", N_v_L3),
        ("L4_1loop_Schwinger_cubic_FP", N_v_L4),
    ]:
        v_p = Nv * m_p_gev
        err_ppq = (v_p - v_exp) / v_exp * mpf("1e15")
        err_sig = (v_p - v_exp) / v_sig
        t2_ew_rows.append({
            "level": lbl,
            "v_pred_GeV": fmt(v_p),
            "err_ppQ": fmt(err_ppq),
            "err_sigma_exp": fmt(err_sig),
            "inside_1sigma_exp": bool(abs(err_sig) < mpf(1)),
        })

    wb.add_assertion(
        name="T2_EW_VEV_L4_strictly_inside_1sigma",
        computed=fmt(abs(N_v_L4 * m_p_gev - v_exp) / v_sig),
        expected="0.1142",
        tolerance="0.01",
        source="ElectroweakBringSchwingerBridge: L=4 Schwinger cubic lands at 0.114 sigma_exp",
    )

    # 1/alpha_EM fixed-point loop level L = 0..3 + required L = 4 two-loop c2
    alpha_entry = _codata.codata("inverse fine-structure constant")
    alpha_inv_exp = mpf(alpha_entry.value_str)
    alpha_inv_sig = mpf(alpha_entry.uncertainty_str)
    sigma_alpha_ppq = alpha_inv_sig / alpha_inv_exp * mpf("1e15")

    a_L0 = q0 * q_bal(9, q0) * q_bal(10, q0)
    T_EM = a_L0 + mpf(2) / (mpf(3) * pi)  # L = 1 (+ Bring zero-mode 2/(3*pi))
    a_em_formA = (-T_EM + mp.sqrt(T_EM ** 2 + mpf(4) * H_hab)) / (mpf(2) * H_hab)
    ainv_L2 = mpf(1) / a_em_formA
    a_em_formB = mp.findroot(
        lambda a: -H_hab * (h0 ** 2) * (a ** 3) + H_hab * (a ** 2) + T_EM * a - mpf(1),
        a_em_formA,
    )
    ainv_L3 = mpf(1) / a_em_formB
    c2_req_alpha = (alpha_inv_exp - ainv_L3) / (a_em_formB ** 2)

    t2_alpha_rows = []
    for lbl, ainv in [
        ("L0_bare_tree_q0_9_10", a_L0),
        ("L1_plus_Bring_2_over_3pi", T_EM),
        ("L2_1loop_FormA_quadratic", ainv_L2),
        ("L3_1loop_FormB_Schwinger_cubic", ainv_L3),
    ]:
        err_ppq = (ainv - alpha_inv_exp) / alpha_inv_exp * mpf("1e15")
        err_sig = (ainv - alpha_inv_exp) / alpha_inv_sig
        t2_alpha_rows.append({
            "level": lbl,
            "alpha_inv_pred": fmt(ainv),
            "err_ppQ": fmt(err_ppq),
            "err_sigma_exp": fmt(err_sig),
            "inside_1sigma_exp": bool(abs(err_sig) < mpf(1)),
        })

    # =========================================================================
    # TOWER T3: Q_beta & m_n Habiro-Kashiwara + Mirror-Projected D-Phase + 2tQED
    # =========================================================================
    q_beta_exp = mpf(str(Q_BETA_MEV))
    q_beta_sig = mpf(str(Q_BETA_MEV_ERR))
    m_n_exp = mpf(str(M_N_MEV_VALIDATION))
    m_n_sig = mpf(str(M_N_MEV_VALIDATION_ERR))
    m_p_exp = mpf(str(M_P_MEV_VALIDATION))

    z_D = (q0 ** 3) / (q0 ** 2 + mpf(1))
    b_sq = (h0 ** 2 + mpf(3)) / (h0 ** 2 + mpf(4))
    b_kash = mp.sqrt(b_sq)
    u_hab = b_kash * (hbar_q ** 2)

    Q_A = m_e * abs(q0 ** 2 - mpf(2) * q0 - mpf(1)) * (q0 + mpf(1)) / (mpf(2) * q0 ** 3)
    w3_zD = (q0 ** 4 + mpf(1)) / ((q0 ** 2 + mpf(1)) ** 2)
    w21_zD = (q0 ** 2) / ((q0 ** 2 + mpf(1)) ** 2)
    chi3_nuc11 = -(q0 ** 2 - mpf(1)) * ((q0 ** 2 + mpf(1)) ** 2) / (mpf(4) * q0)
    p_poly = (
        mpf(2) * (q0 ** 12) - mpf(5) * (q0 ** 10) + mpf(5) * (q0 ** 8)
        - mpf(5) * (q0 ** 6) + mpf(5) * (q0 ** 4) - mpf(5) * (q0 ** 2) + mpf(2)
    )
    chi21_inter = (q0 ** 2 - mpf(1)) * (q0 ** 4 + mpf(1)) * p_poly / (mpf(4) * (q0 ** 9))
    tr_zD_inter = w3_zD * chi3_nuc11 + w21_zD * chi21_inter
    Q_KD6 = E0_base * (-tr_zD_inter) * ((q0 ** 6 + q0 ** (-6)) / mpf(2))

    alpha_D_unproj = (z_D - mpf(1)) * h0 / mpf(2)
    alpha_D_proj = alpha_D_unproj - (h0 ** 2) / mpf(4)

    dm_qed_plain = mpf(str(np_qed_splitting_borromean_conn_mev(weighting="plain")))
    dm_qed_q = mpf(str(np_qed_splitting_borromean_conn_mev(weighting="q")))

    t3_rows = []
    for name, q_pred in [
        ("N0_FormA_tree", Q_A),
        ("N1_FormA_Kashiwara_cos_alphaD", Q_A * mp.cos(alpha_D_unproj - b_kash * (hbar_q ** 2) / mpf(2))),
        ("N2_FormA_c2_neg1_strong_only", Q_A * mp.cos(alpha_D_unproj - b_kash * (hbar_q ** 2) / mpf(2)) * (mpf(1) - u_hab ** 2)),
        ("N2_FormA_plus_2tQED_plain", Q_A * mp.cos(alpha_D_unproj - b_kash * (hbar_q ** 2) / mpf(2)) * (mpf(1) - u_hab ** 2) + dm_qed_plain),
        ("N2_FormA_plus_2tQED_cartan_q", Q_A * mp.cos(alpha_D_unproj - b_kash * (hbar_q ** 2) / mpf(2)) * (mpf(1) - u_hab ** 2) + dm_qed_q),
        ("N2_KD6_unproj_alphaD_plus_2tQED", Q_KD6 * mp.cos(alpha_D_unproj - b_kash * (hbar_q ** 2) / mpf(2)) * (mpf(1) - u_hab ** 2) + dm_qed_plain),
        ("N2_KD6_mirrorProj_alphaD_plus_2tQED", Q_KD6 * mp.cos(alpha_D_proj - b_kash * (hbar_q ** 2) / mpf(2)) * (mpf(1) - u_hab ** 2) + dm_qed_plain),
    ]:
        mn_pred = m_p_exp + m_e + q_pred
        qb_ppq = (q_pred - q_beta_exp) / q_beta_exp * mpf("1e15")
        qb_sig = (q_pred - q_beta_exp) / q_beta_sig
        mn_ppq = (mn_pred - m_n_exp) / m_n_exp * mpf("1e15")
        mn_sig = (mn_pred - m_n_exp) / m_n_sig
        t3_rows.append({
            "level": name,
            "Q_beta_MeV": fmt(q_pred),
            "Q_beta_err_ppQ": fmt(qb_ppq),
            "Q_beta_err_sigma": fmt(qb_sig),
            "m_n_MeV": fmt(mn_pred),
            "m_n_err_ppQ": fmt(mn_ppq),
            "m_n_err_sigma": fmt(mn_sig),
        })

    # Envelope of higher Habiro rungs u^N for N = 3..6
    t3_envelopes = []
    for N_rung in (3, 4, 5, 6):
        dQ = Q_A * (u_hab ** N_rung)
        qb_env_sig = dQ / q_beta_sig
        mn_env_sig = dQ / m_n_sig
        t3_envelopes.append({
            "rung_N": N_rung,
            "u_pow_N": fmt(u_hab ** N_rung),
            "scale_eV": fmt(dQ * mpf("1e6")),
            "Q_beta_sigma_units": fmt(qb_env_sig),
            "m_n_sigma_units": fmt(mn_env_sig),
        })

    # =========================================================================
    # TOWER T4: General-K GPMT Modified Quantum Dimensions on H_K(q) (K = 3..8)
    # =========================================================================
    wb.add_assertion(
        name="T4_GPMT_dMod_111_matches_Lean",
        computed=fmt(gpmt_zero_order_and_dmod_D((1, 1, 1), q0)[1]),
        expected=fmt(gpmt_dmod_111(q0)),
        tolerance="1e-65",
        source="NucleonIdempotentModifiedTrace.dMod111",
    )
    wb.add_assertion(
        name="T4_GPMT_dMod_211_matches_Lean",
        computed=fmt(gpmt_zero_order_and_dmod_D((2, 1, 1), q0)[1]),
        expected=fmt(gpmt_dmod_211(q0)),
        tolerance="1e-65",
        source="H4GPMTModifiedDimensionCumulants.dMod211",
    )
    wb.add_assertion(
        name="T4_GPMT_dMod_1111_matches_Lean",
        computed=fmt(gpmt_zero_order_and_dmod_D((1, 1, 1, 1), q0)[1]),
        expected=fmt(gpmt_dmod_1111(q0)),
        tolerance="1e-65",
        source="H4GPMTModifiedDimensionCumulants.dMod1111",
    )

    t4_k_rows = []
    s_gpmt_by_K: dict[int, mpf] = {}
    for K in range(3, 9):
        parts = partitions_of(K)
        two_row_sum = mpf(0)
        s_row3_signed = mpf(0)
        s_row3_abs = mpf(0)
        n_order1 = 0
        n_order2plus = 0
        for lam in parts:
            f_lam = specht_dim(lam)
            z_ord, val = gpmt_zero_order_and_dmod_D(lam, q0)
            if z_ord == 0:
                two_row_sum += mpf(f_lam) * val
            elif z_ord == 1:
                n_order1 += 1
                n_inv = sum(i * p for i, p in enumerate(lam))
                springer_sign = mpf(-1) ** n_inv
                s_row3_signed += springer_sign * mpf(f_lam) * val
                s_row3_abs += mpf(f_lam) * abs(val)
            else:
                n_order2plus += 1
        s_gpmt_by_K[K] = s_row3_signed
        wb.add_assertion(
            name=f"T4_H{K}_two_row_Wedderburn_sum_eq_one",
            computed=fmt(two_row_sum),
            expected="1",
            tolerance="1e-65",
            source=f"Universal Ocneanu/Wenzl two-row survival identity on H_{K}(q_0)",
        )
        t4_k_rows.append({
            "K": K,
            "num_partitions": len(parts),
            "num_order1_GPMT_sectors": n_order1,
            "num_order2plus_GPMT_sectors": n_order2plus,
            "two_row_prob_sum": fmt(two_row_sum),
            "s_row3_GPMT_signed": fmt(s_row3_signed),
            "s_row3_GPMT_abs_sum": fmt(s_row3_abs),
        })

    # Binomial cumulant inversion mu_K = sum_{j=3}^K (-1)^{K-j} C(K, j) s_j
    t4_cumulants = {}
    for K in range(3, 9):
        mu_K = sum(
            (mpf(-1) ** (K - j)) * mpf(comb(K, j)) * s_gpmt_by_K[j]
            for j in range(3, K + 1)
        )
        t4_cumulants[str(K)] = fmt(mu_K)

    # =========================================================================
    # TOWER T5: Heavy & Light Nuclide Level Sweep + 4x4 Hankel Z_{3A}^{(4)}
    # =========================================================================
    ame = load_ame_nuclides()
    mp_1t, mn_1t = proton_neutron_mass_mev()
    mp_2t = m_p_exp
    mn_2t = mpf(str(neutron_mass_two_term_mev(weighting="plain")))

    MAX_N = 730
    q_int_tbl = [mpf(0)] * (MAX_N + 1)
    q_fact_tbl = [mpf(1)] * (MAX_N + 1)
    for k in range(1, MAX_N + 1):
        q_int_tbl[k] = q_bal(k, q0)
        q_fact_tbl[k] = q_fact_tbl[k - 1] * q_int_tbl[k]

    hankel4 = Hankel4RowPlancherelEvaluator(714, q0, q_fact_tbl)

    # Verify the 4x4 Hankel determinant identity against direct 4-row partition summation at n=168 (56Fe)!
    Z_168_direct = frobenius_plancherel_Z_bounded_rows(168, 4, q_int_tbl, q_fact_tbl)
    Z_168_hankel = hankel4.eval_Z4(168)
    wb.add_assertion(
        name="T5_Hankel_4x4_determinant_matches_4row_Plancherel_at_56Fe",
        computed=fmt((Z_168_hankel - Z_168_direct) / Z_168_direct),
        expected="0",
        tolerance="1e-65",
        source="Andréief/Cauchy-Binet 4x4 Hankel determinant identity for Z_n^{(4)}(q_0) at n=168 (56Fe)",
    )

    w_free_111 = frobenius_W_lambda((1, 1, 1), q_int_tbl, q_fact_tbl)
    Z3_4row = hankel4.eval_Z4(3)
    w_free_norm = w_free_111 / Z3_4row

    tau_bor = (mpf(4) + h0 ** 2 - mpf(3) * h0 ** 4 - h0 ** 6) / (h0 ** 2 + mpf(4))
    f_pp = z_D
    f_pn = z_D
    f_nn = z_D - h0

    def g_bor(x: mpf) -> mpf:
        return -li_2_q(-x, q0, qi)

    # Deuteron (2H) level sweep: R = 0 (1-body dtr only), R = 1 with M = 0..4, inf on E_0^(M)
    entry_2H = ame[(1, 2)]
    B_2H_ame = entry_2H["B_AME_MeV"]
    sig_B_2H = entry_2H["sigma_B_MeV"]
    M_2H_nuc_ame = entry_2H["M_atom_AME_MeV"] - m_e + electron_binding_mev_mp(1, alpha_cs, m_e)
    sig_M_2H = entry_2H["sigma_M_MeV"]
    dtr_2H = (tau_bor ** 2) * (mpf(1) - f_pn)
    pair_2H = (z_D ** 2) * (g_bor(tau_bor ** 2) - g_bor((tau_bor ** 2) * f_pn))

    t5_deuteron_rows = []
    for lbl, B_d, M_d in [
        ("R0_1body_dtr_only_1tNuc", E0_base * dtr_2H, mp_1t + mn_1t - E0_base * dtr_2H),
        ("R1_1pair_E0_M0_1tNuc_OLD", E0_base * (dtr_2H + pair_2H), mp_1t + mn_1t - E0_base * (dtr_2H + pair_2H)),
        ("R1_1pair_E0_M0_2tNuc", E0_base * (dtr_2H + pair_2H), mp_2t + mn_2t - E0_base * (dtr_2H + pair_2H)),
        ("R1_1pair_E0_M1_2tNuc", E0_base * (mpf(1) + hbar_q ** 2) * (dtr_2H + pair_2H), mp_2t + mn_2t - E0_base * (mpf(1) + hbar_q ** 2) * (dtr_2H + pair_2H)),
        ("R1_1pair_E0_M2_2tNuc", E0_base * (mpf(1) + hbar_q ** 2 + hbar_q ** 4) * (dtr_2H + pair_2H), mp_2t + mn_2t - E0_base * (mpf(1) + hbar_q ** 2 + hbar_q ** 4) * (dtr_2H + pair_2H)),
        ("R1_1pair_E0_Minf_2tNuc", E0_exact * (dtr_2H + pair_2H), mp_2t + mn_2t - E0_exact * (dtr_2H + pair_2H)),
    ]:
        t5_deuteron_rows.append({
            "level": lbl,
            "B_2H_MeV": fmt(B_d),
            "B_err_keV": fmt((B_d - B_2H_ame) * mpf(1000)),
            "M_err_ppQ": fmt((M_d - M_2H_nuc_ame) / M_2H_nuc_ame * mpf("1e15")),
            "M_err_sigma_exp": fmt((M_d - M_2H_nuc_ame) / sig_M_2H),
        })

    nuclide_list = [
        ("2H", 1, 1, 2),
        ("3H", 1, 2, 1),
        ("3He", 2, 1, 1),
        ("4He", 2, 2, 0),
        ("12C", 6, 6, 0),
        ("16O", 8, 8, 0),
        ("40Ca", 20, 20, 0),
        ("56Fe", 26, 30, 0),
        ("208Pb", 82, 126, 0),
        ("238U", 92, 146, 0),
    ]

    import mass_binding_dashboard as mbd  # noqa: E402
    Lbond = mbd._bond_type_L()

    t5_nuclides = []
    for name, Z, N, S_twice in nuclide_list:
        A = Z + N
        n_strands = 3 * A
        entry = ame[(Z, A)]
        B_ame = entry["B_AME_MeV"]
        M_atom_ame = entry["M_atom_AME_MeV"]
        sig_M = entry["sigma_M_MeV"]
        B_el = electron_binding_mev_mp(Z, alpha_cs, m_e)
        M_nuc_ame = M_atom_ame - mpf(Z) * m_e + B_el
        sig_M_ppq = sig_M / M_nuc_ame * mpf("1e15") if sig_M > 0 else mpf(0)

        # 1. OLD m_can (unscreened all-pairs Borromean, E0_M0, 1-term nucleons, no Coulomb)
        ratio_bor = (f_pp ** max(Z - 1, 0)) * (f_pn if (Z and N) else mpf(1)) * (f_nn ** max(N - 1, 0))
        dtr = (tau_bor ** A) * (mpf(1) - ratio_bor)
        pair_pp = mpf(comb(Z, 2)) * (g_bor(tau_bor ** 2) - g_bor((tau_bor ** 2) * f_pp))
        pair_pn = mpf(Z * N) * (g_bor(tau_bor ** 2) - g_bor((tau_bor ** 2) * f_pn))
        pair_nn = mpf(comb(N, 2)) * (g_bor(tau_bor ** 2) - g_bor((tau_bor ** 2) * f_nn))
        B_old_bor = E0_base * (dtr + (z_D ** 2) * (pair_pp + pair_pn + pair_nn))
        M_old_bor = mpf(Z) * mp_1t + mpf(N) * mn_1t - B_old_bor

        # 2. NEW-1: 1D bond chain B_sym (with E0_exact) - E_C
        E_C = coulomb_energy_mev(Z, A)
        B_sym_exact_E0 = E0_exact * (
            mpf(max(Z - 1, 0)) * Lbond["pp"]
            + (Lbond["pn"] if (Z >= 1 and N >= 1) else mpf(0))
            + mpf(max(N - 1, 0)) * Lbond["nn"]
        )
        B_new1 = B_sym_exact_E0 - E_C
        M_new1 = mpf(Z) * mp_2t + mpf(N) * mn_2t - B_new1

        # 3. Unnormalized vs Exact 4-Row Hankel-Normalized SU(4) Plancherel (for ALL A up to 238!)
        lam = ground_state_su4_partition(Z, N, S_twice)
        W_unnorm = frobenius_W_lambda(lam, q_int_tbl, q_fact_tbl)
        B_unnorm_gate = -E0_base * mp.log(W_unnorm) - E_C

        Z_4row = hankel4.eval_Z4(n_strands)
        W_norm4 = W_unnorm / Z_4row
        B_norm4_gate = -E0_exact * mp.log(W_norm4) - E_C
        B_norm4_rel = -E0_exact * (mp.log(W_norm4) - mpf(A) * mp.log(w_free_norm)) - E_C

        n_pairs_total = comb(A, 2)
        avg_pair_mev = E0_exact * (z_D ** 2) * (pair_pp + pair_pn + pair_nn) / mpf(n_pairs_total)
        sym_pair_unit = E0_exact * (z_D ** 2) * (g_bor(tau_bor ** 2) - g_bor((tau_bor ** 2) * f_pn))

        t5_nuclides.append({
            "iso": name,
            "Z": Z,
            "N": N,
            "A": A,
            "lam": list(lam),
            "B_AME_MeV": fmt(B_ame),
            "M_nuc_AME_MeV": fmt(M_nuc_ame),
            "sigma_M_ppQ": fmt(sig_M_ppq),
            "E_Coulomb_MeV": fmt(E_C),
            "OLD_m_can": {
                "B_MeV": fmt(B_old_bor),
                "B_pp_share_MeV": fmt(E0_base * (z_D ** 2) * pair_pp),
                "B_pn_share_MeV": fmt(E0_base * (z_D ** 2) * pair_pn),
                "B_nn_share_MeV": fmt(E0_base * (z_D ** 2) * pair_nn),
                "M_err_ppQ": fmt((M_old_bor - M_nuc_ame) / M_nuc_ame * mpf("1e15")),
            },
            "NEW1_Bsym_2tQED": {
                "B_MeV": fmt(B_new1),
                "M_err_ppQ": fmt((M_new1 - M_nuc_ame) / M_nuc_ame * mpf("1e15")),
            },
            "Plancherel_SU4": {
                "W_unnorm": fmt(W_unnorm),
                "B_unnorm_minus_EC_MeV": fmt(B_unnorm_gate),
                "M_unnorm_err_ppQ": fmt(((mpf(Z) * mp_2t + mpf(N) * mn_2t - B_unnorm_gate) - M_nuc_ame) / M_nuc_ame * mpf("1e15")),
                "Z_4row": fmt(Z_4row),
                "W_norm4": fmt(W_norm4),
                "B_norm4_minus_EC_MeV": fmt(B_norm4_gate),
                "M_norm4_err_ppQ": fmt(((mpf(Z) * mp_2t + mpf(N) * mn_2t - B_norm4_gate) - M_nuc_ame) / M_nuc_ame * mpf("1e15")),
                "B_norm4_rel_free_minus_EC_MeV": fmt(B_norm4_rel),
            },
            "pair_unit_pn_MeV": fmt(sym_pair_unit),
            "avg_pair_old_MeV": fmt(avg_pair_mev),
        })

    wb.add_data("T0_E0_geometric_tower", t0_rows)
    wb.add_data("T1_meson_log_tower", {
        "sigma_exp_ppQ": fmt(sigma_kpi_ppq),
        "rows": t1_rows,
    })
    wb.add_data("T2a_electroweak_loop_tower", {
        "sigma_exp_ppQ": fmt(sigma_v_ppq),
        "rows": t2_ew_rows,
    })
    wb.add_data("T2b_alpha_em_loop_tower", {
        "sigma_exp_ppQ": fmt(sigma_alpha_ppq),
        "required_L4_two_loop_c2": fmt(c2_req_alpha),
        "rows": t2_alpha_rows,
    })
    wb.add_data("T3_qbeta_mn_habiro_tower", {
        "sigma_Q_beta_ppQ": fmt(q_beta_sig / q_beta_exp * mpf("1e15")),
        "sigma_m_n_ppQ": fmt(m_n_sig / m_n_exp * mpf("1e15")),
        "rows": t3_rows,
        "higher_rung_envelopes": t3_envelopes,
    })
    wb.add_data("T4_GPMT_general_K_tower", {
        "rows": t4_k_rows,
        "mayer_cumulants_mu_K": t4_cumulants,
    })
    wb.add_data("T5a_deuteron_level_sweep", t5_deuteron_rows)
    wb.add_data("T5b_nuclides_and_heavy_decomposition", t5_nuclides)

    wb.save({"q0Anchor": "proton", "q0Value": Q_50_DIGIT_STR})

    print("=== T0: E_0^(M) GEOMETRIC TOWER ===")
    for r in t0_rows:
        print(f"  M={r['level_M']}  E0={mp.nstr(mpf(r['E0_M_MeV']), 13)} MeV  err={mp.nstr(mpf(r['trunc_err_ppQ']), 4)} ppQ")

    print("\n=== T1: MESON m_K / m_pi LOG TOWER (sigma_exp = 2.64e+10 ppQ) ===")
    for r in t1_rows:
        print(f"  L={r['level_L']:>3s}  err={mp.nstr(mpf(r['err_ppQ']), 4)} ppQ  |err|/sigma={mp.nstr(mpf(r['abs_err_over_sigma_exp']), 5)}  inside={r['inside_1sigma_exp']}")

    print("\n=== T2a: ELECTROWEAK VEV v LOOP TOWER (sigma_exp = 2.57e+08 ppQ) ===")
    for r in t2_ew_rows:
        print(f"  {r['level']:<28s}  err={mp.nstr(mpf(r['err_ppQ']), 4)} ppQ  err/sigma={mp.nstr(mpf(r['err_sigma_exp']), 4)}  inside={r['inside_1sigma_exp']}")

    print(f"\n=== T2b: 1/alpha_EM LOOP TOWER (sigma_exp = {mp.nstr(sigma_alpha_ppq, 4)} ppQ; c2_req = {mp.nstr(c2_req_alpha, 6)}) ===")
    for r in t2_alpha_rows:
        print(f"  {r['level']:<32s}  1/alpha={mp.nstr(mpf(r['alpha_inv_pred']), 13)}  err={mp.nstr(mpf(r['err_ppQ']), 4)} ppQ  err/sigma={mp.nstr(mpf(r['err_sigma_exp']), 4)}  inside={r['inside_1sigma_exp']}")

    print("\n=== T3: Q_beta & m_n TOWER ===")
    for r in t3_rows:
        print(f"  {r['level']:<36s}  Q_err={mp.nstr(mpf(r['Q_beta_err_ppQ']), 4)} ppQ ({mp.nstr(mpf(r['Q_beta_err_sigma']), 4)} sig)  mn_err={mp.nstr(mpf(r['m_n_err_ppQ']), 4)} ppQ ({mp.nstr(mpf(r['m_n_err_sigma']), 4)} sig)")
    for e in t3_envelopes:
        print(f"  Envelope N={e['rung_N']}: u^N={mp.nstr(mpf(e['u_pow_N']), 4)} ({mp.nstr(mpf(e['scale_eV']), 4)} eV) -> {mp.nstr(mpf(e['Q_beta_sigma_units']), 4)} sig(Q_beta), {mp.nstr(mpf(e['m_n_sigma_units']), 4)} sig(m_n)")

    print("\n=== T4: GENERAL-K GPMT MODIFIED QUANTUM DIMENSIONS (K=3..8) ===")
    for r in t4_k_rows:
        mu_k = mp.nstr(mpf(t4_cumulants[str(r["K"])]), 8)
        print(f"  K={r['K']}  parts={r['num_partitions']:2d}  ord1={r['num_order1_GPMT_sectors']:2d}  ord2+={r['num_order2plus_GPMT_sectors']}  s_GPMT={mp.nstr(mpf(r['s_row3_GPMT_signed']), 8)}  mu_{r['K']}={mu_k}")

    print("\n=== T5a: DEUTERON (2H) LEVEL SWEEP ===")
    for r in t5_deuteron_rows:
        print(f"  {r['level']:<28s}  B_2H={mp.nstr(mpf(r['B_2H_MeV']), 8)} MeV (dB={mp.nstr(mpf(r['B_err_keV']), 5)} keV)  M_err={mp.nstr(mpf(r['M_err_ppQ']), 4)} ppQ ({mp.nstr(mpf(r['M_err_sigma_exp']), 4)} sig)")

    print("\n=== T5b: NUCLIDE DECOMPOSITION & 4x4 HANKEL 4-ROW NORMALIZED PLANCHEREL ===")
    for r in t5_nuclides:
        p = r["Plancherel_SU4"]
        print(
            f"  {r['iso']:<5s} B_AME={mp.nstr(mpf(r['B_AME_MeV']), 7):>8s}  E_C={mp.nstr(mpf(r['E_Coulomb_MeV']), 5):>6s}  "
            f"B_old={mp.nstr(mpf(r['OLD_m_can']['B_MeV']), 7):>9s} (nn={mp.nstr(mpf(r['OLD_m_can']['B_nn_share_MeV']), 6):>8s})  "
            f"B_new1={mp.nstr(mpf(r['NEW1_Bsym_2tQED']['B_MeV']), 6):>7s}  "
            f"W_un={mp.nstr(mpf(p['W_unnorm']), 3):>9s}  W_n4={mp.nstr(mpf(p['W_norm4']), 3):>9s}  "
            f"B_norm4={mp.nstr(mpf(p['B_norm4_minus_EC_MeV']), 7):>8s} (err={mp.nstr(mpf(p['M_norm4_err_ppQ']), 4):>10s} ppQ)"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
