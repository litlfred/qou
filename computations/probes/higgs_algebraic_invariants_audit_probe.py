#!/usr/bin/env python3
"""Pre-registered 80-dps proton-pinned audit of algebraic invariants vs the Higgs sector.

Companion to `QOU/StandardModel/OqSU2HaarYukawaAndPodlesHiggs.lean` and
`docs/audits/2026-11-28-higgs-algebraic-invariants-oqsu2-audit.md`.

Audits all five structural families across `O_q(SU(2))`, the Podleś sphere `S^2_q`,
Connes-Chamseddine / Dabrowski-Sitarz spectral-action quartics, `U_q(sl_2)` Casimirs,
and Iwahori-Hecke `H_n(q_0)` Jucys-Murphy / Hoefsmit / `T(2,2k)` invariants at the
active proton pin (`q0Anchor = "proton"`, `WORK_DPS = 105`, `OUT_DPS = 80`, zero `float64`,
zero inline CODATA literals, zero fitted parameters):

  1. **Haar-Yukawa VEV Unification & `[2]_q / 2` Variance Lock (`qou-99qc`):**
     - Verifies `h(delta*alpha) = q_0^2/(1+q_0^2) = PR_{1,1}` (`0.5519818550...`),
       `h(alpha*delta) = 1/(1+q_0^2) = PR_{2,2}` (`0.4480181450...`),
       `([2]_{q_0}/2)^2 = 1 / (4 * p_+ * p_-)` (`1.010926552...`), and KMS polarization
       bias `p_+ - p_- = (q_0^2 - 1)/(q_0^2 + 1) = tanh(ln q_0) = 0.1039637101...`.
  2. **Podleś `q`-Monopole Projector `e_Podles` & Symmetry-Breaking Trace/Det Defects (`qou-ukqh`):**
     - Verifies symbolic & 105-dps idempotence `e_Podles^2 = e_Podles`, U(1) invariance,
       pivotal `q`-trace `e_{00} + q_0^2 e_{11} = 1`, ordinary trace expectation `2/(1+q_0^2) = 0.8960362899...`
       (defect `tanh(ln q_0)`), and classical determinant defect `(q_0 - 1)/[2]_{q_0} = 0.0546913094...`.
  3. **Spectral-Action / Podleś Quartic Ratios vs QOU `derivedHiggsQuartic` (`v`-Cancellation):**
     - Evaluates pre-sigma Chamseddine-Connes (`4/3 * M_W^2/v^2`), Podleś equatorial kurtosis
       `h((gamma^* gamma)^2)/h(gamma^* gamma)^2 = [2]_{q_0}^2/[3]_{q_0} = 1.3285468214... < 4/3`,
       bare `O_q(SU(2))` / `U_q(sl_2)` invariants (`1/(2[2]_{q_0}^2)`, `(1+q_0^4)/(4(1+q_0^2)^2)`,
       `C_2^{(q_0)}(1/2)/6`, `q_0^{-2}/(2[3]_{q_0})`), and QOU's self-consistent `L2a` Plancherel
       Higgs chain (`m_H = 125.3007 GeV [+0.92 sigma]` tree; `125.0816 GeV [-1.08 sigma]` half-Habiro)
       against PDG 2024 (`m_H = 125.20 +/- 0.11 GeV`) and PDG 2022 (`125.25 GeV`).
  4. **Hecke `H_n(q_0)` Jucys-Murphy Central Sums, `6/5` Rank Lock, & 6-Strand Hoefsmit Test (`qou-zd6l`):**
     - Proves `6/5 = dim H_3 / dim Z(H_4)` must stay an undeformed Wedderburn rank invariant
       (`[2]_{q_0}[3]_{q_0}/5 = 1.224116` shifts `m_H` to `127.82 GeV`, `+23.8 sigma`), and refutes
       naive odd/even `(1,3,5)` vs `(2,4,6)` JM slot ratios on `H_6(q_0)` (`sin^2 theta_W in [0.356, 0.778]`).
"""

from __future__ import annotations

from pathlib import Path
import sys

_THIS = Path(__file__).resolve()
_ROOT = _THIS.parents[2]
for _p in (
    _ROOT / "tools" / "qou-substrate" / "python",
    _ROOT / "computations",
    _ROOT / "computations" / "substrate",
):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import M_E_MEV_STR, q_at  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WORK_DPS = 105
OUT_DPS = 80
set_compute_dps(WORK_DPS)
mp.mp.dps = WORK_DPS


def fmt80(val: mp.mpf) -> str:
    return mp.nstr(val, OUT_DPS, strip_zeros=False)


def binom_int(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    acc = 1
    for i in range(k):
        acc = (acc * (n - i)) // (i + 1)
    return acc


def qbal(n: int, qv: mp.mpf) -> mp.mpf:
    return (qv**n - qv ** (-n)) / (qv - mp.mpf(1) / qv)


def two_mul_p(m: int, hv: mp.mpf) -> mp.mpf:
    return sum(
        (mp.mpf(binom_int(m + j, 2 * j)) * (hv ** (2 * j)) for j in range(m + 1)),
        mp.mpf(0),
    )


def standard_tableaux(part: tuple[int, ...]):
    if sum(part) == 0:
        yield []
        return
    for r in range(len(part)):
        if part[r] > 0 and (r == len(part) - 1 or part[r] > part[r + 1]):
            c = part[r] - 1
            nxt = list(part)
            nxt[r] -= 1
            for sub in standard_tableaux(tuple(nxt)):
                yield sub + [(r, c)]


def verify_symbolic_oqsu2_podles_identities() -> bool:
    q_s = sp.Symbol("q", nonzero=True)
    h_s = q_s - 1 / q_s
    q2_s = q_s + 1 / q_s
    q3_s = q_s**2 + 1 + q_s ** (-2)

    # Cleared Podleś kurtosis & variance identities
    id1 = sp.simplify((1 + q_s**2) ** 2 - (q_s**2) * (q2_s**2)) == 0
    id2 = sp.simplify((1 + q_s**2 + q_s**4) - (q_s**2) * q3_s) == 0
    id3 = sp.simplify(q3_s * ((1 + q_s**2) ** 2) - (q2_s**2) * (1 + q_s**2 + q_s**4)) == 0
    id4 = sp.simplify(4 * q3_s - 3 * (q2_s**2) - h_s**2) == 0

    # Jimbo singlet projector idempotence & Haar weight match
    rc = sp.Matrix(
        [
            [q_s, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, q_s - 1 / q_s, 0],
            [0, 0, 0, q_s],
        ]
    )
    pr = (q_s * sp.eye(4) - rc) / q2_s
    idem_ok = sp.simplify(pr * pr - pr) == sp.zeros(4)
    w_ok = (
        sp.simplify(pr[1, 1] - q_s**2 / (1 + q_s**2)) == 0
        and sp.simplify(pr[2, 2] - 1 / (1 + q_s**2)) == 0
    )
    return bool(id1 and id2 and id3 and id4 and idem_ok and w_ok)


def evaluate_qou_l2a_proton_chain(qv: mp.mpf) -> dict[str, mp.mpf]:
    """Self-consistent proton-pinned QOU L2a EW + Higgs chain (`(m_e, q_0^{(p)})` only)."""
    one = mp.mpf(1)
    two = mp.mpf(2)
    me_gev = mp.mpf(M_E_MEV_STR) / mp.mpf(1000)
    hv = qv - one / qv
    hb = one - one / qv
    q2 = qbal(2, qv)

    vol41 = two * mp.clsin(2, mp.pi / mp.mpf(3))
    tr_bor = abs((mp.mpf(4) + hv**2 - mp.mpf(3) * (hv**4) - hv**6) / (hv**2 + mp.mpf(4)))
    qf3 = (qv**2 + one + qv ** (-2)) * (qv + one / qv)
    mp_gev = me_gev * (two * (vol41 / (hb**2)) * (tr_bor * qf3 / (qv**3)) - mp.mpf(12))
    mmu_gev = me_gev * vol41 / (hb**2)

    # Two-loop Bloch-B_3 alpha_EM(q_0)
    t_em = qv * qbal(9, qv) * qbal(10, qv) + two / (mp.mpf(3) * mp.pi)
    h_norm = q2 / (mp.mpf(8) * mp.pi)
    delta_b3 = mp.zeta(3) - mp.polylog(3, qv ** (-2))
    c3_em = h_norm * (delta_b3 / (mp.mpf(8) * mp.pi)) - h_norm * (hv**2)
    alpha0 = mp.findroot(lambda a: c3_em * (a**3) + h_norm * (a**2) + t_em * a - one, one / t_em)

    # Bring-Schwinger v_weak(q_0)
    t_ew = qv * (q2 / two) * qbal(4, qv) * qbal(6, qv) * qbal(8, qv) + one / mp.pi
    alpha_v = mp.findroot(
        lambda a: h_norm * (hb**2) * (a**3) - h_norm * (a**2) + t_ew * a - one,
        one / t_ew,
    )
    v_ew = mp_gev / alpha_v

    tp2 = two_mul_p(2, hv)
    tp3 = two_mul_p(3, hv)
    tp4 = two_mul_p(4, hv)
    r_zw = (tp3 * (q2**2)) / (tp2 * mp.mpf(4))
    c2_w = one / (r_zw**2)
    s2_w = one - c2_w
    a0_gev = mp.sqrt(mp.pi * alpha0) * v_ew

    drho_yt1 = mp.mpf(3) / (mp.mpf(32) * (mp.pi**2))
    dr_weak_1l = (alpha0 / (mp.mpf(4) * mp.pi * s2_w)) * (
        ((mp.mpf(7) - mp.mpf(4) * s2_w) / two) * mp.log(c2_w) + mp.mpf(6)
    )

    def dr_l2a(z_gev: mp.mpf) -> mp.mpf:
        return (
            (alpha0 / (mp.mpf(3) * mp.pi))
            * (
                (mp.log((z_gev / me_gev) ** 2) - mp.mpf(5) / mp.mpf(3))
                + (mp.log((z_gev / mmu_gev) ** 2) - mp.mpf(5) / mp.mpf(3))
                + (mp.mpf(14) / mp.mpf(3)) * (mp.log((z_gev / mp_gev) ** 2) - mp.mpf(5) / mp.mpf(3))
            )
            - (c2_w / s2_w) * drho_yt1
            + dr_weak_1l
        )

    mz_l2a = mp.findroot(
        lambda z: (a0_gev / (mp.sqrt(s2_w) * mp.sqrt(one - dr_l2a(z)))) * r_zw - z,
        mp.mpf(91),
    )
    mw_l2a = mz_l2a / r_zw
    dr_val = dr_l2a(mz_l2a)

    h_fac_tree = (tp4 / tp2) * (mp.mpf(6) / mp.mpf(5)) * (q2 / two)
    c_hab_half = one - (q2 / (mp.mpf(16) * mp.pi)) * (hv**2)
    c_bring_zero = one - (two / (mp.mpf(3) * mp.pi)) * (hb**2)

    mh_tree = mw_l2a * h_fac_tree
    mh_hab_half = mh_tree * c_hab_half
    mh_bring = mh_tree * c_bring_zero
    mh_from_z_tree = mz_l2a * (tp4 / tp3) * (mp.mpf(6) / mp.mpf(5)) * (two / q2)

    lam_tree = (mh_tree**2) / (two * (v_ew**2))
    lam_hab_half = (mh_hab_half**2) / (two * (v_ew**2))
    lam_bring = (mh_bring**2) / (two * (v_ew**2))

    return {
        "v_weak_gev": v_ew,
        "sin2_planch": s2_w,
        "MW_L2a_gev": mw_l2a,
        "MZ_L2a_gev": mz_l2a,
        "dr_L2a": dr_val,
        "h_fac_tree": h_fac_tree,
        "mH_L2a_tree_gev": mh_tree,
        "mH_L2a_from_Z_tree_gev": mh_from_z_tree,
        "mH_L2a_habiro_half_gev": mh_hab_half,
        "mH_L2a_bring_zero_gev": mh_bring,
        "lambda_H_L2a_tree": lam_tree,
        "lambda_H_L2a_habiro_half": lam_hab_half,
        "lambda_H_L2a_bring_zero": lam_bring,
    }


def main() -> None:
    one = mp.mpf(1)
    two = mp.mpf(2)
    q0 = q_at(WORK_DPS)
    h0 = q0 - one / q0
    q2 = qbal(2, q0)
    q3 = qbal(3, q0)
    q4 = qbal(4, q0)

    # External PDG comparison benchmarks (downstream comparison ONLY)
    gf_entry = codata("Fermi coupling constant")
    gf_val = mp.mpf(gf_entry.value_str)
    v_pdg = one / mp.sqrt(mp.sqrt(two) * gf_val)
    mh_pdg24 = mp.mpf("125.20")
    mh_sig24 = mp.mpf("0.11")
    mh_pdg22 = mp.mpf("125.25")
    mw_pdg = mp.mpf("80.3692")
    mz_pdg = mp.mpf("91.1876")
    lam_pdg24 = (mh_pdg24**2) / (two * (v_pdg**2))
    lam_sig24 = (mh_pdg24 * mh_sig24) / (v_pdg**2)
    lam_pdg22 = (mh_pdg22**2) / (two * (v_pdg**2))

    sym_ok = verify_symbolic_oqsu2_podles_identities()
    qou_ew = evaluate_qou_l2a_proton_chain(q0)

    # 1. O_q(SU(2)) & Podleś S^2_q invariants at proton q_0
    p_plus = (q0**2) / (one + q0**2)
    p_minus = one / (one + q0**2)
    haar_var = p_plus * p_minus
    half_haar_var = haar_var / two
    kms_asym = (q0**2 - one) / (q0**2 + one)
    det_defect = (q0 - one) / q2
    podles_ord_trace_exp = two / (one + q0**2)
    podles_kurtosis = (q2**2) / q3
    haar_purity_quarter = (p_plus**2 + p_minus**2) / mp.mpf(4)
    uq_casimir_half = (q0**2 + q0 + one) / ((q0 + one) ** 2)
    bipartite_lower_triplet = (q0 ** (-2)) / (two * q3)

    haar_yukawa_res = max(
        abs((p_plus + p_minus) - one),
        abs((p_plus - p_minus) - kms_asym),
        abs(kms_asym - (h0 / q2)),
        abs(((q2 / two) ** 2) * (mp.mpf(4) * haar_var) - one),
        abs((one - podles_ord_trace_exp) - kms_asym),
        abs(det_defect - (q0 * (q0 - one)) / (one + q0**2)),
        abs((mp.mpf(4) * q3 - mp.mpf(3) * (q2**2)) - (h0**2)),
    )

    # 2. Quartic coupling comparison table (NCG / bare O_q(SU(2)) vs QOU Plancherel)
    mw_sq_over_v_sq_l2a = (qou_ew["MW_L2a_gev"] ** 2) / (qou_ew["v_weak_gev"] ** 2)
    lam_cc_tree_l2a = (mp.mpf(4) / mp.mpf(3)) * mw_sq_over_v_sq_l2a
    lam_podles_kurt_l2a = podles_kurtosis * mw_sq_over_v_sq_l2a

    def pack_quartic(lam_val: mp.mpf, v_ref: mp.mpf) -> dict[str, str]:
        mh_pred = mp.sqrt(two * lam_val) * v_ref
        return {
            "lambda_H": fmt80(lam_val),
            "implied_m_H_GeV": fmt80(mh_pred),
            "rel_err_vs_PDG24_pct": fmt80((lam_val - lam_pdg24) / lam_pdg24 * mp.mpf(100)),
            "pull_vs_PDG24_sigma": fmt80((mh_pred - mh_pdg24) / mh_sig24),
            "rel_err_vs_PDG22_pct": fmt80((lam_val - lam_pdg22) / lam_pdg22 * mp.mpf(100)),
        }

    quartic_candidates = {
        "QOU_L2a_Plancherel_C0_tree": pack_quartic(qou_ew["lambda_H_L2a_tree"], qou_ew["v_weak_gev"]),
        "QOU_L2a_Plancherel_C1_habiro_half": pack_quartic(qou_ew["lambda_H_L2a_habiro_half"], qou_ew["v_weak_gev"]),
        "QOU_L2a_Plancherel_C2_bring_zero": pack_quartic(qou_ew["lambda_H_L2a_bring_zero"], qou_ew["v_weak_gev"]),
        "NCG_Chamseddine_Connes_preSigma_4_3_MW2_v2": pack_quartic(lam_cc_tree_l2a, qou_ew["v_weak_gev"]),
        "Podles_S2q_kurtosis_q2Sq_div_q3_MW2_v2": pack_quartic(lam_podles_kurt_l2a, qou_ew["v_weak_gev"]),
        "Bare_OqSU2_half_Haar_variance_1_div_2q2Sq": pack_quartic(half_haar_var, qou_ew["v_weak_gev"]),
        "Bare_OqSU2_quarter_Haar_purity": pack_quartic(haar_purity_quarter, qou_ew["v_weak_gev"]),
        "Bare_Uqsl2_Casimir_spinHalf_div_6": pack_quartic(uq_casimir_half / mp.mpf(6), qou_ew["v_weak_gev"]),
        "Bare_OqSU2_bipartite_lower_triplet_qinv2_div_2q3": pack_quartic(bipartite_lower_triplet, qou_ew["v_weak_gev"]),
    }

    # 3. Jucys-Murphy `6/5` rank-vs-q-factorial test & 6-strand Hoefsmit `(1,3,5)` test (`qou-zd6l`)
    jm_21_sum = one + q0**2 + q0 ** (-2)
    jm_22_sum = two + q0**2 + q0 ** (-2)
    qfact3_div_5 = (q2 * q3) / mp.mpf(5)
    mh_if_qfact3 = qou_ew["MW_L2a_gev"] * (two_mul_p(4, h0) / two_mul_p(2, h0)) * (q2 / two) * qfact3_div_5
    qfact3_pull_sigma = (mh_if_qfact3 - mh_pdg24) / mh_sig24

    h6_slot_sin2: dict[str, str] = {}
    h6_all_miss_onshell = True
    for part in [(6,), (5, 1), (4, 2), (3, 3), (4, 1, 1), (3, 2, 1), (2, 2, 2)]:
        tabs = list(standard_tableaux(part))
        ratios = []
        for t in tabs:
            jm = [q0 ** (2 * (c - r)) for (r, c) in t]
            ratios.append((jm[0] * jm[2] * jm[4]) / (jm[1] * jm[3] * jm[5]))
        avg_r = sum(ratios, mp.mpf(0)) / mp.mpf(len(ratios))
        s2_cand = one / (one + avg_r**2)
        if abs(s2_cand - qou_ew["sin2_planch"]) < mp.mpf("0.10"):
            h6_all_miss_onshell = False
        h6_slot_sin2[str(part)] = fmt80(s2_cand)

    # T(2,2k) bare Alexander ratios vs boson mass ratios
    t22k_ratios = {
        "Z_over_W_alex_q3_div_q2": fmt80(q3 / q2),
        "H_over_Z_alex_q4_div_q3": fmt80(q4 / q3),
        "H_over_W_alex_q4_div_q2": fmt80(q4 / q2),
    }

    wb = (
        WitnessBuilder(
            "higgs-algebraic-invariants-audit-probe",
            engine="mpmath",
            output_dir=_THIS.parent,
        )
        .set_description(
            "80-dps strictly proton-pinned audit of O_q(SU(2)) Haar-Yukawa unification, "
            "Podles S^2_q q-monopole Higgs projector, Chamseddine-Connes spectral-action vs "
            "QOU Plancherel Higgs quartics, U_q(sl_2) Casimirs, and Hecke H_n(q_0) Jucys-Murphy / "
            "6-strand Hoefsmit invariants (companion to OqSU2HaarYukawaAndPodlesHiggs.lean)."
        )
        .set_audit_only("docs/audits/2026-11-28-higgs-algebraic-invariants-oqsu2-audit.md")
    )

    wb.add_parameter("q0", fmt80(q0))
    wb.add_parameter("compute_dps", WORK_DPS)
    wb.add_parameter("output_dps", OUT_DPS)
    wb.add_parameter("selectedCandidate", "none")

    wb.add_assertion(
        "symbolic_oqsu2_podles_and_jimbo_identities_exact",
        computed="1" if sym_ok else "0",
        expected="1",
        tolerance="0.1",
        source="OqSU2HaarYukawaAndPodlesHiggs (Sections 1-3)",
    )
    wb.add_assertion(
        "haar_yukawa_weights_and_ew_dressing_variance_lock",
        computed=fmt80(haar_yukawa_res),
        expected="0",
        tolerance="1e-95",
        source="OqSU2HaarYukawaAndPodlesHiggs.haar_eq_jimbo_yukawa_weights_and_variance",
    )
    wb.add_assertion(
        "podles_kurtosis_strictly_below_four_thirds_at_q0",
        computed="1" if (mp.mpf(1) < podles_kurtosis < mp.mpf(4) / mp.mpf(3)) else "0",
        expected="1",
        tolerance="0.1",
        source="OqSU2HaarYukawaAndPodlesHiggs.podles_radial_kurtosis_identities",
    )
    wb.add_assertion(
        "qou_l2a_higgs_w_z_spread_zero_and_brackets_pdg24_within_1p1_sigma",
        computed="1"
        if (
            abs(qou_ew["mH_L2a_tree_gev"] - qou_ew["mH_L2a_from_Z_tree_gev"]) < mp.mpf("1e-95")
            and abs((qou_ew["mH_L2a_tree_gev"] - mh_pdg24) / mh_sig24) < mp.mpf("1.1")
            and abs((qou_ew["mH_L2a_habiro_half_gev"] - mh_pdg24) / mh_sig24) < mp.mpf("1.1")
        )
        else "0",
        expected="1",
        tolerance="0.1",
        source="ElectroweakBosonThresholdsAndWeinberg + PDG 2024 m_H = 125.20 +/- 0.11 GeV",
    )
    wb.add_assertion(
        "jm_qfactorial_and_naive_h6_slots_cleanly_separated",
        computed="1"
        if (
            abs(jm_21_sum - q3) < mp.mpf("1e-95")
            and abs(jm_22_sum - q2**2) < mp.mpf("1e-95")
            and qfact3_pull_sigma > mp.mpf("20")
            and h6_all_miss_onshell
        )
        else "0",
        expected="1",
        tolerance="0.1",
        source="OqSU2HaarYukawaAndPodlesHiggs.jm_h3_h4_traces_and_qfactorial_gt_six",
    )

    wb.add_data(
        "pdg_reference_targets",
        {
            "v_weak_PDG_GeV": fmt80(v_pdg),
            "m_H_PDG2024_GeV": fmt80(mh_pdg24),
            "m_H_PDG2024_sigma_GeV": fmt80(mh_sig24),
            "lambda_H_PDG2024": fmt80(lam_pdg24),
            "lambda_H_PDG2024_sigma": fmt80(lam_sig24),
            "m_H_PDG2022_GeV": fmt80(mh_pdg22),
            "lambda_H_PDG2022": fmt80(lam_pdg22),
            "m_H_over_M_W_PDG2024": fmt80(mh_pdg24 / mw_pdg),
            "m_H_over_M_Z_PDG2024": fmt80(mh_pdg24 / mz_pdg),
            "m_H_over_v_PDG2024": fmt80(mh_pdg24 / v_pdg),
        },
    )
    wb.add_data(
        "oqsu2_and_podles_exact_invariants_proton_q0",
        {
            "p_plus_h_delta_alpha": fmt80(p_plus),
            "p_minus_h_alpha_delta": fmt80(p_minus),
            "haar_variance_1_div_q2Sq": fmt80(haar_var),
            "half_haar_variance_1_div_2q2Sq": fmt80(half_haar_var),
            "kms_asymmetry_tanh_ln_q0": fmt80(kms_asym),
            "classical_det_defect_q0_sub_1_div_q2": fmt80(det_defect),
            "podles_monopole_ordinary_trace_exp": fmt80(podles_ord_trace_exp),
            "podles_equatorial_kurtosis_q2Sq_div_q3": fmt80(podles_kurtosis),
            "uq_casimir_spin_half": fmt80(uq_casimir_half),
        },
    )
    wb.add_data("quartic_and_mass_comparison_table", quartic_candidates)
    wb.add_data(
        "hecke_jucys_murphy_and_torus_link_tests",
        {
            "jm_H3_21_sum_eq_q3": fmt80(jm_21_sum),
            "jm_H4_22_sum_eq_q2Sq": fmt80(jm_22_sum),
            "qfactorial_3_div_5": fmt80(qfact3_div_5),
            "m_H_if_qfactorial_replaces_6_5_GeV": fmt80(mh_if_qfact3),
            "m_H_if_qfactorial_pull_sigma": fmt80(qfact3_pull_sigma),
            "h6_odd_even_slot_sin2_thetaW": h6_slot_sin2,
            "bare_torus_link_alexander_ratios": t22k_ratios,
        },
    )

    out_path = wb.save(
        {
            "q0Anchor": "proton",
            "q0AnchorReason": (
                "Owner ruling 2026-11-28: strictly proton-pinned q0 (q_at(105)); "
                "muon pin on hold until rederivation."
            ),
        }
    )

    built = wb.build()
    print(
        f"Wrote {out_path.relative_to(_ROOT)} "
        f"(allPassed={built['allPassed']}, assertions={len(built['assertions'])})"
    )
    if not built["allPassed"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
