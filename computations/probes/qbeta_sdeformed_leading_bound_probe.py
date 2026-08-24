#!/usr/bin/env python3
"""qbeta_sdeformed_leading_bound_probe.py — the leading-form magnitude bound
decouples the open u(q₀) into two orthogonal sub-obstructions.

Subgoal-2 attempt to derive S = Q_β/E₀, off the fibre→observable bridge verdict
(PR #4520). The SDeformedVolumeChannel keystone reduces the derivation to the
open substrate meridian-deformation map u(q₀); the real-boost part is DERIVED
(Re u = ln q₀, meridian-holonomy-boost.md, bean qou-zuk4), the spin part is open.

THE INVARIANT (formalize-first; companion Lean
FigureEightComplexVolume.imV₄₁_le_cuspModulus_reSq / _leading_unreachable_of_lt).
The concrete leading Neumann–Zagier form gives (sorry-free imV₄₁):

    Im 𝔙₄₁(u) = κ·(Re²u − Im²u),   κ = √3/4 > 0   (A-poly cusp modulus τ = −i√3).

Since Im²u ≥ 0 and κ > 0, this is bounded above by its value on the real axis:

    Im 𝔙₄₁(u) ≤ κ·(Re u)²    for EVERY u (any real spin Im u).

The spin part can only DECREASE Im 𝔙₄₁ below κ·Re²u — it flips the sign
(diagonal crossing) but can NEVER lift the magnitude above κ·Re²u.

DERIVE-THEN-CHECK at the derived boost Re u = ln q₀ (nothing inverted to match S;
S_μ, S_p are cited measurements from sdeformed_channel_signflip_probe.py):

  [C1] cap = κ·(ln q₀)² ≈ 0.004714 (= the G1 real-boost value).
  [C2] MUON UNREACHABLE at leading order: S_μ ≈ 0.009683 = 2.054 × cap
       ⇒ required Im²u = Re²u − S_μ/κ < 0 (impossible for real spin).
       ⇒ the muon magnitude is a sub-obstruction ORTHOGONAL to the sign flip:
         it needs the even O(u⁴) NZ tail or an enlarged Re u, NOT the spin part.
  [C3] PROTON reachable: S_p < 0 ⇒ required Im²u = Re²u − S_p/κ > 0
       (real spin exists; diagonal crossed) — the sign flip IS a spin datum.
  [C4] gross-ratio sanity: the CAL-2 gross Q_β = m_e|q₀²−2q₀−1|(q₀+1)/(2q₀³) has
       its sign controlled by (q₀²−2q₀−1), constant near q₀ (zero only at the
       silver ratio q₀ = 1+√2); the measured sign flip lives in the c₃ leak, not
       the gross closed form (the two-"S" distinction).

Anti-fit / anti-laundering: κ and Re u = ln q₀ are DERIVED (A-poly cusp modulus;
meridian-holonomy boost); no coefficient tuned to S; no keystone instance
fabricated; no c_k wired; S not axiomatized. Scope-(a): a magnitude
insufficiency of the LEADING form, NOT an exclusion of the channel identity
(the full 𝔙_q carries the O(u⁴) tail). mpmath dps 50, no float64.

Run:  python3 -u qbeta_sdeformed_leading_bound_probe.py 2>&1 | tee /tmp/bound.log
"""
from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# Derived geometric data (NOT fitted).
KAPPA = mp.sqrt(3) / 4                       # A-poly cusp modulus |a₂|, τ = −i√3
# Muon-anchored canonical substrate modulus (computations/ layer, muon q₀).
Q0 = mp.mpf("1.10997859555733471")
RE_U = mp.log(Q0)                            # derived real boost, meridian-holonomy-boost.md

# Measured bar-odd complex-volume leak (cited: sdeformed_channel_signflip_probe.py L78-82,
# S = c₃ + Vol(4₁); qbeta-udeform-map-constraint witness #3773). NOT fitted here.
S_MUON = mp.mpf("0.00968298")
S_PROTON = mp.mpf("-0.03945936")

# CAL-2 gross closed form (cheat-sheet), for the two-"S" sanity row.
M_E = mp.mpf("0.51099895000")                # MeV
SILVER = 1 + mp.sqrt(2)                       # zero of q²−2q−1


def main() -> int:
    print("=" * 78)
    print(" leading NZ magnitude bound — muon unreachable, sign flip is a spin datum")
    print("=" * 78)
    assertions = []
    t0 = datetime.now(timezone.utc)

    cap = KAPPA * RE_U ** 2
    print(f"\n[C1] κ = √3/4 = {mp.nstr(KAPPA, 12)}")
    print(f"     Re u = ln q₀ = {mp.nstr(RE_U, 12)}  (derived boost)")
    print(f"     leading cap κ·(ln q₀)² = {mp.nstr(cap, 12)}  (= G1 real-boost value)")
    assertions.append({
        "name": "leading_cap_equals_real_boost_value",
        "computed": float(cap), "expected": 0.004714, "tolerance": 1e-5,
        "passed": bool(abs(cap - mp.mpf("0.004714")) < 1e-5),
        "source": "κ·(ln q₀)² = the pure-boost Im 𝔙₄₁ (G1), the leading upper bound"})

    # [C2] muon: unreachable at leading order.
    need_im2_mu = RE_U ** 2 - S_MUON / KAPPA
    ratio_mu = S_MUON / cap
    mu_unreachable = S_MUON > cap
    print(f"\n[C2] MUON: S_μ = {mp.nstr(S_MUON, 10)} = {mp.nstr(ratio_mu, 6)} × cap")
    print(f"     required Im²u = Re²u − S_μ/κ = {mp.nstr(need_im2_mu, 10)}"
          f"  ({'<0 IMPOSSIBLE' if need_im2_mu < 0 else '≥0'})")
    print(f"     ⇒ S_μ exceeds the leading cap ⇒ NO real spin reaches it: "
          f"{mu_unreachable}")
    assertions.append({
        "name": "muon_exceeds_leading_cap",
        "computed": float(ratio_mu), "expected": 2.054, "tolerance": 1e-2,
        "passed": bool(mu_unreachable and ratio_mu > 2.0),
        "source": "S_μ = 2.054 × κ(ln q₀)² > cap ⇒ required Im²u < 0 ⇒ "
                  "unreachable by leading form for any real spin"})
    assertions.append({
        "name": "muon_required_im2_negative",
        "computed": float(need_im2_mu), "expected": -0.01147, "tolerance": 1e-4,
        "passed": bool(need_im2_mu < 0),
        "source": "Im²u = Re²u − S_μ/κ < 0 (impossible): muon magnitude is NOT a "
                  "spin datum; needs O(u⁴) NZ tail or enlarged Re u"})

    # [C3] proton: reachable, spin exists.
    need_im2_pr = RE_U ** 2 - S_PROTON / KAPPA
    pr_spin_exists = need_im2_pr > 0
    print(f"\n[C3] PROTON: S_p = {mp.nstr(S_PROTON, 10)} < 0")
    print(f"     required Im²u = Re²u − S_p/κ = {mp.nstr(need_im2_pr, 10)}"
          f"  ({'>0 real spin exists' if pr_spin_exists else '<0'})")
    print(f"     ⇒ the sign flip IS realizable by the spin part (diagonal crossed)")
    assertions.append({
        "name": "proton_signflip_spin_exists",
        "computed": float(need_im2_pr), "expected": 0.10201, "tolerance": 1e-4,
        "passed": bool(pr_spin_exists),
        "source": "Im²u = Re²u − S_p/κ > 0 ⇒ a real spin part reproduces S_p<0 "
                  "(the sign flip is a spin datum, open bean qou-fook)"})

    # [C4] gross-ratio two-S sanity: sign controlled by (q²−2q−1), constant near q₀.
    poly = Q0 ** 2 - 2 * Q0 - 1
    dq = mp.mpf("1.15e-8") * Q0                # ~muon↔proton anchor gap
    poly_shift = (Q0 + dq) ** 2 - 2 * (Q0 + dq) - 1
    gross_no_flip = (poly < 0) and (poly_shift < 0)
    print(f"\n[C4] gross Q_β sign factor (q₀²−2q₀−1) = {mp.nstr(poly, 10)} "
          f"(zero at silver ratio q=1+√2={mp.nstr(SILVER, 8)})")
    print(f"     across anchor gap: {mp.nstr(poly_shift, 10)} — same sign ⇒ gross "
          f"Q_β does NOT flip near q₀; the flip is the c₃ leak (two-S distinction)")
    assertions.append({
        "name": "gross_Qbeta_no_signflip_near_substrate",
        "computed": 1.0 if gross_no_flip else 0.0, "expected": 1.0, "tolerance": 0.0,
        "passed": bool(gross_no_flip),
        "source": "(q₀²−2q₀−1) constant-sign near q₀ (zero only at q=1+√2); the "
                  "measured sign flip lives in the c₃ complex-volume leak"})

    dur = (datetime.now(timezone.utc) - t0).total_seconds()
    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "OPEN — reduced, sharpened. The leading NZ form Im 𝔙₄₁ ≤ κ·Re²u caps the "
        "channel at the derived boost Re u = ln q₀: the MUON leak (S_μ = 2.054× "
        "cap) is UNREACHABLE for any real spin (required Im²u < 0), while the "
        "PROTON sign flip IS a spin datum (required Im²u > 0). So the single open "
        "u(q₀) piece decouples into two orthogonal sub-obstructions — proton sign "
        "flip (spin part, open, qou-fook) and muon magnitude (even O(u⁴) NZ tail "
        "or enlarged Re u, NEW, beaned). Not a derivation of S (CAL-2 input). "
        "Scope-(a) magnitude insufficiency of the leading form; no fit; no c_k "
        "wired; S not axiomatized.")
    print("\nVERDICT:", verdict)

    witness = {
        "engine": "mpmath",
        "engineVersion": f"mpmath {mp.__version__}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "qbeta-sdeformed-leading-bound",
        "scriptFile": "qbeta_sdeformed_leading_bound_probe.py",
        "commitSha": subprocess.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True,
            check=True).stdout.strip(),
        "contentBlock": "conj:binding-qbeta-complex-volume",
        "discipline": (
            "scope-(a) magnitude insufficiency of the LEADING NZ form (invariant "
            "Im²u≥0, κ>0); NOT a scope-(b) exclusion of the channel identity "
            "S=Im 𝔙_q (the full quantum complex volume carries the O(u⁴) tail "
            "dropped here). Not a derivation of S = Q_β/E₀ (CAL-2 input; Subgoal-2 "
            "open). Anti-fit: κ=√3/4 and Re u=ln q₀ derived (A-poly cusp modulus; "
            "meridian-holonomy boost); S_μ, S_p cited measurements; no coefficient "
            "tuned; no keystone instance fabricated; S not axiomatized; no c_k "
            "wired."),
        "description": (
            "Leading-form magnitude bound Im 𝔙₄₁ ≤ κ·Re²u decouples the open "
            "u(q₀) into two orthogonal sub-obstructions: muon magnitude "
            "(unreachable by leading form + real spin, needs O(u⁴) tail/enlarged "
            "Re u) and proton sign flip (a spin datum). Companion Lean "
            "FigureEightComplexVolume.imV₄₁_le_cuspModulus_reSq / "
            "_leading_unreachable_of_lt."),
        "precisionMetadata": {"compute_dps": 50, "kappa": "sqrt(3)/4",
                              "Re_u": "ln q0 (derived meridian-holonomy boost)"},
        "data": {
            "kappa": mp.nstr(KAPPA, 30),
            "q0": mp.nstr(Q0, 30),
            "Re_u_ln_q0": mp.nstr(RE_U, 30),
            "leading_cap_kappa_ReSq": mp.nstr(cap, 30),
            "S_muon": mp.nstr(S_MUON, 15),
            "S_proton": mp.nstr(S_PROTON, 15),
            "muon_S_over_cap": mp.nstr(ratio_mu, 12),
            "muon_required_Im2u": mp.nstr(need_im2_mu, 15),
            "proton_required_Im2u": mp.nstr(need_im2_pr, 15),
            "gross_Qbeta_sign_factor_q2m2qm1": mp.nstr(poly, 15),
            "silver_ratio_zero": mp.nstr(SILVER, 15),
            "verdict": verdict},
        "assertions": assertions,
        "allPassed": all_passed,
        "durationSeconds": dur,
    }
    out = Path(__file__).with_name("qbeta-sdeformed-leading-bound.witness.json")
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nwitness → {out.name}")
    for a in assertions:
        print(f"  [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")
    print("ALL ASSERTIONS PASS" if all_passed else "ASSERTION FAILURE")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
