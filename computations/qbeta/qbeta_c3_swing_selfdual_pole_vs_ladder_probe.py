#!/usr/bin/env python3
"""qbeta_c3_swing_selfdual_pole_vs_ladder_probe.py

Discriminate two competing functional forms for the c₃ bar-odd `S` swing —
reconciling the PR #4064 c₃⟺q₀ unification synthesis with the already-MERGED
capstone (PRs #3600/#3636/#3654,
[`2026-07-12-c3-wall-resolution-capstone.md`]).

Background. The bar-odd target is `S(q) = c3_target_at(q, Q_β, m_e) + Vol(4₁)`
(`qbeta_utils`), a DETERMINISTIC function of the substrate q₀. It has a fixed
zero at `q* = 1.10997859303152…` (the pure bar-even / ε=0 / CS→0 point), nonzero
and opposite-signed at the two mass pins (`S(muon)=+0.00968`, `S(proton)=−0.03946`)
— so `q*` is a genuine CROSSING, not a tautological "zero wherever you pin q₀".

Two accounts of the huge slope `dc₃/dq ≈ 4.66×10⁶` (the "swing"):

  (C) CAPSTONE (merged): the swing is a `1/u³` LADDER-inversion representation
      artifact over SMOOTH geometry, `u = b·ℏ_q² ≈ 0.00852` the truncation
      small-parameter; `S'(q*) = 2.37 × (1/u³)`, a smooth O(1) prefactor. The
      state integral (Φ_b, #3654) is smooth and anchor-blind — "there was no
      singularity to break."

  (P) PR #4064 SYNTHESIS reinterpretation: the swing is a RIGIDITY DIVERGENCE at
      the self-dual / Chern–Simons-degeneration locus (`Φ_odd → 0`, so
      `dΦ_odd/dq → ∞`), with a pole-form `swing ≈ 1/|u²−1|`.

This probe tests (P) against (C) with the deterministic extractor, at full
precision. It is a scope-(a) consistency check, not a new closure.

FINDINGS (scope-(a); C14; no c_k wired; no fit; no tier change):

  1. **q\\* is a SIMPLE zero of S** — `S(q*)≈0`, `S'(q*)` and `S''(q*)` both
     FINITE. An analytic simple zero has NO pole and NO branch point, so `S`
     (hence `Φ_odd ∝ S`) does not diverge, and neither does any derivative
     ratio `dΦ_odd/dq / Φ_odd` in a way that produces the swing magnitude. The
     "rigidity divergence at q*" mechanism has no numerical support at q*.

  2. **The pole form `1/|u²−1|` is off by ~6 orders of magnitude.** At q₀ the
     ladder parameter is tiny (`u ≈ 0.0085`, `u² ≈ 7.3×10⁻⁵`), so
     `1/|u²−1| ≈ 1.00007` — an O(1) number. The measured swing is `≈ 3.84×10⁶`.
     Matching (P) would require an un-derived prefactor `≈ 3.84×10⁶`; the scale
     gap `(1/u³)/(1/|u²−1|) ≈ 1.6×10⁶` is exactly `1/u³` up to O(1). q₀ is NOT
     near any `u²→1` self-dual locus in the ladder variable — `u` there is small,
     nowhere near 1.

  3. **The swing IS `1/u³` (capstone reproduced).** `S'(q*) = prefactor × 1/u³`
     with `prefactor ≈ 2.37` (smooth O(1)). The magnitude is the extractor's
     `/u³` division of a smooth numerator zero — form (C), merged.

CONCLUSION (scope-(a)). The self-dual-pole reinterpretation of the swing (P)
conflates the ladder small-parameter `u = b·ℏ_q²` (which drives the `1/u³`
amplification) with the Chern–Simons meridian variable, and mistakes the SIMPLE
zero of `S` at `q*` for a pole. The merged capstone stands: the swing is a
`1/u³` representation artifact over smooth geometry, not a divergence at a
self-dual locus.

What SURVIVES and is SHARPENED (the non-circular core, unchanged): `q*` is a
fixed simple zero of the deterministic bar-odd extractor — the CS→0 / ε=0 point
— a third, decay-sector determination of q₀. The swing and `q*` are SEPARATE
facts that merely coincide at `q*`; the swing is not the "signature" of a
divergence at the self-dual locus. This keeps the PR #4064 synthesis honest:
c₃ and q₀ may still share the target `q*`, but the SWING is not extra evidence
for a pole there.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import c3_target_at, substrate_ladder_quantities  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402

mp.mp.dps = 60
ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
with mp.workdps(60):
    VOL41 = +(2 * mp.clsin(2, mp.pi / 3))


def S(q):
    return c3_target_at(q, QCOD, ME) + VOL41


def main() -> int:
    print("=" * 78)
    print(" c₃ swing: self-dual pole 1/|u²−1|  vs  1/u³ ladder artifact")
    print("=" * 78)

    qp, qm = q_at(60), q_muon_at(60)
    print("\n[0] anchors (deterministic extractor; genuine opposite-sign crossing):")
    print(f"    S(proton)={mp.nstr(S(qp),8)}   S(muon)={mp.nstr(S(qm),8)}")
    repro = (abs(S(qp) - mp.mpf("-0.03945936")) < mp.mpf("1e-6")
             and abs(S(qm) - mp.mpf("0.00968298")) < mp.mpf("1e-6"))

    # ---- q* root-found ----
    qstar = mp.findroot(S, (qp + qm) / 2)
    frac = (qstar - qp) / (qm - qp)
    print("\n[1] q* (S=0, CS→0 / ε=0 point):")
    print(f"    q* = {mp.nstr(qstar,25)}   ({mp.nstr(frac*100,5)}% muon-ward)")
    print(f"    S(q*) = {mp.nstr(S(qstar),4)}  (≈0)")

    # ---- FINDING 1: simple zero (S', S'' finite -> no pole) ----
    Sp = mp.diff(S, qstar)
    Spp = mp.diff(S, qstar, 2)
    is_simple_zero = mp.isfinite(Sp) and mp.isfinite(Spp) and abs(Sp) > 0
    print("\n[2] FINDING 1 — q* is a SIMPLE zero (finite S', S'' ⇒ no pole/branch point):")
    print(f"    S'(q*)  = {mp.nstr(Sp,8)}   (finite)")
    print(f"    S''(q*) = {mp.nstr(Spp,8)}   (finite)")
    print("    ⇒ S (hence Φ_odd ∝ S) does not diverge at q*; the 'rigidity")
    print("      divergence at the self-dual locus' mechanism has no support at q*.")

    # ---- FINDING 2: pole form vs ladder form ----
    u = substrate_ladder_quantities(qstar)["u"]
    inv_u3 = 1 / u ** 3
    pole = 1 / abs(u ** 2 - 1)
    prefactor = Sp * u ** 3
    scale_gap = inv_u3 / pole
    print("\n[3] FINDING 2 — pole form 1/|u²−1| is ~6 orders too small:")
    print(f"    u={mp.nstr(u,8)}  u²={mp.nstr(u**2,8)}  1/|u²−1|={mp.nstr(pole,10)} (O(1))")
    print(f"    1/u³={mp.nstr(inv_u3,8)}   measured swing S'(q*)={mp.nstr(Sp,8)}")
    print(f"    scale gap (1/u³)/(1/|u²−1|) = {mp.nstr(scale_gap,8)}  (≈ 1/u³ up to O(1))")
    print("    ⇒ q₀ is NOT near a u²→1 self-dual locus (u≈0.0085, far from 1);")
    print("      matching (P) needs an un-derived prefactor ≈ 3.8e6.")

    print("\n[4] FINDING 3 — the swing IS 1/u³ (capstone reproduced):")
    print(f"    S'(q*) = {mp.nstr(prefactor,6)} × (1/u³)   (smooth O(1) prefactor)")

    pole_form_dead = float(scale_gap) > 1e4  # >4 orders => decisively not the pole form
    ladder_form_ok = mp.mpf("1") < abs(prefactor) < mp.mpf("10")

    verdict = (is_simple_zero and pole_form_dead and ladder_form_ok)
    print("\n" + "=" * 78)
    print(f" VERDICT: self-dual-pole reinterpretation REFUTED (scope-(a)); "
          f"1/u³ capstone stands  [{'PASS' if verdict else 'CHECK'}]")
    print("=" * 78)

    wb = WitnessBuilder("qbeta-c3-swing-selfdual-pole-vs-ladder", engine="mpmath")
    wb.set_description(
        "Discriminate the c₃ bar-odd swing's functional form: the PR #4064 "
        "synthesis's self-dual/CS-degeneration POLE form (swing ≈ 1/|u²−1|, a "
        "'rigidity divergence' at q*) vs the MERGED capstone's 1/u³ LADDER artifact "
        "(#3600/#3636/#3654). Deterministic extractor S(q)=c3_target_at+Vol(4₁), "
        "full precision. (1) q* is a SIMPLE zero — S'(q*)≈3.84e6 and S''(q*)≈−3.70e8 "
        "both FINITE ⇒ no pole/branch point, so Φ_odd∝S does not diverge at q*; the "
        "'rigidity divergence at the self-dual locus' has no support there. (2) The "
        "pole form 1/|u²−1|≈1.00007 (u=b·ℏ_q²≈0.0085, u²≈7.3e-5) is O(1) — ~6 orders "
        "of magnitude below the measured swing; q₀ is NOT near a u²→1 locus. (3) The "
        "swing IS 1/u³: S'(q*)=2.37×(1/u³), smooth O(1) prefactor (capstone). "
        "Scope-(a) REFUTATION of the pole reinterpretation; the 1/u³ capstone stands. "
        "SURVIVES: q* remains a fixed simple zero (CS→0/ε=0), a third decay-sector "
        "determination of q₀ — but the swing and q* are separate facts coinciding at "
        "q*, not evidence for a pole. No c_k wired; no fit; C14; no tier change."
    )
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("q_star", {
        "value": mp.nstr(qstar, 25),
        "frac_muon_ward_pct": mp.nstr(frac * 100, 8),
        "S_at_qstar": mp.nstr(S(qstar), 6),
        "anchors_reproduced": bool(repro),
        "meaning": "S=0: c3 = -Vol(4_1) exactly (pure bar-even, eps=0, CS->0 locus)",
    })
    wb.add_data("finding1_simple_zero", {
        "S_prime_qstar": mp.nstr(Sp, 10),
        "S_double_prime_qstar": mp.nstr(Spp, 10),
        "is_simple_zero": bool(is_simple_zero),
        "verdict": "finite S', S'' => analytic simple zero, no pole/branch point; "
                   "Phi_odd ∝ S does not diverge at q* (rigidity-divergence mechanism unsupported)",
    })
    wb.add_data("finding2_pole_vs_ladder", {
        "u": mp.nstr(u, 12),
        "u_squared": mp.nstr(u ** 2, 12),
        "pole_form_1_over_abs_u2_minus_1": mp.nstr(pole, 12),
        "inv_u_cubed": mp.nstr(inv_u3, 10),
        "measured_swing_S_prime": mp.nstr(Sp, 10),
        "scale_gap_uladder_over_pole": mp.nstr(scale_gap, 10),
        "pole_form_dead": bool(pole_form_dead),
        "verdict": "1/|u^2-1| ~ 1 is ~6 orders below the swing; q0 not near a u^2->1 "
                   "self-dual locus; pole reinterpretation refuted (scope-(a))",
    })
    wb.add_data("finding3_ladder_form", {
        "smooth_prefactor": mp.nstr(prefactor, 8),
        "ladder_form_ok": bool(ladder_form_ok),
        "verdict": "S'(q*) = 2.37 x (1/u^3), smooth O(1) prefactor -- the 1/u^3 "
                   "capstone (merged #3636) stands",
    })
    wb.add_data("scope", {
        "tier": "scope-(a) consistency check / refutation of a reinterpretation",
        "structural_exclusion": False,
        "note": "This is a scope-(a) negative on a FUNCTIONAL FORM (1/|u^2-1| does not "
                "reproduce the swing), supported by the computed simple-zero fact "
                "(S',S'' finite). It does NOT exclude the c3<->q0 unification's shared "
                "target q*; it removes the swing as evidence for a POLE at q*.",
        "c_k_wired": False, "fit": False, "canonical_flip": None,
    })
    wb.add_assertion(
        "qstar_is_simple_zero_no_pole",
        computed=1.0 if is_simple_zero else 0.0, expected=1.0, tolerance=0.5,
        source="S'(q*) and S''(q*) both finite => analytic simple zero; S (hence Phi_odd) "
               "does not diverge at q*, so the 'rigidity divergence at the self-dual locus' "
               "mechanism has no support at q*")
    wb.add_assertion(
        "selfdual_pole_form_refuted_by_scale",
        computed=1.0 if pole_form_dead else 0.0, expected=1.0, tolerance=0.5,
        source="1/|u^2-1| ~ 1.00007 (O(1)) is ~6 orders of magnitude below the measured "
               "swing S'(q*) ~ 3.84e6; scale gap = 1/u^3 up to O(1); q0 not near a u^2->1 locus")
    wb.add_assertion(
        "swing_is_ladder_1_over_u3_smooth_prefactor",
        computed=float(prefactor), expected=2.37, tolerance=0.5,
        source="S'(q*) = 2.37 x (1/u^3), smooth O(1) prefactor -- the merged 1/u^3 capstone "
               "(#3636) stands; the swing is a representation artifact, not a self-dual pole")
    wb.add_assertion(
        "anchors_reproduced_exactly",
        computed=1.0 if repro else 0.0, expected=1.0, tolerance=0.5,
        source="S(proton)/S(muon) from c3_target_at match the committed anchor-blind witness "
               "(genuine opposite-sign crossing at q*)")
    wb.save()
    print("\n  RESULT: self-dual-pole reinterpretation of the swing REFUTED (scope-(a)); "
          "q* is a simple zero; the 1/u³ capstone stands.")
    return 0 if verdict else 1


if __name__ == "__main__":
    raise SystemExit(main())
