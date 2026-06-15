#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical mpmath/sympy regenerator; symbolic source is y-lambda-wenzl-bridge-symbolic-witness.json.
"""Regenerate `y-lambda-mpfr-witness.json` at TRUE 50 dps from the
symbolic Wenzl-bridge witness.

Per the convention/precision audit on PR #564, the previous
`y-lambda-mpfr-witness.json` was produced by
`_deprecated/y_lambda_mpfr_witness.py:152` with

    q_str = str(Q0_FLOAT)   # truncates Python float to 16 digits

so its claimed "50 dps" y_λ values were f64-truncated past digit ~14:

    mpfr  (claimed 50 dps): 0.05918771693214865618475938399646…
    symbolic (true 50 dps): 0.05918771693214863172663201740000…
                                          ^^^^^^^^^^^^^^^^^^ noise

The downstream cascade (`tr_m_wenzl_bridge_mpfr.py` →
`atomic-tr-m-mpfr-50dps.witness.json` → every canonical |tr_M|
reader) inherited this truncation, capping the Schur-Weyl identity
residual in `rho_k_h3a_refinement.py` at 1.4e-16 (machine f64
precision floor) instead of the 1e-40 tolerance the test gates at.

This regenerator side-steps the f64 issue by reading the symbolic
y_λ witness (`y-lambda-wenzl-bridge-symbolic-witness.json`, n=2..12,
exact symbolic in q) and evaluating each y_λ at the substrate q_0 to
true 50 dps via sympy's `subs(q, q_0_str_50dps).evalf(50)`.

The resulting witness is bit-identical at 50 dps to what the Rust
kernel `pyhecke_native.chi_lambda_braid_mpfr` would have produced
had its q_str input been correct, but doesn't require the Rust
extension (which is unavailable in many environments) and covers
n=12 (which the Rust kernel times out on at >45 min wall).

Output: `y-lambda-mpfr-witness.json` (replaces the f64-truncated
witness in place; consumed by `tr_m_wenzl_bridge_mpfr.py`).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q_MP  # noqa: E402

set_compute_dps()

SOURCE = HERE / "y-lambda-wenzl-bridge-symbolic-witness.json"
OUTPUT = HERE / "y-lambda-mpfr-witness.json"


def evaluate_y_at_q0(symbolic_str: str, q0_str_50dps: str) -> str:
    """Evaluate a symbolic y_λ expression at q_0 to 50 dps.

    Returns the value as a 50-dp decimal string (mpf-roundtrip safe).
    """
    expr = sp.sympify(symbolic_str)
    free = expr.free_symbols
    if free:
        qsym = next(iter(free))
        sub = expr.subs(qsym, sp.sympify(q0_str_50dps))
    else:
        sub = expr
    val = sub.evalf(mp.mp.dps)
    # Roundtrip via mp.mpf to canonicalise the string format.
    return mp.nstr(mp.mpf(str(val)), mp.mp.dps, strip_zeros=False)


def main() -> int:
    print("=" * 96)
    print("  Regenerate y-lambda-mpfr-witness.json at TRUE 50 dps")
    print("  Source: y-lambda-wenzl-bridge-symbolic-witness.json (exact symbolic)")
    print("=" * 96)

    q0_str = mp.nstr(Q_MP, 50, strip_zeros=False)
    print(f"\n  q_0 (50 dps) = {q0_str}")

    sym = json.loads(SOURCE.read_text())
    sym_tables = sym["tables_by_n"]
    ns = sorted(int(k) for k in sym_tables.keys())
    print(f"  Source has tables for n in: {ns}")

    out_tables: dict = {}
    for n in ns:
        n_str = str(n)
        src = sym_tables[n_str]
        weights = src["weights"]
        print(f"  Evaluating n={n}: {len(weights)} partitions ...", flush=True)
        # z = 1 / (q^{1/2} + q^{-1/2}) at 50 dps
        q = mp.mpf(q0_str)
        z = mp.mpf(1) / (mp.sqrt(q) + mp.mpf(1) / mp.sqrt(q))

        out_weights = []
        for w in weights:
            lam = w["partition"]
            y_str = evaluate_y_at_q0(w["y_lambda_symbolic"], q0_str)
            out_weights.append({
                "partition": lam,
                "depth": max(0, len(lam) - 1),
                "y_lambda": y_str,
            })

        out_tables[n_str] = {
            "n": n,
            "num_partitions": len(weights),
            "q": q0_str,
            "z": mp.nstr(z, 50, strip_zeros=False),
            "dps": 50,
            "weights": out_weights,
        }

    # ── Emit witness ──────────────────────────────────────────────
    src_bytes = SOURCE.read_bytes()
    src_hash = "sha256:" + hashlib.sha256(src_bytes).hexdigest()
    script_hash = "sha256:" + hashlib.sha256(
        Path(__file__).read_bytes()
    ).hexdigest()

    out = {
        "computation": "y-lambda-mpfr-witness",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "y_λ values at H_n(R, q_0) evaluated to true 50 dps from "
            "the exact symbolic y_λ expressions in "
            "y-lambda-wenzl-bridge-symbolic-witness.json. Replaces the "
            "f64-truncated witness produced by "
            "_deprecated/y_lambda_mpfr_witness.py (line 152: "
            "q_str = str(Q0_FLOAT) truncates to 16 digits). The "
            "previous witness's claimed '50 dps' values matched true "
            "50 dps only to ~14 digits; this regeneration uses "
            "mp.nstr(Q_MP, 50) for q and sympy subs+evalf for each "
            "y_λ, giving full 50-dps precision."
        ),
        "engine": "sympy subs(q, q_0_50dps).evalf(50) over symbolic y_λ",
        "scriptFile": "regenerate_y_lambda_mpfr.py",
        "scriptHash": script_hash,
        "source_witness": "y-lambda-wenzl-bridge-symbolic-witness.json",
        "source_witness_hash": src_hash,
        "q_0_50dps": q0_str,
        "dps": 50,
        "tables_by_n": out_tables,
        "audit_reference": "AUDIT-DEEP-2026-05.md §7; PR #564 convention/precision audit",
        "pr": "#564",
    }
    # NOTE: Cannot use WitnessBuilder.wrap_legacy().save() here
    # because the output filename is `y-lambda-mpfr-witness.json`
    # (without the standard `.witness.json` suffix), and consumers
    # (tr_m_wenzl_bridge_mpfr.py:53 _Y_LAMBDA_DEFAULT) read that
    # exact name. Use the public WitnessBuilder.stamp_staleness_metadata
    # helper to inject scriptHash/scriptCommitSha/commitSha/engine/
    # engineVersion/computedAt/durationMs in place, then write to
    # the legacy filename — keeps the consumer chain unbroken.
    from witness_base import WitnessBuilder
    out["auditOnly"] = "AUDIT-DEEP-2026-05.md"
    WitnessBuilder.stamp_staleness_metadata(
        out, script_path=__file__, engine="python+mpmath",
        engine_version=f"sympy {sp.__version__} + mpmath {mp.__version__}",
    )
    OUTPUT.write_text(json.dumps(out, indent=2) + "\n")
    print(f"\n  Wrote {OUTPUT.name} ({OUTPUT.stat().st_size} bytes).")
    print(f"  tables_by_n keys: {sorted(out_tables.keys(), key=int)}")
    print("=" * 96)
    return 0


if __name__ == "__main__":
    sys.exit(main())
