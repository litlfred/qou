#!/usr/bin/env python3


# polynomial_q_not_applicable: mpmath/numerical-only output; sympy use is intermediate or absent.
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

import argparse
import sys
from pathlib import Path

import sympy as sp
from sympy import GF, Integer, Symbol

sys.path.insert(0, str(Path(__file__).parent))
from habiro_types import HabiroAtomicWitness, HabiroCompletionRecord  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q as CANONICAL_Q  # noqa: E402


HERE = Path(__file__).parent
import _path_bridge as _wp  # noqa: E402 — bridge namespace was deleted at end of shim; re-import for witness_path lookup
INPUT_WITNESS = _wp.witness_path("habiro-coefficients-atomic.witness.json", HERE)  # was: HERE / "..." — moved cross-cluster, use bridge resolver

FINITE_PLACES = [2, 3, 5, 7, 11, 13]

# The Markov-trace convention used in the upstream witness.  The
# `claude/continue-pr-442-DJRWm` audit (now merging via PR #442+
# follow-ups) flags Plancherel vs Wenzl-Schur as a critical
# distinction: the two conventions assign different λ-weights
# `w_λ(q)` in the trace decomposition `tr_M = Σ_λ w_λ(q) χ^λ_q(T_w)`,
# and consume different `tr_M(q_0)` values.  This realizer evaluates
# whatever polynomial it is handed; the flag records the convention
# of the upstream producer so downstream consumers know which trace
# the realizations correspond to.
KNOWN_CONVENTIONS = ("plancherel", "wenzl-schur")
DEFAULT_CONVENTION = "wenzl-schur"


def q_pochhammer_poly(N: int, u: Symbol, domain) -> sp.Poly:
    """`(u;u)_N = ∏_{k=1..N} (1 − u^k)` as a sympy Poly over `domain[u]`."""
    expr = Integer(1)
    for k in range(1, N + 1):
        expr *= (1 - u ** k)
    return sp.Poly(sp.expand(expr), u, domain=domain)


def parse_poly_zz(s: str, u: Symbol) -> sp.Poly:
    return sp.Poly(sp.expand(sp.sympify(s, locals={"check_q": u, "u": u})), u, domain="ZZ")


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
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0] if __doc__ else "")
    parser.add_argument(
        "--convention",
        choices=KNOWN_CONVENTIONS,
        default=DEFAULT_CONVENTION,
        help=(
            "Markov-trace convention assumed for the upstream witness. "
            "Recorded in the output for downstream consumers; this realizer "
            "does not re-run the trace computation."
        ),
    )
    args = parser.parse_args()

    if not INPUT_WITNESS.exists():
        print(f"ERROR: input witness not found at {INPUT_WITNESS}", file=sys.stderr)
        return 1

    witness = HabiroAtomicWitness.from_json(INPUT_WITNESS)
    # Evaluate at the canonical substrate parameter q_parameter.Q (the
    # single source of truth), NOT the q_0 cached in the input witness.
    # The cached value goes stale across a substrate re-pin (e.g. the
    # 2026-05-28 proton-anchor re-pin); a stale cached q_0 here vs the
    # canonical Q used by term6_full_pole_sum.py was the cause of the
    # markov_pipeline_cross_validator ~1e-7 disagreement (q_0 drift of
    # ~1.3e-8 amplified by tr_M's q-sensitivity).
    q_0 = float(CANONICAL_Q)
    witness_q0 = witness.parameters.get("q_0")
    if witness_q0 is not None and abs(float(witness_q0) - q_0) > 1e-12:
        print(
            f"  NOTE: input witness q_0={float(witness_q0)!r} is stale vs "
            f"canonical q_parameter.Q={q_0!r}; evaluating at canonical value.",
            file=sys.stderr,
        )

    per_atom = [realize_atom(record, q_0) for record in witness.records]

    w = WitnessBuilder("markov-substrate-realization", engine="sympy")
    w.set_description(
        "Place-by-place realization of the Habiro Markov trace via "
        "the Lean MotivicSubstrate.realize map: Place.infty → ℝ "
        "(numerical at q_0), Place.finite(p) → 𝔽_p[u] (mod-p "
        "coefficient reduction).  Free consistency check: the "
        "tail_in_ideal axiom is re-verified in 𝔽_p[u]."
    )
    w.set_content_block("prop:full-pole-structure-mass-trace")
    w.add_parameter("q_0", q_0)
    w.add_parameter("finite_places", FINITE_PLACES)
    w.add_parameter("convention", args.convention)
    w.add_data("lean_classes", [
        "qou:QOU.AlgebraicSubstrate.MotivicSubstrate",
        "qou:QOU.BraidKnot.HabiroCompletion",
    ])
    w.add_data("reference_blocks", [
        "def:motivic-substrate",
        "def:adelic-substrate",
        "prop:full-pole-structure-mass-trace",
    ])
    w.add_data("input_witness", INPUT_WITNESS.name)
    w.add_data("results", per_atom)

    # Per-atom-per-prime assertions for tail_in_ideal mod p (the
    # substantive empirical claim of the realizer).
    for r in per_atom:
        for rz in r["realizations"]:
            if rz["place"].startswith("finite"):
                w.add_assertion(
                    f"tail_in_ideal_mod_p[{r['atom']}/{rz['place']}]",
                    computed=bool(rz["tail_in_ideal_mod_p"]),
                    expected=True,
                )

    overall_pass = all(a.passed for a in w.assertions)
    w.save()

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
        infty_repr = (
            f"{infty_val:.6e}" if isinstance(infty_val, (int, float))
            else (infty.get("error") if infty else "missing")
        )
        print(
            f"  {atom:>24}  tr_M(q_0)={infty_repr}   "
            f"{finite_count}/{finite_total} finite-place divisibility checks"
        )
    return 0 if overall_pass else 2


if __name__ == "__main__":
    sys.exit(main())
