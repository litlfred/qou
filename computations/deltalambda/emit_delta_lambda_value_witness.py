#!/usr/bin/env python3
"""Emit `delta-lambda-witness.json` — the PROVED per-partition Δ_λ VALUE (bean qou-e84e).

Δ_λ = (-1)^{n(λ)} · dim V_λ   (signed Springer dimension)
  * sign     = (-1)^{n(λ)}, n(λ) = Σ_i (i-1)λ_i = Σ_i C(λ'_i, 2)  (the a-/n-statistic, jet-order
               valuation parity) — Lean `dtEuler = (-1)^{nStat}·dim`, general-n, sorry-free (#4580,
               `DeltaLambdaGeneralNUnconditional.dtEuler_eq_deltaLambda_unconditional`).
  * magnitude= dim V_λ = f^λ (number of standard Young tableaux, hook-length formula) — the
               Wedderburn dimension of the S_n irrep.

This is the general-n proved VALUE, derived from the drivers (NOT fitted). It moves the consumer
`binding_K_direct.py` off `delta_lambda_unavailable` → `delta_lambda_value_present`. It does NOT
produce accurate binding: the value must still be y_λ·χ^λ-weighted, and the extensive many-body
MAGNITUDE term stays a SEPARATE open input. `value_only: true` tells the consumer to emit only a
labelled raw-Σ diagnostic, never a binding prediction (anti-laundering).

Per-atom partitions: n = 3A strands (p,n → H₃; D → H₆; T,³He → H₉; ⁴He → H₁₂). The Δ_λ VALUE is a
function of λ ALONE (atom-independent); the per-atom nesting only selects the relevant partition set.

Mathlib-free (pure Python int arithmetic). No fit, B_AME never referenced.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent


def partitions(n: int):
    """All integer partitions of n as weakly-decreasing tuples."""
    def _gen(n, maxp):
        if n == 0:
            yield ()
            return
        for first in range(min(n, maxp), 0, -1):
            for rest in _gen(n - first, first):
                yield (first,) + rest
    yield from _gen(n, n)


def n_statistic(lam: tuple[int, ...]) -> int:
    """n(λ) = Σ_i (i-1)·λ_i, i indexed from 1 (the a-/n-statistic)."""
    return sum((i) * part for i, part in enumerate(lam))  # enumerate gives i=0..,(i)=(i+1-1)


def hook_length_syt_count(lam: tuple[int, ...]) -> int:
    """f^λ = n! / Π hooks — the number of standard Young tableaux (Wedderburn dim of the S_n irrep)."""
    n = sum(lam)
    # conjugate (column lengths)
    if not lam:
        return 1
    cols = [0] * lam[0]
    for part in lam:
        for c in range(part):
            cols[c] += 1
    # product of hook lengths
    from math import factorial
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            arm = row - j - 1
            leg = cols[j] - i - 1
            prod *= (arm + leg + 1)
    return factorial(n) // prod


def delta_lambda(lam: tuple[int, ...]) -> int:
    """Δ_λ = (-1)^{n(λ)} · f^λ (proved signed Springer dimension)."""
    sign = -1 if (n_statistic(lam) % 2 == 1) else 1
    return sign * hook_length_syt_count(lam)


# atom → strand count n = 3A
ATOM_N = {"p": 3, "n": 3, "D": 6, "T": 9, "3He": 9, "4He": 12}


def main() -> int:
    per_atom: dict[str, dict[str, int]] = {}
    for atom, n in ATOM_N.items():
        blocks: dict[str, int] = {}
        for lam in partitions(n):
            blocks["[" + ",".join(str(p) for p in lam) + "]"] = delta_lambda(lam)
        per_atom[atom] = blocks

    # sanity identities (self-check, not a fit)
    # Σ (f^λ)^2 = n!  ;  Σ_{λ⊢6} sgn·f^λ should match committed data (D: Σ sgn f^λ = 16 = 2^4, #4556 §4)
    from math import factorial
    checks = {}
    for atom, n in [("D", 6), ("T", 9), ("4He", 12)]:
        sqsum = sum(hook_length_syt_count(l) ** 2 for l in partitions(n))
        signed = sum(delta_lambda(l) for l in partitions(n))
        checks[atom] = {"sum_flambda_sq": sqsum, "n_factorial": factorial(n),
                        "sum_flambda_sq_eq_n_fact": sqsum == factorial(n),
                        "sum_signed_delta_lambda": signed}

    script_bytes = Path(__file__).read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()[:12]
    try:
        commit = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", __file__],
            cwd=HERE, text=True).strip() or "uncommitted"
    except Exception:
        commit = "uncommitted"

    witness = {
        "engine": "python-int-exact",
        "engineVersion": "3",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "scriptFile": "computations/deltalambda/emit_delta_lambda_value_witness.py",
        "scriptHash": script_hash,
        "scriptCommitSha": commit,
        "description": "Proved per-partition Δ_λ = (-1)^{n(λ)}·dim V_λ (signed Springer dimension, "
                       "general-n, sorry-free #4580). VALUE only — NOT a binding prediction: needs "
                       "y_λ·χ^λ weighting + the separate open extensive magnitude term.",
        "contentBlock": "conj:binding-manybody-eq-jet-filtration",
        "tier": "proved-value emission (Lean sorry-free general-n); derivation-legal; value_only; "
                "magnitude/concentration kept OPEN; nothing binding wired.",
        "value_only": True,
        "provenance": {
            "lean_value_theorem": "QOU.BraidsAndKnots.DeltaLambdaGeneralNUnconditional."
                                  "dtEuler_eq_deltaLambda_unconditional (#4580, sorry-free)",
            "sign_theorem": "dtEuler = (-1)^{nStat}·dim; nStat = Σ_i C(λ'_i,2) = Σ_i (i-1)λ_i",
            "magnitude": "dim V_λ = f^λ (SYT count, hook-length formula)",
            "value_is_atom_independent": True,
            "per_atom_nesting_selects_partition_set_only": True,
            "no_fit_no_AME": True,
        },
        "self_checks": checks,
        "delta_lambda_per_atom": per_atom,
        "auditOnly": False,
    }

    out = HERE / "delta-lambda-witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"✓ wrote {out}")
    print(f"  atoms: {list(per_atom)}")
    for atom, n in [("D", 6), ("T", 9), ("4He", 12)]:
        c = checks[atom]
        print(f"  {atom} (n={n}): Σ(f^λ)²={c['sum_flambda_sq']} == n! ? {c['sum_flambda_sq_eq_n_fact']}; "
              f"Σ signed Δ_λ = {c['sum_signed_delta_lambda']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
