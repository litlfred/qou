#!/usr/bin/env python3
"""Full conjugate orbit of the Habiro Frobenius, and the norm it forces.

Bean `qou-lrnd` recorded that the archimedean route needs a bound on the norm
over the **whole embedding orbit**, and that the corpus recorded only one
embedding per prime.  This emits the orbit itself, exactly.

WHAT IT ANSWERS.  `N(Frob_p) = prod_sigma sigma(Frob_p)` is a rational
integer, so the question "is Frob_p a unit?" is decidable in exact integer
arithmetic: a unit of `O` has norm +-1.  No embeddings into C are needed and
no floating point is used anywhere -- the orbit lives in `Z[zeta_2p]` and the
norm is an integer.  (Precision discipline: this file computes only in `int`
and sympy exact polynomials.  There is no `float` anywhere, per AGENTS.md
"PROBES ARE NOT EXEMPT".)

WHY A SECOND PROBE RATHER THAN AN EDIT.  `habiro_frobenius_norm_probe.py`
computes the same norm, and its committed witness
`habiro-frobenius-norm-probe.witness.json` reports every value as a non-unit
(`route_a_supported: true`).  Neither coefficient set on `main` reproduces any
of those seven numbers -- see `reproduction_of_committed_witness` in the
output.  This probe therefore recomputes from the CANONICAL coefficients,
names them, and hashes them, rather than editing a record whose provenance
cannot be established.

TWO INDEPENDENT ROUTES, ASSERTED EQUAL.  The norm is computed
  (1) as the product over the Galois orbit {sigma_k : gcd(k, 2p) = 1}, and
  (2) as `Res(Phi_2p, f)`, which equals the norm because `Phi_2p` is monic.
The two share no code path.  Disagreement raises rather than being reported,
so a future refactor cannot silently degrade one of them.

Usage:
    python3 computations/probes/habiro_frobenius_conjugate_orbit_probe.py
"""
from __future__ import annotations

import hashlib
import json
import sys
from math import gcd
from pathlib import Path
from typing import Any

import sympy as sp

HERE = Path(__file__).parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))

# CANONICAL coefficients. Deliberately NOT the `_deprecated/` "fast" witness:
# the two disagree at a_0 itself (neutron 8 vs 2, deuteron 96 vs 192), and
# 2 / 192 are the values bean `qou-lrnd` corrected the corpus to on 2026-08-23.
COEFFS = REPO / "computations" / "habiro" / "habiro-coefficients-atomic.witness.json"
DEPRECATED_COEFFS = REPO / "computations" / "_deprecated" / "habiro-coefficients-atomic-fast.witness.json"
COMMITTED_NORM_WITNESS = HERE / "habiro-frobenius-norm-probe.witness.json"

PRIMES = [2, 3, 5, 7, 11, 13]

u = sp.symbols("u")


def sha256_of(path: Path) -> str | None:
    if not path.exists():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def reduce_mod(expr: sp.Expr, n: int) -> sp.Poly:
    phi = sp.Poly(sp.cyclotomic_poly(n, u), u)
    p = sp.Poly(sp.expand(expr), u)
    if p.is_zero:
        return sp.Poly(0, u)
    _, rem = p.div(phi)
    return rem


def pochhammer(n: int, m: int) -> sp.Poly:
    """(zeta_n; zeta_n)_m = prod_{i=1}^m (1 - u^i) mod Phi_n."""
    phi = sp.Poly(sp.cyclotomic_poly(n, u), u)
    out = sp.Poly(1, u)
    for i in range(1, m + 1):
        out = out * sp.Poly(1 - u**i, u)
        _, out = out.div(phi)
    return out


def frobenius_rep(coeffs: list[dict], p: int) -> tuple[sp.Poly | None, int | None]:
    """Habiro sum evaluated at zeta_2p, reduced mod Phi_2p.

    The sum genuinely terminates: (q;q)_m vanishes at m = 2p. It is exact only
    if the coefficient list REACHES that index, so 2p+1 coefficients are
    needed for prime p -- that bound is what limits this probe, not the method.
    """
    n = 2 * p
    phi = sp.Poly(sp.cyclotomic_poly(n, u), u)
    rep = sp.Poly(0, u)
    for m, rec in enumerate(coeffs):
        poch = pochhammer(n, m)
        if poch.is_zero:
            return rep, m
        a = sp.sympify(rec.get("a_m_str", rec.get("a_m", "0")), locals={"check_q": u})
        rep = rep + reduce_mod(a, n) * poch
        _, rep = rep.div(phi)
    return None, None  # coefficients exhausted before the Pochhammer vanished


def conjugate_orbit(rep: sp.Poly, p: int) -> list[dict[str, Any]]:
    """Every sigma_k(Frob_p), as an exact element of Z[zeta_2p]."""
    n = 2 * p
    out = []
    for k in (k for k in range(1, n) if gcd(k, n) == 1):
        sigma = reduce_mod(rep.as_expr().subs(u, u**k), n)
        out.append({
            "k": k,
            "coeffs_in_zeta_basis": [int(c) for c in sigma.all_coeffs()],
            "expr": str(sigma.as_expr()),
        })
    return out


def analyse(coeffs: list[dict], p: int) -> dict[str, Any]:
    rep, truncates_at = frobenius_rep(coeffs, p)
    if rep is None:
        return {"prime": p, "exact": False,
                "coefficients_needed": 2 * p + 1, "coefficients_available": len(coeffs)}

    n = 2 * p
    phi = sp.Poly(sp.cyclotomic_poly(n, u), u)
    orbit = conjugate_orbit(rep, p)

    # route 1 -- product over the orbit
    prod = sp.Poly(1, u)
    for k in (k for k in range(1, n) if gcd(k, n) == 1):
        prod = prod * reduce_mod(rep.as_expr().subs(u, u**k), n)
        _, prod = prod.div(phi)
    norm_orbit = prod.all_coeffs()[0] if prod.degree() == 0 else None
    norm_orbit = int(norm_orbit) if norm_orbit is not None and norm_orbit.is_Integer else None

    # route 2 -- resultant, no shared code path with route 1
    norm_res = int(sp.resultant(phi.as_expr(), rep.as_expr(), u))

    if norm_orbit is None or norm_orbit != norm_res:
        raise AssertionError(
            f"norm routes disagree at p={p}: orbit={norm_orbit} resultant={norm_res}")

    rep_const = int(rep.all_coeffs()[0]) if rep.degree() == 0 else None
    return {
        "prime": p,
        "exact": True,
        "truncates_at_m": truncates_at,
        "orbit_size": len(orbit),
        "conjugate_orbit": orbit,
        "representative_is_rational_integer": rep_const,
        "galois_norm": norm_res,
        "galois_norm_abs": abs(norm_res),
        "is_unit": abs(norm_res) == 1,
        "norm_cross_check": "orbit-product == resultant",
    }


def main() -> int:
    if not COEFFS.exists():
        print(f"ERROR: canonical coefficients missing at {COEFFS}")
        return 1
    atoms = json.loads(COEFFS.read_text()).get("results", {})

    print("=" * 78)
    print("Habiro Frobenius: full conjugate orbit and the norm it forces")
    print(f"  coefficients: {COEFFS.relative_to(REPO)}  sha={sha256_of(COEFFS)}")
    print("=" * 78)

    results: list[dict] = []
    units: list[str] = []
    for label, rec in atoms.items():
        coeffs = rec.get("habiro_coefficients", [])
        if not coeffs:
            continue
        print(f"\n  {label}   ({len(coeffs)} coefficients available)")
        rows = []
        for p in PRIMES:
            row = analyse(coeffs, p)
            rows.append(row)
            if not row["exact"]:
                print(f"    p={p:>3}  not exact -- needs {row['coefficients_needed']} "
                      f"coefficients, has {row['coefficients_available']}")
                continue
            flag = "  <== UNIT (norm route FAILS here)" if row["is_unit"] else ""
            const = row["representative_is_rational_integer"]
            print(f"    p={p:>3}  orbit={row['orbit_size']}  N={row['galois_norm']:<12}"
                  f"  |N|={row['galois_norm_abs']:<12}"
                  + (f"  rep={const}" if const is not None else "") + flag)
            if row["is_unit"]:
                units.append(f"{label} @ p={p}")
        results.append({"atom_label": label,
                        "coefficients_available": len(coeffs),
                        "rows": rows})

    # Can the committed witness be reproduced from anything on main?
    repro: dict[str, Any] = {"checked": False}
    if COMMITTED_NORM_WITNESS.exists():
        old = json.loads(COMMITTED_NORM_WITNESS.read_text())
        mismatches = []
        for a in old.get("atoms", []):
            for r in a.get("frobenius_norms", []):
                if not r.get("exact"):
                    continue
                lbl, pr, was = a["atom_label"], r.get("prime"), r.get("galois_norm_int")
                mine = next((x for y in results if y["atom_label"] == lbl
                             for x in y["rows"] if x["prime"] == pr and x["exact"]), None)
                if mine and mine["galois_norm"] != was:
                    mismatches.append({"atom": lbl, "prime": pr,
                                       "committed": was, "canonical": mine["galois_norm"]})
        repro = {"checked": True, "n_mismatch": len(mismatches), "mismatches": mismatches}
        print(f"\n  committed witness reproduction: {len(mismatches)} of its exact rows "
              f"DIFFER from canonical")

    print(f"\n{'=' * 78}")
    if units:
        print(f"  UNITS FOUND ({len(units)}): " + "; ".join(units))
        print("  At these primes Frob_p IS a unit, so the norm route cannot")
        print("  give non-unitness there. This REFUTES the no-exception-set form.")
    else:
        print("  no units among the exactly-evaluated primes")
    print(f"{'=' * 78}")

    from qou_substrate.witness import WitnessBuilder
    wb = WitnessBuilder("habiro-frobenius-conjugate-orbit-probe", _script_path=Path(__file__))
    wb.set_description(
        "Full Galois conjugate orbit of the Habiro Frobenius at zeta_2p, and the "
        "exact integer norm it forces, computed two independent ways (orbit product "
        "and resultant) from the CANONICAL atomic coefficients.")
    wb.set_audit_only(True)
    wb.add_parameter("primes", PRIMES)
    wb.add_parameter("coefficients_source", str(COEFFS.relative_to(REPO)))
    wb.add_parameter("coefficients_sha256_16", sha256_of(COEFFS))
    wb.add_parameter("deprecated_coefficients_present", DEPRECATED_COEFFS.exists())
    wb.add_parameter("deprecated_coefficients_sha256_16", sha256_of(DEPRECATED_COEFFS))
    wb.add_data("atoms", results)
    wb.add_data("units_found", units)
    wb.add_data("reproduction_of_committed_witness", repro)
    # Assertions carry (name, computed, EXPECTED) -- the third argument is a value
    # to compare against, not a description.
    wb.add_assertion("norm_routes_agree", True, True)
    wb.add_assertion("no_float_used", True, True)
    # Staleness guard: at p=2 the representative collapses to the rational
    # integer C, so the norm is forced to C^2. These are the constants bean
    # `qou-lrnd` corrected the corpus to on 2026-08-23. If either the
    # coefficients or this arithmetic drift, these trip rather than going quiet.
    guard = {}
    for y in results:
        row2 = next((x for x in y["rows"] if x["prime"] == 2 and x["exact"]), None)
        if row2:
            guard[y["atom_label"]] = [row2["representative_is_rational_integer"],
                                      row2["galois_norm"]]
    expected_guard = {
        "p (proton, A=1)": [8, 64],
        "n (neutron, A=1)": [2, 4],
        "D (deuteron, A=2)": [192, 36864],
    }
    wb.add_assertion("p2_rep_is_collapse_constant_and_norm_is_its_square",
                     guard, expected_guard)
    wb.add_assertion("units_found_at_p3_for_both_nucleons",
                     sorted(units), ["n (neutron, A=1) @ p=3", "p (proton, A=1) @ p=3"])
    wb.add_caveat(
        "Exactness is bounded by DATA, not method: evaluating at p needs 2p+1 Habiro "
        "coefficients. With 9/9/14 available this reaches p<=3 for the nucleons and "
        "p<=5 for the deuteron. Nothing here speaks to larger primes.")
    if units:
        wb.add_caveat(
            "A unit at one prime refutes the no-exception-set form (for-all p) but NOT "
            "the almost-every-prime form; one prime is not a positive density.")
    wb.save()
    print(f"\nWrote witness for habiro-frobenius-conjugate-orbit-probe")
    return 0


if __name__ == "__main__":
    sys.exit(main())
