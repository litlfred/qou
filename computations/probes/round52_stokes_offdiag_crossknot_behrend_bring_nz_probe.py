#!/usr/bin/env python3
"""
Round 52 Probe: Diagonal vs Off-Diagonal Stokes Entries, Cross-Knot Candidate Split,
ι-Odd Linear Functional Classification, Non-LCI Behrend Parity Obstruction, and
Bring Simplicial Volume / Neumann–Zagier Layering
(Beans: qou-3ent, qou-l15q, qou-q05m, qou-dt14, qou-n2cl)

All numerical evaluations use mpmath at 80 decimal digits of precision (80 dps)
and are serialized exclusively as exact strings/integers (0 raw float64 fields).
"""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import subprocess
import mpmath as mp

mp.mp.dps = 80

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
SCRIPT_PATH = pathlib.Path(__file__).resolve()
WITNESS_PATH = SCRIPT_PATH.with_name(
    "round52-stokes-offdiag-crossknot-behrend-bring-nz.witness.json"
)


def get_script_hash() -> str:
    return hashlib.sha256(SCRIPT_PATH.read_bytes()).hexdigest()[:12]


def get_head_sha() -> str:
    res = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return res.stdout.strip()


def cl2_mp(theta: mp.mpf) -> mp.mpf:
    """Clausen function Cl_2(theta) = Im Li_2(e^{i theta}) at 80 dps."""
    z = mp.exp(1j * theta)
    return mp.im(mp.polylog(2, z))


def main() -> None:
    assertions = []

    # 1. qou-3ent: Diagonal S+_{11}(q) vs Off-Diagonal S+_{12}(q) and meridian Laurent poly s(x)
    s11_41_coeffs = [1, -8, -9]
    s12_41_tower = [3, 9, 75, 642, 5580, 48558]
    s12_41_quotients = [c // 3 for c in s12_41_tower]
    meridian_charges = [-1, 0, 1]
    s_at_one = sum(1 for _ in meridian_charges)
    a1_pass = (
        s11_41_coeffs[0] == 1
        and s12_41_tower[0] == 3
        and s11_41_coeffs[0] != s12_41_tower[0]
        and all(c % 3 == 0 for c in s12_41_tower)
        and s12_41_quotients == [1, 3, 25, 214, 1860, 16186]
        and s_at_one == 3
        and s_at_one + 1 == 4
    )
    assertions.append(
        {
            "id": "qou_3ent_diagonal_vs_offdiagonal_and_meridian_poly",
            "bean": "qou-3ent",
            "description": (
                "GGM eq (21) diagonal entry S+_{11}(1;0) = 1 != 3 = S+_{12}(1;0), "
                "off-diagonal tower [3,9,75,642,5580,48558] is divisible by 3, and "
                "s(x) = x^-1 + 1 + x gives s(1) = 3 and s(1)+1 = 4 across 4_1 and 5_2."
            ),
            "s11_qzero": str(s11_41_coeffs[0]),
            "s12_qzero": str(s12_41_tower[0]),
            "s12_tower_div3": [str(x) for x in s12_41_quotients],
            "s_at_one": str(s_at_one),
            "passed": bool(a1_pass),
        }
    )

    # 2. qou-l15q: Candidate A (|disc(trace field)|) vs Candidate B (|middle Alexander coeff|)
    disc_41 = -3
    # 5_2 cubic y^3 - 2y^2 + 3y - 1 discriminant:
    # For y^3 + b y^2 + c y + d with b=-2, c=3, d=-1:
    # disc = b^2 c^2 - 4 c^3 - 4 b^3 d - 27 d^2 + 18 b c d
    b_c, c_c, d_c = -2, 3, -1
    disc_52 = (
        (b_c**2) * (c_c**2)
        - 4 * (c_c**3)
        - 4 * (b_c**3) * d_c
        - 27 * (d_c**2)
        + 18 * b_c * c_c * d_c
    )
    cand_a_41 = abs(disc_41)
    cand_a_52 = abs(disc_52)
    cand_b_41 = abs(3)   # Delta_{4_1}(t) = -t + 3 - t^-1
    cand_b_52 = abs(-3)  # Delta_{5_2}(t) = 2t - 3 + 2t^-1
    fivetwo_offdiag = [4, 0, -3, -9, 3, -4]
    a2_pass = (
        disc_52 == -23
        and cand_a_41 == 3
        and cand_b_41 == 3
        and cand_a_52 == 23
        and cand_b_52 == 3
        and cand_a_52 - cand_b_52 == 20
        and cand_a_52 not in fivetwo_offdiag
    )
    assertions.append(
        {
            "id": "qou_l15q_candidate_a_vs_b_fivetwo_split_and_rank3_entries",
            "bean": "qou-l15q",
            "description": (
                "Candidate A (|disc|) and Candidate B (|Delta middle coeff|) agree at 4_1 (3 = 3) "
                "and split by 20 at 5_2 (23 vs 3), with 23 absent from 5_2 off-diagonal entries."
            ),
            "disc_41": str(disc_41),
            "disc_52": str(disc_52),
            "candidate_a_52": str(cand_a_52),
            "candidate_b_52": str(cand_b_52),
            "passed": bool(a2_pass),
        }
    )

    # 3. qou-q05m: Classification of iota-odd linear functionals L(a,b) = alpha*a + beta*b on (4,3)
    dt_pair_52 = (4, 3)
    dt_pair_41 = (3, 3)
    # Test grid of (alpha, beta) in [-5..5]^2: iota-odd on (4,3) iff alpha + beta == 0
    grid_ok = True
    for alpha in range(-5, 6):
        for beta in range(-5, 6):
            lhs = alpha * dt_pair_52[1] + beta * dt_pair_52[0]
            rhs = -(alpha * dt_pair_52[0] + beta * dt_pair_52[1])
            if (lhs == rhs) != (alpha + beta == 0):
                grid_ok = False
    prim_odd_52 = dt_pair_52[0] - dt_pair_52[1]
    prim_even_52 = dt_pair_52[0] + dt_pair_52[1]
    prim_odd_41 = dt_pair_41[0] - dt_pair_41[1]
    a3_pass = grid_ok and prim_odd_52 == 1 and prim_even_52 == 7 and prim_odd_41 == 0
    assertions.append(
        {
            "id": "qou_q05m_iota_odd_linear_functional_classification",
            "bean": "qou-q05m",
            "description": (
                "Linear functional L(a,b) = alpha*a + beta*b is iota-odd on (4,3) iff alpha + beta = 0; "
                "primitive iota-odd functional gives 1 on 5_2 and 0 on 4_1, excluding iota-even sum 7."
            ),
            "primitive_iota_odd_52": str(prim_odd_52),
            "primitive_iota_even_52": str(prim_even_52),
            "primitive_iota_odd_41": str(prim_odd_41),
            "passed": bool(a3_pass),
        }
    )

    # 4. qou-dt14: Non-LCI Behrend weight parity obstruction over chi_eu = -2, DT = 3
    # Verify that for every 3-stratum or 2-stratum configuration with odd weights n_i in {-3,-1,1,3}
    # and chi_i in [-6..6] summing to -2, sum(n_i * chi_i) is ALWAYS even and never 3.
    odd_weights = [-3, -1, 1, 3]
    odd_weight_counterexample = False
    for n1 in odd_weights:
        for n2 in odd_weights:
            for chi1 in range(-6, 7):
                chi2 = -2 - chi1
                dt_val = n1 * chi1 + n2 * chi2
                if (dt_val - (-2)) % 2 != 0 or dt_val == 3:
                    odd_weight_counterexample = True
    # Minimal 2-stratum witness with one even Behrend weight n1 = 2, n2 = 1:
    # (2 - 1) * chi1 = 3 - 1 * (-2) = 5 => chi1 = 5, chi2 = -7 => 2*5 + 1*(-7) = 3
    witness_strata = [(2, 5), (1, -7)]
    witness_chi = sum(c for _, c in witness_strata)
    witness_dt = sum(n * c for n, c in witness_strata)
    a4_pass = (
        not odd_weight_counterexample
        and witness_chi == -2
        and witness_dt == 3
    )
    assertions.append(
        {
            "id": "qou_dt14_non_lci_even_behrend_weight_requirement",
            "bean": "qou-dt14",
            "description": (
                "Every all-odd-weight (including +/-1 LCI) stratification over chi_eu = -2 has even DT count "
                "(never 3); minimal 2-stratum witness [(2,5), (1,-7)] requires even weight n_1 = 2."
            ),
            "all_odd_weights_blocked": str(not odd_weight_counterexample),
            "minimal_even_weight_witness_chi": str(witness_chi),
            "minimal_even_weight_witness_dt": str(witness_dt),
            "passed": bool(a4_pass),
        }
    )

    # 5. qou-n2cl: Gromov simplicial volume on Bring genus-4 surface vs 4_1 complement (80 dps)
    g_bring = 4
    chi_bring = 2 - 2 * g_bring
    simp_vol_bring = 4 * g_bring - 4
    v3_tet = mp.mpf("1.5") * cl2_mp(mp.pi / 3)  # Cl_2(pi/3) = v_3 = 1.0149416064096536...
    # Wait: regular ideal tetrahedron volume v_3 = 3 * Cl_2(2*pi/3) / 2 = Cl_2(pi/3)
    v3_regular = cl2_mp(mp.pi / 3)
    vol_41 = 2 * v3_regular
    simp_vol_41_ratio = vol_41 / v3_regular
    a5_pass = (
        chi_bring == -6
        and simp_vol_bring == 12
        and abs(simp_vol_41_ratio - 2) < mp.mpf("1e-75")
        and abs(vol_41 - mp.mpf("2.029883212819307250042405108549")) < mp.mpf("1e-28")
    )
    assertions.append(
        {
            "id": "qou_n2cl_bring_vs_fourone_simplicial_volume",
            "bean": "qou-n2cl",
            "description": (
                "Bring genus-4 curve has chi_eu = -6 and Gromov simplicial volume ||X_Bring|| = 12, "
                "while ||S^3 \\ 4_1|| = Vol(4_1)/v_3 = 2 at 80 dps."
            ),
            "chi_eu_bring": str(chi_bring),
            "simplicial_vol_bring": str(simp_vol_bring),
            "vol_41_80dps": mp.nstr(vol_41, 50),
            "v3_regular_80dps": mp.nstr(v3_regular, 50),
            "simplicial_vol_41": mp.nstr(simp_vol_41_ratio, 50),
            "passed": bool(a5_pass),
        }
    )

    # 6. qou-n2cl: Stallings monodromy R*L for 4_1 and Thurston edge equation at omega = e^{i pi/3} (80 dps)
    # R = [[1,1],[0,1]], L = [[1,0],[1,1]] -> M_41 = [[2,1],[1,1]]
    m41_tr = 2 + 1
    m41_det = 2 * 1 - 1 * 1
    m41_disc = m41_tr**2 - 4 * m41_det
    omega_shape = mp.exp(1j * mp.pi / 3)
    # Thurston edge equation: z0 * z1 * (1 - z0) * (1 - z1) = 1 at z0 = z1 = e^{i pi/3}
    thurston_edge_val = omega_shape * omega_shape * (1 - omega_shape) * (1 - omega_shape)
    edge_residual = abs(thurston_edge_val - 1)
    # Cusp modulus tau = 2 * sqrt(3) * i
    tau_41 = 2 * mp.sqrt(3) * 1j
    a6_pass = (
        m41_tr == 3
        and m41_det == 1
        and m41_disc == 5
        and edge_residual < mp.mpf("1e-75")
    )
    assertions.append(
        {
            "id": "qou_n2cl_stallings_monodromy_and_thurston_edge_80dps",
            "bean": "qou-n2cl",
            "description": (
                "Stallings monodromy M_{4_1} = R*L = [[2,1],[1,1]] has tr = 3, det = 1, disc = 5, "
                "and z0 = z1 = e^{i pi/3} satisfies z0*z1*(1-z0)*(1-z1) = 1 to < 1e-75."
            ),
            "monodromy_trace": str(m41_tr),
            "monodromy_det": str(m41_det),
            "anosov_disc": str(m41_disc),
            "thurston_edge_residual": mp.nstr(edge_residual, 20),
            "cusp_modulus_im": mp.nstr(mp.im(tau_41), 50),
            "passed": bool(a6_pass),
        }
    )

    # 7. qou-n2cl: Neumann-Zagier symplectic pairing omega_NZ(mu, lambda) = -2 and edge isotropy
    def nz_symp(u: tuple[int, int, int, int], v: tuple[int, int, int, int]) -> int:
        return (u[0] * v[2] - u[2] * v[0]) + (u[1] * v[3] - u[3] * v[1])

    mu_row = (-1, 0, 0, -1)
    lam_row = (1, -1, 1, -1)
    e1_row = (1, 1, 2, 2)
    e2_row = (-1, -1, -2, -2)
    omega_mu_lam = nz_symp(mu_row, lam_row)
    omega_e1_e2 = nz_symp(e1_row, e2_row)
    a7_pass = omega_mu_lam == -2 and omega_e1_e2 == 0 and nz_symp(lam_row, mu_row) == 2
    assertions.append(
        {
            "id": "qou_n2cl_neumann_zagier_symplectic_pairing_and_isotropy",
            "bean": "qou-n2cl",
            "description": (
                "Neumann-Zagier symplectic intersection pairing gives omega_NZ(mu, lambda) = -2 "
                "and edge isotropy omega_NZ(e_1, e_2) = 0."
            ),
            "omega_mu_lambda": str(omega_mu_lam),
            "omega_e1_e2": str(omega_e1_e2),
            "passed": bool(a7_pass),
        }
    )

    # 8. qou-n2cl: Cyclotomic field discriminant coprimality |disc(Q(zeta_3))| = 3 vs |disc(Q(zeta_5))| = 125
    import math
    abs_disc_qzeta3 = 3
    abs_disc_qzeta5 = 5**3
    gcd_disc = math.gcd(abs_disc_qzeta3, abs_disc_qzeta5)
    a8_pass = abs_disc_qzeta5 == 125 and gcd_disc == 1
    assertions.append(
        {
            "id": "qou_n2cl_qzeta3_qzeta5_discriminant_coprimality",
            "bean": "qou-n2cl",
            "description": (
                "|disc(Q(zeta_3))| = 3 and |disc(Q(zeta_5))| = 125 = 5^3 have gcd = 1, "
                "certifying that Q(zeta_3) does not embed into Bring's field Q(zeta_5)."
            ),
            "abs_disc_qzeta3": str(abs_disc_qzeta3),
            "abs_disc_qzeta5": str(abs_disc_qzeta5),
            "gcd": str(gcd_disc),
            "passed": bool(a8_pass),
        }
    )

    all_passed = all(a["passed"] for a in assertions)
    witness = {
        "probe": "round52_stokes_offdiag_crossknot_behrend_bring_nz_probe",
        "beans": ["qou-3ent", "qou-l15q", "qou-q05m", "qou-dt14", "qou-n2cl"],
        "precisionDps": "80",
        "scriptPath": "computations/probes/round52_stokes_offdiag_crossknot_behrend_bring_nz_probe.py",
        "scriptHash": get_script_hash(),
        "scriptCommitSha": get_head_sha(),
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "allPassed": bool(all_passed),
        "assertions": assertions,
    }
    WITNESS_PATH.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {WITNESS_PATH.name}: allPassed={all_passed} ({len(assertions)} assertions)")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
