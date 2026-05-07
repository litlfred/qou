#!/usr/bin/env python3
"""α_λ(H_n) via the Wenzl bridge for n = 2, ..., 12.

In the natural Wedderburn dual basis (where χ_λ(r_λ) = 1), the
identity tr_M = Σ_µ y_µ χ_µ collapses to

    α_λ(H_n) := tr_M(r_λ) = y_λ.

The Wenzl bridge gives closed-form y_λ ∈ Q(q^{1/2}) at every n
through n = 12 (witness:
folio-assistant/computations/y-lambda-wenzl-bridge-symbolic-witness.json,
prop:y-lambda-closed-form-wenzl-bridge). This script promotes those
y_λ to α_λ closed forms with the natural-normalization convention
and tabulates numerical values at q_0.

Compatibility note: the H_3 / H_4 / H_5 / H_6 explicit-α_k
propositions use a different normalization (c[last]=1 gauge).
The conversion factor is (c[last] in the natural-normalization
expansion of r_λ); when c[last] is non-zero (every hook) the
two conventions are related by a multiplicative factor. For the
canonical χ_λ(r_λ) = 1 normalization this script's α_λ equals
y_λ exactly.
"""
from __future__ import annotations
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

# P2.5 migration: emit polynomial_q alongside numerical evaluation
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).parent))
from witness_polynomial import expose_polynomial

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from q_parameter import Q as Q0_FLOAT  # noqa: E402


def main() -> int:
    src = HERE / "y-lambda-wenzl-bridge-symbolic-witness.json"
    if not src.exists():
        print(f"[ERROR] missing input: {src.name}")
        return 1

    W = json.loads(src.read_text())

    q = sp.symbols("q", positive=True)
    q0 = sp.Rational(str(Q0_FLOAT))  # centralized via q_parameter

    print("=" * 90)
    print(f"α_λ(H_n) via Wenzl bridge (natural normalization: α_λ = y_λ)")
    print(f"q_0 = {Q0_FLOAT}")
    print("=" * 90)

    out_results = {}
    for n_str, table in W["tables_by_n"].items():
        n = int(n_str)
        print(f"\n--- H_{n} ---")
        weights = table["weights"]
        rows = []
        for w in weights:
            part = tuple(w["partition"])
            sym_str = w["y_lambda_symbolic"]
            try:
                # Bind 'q' in the parsed expression to our positive symbol —
                # plain sp.sympify creates a fresh Symbol('q') that
                # subs(q, q0) won't match, leaving the value un-evaluated.
                expr = sp.sympify(sym_str, locals={"q": q})
                val_num = float(expr.subs(q, q0))
            except Exception as e:
                expr = None
                val_num = None
            row_entry = {
                "partition": list(part),
                "alpha_lambda_symbolic": sym_str if expr is not None else None,
                "alpha_lambda_at_q0": val_num,
                "depth": len(part) - 1,
            }
            # P2.5: dual symbolic + numeric exposure
            if expr is not None:
                row_entry["alpha_lambda_polynomial_q"] = expose_polynomial(expr, q)
            rows.append(row_entry)
            part_str = str(part)
            num_str = f"{val_num:+.10e}" if val_num is not None else "--"
            print(f"  {part_str:>20}  α_λ = {num_str}")
        out_results[n_str] = {"n": n, "weights": rows}

    out = {
        "computation": "alpha-k-via-wenzl-bridge",
        "description": (
            "α_λ(H_n) closed forms for n=2..12 derived from the Wenzl-bridge "
            "y_λ symbolic witness (prop:y-lambda-closed-form-wenzl-bridge). "
            "In the natural Wedderburn dual basis (χ_λ(r_λ)=1), α_λ = y_λ; "
            "this script just relabels and tabulates numerical values at q_0."
        ),
        "engine": "sympy",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q_0": float(Q0_FLOAT),
        "normalization": "natural (chi_lambda(r_lambda) = 1) — α_λ = y_λ",
        "tables_by_n": out_results,
    }
    out_path = HERE / "alpha-k-via-wenzl-bridge.witness.json"
    with open(out_path, "w") as fp:
        json.dump(out, fp, indent=2, default=str)
    print(f"\nWitness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
