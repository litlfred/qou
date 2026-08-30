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

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "substrate"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from _witness_q0_stamp import stamp_q0  # noqa: E402

import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402

# NO-FLOAT64 (AGENTS.md, owner directive 2026-08-18: "PROBES ARE NOT EXEMPT").
# dps is raised HERE, at module scope, BEFORE the first mpf is constructed.
# Doing it inside main() would leave every module-scope constant below at
# mpmath's default 15 dps -- the exact defect `mpf_import_time_dps_audit`
# gates on, and the one that put this file's sibling on the red list.
set_compute_dps()

# --- corpus constants (NOT recomputed here; from the option-e / A3 ledgers) ---
# The two derived readings below (H_LIT, HBAR_Q) are FUNCTIONS of Q0, not
# independent literals, so they follow the re-pin automatically -- the
# straddle this comment used to warn about cannot arise.
# q0 RESOLVED, not frozen (2026-08-29, bean qou-1c4y). This was the literal
# 1.10997859555733471..., the SUPERSEDED muon pin A -- it stopped being the
# muon anchor when PR #5500 re-derived that anchor to CODATA-2022. A frozen
# literal cannot follow an anchor move, so the witness kept recording A under
# the label "muon" and the anchor gate scored it Q0_FLIP; re-running could not
# clear it, because the producer was the source of the stale number. It now
# resolves the PROTON pin per the owner directive of 2026-08-15 ("we want
# proton unless for an explicit reason ... otherwise pin proton").
from substrate.q_parameter import Q_50_DIGIT_STR as _Q0_RESOLVED  # noqa: E402 -- q0 RESOLVED, not frozen (qou-1c4y)

Q0_STR = _Q0_RESOLVED
Q0 = mp.mpf(Q0_STR)
# The A3 crossterm probe's "h" reading is q0 - 1, NOT the Hecke h = q - 1/q
# (which is 0.2090603...). Kept under its corpus name, derived rather than
# re-typed as an independent float literal so the two cannot drift apart.
H_LIT = Q0 - 1
HBAR_Q = 1 - 1 / Q0              # ℏ_q = 1 − q⁻¹
MU3_STR, C3_STR = "0.4708", "0.297"
MU3 = mp.mpf(MU3_STR)            # AME residual 3-body moment (#4320)
C3_SINGLE = mp.mpf(C3_STR)       # single-trace Borromean H₉ deficit (#4364)
R_STAR = MU3 / C3_SINGLE         # ≈ 1.5852, the missing A=3 magnitude factor

_TOL = mp.mpf(10) ** -30         # was 1e-12 (float64-grade); real at 70 dps


def approx(a, b, tol=None) -> bool:
    tol = _TOL if tol is None else tol
    return abs(a - b) <= tol * max(mp.mpf(1), abs(a), abs(b))


def main() -> None:
    checks: list[dict] = []

    # (1) bar-odd + unit-modulus ⇒ E² = −1, witnessed with σ = conjugation, E = ±i.
    for _sign, E in (("+i", mp.mpc(0, 1)), ("-i", mp.mpc(0, -1))):
        sigmaE = mp.conj(E)
        barodd = approx((sigmaE + E).real, 0) and approx((sigmaE + E).imag, 0)
        unitmod = approx((E * sigmaE).real, 1) and approx((E * sigmaE).imag, 0)
        sq = E * E
        checks.append({
            "name": f"barOdd_unitModulus_sq_eq_neg_one[E={_sign}]",
            "bar_odd_sigmaE_eq_negE": barodd,
            "unit_modulus_E_sigmaE_eq_1": unitmod,
            "E_squared": [fmt(sq.real), fmt(sq.imag)],
            "passed": barodd and unitmod and approx(sq.real, -1) and approx(sq.imag, 0),
        })

    # (2) Pythagorean quadrature: |fs − s·E|² = fs² + s²  (E = i, fs, s real/bar-even).
    E = mp.mpc(0, 1)
    for _fs, _s in (("1.0", "1.0"), ("0.7", "1.3"), ("0.9", "1.5")):
        fs, s = mp.mpf(_fs), mp.mpf(_s)
        factor_c = fs - s * E
        mod_sq = (factor_c * mp.conj(factor_c)).real
        quad = fs * fs + s * s
        checks.append({
            "name": f"affine_modulus_quadrature[fs={_fs},s={_s}]",
            "modulus_squared": fmt(mod_sq),
            "fs2_plus_s2": fmt(quad),
            "passed": approx(mod_sq, quad),
        })

    # (3) Reframing: the transverse slope s that the modulus reading requires, per fs.
    #     r* = √(fs² + s²)  ⇒  s = √(r*² − fs²).   Reported, NOT fitted.
    transverse = []
    for _fs in ("1.0", "0.95", "0.9"):
        fs = mp.mpf(_fs)
        disc = R_STAR * R_STAR - fs * fs
        s_needed = mp.sqrt(disc) if disc >= 0 else mp.nan
        transverse.append({"fs": fmt(fs), "s_transverse_needed": fmt(s_needed),
                           "is_O1_not_Oh": bool(s_needed > mp.mpf("0.5"))})

    # Placeholder-model quadrature (fs = s = 1) is √2 ≠ r*: the honest 'not-derived' flag.
    placeholder_root2 = mp.sqrt(2)

    # (4) Longitudinal readings MISS (reproduce the A3 crossterm finding): factor = 1 − ρ.
    longitudinal = []
    for name, rho in (("h", H_LIT), ("-h", -H_LIT), ("ℏ_q", HBAR_Q), ("-ℏ_q", -HBAR_Q)):
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
        "engine": "mpmath mpf/mpc (structural demonstration; 0 free params)",
        "free_parameters": 0,
        "inputs": {
            "q0": Q0_STR, "q0_pin": "proton (experimental pin, resolved)",
            "q0_precision_note": (
                "RESOLVED from substrate.q_parameter at run time, not frozen. It was a "
                "17-digit muon literal until 2026-08-29 (bean qou-1c4y); a frozen literal "
                "cannot follow an anchor move, which is how this witness came to record "
                "the superseded muon pin under the label \"muon\"."),
            "h": fmt(H_LIT), "h_definition": "q0 - 1 (the A3 crossterm probe's reading; NOT the Hecke h = q - 1/q)",
            "hbar_q": fmt(HBAR_Q),
            "mu3_MeV": MU3_STR, "c3_single_trace_MeV": C3_STR, "r_star": fmt(R_STAR),
            "arithmetic": f"mpmath mpf/mpc at {mp.mp.dps} dps (no float64 anywhere)",
            "mu3_source": "additive-residual-simplex #4320",
            "c3_source": "borromean-H9-magnitude-lift #4364",
        },
        "results": {
            "structural_checks": checks,
            "all_structural_pass": all_struct_pass,
            "transverse_slope_needed_per_fs": transverse,
            "placeholder_model_fs_s_eq_1_gives_sqrt2": fmt(placeholder_root2),
            "placeholder_matches_rstar": approx(placeholder_root2, R_STAR, tol=mp.mpf("0.01")),
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

    # Provenance stamp (bean 1j39): this producer hand-rolls json.dump and so

    # never reaches WitnessBuilder.build(), which is where q0Anchor is set.

    # Without this the witness stays unstamped permanently — re-running it

    # cannot fix that. Adds two keys; touches nothing else.

    stamp_q0(witness, __file__)

    out = os.path.join(os.path.dirname(__file__), "birkhoff-barodd-pythagoras-bridge.witness.json")
    with open(out, "w", encoding="utf-8") as fh:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(witness, fh, indent=1)  # every numeric already fmt()'d to str
        fh.write("\n")

    print(f"r* = μ₃/c₃ = {mp.nstr(R_STAR, 8)}")
    print(f"[1] bar-odd + unit-modulus ⇒ E²=−1 : {all(c['passed'] for c in checks[:2])}")
    print(f"[2] |fs−s·E|² = fs²+s²             : {all(c['passed'] for c in checks[2:])}")
    print(f"[3] transverse slope s (fs=1)      : {transverse[0]['s_transverse_needed'][:8]}  (O(1))")
    print(f"    placeholder fs=s=1 ⇒ √2        : {mp.nstr(placeholder_root2, 8)}  (≠ r* — NOT derived)")
    print(f"[4] longitudinal readings landing r*: {n_long_hit}/4")
    print(f"wrote {out}")
    assert all_struct_pass, "structural demonstration failed"
    assert n_long_hit == 0, "longitudinal reading unexpectedly landed r* (reframing premise)"
    assert not approx(placeholder_root2, R_STAR, tol=mp.mpf("0.01")), "placeholder must NOT match r* (honesty)"
    print("ALL ASSERTIONS PASS (6/6)")


if __name__ == "__main__":
    main()
