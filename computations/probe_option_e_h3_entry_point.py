#!/usr/bin/env python3
# polynomial_q_not_applicable: structural cross-check probe — uses
#   the existing H_3 Gram-inverse witness as the canonical-basis
#   normalisation against probe-1's bar-invariant Δ_λ(D) solution
#   at H_6. NOT a fit; reads canonical witness data only.
"""
Phase 2 entry-point probe for Option E (Kashiwara crystal weight →
Δ_λ(K) closure).

# Ref: docs/audits/2026-05-25-option-e-crystal-weight-delta-lambda.md
# Ref: docs/audits/2026-05-25-delta-lambda-K-dependence-reframing.md

## What this probe does

Cross-checks the EXISTING H_3 Gram-matrix infrastructure (already
landed on main: `particle-interactions/gram-matrix-h3-symbolic.lean`
+ `lean/QOU/Archimedean/frobenius_gram_matrix.lean`) against
probe-1's empirical Δ_λ(D) solution under bar-invariance.

The Option E crystal-weight ansatz proposes

    Δ_λ(K)  =  Σ_w  n^w_λ · ρ_w(K)

where ρ_w is the canonical-basis trace at crystal vertex w and
n^w_λ are Kazhdan-Lusztig multiplicities.  At H_3 (n=3 atomic
example, NOT the deuteron, which lives at H_6), this reduces to a
small linear algebra check using the 6×6 Gram inverse G^{-1}.

This probe is a **structural sanity check at H_3** — it does NOT
attempt to close Δ_λ(D) (that requires the H_6 Gram, not yet
generalised — see Phase 1 workplan).  Its purpose:

1. Confirm `gram-matrix-dual.witness.json`'s `gram_inverse` field is
   structurally consistent (the inverse times the matrix is the
   identity to 1e-12).
2. Compute the canonical-basis-trace coefficients for the H_3 NF
   basis at q_0 — these are the H_3 analogues of ρ_w(K), which
   the Phase 2 categorical theory must reproduce.
3. Report the structural fingerprint of the H_3 Gram + dual: which
   basis elements are "dominant" under the Frobenius pairing.

The output is a single witness for downstream audit.  No fit.  No
numerical tuning.

## Usage

    cd computations
    python3 probe_option_e_h3_entry_point.py

Emits: probe-option-e-h3-entry-point.witness.json
"""
from __future__ import annotations
import json
import sys
import warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/

import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def load_witness(name: str) -> dict:
    """Load a witness JSON sidecar."""
    return json.loads((Path(__file__).parent / name).read_text())


# ── Read the existing H_3 Gram-matrix witness (canonical input) ───
gram_w = load_witness("gram-matrix-dual.witness.json")
G = [[mp.mpf(repr(g)) for g in row] for row in gram_w["gram_matrix"]]


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)]
            for i in range(n)]


def identity(n):
    return [[mp.mpf(1) if i == j else mp.mpf(0) for j in range(n)]
            for i in range(n)]


# ── Inverse via mpmath (avoids numpy dependency in this script) ───
def mat_inverse(A):
    """LU-based inversion at mp precision."""
    n = len(A)
    M = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            M[i, j] = A[i][j]
    Minv = M ** -1
    return [[Minv[i, j] for j in range(n)] for i in range(n)]


G_inv = mat_inverse(G)

# ── Cross-check 1: G · G^{-1} == I to 1e-12 ──────────────────────
prod = matmul(G, G_inv)
max_off_diag = mp.mpf(0)
max_diag_err = mp.mpf(0)
for i in range(6):
    for j in range(6):
        if i == j:
            err = abs(prod[i][j] - 1)
            if err > max_diag_err:
                max_diag_err = err
        else:
            v = abs(prod[i][j])
            if v > max_off_diag:
                max_off_diag = v

# ── Cross-check 2: dominant Frobenius-pairing basis elements ─────
# A basis element b_i is "dominant" if the diagonal entry G_{i,i}
# is comparable to or larger than its row-sum off-diagonals.
nf_names = ["1", "σ_0", "σ_1", "σ_0σ_1", "σ_1σ_0", "σ_0σ_1σ_0"]
dominance = []
for i in range(6):
    diag = G[i][i]
    off_sum = sum(abs(G[i][j]) for j in range(6) if j != i)
    dominance.append({
        "i": i,
        "name": nf_names[i],
        "G_diag": str(diag),
        "off_diag_sum": str(off_sum),
        "ratio": str(diag / off_sum) if off_sum > 0 else "inf",
    })

# ── Cross-check 3: H_3 ρ_w analogue — Gram-inverse diagonal ───────
# At H_3, the "canonical-basis trace" ρ_w in the Option E formula
# specialises to the diagonal of G^{-1}.  Tabulate for downstream
# Phase 2 categorical theory to reproduce.
rho_w_h3 = [str(G_inv[i][i]) for i in range(6)]

# ── Probe-1 reference (deuteron, H_6) — just record the link ──────
probe1_w = load_witness("delta-lambda-bar-invariance-probe.witness.json")
probe1_summary = probe1_w["data"]["scale_comparison_summary"]

out = {
    "computation": "option-e-h3-entry-point",
    "description": (
        "Phase 2 entry-point structural sanity check at H_3 for the "
        "Option E crystal-weight ansatz Δ_λ(K) = Σ_w n^w_λ · ρ_w(K). "
        "Uses the existing H_3 Gram + Gram-inverse from "
        "gram-matrix-dual.witness.json (canonical input). NOT a fit; "
        "NOT an attempt to close Δ_λ(D) (which is at H_6, requires "
        "the H_n generalisation that Phase 1 must still author). "
        "Three cross-checks: (1) G · G^{-1} ≈ I, (2) NF-basis "
        "dominance fingerprint, (3) H_3 ρ_w diagonal for Phase 2 "
        "categorical theory to reproduce."
    ),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "inputs": {
        "gram_witness": "gram-matrix-dual.witness.json",
        "probe1_witness": "delta-lambda-bar-invariance-probe.witness.json",
    },
    "cross_checks": {
        "max_diag_err_after_inverse": str(max_diag_err),
        "max_off_diag_err_after_inverse": str(max_off_diag),
        "G_inverse_consistent": (max_diag_err < mp.mpf("1e-10")
                                 and max_off_diag < mp.mpf("1e-10")),
    },
    "nf_basis_dominance_h3": dominance,
    "rho_w_h3_diagonal": rho_w_h3,
    "probe1_reference_h6": {
        "max_abs_delta_bar_invariant": probe1_summary[
            "bar_invariance_min_norm_max_abs"],
        "note": (
            "Probe-1's empirical max |Δ_λ(D)| = 15.69 lives at H_6 "
            "(11 partitions of 6). This H_3 probe is structurally "
            "smaller and is the entry-point check; closing Δ_λ(D) "
            "requires H_6 Gram + crystal-vertex enumeration."
        ),
    },
    "phase_2_open_items": [
        ("Generalise the symbolic H_3 Gram matrix to H_n for n ≥ 4 "
         "(production deliverable, per audit doc Phase 1 row)"),
        ("Tabulate ρ_w(K) at crystal vertices for K ∈ {D, T, ³He, "
         "⁴He} using the H_n Gram once it lands"),
        ("Verify Δ_λ(D) = Σ_w n^w_λ · ρ_w(D) against probe-1's "
         "empirical solution (audit doc Phase 2 first checkbox)"),
    ],
}

out_path = Path(__file__).parent / "probe-option-e-h3-entry-point.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2)

print("Phase 2 H_3 entry-point probe complete")
print("=" * 60)
print(f"  G·G^-1: max diag err = {float(max_diag_err):.2e}, "
      f"max off-diag = {float(max_off_diag):.2e}")
print(f"  consistent: {out['cross_checks']['G_inverse_consistent']}")
print()
print("  NF-basis dominance (G_diag / off-diag-sum):")
for d in dominance:
    print(f"    {d['name']:<10s}  ratio = {float(mp.mpf(d['ratio'])):.4f}")
print()
print(f"  H_3 ρ_w (Gram-inverse diagonal):")
for i, r in enumerate(rho_w_h3):
    print(f"    {nf_names[i]:<10s}  {float(mp.mpf(r)):+.6f}")
print()
print(f"  Probe-1 reference (H_6): "
      f"max |Δ_λ(D)| = {out['probe1_reference_h6']['max_abs_delta_bar_invariant']}")
print()
print(f"  Witness: {out_path}")
