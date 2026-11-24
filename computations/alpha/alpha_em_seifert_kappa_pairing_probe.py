#!/usr/bin/env python3
"""80-dps SymPy + mpmath Probe for the Homological Seifert Pairing Ratio kappa_Seifert(q).

Evaluates and verifies symbolically (SymPy exact rational/Laurent arithmetic) and
numerically at 80 decimal places (mp.mp.dps = 80, zero float64, NO FITTING):

1. Exact 8x8 Milnor/Seifert matrices on H_1(Sigma_4; Z) ~= Z^8 (b_1(Sigma_4) = 8)
   for the force-carrier torus knots T(2,9) and T(3,5):
     V_k in Z^{(k-1)x(k-1)},  (V_k)_{i,i} = 1,  (V_k)_{i,i+1} = -1,
     V_{2,9} = V_2 (x) V_9 in Z^{8x8},
     V_{3,5} = V_3 (x) V_5 in Z^{8x8}.

2. Exact symbolic identities (diff == 0):
   - det(t V_{2,9} - V_{2,9}^T) = (t^2 - t + 1)(t^6 - t^3 + 1),
   - det(t V_{3,5} - V_{3,5}^T) = t^8 - t^7 + t^5 - t^4 + t^3 - t + 1,
   - det(V_{2,9} - V_{2,9}^T) = 1 and det(V_{3,5} - V_{3,5}^T) = 1,
   - Balanced Alexander polynomials (Delta_K(1) = 1, Delta_K(q^-1) = Delta_K(q)):
       Delta_{T(2,9)}(q) = (q - 1 + q^-1)(q^3 - 1 + q^-3),
       Delta_{T(3,5)}(q) = q^4 - q^3 + q - 1 + q^-1 - q^-3 + q^-4,
   - Homological Seifert determinant ratio at the horizontal Dirac scale u = q^-1:
       kappa_Seifert(q)
         := [det(V_{2,9} - V_{2,9}^T) det(V_{3,5} - V_{3,5}^T)]
            / [det(V_{2,9} - q^-1 V_{2,9}^T) det(V_{3,5} - q^-1 V_{3,5}^T)]
          = q^{b_1(Sigma_4)} / (Delta_{T(2,9)}(q) * Delta_{T(3,5)}(q))   (b_1(Sigma_4) = 8).

3. 80-dps evaluation at BOTH registered substrate pins (proton default q_p and
   muon comparison q_mu, scored against CODATA-2022 1/alpha_EM read from
   qou_substrate.codata):
   - At q_p: kappa_Seifert(q_p) = 1.90515532823217... (-0.5304% from exact-closure
     kappa_needed = 1.915314296..., strictly inside the [1.8739, 1.9567] 100-ppb
     window missed by all 16 naive [m]_q substitutions into Witten's 2x2 ansatz),
     yielding resummed 1/alpha_EM = 137.0359958150852... (-24.53 ppb, 19.06x closer
     than Witten's -467.64 ppb, though 67.17x larger in magnitude than the additive
     Bring zero-mode Form B residual of -0.3652 ppb, and still conditional/unproved
     as the Chern-Simons J^2 Jacobian).
   - At q_mu: kappa_Seifert(q_mu) = 1.90515542693417..., resummed
     1/alpha_EM = 137.0360067360907..., residual +55.16 ppb.

Run:
  python3 -u computations/alpha/alpha_em_seifert_kappa_pairing_probe.py
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
from _precision import set_compute_dps  # noqa: E402
from meson_em_sinh_closed_form import _alpha_em_inv_derived  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, q_muon_at  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.witness import WitnessBuilder, q0_comparison  # noqa: E402

set_compute_dps()
mp.mp.dps = 80

B1_BRING = 8  # b_1(Sigma_4) = 2g = 8 at genus g = 4


def fmt80(val: mpf) -> str:
    """Serialize an mpmath mpf to an 80-significant-digit decimal string (zero float64)."""
    return mp.nstr(val, 80)


def seifert_chain(k: int) -> sp.Matrix:
    """Standard (k-1)x(k-1) Seifert chain matrix V_k with (V_k)_{i,i}=1, (V_k)_{i,i+1}=-1."""
    n = k - 1
    entries = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(sp.Integer(1))
            elif j == i + 1:
                row.append(sp.Integer(-1))
            else:
                row.append(sp.Integer(0))
        entries.append(row)
    return sp.Matrix(entries)


def q_bal(k: int, q: mpf) -> mpf:
    """Balanced quantum integer [k]_q = (q^k - q^-k) / (q - q^-1)."""
    return (q ** k - q ** (-k)) / (q - mpf(1) / q)


def cs_torus_classical(m: int, n: int) -> mpf:
    """Classical Chern-Simons invariant CS(T_{m,n}) = pi^2 (m^2 - 1)(n^2 - 1) / (12 m n)."""
    num = mpf((m * m - 1) * (n * n - 1))
    den = mpf(12 * m * n)
    return (mp.pi ** 2) * num / den


def delta_cs(q: mpf) -> mpf:
    """First-order Chern-Simons descent ratio delta_CS(q) from rem:em-coupling-chern-simons."""
    bare_val = q * q_bal(9, q) * q_bal(10, q)
    hbar_q = mpf(1) - mpf(1) / q
    cs_sum = cs_torus_classical(2, 9) + cs_torus_classical(3, 5)
    return cs_sum * (q_bal(2, q) / mpf(2)) * (hbar_q ** 2) / bare_val


def delta_alex_t29(q: mpf) -> mpf:
    """Balanced Alexander polynomial Delta_{T(2,9)}(q) = (q - 1 + q^-1)(q^3 - 1 + q^-3)."""
    inv_q = mpf(1) / q
    return (q - mpf(1) + inv_q) * (q ** 3 - mpf(1) + inv_q ** 3)


def delta_alex_t35(q: mpf) -> mpf:
    """Balanced Alexander polynomial Delta_{T(3,5)}(q) = q^4 - q^3 + q - 1 + q^-1 - q^-3 + q^-4."""
    inv_q = mpf(1) / q
    return (q ** 4) - (q ** 3) + q - mpf(1) + inv_q - (inv_q ** 3) + (inv_q ** 4)


def seifert_det_mp(V: sp.Matrix, u: mpf) -> mpf:
    """Evaluate det(V - u * V^T) directly in 80-dps mpmath from exact integer matrix V."""
    n = V.rows
    M = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            M[i, j] = mpf(int(V[i, j])) - u * mpf(int(V[j, i]))
    return mp.det(M)


def solve_form_b_hhecke_sq(q: mpf) -> mpf:
    """Form B reference (BringSchwingerNormalizationDerivation):
    1/alpha = q[9]_q[10]_q + 2/(3*pi) + alpha * ([2]_q/(8*pi)) * (1 - h_Hecke(q)^2 * alpha),
    where h_Hecke(q) = q - q^-1 is the bar-Hermitian skein 2-vertex contraction."""
    T_const = q * q_bal(9, q) * q_bal(10, q) + mpf(2) / (mpf(3) * mp.pi)
    H_norm = q_bal(2, q) / (mpf(8) * mp.pi)
    c_loop = (q - mpf(1) / q) ** 2

    def cubic(a: mpf) -> mpf:
        return -c_loop * H_norm * (a ** 3) + H_norm * (a ** 2) + T_const * a - mpf(1)

    a_root = mp.findroot(cubic, mpf(1) / T_const)
    return mpf(1) / a_root


def main() -> int:
    mp.mp.dps = 80

    # ------------------------------------------------------------------
    # Part 1: Exact SymPy construction & symbolic determinant identities
    # ------------------------------------------------------------------
    V2 = seifert_chain(2)
    V9 = seifert_chain(9)
    V3 = seifert_chain(3)
    V5 = seifert_chain(5)

    V29 = sp.kronecker_product(V2, V9)
    V35 = sp.kronecker_product(V3, V5)

    assert V29.shape == (B1_BRING, B1_BRING), f"Expected 8x8 for V29, got {V29.shape}"
    assert V35.shape == (B1_BRING, B1_BRING), f"Expected 8x8 for V35, got {V35.shape}"

    t, q_sym = sp.symbols("t q", nonzero=True)

    poly_29 = sp.expand((t * V29 - V29.T).det())
    target_29 = sp.expand((t ** 2 - t + 1) * (t ** 6 - t ** 3 + 1))
    diff_poly_29 = sp.expand(poly_29 - target_29)

    poly_35 = sp.expand((t * V35 - V35.T).det())
    target_35 = sp.expand(t ** 8 - t ** 7 + t ** 5 - t ** 4 + t ** 3 - t + 1)
    diff_poly_35 = sp.expand(poly_35 - target_35)

    det_cl_29 = int((V29 - V29.T).det())
    det_cl_35 = int((V35 - V35.T).det())

    # Balanced Alexander polynomials in SymPy
    delta_29_sym = sp.cancel((q_sym - 1 + 1 / q_sym) * (q_sym ** 3 - 1 + 1 / (q_sym ** 3)))
    delta_35_sym = sp.cancel(
        q_sym ** 4 - q_sym ** 3 + q_sym - 1 + 1 / q_sym - 1 / (q_sym ** 3) + 1 / (q_sym ** 4)
    )
    diff_bal_29 = sp.simplify((q_sym ** (-4)) * poly_29.subs(t, q_sym) - delta_29_sym)
    diff_bal_35 = sp.simplify((q_sym ** (-4)) * poly_35.subs(t, q_sym) - delta_35_sym)
    delta_29_at_1 = int(sp.simplify(delta_29_sym.subs(q_sym, 1)))
    delta_35_at_1 = int(sp.simplify(delta_35_sym.subs(q_sym, 1)))

    # Horizontal Dirac parameter u = q^{-1}
    det_qinv_29 = (V29 - (1 / q_sym) * V29.T).det()
    det_qinv_35 = (V35 - (1 / q_sym) * V35.T).det()
    kappa_det_sym = sp.cancel((det_cl_29 * det_cl_35) / (det_qinv_29 * det_qinv_35))
    kappa_closed_sym = sp.cancel((q_sym ** B1_BRING) / (delta_29_sym * delta_35_sym))
    diff_kappa_identity = sp.simplify(sp.cancel(kappa_det_sym - kappa_closed_sym))

    assert diff_poly_29 == 0, f"Alexander T(2,9) mismatch: {diff_poly_29}"
    assert diff_poly_35 == 0, f"Alexander T(3,5) mismatch: {diff_poly_35}"
    assert det_cl_29 == 1 and det_cl_35 == 1, f"Unimodular check failed: {det_cl_29}, {det_cl_35}"
    assert diff_bal_29 == 0 and diff_bal_35 == 0, "Balanced Alexander identity failed"
    assert delta_29_at_1 == 1 and delta_35_at_1 == 1, "Delta_K(1) == 1 check failed"
    assert diff_kappa_identity == 0, f"kappa_Seifert identity mismatch: {diff_kappa_identity}"

    # ------------------------------------------------------------------
    # Part 2: 80-dps numerical evaluation at proton and muon pins
    # ------------------------------------------------------------------
    q_proton = mpf(Q_50_DIGIT_STR)
    q_muon = q_muon_at(80)

    alpha_entry = codata("inverse fine-structure constant")
    alpha_inv_c22 = mpf(alpha_entry.value_str)
    alpha_inv_c22_sig = mpf(alpha_entry.uncertainty_str)
    alpha_inv_c22_sig_ppb = alpha_inv_c22_sig / alpha_inv_c22 * mpf("1e9")

    wb = WitnessBuilder("alpha-em-seifert-kappa-pairing", engine="sympy")
    wb.set_content_block("rem:em-coupling-chern-simons")
    wb.set_description(
        "80-dps SymPy + mpmath verification of the 8x8 homological Milnor/Seifert pairing "
        "ratio kappa_Seifert(q) = det(V_{2,9} - V_{2,9}^T) det(V_{3,5} - V_{3,5}^T) / "
        "[det(V_{2,9} - q^-1 V_{2,9}^T) det(V_{3,5} - q^-1 V_{3,5}^T)] = "
        "q^{b_1(Sigma_4)} / (Delta_{T(2,9)}(q) Delta_{T(3,5)}(q)) on H_1(Sigma_4; Z) ~= Z^8 "
        "(b_1 = 8) at both registered substrate pins (q_proton default and q_muon comparison), "
        "contrasted against Witten's 2x2 ansatz and Form B Bring zero-mode."
    )

    # Record symbolic assertions (exact integer / zero-polynomial checks)
    wb.add_assertion(
        name="alexander_poly_T29_symbolic_diff_zero",
        computed=str(int(diff_poly_29)),
        expected="0",
        tolerance="0",
        source="det(t V_{2,9} - V_{2,9}^T) - (t^2 - t + 1)(t^6 - t^3 + 1) == 0",
    )
    wb.add_assertion(
        name="alexander_poly_T35_symbolic_diff_zero",
        computed=str(int(diff_poly_35)),
        expected="0",
        tolerance="0",
        source="det(t V_{3,5} - V_{3,5}^T) - (t^8 - t^7 + t^5 - t^4 + t^3 - t + 1) == 0",
    )
    wb.add_assertion(
        name="seifert_classical_unimodular_det_one",
        computed=str(det_cl_29 * det_cl_35),
        expected="1",
        tolerance="0",
        source="det(V_{2,9} - V_{2,9}^T) == 1 and det(V_{3,5} - V_{3,5}^T) == 1",
    )
    wb.add_assertion(
        name="kappa_seifert_closed_form_symbolic_diff_zero",
        computed=str(int(diff_kappa_identity)),
        expected="0",
        tolerance="0",
        source="kappa_Seifert(q) - q^8 / (Delta_{T(2,9)}(q) * Delta_{T(3,5)}(q)) == 0",
    )

    wb.add_data("symbolic_identities", {
        "homology_rank_b1_Sigma4": B1_BRING,
        "V29_shape": list(V29.shape),
        "V35_shape": list(V35.shape),
        "V29_entries": [[int(V29[i, j]) for j in range(B1_BRING)] for i in range(B1_BRING)],
        "V35_entries": [[int(V35[i, j]) for j in range(B1_BRING)] for i in range(B1_BRING)],
        "det_tV29_minus_V29T": str(poly_29),
        "det_tV35_minus_V35T": str(poly_35),
        "det_V29_minus_V29T_at_1": det_cl_29,
        "det_V35_minus_V35T_at_1": det_cl_35,
        "Delta_T29_at_1": delta_29_at_1,
        "Delta_T35_at_1": delta_35_at_1,
        "kappa_Seifert_closed_form": "q^8 / ((q - 1 + q^-1)*(q^3 - 1 + q^-3)*(q^4 - q^3 + q - 1 + q^-1 - q^-3 + q^-4))",
        "symbolic_diff_poly_29": str(diff_poly_29),
        "symbolic_diff_poly_35": str(diff_poly_35),
        "symbolic_diff_kappa_identity": str(diff_kappa_identity),
    })

    pin_results: dict[str, dict[str, object]] = {}

    print("=" * 88)
    print("80-DPS HOMOLOGICAL SEIFERT PAIRING PROBE FOR CHERN-SIMONS KAPPA (b_1(Sigma_4) = 8)")
    print("=" * 88)
    print(f"  Symbolic check det(t V_29 - V_29^T) diff : {diff_poly_29}")
    print(f"  Symbolic check det(t V_35 - V_35^T) diff : {diff_poly_35}")
    print(f"  Symbolic check det(V_K - V_K^T) at t=1   : ({det_cl_29}, {det_cl_35})")
    print(f"  Symbolic check kappa_Seifert closed form : diff = {diff_kappa_identity}")
    print(
        f"  CODATA-2022 1/alpha_EM                   : {alpha_entry.value_str} +/- "
        f"{alpha_entry.uncertainty_str} ({mp.nstr(alpha_inv_c22_sig_ppb, 6)} ppb)"
    )
    print()

    for pin_name, q_val in [("proton", q_proton), ("muon", q_muon)]:
        inv_q = mpf(1) / q_val
        bare_val = q_val * q_bal(9, q_val) * q_bal(10, q_val)
        d_cs = delta_cs(q_val)

        # Direct matrix determinants vs balanced Alexander closed form
        det_29_qinv = seifert_det_mp(V29, inv_q)
        det_35_qinv = seifert_det_mp(V35, inv_q)
        kappa_from_det = mpf(det_cl_29 * det_cl_35) / (det_29_qinv * det_35_qinv)

        d29_val = delta_alex_t29(q_val)
        d35_val = delta_alex_t35(q_val)
        kappa_from_alex = (q_val ** B1_BRING) / (d29_val * d35_val)

        # Opposite orientation u = q check (gives q^{-8}/(Delta_29 Delta_35) < 1)
        kappa_u_eq_q = (q_val ** (-B1_BRING)) / (d29_val * d35_val)

        # Exact-closure kappa_needed for CODATA-2022 at this pin (diagnostic reference only, NOT used in prediction)
        target_shift = alpha_inv_c22 / bare_val - mpf(1)
        kappa_needed = (mpf(1) - d_cs / target_shift) / d_cs
        kappa_rel_diff_pct = (kappa_from_alex - kappa_needed) / kappa_needed * mpf(100)

        # 100-ppb window [kappa_lo_100ppb, kappa_hi_100ppb] around CODATA-2022
        alpha_lo = alpha_inv_c22 * (mpf(1) - mpf("1e-7"))
        alpha_hi = alpha_inv_c22 * (mpf(1) + mpf("1e-7"))
        kappa_lo_100ppb = (mpf(1) - d_cs / (alpha_lo / bare_val - mpf(1))) / d_cs
        kappa_hi_100ppb = (mpf(1) - d_cs / (alpha_hi / bare_val - mpf(1))) / d_cs
        inside_100ppb_window = kappa_lo_100ppb <= kappa_from_alex <= kappa_hi_100ppb

        # Resummed CS tower with kappa_Seifert(q)
        tower_ratio_seifert = d_cs * kappa_from_alex
        alpha_inv_seifert = bare_val * (mpf(1) + d_cs / (mpf(1) - tower_ratio_seifert))
        err_seifert_ppb = (alpha_inv_seifert - alpha_inv_c22) / alpha_inv_c22 * mpf("1e9")
        err_seifert_sigma = (alpha_inv_seifert - alpha_inv_c22) / alpha_inv_c22_sig

        # Witten 2x2 ansatz comparison (imported canonical implementation)
        alpha_inv_witten = _alpha_em_inv_derived(q_val)
        err_witten_ppb = (alpha_inv_witten - alpha_inv_c22) / alpha_inv_c22 * mpf("1e9")

        # Form B additive Bring zero-mode + 1-loop bar-Hermitian skein comparison
        alpha_inv_form_b = solve_form_b_hhecke_sq(q_val)
        err_form_b_ppb = (alpha_inv_form_b - alpha_inv_c22) / alpha_inv_c22 * mpf("1e9")

        improvement_vs_witten = abs(err_witten_ppb) / abs(err_seifert_ppb)
        ratio_vs_form_b = abs(err_seifert_ppb) / abs(err_form_b_ppb)

        wb.add_assertion(
            name=f"kappa_det_equals_closed_form_{pin_name}",
            computed=fmt80(kappa_from_det),
            expected=fmt80(kappa_from_alex),
            tolerance="1e-70",
            source=f"80-dps matrix det ratio vs q^8/(Delta_T29*Delta_T35) at {pin_name} pin",
        )

        if pin_name == "proton":
            wb.add_assertion(
                name="kappa_seifert_proton_inside_100ppb_window",
                computed="1" if inside_100ppb_window else "0",
                expected="1",
                tolerance="0.5",
                source="kappa_Seifert(q_p) in [1.8739, 1.9567] 100-ppb window",
            )

        pin_results[pin_name] = {
            "q0": fmt80(q_val),
            "bare_q_9_10": fmt80(bare_val),
            "delta_CS": fmt80(d_cs),
            "Delta_T29": fmt80(d29_val),
            "Delta_T35": fmt80(d35_val),
            "det_V29_minus_qinv_V29T": fmt80(det_29_qinv),
            "det_V35_minus_qinv_V35T": fmt80(det_35_qinv),
            "kappa_Seifert_from_matrix_det": fmt80(kappa_from_det),
            "kappa_Seifert_closed_form": fmt80(kappa_from_alex),
            "kappa_opposite_orientation_u_eq_q": fmt80(kappa_u_eq_q),
            "kappa_exact_codata2022_closure_diagnostic": fmt80(kappa_needed),
            "kappa_rel_diff_vs_exact_closure_pct": fmt80(kappa_rel_diff_pct),
            "window_100ppb_low": fmt80(kappa_lo_100ppb),
            "window_100ppb_high": fmt80(kappa_hi_100ppb),
            "inside_100ppb_window": inside_100ppb_window,
            "tower_geometric_ratio_delta_CS_mul_kappa_Seifert": fmt80(tower_ratio_seifert),
            "alpha_inv_resummed_Seifert": fmt80(alpha_inv_seifert),
            "residual_Seifert_vs_codata2022_ppb": fmt80(err_seifert_ppb),
            "residual_Seifert_vs_codata2022_sigma": fmt80(err_seifert_sigma),
            "alpha_inv_resummed_Witten_2x2": fmt80(alpha_inv_witten),
            "residual_Witten_2x2_vs_codata2022_ppb": fmt80(err_witten_ppb),
            "alpha_inv_Form_B_Bring_zero_mode_hHecke_sq": fmt80(alpha_inv_form_b),
            "residual_Form_B_vs_codata2022_ppb": fmt80(err_form_b_ppb),
            "abs_residual_improvement_factor_over_Witten_2x2": fmt80(improvement_vs_witten),
            "abs_residual_ratio_over_Form_B": fmt80(ratio_vs_form_b),
            "status_note": (
                "Conditional/unproved: kappa_Seifert(q) is an exact parameter-free homological "
                "Seifert determinant ratio on H_1(Sigma_4; Z) ~= Z^8, but its derivation as the "
                "Chern-Simons J^2 Gram Jacobian remains open."
            ),
        }

        print(f"--- PIN: {pin_name.upper()} (q0 = {mp.nstr(q_val, 26)}) ---")
        print(f"  Delta_{{T(2,9)}}(q0)               = {mp.nstr(d29_val, 30)}")
        print(f"  Delta_{{T(3,5)}}(q0)               = {mp.nstr(d35_val, 30)}")
        print(f"  kappa_Seifert(q0) [8x8 det]      = {mp.nstr(kappa_from_det, 34)}")
        print(f"  kappa_Seifert(q0) [closed form]  = {mp.nstr(kappa_from_alex, 34)}")
        print(
            f"  kappa_needed (CODATA-2022 diag)  = {mp.nstr(kappa_needed, 20)} "
            f"(rel diff {mp.nstr(kappa_rel_diff_pct, 8)}%, 100-ppb window "
            f"[{mp.nstr(kappa_lo_100ppb, 6)}, {mp.nstr(kappa_hi_100ppb, 6)}], inside={inside_100ppb_window})"
        )
        print(
            f"  1/alpha_EM (Seifert resummed)    = {mp.nstr(alpha_inv_seifert, 28)}  "
            f"({mp.nstr(err_seifert_ppb, 10)} ppb, {mp.nstr(err_seifert_sigma, 6)} sigma)"
        )
        print(
            f"  1/alpha_EM (Witten 2x2 resummed) = {mp.nstr(alpha_inv_witten, 20)}  "
            f"({mp.nstr(err_witten_ppb, 10)} ppb -> {mp.nstr(improvement_vs_witten, 6)}x closer)"
        )
        print(
            f"  1/alpha_EM (Form B Bring 0-mode) = {mp.nstr(alpha_inv_form_b, 20)}  "
            f"({mp.nstr(err_form_b_ppb, 10)} ppb -> Seifert is {mp.nstr(ratio_vs_form_b, 6)}x larger)"
        )
        print()

    wb.add_data("pins", pin_results)
    wb.add_data("references", {
        "codata_2022_alpha_inv": alpha_entry.value_str,
        "codata_2022_uncertainty": alpha_entry.uncertainty_str,
        "codata_2022_sigma_ppb": fmt80(alpha_inv_c22_sig_ppb),
        "working_dps": 80,
    })

    out_path = wb.save(
        q0_comparison(
            muon=mp.nstr(q_muon, 50),
            proton=Q_50_DIGIT_STR,
            reason=(
                "evaluates the parameter-free 8x8 homological Seifert determinant ratio "
                "kappa_Seifert(q) = q^8 / (Delta_{T(2,9)}(q) * Delta_{T(3,5)}(q)) and its "
                "resummed Chern-Simons 1/alpha_EM residual at both registered pins "
                "(proton default q_p and muon CAL-2 comparison q_mu)"
            ),
        )
    )
    print(f"Witness written to: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
