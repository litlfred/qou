#!/usr/bin/env python3
"""
Compute tr_M(T_w, q_0) via the Hoefsmit + Wenzl-bridge path,
sidestepping sympy's H_9 cost wall.

Method (per prop:atom-knot-mass-derivation, master prop):

    tr_M(T_w) = Σ_{λ ⊢ n} y_λ(q) · χ_λ(T_w)
              = Σ_{λ ⊢ n} y_λ(q) · Tr(ρ_λ(T_w))

where:
  - ρ_λ(T_w) is the Hoefsmit seminormal-form matrix of T_w in the
    Wedderburn block λ. Built by `tools/hecke-engine/src/bin/
    dump_block_matrices.rs` for any atom in its registry.
  - y_λ(q) are the Wenzl-bridge weights from
    `y-lambda-mpfr-witness.json` (precomputed at 50 dps for n ≤ 11).
  - Tr(ρ_λ(T_w)) is the matrix trace (sum of diagonal entries),
    NOT the symmetric-part eigenvalue used by α*.

Cost: O(p(n) · d_max² · |word|) per atom — bounded for n ≤ 11.
For n=5 (³H), 7 partitions, max d=6, 14-letter word: ~600 ops.
For n=3 (³He, p, n), 3 partitions, max d=2, 6-letter word: ~50 ops.

Output: `atomic-tr-m-wenzl-bridge.witness.json`
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from datetime import datetime, timezone

from mpmath import mp, mpf

mp.dps = 50

HERE = Path(__file__).parent
Y_LAMBDA = HERE / "y-lambda-mpfr-witness.json"
DUMP_BIN = HERE.parent.parent / "tools/hecke-engine/target/release/dump-block-matrices"
OUT = HERE / "atomic-tr-m-wenzl-bridge.witness.json"

M_E_MEV = mpf("0.51099895")

J_PUBLISHED = {
    "6_2":   "q - 1 + 2/q - 2/q**2 + 2/q**3 - 2/q**4 + 1/q**5",
    "8_11":  "-q**6 + 2*q**5 - 4*q**4 + 5*q**3 - 5*q**2 + 5*q - 4 + 3/q - 1/q**2",
    "L_6a4": "q**3 - 3*q**2 + 6*q - 7 + 6/q - 3/q**2 + 1/q**3",
}

ATOMS = [
    # (binary-name,  rho, native-strands, historical-K)
    ("proton",       1, 3, None),
    ("neutron",      1, 3, None),
    ("helium3-3He",  2, 3, "L_6a4"),
    ("tritium-3H",   2, 5, "8_11"),
]


def parse_block_matrix_dump(atom_name: str) -> dict[tuple, float]:
    """Run dump-block-matrices and parse the per-block trace values.
    Returns {partition_tuple: trace_value}.
    """
    result = subprocess.run(
        [str(DUMP_BIN), "--atom", atom_name],
        capture_output=True, text=True, timeout=60,
    )
    if result.returncode != 0:
        raise RuntimeError(f"dump-block-matrices failed for {atom_name}: {result.stderr}")
    out = result.stdout
    # Match patterns like:
    #   ## λ = [5],  d_λ = 1
    #   ...
    #   trace = 0.658782, ...
    pattern = re.compile(
        r"## λ = \[([\d, ]+)\],\s+d_λ = \d+.*?trace = ([-\d.]+)",
        re.DOTALL,
    )
    matches = pattern.findall(out)
    return {
        tuple(int(x) for x in shape.split(",")): float(trace)
        for shape, trace in matches
    }


def load_y_lambda(n: int) -> dict[tuple, mpf]:
    """Load y_λ(q_0) at 50 dps for partitions of n."""
    d = json.load(open(Y_LAMBDA))
    table = d["tables_by_n"][str(n)]
    return {
        tuple(w["partition"]): mpf(w["y_lambda"])
        for w in table["weights"]
    }


def compute_tr_m(atom: str, n: int) -> tuple[mpf, dict]:
    """tr_M = Σ_λ y_λ · Tr(ρ_λ(T_w))."""
    traces = parse_block_matrix_dump(atom)
    y_lambdas = load_y_lambda(n)
    tr_m = mpf(0)
    breakdown = []
    for lam, y in y_lambdas.items():
        tr_lam = mpf(traces[lam])
        contribution = y * tr_lam
        tr_m += contribution
        breakdown.append({
            "partition": list(lam),
            "y_lambda_50dps": str(y),
            "tr_rho_lambda_f64": float(tr_lam),
            "contribution_mixed_precision": str(contribution),
        })
    return tr_m, breakdown


def main() -> int:
    if not DUMP_BIN.exists():
        print(f"  ERROR: dump-block-matrices binary not found at {DUMP_BIN}")
        print(f"  Build with: cd tools/hecke-engine && cargo build --release --bin dump-block-matrices")
        return 1

    q0_str = json.load(open(HERE / "q-pinning-50-digit.witness.json"))["derived_50_digit"]["q"]
    q0_mpf = mpf(q0_str)
    print(f"  q_0 = {q0_str}")

    results = []
    for atom, rho, n, historical_K in ATOMS:
        print(f"\n  === {atom} (n={n}, ρ={rho}) ===")
        tr_m, breakdown = compute_tr_m(atom, n)
        b_term1 = M_E_MEV * rho * abs(tr_m)
        print(f"    tr_M(q_0) (mixed precision: y_λ@50dps × Tr(ρ_λ)@f64) = {tr_m}")
        print(f"    Term-1 contribution: m_e · ρ · |tr_M| = {b_term1} MeV")

        comparison = None
        if historical_K and historical_K in J_PUBLISHED:
            import sympy as sp
            J_sym = sp.sympify(J_PUBLISHED[historical_K])
            J_at_q0 = sp.N(J_sym.subs({s: sp.Float(q0_str, 60) for s in J_sym.free_symbols}), 50)
            J_at_q0_mpf = mpf(str(J_at_q0))
            ratio = tr_m / J_at_q0_mpf if J_at_q0_mpf != 0 else None
            from mpmath import log as mp_log
            log_ratio_over_log_q0 = (
                mp_log(abs(ratio)) / mp_log(q0_mpf) if ratio and ratio != 0 else None
            )
            comparison = {
                "historical_K": historical_K,
                "J_K_at_q0": str(J_at_q0_mpf),
                "tr_M_over_J_K": str(ratio),
                "log_ratio_over_log_q0": str(log_ratio_over_log_q0),
                "writhe_match":
                    abs(round(float(log_ratio_over_log_q0)) - float(log_ratio_over_log_q0)) < 0.01
                    if log_ratio_over_log_q0 else False,
            }
            print(f"    historical K = {historical_K}")
            print(f"    J_K(q_0)   = {J_at_q0_mpf}")
            print(f"    tr_M / J_K = {ratio}")
            print(f"    log(|ratio|)/log(q_0) = {log_ratio_over_log_q0}")
            print(f"    writhe-normalised match? {comparison['writhe_match']}")

        results.append({
            "atom": atom,
            "n_strands": n,
            "rho_factor": rho,
            "tr_M_mixed_precision": str(tr_m),
            "term1_b_pred_mev": str(b_term1),
            "per_block_breakdown": breakdown,
            "historical_K_comparison": comparison,
        })

    out = {
        "computation": "atomic-tr-m-wenzl-bridge",
        "description":
            "tr_M(T_w, q_0) computed via Hoefsmit + Wenzl-bridge per "
            "prop:atom-knot-mass-derivation: tr_M = Σ_λ y_λ · Tr(ρ_λ(T_w)). "
            "y_λ at 50 dps from y-lambda-mpfr-witness.json; Tr(ρ_λ) at "
            "f64 from dump-block-matrices Rust binary. Mixed precision: "
            "the y_λ × Tr product is at f64 precision (~15 digits) — "
            "good enough for the Markov-class invariant J_K test. "
            "Sidesteps sympy's H_9 cost wall (>4 min vs <1 sec here).",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "precision": "mixed (y_λ@50dps; Tr(ρ_λ)@f64)",
        "q_0_50dps": q0_str,
        "results": results,
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(f"\n  Output: {OUT.relative_to(HERE.parent.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
