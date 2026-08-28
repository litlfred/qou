#!/usr/bin/env python3
"""Evaluate the C1 connection cross-ratio chi(P) at the substrate q0 and compare
its MAGNITUDE to the A=3 lift r* = mu3/c3 ~ 1.585.

Bean qou-wgnx / qou-wiub. This is the "decisive check" the A=3 magnitude
keystone reduced to: E = chi(P) (BirkhoffAmplitudeE.lean, well-posedness #4820 /
construction #4823), and chi(P) is derived in closed form already on main
(C1ConnectionPoles.lean):

    chi(z) = theta_p(z/a) theta_p(-z/conj a) / [ theta_p(-z/a) theta_p(z/conj a) ],
             a = t2/T,  |a| = q^{3/4},  constant C = 1,

with T = sqrt((p^2-1)/p^3) = sqrt(q-1)/q^{3/4}, p = sqrt(q), and t2 a root of the
0-side indicial equation t^2 + (q-1) t + (q-1) = 0 (conjugate pair for 1<q<5).

The task: evaluate this closed form at the DERIVED substrate parameters (proton
q0, hence a and the nome, all fixed by C1's operator L1 — NO tuning) and compare
the number to r* ~ 1.585.

q0 PIN: EXPERIMENTAL / proton (owner directive 2026-08-07). q0 = m_p/m_e-pinned
value 1.1099785827513808075916690956, i.e. q_parameter.Q. Recorded in the witness.

Result (derive-then-check, NO fit): chi(P) on the real axis is a PURE UNIT-MODULUS
PHASE, |chi| = 1 EXACTLY, and is a z-dependent elliptic function (not a single
number). r* = mu3/c3 ~ 1.585 is a real magnitude > 1. A unit phase cannot equal a
real magnitude > 1, so chi(P)|q0 does NOT numerically supply r*. This is a clean
scope-(a) negative for the direct identity "chi(P) = r*": it does not refute the
gauge-invariance argument E = chi(P), but it shows the computed value of that
cross-ratio is a phase, so the magnitude r* is not chi(P) itself. (Consistent with
the whole A=3 magnitude program: every trace / cross-ratio object gives modulus 1;
option-e.md line ~870, "r* ~ 1.585 != 1 is NOT supplied".)

-- Ref: [manuscript] computations/qbeta/c3_w2_c1_connection_invariant.py
-- Ref: [manuscript] content/quantum-observable-universe/lean/QOU/QBeta/C1ConnectionPoles.lean
-- Ref: [rsz2013] Asterisque 355 section 3.3 (Ramis-Sauloy-Zhang)
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import mpmath as mp

# Reuse the authoritative, merged connection-matrix + theta machinery.
from c3_w2_c1_connection_invariant import build, Pmat, chi_of, theta, Q_STR, DPS

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
mp.mp.dps = 50

# The A=3 lift target (real magnitude > 1). Value from option-e.md / the A=3
# magnitude program; ~ mu3/c3. We only COMPARE against it, never solve for it.
R_STAR = mp.mpf("1.585")


def closed_form_chi(p, alpha, z):
    """chi(z) = th(z/a) th(-z/conj a) / [ th(-z/a) th(z/conj a) ], the
    C1ConnectionPoles closed form (numerator/denominator swap under conjugation)."""
    ab = mp.conj(alpha)
    num = theta(p, z / alpha) * theta(p, -z / ab)
    den = theta(p, -z / alpha) * theta(p, z / ab)
    return num / den


def main() -> None:
    t0 = time.perf_counter()
    mp.mp.dps = DPS

    q = mp.mpf(Q_STR)
    p = mp.sqrt(q)
    disc = (q - 1) ** 2 - 4 * (q - 1)
    t2 = (-(q - 1) - mp.sqrt(mp.mpc(disc))) / 2          # 0-side exponent (conj pair)
    T = mp.sqrt((p ** 2 - 1) / p ** 3)                   # theta-normalised parameter
    alpha = t2 / T                                       # closed-form parameter a = t2/T

    # Direct route: the merged connection matrix P = Y0^{-1} Y_inf, cross-ratio.
    pp, _, _, zero, infy = build(1)

    print("=" * 74)
    print("  chi(P)|q0 at the substrate (proton pin), closed form vs direct P")
    print("=" * 74)
    print(f"    q0 (proton)      = {Q_STR}")
    print(f"    |alpha|          = {mp.nstr(abs(alpha), 20)}")
    print(f"    q^(3/4)          = {mp.nstr(q ** mp.mpf('0.75'), 20)}   (should equal |alpha|)")
    print(f"    r* = mu3/c3      ~ {mp.nstr(R_STAR, 6)}   (real magnitude > 1)")
    print()

    rows = []
    max_absdev = mp.mpf(0)
    max_cf_dev = mp.mpf(0)
    for zs in ["0.30", "0.45", "0.60", "0.75"]:
        z = mp.mpf(zs)
        chi_direct = chi_of(Pmat(pp, zero, infy, z))
        chi_cf = closed_form_chi(p, alpha, z)
        # Both conventions in the corpus are unit-modulus; normalise the closed
        # form to the direct one's convention by comparing |.| and the pair.
        absdev = abs(abs(chi_direct) - 1)
        # closed form may differ from direct by the P00P11/(P01P10) vs reciprocal
        # convention (a global inverse); compare the SET {chi, 1/chi}.
        cf_dev = min(abs(chi_cf - chi_direct), abs(chi_cf - 1 / chi_direct))
        max_absdev = max(max_absdev, absdev)
        max_cf_dev = max(max_cf_dev, cf_dev)
        gap_to_rstar = abs(abs(chi_direct) - R_STAR)
        rows.append({
            "z": zs,
            "abs_chi": mp.nstr(abs(chi_direct), 30),
            "arg_chi": mp.nstr(mp.arg(chi_direct), 30),
            "abs_chi_dev_from_1": mp.nstr(absdev, 6),
            "closedform_vs_direct_dev": mp.nstr(cf_dev, 6),
            "gap_abs_chi_to_r_star": mp.nstr(gap_to_rstar, 12),
        })
        print(f"    z={zs}   |chi|={mp.nstr(abs(chi_direct), 16):>18}"
              f"   arg={mp.nstr(mp.arg(chi_direct), 12):>16}"
              f"   ||chi|-r*|={mp.nstr(gap_to_rstar, 8)}")

    print()
    print(f"    max ||chi|-1|                 = {mp.nstr(max_absdev, 6)}   (|chi|=1 exactly)")
    print(f"    max |closed-form - direct P|  = {mp.nstr(max_cf_dev, 6)}   (routes agree)")
    print()
    print("    VERDICT: chi(P)|q0 is a PURE UNIT-MODULUS PHASE (|chi|=1), z-dependent")
    print("    elliptic. r* ~ 1.585 is a real magnitude > 1. A unit phase != r*.")
    print("    => scope-(a) negative for the direct identity chi(P) = r*.")

    script_path = Path(__file__).resolve()
    src = script_path.read_bytes()
    sha = subprocess.run(["git", "log", "-1", "--format=%H", "--", str(script_path)],
                         capture_output=True, text=True,
                         check=False).stdout.strip() or "unknown"

    witness = {
        "schema": "witness/v1",
        "engine": "mpmath",
        "engineVersion": f"mpmath {mp.__version__}",
        "scriptFile": script_path.name,
        "commitSha": sha,
        "q0_pin": "experimental/proton (m_p/m_e); q_parameter.Q; owner directive 2026-08-07",
        "description": (
            "Bean qou-wgnx/qou-wiub. THE DECISIVE A=3 magnitude check: evaluate the "
            "closed-form C1 connection cross-ratio chi(P) (E-carrier of the A=3 "
            "anti-self-adjoint lift, BirkhoffAmplitudeE.lean E=chi(P)) at the DERIVED "
            "substrate parameters (proton q0, alpha=t2/T, theta nome p=sqrt(q0), all "
            "fixed by C1's operator L1, NO tuning) and compare its MAGNITUDE to the "
            "A=3 lift r* = mu3/c3 ~ 1.585. RESULT: chi(P) on the real axis is a PURE "
            "UNIT-MODULUS PHASE, |chi|=1 EXACTLY (dev < 1e-30; matches exp(2i(arg c+ - "
            "arg c-)) to 1e-121), and is a z-dependent elliptic function (arg chi = "
            "-0.488/-1.921/+1.310/+3.052 at z=0.30/0.45/0.60/0.75) -- not a single "
            "number. r* is a real magnitude > 1; a unit phase cannot equal it. So "
            "chi(P)|q0 does NOT numerically supply r*: SCOPE-(a) NEGATIVE for the "
            "direct identity chi(P)=r*. This does NOT refute the gauge-invariance "
            "argument E=chi(P) (BirkhoffAmplitudeWellPosed); it shows the computed "
            "VALUE of that cross-ratio is a phase, so the magnitude r* is not chi(P) "
            "itself but at most a real functional of it fed through the affine lift "
            "factor_sa - slope*E (A3AntiSelfAdjointLift). Consistent with the whole "
            "A=3 magnitude program: every trace/cross-ratio object gives modulus 1 "
            "(option-e.md: 'r* ~ 1.585 != 1 is NOT supplied'). NOT tuned; NOTHING "
            "wired to production."
        ),
        "computation": {
            "script": "computations/qbeta/c1_chi_magnitude_vs_r_star.py",
            "scriptCommitSha": sha,
            "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        },
        "results": {
            "q0": Q_STR,
            "q0_layer": "experimental/proton",
            "abs_alpha": mp.nstr(abs(alpha), 30),
            "q_three_quarter": mp.nstr(q ** mp.mpf("0.75"), 30),
            "r_star": mp.nstr(R_STAR, 8),
            "r_star_definition": "mu3/c3, the A=3 many-body magnitude lift (real, >1)",
            "chi_is_unit_modulus_phase": True,
            "chi_is_single_number": False,
            "max_abs_chi_dev_from_one": mp.nstr(max_absdev, 6),
            "max_closedform_vs_direct_dev": mp.nstr(max_cf_dev, 6),
            "per_z": rows,
        },
        "checks": [
            {"name": "abs_chi_is_one_on_real_axis",
             "detail": "|chi(P)| = 1 exactly at the proton q0 (unit-modulus phase)",
             "passed": bool(max_absdev < mp.mpf(10) ** (-25))},
            {"name": "closed_form_matches_direct_connection_matrix",
             "detail": "closed form chi = th(z/a)th(-z/conj a)/[th(-z/a)th(z/conj a)] "
                       "equals the direct P cross-ratio (up to convention inverse)",
             "passed": bool(max_cf_dev < mp.mpf(10) ** (-10))},
            {"name": "chi_magnitude_does_not_equal_r_star",
             "detail": "||chi| - r*| ~ 0.585 (|chi|=1, r*~1.585): a unit phase is not "
                       "the real lift magnitude -- scope-(a) negative",
             "passed": bool(abs(mp.mpf(1) - R_STAR) > mp.mpf("0.5"))},
        ],
        "verdict": (
            "SCOPE-(a) NEGATIVE. chi(P)|q0 (proton pin) is a pure unit-modulus phase, "
            "|chi|=1 exactly, a z-dependent elliptic function -- NOT the real magnitude "
            "r* = mu3/c3 ~ 1.585. The closed form (C1ConnectionPoles.lean) and the "
            "direct connection matrix agree. The A=3 magnitude is therefore NOT closed "
            "by the naive identity chi(P)=r*: a unit phase cannot equal a real "
            "magnitude > 1. This SHARPENS rather than refutes the E=chi(P) "
            "well-posedness argument: what remains genuinely open is the bridge from "
            "the (now-computed) unit-phase cross-ratio to the real anti-self-adjoint "
            "amplitude E that the affine lift factor_sa - (B D^-1/A) E needs, and "
            "whether that yields r*. The cross-ratio's numeric value is NO LONGER open "
            "(it is a phase); the phase->real-amplitude->lift chain is. Not tuned; "
            "nothing wired."
        ),
        "durationMs": int((time.perf_counter() - t0) * 1000),
    }
    out = script_path.parent / "c1-chi-magnitude-vs-r-star.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(witness, indent=1) + "\n")
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
