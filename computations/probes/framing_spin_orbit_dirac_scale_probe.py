#!/usr/bin/env python3
"""80-dps SymPy + mpmath Probe for Categorical Framing Spin-Orbit Scale (`qou-frso`).

Derives over Q(q) in SymPy and tests at 80 decimal places (mp.mp.dps = 80, zero float64,
NO FITTING, q0_comparison at proton default q_p and muon comparison q_mu) the parameter-free
spin-orbit coupling scales induced by QOU's categorical Dirac spatial-Reeb anticommutator
(`CategoricalLagrangianTwoTermBridge.dirac_sq_three_term_expansion`) + ribbon framing
(`def:strand-twist-datum`), scored honestly against:
  (A) Global nuclear magic-shell ladder {2, 8, 20, 28, 50, 82, 126} under BOTH the legacy
      unsubtracted oscillator test (`framing_spin_orbit_magic_probe.py`) and the sharpened
      centroid-subtracted Nilsson test (`nilssonCentroidLevel`, resolving `qou-frso` Next #2),
  (B) 11 experimental single-particle spin-orbit doublet splittings across doubly-magic +/- 1
      cores (15N, 15O, 17O, 17F, 41Ca, 49Ca, 91Zr, 133Sn, 207Pb, 209Pb),
  (C) 7 experimental two-neutron separation shell gaps Delta_{2n}(Z, N_magic) read at 80 dps
      directly from `computations/data/ame2020.mas20.txt` (zero float64 intermediates).

Formalized companion:
  `folio/quantum-observable-universe/lean/QOU/MassTheory/FramingSpinOrbitDiracScale.lean`

Run:
  python3 -u computations/probes/framing_spin_orbit_dirac_scale_probe.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp
from mpmath import mpf

_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(_ROOT / "computations"))
sys.path.insert(0, str(_ROOT / "computations" / "substrate"))
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))

import _path_bridge  # noqa: F401, E402
import codata_constants as cc  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, q_muon_at  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.witness import WitnessBuilder, q0_comparison  # noqa: E402

set_compute_dps()
mp.mp.dps = 80

MAGIC_LIST = [2, 8, 20, 28, 50, 82, 126]
MAGIC_SET = set(MAGIC_LIST)


def fmt80(val: mpf) -> str:
    """Serialize an mpmath mpf to an 80-significant-digit decimal string (zero float64)."""
    return mp.nstr(val, 80)


def parse_ame2020_exact(mas20_path: Path) -> dict[tuple[int, int], tuple[str, int, mpf, mpf, bool]]:
    """Parse AME2020 fixed-width ASCII table directly into 80-dps mpf via string literals."""
    table: dict[tuple[int, int], tuple[str, int, mpf, mpf, bool]] = {}
    with mas20_path.open("r", encoding="utf-8") as fh:
        for line in fh:
            if len(line) < 100 or line[0] not in (" ", "0", "1"):
                continue
            try:
                n_val = int(line[4:9].strip())
                z_val = int(line[9:14].strip())
                a_val = int(line[14:19].strip())
                el = line[20:23].strip()
                bfield = line[54:67].strip()
                ufield = line[68:78].strip()
                if not bfield or bfield == "*":
                    continue
                est = "#" in bfield
                b_per_a_kev = mpf(bfield.replace("#", ""))
                u_per_a_kev = mpf(ufield.replace("#", "")) if ufield and ufield != "*" else mpf(0)
                b_total_mev = b_per_a_kev * mpf(a_val) / mpf(1000)
                u_total_mev = u_per_a_kev * mpf(a_val) / mpf(1000)
                table[(z_val, n_val)] = (el, a_val, b_total_mev, u_total_mev, est)
            except ValueError:
                continue
    return table


def nilsson_centroid_levels(c_so_val: mpf, d_flat_val: mpf, n_max: int = 7) -> list[tuple[mpf, int, int, int, int]]:
    """Centroid-subtracted Nilsson oscillator levels E / hw_0 up to shell n_max."""
    levels: list[tuple[mpf, int, int, int, int]] = []
    for n_sh in range(n_max + 1):
        l2_mean = mpf(n_sh * (n_sh + 3)) / mpf(2)
        for ell in range(n_sh % 2, n_sh + 1, 2):
            j_twice_list = [2 * ell + 1] if ell == 0 else [2 * ell + 1, 2 * ell - 1]
            for tj2 in j_twice_list:
                ls_eig = mpf(ell) / mpf(2) if tj2 == 2 * ell + 1 else -mpf(ell + 1) / mpf(2)
                energy = (
                    mpf(n_sh)
                    + mpf(3) / mpf(2)
                    + d_flat_val * (mpf(ell * (ell + 1)) - l2_mean)
                    + c_so_val * ls_eig
                )
                levels.append((energy, tj2 + 1, n_sh, ell, tj2))
    levels.sort(key=lambda row: row[0])
    return levels


def evaluate_top_gaps(levels: list[tuple[mpf, int, int, int, int]], k: int = 7, upto: int = 140) -> tuple[int, int, list[int]]:
    """Return (magic_hits, false_positives, sorted_top_k_closures) with zero selection bias."""
    cum = 0
    rows: list[tuple[int, mpf]] = []
    for idx, (energy, deg, _, _, _) in enumerate(levels):
        cum += deg
        if cum > upto:
            break
        gap = levels[idx + 1][0] - energy if idx + 1 < len(levels) else mpf(0)
        rows.append((cum, gap))
    top_closures = sorted(c for c, _ in sorted(rows, key=lambda r: -r[1])[:k])
    got = set(top_closures)
    return len(got & MAGIC_SET), len(got - MAGIC_SET), top_closures


def main() -> int:
    mp.mp.dps = 80

    # ------------------------------------------------------------------
    # Part 1: Exact Q(q) Symbolic Derivation in SymPy
    # ------------------------------------------------------------------
    q_sym, ell_sym, m_e_sym = sp.symbols("q ell m_e", nonzero=True)
    qinv_sym = 1 / q_sym

    c_orb_sym = qinv_sym ** 2
    c_so_sym = qinv_sym * (1 - qinv_sym)
    c_reeb_sym = (1 - qinv_sym) ** 2

    diff_partition = sp.simplify(c_orb_sym + 2 * c_so_sym + c_reeb_sym - 1)
    diff_geom_mean = sp.simplify(c_so_sym ** 2 - c_orb_sym * c_reeb_sym)
    diff_step1 = sp.simplify((q_sym - 1) * c_orb_sym - c_so_sym)
    diff_step2 = sp.simplify((q_sym - 1) * c_so_sym - c_reeb_sym)
    diff_kin_so = sp.simplify((q_sym ** 2) * c_so_sym - (q_sym - 1))
    diff_kin_reeb = sp.simplify((q_sym ** 2) * c_reeb_sym - (q_sym - 1) ** 2)

    e0_sym = m_e_sym / (q_sym * (q_sym - 1))
    diff_e0_kin = sp.simplify(e0_sym * (q_sym - 1) - m_e_sym / q_sym)
    diff_e0_raw = sp.simplify(e0_sym * c_so_sym - m_e_sym / (q_sym ** 3))

    casimir = lambda x: x * (x + 1)
    diff_casimir_split = sp.simplify(
        casimir(ell_sym + sp.Rational(1, 2)) - casimir(ell_sym - sp.Rational(1, 2)) - (2 * ell_sym + 1)
    )
    ls_plus = sp.simplify((casimir(ell_sym + sp.Rational(1, 2)) - casimir(ell_sym) - casimir(sp.Rational(1, 2))) / 2)
    ls_minus = sp.simplify((casimir(ell_sym - sp.Rational(1, 2)) - casimir(ell_sym) - casimir(sp.Rational(1, 2))) / 2)
    diff_two_ls = sp.simplify(2 * ls_plus - 2 * ls_minus - (2 * ell_sym + 1))
    diff_multiplet_trace = sp.simplify((2 * ell_sym + 2) * ls_plus + (2 * ell_sym) * ls_minus)

    # Exact rational interval (43/39, 19/17) verification in SymPy at C = -(q-1), D = -(q-1)/4
    c_dirac_expr = -(q_sym - 1)
    d_ws_expr = -(q_sym - 1) / 4
    sym_orbs = []
    for n_sh in range(8):
        l2_avg = sp.Rational(n_sh * (n_sh + 3), 2)
        for ell in range(n_sh % 2, n_sh + 1, 2):
            for tj2 in ([2 * ell + 1] if ell == 0 else [2 * ell + 1, 2 * ell - 1]):
                ls_v = sp.Rational(ell, 2) if tj2 == 2 * ell + 1 else -sp.Rational(ell + 1, 2)
                e_expr = sp.Rational(2 * n_sh + 3, 2) + d_ws_expr * (ell * (ell + 1) - l2_avg) + c_dirac_expr * ls_v
                sym_orbs.append((e_expr.subs(q_sym, sp.Rational(111, 100)), sp.simplify(e_expr), tj2 + 1, (n_sh, ell, tj2)))
    sym_orbs.sort(key=lambda r: (r[0], r[3]))

    lo_q = sp.Rational(1, 1)
    hi_q = sp.Rational(2, 1)
    cum_s = 0
    adj_sym_gaps = []
    for i in range(len(sym_orbs) - 1):
        cum_s += sym_orbs[i][2]
        diff_e = sp.simplify(sym_orbs[i + 1][1] - sym_orbs[i][1])
        a_c = diff_e.coeff(q_sym)
        b_c = diff_e.subs(q_sym, 0)
        if a_c > 0:
            lo_q = max(lo_q, -b_c / a_c)
        elif a_c < 0:
            hi_q = min(hi_q, -b_c / a_c)
        if cum_s <= 140:
            adj_sym_gaps.append((cum_s, diff_e))

    m_sym = [(c, d) for c, d in adj_sym_gaps if c in MAGIC_SET]
    nm_sym = [(c, d) for c, d in adj_sym_gaps if c not in MAGIC_SET]
    lo_strict, hi_strict = lo_q, hi_q
    for _, md in m_sym:
        for _, nd in nm_sym:
            delta_mn = sp.simplify(md - nd)
            a_c = delta_mn.coeff(q_sym)
            b_c = delta_mn.subs(q_sym, 0)
            if a_c > 0:
                lo_strict = max(lo_strict, -b_c / a_c)
            elif a_c < 0:
                hi_strict = min(hi_strict, -b_c / a_c)

    assert diff_partition == 0 and diff_geom_mean == 0
    assert diff_step1 == 0 and diff_step2 == 0 and diff_kin_so == 0 and diff_kin_reeb == 0
    assert diff_e0_kin == 0 and diff_e0_raw == 0
    assert diff_casimir_split == 0 and diff_two_ls == 0 and diff_multiplet_trace == 0
    assert lo_strict == sp.Rational(43, 39) and hi_strict == sp.Rational(19, 17)

    # ------------------------------------------------------------------
    # Part 2: Sharpened Nilsson 7/7 Genericity Scan (Zero float64)
    # ------------------------------------------------------------------
    # Scan C in [-0.300, -0.005] (60 steps of 0.005) x D in [-0.0500, 0] (21 steps of 0.0025)
    total_grid = 0
    seven_hit_pts = 0
    six_plus_c: set[int] = set()
    seven_c: set[int] = set()
    for ci in range(1, 61):
        c_val = -mpf(ci) * mpf(5) / mpf(1000)
        for di in range(0, 21):
            d_val = -mpf(di) * mpf(25) / mpf(10000)
            total_grid += 1
            hits, fps, _ = evaluate_top_gaps(nilsson_centroid_levels(c_val, d_val))
            if hits >= 6:
                six_plus_c.add(ci)
            if hits == 7 and fps == 0:
                seven_hit_pts += 1
                seven_c.add(ci)

    seven_grid_frac = mpf(seven_hit_pts) / mpf(total_grid)
    seven_c_lo = mpf(min(seven_c)) * mpf(5) / mpf(1000)
    seven_c_hi = mpf(max(seven_c)) * mpf(5) / mpf(1000)

    # ------------------------------------------------------------------
    # Part 3: 80-dps Evaluation at Proton and Muon Pins + Empirical Scoring
    # ------------------------------------------------------------------
    q_proton = mpf(Q_50_DIGIT_STR)
    q_muon = q_muon_at(80)

    me_entry = codata("electron mass energy equivalent in MeV")
    mp_entry = codata("proton mass energy equivalent in MeV")
    m_e_mev = mpf(me_entry.value_str)
    m_p_mev = mpf(mp_entry.value_str)
    m_pi_0 = mpf(str(cc.M_PI_0_MEV_VALIDATION))
    m_pi_pm = mpf(str(cc.M_PI_PM_MEV_VALIDATION))
    m_pi_iso = (mpf(2) * m_pi_pm + m_pi_0) / mpf(3)

    # Empirical single-particle spin-orbit doublet splittings (MeV) around doubly-magic cores
    # Sources: Bohr & Mottelson Vol. I Table 2-2; Schwierz, Wiedenhover & Volya (2007), arXiv:0709.3525
    so_doublets = [
        ("15N_1p", 15, 0, 1, mpf("6.3238")),
        ("15O_1p", 15, 0, 1, mpf("6.1763")),
        ("17O_1d", 17, 0, 2, mpf("5.0848")),
        ("17F_1d", 17, 0, 2, mpf("4.9999")),
        ("41Ca_1f", 41, 0, 3, mpf("6.4700")),
        ("49Ca_2p", 49, 1, 1, mpf("2.0230")),
        ("91Zr_2d", 91, 1, 2, mpf("2.0420")),
        ("133Sn_2f", 133, 1, 3, mpf("2.0050")),
        ("207Pb_3p", 207, 2, 1, mpf("0.8977")),
        ("207Pb_2f", 207, 1, 3, mpf("1.7702")),
        ("209Pb_2g", 209, 1, 4, mpf("2.4910")),
    ]

    # Exact 80-dps AME2020 two-neutron separation gaps Delta_{2n}(Z, N) = S_{2n}(Z, N) - S_{2n}(Z, N+2)
    ame_table = parse_ame2020_exact(_ROOT / "computations" / "data" / "ame2020.mas20.txt")
    magic_gap_nuclei = [
        ("16O_N8", 8, 8, 1),
        ("40Ca_N20", 20, 20, 2),
        ("48Ca_N28", 20, 28, 3),
        ("56Ni_N28", 28, 28, 3),
        ("90Zr_N50", 40, 50, 4),
        ("132Sn_N82", 50, 82, 5),
        ("208Pb_N126", 82, 126, 6),
    ]

    ame_shell_gaps: list[dict[str, object]] = []
    for tag, z_v, n_v, ell_intr in magic_gap_nuclei:
        _, a_v, b_0, _, est_0 = ame_table[(z_v, n_v)]
        _, _, b_m2, _, est_m2 = ame_table[(z_v, n_v - 2)]
        _, _, b_p2, _, est_p2 = ame_table[(z_v, n_v + 2)]
        s2n_in = b_0 - b_m2
        s2n_out = b_p2 - b_0
        delta_2n = s2n_in - s2n_out
        ame_shell_gaps.append({
            "nuclide": tag,
            "Z": z_v,
            "N": n_v,
            "A": a_v,
            "intruder_ell": ell_intr,
            "S_2n_at_magic_MeV": fmt80(s2n_in),
            "S_2n_above_magic_MeV": fmt80(s2n_out),
            "Delta_2n_shell_gap_MeV": fmt80(delta_2n),
            "experimental_non_estimated": not (est_0 or est_m2 or est_p2),
        })

    wb = WitnessBuilder("framing-spin-orbit-dirac-scale-probe", engine="sympy")
    wb.set_description(
        "80-dps SymPy + mpmath derivation and zero-fit empirical audit of QOU's categorical "
        "Dirac spatial-Reeb spin-orbit cross-term (`qou-frso`, companion Lean module "
        "`QOU/MassTheory/FramingSpinOrbitDiracScale.lean`): "
        "(1) proves symbolically that (D.q)^2 * D.dirac^2 normalizes horizontal curvature to 1 "
        "and locks the relative spin-orbit coupling to q - 1 (zero independent parameter, "
        "c_SO^2 = c_orb * c_Reeb); "
        "(2) resolves `qou-frso` Next #2 by showing Nilsson's parameter-free shell-centroid "
        "subtraction lifts the 6/7 cap to an exact 7/7 (0 FP) polygon (2.22% of scanned plane, "
        "|C| in [0.105, 0.155]), with q - 1 = 0.109979 inside the 7/7 C-projection and exact "
        "rational q-window (43/39, 19/17) under the explicit §3b-cond Woods-Saxon ratio D = -C/4 "
        "(while bare D = -(q-1)^2 fails 28 vs 40 unconditionally); "
        "(3) tests all zero-parameter MeV spin-orbit scale candidates at both q_p and q_mu "
        "against 11 experimental spin-orbit doublets and 7 AME2020 two-neutron magic gaps."
    )

    # Symbolic assertions
    wb.add_assertion(
        name="dirac_weights_partition_and_zero_discriminant_symbolic",
        computed=str(int(diff_partition) + abs(int(diff_geom_mean))),
        expected="0",
        tolerance="0",
        source="c_orb + 2*c_so + c_reeb == 1 and c_so^2 == c_orb * c_reeb over Q(q)",
    )
    wb.add_assertion(
        name="kinetic_normalized_dirac_so_ratio_equals_q_minus_1",
        computed=str(int(diff_kin_so) + abs(int(diff_kin_reeb))),
        expected="0",
        tolerance="0",
        source="q^2 * c_so == q - 1 and q^2 * c_reeb == (q - 1)^2 over Q(q)",
    )
    wb.add_assertion(
        name="ribbon_casimir_and_multiplet_centroid_identities",
        computed=str(int(diff_casimir_split) + abs(int(diff_two_ls)) + abs(int(diff_multiplet_trace))),
        expected="0",
        tolerance="0",
        source="C(l+1/2)-C(l-1/2) == 2l+1, 2(l.s)_+ - 2(l.s)_- == 2l+1, multiplet trace == 0",
    )
    wb.add_assertion(
        name="sharpened_nilsson_criterion_reaches_exact_7_of_7",
        computed="1" if seven_hit_pts > 0 else "0",
        expected="1",
        tolerance="0",
        source=f"Nilsson centroid-subtracted top-7 gap test hits 7/7 (0 FP) at {seven_hit_pts}/{total_grid} grid pts",
    )

    wb.add_data("symbolic_q_identities", {
        "c_orb": "q^-2",
        "c_so": "q^-1 * (1 - q^-1)",
        "c_reeb": "(1 - q^-1)^2",
        "kinetic_normalized_so_coupling": "q - 1",
        "kinetic_normalized_reeb_weight": "(q - 1)^2",
        "hadronic_scale_E0_mul_q_minus_1": "m_e / q",
        "hadronic_scale_E0_mul_c_so": "m_e / q^3",
        "exact_7_of_7_rational_q_interval_under_D_eq_neg_C_div_4": [str(lo_strict), str(hi_strict)],
        "nilsson_7_of_7_grid_points": seven_hit_pts,
        "nilsson_total_grid_points": total_grid,
        "nilsson_7_of_7_grid_fraction": fmt80(seven_grid_frac),
        "nilsson_7_of_7_abs_C_range": [fmt80(seven_c_lo), fmt80(seven_c_hi)],
    })
    wb.add_data("ame2020_two_neutron_magic_gaps", ame_shell_gaps)

    pins_out: dict[str, object] = {}

    print("=" * 92)
    print("80-DPS CATEGORICAL FRAMING SPIN-ORBIT SCALE & NILSSON MAGIC-SHELL PROBE (`qou-frso`)")
    print("=" * 92)
    print(f"  Symbolic Q(q) checks (partition, geom-mean, q^2 norm, 2l+1) : ALL ZERO DIFF")
    print(
        f"  Sharpened Nilsson centroid-subtracted 7/7 (0 FP) polygon    : "
        f"{seven_hit_pts}/{total_grid} pts ({mp.nstr(seven_grid_frac * 100, 4)}%), "
        f"|C| in [{mp.nstr(seven_c_lo, 4)}, {mp.nstr(seven_c_hi, 4)}]"
    )
    print(f"  Exact rational q-window for 7/7 under D = -(q-1)/4 (§3b-cond): ({lo_strict}, {hi_strict})")
    print()

    for pin_name, q_val in [("proton", q_proton), ("muon", q_muon)]:
        inv_q = mpf(1) / q_val
        hbar_q = mpf(1) - inv_q
        c_orb = inv_q ** 2
        c_so = inv_q * hbar_q
        c_reeb = hbar_q ** 2
        eta_dirac = q_val - mpf(1)
        e0_mev = m_e_mev / (q_val * (q_val - mpf(1)))
        hw00_pion_iso = mpf(2) * (m_pi_iso ** 2) / m_p_mev

        in_rational_window = (mpf(43) / mpf(39)) < q_val < (mpf(19) / mpf(17))

        # Dimensionless shell-closure tests (pure algebraic vs §3b-cond Woods-Saxon D = -C/4)
        hits_bare, fps_bare, closures_bare = evaluate_top_gaps(
            nilsson_centroid_levels(-eta_dirac, -(eta_dirac ** 2))
        )
        hits_cond, fps_cond, closures_cond = evaluate_top_gaps(
            nilsson_centroid_levels(-eta_dirac, -eta_dirac / mpf(4))
        )
        hits_raw_cso, fps_raw_cso, closures_raw_cso = evaluate_top_gaps(
            nilsson_centroid_levels(-c_so, -c_so / mpf(4))
        )

        wb.add_assertion(
            name=f"pin_{pin_name}_inside_exact_rational_7_of_7_window",
            computed="1" if (in_rational_window and hits_cond == 7 and fps_cond == 0) else "0",
            expected="1",
            tolerance="0",
            source=f"43/39 < q_{pin_name} < 19/17 and Nilsson(C=-(q-1), D=-(q-1)/4) gives 7/7 (0 FP)",
        )
        wb.add_assertion(
            name=f"pin_{pin_name}_bare_reeb_flatness_prune_verified",
            computed="1" if (40 in closures_bare and 28 not in closures_bare) else "0",
            expected="1",
            tolerance="0",
            source="Unconditional prune: bare D = -(q-1)^2 leaves HO 40 > intruder 28",
        )

        # Score zero-parameter MeV spin-orbit scale candidates across the 11 doublets
        v_reeb_surface_mev = m_p_mev * c_reeb  # m_p * (1 - q^-1)^2
        v_dirac_cross_hb_mev = m_p_mev * c_so * hbar_q  # m_p * q^-1 * (1 - q^-1)^2
        v_two_e0_mev = mpf(2) * e0_mev  # 2 * m_e / (q(q-1))
        v_e0_kin_mev = e0_mev * eta_dirac  # m_e / q

        candidate_defs = [
            (
                "reeb_surface_mp_hbar2_A_neg2_3",
                "m_p * (1 - q^-1)^2 * (2l + 1) * A^{-2/3} [Thomas/Reeb surface scaling]",
                lambda a_num, ell: v_reeb_surface_mev * mpf(2 * ell + 1) * (mpf(a_num) ** (-mpf(2) / mpf(3))),
            ),
            (
                "dirac_cross_mp_qinv_hbar2_A_neg2_3",
                "m_p * q^-1 * (1 - q^-1)^2 * (2l + 1) * A^{-2/3} [Dirac cross * Reeb surface]",
                lambda a_num, ell: v_dirac_cross_hb_mev * mpf(2 * ell + 1) * (mpf(a_num) ** (-mpf(2) / mpf(3))),
            ),
            (
                "hadronic_2E0_A_neg2_3",
                "2 * E_0(q) * (2l + 1) * A^{-2/3} [2 m_e / (q(q-1)) surface scaling]",
                lambda a_num, ell: v_two_e0_mev * mpf(2 * ell + 1) * (mpf(a_num) ** (-mpf(2) / mpf(3))),
            ),
            (
                "nilsson_pion_compton_dirac_ratio_A_neg1_3",
                "(q - 1) * (l + 1/2) * (2 m_pi^2 / m_p) * A^{-1/3} [Pion-Compton oscillator]",
                lambda a_num, ell: eta_dirac * (mpf(2 * ell + 1) / mpf(2)) * hw00_pion_iso * (mpf(a_num) ** (-mpf(1) / mpf(3))),
            ),
            (
                "bare_1d_hadronic_E0_mul_q_minus_1_no_A",
                "E_0(q) * (q - 1) * (2l + 1) = (m_e / q) * (2l + 1) [1D unscaled electronic]",
                lambda _a_num, ell: v_e0_kin_mev * mpf(2 * ell + 1),
            ),
        ]

        model_scores: dict[str, object] = {}
        for key, desc, fn in candidate_defs:
            per_doublet = []
            rel_all = []
            rel_heavy = []
            for d_tag, a_num, n_rad, ell, de_exp in so_doublets:
                pred = fn(a_num, ell)
                rel_err = (pred - de_exp) / de_exp
                rel_all.append(abs(rel_err))
                if a_num >= 41:
                    rel_heavy.append(abs(rel_err))
                per_doublet.append({
                    "doublet": d_tag,
                    "A": a_num,
                    "n_radial": n_rad,
                    "ell": ell,
                    "exp_MeV": fmt80(de_exp),
                    "pred_MeV": fmt80(pred),
                    "rel_err_pct": fmt80(rel_err * mpf(100)),
                })
            mare_all = sum(rel_all) / mpf(len(rel_all)) * mpf(100)
            mare_heavy = sum(rel_heavy) / mpf(len(rel_heavy)) * mpf(100)
            model_scores[key] = {
                "formula": desc,
                "mare_all_11_doublets_pct": fmt80(mare_all),
                "mare_A_ge_41_7_doublets_pct": fmt80(mare_heavy),
                "doublets": per_doublet,
            }

        pins_out[pin_name] = {
            "q0": fmt80(q_val),
            "hbar_q": fmt80(hbar_q),
            "c_orb_qinv2": fmt80(c_orb),
            "c_so_qinv_hbar": fmt80(c_so),
            "c_reeb_hbar2": fmt80(c_reeb),
            "kinetic_normalized_so_ratio_q_minus_1": fmt80(eta_dirac),
            "hadronic_scale_E0_MeV": fmt80(e0_mev),
            "reeb_surface_coeff_mp_hbar2_MeV": fmt80(v_reeb_surface_mev),
            "dirac_cross_hb_coeff_mp_qinv_hbar2_MeV": fmt80(v_dirac_cross_hb_mev),
            "two_E0_MeV": fmt80(v_two_e0_mev),
            "pion_compton_hw00_iso_MeV": fmt80(hw00_pion_iso),
            "inside_rational_7_of_7_window_43_39_to_19_17": in_rational_window,
            "closures_bare_D_eq_neg_q_minus_1_sq": {
                "hits": hits_bare,
                "false_positives": fps_bare,
                "top_7": closures_bare,
            },
            "closures_conditional_D_eq_neg_q_minus_1_div_4": {
                "hits": hits_cond,
                "false_positives": fps_cond,
                "top_7": closures_cond,
            },
            "closures_unnormalized_c_so_with_D_eq_neg_c_so_div_4": {
                "hits": hits_raw_cso,
                "false_positives": fps_raw_cso,
                "top_7": closures_raw_cso,
            },
            "zero_parameter_mev_spin_orbit_models": model_scores,
        }

        print(f"--- PIN: {pin_name.upper()} (q0 = {mp.nstr(q_val, 24)}) ---")
        print(
            f"  Dirac weights (c_orb, c_so, c_reeb) : "
            f"({mp.nstr(c_orb, 10)}, {mp.nstr(c_so, 10)}, {mp.nstr(c_reeb, 10)})"
        )
        print(f"  Kinetic-normalized SO ratio (q - 1) : {mp.nstr(eta_dirac, 14)}")
        print(
            f"  Closure test [bare D = -(q-1)^2]    : {hits_bare}/7 hits, {fps_bare} FP -> {closures_bare}"
        )
        print(
            f"  Closure test [§3b-cond D = -(q-1)/4]: {hits_cond}/7 hits, {fps_cond} FP -> {closures_cond}"
        )
        print(
            f"  Closure test [raw C = -c_so, -c_so/4]: {hits_raw_cso}/7 hits, {fps_raw_cso} FP -> {closures_raw_cso}"
        )
        print(
            f"  MeV scales: m_p*hbar_q^2 = {mp.nstr(v_reeb_surface_mev, 8)} MeV | "
            f"2*E_0 = {mp.nstr(v_two_e0_mev, 8)} MeV | "
            f"hw00(pi) = {mp.nstr(hw00_pion_iso, 8)} MeV"
        )
        for key, _, _ in candidate_defs:
            sc = model_scores[key]
            print(
                f"    {key:42s}: all-11 MARE = {mp.nstr(mpf(sc['mare_all_11_doublets_pct']), 4):>6s}% | "
                f"A>=41 MARE = {mp.nstr(mpf(sc['mare_A_ge_41_7_doublets_pct']), 4):>6s}%"
            )
        print()

    wb.add_data("pins", pins_out)
    wb.add_caveat(
        "Unconditional vs. conditional boundary (`qou-frso`): "
        "(1) The 2l+1 Landé/Casimir shape and the kinetic-normalized Dirac cross-term ratio "
        "|C_Dirac| = c_SO / c_orb = q - 1 = 0.109979 are derived parameter-free; "
        "(2) Under Nilsson's centroid-subtracted oscillator, |C_Dirac| = q - 1 lands inside "
        "the narrow [0.105, 0.155] 7/7-admissible interval (whereas raw c_SO = 0.08926 falls "
        "below 0.105 and gives 5/7), BUT achieving 7/7 (0 FP) requires the 3D Woods-Saxon "
        "surface-flatness ratio D = -(q - 1)/4 (`RadialSpinOrbitReductionHypothesis`, §3b-cond), "
        "since bare algebraic D = -(q - 1)^2 gives 5/7 (40 > 28); "
        "(3) In MeV, zero-parameter surface scaling m_p*(1 - q^-1)^2*(2l+1)*A^{-2/3} matches "
        "A >= 41 spin-orbit doublets to 10.68% MARE (18.69% across all 11 doublets), leaving "
        "radial node (n_r) matrix elements open until the 3D nuclear wave-function reduction "
        "is derived."
    )

    out_path = wb.save(
        q0_comparison(
            muon=mp.nstr(q_muon, 50),
            proton=Q_50_DIGIT_STR,
            reason=(
                "evaluates QOU's parameter-free Dirac spatial-Reeb spin-orbit coupling ratio "
                "(q - 1), sharpened 7/7 Nilsson closure tests, and dimensionful MeV spin-orbit "
                "scales against 11 nuclear doublets and 7 AME2020 shell gaps at both q_p and q_mu"
            ),
        )
    )
    print(f"Witness written to: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
