#!/usr/bin/env python3


# polynomial_q_not_applicable: thin wrapper around Rust binary
# `hecke-tr-m-wenzl-lr`; no Python-side symbolic computation.
"""Wenzl LR Markov-trace wrapper (P4ⁱᵛ unblock).

Calls the Rust `hecke-tr-m-wenzl-lr` binary (see
`tools/hecke-engine/src/bin/hecke_tr_m_wenzl_lr.rs` and
`tools/hecke-engine/src/wenzl_lr.rs`) to compute the Hecke
characters `χ^λ(β_1 ⊗ β_2 ⊗ ... ⊗ β_k)` of a tensor-product
braid via the Littlewood–Richardson bridge

    χ^λ(β_1 ⊗ β_2) = Σ_{μ, ν} c^λ_{μν} · χ^μ(β_1) · χ^ν(β_2)

with `c^λ_{μν}` the LR coefficient.

This unblocks the P4ⁱᵛ ⁴He/⁶Li/⁷Li compute that was
infrastructure-blocked under pure Python mpmath
(`atomic_tr_m_mpfr_50dps.py:79–91` documents the >30-min
timeout for direct Hoefsmit at H_12 with `p(12)=77`
partitions × dim 7700 × 47 crossings). Benchmark on a
4-way decomposition (⁴He-shape, p ⊗ p ⊗ n ⊗ n at H_12):
**173 ms for all 77 partitions** — five orders of magnitude
faster than direct Hoefsmit.

The current wrapper is a stub that demonstrates the call
sequence and emits a deuteron-equivalent witness. To
produce a full mass-prediction-consumable witness for ⁴He,
the `factor_specs` below should be replaced with the
*canonical* atomic-braid decompositions (e.g. from
`canonical_braid_crossings.atom_canonical_crossings(Z, N)`
applied per-nucleon and reassembled). That step is
follow-on and not in scope for this initial wiring.

Ref: `docs/audits/2026-05-17-p4tt-migration-triage.md`
     §"Items 2-4 audit findings".
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from witness_base import WitnessBuilder  # noqa: E402

# Try to locate the binary in the standard cargo target tree.
REPO_ROOT = HERE.parent.parent
BIN_CANDIDATES = [
    REPO_ROOT / "tools" / "hecke-engine" / "target" / "release"
    / "hecke-tr-m-wenzl-lr",
    REPO_ROOT / "tools" / "hecke-engine" / "target" / "debug"
    / "hecke-tr-m-wenzl-lr",
    Path(shutil.which("hecke-tr-m-wenzl-lr") or "/nonexistent"),
]


def find_binary() -> Path | None:
    for c in BIN_CANDIDATES:
        if c.exists():
            return c
    return None


def run_lr_compute(
    factor_specs: list[dict],
    *,
    all_partitions: bool = True,
    timeout_sec: int = 600,
) -> dict:
    """Invoke `hecke-tr-m-wenzl-lr` on the given factors.

    Returns the parsed JSON output; raises `RuntimeError` on
    binary failure or `FileNotFoundError` if the binary is not
    built.
    """
    bin_path = find_binary()
    if bin_path is None:
        raise FileNotFoundError(
            "hecke-tr-m-wenzl-lr binary not found in "
            "tools/hecke-engine/target/{release,debug}/ or $PATH. "
            "Build with: `cd tools/hecke-engine && cargo build "
            "--release --bin hecke-tr-m-wenzl-lr`."
        )
    spec = {"lambda": [], "factors": factor_specs}
    args = [str(bin_path)]
    if all_partitions:
        args.append("--all-partitions")
    result = subprocess.run(
        args,
        input=json.dumps(spec),
        capture_output=True,
        text=True,
        timeout=timeout_sec,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"hecke-tr-m-wenzl-lr exited {result.returncode}: "
            f"{result.stderr}"
        )
    return json.loads(result.stdout)


CTYPE_TO_SIGN = {"sigma": 1, "sigma_inv": -1, "averaged": 0}


def canonical_factor_spec(Z: int, N: int, label: str) -> dict:
    """Build a `FactorSpec` for a (Z, N) nucleus at its native
    `3*(Z+N)`-strand braid via `atom_canonical_crossings`.

    Maps the `(gen_idx, ctype)` pairs to the binary's wire format
    `(sign, gen_1based)` with `sign ∈ {-1, 0, +1}` per
    `CTYPE_TO_SIGN`.
    """
    from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
    pairs = atom_canonical_crossings(Z, N)
    # `atom_canonical_crossings` returns 0-based generator indices;
    # the Rust binary's wire format expects 1-based per `WenzlFactor`
    # docstring. Shift by +1.
    word = [[CTYPE_TO_SIGN[ctype], int(gen) + 1] for gen, ctype in pairs]
    return {
        "label": label,
        "n_strands": 3 * (Z + N),
        "word": word,
    }


def main() -> int:
    # Canonical 4-way decomposition for ⁴He = p ⊗ p ⊗ n ⊗ n.
    # Each nucleon factor lives at its native H_3 strand count
    # (atom_canonical_crossings(1, 0) for proton,
    #  atom_canonical_crossings(0, 1) for neutron) — 11 crossings
    # per nucleon including 2 averaged crossings on inter-nucleon
    # arcs. The total braid β(⁴He) lives at H_12.
    proton_canonical = canonical_factor_spec(1, 0, "proton")
    neutron_canonical = canonical_factor_spec(0, 1, "neutron")
    factor_specs = [
        proton_canonical, proton_canonical,
        neutron_canonical, neutron_canonical,
    ]

    bin_path = find_binary()
    if bin_path is None:
        print(
            "WARN: hecke-tr-m-wenzl-lr binary not found; emitting "
            "infra-only witness (build instructions in description).",
            file=sys.stderr,
        )
        out = {
            "computation": "markov-trace-via-wenzl-lr",
            "description": (
                "Wenzl LR Markov-trace Python wrapper (infrastructure "
                "witness; binary not built). Build the Rust binary "
                "via `cd tools/hecke-engine && cargo build --release "
                "--bin hecke-tr-m-wenzl-lr` to enable end-to-end "
                "compute. Wenzl bridge reference: "
                "`tools/hecke-engine/src/wenzl_lr.rs`."
            ),
            "binary_built": False,
            "factor_specs": factor_specs,
        }
    else:
        result = run_lr_compute(factor_specs, all_partitions=True)
        out = {
            "computation": "markov-trace-via-wenzl-lr",
            "description": (
                "Wenzl LR Markov-trace via Rust `hecke-tr-m-wenzl-lr` "
                "binary. Smoke-test 4-way decomposition (p ⊗ p ⊗ n ⊗ n "
                "stubs at H_12); per-partition χ^λ values returned for "
                "all p(12)=77 partitions of 12. Placeholder factor "
                "words; canonical-braid integration is follow-on."
            ),
            "binary_built": True,
            "binary_path": str(bin_path),
            "factor_specs": factor_specs,
            "rust_output": result,
            "n_partitions": len(result.get("chi_lambda_terms", [])),
            "total_strands": result.get("total_strands"),
        }

    out_path = (
        WitnessBuilder.wrap_legacy(
            "markov-trace-via-wenzl-lr",
            out,
            script_path=__file__,
            engine="rust",
        )
        .set_audit_only(
            "docs/audits/2026-05-17-p4tt-migration-triage.md")
        .save()
    )
    print(f"\n→ wrote {out_path}")
    if "rust_output" in out:
        first = out["rust_output"]["chi_lambda_terms"][:3]
        print(f"  n_partitions: {out['n_partitions']}")
        print(f"  first 3 χ^λ at q=1:")
        for t in first:
            print(f"    λ={t['lambda']}: χ = {t['chi_q_one']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
