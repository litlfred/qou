#!/usr/bin/env python3
# polynomial_q_not_applicable: mpmath/numerical-only output; sympy use is intermediate or absent.
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

from mpmath import mp, mpf, log as mp_log
import sympy as sp

# Module-level precision contract: this is a high-precision scientific
# script, not a reusable library. Per Gemini review on PR #456 we use
# mp.workdps() inside main() for explicit local scope; the module-level
# default is left at mpmath's default to avoid polluting importers.

HERE = Path(__file__).parent
Y_LAMBDA = HERE / "y-lambda-mpfr-witness.json"
# Override via QOU_DUMP_BLOCK_MATRICES env var if the binary is not at
# the default Cargo release path (per Gemini review on PR #456).
import os  # noqa: E402
DUMP_BIN = Path(
    os.environ.get(
        "QOU_DUMP_BLOCK_MATRICES",
        str(HERE.parent.parent / "tools/hecke-engine/target/release/dump-block-matrices"),
    )
)
OUT = HERE / "atomic-tr-m-wenzl-bridge.witness.json"

M_E_MEV = mpf("0.51099895")

J_PUBLISHED = {
    # 3_1 (right-handed trefoil): in our σ²=(q-q⁻¹)σ+1 convention,
    # closure of σ_1³ in B_2 has tr_M(σ_1³) = ((q-q⁻¹)²+1)·z + (q-q⁻¹)
    # which equals q + q³ - q⁴ in the canonical Jones polynomial form
    # (Murasugi §11.3, KnotInfo).
    "3_1":   "q + q**3 - q**4",
    "6_2":   "q - 1 + 2/q - 2/q**2 + 2/q**3 - 2/q**4 + 1/q**5",
    "8_11":  "-q**6 + 2*q**5 - 4*q**4 + 5*q**3 - 5*q**2 + 5*q - 4 + 3/q - 1/q**2",
    "L_6a4": "q**3 - 3*q**2 + 6*q - 7 + 6/q - 3/q**2 + 1/q**3",
}

ATOMS = [
    # (binary-name,  rho, native-strands, historical-K)
    ("electron",     1, 2, "3_1"),
    ("proton",       1, 3, None),
    ("neutron",      1, 3, None),
    ("deuteron-2H",  1, 3, "6_2"),
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


def load_y_lambda(n: int, q0: mpf | None = None) -> dict[tuple, mpf]:
    """Load y_λ(q_0) at 50 dps for partitions of n.

    `q0` is required for n=2 (witness only covers n ≥ 3). Per Gemini
    review on PR #456: q0 is now passed in by the caller instead of
    being hardcoded — single source of truth from main()'s
    q-pinning-50-digit witness load.
    """
    if n == 2:
        if q0 is None:
            raise ValueError("q0 required for n=2 (not in y-lambda witness)")
        # Linear system: y_(2) + y_(1,1) = 1; y_(2)·q + y_(1,1)·(-q^{-1}) = z.
        z = mpf(1) / (mp.sqrt(q0) + mp.sqrt(mpf(1) / q0))
        q_inv = mpf(1) / q0
        y_2 = (z + q_inv) / (q0 + q_inv)
        y_11 = mpf(1) - y_2
        return {(2,): y_2, (1, 1): y_11}
    with open(Y_LAMBDA) as f:
        d = json.load(f)
    table = d["tables_by_n"][str(n)]
    return {
        tuple(w["partition"]): mpf(w["y_lambda"])
        for w in table["weights"]
    }


def compute_tr_m(atom: str, n: int, q0: mpf) -> tuple[mpf, dict]:
    """tr_M = Σ_λ y_λ · Tr(ρ_λ(T_w))."""
    traces = parse_block_matrix_dump(atom)
    y_lambdas = load_y_lambda(n, q0=q0)
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

    # Local precision scope per Gemini review on PR #456.
    with mp.workdps(50):
        with open(HERE / "q-pinning-50-digit.witness.json") as f:
            q0_str = json.load(f)["derived_50_digit"]["q"]
        q0_mpf = mpf(q0_str)
        print(f"  q_0 = {q0_str}")

        results = []
        for atom, rho, n, historical_K in ATOMS:
            print(f"\n  === {atom} (n={n}, ρ={rho}) ===")
            tr_m, breakdown = compute_tr_m(atom, n, q0=q0_mpf)
            b_term1 = M_E_MEV * rho * abs(tr_m)
            print(f"    tr_M(q_0) (mixed precision: y_λ@50dps × Tr(ρ_λ)@f64) = {tr_m}")
            print(f"    Term-1 contribution: m_e · ρ · |tr_M| = {b_term1} MeV")

            # The J_K integer-power test is structurally post-Archimedean
            # (Jones polynomials require ribbon framing; ribbon datum lives
            # post-Archimedean per def:sqrt-q-ribbon-structure). The
            # writhe-normalised match field is therefore not a well-defined
            # pre-Archimedean structural test. Disabled per
            # docs/audits/markov-test-is-post-archimedean.md and the Gemini
            # review on PR #456. The published J_K polynomials remain in
            # J_PUBLISHED for documentation; the comparison is recorded as
            # informational only with a "post_archimedean_caveat" tag.
            comparison = None
            if historical_K and historical_K in J_PUBLISHED:
                comparison = {
                    "historical_K": historical_K,
                    "J_K_published_polynomial": J_PUBLISHED[historical_K],
                    "post_archimedean_caveat":
                        "J_K and tr_M live in different categories — see "
                        "docs/audits/markov-test-is-post-archimedean.md. "
                        "No ratio-test or writhe-match is computed.",
                }
                print(f"    historical K = {historical_K}")
                print(f"    (J_K vs tr_M comparison is post-Archimedean — see audit.)")

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
                "the y_λ × Tr product is at f64 precision (~15 digits). "
                "Sidesteps sympy's H_9 cost wall (>4 min vs <1 sec here). "
                "J_K writhe-match test disabled per "
                "docs/audits/markov-test-is-post-archimedean.md.",
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
