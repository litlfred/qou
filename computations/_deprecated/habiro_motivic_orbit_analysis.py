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
    python3 computations/habiro_motivic_orbit_analysis.py

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
            # Use the numerator field (always defined and integer-poly).
            # The full tr_M(ζ_{2p}) = num/denom is in Q(ζ_{2p}) but
            # only in Z[ζ_{2p}] when denom is a unit there — typically
            # not the case for Markov traces. Working with the
            # numerator preserves the substantive motivic structure.
            field = r.get("frob_num_in_Z_zeta_str") or r.get("frob_p_in_Z_zeta_str")
            expr = sp.sympify(field, locals={"u": u})
            out[label][int(r["prime"])] = expr
    return out


def reduce_in_ring(expr: sp.Expr, n: int, u: sp.Symbol) -> sp.Poly:
    phi_n = sp.Poly(sp.cyclotomic_poly(n, u), u)
    p = sp.Poly(sp.expand(expr), u)
    if p.is_zero:
        return sp.Poly(0, u)
    _, rem = p.div(phi_n)
    return rem


def cyclotomic_pochhammer_in_ring(n: int, m: int,
                                    u: sp.Symbol) -> sp.Poly:
    """(ζ_n; ζ_n)_m = ∏_{i=1}^{m} (1 − ζ_n^i) in Z[ζ_n] = Z[u]/Φ_n(u)."""
    result = sp.Poly(1, u)
    phi_n = sp.Poly(sp.cyclotomic_poly(n, u), u)
    for i in range(1, m + 1):
        factor = sp.Poly(1, u) - sp.Poly(u ** i, u)
        result = result * factor
        _, result = result.div(phi_n)
    return result


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
    """Test whether Frob_p(ab) = Frob_p(a) · Frob_p(b) in Z[ζ_n].

    Also returns the **residue** `ε = Frob(ab) − Frob(a)·Frob(b)`,
    its Galois TRACE (rational integer if ε ∈ Z[ζ_n]), and the
    residue's degree. The field is named `residue_galois_norm_int`
    for historical compatibility, but the value computed is the
    SUM of conjugates (= trace), NOT the product (= norm).
    """
    product = reduce_in_ring(frob_a * frob_b, n, u)
    target = reduce_in_ring(frob_ab, n, u)
    diff = reduce_in_ring((product - target).as_expr(), n, u)
    # Compute the Galois TRACE of the residue:
    #   Tr(ε) = Σ_{k coprime to n} σ_k(ε)
    # (sum of conjugates, NOT product = norm). Use `galois_orbit`
    # for per-term reduction modulo Φ_n (avoids expression
    # explosion — for higher conductors n, the un-reduced sum can
    # grow combinatorially before final reduction).
    diff_expr = diff.as_expr()
    orbit_terms = galois_orbit(diff_expr, n, u)
    galois_norm = reduce_in_ring(sum(orbit_terms), n, u)
    norm_int = (
        int(galois_norm.all_coeffs()[0]) if galois_norm.degree() == 0
        and galois_norm.all_coeffs()
        and galois_norm.all_coeffs()[0].is_Integer
        else None
    )
    return {
        "exact_match": diff.is_zero,
        "product_str": str(product.as_expr()),
        "target_str": str(target.as_expr()),
        "residue_str": str(diff.as_expr()),
        "residue_degree": int(diff.degree()) if not diff.is_zero else 0,
        "residue_galois_norm_int": norm_int,
        "residue_is_galois_stable": norm_int is not None,
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
            stable_mark = ("[stable, N=" + str(test["residue_galois_norm_int"]) + "]"
                           if test["residue_is_galois_stable"] else "[non-stable]")
            print(f"  p={p}: {mark}  ε_p(D) = "
                  f"{test['residue_str'][:60]}  {stable_mark}")
            relations.append({
                "kind": "multiplicative",
                "atom": D_lbl,
                "factors": [proton_lbl, neutron_lbl or "(no n)"],
                "prime": p,
                "exact_match": test["exact_match"],
                "residue": test["residue_str"],
                "residue_galois_norm": test["residue_galois_norm_int"],
                "residue_is_galois_stable": test["residue_is_galois_stable"],
            })
        print()

    # Test 1b: T = D ⊗ n  (composition of deuteron + neutron).
    if D_lbl and neutron_lbl and T_lbl:
        print("─── Test 1b: Frob_p(T) =? Frob_p(D) · Frob_p(neutron) ───")
        for p in primes:
            n_2p = 2 * p
            f_D = frobs.get(D_lbl, {}).get(p)
            f_n = frobs.get(neutron_lbl, {}).get(p)
            f_T = frobs.get(T_lbl, {}).get(p)
            if f_D is None or f_n is None or f_T is None:
                continue
            test = check_multiplicative(f_D, f_n, f_T, n_2p, u)
            mark = "✓" if test["exact_match"] else "·"
            stable_mark = ("[stable, N=" + str(test["residue_galois_norm_int"]) + "]"
                           if test["residue_is_galois_stable"] else "[non-stable]")
            print(f"  p={p}: {mark}  ε_p(T) = "
                  f"{test['residue_str'][:60]}  {stable_mark}")
            relations.append({
                "kind": "multiplicative",
                "atom": T_lbl,
                "factors": [D_lbl, neutron_lbl],
                "prime": p,
                "exact_match": test["exact_match"],
                "residue": test["residue_str"],
                "residue_galois_norm": test["residue_galois_norm_int"],
                "residue_is_galois_stable": test["residue_is_galois_stable"],
            })
        print()

    # Test 1c: ³He = D ⊗ p.
    if D_lbl and proton_lbl and He3_lbl:
        print("─── Test 1c: Frob_p(³He) =? Frob_p(D) · Frob_p(proton) ───")
        for p in primes:
            n_2p = 2 * p
            f_D = frobs.get(D_lbl, {}).get(p)
            f_p = frobs.get(proton_lbl, {}).get(p)
            f_He = frobs.get(He3_lbl, {}).get(p)
            if f_D is None or f_p is None or f_He is None:
                continue
            test = check_multiplicative(f_D, f_p, f_He, n_2p, u)
            mark = "✓" if test["exact_match"] else "·"
            stable_mark = ("[stable, N=" + str(test["residue_galois_norm_int"]) + "]"
                           if test["residue_is_galois_stable"] else "[non-stable]")
            print(f"  p={p}: {mark}  ε_p(³He) = "
                  f"{test['residue_str'][:60]}  {stable_mark}")
            relations.append({
                "kind": "multiplicative",
                "atom": He3_lbl,
                "factors": [D_lbl, proton_lbl],
                "prime": p,
                "exact_match": test["exact_match"],
                "residue": test["residue_str"],
                "residue_galois_norm": test["residue_galois_norm_int"],
                "residue_is_galois_stable": test["residue_is_galois_stable"],
            })
        print()

    # Test 1d: residue comparison T vs ³He.
    if T_lbl and He3_lbl and D_lbl:
        print("─── Test 1d: ε_p(T) − ε_p(³He) — isobaric mirror residue gap ───")
        for p in primes:
            n_2p = 2 * p
            f_D = frobs.get(D_lbl, {}).get(p)
            f_p = frobs.get(proton_lbl, {}).get(p) if proton_lbl else None
            f_n = frobs.get(neutron_lbl, {}).get(p) if neutron_lbl else None
            f_T = frobs.get(T_lbl, {}).get(p)
            f_He = frobs.get(He3_lbl, {}).get(p)
            if not all([f_D, f_p, f_n, f_T, f_He]):
                continue
            eps_T = reduce_in_ring(f_T - f_D * f_n, n_2p, u).as_expr()
            eps_He = reduce_in_ring(f_He - f_D * f_p, n_2p, u).as_expr()
            gap = reduce_in_ring(eps_T - eps_He, n_2p, u)
            print(f"  p={p}: ε_T - ε_³He = {str(gap.as_expr())[:60]}")
            relations.append({
                "kind": "isobaric_mirror_residue_gap",
                "prime": p,
                "epsilon_T": str(eps_T),
                "epsilon_He3": str(eps_He),
                "gap": str(gap.as_expr()),
                "gap_is_zero": gap.is_zero,
            })
        print()

    # Test 1e: 3-fold multiplicative — T = p · n · n; ³He = p · p · n.
    # If perfectly multiplicative, Frob_p(T) = Frob(p) · Frob(n)^2 etc.
    if proton_lbl and neutron_lbl and T_lbl and He3_lbl:
        print("─── Test 1e: 3-fold T = p · n²; ³He = p² · n ───")
        for p in primes:
            n_2p = 2 * p
            f_p = frobs.get(proton_lbl, {}).get(p)
            f_n = frobs.get(neutron_lbl, {}).get(p)
            f_T = frobs.get(T_lbl, {}).get(p)
            f_He = frobs.get(He3_lbl, {}).get(p)
            if not all([f_p, f_n, f_T, f_He]):
                continue
            test_T = check_multiplicative(f_p, f_n * f_n, f_T, n_2p, u)
            test_He = check_multiplicative(f_p * f_p, f_n, f_He, n_2p, u)
            print(f"  p={p}: T-residue norm = {test_T['residue_galois_norm_int']}, "
                  f"³He-residue norm = {test_He['residue_galois_norm_int']}")
            relations.append({
                "kind": "three_fold_multiplicative",
                "prime": p,
                "T_residue_norm": test_T["residue_galois_norm_int"],
                "He3_residue_norm": test_He["residue_galois_norm_int"],
                "T_residue": test_T["residue_str"],
                "He3_residue": test_He["residue_str"],
            })
        print()

    # Test 1f: Galois-trace symmetry — does the binding-norm depend
    # only on A (mass number) or on (Z, N) separately?
    if proton_lbl and neutron_lbl and T_lbl and He3_lbl:
        print("─── Test 1f: ε(T) - ε(³He) Galois trace — isobaric asymmetry ───")
        for p in primes:
            n_2p = 2 * p
            f_p = frobs.get(proton_lbl, {}).get(p)
            f_n = frobs.get(neutron_lbl, {}).get(p)
            f_D = frobs.get(D_lbl, {}).get(p)
            f_T = frobs.get(T_lbl, {}).get(p)
            f_He = frobs.get(He3_lbl, {}).get(p)
            if not all([f_p, f_n, f_D, f_T, f_He]):
                continue
            eps_T = reduce_in_ring(f_T - f_D * f_n, n_2p, u).as_expr()
            eps_He = reduce_in_ring(f_He - f_D * f_p, n_2p, u).as_expr()
            gap = reduce_in_ring(eps_T - eps_He, n_2p, u)
            gap_expr = gap.as_expr()
            # Per-term reduction via `galois_orbit` to avoid
            # expression explosion before final reduction.
            gap_norm = reduce_in_ring(
                sum(galois_orbit(gap_expr, n_2p, u)), n_2p, u,
            )
            norm_int = (
                int(gap_norm.all_coeffs()[0]) if gap_norm.degree() == 0
                and gap_norm.all_coeffs()
                and gap_norm.all_coeffs()[0].is_Integer
                else None
            )
            print(f"  p={p}: gap-norm = {norm_int}  "
                  f"(eps_T-norm − eps_He-norm = "
                  f"{(test_T['residue_galois_norm_int'] if False else '—')})")
            relations.append({
                "kind": "isobaric_gap_norm",
                "prime": p,
                "gap_galois_norm": norm_int,
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

    # Test 5: L-function Frobenius-trace extraction from the
    # isobaric-asymmetry motive M_iso = M_T − M_³He.
    print("─── Test 5: L-function Frobenius-trace candidate (M_iso) ───")
    from sympy import factorint, sqrt
    iso_gap_norms = {}
    for r in relations:
        if r.get("kind") == "isobaric_gap_norm":
            p = r["prime"]
            n = r.get("gap_galois_norm")
            if n is not None:
                iso_gap_norms[p] = n
    weight_candidates = []
    print("  p     gap_norm        v_p  a_p (= norm/p^v_p)   Weil-bound check")
    print("  ──────────────────────────────────────────────────────────────────")
    for p in sorted(iso_gap_norms):
        n = iso_gap_norms[p]
        fac = factorint(abs(n))
        vp = fac.get(p, 0)
        a_p = n // (p ** vp)
        # Weil bound: |a_p| ≤ 2·p^{w/2} for weight w (rank-2 motive).
        # Find the smallest weight w (even integer) consistent with this.
        # For rank-1 motives the trace IS the eigenvalue: |a_p| = p^{w/2}.
        weight_for_w = []
        for w in [0, 1, 2, 3, 4, 5, 6]:
            # Rank-2 Weil bound:
            bound = 2 * (p ** (w / 2))
            ok = abs(a_p) <= bound
            weight_for_w.append((w, ok))
        min_consistent_w = next(
            (w for w, ok in weight_for_w if ok), None
        )
        weight_candidates.append({
            "prime": p,
            "gap_norm": n,
            "v_p": vp,
            "a_p_candidate": a_p,
            "min_weight_consistent": min_consistent_w,
            "weil_bound_at_min_w": (
                2 * (p ** (min_consistent_w / 2))
                if min_consistent_w is not None else None
            ),
        })
        weight_str = (f"w ≥ {min_consistent_w}"
                      if min_consistent_w is not None else "w → ∞")
        print(f"  {p:>2}    {n:>+10d}   {vp:>2}   {a_p:>+10d}            {weight_str}")
    print()

    # Test 4: p-adic divisibility analysis of residue norms.
    # If the residues encode motivic L-function local factors, we
    # expect the norm at prime p to be divisible by p^k for some
    # k ≥ 0 related to the motive's weight at p.
    print("─── Test 4: p-adic divisibility of residue Galois traces ───")
    pdic_table: list[dict[str, Any]] = []
    for r in relations:
        if r.get("kind") not in {"multiplicative", "isobaric_gap_norm",
                                  "three_fold_multiplicative"}:
            continue
        p = r["prime"]
        norms = []
        if r["kind"] == "multiplicative":
            n = r.get("residue_galois_norm")
            label = f"{r['atom']} = {' · '.join(r['factors'])}"
            if n is not None:
                norms.append((label, n))
        elif r["kind"] == "isobaric_gap_norm":
            n = r.get("gap_galois_norm")
            if n is not None:
                norms.append(("ε(T) - ε(³He)", n))
        elif r["kind"] == "three_fold_multiplicative":
            for k in ["T_residue_norm", "He3_residue_norm"]:
                n = r.get(k)
                if n is not None:
                    norms.append((f"3fold-{k}", n))
        for label, n in norms:
            if n == 0:
                pval = "∞ (zero)"
            else:
                # p-adic valuation of |n|.
                from sympy import factorint
                fac = factorint(abs(n))
                pval = fac.get(p, 0)
            pdic_table.append({
                "prime": p,
                "residue_label": label,
                "norm": n,
                "p_adic_valuation": pval,
                "factorization": dict(factorint(abs(n))) if n else {},
            })
    # Print a focused table of "high p-adic valuation" hits.
    print("  Residues with p-adic valuation ≥ 1 (motivic-Euler-factor signature):")
    hits = sorted([r for r in pdic_table if isinstance(r["p_adic_valuation"], int)
                   and r["p_adic_valuation"] >= 1], key=lambda r: -r["p_adic_valuation"])
    for r in hits[:20]:
        fac_str = " · ".join(f"{p}^{e}" for p, e in r["factorization"].items())
        print(f"  p={r['prime']:>2}: {r['residue_label']:<35} "
              f"norm = {r['norm']:>+10d}  v_{r['prime']} = {r['p_adic_valuation']}  "
              f"= ±{fac_str}")
    print()

    # Test 6: Hecke multiplicativity test — a_{pq} =? a_p · a_q
    # for distinct primes p, q.
    #
    # Method: evaluate the gap residue ε(T) − ε(³He) at u = ζ_{2pq}
    # (the cyclotomic level covering both primes), take its Galois
    # norm under Gal(Q(ζ_{2pq})/Q) — this gives a candidate "a_{pq}".
    # Compare to a_p · a_q predicted from the individual probes.
    #
    # If multiplicative, M_iso is consistent with a classical
    # GL_2 modular form (or Hecke-eigenform). If not, the motive
    # is non-modular.
    print("─── Test 6: Hecke multiplicativity a_{pq} =? a_p · a_q ───")

    def parse_int_coeffs(coeffs: list[dict],
                         u_sym: sp.Symbol
                         ) -> list[tuple[int, list[int]]]:
        """Parse Habiro coefficients (m, a_m_str) → integer-coefficient
        Horner lists once, for reuse across multiple cyclotomic
        conductors."""
        out = []
        for c in coeffs:
            m = int(c["m"])
            expr = sp.sympify(str(c["a_m"]), locals={"u": u_sym})
            try:
                poly = sp.Poly(expr, u_sym)
                ic = [int(co) for co in poly.all_coeffs()]
            except (sp.PolynomialError, ValueError):
                ic = []
            out.append((m, ic))
        return out

    def evaluate_gap_in_ring(parsed_T: list[tuple[int, list[int]]],
                              parsed_He: list[tuple[int, list[int]]],
                              N: int, u_sym: sp.Symbol,
                              terminated_T: bool,
                              terminated_He: bool) -> sp.Poly:
        """Evaluate Frob_N(T) - Frob_N(³He) at u = ζ_N. Reuses
        pre-parsed integer-coefficient lists across cyclotomic
        conductors.

        Iterative Pochhammer update: (u;u)_m = (u;u)_{m-1} · (1-u^m).
        """
        phi_N = sp.Poly(sp.cyclotomic_poly(N, u_sym), u_sym)

        def frob_at_N(parsed: list[tuple[int, list[int]]],
                      terminated: bool) -> sp.Poly:
            total = sp.Poly(0, u_sym)
            poch = sp.Poly(1, u_sym)
            last_m = 0
            for m, ic in parsed:
                if not terminated and m >= N:
                    break
                for i in range(last_m + 1, m + 1):
                    factor = sp.Poly(1, u_sym) - sp.Poly(u_sym ** i, u_sym)
                    poch = poch * factor
                    _, poch = poch.div(phi_N)
                last_m = m
                a_m_poly = sp.Poly(ic, u_sym) if ic else sp.Poly(0, u_sym)
                term = a_m_poly * poch
                _, term = term.div(phi_N)
                total = total + term
                _, total = total.div(phi_N)
            return total

        f_T = frob_at_N(parsed_T, terminated_T)
        f_He = frob_at_N(parsed_He, terminated_He)
        return reduce_in_ring((f_T - f_He).as_expr(), N, u_sym)

    # Need access to the original Habiro records.
    fast_witness = HERE / "habiro-coefficients-atomic-fast.witness.json"
    if fast_witness.exists():
        fast_data = json.loads(fast_witness.read_text())["results"]
        T_record = fast_data.get("T (tritium, A=3)")
        He_record = fast_data.get("3He (helium-3, A=3)")
    else:
        T_record = He_record = None

    if T_record and He_record:
        T_terminated = bool(T_record.get("expansion_terminated_clean"))
        He_terminated = bool(He_record.get("expansion_terminated_clean"))
        T_coeffs = T_record["habiro_coefficients"]
        He_coeffs = He_record["habiro_coefficients"]

        # Pre-parse Habiro coefficients ONCE here — independent of N
        # (since they're integer-coefficient polynomials in u). Reused
        # across the (p, q) loop below to avoid redundant sp.sympify.
        parsed_T = parse_int_coeffs(T_coeffs, u)
        parsed_He = parse_int_coeffs(He_coeffs, u)

        # Test: pq pairs from primes ∈ {3, 7, 11}. Skip larger ones
        # because deg(Φ_{2pq}) = (p-1)(q-1) gets expensive fast.
        pq_pairs = [(3, 7), (3, 11), (7, 11)]
        # Predicted a_p values (already extracted in Test 5):
        a_p_table = {
            wc["prime"]: wc["a_p_candidate"]
            for wc in weight_candidates
        }
        for p, q in pq_pairs:
            N = 2 * p * q
            print(f"  (p, q) = ({p}, {q})  → N = 2pq = {N}, "
                  f"φ(N) = {sp.totient(N)}")
            try:
                gap_at_N = evaluate_gap_in_ring(
                    parsed_T, parsed_He, N, u,
                    T_terminated, He_terminated,
                )
                # Galois trace of the gap residue at level N
                # (per-term reduction via `galois_orbit`).
                gap_expr = gap_at_N.as_expr()
                norm_at_N = reduce_in_ring(
                    sum(galois_orbit(gap_expr, N, u)), N, u,
                )
                norm_int = (
                    int(norm_at_N.all_coeffs()[0])
                    if norm_at_N.degree() == 0
                    and norm_at_N.all_coeffs()
                    and norm_at_N.all_coeffs()[0].is_Integer
                    else None
                )
                # Strip p-factor and q-factor: norm should equal
                # something ~ p^? · q^? · a_{pq} after dividing out
                # the bad-reduction multiplicities.
                a_pq_predicted = a_p_table.get(p, 0) * a_p_table.get(q, 0)
                # Strip primes p and q from norm.
                from sympy import factorint
                if norm_int is not None and norm_int != 0:
                    fac = factorint(abs(norm_int))
                    vp = fac.get(p, 0)
                    vq = fac.get(q, 0)
                    a_pq_observed = norm_int // (p ** vp * q ** vq)
                else:
                    a_pq_observed = norm_int
                print(f"    gap-norm at N={N}: {norm_int}")
                print(f"    a_{p}·a_{q} predicted: "
                      f"{a_p_table.get(p)} · {a_p_table.get(q)} = {a_pq_predicted}")
                print(f"    observed (norm / p^v_p / q^v_q): {a_pq_observed}")
                relations.append({
                    "kind": "hecke_multiplicativity",
                    "primes": [p, q],
                    "N": N,
                    "gap_norm_at_N": norm_int,
                    "a_pq_predicted": a_pq_predicted,
                    "a_pq_observed": a_pq_observed,
                    "ratio_observed_predicted": (
                        a_pq_observed / a_pq_predicted
                        if a_pq_predicted != 0 and a_pq_observed is not None
                        else None
                    ),
                })
            except Exception as e:
                print(f"    ERROR: {type(e).__name__}: {str(e)[:120]}")
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
        "p_adic_signature": pdic_table,
        "lfunction_frobenius_trace_candidate": weight_candidates,
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
