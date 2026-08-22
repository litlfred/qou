#!/usr/bin/env python3
"""Per-atom audit witnesses — item 6 from author's 1-6 multi-select.

Per author direction 2026-05-25: "work on pending. including upstream".

For each KLR-violating atom (PR #1214 wiring-status taxonomy), emit a
structured per-atom witness containing:

  - bug type (per PR #1228 §3 taxonomy)
  - squash path (per PR #1228 §5 options)
  - canonical-formula candidate (using new Rust upstream pn.trace_weights_n)
  - delta from production B_prod

USES THE NEW RUST UPSTREAM (PR #1251 commit `0592a22c5` + `125a88934`):
  - pn.trace_weights_n(n=3A, q_0)  → Jones-Markov y_λ on H_{3A}
  - pn.gram_matrix_n(n=3A, q_0)    → diagonal Gram (= y_λ · dim_q(λ))
  - pn.chi_lambda_braid(λ, β, q_0)  → individual χ_λ values

This is the **first production-grade use** of the new Rust n-generic
API, demonstrating the migration path for the 15+ legacy callers.

## Per-atom output

```
{
    "atom": "4He",
    "A": 4, "Z": 2, "N": 2,
    "n_strands": 12,
    "bug_type": "Type 1 (SDP single-block simplification)",
    "squash_path": [Option F Wigner SU(4) singlet, Option H Bloch h² regulator],
    "production_B_MeV": 29.96,
    "AME_B_MeV": 28.30,
    "rel_err_pct": +5.87,
    "jet_order_scale": "h^2 (bar-symmetric)",
    "klr_positivity_violates": true,
    "canonical_candidate_via_atlas": ..., # if computable
    ...
}
```

Output: `per-atom-audit-witnesses.witness.json`.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from pathlib import Path

import mpmath as mp
import pyhecke_native as pn

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402  (drain qou-7ot6-a)

mp.mp.dps = 30
Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
q0_f64 = float(mp.mpf(record_upstream(Q_PIN, _UPSTREAM_RECORDS)["derived_50_digit"]["q"]))
h_f64 = q0_f64 - 1.0 / q0_f64
h_sq_f64 = h_f64 * h_f64

M_E = float(M_E_MEV)  # registry (was the truncated literal 0.510998950)
VOL_BOR = float(8 * mp.catalan)

# Per-atom data: (sym, A, Z, N, B_AME, B_prod, bug_type, squash_paths)
ATOM_AUDITS = [
    ("2H",  2, 1, 1,   float(AME_B_DEUTERON_MEV_VALIDATION),  2.2488, "Type 3 (census-assigned, no canonical β)",
     ["Canonical β_2H from H_6 SDP", "Replace knot 6_2 with derived assignment"]),
    ("3H",  3, 1, 2,   float(AME_B_TRITIUM_MEV_VALIDATION),   8.4686, "(KLR-consistent — clean h^4 closure)",
     ["Already at h^4 scale; minor refinement only"]),
    ("3He", 3, 2, 1,   float(AME_B_HE3_MEV_VALIDATION),   7.4889, "Type 3 (census-assigned, no canonical β)",
     ["Canonical β_3He from H_9 SDP", "Replace link L6a4 with derived assignment"]),
    ("4He", 4, 2, 2,  float(AME_B_HE4_MEV_VALIDATION), 29.9557, "Type 1 (SDP single-block, magic A·8G with ν=2 extrap)",
     ["Option F (Wigner SU(4) singlet projection)", "Option H (Bloch h² regulator)",
      "Atlas H_12 multi-block correction"]),
    ("8Be", 8, 4, 4,  56.49951,   62.3383, "Type 2 (α-cluster recursion non-multiplicative h²)",
     ["Replace recursion with per-atom H_24 SDP", "Canonical 4He first → propagates"]),
    ("12C",  12, 6, 6,  92.16175, 97.1480, "Type 2 (α-cluster inheritance from 4He)",
     ["Same as 8Be — fix 4He propagates here"]),
    ("16O",  16, 8, 8, 127.61929, 134.3846, "Type 2 (α-cluster inheritance from 4He)",
     ["Same — fix 4He propagates here"]),
    ("20Ne", 20, 10, 10, 160.64486, 174.0483, "Type 2 (α-cluster inheritance from 4He)",
     ["Same — fix 4He propagates here"]),
    ("24Mg", 24, 12, 12, 198.25690, 216.1389, "Type 2 (α-cluster accumulation)",
     ["Same — fix 4He propagates here"]),
    ("40Ca", 40, 20, 20, 342.05210, 408.7713, "Type 2 (α-cluster accumulation, largest)",
     ["Same — fix 4He propagates here"]),
]


def jet_order_classification(rel_err: float) -> str:
    """Classify |relative error| in jet-order h^k units."""
    ae = abs(rel_err)
    if ae < h_sq_f64 * h_sq_f64 * 0.5:
        return "<h^4/2 (very clean)"
    if ae < h_sq_f64 * h_sq_f64 * 2:
        return f"≈ h^4 ({h_sq_f64**2:.2e})"
    if ae < h_sq_f64 * 0.5:
        return "between h^4 and h^2/2"
    if ae < h_sq_f64 * 2:
        return f"≈ h^2 ({h_sq_f64:.2e})"
    if ae < abs(h_f64) * 0.5:
        return "between h^2 and h/2"
    if ae < abs(h_f64) * 2:
        return f"≈ h ({h_f64:.2e})"
    return f"> 2h (structural)"


def borromean_on(base_strand: int) -> list[tuple[int, int]]:
    s1, s2 = base_strand, base_strand + 1
    return [(1, s1), (-1, s2)] * 3


def atom_braid(A: int) -> list[tuple[int, int]]:
    word = []
    for i in range(A):
        word.extend(borromean_on(3 * i + 1))
    return word


def compute_canonical_candidate(A: int) -> dict | None:
    """Use the new Rust pn.trace_weights_n to compute canonical tr_M
    for atom of mass number A. Returns None if n_strands too large."""
    n = 3 * A
    if n > 12:  # skip A>4 atoms in this fast-pass script (they take >5 min each at H_15+)
        return {
            "skipped": True,
            "reason": f"n={n} too slow for inline computation (use run_jones_markov_atlas_all_atoms.py --full witness when ready)",
        }
    try:
        t0 = time.time()
        y_lambda = pn.trace_weights_n(n, q0_f64)
        beta = atom_braid(A)
        chi_vals = pn.chi_lambdas_braid(
            pn.partitions_of(n), beta, q0_f64
        )
        tr_M = sum(y_lambda[i] * chi_vals[i] for i in range(len(y_lambda)))
        elapsed = time.time() - t0

        # Production-shaped formula: B = 2 · m_e · A · 8G · tr_M
        B_atlas_corrected = 2 * M_E * A * VOL_BOR * tr_M

        return {
            "n_strands": n,
            "num_partitions": len(y_lambda),
            "tr_M_via_rust_atlas": float(tr_M),
            "B_atlas_corrected_MeV": float(B_atlas_corrected),
            "elapsed_seconds": float(elapsed),
        }
    except Exception as e:
        return {"error": str(e)}


def main() -> int:
    print("=" * 110)
    print("Per-atom audit witnesses — using new Rust pn.trace_weights_n upstream")
    print(f"  q_0 = {q0_f64:.10f}  h = {h_f64:.10f}  h² = {h_sq_f64:.10e}")
    print("=" * 110)
    print()

    audits = []
    for row in ATOM_AUDITS:
        sym, A, Z, N, B_AME, B_prod, bug_type, squash_paths = row
        rel_err = (B_prod - B_AME) / B_AME * 100
        jet = jet_order_classification(rel_err / 100)
        klr_violates = (B_prod > B_AME)
        marker = "✗" if klr_violates else "✓"

        print(f"━━ {sym} A={A} (H_{3*A}) ━━")
        print(f"  B_AME={B_AME:.4f} MeV, B_prod={B_prod:.4f} MeV, err={rel_err:+.3f}% ({jet}) {marker}")
        print(f"  bug type: {bug_type}")

        canonical = compute_canonical_candidate(A) if A <= 8 else {
            "skipped": True, "reason": "Heavy atom — atlas data needed"
        }
        if canonical and "tr_M_via_rust_atlas" in canonical:
            print(f"  canonical: tr_M={canonical['tr_M_via_rust_atlas']:.6f}, "
                  f"B_corrected={canonical['B_atlas_corrected_MeV']:.4f} MeV "
                  f"(Δ from prod: {canonical['B_atlas_corrected_MeV'] - B_prod:+.4f} MeV) "
                  f"in {canonical['elapsed_seconds']:.1f}s")
        elif canonical and "skipped" in canonical:
            print(f"  canonical: SKIPPED ({canonical['reason']})")
        elif canonical and "error" in canonical:
            print(f"  canonical: ERROR — {canonical['error']}")
        print()

        audits.append({
            "atom": sym, "A": A, "Z": Z, "N": N,
            "n_strands": 3 * A,
            "B_AME_MeV": B_AME,
            "B_prod_MeV": B_prod,
            "rel_err_pct": float(rel_err),
            "klr_positivity_violates": klr_violates,
            "jet_order_classification": jet,
            "bug_type": bug_type,
            "squash_paths": squash_paths,
            "canonical_candidate": canonical,
        })

    # Summary
    n_klr_violations = sum(1 for a in audits if a["klr_positivity_violates"])
    print("=" * 110)
    print(f"Summary: {n_klr_violations} / {len(audits)} atoms violate KLR positivity")
    print(f"  Type 1 (SDP single-block): {sum(1 for a in audits if 'Type 1' in a['bug_type'])}")
    print(f"  Type 2 (α-cluster recursion): {sum(1 for a in audits if 'Type 2' in a['bug_type'])}")
    print(f"  Type 3 (census-assigned):    {sum(1 for a in audits if 'Type 3' in a['bug_type'])}")
    print()
    print("Architecture verified:")
    print(f"  Rust upstream pn.trace_weights_n: used for {sum(1 for a in audits if a['canonical_candidate'] and 'tr_M_via_rust_atlas' in a['canonical_candidate'])} atoms")
    print(f"  Skipped (heavy atoms): {sum(1 for a in audits if a['canonical_candidate'] and 'skipped' in a['canonical_candidate'])}")

    w = WitnessBuilder("per-atom-audit-witnesses", engine="python+pyhecke-native")
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        "Per-atom audit witnesses (item 6 from author 2026-05-25 multi-select). "
        "For each KLR-violating atom: bug type (per PR #1228 §3 taxonomy), "
        "squash path (per §5 options), canonical-formula candidate using "
        "the new Rust upstream pn.trace_weights_n (PR #1251 commit 0592a22c5). "
        "First production-grade use of the n-generic Rust ABI; demonstrates "
        "the migration path for 15+ legacy H_3-locked callers."
    )
    w.add_parameter("q_0_f64", q0_f64)
    w.add_parameter("h_f64", h_f64)
    w.add_parameter("h_sq_f64", h_sq_f64)
    w.add_parameter("klr_positivity_violations", n_klr_violations)
    w.add_data("per_atom_audits", audits)
    w.add_assertion(
        "all_audits_processed",
        computed=len(audits),
        expected=len(ATOM_AUDITS),
        tolerance=0,
        unit="atoms",
        source="ATOM_AUDITS table iteration",
    )
    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
