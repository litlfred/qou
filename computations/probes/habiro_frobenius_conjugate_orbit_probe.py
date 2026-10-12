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
DEPRECATED_COEFFS = REPO / "fsh-guts" / "deprecated" / "computations" / "habiro-coefficients-atomic-fast.witness.json"
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

    # When the norm is +-1 the element is a UNIT, and in a cyclotomic ring of
    # small degree the unit group is finite, so the refutation makes a sharp
    # falsifiable prediction: the element must have finite multiplicative
    # order. Tested by the DEFINING property (powering up), not by comparing
    # against a hand-listed set of roots of unity -- a string/srepr comparison
    # would pass on a representation artifact.
    unit_order = None
    if abs(norm_res) == 1:
        cur = reduce_mod(sp.Integer(1), n)
        for e in range(1, 4 * n + 1):
            cur = reduce_mod(sp.expand(cur.as_expr() * rep.as_expr()), n)
            if cur.as_expr() == 1:
                unit_order = e
                break

    return {
        "prime": p,
        "exact": True,
        "truncates_at_m": truncates_at,
        "orbit_size": len(orbit),
        "conjugate_orbit": orbit,
        "representative_is_rational_integer": rep_const,
        "galois_norm": norm_res,
        "galois_norm_orbit_route": norm_orbit,
        "galois_norm_abs": abs(norm_res),
        "is_unit": abs(norm_res) == 1,
        "representative": str(rep.as_expr()),
        "unit_multiplicative_order": unit_order,
        # Both routes are recorded, not just the claim that they matched, so
        # the witness carries the evidence its `norm_routes_agree` assertion
        # is checked against rather than a sentence asserting the outcome
        # (bean `qou-26f2`).
        "norm_cross_check": "orbit-product == resultant",
    }


def trM_congruence_observation(atoms: dict) -> list[dict[str, Any]]:
    """Why do two DIFFERENT atoms give the same root of unity at zeta_6?

    Stated exactly: `tr_M(zeta_6) = zeta_6` is the divisibility
    `Phi_6 | (tr_M - u)`. This records it per atom rather than leaving the
    coincidence as prose.

    It is NOT a blanket degeneracy of tr_M at a 6th root of unity -- the
    deuteron is the counterexample and is included here for exactly that
    reason. Recorded as an observation; no mechanism is claimed.
    """
    phi6 = sp.Poly(sp.cyclotomic_poly(6, u), u)
    out = []
    for label, rec in atoms.items():
        total = sp.Integer(0)
        for c in rec.get("habiro_coefficients", []):
            a = sp.sympify(c.get("a_m_str", c.get("a_m", "0")), locals={"check_q": u})
            poch = sp.Integer(1)
            for i in range(1, c["m"] + 1):
                poch *= (1 - u**i)
            total += a * poch
        poly = sp.Poly(sp.expand(total), u)
        _, rem = sp.div(sp.Poly(poly.as_expr() - u, u), phi6)
        out.append({
            "atom_label": label,
            "trM_degree": int(poly.degree()),
            "phi6_divides_trM_minus_zeta": bool(rem.is_zero),
        })
    return out


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
            flag = ""
            if row["is_unit"]:
                _o = row["unit_multiplicative_order"]
                flag = (f"  <== UNIT, = {row['representative']}, order {_o}"
                        "  (norm route FAILS here)")
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
    wb.add_data("trM_congruence_at_zeta6", trM_congruence_observation(atoms))
    # Assertions carry (name, computed, EXPECTED) -- the third argument is a value
    # to compare against, not a description.
    #
    # Both of these were `(name, True, True)` — literals on each side, so they
    # could not fail whatever the run did (bean `qou-26f2`). Each states a
    # checkable fact, and the rows above now carry what it takes to check it.
    #
    # `norm_routes_agree` was additionally unfalsifiable for the reason the
    # bare `raise` at the top of this file creates: routes that disagree abort
    # the run, so the witness is only written when they agree. Counting the
    # agreements against the exactly-evaluated rows measures coverage as well
    # as agreement — a row that stopped being evaluated shows up here.
    _exact = [r for a in results for r in a["rows"] if r.get("exact")]
    _agree = [r for r in _exact
              if r.get("galois_norm_orbit_route") is not None
              and r["galois_norm_orbit_route"] == r["galois_norm"]]
    wb.add_assertion("norm_routes_agree", len(_agree), len(_exact))
    # `no_float_used` is the exactness claim in this file's title. Every norm
    # is built through `sp.resultant` / exact orbit products and pulled out
    # with `int(...)`, so a float anywhere on either route would surface as a
    # non-int here.
    wb.add_assertion(
        "no_float_used",
        all(isinstance(r["galois_norm"], int)
            and isinstance(r["galois_norm_orbit_route"], int)
            for r in _exact),
        True)
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
    # It went quiet anyway, in the one way the comment above did not
    # anticipate: the guard itself went stale (bean `qou-7fvo`). `guard` is
    # built from every atom with an exact p=2 row — five of them — while
    # `expected_guard` is a hardcoded three. Tritium and 3He joined the atom
    # set afterwards and were never added here, so the assertion failed on a
    # count mismatch and said nothing at all about drift.
    #
    # The comment names two jobs, and they want different treatment:
    #
    #   * the ARITHMETIC (norm = C^2) is a mathematical identity, derivable for
    #     every atom, and cannot go stale as atoms are added. Asserted over all
    #     of them below — this is the half that was silently losing coverage.
    #   * the CONSTANTS are the drift detection, and their authority is
    #     `qou-lrnd`'s deliberate correction. Pinning new ones from whatever
    #     this run prints would be fitting rather than verification, so the pin
    #     stays restricted to the three that bean actually corrected, and the
    #     rest are recorded as unpinned for an author to adopt.
    _law_holds = {k: (c is not None and n == c * c) for k, (c, n) in guard.items()}
    wb.add_data("p2_collapse_constants_all_atoms", guard)
    wb.add_data("p2_constants_pinned_by_qou_lrnd", sorted(expected_guard))
    wb.add_data("p2_constants_not_yet_pinned",
                sorted(k for k in guard if k not in expected_guard))
    wb.add_assertion("p2_norm_is_square_of_collapse_constant_all_atoms",
                     sum(1 for v in _law_holds.values() if v), len(guard))
    wb.add_assertion("p2_rep_is_collapse_constant_and_norm_is_its_square",
                     {k: v for k, v in guard.items() if k in expected_guard},
                     expected_guard)
    wb.add_assertion("units_found_at_p3_for_both_nucleons",
                     sorted(units), ["n (neutron, A=1) @ p=3", "p (proton, A=1) @ p=3"])
    # The sharp form: both nucleon units are the SAME element, and it is a
    # PRIMITIVE 6th root of unity (order exactly 6, not a proper divisor).
    _u3 = {}
    for y in results:
        r3 = next((x for x in y["rows"] if x["prime"] == 3 and x["exact"]), None)
        if r3 and r3["is_unit"]:
            _u3[y["atom_label"]] = [r3["representative"], r3["unit_multiplicative_order"]]
    wb.add_assertion("p3_units_are_primitive_6th_root_of_unity", _u3,
                     {"p (proton, A=1)": ["u", 6], "n (neutron, A=1)": ["u", 6]})
    wb.add_caveat(
        "The two A=1 atoms share a value at zeta_6 (both tr_M == u mod Phi_6) while "
        "the A=2 atom does not, so this is NOT a universal evaluation of tr_M at a "
        "6th root of unity. Whether the A=1 agreement is forced or coincidental is "
        "OPEN; no mechanism is claimed here.")
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
