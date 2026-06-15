#!/usr/bin/env python3
"""Categorical bypass demo — compute B(𝔥) directly from SDP T_w, no knot id.

Implements **step 1** of the canonical-chain bypass plan: compute
binding energy directly from the joint-tower SDP solution via

    B(𝔥) = m_e · ρ · tr_M(T_w) | q = q_0
    tr_M(T_w) = Σ_λ y_λ(q_0) · χ_λ(T_w)

with the Wedderburn block traces χ_λ(T_w) read from the SDP witness
(joint-tower-sdp-rust.witness.json) and the Wenzl-bridge weights
y_λ(q_0) read from y-lambda-wenzl-witness.json. **No knot
identification, no volume-match.**

This is the bypass that moves family-1 atoms (D, T, ³He) from
"partial-knot-id-via-vol-match" to fully derived — IF the direct
formula reproduces the mass-table-ppb predictions. **It does not**,
and that surfaces a fundamental gap that must be resolved before
sub-percent (let alone 1 ppb) accuracy is achievable.

Findings:
- Electron H_2: tr_M(T_w(e)) = 0.7292 → B_pred = 0.373 MeV vs
  m_e = 0.511 MeV (27% off). The σ_1³ Hecke element in H_2(q)
  has Wedderburn-direct Markov trace ≠ 1.
- Deuteron H_3 (6_2): tr_M(T_w(²H)) = 0.288 → B_pred = 0.147 MeV
  vs AME 2.225 MeV (15× off). The volume-match identity
  tr_M(T_w(²H)) ≈ Vol_hyp(6_2) ≈ 4.401 does NOT hold for the
  Wenzl-y_λ × Wedderburn-χ_λ Markov trace evaluated at q_0.
- ³He H_3 (Borromean): tr_M(T_w(³He)) = 1.000 — interesting:
  exactly the identity-rep Markov trace, suggesting T_w(³He) is
  the categorical identity (which would mean B(³He) = m_e · ρ = 2·m_e
  = 1.022 MeV, far from AME 7.718 MeV).

Diagnosis: the canonical chain `tr_M = Σ y_λ χ_λ` and the
volume-match formula `B = m_e · ρ · Vol_hyp(K)` are NOT the same
function of T_w at q_0. The former is the **regular Markov trace**
on H_n(q); the latter is the **Reshetikhin–Turaev / colored Jones
invariant evaluated at the Volume Conjecture root of unity**. They
agree only at specific q values (roots of unity for Volume
Conjecture), not at the substrate parameter q_0 ≈ 1.110.

Implication: the bypass cannot simply replace volume-match with
Wenzl-Wedderburn at q_0. We need either:

  (A) Additional Markov-trace normalization factor to bridge the
      regular trace to the writhe-/framing-normalized closure.
  (B) Evaluate tr_M at a different q (root of unity), then
      analytically continue to q_0.
  (C) Reformulate the canonical chain to use a different categorical
      invariant (Reshetikhin–Turaev rather than Wenzl Markov).

Output: categorical-bypass-volmatch-demo.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from experimental_constants import M_E_MEV
from q_parameter import Q as Q_0
from witness_base import WitnessBuilder

SDP_WITNESS = Path(__file__).parent / "joint-tower-sdp-rust.witness.json"
Y_LAMBDA_WITNESS = Path(__file__).parent / "y-lambda-wenzl-witness.json"
MASS_TABLE_WITNESS = Path(__file__).parent / "mass-table-ppb.witness.json"


def load_y_lambda():
    """Return y_λ(q_0) keyed by (n, partition_tuple)."""
    with open(Y_LAMBDA_WITNESS) as f:
        d = json.load(f)
    out = {}
    for n_str, table in d["tables_by_n"].items():
        n = int(n_str)
        for w in table["weights"]:
            partition = tuple(w["partition"])
            out[(n, partition)] = float(w["y_lambda_numeric"])
    return out


def load_sdp_certificates():
    """Return SDP certificate per atom keyed by name."""
    with open(SDP_WITNESS) as f:
        d = json.load(f)
    return {e["name"]: e for e in d["per_atom_certificates"]}


def load_volmatch_predictions():
    """Pull mass-table-ppb predicted B values for comparison."""
    with open(MASS_TABLE_WITNESS) as f:
        d = json.load(f)
    out = {}
    for row in d["rows"]:
        out[row["sym"]] = {
            "B_AME_MeV": row["B_AME_MeV"],
            "B_pred_MeV": row["B_pred_MeV"],
            "formula": row["formula"],
        }
    return out


def chi_lambda_from_block(block):
    """χ_λ(T_w) = trace(ρ_λ(T_w)) = sum of (sym-part) eigenvalues.

    For non-symmetric matrices, the trace still equals the sum of
    eigenvalues by linearity. The witness records eigenvalues of the
    symmetric part (M+M^T)/2; their sum equals tr(M) regardless.
    """
    return sum(block["matrix_at_q_0_sym_eigvals"])


def native_strand_n(cert):
    """SDP runs at native_strand_count (knot-braid strands), not atomic n_0."""
    return cert["native_strand_count"]


def main():
    y_lambda = load_y_lambda()
    sdp_certs = load_sdp_certificates()
    volmatch = load_volmatch_predictions()

    rows = []
    sym_map = {
        "electron":     ("e", None,    None,   1.0,    "ref m_e"),
        "deuteron-2H":  ("2H", "²H",   "6_2",  None,   "vs mass-table-ppb"),
        "tritium-3H":   ("3H", "³H",   "8_11", None,   "vs mass-table-ppb"),
        "helium3-3He":  ("3He", "³He", "L6a4", None,   "vs mass-table-ppb"),
    }
    for sdp_name, (sym, sym_pretty, knot, ref_val, ref_label) in sym_map.items():
        cert = sdp_certs.get(sdp_name)
        if cert is None:
            continue
        n_native = native_strand_n(cert)
        rho = cert["rho_factor"]
        wb = cert.get("wedderburn_blocks", [])
        # Compute tr_M(T_w) = Σ_λ y_λ(q_0) · χ_λ(T_w)
        terms = []
        tr_M = 0.0
        for block in wb:
            partition = tuple(block["partition"])
            chi = chi_lambda_from_block(block)
            y = y_lambda.get((n_native, partition))
            if y is None:
                terms.append({"partition": list(partition), "chi": chi,
                              "y_lambda": None, "skipped": True})
                continue
            contribution = y * chi
            tr_M += contribution
            terms.append({
                "partition": list(partition),
                "d_lambda": block["d_lambda"],
                "chi_lambda": chi,
                "y_lambda": y,
                "contribution": contribution,
            })
        # B_pred from direct chain
        B_pred_direct = M_E_MEV * rho * tr_M
        # B_pred from volume-match (mass-table-ppb)
        vm = volmatch.get(sym, {})
        B_volmatch = vm.get("B_pred_MeV")
        B_AME = vm.get("B_AME_MeV", ref_val)

        rows.append({
            "sym":          sym,
            "sdp_name":     sdp_name,
            "knot":         knot,
            "n_native":     n_native,
            "rho":          rho,
            "tr_M_direct":  tr_M,
            "B_pred_direct_MeV": B_pred_direct,
            "B_volmatch_MeV": B_volmatch,
            "B_AME_MeV":    B_AME,
            "ratio_direct_to_volmatch": (
                B_pred_direct / B_volmatch if B_volmatch else None
            ),
            "ratio_direct_to_AME": (
                B_pred_direct / B_AME if B_AME else None
            ),
            "wedderburn_terms": terms,
            "comparison_label": ref_label,
        })

    print("\n" + "=" * 78)
    print("Bypass demo: B = m_e · ρ · Σ_λ y_λ · χ_λ(T_w) at q_0 — direct from SDP")
    print("=" * 78)
    print(f"{'sym':<6} {'n':>2} {'ρ':>2} {'tr_M':>9} "
          f"{'B_direct':>10} {'B_volmatch':>10} {'B_AME':>10} {'ratio':>7}")
    print("-" * 78)
    for r in rows:
        rd = r["ratio_direct_to_volmatch"]
        rd_str = f"{rd:>7.4f}" if rd is not None else f"{'—':>7}"
        bv = f"{r['B_volmatch_MeV']:>10.4f}" if r['B_volmatch_MeV'] is not None else f"{'—':>10}"
        ba = f"{r['B_AME_MeV']:>10.4f}" if r['B_AME_MeV'] is not None else f"{'—':>10}"
        print(f"{r['sym']:<6} {r['n_native']:>2} {r['rho']:>2} "
              f"{r['tr_M_direct']:>9.4f} {r['B_pred_direct_MeV']:>10.4f} "
              f"{bv} {ba} {rd_str}")

    print("\n" + "=" * 78)
    print("DIAGNOSIS: B_direct ≠ B_volmatch at q_0.")
    print("=" * 78)
    print("""
The Wenzl-y_λ × Wedderburn-χ_λ Markov trace evaluated at q_0 ≈ 1.110
does NOT reproduce the volume-match formula B = m_e · ρ · Vol_hyp(K).

Two distinct categorical invariants:
  - Wenzl Markov trace tr_M(T_w) = Σ_λ y_λ · χ_λ(T_w)  [REGULAR trace]
  - Vol_hyp(K) ≈ Reshetikhin–Turaev / colored-Jones invariant
    evaluated at q = root of unity (Volume Conjecture)

These agree only at Volume-Conjecture root-of-unity points, not at
the substrate parameter q_0. Resolving the bypass requires picking
ONE invariant as canonical and rederiving the other relations.

This is a real gap in the canonical chain (PR #442). Step 1 of the
1-ppb plan must include resolving it.
""")

    # Build witness via canonical infrastructure
    w = (
        WitnessBuilder("categorical-bypass-volmatch-demo", engine="python")
        .set_description(
            "Bypass demo: compute B(𝔥) directly from joint-tower SDP "
            "Wedderburn blocks via tr_M = Σ_λ y_λ · χ_λ at q_0, "
            "without using volume-match knot identification. "
            "Surfaces a 27%–15× discrepancy with mass-table-ppb's "
            "volume-match B = m_e · ρ · Vol_hyp(K), establishing that "
            "the regular Markov trace at q_0 ≠ Vol_hyp(K). The "
            "canonical chain in PR #442 step (5)–(7) needs further "
            "resolution before sub-percent accuracy is possible."
        )
        .set_content_block("prop:atom-knot-mass-derivation")
        .add_parameter("q_0", Q_0)
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_data("rows", rows)
        .add_data("sources", {
            "sdp_witness": str(SDP_WITNESS.name),
            "y_lambda_witness": str(Y_LAMBDA_WITNESS.name),
            "mass_table_witness": str(MASS_TABLE_WITNESS.name),
        })
        .add_caveat(
            "Direct formula tr_M = Σ y_λ · χ_λ at q_0 does NOT reproduce "
            "the volume-match B values; ratio is 0.73 for electron, "
            "~0.07 for deuteron, ~0.10 for ³He."
        )
        .add_caveat(
            "Resolving the bypass requires either (A) extra Markov-trace "
            "normalization, (B) evaluation at root of unity then "
            "analytic continuation, or (C) switching the canonical "
            "invariant from Wenzl-Markov to RT / colored-Jones."
        )
        .add_caveat(
            "Cannot reach 1 ppb on B/A or sub-MeV on Q until this gap "
            "is resolved."
        )
    )
    out_path = w.save()
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
