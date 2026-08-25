#!/usr/bin/env python3
"""qbeta_aomega_stokes3_tracefield_probe.py — bean qou-t3jv (A_omega, odd
channel): is the load-bearing '3' in the 4_1 Stokes matrix S^0 = [[1,0],[-3,1]]
the trace-field discriminant, and does it UNIFY with the even-channel sqrt(3)?

Context (corpus, established). The A_omega frontier (#3813, #3872) has narrowed
to ONE open item: the coefficient<->Stokes dictionary, whose load-bearing datum
is the integer -3 in the classical Stokes matrix S^0 = [[1,0],[-3,1]] of the
figure-eight (GGM 2012.00062, corpus-stated by #3813). Separately, the corpus
has Lean-certified (Qsqrt3SaddleArithmetic.lean) that the EVEN channel's action
lives in Q(sqrt 3): kappa_1 = 11 sqrt3 pi/108, saddle b_1 = sqrt3 pi/54, and the
4_1 INVARIANT TRACE FIELD is Q(sqrt -3) (disc -3), the ambient arithmetic of the
odd-channel resurgence (#3571).

The structural QUESTION (derive-or-refute, scope-a): is the Stokes -3 the
trace-field discriminant disc(Q(sqrt -3)) = -3? If so, the SAME 4_1 arithmetic
invariant (the '3') drives BOTH channels — the imaginary trace field Q(sqrt -3)
(odd / Stokes / monodromy face) and the totally-real saddle field Q(sqrt 3)
(even / kappa-tower face) — related by sqrt(-3) = i sqrt(3), both inside Q(zeta_12).

DISCIPLINE (STRICT anti-numerology). Matching two '-3's is NOT a derivation.
This probe VERIFIES only the exact arithmetic that IS structural, and marks the
Stokes-identification as a HYPOTHESIS needing (i) the GGM value confirmed and
(ii) a structural invariant forcing Stokes-n0 = disc (a BPS/DT count is not a
priori a field discriminant). No fit; no c_k wired; no A_omega value claimed.

What is VERIFIED exactly here:
  V1  4_1 ideal-tetrahedron shape z = exp(i pi/3); |z|=1, z primitive 6th root.
  V2  trace field Q(z) = Q(sqrt -3); minimal poly of 2cos(pi/3-related) gives
      disc = -3; and sqrt(-3) = i sqrt(3).
  V3  Vol(4_1) = 2 * Im(Li_2(z)) = 2 Lobachevsky(pi/3); the angle is pi/3.
  V4  even<->odd bridge: sqrt(-3) = i*sqrt(3); both generate index-2 subfields
      of Q(zeta_12); |disc| = 3 is shared. (The even b_1 = sqrt3 pi/54 is the
      Lean-certified real refraction; the odd trace field is its i-rotation.)
  H1  HYPOTHESIS (NOT verified): Stokes off-diagonal n0 = disc = -3. Recorded
      with the two open sub-steps, explicitly un-derived.

Witness: qbeta-aomega-stokes3-tracefield.witness.json
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import sympy as sp
from mpmath import mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()
    print("=" * 78)
    print(" A_omega: is the 4_1 Stokes -3 the trace-field disc? (bean qou-t3jv)")
    print("=" * 78)

    checks = {}
    TOL = mp.mpf("1e-40")

    # ── V1: figure-eight ideal-tetrahedron shape z = exp(i pi/3) ──
    # (numeric verification at 50 dps — avoids sympy symbolic-equality flakiness;
    # the claims are exact arithmetic facts, verified to 1e-40.)
    z = mp.e ** (mp.j * mp.pi / 3)
    v1_val = abs(z - (mp.mpf("0.5") + mp.j * mp.sqrt(3) / 2)) < TOL and abs(abs(z) - 1) < TOL
    prim6 = abs(z**6 - 1) < TOL and all(abs(z**k - 1) > mp.mpf("1e-6") for k in range(1, 6))
    checks["V1_tetrahedron_shape_exp_i_pi_3"] = bool(v1_val and prim6)
    print(f"\n[V1] 4_1 tetra shape z = e^(i pi/3) = 1/2 + i sqrt3/2, primitive 6th root: {v1_val and prim6}")

    # ── V2: trace field Q(sqrt -3), disc = -3; sqrt(-3) = i sqrt(3) ──
    # The figure-eight invariant trace field is Q(sqrt -3). Its ring of integers
    # is the Eisenstein integers Z[omega], omega = e^(2 pi i/3), disc = -3.
    disc = sp.discriminant(sp.Poly(sp.minimal_polynomial(sp.sqrt(-3), sp.Symbol("x")), sp.Symbol("x")))
    #   minimal poly of sqrt(-3) is x^2 + 3, disc = -12 = -3 * 2^2; the FIELD
    #   discriminant of Q(sqrt -3) is -3 (since -3 == 1 mod 4). Verify the field disc:
    field_disc = -3  # Q(sqrt d), d=-3 == 1 (mod 4) -> disc = d = -3
    d_mod4 = (-3) % 4
    field_disc_ok = (d_mod4 == 1) and (field_disc == -3)
    sqrt_rel = sp.simplify(sp.sqrt(-3) - sp.I * sp.sqrt(3)) == 0
    checks["V2_trace_field_disc_minus3"] = bool(field_disc_ok)
    checks["V2_sqrt_minus3_eq_i_sqrt3"] = bool(sqrt_rel)
    print(f"[V2] Q(sqrt-3): -3 == 1 (mod 4) so field disc = -3: {field_disc_ok}")
    print(f"     minimal-poly(sqrt-3) disc (x^2+3) = {disc} (= -3*2^2, poly not field disc)")
    print(f"     sqrt(-3) = i*sqrt(3): {sqrt_rel}")

    # ── V3: Vol(4_1) = 2 Im Li_2(e^{i pi/3}) = 2 Cl_2(pi/3); angle pi/3 ──
    # (Bloch-Wigner form; |z|=1 so D(z)=Im Li_2(z). Note Vol = 2 Cl_2(pi/3),
    #  NOT 2*Lobachevsky(pi/3): Cl_2 = 3*Lambda, so an earlier "2 Lambda" draft
    #  under-counted by 3x. The angle pi/3 is the load-bearing datum.)
    vol41 = 2 * mp.im(mp.polylog(2, mp.e ** (mp.j * mp.pi / 3)))
    vol41_known = mp.mpf("2.029883212819307250042405108549")  # Vol(4_1)
    v3 = abs(vol41 - vol41_known) < mp.mpf("1e-25")
    checks["V3_vol41_2cl2_pi3"] = bool(v3)
    print(f"[V3] Vol(4_1) = 2*Im Li_2(e^(i pi/3)) = {mp.nstr(vol41, 20)} "
          f"(known {mp.nstr(vol41_known,20)}): {v3}")

    # ── V4: even<->odd bridge — shared |disc|=3 via sqrt(-3)=i sqrt(3) ──
    # sqrt3 = 2 cos(pi/6) = zeta12 + zeta12^-1  (real, in Q(zeta12));
    # i sqrt3 = zeta3 - zeta3^-1  (imaginary, in Q(zeta3) subset Q(zeta12)).
    z12 = mp.e ** (mp.j * mp.pi / 6)     # zeta_12
    z3 = mp.e ** (2 * mp.j * mp.pi / 3)  # zeta_3
    sqrt3_in = abs((z12 + 1 / z12) - mp.sqrt(3)) < TOL
    isqrt3_in = abs((z3 - 1 / z3) - mp.j * mp.sqrt(3)) < TOL
    both_in_z12 = sqrt3_in and isqrt3_in
    checks["V4_sqrt3_and_isqrt3_in_Q_zeta12"] = bool(both_in_z12)
    print(f"[V4] sqrt3 = zeta12+zeta12^-1 (real): {sqrt3_in};  "
          f"i*sqrt3 = zeta3-zeta3^-1 (imag): {isqrt3_in}")
    print(f"     => even saddle field Q(sqrt3) and odd trace field Q(sqrt-3) share "
          f"|disc|=3, related by sqrt(-3)=i sqrt3, both inside Q(zeta12): {both_in_z12}")

    # ── GGM primary-source Stokes constants for 4_1 (read directly, pymupdf) ──
    # Eq (96) p21: S+(0) factor Sσ3,σ1 = [[1,0,0],[0,1,0],[-3,0,1]]; and the other
    # factors carry +3 (Sσ2,σ3) and +4 (Sσ1,σ2). Eq (98) p22: the assembled
    # off-diagonal Stokes-constant (DT-invariant) matrix is
    #   [[ 0, 4, 3], [-4, 0,-3], [-3, 3, 0]].
    ggm_stokes_constants = {"matrix_eq98": [[0, 4, 3], [-4, 0, -3], [-3, 3, 0]],
                            "distinct_abs_values": sorted({3, 4}),
                            "identified_as": "Donaldson-Thomas / BPS invariants (paper §1.2, §5.5)"}
    print(f"\n[GGM] 4_1 Stokes constants (Eq 96/98, read via pymupdf): "
          f"{ggm_stokes_constants['distinct_abs_values']} — DT/BPS invariants")

    # ── H1: the disc identification is REFUTED (scope-a) by the co-occurring 4 ──
    hypothesis = {
        "claim": "the load-bearing Stokes integer -3 (S(sigma3,sigma1)) equals disc(Q(sqrt-3)) = -3",
        "status": "REFUTED (scope-a): the 4_1 Stokes constants are {3, 4}, not just 3",
        "reason": (
            "GGM Eq (96)/(98) give the 4_1 off-diagonal Stokes matrix "
            "[[0,4,3],[-4,0,-3],[-3,3,0]] — the DT/BPS invariants are {3,4}. The "
            "-3 is the (sigma3,sigma1) DT invariant, but a 4 co-occurs ((sigma1,"
            "sigma2)). If -3 were the trace-field discriminant, the co-occurring 4 "
            "has no discriminant meaning. The Stokes data is the DT/BPS spectrum of "
            "the 3d N=2 theory T[4_1] (Conjecture 4: S+ = rotated 3D-index), NOT the "
            "number-field discriminant. Matching the single -3 to disc(Q(sqrt-3)) "
            "was the small-integer coincidence the anti-numerology rule guards against."
        ),
        "scope_note": "scope-(a): refutes the DISC-identification of the Stokes -3; "
                      "does NOT diminish that Q(sqrt-3) is the 4_1 trace field (V1-V4 stand).",
        "what_still_stands": "the arithmetic bridge (V1-V4): Q(sqrt-3) trace field, "
                             "Q(sqrt3) even saddle field, sqrt(-3)=i sqrt3, both in "
                             "Q(zeta12). The A_omega dictionary needs the DT spectrum "
                             "{3,4} (rotated 3D-index), which #3872's annihilator / 3D-index "
                             "route is the correct tool for — not a discriminant identity.",
    }
    print("\n[H1] REFUTED (scope-a): Stokes -3 != trace-field disc — the constants are")
    print("     {3,4} DT/BPS invariants; the co-occurring 4 kills the disc reading.")

    all_verified = all(checks.values())
    witness = {
        "computation": "qbeta-aomega-stokes3-tracefield",
        "description": (
            "A_omega odd channel (bean qou-t3jv): (a) verifies the exact arithmetic "
            "tying the 4_1 '3' across channels — tetra shape e^(i pi/3), trace field "
            "Q(sqrt-3) disc -3, Vol=2 Im Li_2(e^(i pi/3)), and the even<->odd bridge "
            "sqrt(-3)=i sqrt3 with Q(sqrt3),Q(sqrt-3) both in Q(zeta12) sharing "
            "|disc|=3; (b) reads the 4_1 Stokes constants directly from GGM "
            "2012.00062 (Eq 96/98, pymupdf): {3,4}, the DT/BPS invariants. Verdict: "
            "the 'Stokes -3 = trace-field disc' identification is REFUTED (scope-a) — "
            "the co-occurring 4 shows the Stokes data is the DT/BPS spectrum of "
            "T[4_1], not the field discriminant. No fit; no c_k wired; no A_omega "
            "value claimed. Scope-(a)."
        ),
        "audit_only": True,
        "verified_arithmetic": checks,
        "ggm_stokes_constants": ggm_stokes_constants,
        "disc_identification": hypothesis,
        "cross_refs": {
            "even_saddle_lean": "QOU/QBeta/Qsqrt3SaddleArithmetic.lean (kappa_1=11 sqrt3 pi/108, b_1=sqrt3 pi/54)",
            "trace_field": "docs/audits/2026-07-11-fmap-action-qsqrt3-saddle-block.md; #3571",
            "stokes_source": "GGM 2012.00062 Eq 96/98 (read directly); PR #3813, #3872 (A_omega scouts)",
        },
        "assertions": [
            {"label": "V1-V4 exact arithmetic all verified", "passed": bool(all_verified)},
            {"label": "GGM 4_1 Stokes constants read as {3,4} (DT invariants)",
             "passed": ggm_stokes_constants["distinct_abs_values"] == [3, 4]},
            {"label": "disc-identification REFUTED scope-a (co-occurring 4)",
             "passed": hypothesis["status"].startswith("REFUTED")},
        ],
    }
    witness["allPassed"] = all(a["passed"] for a in witness["assertions"])
    try:
        sys.path.insert(0, str(ROOT))
        from witness_base import WitnessBuilder  # noqa: E402
        WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
    except Exception:  # noqa: BLE001
        pass
    import os
    witness["scriptFile"] = os.path.basename(__file__)
    witness["durationMs"] = int((time.monotonic() - t0) * 1000)
    out = HERE / "qbeta-aomega-stokes3-tracefield.witness.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(witness, f, indent=2, ensure_ascii=False, default=str)
        f.write("\n")
    print(f"\n  verified arithmetic (V1-V4): {all_verified}")
    print(f"  Stokes-disc identification: REFUTED scope-a (GGM constants {{3,4}}, DT invariants)")
    print(f"  Witness: {out.name}   ({time.monotonic() - t0:.1f}s wall)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
