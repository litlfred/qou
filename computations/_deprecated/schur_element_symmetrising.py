"""
Theorem 4.3 from Chlouveraki HDR — Schur element for the
SYMMETRISING TRACE on the type-A Iwahori-Hecke algebra.

Reference: Chlouveraki, "Hecke algebras, generalisations and
representation theory" (HDR thesis), Theorem 4.3, l = 1 (type A).

For λ ⊢ n in the type A Iwahori-Hecke algebra H_n(q):

    s_λ(q) = q^{-N(λ)} · (q-1)^{-n} · ∏_{x ∈ λ} (q^{h(x)} - 1)

where:
- N(λ) = Σ_{i ≥ 1} (i-1) λ_i  (1-indexed convention)
- h(x) = hook length at cell x = (i, j) ∈ λ
- The trace τ is the SYMMETRISING form on H_n(q): τ(σ_w) = δ_{w, 1}.

This is NOT the same as the Markov-trace block weight y_λ used
elsewhere in this codebase.  The Markov trace tr_M is a DIFFERENT
trace:

    tr_M(x · σ_n) = z · tr_M(x),  z = 1/(q^{1/2} + q^{-1/2}).

The symmetrising trace satisfies τ(σ_w) = δ_{w,1} (zero on every
non-identity reduced word), whereas the Markov trace satisfies
tr_M(σ_i) = z and tr_M(σ_i σ_j) = z² for distinct i, j.

Implication for closed-form y_λ at n ≥ 5:

If our Markov-trace parameter z corresponded to a Wenzl SU_q(N)
specialisation (i.e. z = (1-q)/(1-q^{N+1}) for some integer N,
or equivalently z = q^{N/2}/[N+1]_q^{symm}), the Markov-trace y_λ
would be related to s_λ by an explicit specialisation formula
(Wenzl 1988), giving a closed-form product.

But our z = 1/(q^{1/2} + q^{-1/2}) at q_0 ≈ 1.1097 satisfies neither
Wenzl-specialisation equation for any integer N.  Specifically, the
equation (1-q)(q^{1/2}+q^{-1/2}) = 1 - q^{N+1} solves at N+1 =
ln(1.22)/ln(1.11) ≈ 1.91 — non-integer.

So our Markov trace is the GENERIC one (Markov property + tr(1)=1
+ tr(σ_i)=z), and the y_λ are just the linear-system inverse
solution.  No closed-form product over cells applies; the
symbolic q-rational expressions we already compute are the canonical
answer.

This script implements Theorem 4.3 for verification / cross-check
purposes only — it gives the symmetrising-trace Schur elements,
not the Markov-trace y_λ.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401

sys.path.insert(0, str(Path(__file__).parent))
from y_lambda_jones_markov_witness import partitions_of


def hook_lengths(partition: list[int]) -> dict:
    """Hook length at every cell (i, j) ∈ λ."""
    rows = len(partition)
    cols = max(partition) if rows else 0
    transpose = [
        sum(1 for r in range(rows) if partition[r] > c)
        for c in range(cols)
    ]
    return {
        (i, j): (partition[i] - j - 1) + (transpose[j] - i - 1) + 1
        for i in range(rows)
        for j in range(partition[i])
    }


def n_lambda(partition: list[int]) -> int:
    """N(λ) = Σ (i-1) λ_i  (1-indexed) = Σ i · λ_{i+1} (0-indexed)."""
    return sum(i * partition[i] for i in range(len(partition)))


def schur_element_steinberg(partition: list[int], q: sp.Symbol):
    """Theorem 4.3 (Chlouveraki HDR) at l = 1 — type A symmetrising Schur."""
    n = sum(partition)
    hooks = hook_lengths(partition)
    prod = sp.Integer(1)
    for hx in hooks.values():
        prod *= (q ** hx - 1)
    return q ** (-n_lambda(partition)) * (q - 1) ** (-n) * prod


def main() -> None:
    """Generate symbolic Schur-element table for n ≤ 12."""
    q = sp.Symbol("q", positive=True)
    out = {
        "description": (
            "Symmetrising-trace Schur elements s_λ(q) for type-A "
            "Iwahori-Hecke H_n(q) via Chlouveraki HDR Theorem 4.3 at "
            "l = 1.  These are NOT the Markov-trace block weights y_λ; "
            "see this script's docstring for why our generic Markov "
            "trace (z = 1/(q^{1/2}+q^{-1/2})) does not match any Wenzl "
            "SU_q(N) specialisation, and therefore has no closed-form "
            "product-over-cells formula."
        ),
        "reference": "Chlouveraki, HDR thesis, Theorem 4.3 (l=1)",
        "formula": "s_λ(q) = q^{-N(λ)} (q-1)^{-n} ∏_{x ∈ λ} (q^{h(x)} - 1)",
        "tables_by_n": {},
    }
    for n in range(2, 13):
        parts = list(partitions_of(n))
        out["tables_by_n"][str(n)] = [
            {
                "partition": list(p),
                "schur_element": str(sp.factor(schur_element_steinberg(list(p), q))),
            }
            for p in parts
        ]
        print(f"n = {n}: {len(parts)} Schur elements computed")

    out_path = Path(__file__).parent / "schur-element-symmetrising-witness.json"
    out_path.write_text(json.dumps(out, indent=2))
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
