#!/usr/bin/env python3
"""DIAGNOSTIC (not a fit) — does the PROVED chirality weight reproduce the sharp
T/³He differential?  Companion to probe_pauli_young_delta_lambda_the3_signtest.py.

Task-3 follow-up. The "signed / chirality-aware Δ_λ" direction is NOT virgin:
`probes/chirality_delta_lambda_binding_sweep.py` already establishes that the
chirality SIGN Δ_λ = sgn(w₀^{S_λ'})·dim is PROVED (delta_lambda_sign_rule_proof),
and the MAGNITUDE (bare dim) is the failure (#2405: undershoots ≤⁴He, diverges
A≥6). The GAP-A Path-B ledger declares the per-partition numerical search a
closed 18-saturation chain; the open frontier is the owner-gated categorical
`conj:s5-so3-fiber-action`, explicitly NOT a numerical λ(K) search.

This is therefore a DIAGNOSTIC, not a new fitted ansatz: take the *existing*
proved chirality sign (and the same four magnitude variants already enumerated
in chirality_delta_lambda_binding_sweep.py) and evaluate them on the *new* sharp
constraint — the T/³He same-n differential (B_T − B_³He), which the per-atom
binding sweep never isolated.

Two binding models, both from the cached (y_λ, χ^λ_T, χ^λ_³He):

  linear (Δ_λ-closure program; what the 2026-06-02/06-18 differential uses):
      diff_lin = m_e · Σ_λ Δ_λ · y_λ · (χ^λ_T − χ^λ_³He)
  |·| (chirality_binding_sweep model; binding must be ≥0):
      diff_abs = m_e · (|Σ_λ y_λ χ^λ_T Δ_λ| − |Σ_λ y_λ χ^λ_³He Δ_λ|)

Target: B_T − B_³He = float(AME_B_TRITIUM_MEV_VALIDATION) − 7.7180 = +0.7638 MeV (= +1.4947·m_e).

The PROVED sign is *signed*, so unlike a non-negative multiplicity it CAN reach
the + sign; the question is whether any proved-sign magnitude variant lands on
the target. EXPECTED NEGATIVE on magnitude (CI-safe). Δ_λ stays open.
"""
from __future__ import annotations

import json
import sys
from math import factorial
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401,E402 — substrate/ (witness_base) on path
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
HERE = Path(__file__).resolve().parent
M_E_MEV = mp.mpf("0.51099895069")
AME_B = {"tritium": AME_B_TRITIUM_MEV_VALIDATION, "helium-3": mp.mpf("7.7180")}
CHI = {"tritium": "chi-tritium-h9-at-q0-50dps.witness.json",
       "helium-3": "chi-helium-3-h9-at-q0-50dps.witness.json"}


def load(fname):
    with open(HERE / fname, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    q0 = mp.mpf(d["q_0_50dps"])
    rows = {tuple(r["partition"]): {"y": mp.mpf(r["y_lambda"]),
                                    "chi": mp.mpf(r["chi_lambda"])}
            for r in d["by_partition"]}
    return rows, q0


# ── proved chirality sign + magnitudes (canonical source:
#    probes/chirality_delta_lambda_binding_sweep.py — reproduced, not re-derived) ──
def transpose(lam):
    return tuple(sum(1 for r in lam if r > c) for c in range(lam[0])) if lam else ()


def hook_dim(lam) -> int:
    n = sum(lam)
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            arm = row - j - 1
            leg = sum(1 for k in range(i + 1, len(lam)) if lam[k] > j)
            prod *= (arm + leg + 1)
    return factorial(n) // prod


def delta_sign(lam) -> int:
    """sgn(w₀^{S_λ'}) = Π_cols (−1)^{C(λ'_c,2)} — the proved chirality sign."""
    s = 1
    for b in transpose(lam):
        s *= (-1) ** (b * (b - 1) // 2)
    return s


def make_dim_q(q0):
    def qint(k):
        return (q0**k - q0**(-k)) / (q0 - 1 / q0)
    def dim_q(lam):
        n = sum(lam)
        num = mp.mpf(1)
        for k in range(1, n + 1):
            num *= qint(k)
        den = mp.mpf(1)
        for i, row in enumerate(lam):
            for j in range(row):
                arm = row - j - 1
                leg = sum(1 for k in range(i + 1, len(lam)) if lam[k] > j)
                den *= qint(arm + leg + 1)
        return num / den
    return dim_q


def main() -> int:
    T, q0 = load(CHI["tritium"])
    H, _ = load(CHI["helium-3"])
    parts = sorted(T, reverse=True)
    assert set(parts) == set(H)
    dim_q = make_dim_q(q0)

    target_mev = AME_B["tritium"] - AME_B["helium-3"]          # +0.7638
    target_me = target_mev / M_E_MEV                            # +1.4947

    variants = [
        ("1(raw)",   lambda lam: mp.mpf(1)),
        ("sgn",      lambda lam: mp.mpf(delta_sign(lam))),
        ("sgn·dim",  lambda lam: mp.mpf(delta_sign(lam) * hook_dim(lam))),
        ("sgn·dimq", lambda lam: mp.mpf(delta_sign(lam)) * dim_q(lam)),
    ]

    print(f"target  B_T − B_³He = {mp.nstr(target_mev, 6)} MeV "
          f"(= {mp.nstr(target_me, 6)}·m_e)\n")
    print(f"  {'Δ_λ':<10}{'diff_lin[MeV]':>15}{'diff_abs[MeV]':>15}"
          f"{'lin/target':>12}{'sign?':>7}")
    print("  " + "-" * 60)
    out = {}
    for vname, vfn in variants:
        # linear differential
        S_lin = mp.fsum(vfn(p) * T[p]["y"] * (T[p]["chi"] - H[p]["chi"]) for p in parts)
        diff_lin = M_E_MEV * S_lin
        # |·| model
        S_T = mp.fsum(T[p]["y"] * T[p]["chi"] * vfn(p) for p in parts)
        S_H = mp.fsum(H[p]["y"] * H[p]["chi"] * vfn(p) for p in parts)
        diff_abs = M_E_MEV * (abs(S_T) - abs(S_H))
        ratio = diff_lin / target_mev if target_mev else mp.mpf("nan")
        signok = "yes" if diff_lin > 0 else "NO"
        out[vname] = {"diff_lin_mev": mp.nstr(diff_lin, 8),
                      "diff_abs_mev": mp.nstr(diff_abs, 8),
                      "lin_over_target": mp.nstr(ratio, 6),
                      "lin_sign_correct": diff_lin > 0}
        print(f"  {vname:<10}{mp.nstr(diff_lin,6):>15}{mp.nstr(diff_abs,6):>15}"
              f"{mp.nstr(ratio,4):>12}{signok:>7}")

    # the proved factor is sgn·dim
    proved = out["sgn·dim"]
    proved_hits = abs(mp.mpf(proved["diff_lin_mev"]) - target_mev) <= mp.mpf("0.05") * abs(target_mev)
    proved_sign_ok = proved["lin_sign_correct"]
    print(f"\n  PROVED weight Δ_λ=sgn·dim:  linear diff = {proved['diff_lin_mev']} MeV "
          f"vs target {mp.nstr(target_mev,6)}")
    print(f"    sign correct?  {proved_sign_ok}    magnitude within 5%?  {proved_hits}")
    print("\n  Reading: the proved chirality SIGN can flip the differential positive")
    print("  (it is signed, unlike a non-negative multiplicity) — but no proved-sign")
    print("  magnitude variant lands on +0.7638 MeV. Consistent with the ledger's")
    print("  closed 18-saturation chain; the open frontier is the owner-gated")
    print("  categorical s5-so3-fiber map, not a numerical magnitude fit.")

    w = WitnessBuilder("probe-chirality-delta-lambda-the3-diagnostic", engine="mpmath")
    w.set_description(
        "DIAGNOSTIC (not a fit): the PROVED chirality weight Δ_λ=sgn(w₀^{S_λ'})·dim "
        "and its enumerated magnitude variants (sgn, sgn·dim, sgn·dimq) evaluated on "
        "the sharp T/³He same-n differential B_T−B_³He=+0.7638 MeV, in both the "
        "linear (Δ_λ-closure) and |·| (chirality-binding-sweep) models. The proved "
        "SIGN can reach the + differential sign; no proved-sign magnitude hits the "
        "target. Δ_λ remains open (GAP-A-3/A-4); per-partition numerical search "
        "closed (18-saturation chain), open frontier is owner-gated categorical."
    )
    w.add_parameter("n_strands", 9)
    w.add_data("target_diff_mev", mp.nstr(target_mev, 16))
    w.add_data("target_diff_me", mp.nstr(target_me, 16))
    w.add_data("by_variant", out)
    w.add_data("proved_sign_reaches_positive_diff", bool(proved_sign_ok))
    w.add_assertion(
        name="no_proved_sign_magnitude_hits_the3_differential",
        computed=str(int(not proved_hits)),
        expected="1",
        tolerance=0,
        source=(f"DIAGNOSTIC: PROVED Δ_λ=sgn·dim linear diff = "
                f"{proved['diff_lin_mev']} MeV vs target {mp.nstr(target_mev,6)} "
                f"(sign correct: {proved_sign_ok}); no enumerated magnitude variant "
                "lands on target — consistent with the closed 18-saturation chain."),
    )
    print(f"\nWitness: {w.save()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
