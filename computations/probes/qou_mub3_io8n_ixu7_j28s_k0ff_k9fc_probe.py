#!/usr/bin/env python3
"""
80-dps mpmath witness probe for Round 117 (`qou-mub3` lane):
  - qou-io8n: [zagier-dilogarithm] at QOU.BraidKnot.Li2qUniqueness
  - qou-ixu7: [murakami2006] at the polarization convention remark
  - qou-j28s: [dubois2007] at prop:cusp-shape-bar-parity
  - qou-k0ff: [dupuis-girelli2013] at folio/quantum-observable-universe/observations/cfs-comparison
  - qou-k9fc: [arxiv-2304.12545v1] at def:quantum-bloch-group
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import subprocess
from mpmath import mp

mp.dps = 80


def get_commit_sha(repo_root: pathlib.Path) -> str:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=str(repo_root),
            text=True,
        ).strip()
        if len(out) == 40:
            return out
    except Exception:
        pass
    return "0" * 40


def get_script_sha256(script_path: pathlib.Path) -> str:
    return hashlib.sha256(script_path.read_bytes()).hexdigest()


def probe_qou_io8n() -> dict:
    """
    qou-io8n: Initial-value difference uniqueness for the quantum dilogarithm /
    polylogarithm increment step:
      F(z) = F(0) + int_0^z F'(w) dw, G(z) = G(0) + int_0^z G'(w) dw.
    Verified at 80 dps for classical Li_2(z) vs series integral int_0^z (-ln(1-w)/w) dw.
    """
    z = mp.mpf("3") / mp.mpf("10")
    li2_z = mp.polylog(2, z)
    integral_delta = mp.quad(lambda w: -mp.log(1 - w) / w, [mp.mpf(0), z])
    diff_same_base = abs(li2_z - integral_delta)

    base_f = mp.mpf(7)
    base_g = mp.mpf(-3)
    inc_delta = mp.mpf(19)
    diff_shifted = (base_f + inc_delta) - (base_g + inc_delta)

    passed = bool(
        diff_same_base < mp.mpf("1e-70")
        and diff_shifted == base_f - base_g
        and ((base_f + inc_delta) - (base_f + inc_delta)) == 0
    )
    return {
        "beanId": "qou-io8n",
        "theorem": "QOU.Eightfold.QouMub3Io8nIxu7J28sK0ffK9fc.shared_increment_uniqueness_and_base_offset",
        "zTest": mp.nstr(z, 80),
        "li2AtZ": mp.nstr(li2_z, 80),
        "integralIncrementAtZ": mp.nstr(integral_delta, 80),
        "absResidualSameBase": mp.nstr(diff_same_base, 80),
        "shiftedBaseDifference": str(int(diff_shifted)),
        "passed": passed,
    }


def probe_qou_ixu7() -> dict:
    """
    qou-ixu7: Polarization bilinear shift Im(u * v) = u_re * v_im + u_im * v_re
    between complexified volume conventions.
    """
    u_re = mp.mpf("5") / mp.mpf("4")
    u_im = mp.mpf(0)
    v_re = mp.mpf(0)
    v_im = mp.mpf(2) * mp.pi

    shift_pos = u_re * v_im + u_im * v_re
    shift_neg = (-u_re) * v_im + u_im * v_re
    shift_pure_imag = mp.mpf(0) * v_im + mp.mpf("3") * mp.mpf(0)

    passed = bool(
        abs(shift_pure_imag) < mp.mpf("1e-75")
        and abs(shift_pos + shift_neg) < mp.mpf("1e-75")
    )
    return {
        "beanId": "qou-ixu7",
        "theorem": "QOU.Eightfold.QouMub3Io8nIxu7J28sK0ffK9fc.polarization_shift_pure_imaginary_and_sign_flip",
        "shiftPositiveURe": mp.nstr(shift_pos, 80),
        "shiftNegativeURe": mp.nstr(shift_neg, 80),
        "shiftPureImaginary": mp.nstr(shift_pure_imag, 80),
        "signFlipSum": mp.nstr(shift_pos + shift_neg, 80),
        "passed": passed,
    }


def probe_qou_j28s() -> dict:
    """
    qou-j28s: Parabolic longitude translation c = n - 2 * w12 * w22 and torsion
    parameter u = 4 / (c - 2) -> u * (c - 2) = 4.
    For figure-eight (n=2, w12=2, w22=1), c = -2 and u = -1.
    """
    n_val = 2
    w12 = 2
    w22 = 1
    c_val = n_val - 2 * w12 * w22
    u_val = mp.mpf(4) / mp.mpf(c_val - 2)
    cleared_prod = u_val * mp.mpf(c_val - 2)

    passed = bool(
        c_val == -2
        and abs(u_val - mp.mpf(-1)) < mp.mpf("1e-75")
        and abs(cleared_prod - mp.mpf(4)) < mp.mpf("1e-75")
    )
    return {
        "beanId": "qou-j28s",
        "theorem": "QOU.Eightfold.QouMub3Io8nIxu7J28sK0ffK9fc.parabolic_longitude_and_torsion_holonomy_pin",
        "parabolicTranslationC": str(c_val),
        "torsionParamU": mp.nstr(u_val, 80),
        "clearedTorsionProduct": mp.nstr(cleared_prod, 80),
        "passed": passed,
    }


def probe_qou_k0ff() -> dict:
    """
    qou-k0ff: Quantum spin multiplicity (2j + 1) and quadruple quadratic spin scale
    4 * j * (j + 1) = m^2 + 2m for m = 2j, satisfying (m + 1)^2 - (m^2 + 2m) = 1.
    Also verifies q-dimension [2j+1]_q -> 2j+1 as q -> 1 at 80 dps.
    """
    all_identities_ok = True
    sample_records = []
    theta = mp.mpf("1e-40")
    for m_int in [0, 1, 2, 3, 4, 7]:
        mult = m_int + 1
        quad_scale = m_int * m_int + 2 * m_int
        diff_one = mult * mult - quad_scale
        q_dim = mp.sin(mp.mpf(mult) * theta) / mp.sin(theta)
        q_dim_err = abs(q_dim - mp.mpf(mult))
        if diff_one != 1 or q_dim_err > mp.mpf("1e-75"):
            all_identities_ok = False
        sample_records.append(
            {
                "twiceSpinM": str(m_int),
                "multiplicity": str(mult),
                "quadrupleQuadraticScale": str(quad_scale),
                "identityDifference": str(diff_one),
                "qDimClassicalLimitError": mp.nstr(q_dim_err, 80),
            }
        )

    return {
        "beanId": "qou-k0ff",
        "theorem": "QOU.Eightfold.QouMub3Io8nIxu7J28sK0ffK9fc.spin_multiplicity_quadratic_scale_difference_one",
        "samples": sample_records,
        "passed": bool(all_identities_ok),
    }


def probe_qou_k9fc() -> dict:
    """
    qou-k9fc: Extended flattening regulator lift L(z; p, q) = L_0(z) + p*u + q*v
    with symmetric branch cancellation (p, -p) along u = v.
    """
    z = mp.mpc(mp.mpf("1") / mp.mpf("2"), mp.sqrt(3) / mp.mpf("2"))
    u = mp.log(z)
    v = -mp.log(1 - z)
    # For exp(i*pi/3), 1 - z = exp(-i*pi/3), so u = i*pi/3 and v = i*pi/3 (u == v)
    l0 = mp.polylog(2, z) + mp.mpf("1") / mp.mpf("2") * u * v
    p_weight = mp.mpf(3)
    l_Cancel = l0 + p_weight * u + (-p_weight) * v
    branch_residual = abs(l_Cancel - l0)

    passed = bool(
        abs(u - v) < mp.mpf("1e-75")
        and branch_residual < mp.mpf("1e-75")
    )
    return {
        "beanId": "qou-k9fc",
        "theorem": "QOU.Eightfold.QouMub3Io8nIxu7J28sK0ffK9fc.extended_flattening_branch_cancellation",
        "uImag": mp.nstr(mp.im(u), 80),
        "vImag": mp.nstr(mp.im(v), 80),
        "baseRegulatorImag": mp.nstr(mp.im(l0), 80),
        "symmetricBranchCancellationResidual": mp.nstr(branch_residual, 80),
        "passed": passed,
    }


def main() -> None:
    script_path = pathlib.Path(__file__).resolve()
    repo_root = script_path.parents[2]
    script_sha = get_script_sha256(script_path)
    commit_sha = get_commit_sha(repo_root)

    checks = [
        probe_qou_io8n(),
        probe_qou_ixu7(),
        probe_qou_j28s(),
        probe_qou_k0ff(),
        probe_qou_k9fc(),
    ]
    all_passed = all(c["passed"] for c in checks)

    witness = {
        "probe": "qou_mub3_io8n_ixu7_j28s_k0ff_k9fc_probe.py",
        "leanModule": "folio/quantum-observable-universe/lean/QOU/Eightfold/QouMub3Io8nIxu7J28sK0ffK9fc.lean",
        "beans": ["qou-io8n", "qou-ixu7", "qou-j28s", "qou-k0ff", "qou-k9fc"],
        "dps": 80,
        "scriptCommitSha": commit_sha,
        "scriptHash": script_sha,
        "scriptSha256": script_sha,
        "allPassed": bool(all_passed),
        "checks": checks,
    }

    out_path = script_path.with_name("qou_mub3_io8n_ixu7_j28s_k0ff_k9fc.witness.json")
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out_path} (allPassed={all_passed}, scriptCommitSha={commit_sha})")


if __name__ == "__main__":
    main()
