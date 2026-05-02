#!/usr/bin/env python3
"""Motivic-orbit relation analysis for Frobenius eigenvalues.

Reads `habiro-frobenius-probe.witness.json` (which now stores each
Frobenius value as its **exact polynomial representative** in
`Z[ζ_{2p}] = Z[u]/Φ_{2p}(u)`) and looks for relations among atoms:

  - Multiplicative: does `Frob_p(D) = Frob_p(p) · Frob_p(n)` hold?
    (would imply the deuteron motive factors as proton ⊗ neutron)
  - Sign / conjugacy: does `Frob_p(³He) = ±σ(Frob_p(³H))` for some
    Galois automorphism σ ∈ Gal(Q(ζ_{2p})/Q)?
  - Per-prime weight: |Frob_p|² when interpreted via Weil — hints
    at the motive's pure-piece weight at p.

When a relation holds, that's evidence the underlying motive
factors / has a specific Galois structure. When it doesn't, the
motive is genuinely "new" at that level.

This is **R6 step 3 reconnaissance** — the next step toward the
explicit `MotivicGaloisCharacter` instance for the QOU substrate.

Usage:
    python3 folio-assistant/computations/habiro_motivic_orbit_analysis.py

Output: `habiro-motivic-orbit-relations.witness.json`
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from math import gcd
from pathlib import Path
from typing import Any

import sympy as sp

HERE = Path(__file__).parent
WITNESS_IN = HERE / "habiro-frobenius-probe.witness.json"
WITNESS_OUT = HERE / "habiro-motivic-orbit-relations.witness.json"


def load_frob_polys() -> dict[str, dict[int, sp.Expr]]:
    """Load Frob_p polynomial reps from the probe witness.
    Returns: {atom_label: {prime: sp.Expr in u}}"""
    data = json.loads(WITNESS_IN.read_text())
    u = sp.Symbol("u")
    out: dict[str, dict[int, sp.Expr]] = {}
    for atom in data["atoms"]:
        label = atom["atom_label"]
        out[label] = {}
        for r in atom["frobenius"]:
            if not r.get("frob_p_is_exact", False):
                continue
            expr = sp.sympify(r["frob_p_in_Z_zeta_str"], locals={"u": u})
            out[label][int(r["prime"])] = expr
    return out


def reduce_in_ring(expr: sp.Expr, n: int, u: sp.Symbol) -> sp.Poly:
    phi_n = sp.Poly(sp.cyclotomic_poly(n, u), u)
    p = sp.Poly(sp.expand(expr), u)
    if p.is_zero:
        return sp.Poly(0, u)
    _, rem = p.div(phi_n)
    return rem


def galois_orbit(expr: sp.Expr, n: int, u: sp.Symbol) -> list[sp.Expr]:
    """Return the Galois orbit of `expr ∈ Z[ζ_n]` under
    Gal(Q(ζ_n)/Q) ≅ (Z/nZ)*.
    """
    ks = [k for k in range(1, n) if gcd(k, n) == 1]
    out = []
    for k in ks:
        sub = expr.subs(u, u ** k)
        rep = reduce_in_ring(sub, n, u)
        out.append(rep.as_expr())
    return out


def in_galois_orbit(target: sp.Expr, candidate: sp.Expr,
                     n: int, u: sp.Symbol) -> tuple[bool, int | None]:
    """Check whether `candidate` is in the Galois orbit of `target`.
    Returns (is_in_orbit, k_value-or-None).
    """
    target_rep = reduce_in_ring(target, n, u)
    candidate_rep = reduce_in_ring(candidate, n, u)
    if (target_rep - candidate_rep).is_zero:
        return True, 1
    for k in range(1, n):
        if gcd(k, n) != 1:
            continue
        sub = target.subs(u, u ** k)
        sub_rep = reduce_in_ring(sub, n, u)
        if (sub_rep - candidate_rep).is_zero:
            return True, k
    return False, None


def check_multiplicative(frob_a: sp.Expr, frob_b: sp.Expr,
                          frob_ab: sp.Expr,
                          n: int, u: sp.Symbol) -> dict[str, Any]:
    """Test whether Frob_p(ab) = Frob_p(a) · Frob_p(b) in Z[ζ_n]."""
    product = reduce_in_ring(frob_a * frob_b, n, u)
    target = reduce_in_ring(frob_ab, n, u)
    diff = reduce_in_ring((product - target).as_expr(), n, u)
    return {
        "exact_match": diff.is_zero,
        "product_str": str(product.as_expr()),
        "target_str": str(target.as_expr()),
        "diff_str": str(diff.as_expr()),
    }


def main() -> int:
    if not WITNESS_IN.exists():
        print(f"ERROR: {WITNESS_IN.name} not found")
        return 1

    frobs = load_frob_polys()
    u = sp.Symbol("u")

    print("=" * 72)
    print("R6 step-3 reconnaissance: motivic-orbit relations on Frob_p")
    print("=" * 72)
    print(f"  Atoms: {list(frobs.keys())}")
    print()

    # Identify proton, neutron, D, T, ³He labels.
    proton_lbl = next((k for k in frobs if k.startswith("p ")), None)
    neutron_lbl = next((k for k in frobs if k.startswith("n ")), None)
    D_lbl = next((k for k in frobs if k.startswith("D ")), None)
    T_lbl = next((k for k in frobs if k.startswith("T ")), None)
    He3_lbl = next((k for k in frobs if k.startswith("3He")), None)

    relations: list[dict[str, Any]] = []
    primes = sorted({p for atom in frobs.values() for p in atom})

    # Test 1: D = p · n multiplicative relation.
    if proton_lbl and D_lbl:
        print("─── Test 1: Frob_p(D) =? Frob_p(proton) · Frob_p(neutron) ───")
        for p in primes:
            n_2p = 2 * p
            f_p = frobs.get(proton_lbl, {}).get(p)
            f_n = (frobs.get(neutron_lbl, {}).get(p)
                   if neutron_lbl else None)
            f_D = frobs.get(D_lbl, {}).get(p)
            if f_p is None or f_D is None:
                continue
            if f_n is None:
                # In the absence of neutron data, test if Frob_p(D)
                # is just Frob_p(proton) — a degenerate factoring.
                test = check_multiplicative(f_p, sp.Integer(1), f_D, n_2p, u)
                if test["exact_match"]:
                    print(f"  p={p}: Frob(D) = Frob(p)  → degenerate factor")
                continue
            test = check_multiplicative(f_p, f_n, f_D, n_2p, u)
            mark = "✓" if test["exact_match"] else "·"
            print(f"  p={p}: {mark}  Frob(D) - Frob(p)·Frob(n) = "
                  f"{test['diff_str'][:60]}")
            relations.append({
                "kind": "multiplicative",
                "atom": D_lbl,
                "factors": [proton_lbl, neutron_lbl or "(no n)"],
                "prime": p,
                "exact_match": test["exact_match"],
                "diff": test["diff_str"],
            })
        print()

    # Test 2: ³He vs ³H Galois conjugacy.
    if T_lbl and He3_lbl:
        print("─── Test 2: Frob_p(³He) ∈ Galois orbit of Frob_p(³H)? ───")
        for p in primes:
            n_2p = 2 * p
            f_T = frobs.get(T_lbl, {}).get(p)
            f_He3 = frobs.get(He3_lbl, {}).get(p)
            if f_T is None or f_He3 is None:
                continue
            in_orbit, k = in_galois_orbit(f_T, f_He3, n_2p, u)
            mark = "✓" if in_orbit else "·"
            k_str = f"σ_{k}" if k is not None else "no"
            print(f"  p={p}: {mark}  Frob(³He) = {k_str}(Frob(³H))?")
            relations.append({
                "kind": "galois_conjugacy",
                "atom": He3_lbl,
                "conjugate_of": T_lbl,
                "prime": p,
                "in_orbit": in_orbit,
                "galois_index_k": k,
            })
        print()

        # Also check sign-conjugacy: ³He = -σ(³H)?
        print("─── Test 2b: Frob_p(³He) = −σ(Frob_p(³H))? ───")
        for p in primes:
            n_2p = 2 * p
            f_T = frobs.get(T_lbl, {}).get(p)
            f_He3 = frobs.get(He3_lbl, {}).get(p)
            if f_T is None or f_He3 is None:
                continue
            in_orbit, k = in_galois_orbit(-f_T, f_He3, n_2p, u)
            mark = "✓" if in_orbit else "·"
            k_str = f"σ_{k}" if k is not None else "no"
            print(f"  p={p}: {mark}  Frob(³He) = -{k_str}(Frob(³H))?")
            relations.append({
                "kind": "sign_galois_conjugacy",
                "atom": He3_lbl,
                "conjugate_of": T_lbl,
                "prime": p,
                "in_orbit": in_orbit,
                "galois_index_k": k,
            })
        print()

    # Test 3: per-prime weight signature (Weil bound) — abs of
    # the orbit values; uniform abs ⇒ pure motive of single weight.
    print("─── Test 3: per-(atom, prime) Weil weight signature ───")
    weight_table: list[dict[str, Any]] = []
    for atom_lbl, atom_frobs in frobs.items():
        for p, frob_expr in atom_frobs.items():
            n_2p = 2 * p
            orbit = galois_orbit(frob_expr, n_2p, u)
            # Numerical evaluate each.
            zeta = sp.exp(2 * sp.pi * sp.I / n_2p)
            orbit_abs = []
            for o in orbit:
                v = complex(sp.N(o.subs(u, zeta), 30))
                orbit_abs.append(abs(v))
            if not orbit_abs:
                continue
            mx = max(orbit_abs)
            mn = min(orbit_abs)
            spread = (mx - mn) / mx if mx > 1e-20 else 0
            from math import log
            inferred_weight = (
                2 * log(mx) / log(p) if mx > 1e-20 else None
            )
            is_pure = spread < 1e-6
            weight_table.append({
                "atom": atom_lbl, "prime": p,
                "orbit_max_abs": mx,
                "orbit_min_abs": mn,
                "orbit_spread": spread,
                "inferred_weight": inferred_weight,
                "is_pure_motive": is_pure,
            })
    print(f"  pure-motive count: "
          f"{sum(1 for r in weight_table if r['is_pure_motive'])} of "
          f"{len(weight_table)} (atom, prime) pairs")
    print()

    out = {
        "computation": "habiro-motivic-orbit-relations",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Motivic-orbit relation analysis on the exact-algebraic "
            "Frobenius eigenvalues from habiro-frobenius-probe. Tests "
            "(a) multiplicative factoring D = p ⊗ n, (b) Galois "
            "conjugacy ³He ~ σ(³H), (c) per-(atom, prime) Weil-purity "
            "signature. All relations are checked in exact ring "
            "arithmetic in Z[ζ_{2p}] = Z[u]/Φ_{2p}(u)."
        ),
        "reference_blocks": [
            "def:motivic-galois-character",
            "prop:motivic-perpetual-obstruction",
        ],
        "input_witness": WITNESS_IN.name,
        "atoms": list(frobs.keys()),
        "primes": primes,
        "relations": relations,
        "weight_signature": weight_table,
        "summary": {
            "n_relations": len(relations),
            "n_multiplicative_matches": sum(
                1 for r in relations
                if r["kind"] == "multiplicative" and r.get("exact_match")
            ),
            "n_galois_conjugacy_matches": sum(
                1 for r in relations
                if r["kind"] == "galois_conjugacy" and r.get("in_orbit")
            ),
            "n_sign_conjugacy_matches": sum(
                1 for r in relations
                if r["kind"] == "sign_galois_conjugacy" and r.get("in_orbit")
            ),
            "n_pure_motives": sum(
                1 for r in weight_table if r["is_pure_motive"]
            ),
        },
    }
    WITNESS_OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"Wrote: {WITNESS_OUT.name}")
    print(f"Summary: {out['summary']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
