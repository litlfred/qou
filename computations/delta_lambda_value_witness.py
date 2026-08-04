#!/usr/bin/env python3
# polynomial_q_not_applicable: exact integer partition arithmetic; no q, no float.
"""
Emit the PROVED per-partition binding weight

    Δ_λ = (-1)^{n(λ)} · dim V_λ        (the signed Springer dimension)

for the partitions relevant to each light-atom braid index, into
`delta-lambda-witness.json`.  This is the closed form proved sorry-free,
general-n, in Lean:

    QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional   (PR #4580)

where the SIGN is the jet-order valuation parity
`deltaSign_eq_nStat_parity` — n(λ) = Σ_i C(λ'_i, 2) (Lusztig a-function,
λ' the conjugate) — and the MAGNITUDE is the Wedderburn dimension
dim V_λ = f^λ (number of standard Young tableaux, hook-length formula).

**IMPORTANT — value only, NOT a binding prediction.** The per-isotope
binding total is

    B(K) = m_e · Σ_λ y_λ(q_0) · χ^λ(β_K) · Δ_λ(K)

and additionally requires (a) the y_λ·χ^λ weighting and (b) a SEPARATE
super-pairwise additive *extensive* magnitude term that no per-block Δ_λ
can supply (proved: 2026-06-02-binding-intensive-vs-extensive-derivation.md;
2026-07-18-deltalambda-saturation-det-ceiling.md, cap ρ_A ≤ C(A,2)).
This witness therefore sets `value_only: true`; downstream consumers must
NOT read the raw Σ Δ_λ as a binding energy.

Braid index per atom is 3A (three quark colour strands per nucleon):
    p, n → λ ⊢ 3 ;  D → λ ⊢ 6 ;  T, 3He → λ ⊢ 9 ;  4He → λ ⊢ 12.

Usage:
    python3 computations/delta_lambda_value_witness.py
"""
from __future__ import annotations

import _path_bridge  # noqa: F401
import sys
from math import comb, factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402


def partitions(n: int, maxpart: int | None = None):
    """Yield partitions of n as weakly-decreasing tuples."""
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def conjugate(lam: tuple[int, ...]) -> tuple[int, ...]:
    if not lam:
        return ()
    return tuple(sum(1 for p in lam if p >= i) for i in range(1, lam[0] + 1))


def n_lambda(lam: tuple[int, ...]) -> int:
    """Lusztig a-function n(λ) = Σ_i C(λ'_i, 2)  (jet-order valuation)."""
    return sum(comb(c, 2) for c in conjugate(lam))


def dim_irrep(lam: tuple[int, ...]) -> int:
    """dim V_λ = f^λ = n! / ∏ hook lengths (Frame–Robinson–Thrall)."""
    n = sum(lam)
    lp = conjugate(lam)
    prod = 1
    for i, row in enumerate(lam):          # 0-indexed row i, column j
        for j in range(row):
            hook = (row - j - 1) + (lp[j] - i - 1) + 1
            prod *= hook
    return factorial(n) // prod


def delta_lambda(lam: tuple[int, ...]) -> int:
    """Δ_λ = (-1)^{n(λ)} · dim V_λ  (the proved signed Springer dimension)."""
    return (-1) ** n_lambda(lam) * dim_irrep(lam)


def shape_str(lam: tuple[int, ...]) -> str:
    return "[" + ",".join(str(p) for p in lam) + "]"


ATOM_BRAID_INDEX = {"p": 3, "n": 3, "D": 6, "T": 9, "3He": 9, "4He": 12}


def main() -> int:
    w = WitnessBuilder("delta-lambda-value", engine="exact-integer")
    w.set_description(
        "Proved per-partition binding weight Δ_λ = (-1)^{n(λ)}·dim V_λ "
        "(signed Springer dimension), the sorry-free general-n closed form "
        "(Lean QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional, PR #4580). "
        "VALUE ONLY: the binding total additionally needs the y_λ·χ^λ weighting "
        "and a separate super-pairwise extensive magnitude term (open). Consumers "
        "must not read Σ Δ_λ as a binding energy."
    )
    w.set_content_block("alg:delta-lambda-closure")
    w.add_parameter("value_only", True)
    w.add_parameter("formula", "Delta_lambda = (-1)^{n(lambda)} * dim V_lambda")
    w.add_parameter("sign_leg", "n(lambda) = sum_i C(lambda'_i, 2)  (jet-order parity)")
    w.add_parameter("magnitude_leg", "dim V_lambda = f^lambda (hook-length)")
    w.add_parameter("lean_ref", "QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional")

    # by-partition reference table (Δ_λ depends only on λ, not on the atom)
    by_partition: dict[str, dict[str, str]] = {}
    completeness_ok = True
    for n in (2, 3, 4, 5, 6, 9, 12):
        tab: dict[str, str] = {}
        sum_sq = 0
        for lam in partitions(n):
            d = dim_irrep(lam)
            sum_sq += d * d
            # internal cross-check: |Δ_λ| = dim V_λ  (abs_deltaLambda_eq_dim)
            assert abs(delta_lambda(lam)) == d, (lam, delta_lambda(lam), d)
            tab[shape_str(lam)] = str(delta_lambda(lam))
        # completeness: Σ_λ (dim V_λ)^2 = n!  (Wedderburn)
        if sum_sq != factorial(n):
            completeness_ok = False
        by_partition[str(n)] = tab
    w.add_parameter("dim_completeness_check_ok", completeness_ok)
    assert completeness_ok, "Wedderburn completeness Σ (dim)^2 = n! failed"
    w.add_data("delta_lambda_by_partition", by_partition)

    # per-atom map keyed by the atom's braid index 3A
    per_atom: dict[str, dict[str, str]] = {}
    for atom, nidx in ATOM_BRAID_INDEX.items():
        per_atom[atom] = {shape_str(lam): str(delta_lambda(lam))
                          for lam in partitions(nidx)}
    w.add_data("delta_lambda_per_atom", per_atom)
    w.add_caveat(
        "value_only: Σ_λ Δ_λ is NOT a binding energy. The binding weight per λ "
        "is proved; the many-body magnitude (super-pairwise extensive term) is open."
    )

    # The consumer (binding_K_direct.py::load_delta_lambda) hard-codes the
    # filename `delta-lambda-witness.json` and reads TOP-LEVEL keys, so hoist
    # the consumer keys to top level while keeping the standard witness
    # provenance (build() nests add_data/add_parameter under data/parameters).
    import json
    built = w.build()
    built["delta_lambda_per_atom"] = per_atom
    built["delta_lambda_by_partition"] = by_partition
    built["value_only"] = True
    out = HERE / "delta-lambda-witness.json"
    out.write_text(json.dumps(built, indent=2, sort_keys=True) + "\n")
    print(f"  wrote {out.name}")
    print(f"  Wedderburn completeness Σ(dim)² = n!  : {'OK' if completeness_ok else 'FAIL'}")
    print(f"  atoms: {', '.join(per_atom)}")
    for n in (3, 5, 6):
        row = ", ".join(f"{k}:{v}" for k, v in by_partition[str(n)].items())
        print(f"  Δ_λ, n={n}: {row}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
