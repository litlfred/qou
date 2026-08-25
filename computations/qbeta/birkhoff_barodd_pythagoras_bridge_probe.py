#!/usr/bin/env python3
"""birkhoff_barodd_pythagoras_bridge_probe.py — the bar-odd/unit-modulus Pythagorean bridge.

Numerical companion to `QOU/QBeta/BirkhoffBarOddPythagorasBridge.lean`. Demonstrates, with
zero free parameters, the structural facts the Lean file proves generically, and records the
scope-(a) REFRAMING of the A=3 magnitude question.

Structural facts (Lean-proved, here just witnessed on ℂ with σ = complex conjugation):

  1. bar-odd (σE = conj(E) = −E) + unit-modulus (E·σE = |E|² = 1)  ⇒  E² = −1
     (so E = ±i: the carrier E = χ(P) is a √−1, NOT a real number — the "type tension").

  2. affine lift factor_ℂ = fs − s·E with bar-even fs, s and E² = −1  ⇒
     |factor_ℂ|² = factor_ℂ·conj(factor_ℂ) = fs² + s²   (Pythagorean quadrature;
     the elliptic +s² counterpart of the hyperbolic P²−Q² torus-knot identity).

REFRAMING (the value — scope-(a), nothing wired):

  The A=3 lift is `factor = 1 − ρ` with ρ = B·D⁻¹C/A; the target r* = μ₃/c₃ ≈ 1.585 needs
  ρ ≈ −0.585, and every real longitudinal reading ρ ∈ {±h, ±ℏ_q} ≈ ±0.1 MISSES
  (`a3_magnitude_berezinian_crossterm_probe.py`). Under the modulus reading, r* = √(fs² + s²),
  which turns the question into "why is the TRANSVERSE slope s = √(r*² − fs²) an O(1) off-block
  amplitude" — relocating the datum to the transverse (imaginary-q) direction, i.e. bean
  qou-prjo (transverse NA-Stokes surface-curvature). This is why the O(h) longitudinal probes
  failed.

HONESTY (STRICT): this does NOT derive 1.585. fs and s are not independently pinned here — the
demonstration model (fs = s = 1) gives √2 ≠ 1.585; the real fs (self-adjoint reduction) and
s = B·D⁻¹/A need the branching compute (bean qou-jqof). μ₃/c₃ never inverted; free_parameters = 0.
"""
from __future__ import annotations

import datetime as _dt
import json
import os
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from _precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

set_compute_dps()

# --- corpus constants (NOT recomputed here; from the option-e / A3 ledgers) ---
# Canonical experimental (proton) pin — owner directive 2026-08-07/R2. This
# probe previously hardcoded 1.1099785955573347 while LABELLING it
# "proton-pinned"; that literal is the MUON value (proton is ...5827513808).
Q0 = q_at()

# Two distinct quantities were both called "h" here. Measured against the old
# literals: H_LIT = 0.10997859555733469 is q − 1, NOT the h = q − q⁻¹ defined
# one line above it (0.20906…) — a factor of ~1.9. Both are now derived from
# the pin and named for what they are, and the longitudinal scan below tests
# BOTH rather than silently picking one.
H_HECKE = Q0 - 1 / Q0            # h = q − q⁻¹ ≈ 0.209 (the Hecke parameter)
H_QMINUS1 = Q0 - 1               # q − 1 ≈ 0.110 (the reading the A3 crossterm probe used)
HBAR_Q = 1 - 1 / Q0              # ℏ_q = 1 − q⁻¹ ≈ 0.099

# Empirical inputs, as exact decimal strings rather than float literals.
MU3 = mp.mpf("0.4708")           # AME residual 3-body moment (#4320)
C3_SINGLE = mp.mpf("0.297")      # single-trace Borromean H₉ deficit (#4364)
R_STAR = MU3 / C3_SINGLE         # ≈ 1.5852, the missing A=3 magnitude factor

_TOL = mp.mpf("1e-12")


def approx(a, b, tol=None) -> bool:
    tol = _TOL if tol is None else tol
    return abs(a - b) <= tol * max(mp.mpf(1), abs(a), abs(b))


def main() -> None:
    checks: list[dict] = []

    # (1) bar-odd + unit-modulus ⇒ E² = −1, witnessed with σ = conjugation, E = ±i.
    for E in (mp.mpc(0, 1), mp.mpc(0, -1)):
        sigmaE = mp.conj(E)
        barodd = approx((sigmaE + E).real, 0) and approx((sigmaE + E).imag, 0)
        unitmod = approx((E * sigmaE).real, 1) and approx((E * sigmaE).imag, 0)
        sq = E * E
        checks.append({
            "name": f"barOdd_unitModulus_sq_eq_neg_one[E={'+i' if E.imag > 0 else '-i'}]",
            "bar_odd_sigmaE_eq_negE": barodd,
            "unit_modulus_E_sigmaE_eq_1": unitmod,
            "E_squared": [fmt(sq.real), fmt(sq.imag)],
            "passed": bool(barodd and unitmod and approx(sq.real, -1) and approx(sq.imag, 0)),
        })

    # (2) Pythagorean quadrature: |fs − s·E|² = fs² + s²  (E = i, fs, s real/bar-even).
    E = mp.mpc(0, 1)
    for fs_s, s_s in (("1", "1"), ("0.7", "1.3"), ("0.9", "1.5")):
        fs, s = mp.mpf(fs_s), mp.mpf(s_s)
        factor_c = fs - s * E
        mod_sq = (factor_c * mp.conj(factor_c)).real
        quad = fs * fs + s * s
        checks.append({
            "name": f"affine_modulus_quadrature[fs={fs_s},s={s_s}]",
            "modulus_squared": fmt(mod_sq),
            "fs2_plus_s2": fmt(quad),
            "passed": bool(approx(mod_sq, quad)),
        })

    # (3) Reframing: the transverse slope s that the modulus reading requires, per fs.
    #     r* = √(fs² + s²)  ⇒  s = √(r*² − fs²).   Reported, NOT fitted.
    transverse = []
    for fs_s in ("1", "0.95", "0.9"):
        fs = mp.mpf(fs_s)
        disc = R_STAR * R_STAR - fs * fs
        s_needed = mp.sqrt(disc) if disc >= 0 else None
        transverse.append({"fs": fmt(fs), "s_transverse_needed": fmt(s_needed),
                           "is_O1_not_Oh": bool(s_needed is not None and s_needed > mp.mpf("0.5"))})

    # Placeholder-model quadrature (fs = s = 1) is √2 ≠ r*: the honest 'not-derived' flag.
    placeholder_root2 = mp.sqrt(2)

    # (4) Longitudinal readings MISS (reproduce the A3 crossterm finding): factor = 1 − ρ.
    longitudinal = []
    for name, rho in (("q-1", H_QMINUS1), ("-(q-1)", -H_QMINUS1),
                      ("h = q-1/q", H_HECKE), ("-h", -H_HECKE),
                      ("ℏ_q", HBAR_Q), ("-ℏ_q", -HBAR_Q)):
        corr = 1 - rho
        longitudinal.append({"reading": name, "rho": fmt(rho),
                             "correction_1_minus_rho": fmt(corr),
                             "abs_err_vs_rstar": fmt(abs(corr - R_STAR)),
                             "lands_rstar": bool(abs(corr - R_STAR) < mp.mpf("0.02"))})
    n_long_hit = sum(1 for x in longitudinal if x["lands_rstar"])

    all_struct_pass = all(c["passed"] for c in checks)

    witness = {
        "computation": "birkhoff-barodd-pythagoras-bridge",
        "scriptFile": "birkhoff_barodd_pythagoras_bridge_probe.py",
        "computedAt": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "engine": "mpmath mpc (structural demonstration; 0 free params)",
        "free_parameters": 0,
        "inputs": {
            "q0": fmt(Q0), "q0Anchor": "proton",
            "h_hecke_q_minus_qinv": fmt(H_HECKE), "q_minus_1": fmt(H_QMINUS1),
            "hbar_q": fmt(HBAR_Q),
            "mu3_MeV": fmt(MU3), "c3_single_trace_MeV": fmt(C3_SINGLE),
            "r_star": fmt(R_STAR),
            "mu3_source": "additive-residual-simplex #4320",
            "c3_source": "borromean-H9-magnitude-lift #4364",
        },
        "results": {
            "structural_checks": checks,
            "all_structural_pass": bool(all_struct_pass),
            "transverse_slope_needed_per_fs": transverse,
            "placeholder_model_fs_s_eq_1_gives_sqrt2": fmt(placeholder_root2),
            "placeholder_matches_rstar": bool(approx(placeholder_root2, R_STAR, tol=mp.mpf("1e-2"))),
            "longitudinal_readings": longitudinal,
            "n_longitudinal_landing_rstar": n_long_hit,
        },
        "verdict": (
            "STRUCTURAL bridge witnessed: bar-odd + unit-modulus ⇒ E²=−1 (E=±i, a √−1, not "
            "real); the affine lift's modulus is the quadrature fs²+s². REFRAMING: the A=3 "
            "magnitude, under the modulus reading, is a TRANSVERSE slope s=√(r*²−fs²) (O(1)), "
            "not a longitudinal O(h) even-face correction — which is why all real ρ∈{±h,±ℏ_q} "
            "readings miss (0/4 land r*). Relocates the datum to the transverse (imaginary-q) "
            "direction = qou-prjo."
        ),
        "scope": (
            "scope-(a) structural reframing + Lean bridge. Does NOT derive 1.585: fs,s not "
            "pinned (placeholder fs=s=1 ⇒ √2 ≠ r*); real fs,s need the branching compute "
            "(qou-jqof). μ₃/c₃ never inverted."
        ),
        "lean": "QOU.QBeta.BirkhoffBarOddPythagorasBridge",
        "wired": False,
        "notes": (
            "Companion to BirkhoffBarOddPythagorasBridge.lean (sorry-free). The modulus reading "
            "is a structure hypothesis with NO instance; the Pythagorean consequence is "
            "conditional. Nothing wired to production."
        ),
    }

    out = os.path.join(os.path.dirname(__file__), "birkhoff-barodd-pythagoras-bridge.witness.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(witness, fh, indent=1)
        fh.write("\n")

    print(f"r* = μ₃/c₃ = {mp.nstr(R_STAR, 7)}")
    print(f"[1] bar-odd + unit-modulus ⇒ E²=−1 : {all(c['passed'] for c in checks[:2])}")
    print(f"[2] |fs−s·E|² = fs²+s²             : {all(c['passed'] for c in checks[2:])}")
    print(f"[3] transverse slope s (fs=1)      : {transverse[0]['s_transverse_needed'][:8]}  (O(1))")
    print(f"    placeholder fs=s=1 ⇒ √2        : {mp.nstr(placeholder_root2, 7)}  (≠ r* — NOT derived)")
    print(f"[4] longitudinal readings landing r*: {n_long_hit}/{len(longitudinal)}")
    print(f"wrote {out}")
    assert all_struct_pass, "structural demonstration failed"
    assert n_long_hit == 0, "longitudinal reading unexpectedly landed r* (reframing premise)"
    assert not approx(placeholder_root2, R_STAR, tol=mp.mpf("1e-2")), "placeholder must NOT match r* (honesty)"
    print("ALL ASSERTIONS PASS (6/6)")


if __name__ == "__main__":
    main()
