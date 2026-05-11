#!/usr/bin/env python3
# polynomial_q_not_applicable: probe — δQ_β via per-nucleon residue diff.
"""Q_β residue closure via per-nucleon δm_n - δm_p (canonical β_p, β_n at H_3).

Per the previous probe finding (commit 07636229): applying the
residue sum directly to Δ_NF gives +17.5 keV (wrong). The correct
chain is

    δQ_β = δm_n - δm_p - 0 (free electron, no H_3 braid)

where each δm_K = Σ_{λ, ζ} Res[w_λ(q) χ_λ(β_K)] / (q_0 - ζ_ℓ),
computed on the CANONICAL nucleon braids β_p, β_n. Characters
loaded symbolically from chi-{proton,neutron}-h3.witness.json.

NO FITTING. All inputs substrate-derived:
  * χ_λ(β_K) from H_3 Hoefsmit canonical computations (witnesses)
  * w_λ from prop:schur-weyl-mass-decomposition
  * Poles from [n]_q = 0 algebraic factoring
  * Residues by num/den' formula
  * q_0, m_e from CAL-1, CAL-2
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 50

OUT = HERE / "q-beta-residue-per-nucleon-probe.witness.json"


def load_chi_symbolic(witness_path: Path) -> dict:
    """Load symbolic χ_λ for each H_3 partition from a chi-{atom}-h3 witness."""
    with witness_path.open() as fh:
        d = json.load(fh)
    chi_list = d.get("chi_lambda_symbolic", d.get("data", {}).get("chi_lambda_symbolic"))
    return {tuple(entry["partition"]): entry["chi_q_symbolic"] for entry in chi_list}


def residue_sum_for_irrep(weight_sym, chi_sym, q_sym, q_0):
    """Compute Σ_ζ Res_{q=ζ}[w(q) χ(q)] / (q_0 - ζ) for the simple poles
    of w(q) (poles of the integrand)."""
    chi_parsed = sp.sympify(chi_sym, locals={"q": q_sym}) if isinstance(chi_sym, str) else chi_sym
    integrand = sp.cancel(sp.together(weight_sym * chi_parsed))
    num, den = sp.fraction(integrand)
    num_poly = sp.Poly(num, q_sym)
    den_poly = sp.Poly(den, q_sym)
    if den_poly.degree() == 0:
        return mp.mpf(0), []
    roots = sp.roots(den_poly, q_sym)
    if not roots:
        roots = {r: 1 for r in den_poly.nroots(n=50)}
    total = mp.mpf(0)
    records = []
    for zeta, mult in roots.items():
        if mult != 1:
            continue
        num_v = num_poly.eval(zeta)
        den_d_v = den_poly.diff().eval(zeta)
        if den_d_v == 0:
            continue
        res_sym = sp.simplify(num_v / den_d_v)
        # Preserve precision via component-wise sp.re/sp.im → str → mp.mpf,
        # avoiding the truncating round-trip through Python `complex`.
        res_eval = res_sym.evalf(mp.dps)
        res_mp = mp.mpc(mp.mpf(str(sp.re(res_eval))), mp.mpf(str(sp.im(res_eval))))
        # Tolerance tied to current dps.
        if abs(res_mp) < mp.mpf(10) ** (-mp.dps + 10):
            continue
        zeta_eval = zeta.evalf(mp.dps)
        zeta_mp = mp.mpc(mp.mpf(str(sp.re(zeta_eval))), mp.mpf(str(sp.im(zeta_eval))))
        weight = 1 / (mp.mpf(q_0) - zeta_mp)
        contribution = res_mp * weight
        total += contribution.real
        records.append({
            "pole_symb": str(zeta),
            "pole_num": [float(zeta_mp.real), float(zeta_mp.imag)],
            "residue_symb": str(res_sym),
            "contribution_real": float(contribution.real),
        })
    return total, records


def evaluate_at_q0(expr_sym, q_sym, q_0):
    """Numerical evaluation of a sympy expression at q = q_0."""
    # Substitute q with a high-precision rational approximation of q_0
    q_rat = sp.Rational(str(q_0))
    val = sp.N(expr_sym.subs(q_sym, q_rat), 50)
    return mp.mpf(str(val))


def main() -> int:
    q = sp.Symbol("q", positive=True)
    # Load CAL-2 q_0 from the canonical pinning witness so this probe
    # stays aligned with the single source of truth (per Copilot review).
    q_pinning = HERE / "q-pinning-50-digit.witness.json"
    with q_pinning.open() as fh:
        q_0 = mp.mpf(json.load(fh)["derived_50_digit"]["q"])
    q_0_str = str(q_0)
    m_e_f = M_E_MEV
    q_codata = mp.mpf(str(Q_BETA_MEV))

    # Schur-Weyl weights at H_3
    bracket_n = lambda n: sp.simplify((q ** n - q ** (-n)) / (q - q ** (-1)))
    w = {
        (3,):       sp.Integer(1),
        (2, 1):     bracket_n(2) / bracket_n(3),
        (1, 1, 1):  1 / (bracket_n(3) * bracket_n(2)),
    }

    # Characters from canonical witnesses
    chi_p = load_chi_symbolic(HERE / "chi-proton-h3.witness.json")
    chi_n = load_chi_symbolic(HERE / "chi-neutron-h3.witness.json")
    # Normalize keys (lists from JSON, want tuples)
    chi_p = {tuple(k): v for k, v in chi_p.items()}
    chi_n = {tuple(k): v for k, v in chi_n.items()}

    print("=" * 80)
    print(" Q_β residue closure via per-nucleon δm_n - δm_p (canonical β_p, β_n at H_3)")
    print("=" * 80)
    print()
    print(f"  q_0 = {q_0_str[:14]}")
    print(f"  m_e = {float(m_e_f):.6f} MeV   (CAL-1)")
    print(f"  CODATA Q_β = {float(q_codata):.6f} MeV   (CAL-3 cross-check)")
    print()
    print(f"  Leading-order Schur-Weyl sum Σ_λ w_λ χ_λ(β_K) at q_0:")
    print(f"  {'λ':<10} {'w_λ':>14} {'χ_p(β_p)':>16} {'χ_p(β_n)':>16} {'Δχ_λ':>16}")

    lo_p = mp.mpf(0)
    lo_n = mp.mpf(0)
    delta_chi_at_q0 = {}
    for lam in [(3,), (2, 1), (1, 1, 1)]:
        w_lam_q0 = evaluate_at_q0(sp.simplify(w[lam]), q, q_0)
        chi_p_q0 = evaluate_at_q0(sp.sympify(chi_p[lam], locals={"q": q}), q, q_0)
        chi_n_q0 = evaluate_at_q0(sp.sympify(chi_n[lam], locals={"q": q}), q, q_0)
        delta = chi_n_q0 - chi_p_q0
        delta_chi_at_q0[lam] = delta
        lo_p += w_lam_q0 * chi_p_q0
        lo_n += w_lam_q0 * chi_n_q0
        print(f"  {str(lam):<10} {float(w_lam_q0):>+14.8f} {float(chi_p_q0):>+16.8f} {float(chi_n_q0):>+16.8f} {float(delta):>+16.8f}")
    print()
    print(f"  Σ_λ w_λ χ_λ(β_p) = {float(lo_p):+.6f}")
    print(f"  Σ_λ w_λ χ_λ(β_n) = {float(lo_n):+.6f}")
    print(f"  Difference        = {float(lo_n - lo_p):+.6f}")
    print(f"  × m_e (MeV)       = {float((lo_n - lo_p) * m_e_f):+.6f} MeV")
    print(f"  (Reference Q_β + m_e from CODATA = {float(q_codata + m_e_f):.4f} MeV)")
    print()
    print(f"  Residue sums at roots of unity (per λ, per atom):")

    residue_p_total = mp.mpf(0)
    residue_n_total = mp.mpf(0)
    per_lambda_records = {}
    for lam in [(3,), (2, 1), (1, 1, 1)]:
        rec_p_total, rec_p_list = residue_sum_for_irrep(w[lam], chi_p[lam], q, q_0)
        rec_n_total, rec_n_list = residue_sum_for_irrep(w[lam], chi_n[lam], q, q_0)
        residue_p_total += rec_p_total
        residue_n_total += rec_n_total
        per_lambda_records[str(lam)] = {
            "proton_residue_contribution": float(rec_p_total),
            "neutron_residue_contribution": float(rec_n_total),
            "difference_n_minus_p": float(rec_n_total - rec_p_total),
            "poles_per_atom_proton": rec_p_list,
            "poles_per_atom_neutron": rec_n_list,
        }
        print(f"    λ={lam}: δm_p contrib = {float(rec_p_total):+.6e}, δm_n contrib = {float(rec_n_total):+.6e}, diff = {float(rec_n_total - rec_p_total):+.6e}")

    print()
    delta_residue = residue_n_total - residue_p_total
    delta_residue_MeV = delta_residue * m_e_f
    print(f"  δm_p (residue total) = {float(residue_p_total):+.8f}  (cat-units of m_e)")
    print(f"  δm_n (residue total) = {float(residue_n_total):+.8f}")
    print(f"  δQ_β = δm_n - δm_p   = {float(delta_residue):+.8f}")
    print(f"                       × m_e = {float(delta_residue_MeV):+.8f} MeV = {float(delta_residue_MeV * 1000):+.4f} keV")
    print()
    baseline_resid_kev = 1.31
    correction_kev = float(delta_residue_MeV * 1000)
    print(f"  Q_β baseline residual (N=0, single-wrap) = {baseline_resid_kev:+.2f} keV")
    print(f"  Q_β residue correction (per-nucleon diff) = {correction_kev:+.2f} keV")
    print(f"  After correction:                        = {baseline_resid_kev + correction_kev:+.2f} keV")

    new_resid_abs = abs(baseline_resid_kev + correction_kev)
    if new_resid_abs < abs(baseline_resid_kev):
        print(f"  ✓ TIGHTENS by {abs(baseline_resid_kev)/new_resid_abs:.2f}×")
    else:
        ratio = new_resid_abs / abs(baseline_resid_kev)
        if abs(correction_kev) > 10:
            print(f"  ✗ Correction too large ({abs(correction_kev):.1f} keV)  → wrong decomposition")
        else:
            print(f"  ? Correction {correction_kev:+.2f} keV, post-residual {new_resid_abs:.2f} keV ({ratio:.2f}× baseline)")

    out = {
        "computation": "q-beta-residue-per-nucleon-probe",
        "scriptFile": "probe_q_beta_residue_per_nucleon.py",
        "description": (
            "Q_β residue closure via per-nucleon residue diff. "
            "Computes δm_K = Σ_λ residue-sum[w_λ(q) χ_λ(β_K)] at "
            "roots of unity for each canonical nucleon braid, then "
            "takes δQ_β = δm_n - δm_p. Characters loaded from "
            "chi-{proton,neutron}-h3.witness.json (substrate-"
            "derived). NO FITTING."
        ),
        "auditOnly": (
            "docs/audits/2026-05-10-hbar-q-scaling-audit.md; "
            "schur-weyl-mass-decomposition.md (residue sum formula)"
        ),
        "no_fitting_assertion": (
            "All inputs (χ_λ for canonical β_p β_n, w_λ from prop, "
            "poles from algebraic [n]_q factoring, q_0 from CAL-2, "
            "m_e from CAL-1) are substrate-derived. No parameter "
            "tuning anywhere."
        ),
        "data": {
            "q_0_50dps": q_0_str,
            "m_e_MeV": str(m_e_f),
            "Q_beta_codata_MeV": str(q_codata),
            "leading_order_sum_proton": str(lo_p),
            "leading_order_sum_neutron": str(lo_n),
            "leading_order_diff": str(lo_n - lo_p),
            "leading_order_diff_MeV": str((lo_n - lo_p) * m_e_f),
            "residue_total_proton": str(residue_p_total),
            "residue_total_neutron": str(residue_n_total),
            "residue_diff_n_minus_p": str(delta_residue),
            "residue_diff_MeV": str(delta_residue_MeV),
            "residue_diff_keV": float(delta_residue_MeV * 1000),
            "baseline_Q_beta_residual_keV": baseline_resid_kev,
            "post_correction_residual_keV": baseline_resid_kev + correction_kev,
            "per_lambda_records": per_lambda_records,
        },
    }
    saved = WitnessBuilder.wrap_legacy(
        "q-beta-residue-per-nucleon-probe", out,
        script_path=__file__, engine="mpmath",
    ).save()
    print(f"\n  Wrote {saved.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
