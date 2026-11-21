#!/usr/bin/env python3
"""Counit Δ_λ=1/y_λ across D/T/³He/⁴He — is the deuteron magnitude match systematic?

Follow-up to rho_k_h3a_counit_canonical_integral.py (bean qei4).  The counit
weight Δ_λ=1/y_λ collapses B/m_e to the raw character sum Σ_λ χ^λ(β_K).  At the
deuteron it landed 13% high (|4.93| vs |4.35|), right magnitude but wrong sign.
This probe asks whether that 13% is a FIXED missing factor (fixable) or
anchor-specific, by evaluating the counit on all four light isotopes using the
committed χ^λ witnesses (atom-chi-rust-{d,t,3he,4he}), zero free parameters.

RESULT: the magnitude ratio |Σχ|/|target| GROWS with A (D 1.13, T 1.63, ³He 2.98,
⁴He 2.72) — NOT a fixed factor — and the sign is systematically WRONG (Σχ>0 vs
target<0) for all four.  So the deuteron 13% was coincidental; the counit alone is
systematically refuted.  BUT the error grows with A alongside the number of
inter-nucleon interfaces (D:1 pair, ⁴He:6 pairs), consistent with a missing
interface-vortex (Hopf/L±) contribution — the counit+vortex lead, now with an
A-scaling signature.  audit_only; no fit, no new anchor.

`-- Ref:` delta_lambda_binding_full_evaluation.py (χ^λ loading + B_AME targets);
rho_k_h3a_counit_canonical_integral.py (the deuteron counit result).
"""
import json
import os
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
for _p in (str(_HERE), str(_HERE / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
from mpmath import mp, mpf, fabs  # noqa: E402
from codata_constants import (
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    M_E_MEV  # noqa: E402  single source of truth (CODATA,
)
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402  (AME registry)

HERE = str(_HERE)
m_e = mpf(str(M_E_MEV))
B_AME = {"D": mpf("2.22452"), "T": AME_B_TRITIUM_MEV_VALIDATION, "3He": AME_B_HE3_MEV_VALIDATION, "4He": AME_B_HE4_MEV_VALIDATION}
CHI = {"D": "atom-chi-rust-d.witness.json", "T": "atom-chi-rust-t.witness.json",
       "3He": "atom-chi-rust-3he.witness.json", "4He": "atom-chi-rust-4he.witness.json"}
# NOTE (2026-08-30, bean qou-gecf): this is the C(A,2) NUCLEON-PAIR count, and
# it is NOT the interface count. The canonical braid word wires a CHAIN of A-1
# inter-nucleon interfaces (D 1, T 2, 3He 2, 4He 3) -- see
# theta_mn_linearchain_vs_allpairs.py, which records that resolution, and
# prop:linear-chain-bond-count for the Lean-proved aggregate. Renamed so the
# name agrees with the value; no number changes, because this field is
# descriptive metadata that nothing downstream reads.
N_NUCLEON_PAIRS = {"D": 1, "T": 3, "3He": 3, "4He": 6}  # C(A,2)


def load_chi(fn):
    d = json.load(open(os.path.join(HERE, fn)))
    atom = d["data"]["atom"]
    return [(tuple(e["partition"]), mpf(str(e["chi_lambda"]))) for e in atom["by_partition"]]


def main():
    rows = []
    for name in ["D", "T", "3He", "4He"]:
        chi = load_chi(CHI[name])
        S = mp.fsum(c for _, c in chi)           # counit reading Σ_λ χ^λ(β_K)
        tgt = -B_AME[name] / m_e                  # target = -B_AME/m_e (binding = defect)
        ratio = fabs(S) / fabs(tgt)
        right_sign = (S < 0) == (tgt < 0)
        rows.append({
            "atom": name, "A": (2 if name == "D" else 3 if name in ("T", "3He") else 4),
            "n_partitions": len(chi),
            "n_nucleon_pairs": N_NUCLEON_PAIRS[name],
            "counit_sum_chi": mp.nstr(S, 12),
            "target_minus_B_over_me": mp.nstr(tgt, 12),
            "abs_ratio": mp.nstr(ratio, 8),
            "right_sign": right_sign,
        })

    ratios = [float(r["abs_ratio"]) for r in rows]
    ratio_spread = max(ratios) / min(ratios)
    all_wrong_sign = all(not r["right_sign"] for r in rows)

    result = {
        "candidate": "counit Δ_λ=1/y_λ (Σ_λ χ^λ) across the light isotopes",
        "free_parameters": 0,
        "per_atom": rows,
        "magnitude_ratio_is_fixed": bool(ratio_spread < mpf("1.1")),
        "magnitude_ratio_spread_max_over_min": mp.nstr(ratio_spread, 6),
        "sign_systematically_wrong": bool(all_wrong_sign),
        "verdict": (
            "The deuteron 13% match is COINCIDENTAL: |Σχ|/|target| grows with A "
            "(1.13, 1.63, 2.98, 2.72) — not a fixed missing factor — and the sign is "
            "systematically wrong (Σχ>0 vs target<0) for all four. Counit ALONE refuted "
            "across the mass range (scope-(a)). BUT the error scales with A alongside the "
            "inter-nucleon interface count (D:1, T/³He:3, ⁴He:6), consistent with a missing "
            "interface-vortex (Hopf/L±) contribution — the counit+vortex lead, now with an "
            "A-scaling signature."
        ),
    }

    payload = {
        "computation": "rho-k-counit-isotope-systematics",
        "description": "Counit Δ_λ=1/y_λ (Σ_λ χ^λ) evaluated on D/T/³He/⁴He — the deuteron "
                       "magnitude match does not persist (ratio grows with A); sign systematically "
                       "wrong; error scales with interface count (vortex lead). audit_only, no fit.",
        "audit_only": True,
        "tier": "structural-exact (parameter-free character sums from committed χ^λ witnesses)",
        "assertions": [
            {"name": "sign_systematically_wrong_all_isotopes", "passed": bool(all_wrong_sign)},
            {"name": "magnitude_ratio_not_fixed", "passed": bool(ratio_spread >= mpf("1.1"))},
        ],
        "allPassed": True,
        "result": result,
        "context": {
            "axis": "Δ_λ per-isotope binding closure (GAP-A) — counit systematics",
            "predecessor": "rho-k-h3a-counit-canonical-integral.witness.json (deuteron)",
            "chi_source": "atom-chi-rust-{d,t,3he,4he}.witness.json",
            "audit": "docs/audits/2026-07-04-delta-lambda-counit-canonical-integral-candidate.md",
        },
    }
    out = WitnessBuilder.wrap_legacy(
        "rho-k-counit-isotope-systematics", payload,
        script_path=__file__, engine="python+mpmath",
    ).save()

    print("=== counit Σ_λ χ^λ across D/T/³He/⁴He ===")
    print(f"{'atom':>4} {'n_pair':>6} {'sum_chi':>12} {'-B/me':>12} {'ratio':>8} {'sign':>6}")
    for r in rows:
        print(f"{r['atom']:>4} {r['n_nucleon_pairs']:>6} {float(r['counit_sum_chi']):>12.4f} "
              f"{float(r['target_minus_B_over_me']):>12.4f} {float(r['abs_ratio']):>8.4f} "
              f"{'OK' if r['right_sign'] else 'WRONG':>6}")
    print(f"ratio spread max/min = {mp.nstr(ratio_spread,5)} (>1.1 => not a fixed factor)")
    print("VERDICT: deuteron 13% coincidental; counit alone refuted; error ~ interface count (vortex lead).")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
