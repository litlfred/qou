#!/usr/bin/env python3
"""
Markov substrate realizer — `Place → realize` map for the Habiro
completion of the Markov trace.

Mirrors the Lean class `QOU.AlgebraicSubstrate.MotivicSubstrate`:

    realize : (v : Place) → Mhat →+* Target v

with `Place = infty | finite p`.  For the Habiro-completion sector
(`Mhat = ℤ[u]`):

  * `Place.infty`           — archimedean realization, `Target = ℝ`,
    obtained by evaluating `tr_M(q)` at the substrate parameter `q_0`
    (numerical mpmath, 60 dps).
  * `Place.finite p`        — `Target = 𝔽_p[u]`, obtained by reducing
    the coefficients of `p_in_u ∈ ℤ[u]` modulo `p` via the ring
    homomorphism `Int.castRingHom (ZMod p)`.

This is **Win 2** of the post-#460 pipeline audit, in its
simplified form: only mod-p coefficient reduction is implemented;
full p-adic numerics (e.g. `ℚ_p`-valued evaluation at p-adic units,
LP shadow prices, Iwasawa-style decomposition) are left for a
follow-up.

The realizer also re-validates the `tail_in_ideal` axiom in the
mod-p reduced ring: ring homomorphisms preserve divisibility, so
`(u;u)_N` mod p must still divide the residual mod p.  This is a
free consistency check — failure would indicate a sympy domain-
coercion bug rather than a genuine mathematical issue.

Output witness: `markov-substrate-realization.witness.json` —
per-atom, per-place table of realizations.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp
from sympy import GF, Integer, Symbol

sys.path.insert(0, str(Path(__file__).parent))
from habiro_types import HabiroAtomicWitness, HabiroCompletionRecord


HERE = Path(__file__).parent
INPUT_WITNESS = HERE / "habiro-coefficients-atomic.witness.json"
OUTPUT_WITNESS = HERE / "markov-substrate-realization.witness.json"

FINITE_PLACES = [2, 3, 5, 7, 11, 13]


def q_pochhammer_poly(N: int, u: Symbol, domain) -> sp.Poly:
    """`(u;u)_N = ∏_{k=1..N} (1 − u^k)` as a sympy Poly over `domain[u]`."""
    expr = Integer(1)
    for k in range(1, N + 1):
        expr *= (1 - u ** k)
    return sp.Poly(sp.expand(expr), u, domain=domain)


def parse_poly_zz(s: str, u: Symbol) -> sp.Poly:
    return sp.Poly(sp.expand(sp.sympify(s, locals={"u": u})), u, domain="ZZ")


def realize_archimedean(record: HabiroCompletionRecord, q_0: float) -> dict:
    """Numerical archimedean realization at `q = q_0`.

    The Markov-normalised polynomial `p_in_u(u)` in `u = q^{1/2}` is
    evaluated at `u_0 = q_0^{1/2}`; division by `denom_in_u(u_0)`
    recovers the trace `tr_M(q_0)`.
    """
    u = sp.symbols("u")
    p_u = parse_poly_zz(record.p_in_u, u)
    d_u = parse_poly_zz(record.denom_in_u, u)
    u_0 = sp.sqrt(sp.Rational(q_0).limit_denominator(10**12))
    p_val = p_u.eval(u_0)
    d_val = d_u.eval(u_0)
    if d_val == 0:
        return {"place": "infty", "target": "ℝ", "value": None, "error": "denom vanishes at u_0"}
    return {
        "place": "infty",
        "target": "ℝ",
        "u_0": float(sp.N(u_0, 30)),
        "tr_M_at_q0": float(sp.N(p_val / d_val, 30)),
    }


def realize_finite_prime(record: HabiroCompletionRecord, prime: int) -> dict:
    """Reduce `p_in_u : ℤ[u]` modulo `prime` via the canonical ring
    homomorphism `Int.castRingHom (ZMod p)`, then check that the
    `tail_in_ideal` axiom carries through.  This is a free
    consistency check on the realization map.
    """
    u = sp.symbols("u")
    p_u_zz = parse_poly_zz(record.p_in_u, u)
    p_u_fp = sp.Poly(p_u_zz.as_expr(), u, domain=GF(prime))

    coeffs_fp = [
        sp.Poly(parse_poly_zz(c.a_m, u).as_expr(), u, domain=GF(prime))
        for c in record.habiro_coefficients
    ]

    # Sanity: tail_in_ideal must hold modulo prime as well.
    divisibility_holds = True
    for N in range(1, len(coeffs_fp) + 1):
        partial = sp.Poly(0, u, domain=GF(prime))
        for m in range(N):
            partial = partial + coeffs_fp[m] * q_pochhammer_poly(m, u, GF(prime))
        residual = p_u_fp - partial
        divisor = q_pochhammer_poly(N, u, GF(prime))
        try:
            _, remainder = sp.div(residual, divisor, u, domain=GF(prime))
            if not remainder.is_zero:
                divisibility_holds = False
                break
        except sp.PolynomialError:
            divisibility_holds = False
            break

    return {
        "place": f"finite({prime})",
        "target": f"𝔽_{prime}[u]",
        "p_in_u_mod_p": str(p_u_fp.as_expr()),
        "deg": int(p_u_fp.degree()) if not p_u_fp.is_zero else -1,
        "tail_in_ideal_mod_p": bool(divisibility_holds),
    }


def realize_atom(record: HabiroCompletionRecord, q_0: float) -> dict:
    """Compute realizations at every place for one atom."""
    realizations = [realize_archimedean(record, q_0)]
    for p in FINITE_PLACES:
        realizations.append(realize_finite_prime(record, p))
    return {
        "atom": record.atom_label,
        "Z": record.Z,
        "N": record.N,
        "deg_p_u": record.deg_p_u,
        "realizations": realizations,
    }


def main() -> int:
    if not INPUT_WITNESS.exists():
        print(f"ERROR: input witness not found at {INPUT_WITNESS}", file=sys.stderr)
        return 1

    witness = HabiroAtomicWitness.from_json(INPUT_WITNESS)
    q_0 = float(witness.parameters.get("q_0", 1.1099785955541805))

    per_atom = [realize_atom(record, q_0) for record in witness.records]

    overall_pass = all(
        rz["tail_in_ideal_mod_p"]
        for r in per_atom
        for rz in r["realizations"]
        if rz["place"].startswith("finite")
    )

    output = {
        "computation": "markov-substrate-realization",
        "description": (
            "Place-by-place realization of the Habiro Markov trace "
            "via the Lean MotivicSubstrate.realize map: Place.infty → ℝ "
            "(numerical at q_0), Place.finite(p) → 𝔽_p[u] (mod-p "
            "coefficient reduction).  Free consistency check: the "
            "tail_in_ideal axiom is re-verified in 𝔽_p[u]."
        ),
        "reference_blocks": [
            "def:motivic-substrate",
            "def:adelic-substrate",
            "prop:full-pole-structure-mass-trace",
        ],
        "lean_classes": [
            "qou:QOU.AlgebraicSubstrate.MotivicSubstrate",
            "qou:QOU.BraidKnot.HabiroCompletion",
        ],
        "input_witness": INPUT_WITNESS.name,
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q_0": q_0, "finite_places": FINITE_PLACES},
        "engine": "sympy.Poly over ZZ and GF(p)",
        "overall_pass": overall_pass,
        "results": per_atom,
    }

    with OUTPUT_WITNESS.open("w") as f:
        json.dump(output, f, indent=2)
        f.write("\n")

    status = "PASS" if overall_pass else "FAIL"
    print(f"markov_substrate_realizer: {status}")
    for r in per_atom:
        atom = r["atom"]
        infty = next((rz for rz in r["realizations"] if rz["place"] == "infty"), None)
        infty_val = infty.get("tr_M_at_q0") if infty else None
        finite_count = sum(
            1 for rz in r["realizations"] if rz["place"].startswith("finite") and rz["tail_in_ideal_mod_p"]
        )
        finite_total = len(FINITE_PLACES)
        print(
            f"  {atom:>24}  tr_M(q_0)={infty_val:.6e}   "
            f"{finite_count}/{finite_total} finite-place divisibility checks"
        )
    print(f"Wrote {OUTPUT_WITNESS}")
    return 0 if overall_pass else 2


if __name__ == "__main__":
    sys.exit(main())
