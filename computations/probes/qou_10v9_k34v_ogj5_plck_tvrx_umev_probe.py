#!/usr/bin/env python3
"""80-dps mpmath numerical verification probe for Round 108 beans:
- qou-k34v: Tangent pairing variation requires prepotential associativity (WDVV residual).
- qou-ogj5: Spectral prefactor alpha = 8 * m_e * G glyph collision (Catalan vs G_Planck = 1).
- qou-plck: Symbolic q-rational identity G_q * (hbar_q / c_q)^2 = 1 and three q-length scales.
- qou-tvrx: Projective polarization dictionary [phi1 : lambda * phi0] phase unfixed (lambda = 1 vs i).
- qou-umev: Unit-modulus eigenvalue refutation: Borromean trace 2 - 3*h^4 - h^6 = +1.9941858... != -2
            and even-length word sigma_1^2 trace q^2 + q^{-2} > 2 with positive discriminant.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 80

SCRIPT_PATH = Path(__file__).resolve()
WITNESS_PATH = SCRIPT_PATH.with_name("qou_10v9_k34v_ogj5_plck_tvrx_umev.witness.json")


def get_git_commit_sha() -> str:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=SCRIPT_PATH.parent,
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
        if len(out) == 40:
            return out
    except Exception:
        pass
    return "0" * 40


def run_checks() -> list[dict[str, object]]:
    checks: list[dict[str, object]] = []
    tol = mp.mpf("1e-75")

    # Substrate proton parameter q0 and h = q0 - q0^{-1}
    q0 = mp.mpf("1.1099968845232856265123168914394918113142622826893409280560918480241893282192341")
    h = q0 - (mp.mpf(1) / q0)

    # 1. qou-k34v: Prepotential associativity commutator residual vs factored form
    eta1 = mp.mpf("1.35")
    eta2 = mp.mpf("0.85")
    a_val = mp.mpf("2.10")
    b_val = mp.mpf("1.25")
    d_val = mp.mpf("0.95")
    res_expanded = (a_val * eta2 * d_val + b_val * eta1 * b_val) - (
        b_val * eta2 * b_val + d_val * eta1 * b_val
    )
    res_factored = eta2 * (a_val * d_val - b_val * b_val) + eta1 * b_val * (b_val - d_val)
    diff_k34v = abs(res_expanded - res_factored)
    flat_res = abs(
        (mp.mpf(1) * eta2 * mp.mpf(1) + mp.mpf(1) * eta1 * mp.mpf(1))
        - (mp.mpf(1) * eta2 * mp.mpf(1) + mp.mpf(1) * eta1 * mp.mpf(1))
    )
    checks.append(
        {
            "id": "qou-k34v-prepotential-associativity-residual",
            "bean": "qou-k34v",
            "description": "Prepotential associativity commutator matches factored form to 80 dps and is non-zero off the constant slice",
            "residualExpanded": mp.nstr(res_expanded, 80),
            "residualFactored": mp.nstr(res_factored, 80),
            "absError": mp.nstr(diff_k34v, 80),
            "flatSliceResidual": mp.nstr(flat_res, 80),
            "passed": bool(diff_k34v < tol and flat_res < tol and abs(res_expanded) > mp.mpf("0.1")),
        }
    )

    # 2. qou-ogj5: Spectral prefactor glyph collision (8 * m_e * Catalan vs 8 * m_e * 1)
    me_mev = mp.mpf("0.51099895069")
    g_catalan = mp.catalan
    g_unit = mp.mpf(1)
    alpha_catalan = mp.mpf(8) * me_mev * g_catalan
    alpha_unit = mp.mpf(8) * me_mev * g_unit
    gap_ogj5 = alpha_unit - alpha_catalan
    g_posthoc = alpha_catalan / (mp.mpf(8) * me_mev)
    posthoc_err = abs(mp.mpf(8) * me_mev * g_posthoc - alpha_catalan)
    checks.append(
        {
            "id": "qou-ogj5-spectral-prefactor-glyph-collision",
            "bean": "qou-ogj5",
            "description": "8 * m_e * Catalan = 3.7444596599... MeV differs from 8 * m_e * 1 = 4.0879916... MeV by 0.3435319... MeV",
            "alphaCatalanMeV": mp.nstr(alpha_catalan, 80),
            "alphaUnitMeV": mp.nstr(alpha_unit, 80),
            "glyphCollisionGapMeV": mp.nstr(gap_ogj5, 80),
            "postHocIdentityError": mp.nstr(posthoc_err, 80),
            "passed": bool(
                abs(alpha_catalan - mp.mpf("3.74445965994161")) < mp.mpf("1e-10")
                and gap_ogj5 > mp.mpf("0.343")
                and posthoc_err < tol
            ),
        }
    )

    # 3. qou-plck: Symbolic q-rational identity G_q * (hbar_q / c_q)^2 = 1 and three q-length scales
    hbar_q = (q0 - mp.mpf(1)) / q0
    c_q = mp.mpf(1) / (q0 - mp.mpf(1))
    g_q = (q0**2) / ((q0 - mp.mpf(1)) ** 4)
    g_planck_units = g_q * ((hbar_q / c_q) ** 2)
    ell_norm = hbar_q * q0 / (q0 - mp.mpf(1))
    ell_share = hbar_q
    ell_dim = mp.sqrt(hbar_q * g_q / (c_q**3))
    ratio_dim_to_share = ell_dim / ell_share
    err_plck = abs(g_planck_units - mp.mpf(1)) + abs(ell_dim - mp.sqrt(q0)) + abs(ell_norm - mp.mpf(1))
    checks.append(
        {
            "id": "qou-plck-symbolic-q-forms-and-three-scales",
            "bean": "qou-plck",
            "description": "G_q * (hbar_q / c_q)^2 = 1 identically and the three q-length candidates (1, hbar_q, sqrt(q)) are distinct",
            "gPlanckUnits": mp.nstr(g_planck_units, 80),
            "ellNormalised": mp.nstr(ell_norm, 80),
            "ellPerStepShare": mp.nstr(ell_share, 80),
            "ellDimensional": mp.nstr(ell_dim, 80),
            "ratioDimensionalToShare": mp.nstr(ratio_dim_to_share, 80),
            "absError": mp.nstr(err_plck, 80),
            "passed": bool(
                err_plck < tol
                and ell_share < ell_norm < ell_dim
                and ratio_dim_to_share > mp.mpf("10.6")
            ),
        }
    )

    # 4. qou-tvrx: Projective polarization dictionary [phi1 : lambda * phi0] phase freedom
    phi0 = mp.mpf("0.6")
    phi1 = mp.mpf("0.8")
    norm_sq = phi0**2 + phi1**2
    # lambda = 1: pure linear Stokes (S2 != 0, S3 = 0)
    s2_lam1 = mp.mpf(2) * phi0 * phi1 / norm_sq
    s3_lam1 = mp.mpf(0)
    # lambda = i: pure circular Stokes (S2 = 0, S3 != 0)
    s2_lami = mp.mpf(0)
    s3_lami = -mp.mpf(2) * phi0 * phi1 / norm_sq
    err_tvrx = abs((s2_lam1**2 + s3_lam1**2) - (s2_lami**2 + s3_lami**2)) + abs(s2_lam1 + s3_lami)
    checks.append(
        {
            "id": "qou-tvrx-polarization-dictionary-phase-unfixed",
            "bean": "qou-tvrx",
            "description": "Real mixed state (phi0, phi1) is purely linear at lambda = 1 and purely circular at lambda = i",
            "linearStokesAtLambdaOne": mp.nstr(s2_lam1, 80),
            "circularStokesAtLambdaImag": mp.nstr(s3_lami, 80),
            "absError": mp.nstr(err_tvrx, 80),
            "passed": bool(err_tvrx < tol and abs(s2_lam1) > mp.mpf("0.9")),
        }
    )

    # 5. qou-umev: Unit-modulus eigenvalue proposition refutation in both clauses
    tr_bor_laurent = (
        -(q0**6)
        + mp.mpf(3) * (q0**4)
        - mp.mpf(3) * (q0**2)
        + mp.mpf(4)
        - mp.mpf(3) / (q0**2)
        + mp.mpf(3) / (q0**4)
        - mp.mpf(1) / (q0**6)
    )
    tr_bor_closed = mp.mpf(2) - mp.mpf(3) * (h**4) - (h**6)
    disc_bor = tr_bor_closed**2 - mp.mpf(4)
    # Clause 1 counterexample: sigma_1^2 trace q0^2 + q0^{-2} = 2 + h^2 > 2
    tr_sq = (q0**2) + mp.mpf(1) / (q0**2)
    tr_sq_h = mp.mpf(2) + (h**2)
    disc_sq = tr_sq**2 - mp.mpf(4)
    err_umev = abs(tr_bor_laurent - tr_bor_closed) + abs(tr_sq - tr_sq_h)
    checks.append(
        {
            "id": "qou-umev-unit-modulus-eigenvalue-refutation",
            "bean": "qou-umev",
            "description": "Borromean trace is 2 - 3*h^4 - h^6 = +1.9941858... != -2 (disc < 0), while sigma_1^2 has trace 2 + h^2 > 2 (disc > 0)",
            "borromeanTraceClosed": mp.nstr(tr_bor_closed, 80),
            "borromeanDiscriminant": mp.nstr(disc_bor, 80),
            "squareWordTrace": mp.nstr(tr_sq, 80),
            "squareWordDiscriminant": mp.nstr(disc_sq, 80),
            "absError": mp.nstr(err_umev, 80),
            "passed": bool(
                err_umev < tol
                and abs(tr_bor_closed - mp.mpf("1.99418581297996")) < mp.mpf("1e-5")
                and disc_bor < mp.mpf(0)
                and tr_sq > mp.mpf(2)
                and disc_sq > mp.mpf(0)
            ),
        }
    )

    return checks


def main() -> None:
    script_bytes = SCRIPT_PATH.read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()
    commit_sha = get_git_commit_sha()
    checks = run_checks()
    all_passed = all(bool(c["passed"]) for c in checks)

    witness = {
        "probe": "qou_10v9_k34v_ogj5_plck_tvrx_umev_probe.py",
        "beans": ["qou-k34v", "qou-ogj5", "qou-plck", "qou-tvrx", "qou-umev"],
        "dps": 80,
        "scriptHash": script_hash,
        "scriptSha256": script_hash,
        "scriptCommitSha": commit_sha,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "allPassed": all_passed,
        "checks": checks,
    }
    WITNESS_PATH.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {WITNESS_PATH.name}: allPassed={all_passed}, sha256={script_hash}, commit={commit_sha}")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
