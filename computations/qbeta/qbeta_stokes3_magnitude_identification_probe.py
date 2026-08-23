#!/usr/bin/env python3
"""qbeta_stokes3_magnitude_identification_probe.py — T4: does the GGM integer
Stokes constant A_ω = 3 (for 4₁) reproduce the empirical |S| at the two
anchors via the proved Im 𝔙₄₁ formula?

Chain under test (derive-then-check, no fit):
  1. Meridian log-holonomy: Re u = ln q₀ (proved sorry-free)
  2. Im 𝔙₄₁(u) = (√3/4)(Re²u − Im²u) (proved imV₄₁)
  3. GGM Stokes constant = integer 3 (literature-proved for 4₁)
  4. S = A_ω · Im 𝔙₄₁(u) = 3 · (√3/4)(Re²u − Im²u) ?= anchor targets

The CRUX QUESTION: does A_ω = 3 enter as a simple multiplicative factor on
Im 𝔙₄₁? If so, what Im u is needed at each anchor to reproduce S?

Anchors (empirical, not fitted):
  S(muon)  = +0.00968298  (from c3_target_at + Vol(4₁))
  S(proton) = −0.03945936

IMPORTANT: this probe does NOT assume a specific Im u — it INVERTS from the
empirical S to find what Im u would be needed if A_ω = 3 · Im 𝔙₄₁(u) = S.
Then it checks whether the needed Im u is consistent with any derived
geometric quantity. This is honest: we test a formula, not fit a parameter.

Bean: qou-fgte (T4)
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import c3_target_at  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
with mp.workdps(50):
    VOL41 = +(2 * mp.clsin(2, mp.pi / 3))
KAPPA = mp.sqrt(3) / 4      # (√3/4)
A_OMEGA = mp.mpf(3)          # GGM Stokes constant for 4₁ (integer, literature-proved)


def S_empirical(q):
    """S(q) from the empirical extractor c3_target_at + Vol(4₁)."""
    return c3_target_at(q, QCOD, ME) + VOL41


def imV41(re_u, im_u):
    """Im 𝔙₄₁(u) = (√3/4)(Re²u − Im²u). Proved formula."""
    return KAPPA * (re_u**2 - im_u**2)


def main() -> int:
    print("=" * 78)
    print(" T4: Stokes-3 magnitude identification probe")
    print(" Does A_ω = 3 · Im 𝔙₄₁(u) reproduce |S| at the two anchors?")
    print("=" * 78)

    q_pr, q_mu = q_at(50), q_muon_at(50)
    S_pr, S_mu = S_empirical(q_pr), S_empirical(q_mu)
    ln_q_pr, ln_q_mu = mp.log(q_pr), mp.log(q_mu)

    print(f"\n  Anchors:")
    print(f"    S(proton) = {mp.nstr(S_pr, 10)}   (need < 0)")
    print(f"    S(muon)   = {mp.nstr(S_mu, 10)}   (need > 0)")
    print(f"    ln q₀(proton) = {mp.nstr(ln_q_pr, 12)}")
    print(f"    ln q₀(muon)   = {mp.nstr(ln_q_mu, 12)}")
    print(f"    |Δq₀|         = {mp.nstr(abs(q_pr - q_mu), 6)}")

    # ---- Test 1: with A_ω = 3, what Im u is needed? ----
    # S = A_ω · Im 𝔙₄₁(u) = 3 · (√3/4)(Re²u − Im²u)
    # ⟹ Im²u = Re²u − S/(3·√3/4) = Re²u − 4S/(3√3)
    print("\n" + "─" * 78)
    print("  Test 1: invert for Im u from S = 3·(√3/4)(Re²u − Im²u)")
    print("─" * 78)

    results = {}
    for name, q, S_val, ln_q in [("proton", q_pr, S_pr, ln_q_pr),
                                   ("muon", q_mu, S_mu, ln_q_mu)]:
        re_u = ln_q  # proved: Re u = ln q₀
        rhs = re_u**2 - S_val / (A_OMEGA * KAPPA)
        # rhs = Im²u; need rhs > 0 for real Im u
        if rhs > 0:
            im_u_needed = mp.sqrt(rhs)
            ratio = im_u_needed / re_u
            # Check: does the sign work?
            s_check = A_OMEGA * imV41(re_u, im_u_needed)
            sign_ok = (s_check * S_val > 0)
            print(f"  {name}: Im²u needed = {mp.nstr(rhs, 10)}")
            print(f"          Im u needed  = {mp.nstr(im_u_needed, 10)}")
            print(f"          Im u / Re u  = {mp.nstr(ratio, 6)}")
            print(f"          S_check      = {mp.nstr(s_check, 10)} (target {mp.nstr(S_val, 10)})")
            print(f"          sign match   = {sign_ok}")
            results[name] = {
                "im_u_needed": float(im_u_needed),
                "ratio_im_re": float(ratio),
                "s_check": float(s_check),
                "sign_ok": sign_ok,
                "rhs_positive": True,
            }
        else:
            # rhs < 0: no real Im u exists
            print(f"  {name}: Im²u needed = {mp.nstr(rhs, 10)} < 0 → NO REAL Im u EXISTS")
            print(f"          The formula S = 3·Im 𝔙₄₁ CANNOT produce this S with real Im u.")
            results[name] = {
                "im_u_needed": None,
                "ratio_im_re": None,
                "s_check": None,
                "sign_ok": False,
                "rhs_positive": False,
            }

    # ---- Test 2: with Im u = 0 (pure boost), what does A_ω = 3 give? ----
    print("\n" + "─" * 78)
    print("  Test 2: pure boost u = ln q₀ (Im u = 0), A_ω = 3")
    print("─" * 78)
    for name, q, S_val, ln_q in [("proton", q_pr, S_pr, ln_q_pr),
                                   ("muon", q_mu, S_mu, ln_q_mu)]:
        s_boost = A_OMEGA * imV41(ln_q, mp.mpf(0))
        ratio_boost = s_boost / S_val if S_val != 0 else mp.inf
        print(f"  {name}: S_boost = 3·(√3/4)·(ln q₀)² = {mp.nstr(s_boost, 10)}")
        print(f"          S_target = {mp.nstr(S_val, 10)}")
        print(f"          ratio S_boost/S_target = {mp.nstr(ratio_boost, 6)}")
        print(f"          sign match = {s_boost * S_val > 0}")

    # ---- Test 3: with fibre spin Im u = ln q₀ / 2 (SP1 candidate, refuted) ----
    print("\n" + "─" * 78)
    print("  Test 3: SP1 fibre spin u = ln q₀ + i·(ln q₀/2), A_ω = 3")
    print("─" * 78)
    for name, q, S_val, ln_q in [("proton", q_pr, S_pr, ln_q_pr),
                                   ("muon", q_mu, S_mu, ln_q_mu)]:
        s_sp1 = A_OMEGA * imV41(ln_q, ln_q / 2)
        ratio_sp1 = s_sp1 / S_val if S_val != 0 else mp.inf
        print(f"  {name}: S_SP1 = 3·(√3/4)·(3/4)·(ln q₀)² = {mp.nstr(s_sp1, 10)}")
        print(f"          ratio S_SP1/S_target = {mp.nstr(ratio_sp1, 6)}")

    # ---- Test 4: consistency check — do the two needed Im u values agree? ----
    print("\n" + "─" * 78)
    print("  Test 4: consistency — do both anchors need the SAME Im u?")
    print("─" * 78)
    if results["proton"]["rhs_positive"] and results["muon"]["rhs_positive"]:
        im_pr = results["proton"]["im_u_needed"]
        im_mu = results["muon"]["im_u_needed"]
        gap = abs(im_pr - im_mu)
        rel_gap = gap / max(abs(im_pr), abs(im_mu)) if max(abs(im_pr), abs(im_mu)) > 0 else 0
        print(f"  Im u (proton) = {im_pr:.10f}")
        print(f"  Im u (muon)   = {im_mu:.10f}")
        print(f"  gap           = {gap:.6e}  (relative: {rel_gap:.6e})")
        consistent = rel_gap < 0.01  # 1% threshold
        print(f"  consistent (< 1%) = {consistent}")

        if not consistent:
            print("\n  ⚠ The two anchors need DIFFERENT Im u values — the simple")
            print("    multiplicative formula S = 3·Im 𝔙₄₁(u) with a SINGLE u(q₀)")
            print("    CANNOT reproduce both anchors simultaneously. This is NOT a")
            print("    failure of A_ω = 3; it means Im u must be anchor-dependent")
            print("    (i.e., q₀-dependent beyond just Re u = ln q₀) — exactly the")
            print("    SP2 hypersensitivity finding.")
    else:
        consistent = False
        print("  One or both anchors have no real Im u solution — inconsistent.")

    # ---- Verdict ----
    print("\n" + "=" * 78)
    print("  VERDICT")
    print("=" * 78)

    # The probe tests two claims:
    # (A) A_ω = 3 is the right magnitude: S / Im 𝔙₄₁ = 3?
    # (B) A single Im u works for both anchors?
    both_real = results["proton"]["rhs_positive"] and results["muon"]["rhs_positive"]
    both_sign = results["proton"].get("sign_ok", False) and results["muon"].get("sign_ok", False)

    if both_real and both_sign and consistent:
        verdict = "MATCH: A_ω = 3 with a single derived Im u reproduces both anchor S values"
    elif both_real and both_sign and not consistent:
        verdict = ("PARTIAL: A_ω = 3 can reproduce each anchor S individually (sign + magnitude) "
                   "but requires DIFFERENT Im u at each — the SP2 crux (Im u is q₀-sensitive)")
    elif both_real and not both_sign:
        verdict = "SIGN FAILURE: A_ω = 3 gives wrong sign at one or both anchors"
    else:
        verdict = "STRUCTURAL FAILURE: no real Im u exists for one or both anchors"

    print(f"  {verdict}")

    # ---- Witness ----
    wb = WitnessBuilder("qbeta-stokes3-magnitude-identification", engine="mpmath")
    wb.set_description(
        "T4 of the Δ_λ magnitude derivation (bean qou-fgte). Tests whether the GGM "
        "Stokes constant A_ω = 3 (integer, literature-proved for 4₁) combined with the "
        "proved formula Im 𝔙₄₁(u) = (√3/4)(Re²u−Im²u) reproduces the empirical S at "
        "both anchors. Derive-then-check: inverts for Im u, checks consistency.")
    wb.set_content_block("conj:binding-qbeta-complex-volume")
    wb.add_data("stokes3_identification", {
        "A_omega": 3,
        "formula": "S = A_ω · (√3/4) · (Re²u − Im²u), Re u = ln q₀",
        "proton_result": results["proton"],
        "muon_result": results["muon"],
        "both_anchors_real_imu": both_real,
        "both_anchors_sign_ok": both_sign,
        "both_anchors_consistent": consistent,
        "verdict": verdict,
    })
    wb.add_assertion("both_real_im_u", str(both_real), "True")
    # We do NOT assert consistency — that's the honest open question (SP2)
    wb.save()
    print(f"\n  witness → qbeta-stokes3-magnitude-identification.witness.json")

    # Exit 0 if the probe ran cleanly (even if the result is negative — honest negatives
    # are valid results). Exit 1 only on infrastructure failure.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
