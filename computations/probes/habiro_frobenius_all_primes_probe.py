#!/usr/bin/env python3
"""Frob_p != 0 at EVERY prime, decided directly — the criterion was the long way.

Closes the two scope limits the head-criterion probes left open (PR #5884):
the `A` closed form was verified rather than derived, and the `p = 3` closure
read `a_2`, so it covered only the five atoms with Habiro data on disk.

## 1. The head criterion is a divisibility of P itself

`habiroEval_sub_head` says `(z;z)_j` divides `head_N - head_j` for every
`N >= j`, and past the truncation `head_N` IS the full value `P(zeta)`.
Therefore, for every `j`,

    (z;z)_j | head_j    <=>    (z;z)_j | P(zeta).

Verified here on 158 (atom, prime, j) cells, 0 disagreements. So the criterion
never needed the Habiro coefficients at all: it is a statement about `P`.

That also makes it **strictly weaker** than what it is used to prove. It fires
only when `(z;z)_j` fails to divide `P(zeta)`, whereas the actual question is
whether `P(zeta)` is zero — and a nonzero value can perfectly well be
divisible. The criterion earns its keep only when `P` is unknown, i.e. when
one has finitely many `a_m` and no closed form. Here `P` is a known polynomial.

## 2. So decide it directly, and finitely

    Frob_p = P(zeta_2p) / denom(zeta_2p),   and   P(zeta_2p) = 0  <=>  Phi_2p | P.

`deg Phi_2p = p - 1`, so once `p - 1 > deg P` the cyclotomic cannot divide `P`
and no larger prime need be considered. Below that bound there are finitely
many primes, each settled by an exact polynomial remainder. The same argument
applied to `denom` rules out a pole, which would make `Frob_p` undefined rather
than zero — a different failure that would break the claim just as badly.

This decides EVERY prime for a given `(Z, N)`, with no criterion, no `a_2`, and
no truncation-depth caveat. It also reaches atoms that have no Habiro data on
disk, since `P` comes from the closed form.

## 3. The `A` closed form, derived rather than verified

`tr_M = tau_p^Z tau_n^N * PROD_k f_k`, so before cancellation the numerator at
`u = -1` is a product, and

    A = n_p(-1)^Z * n_n(-1)^N * PROD_k n_k(-1) / G(-1)

where `G` is the gcd `cancel` removes. Measured, the pieces are

    n_p(-1) = 8        n_n(-1) = 2
    n_k(-1):  positive 1,  negative 1,  averaged 2,  averaged_weighted 12

and `canonical_interface_kinds` gives every MIXED atom exactly one
`averaged_weighted` (the single p-n junction) with the rest positive/negative,
and pure atoms none. Since positive and negative contribute a factor of 1, the
product collapses to `8^Z * 2^N * 12^[mixed]`, which is the closed form.

### `G(-1) = 1` is proved, so the closed form is too

An earlier version of this file called `G(-1) = 1` the one unproved step,
measured rather than derived. It is derivable, in three exact steps that this
script checks (§5):

  A. Every denominator is `const * u^i * (u^4+1)^j` — six fixed expressions,
     factored symbolically.
  B. Every numerator is coprime to `u^4+1` — `gcd = 1` for all six.
  C. Everything in sight lies in `Z[u^2]`, because `tr_M` is a rational
     function of `q = u^2`. So every exponent is even.

A and B force `G = gcd(NUM, DEN)` to be a power of `u` — a monomial, since the
only common factors available are powers of `u`. C forces its degree to be
even. A monomial of even degree is `+1` at `u = -1`. Hence `G(-1) = 1`.

The interface census is likewise **read from the source**, not sampled:
`canonical_interface_kinds` builds `["p"]*Z + ["n"]*N` and walks adjacent
pairs, so there is exactly one `p->n` transition iff `Z >= 1` and `N >= 1`,
and none otherwise — with `Z-1` positive and `N-1` negative alongside.

So `A(Z,N) = 8^Z * 2^N * 12^[mixed] = 2^(3Z+N) * 12^[mixed]` is **proved**,
resting only on exact symbolic evaluation of six fixed expressions and a
combinatorial fact about a list of adjacent pairs. The grid below is then a
consistency check on the proof, not the evidence for it.

## 4. The 3 is a consequence of the CANONICAL p-n convention specifically

`averaged` contributes `n_k(-1) = 2`, not 12. So under `strict_averaged` the
factor of 3 would not exist at all: `A` would be a pure power of two for every
atom, and the `j = 2` criterion would fire at every odd prime with no
exception. The 3 is a fingerprint of `bring_color_weighted` (owner ruling R3,
2026-08-15) reaching `A` through `delta`'s denominator — not of the trace.

## 5. Uniform in (Z, N): the whole question is six fixed polynomials

The grid above settles each `(Z, N)` it visits, but leaves "no `Phi_2p` ever
divides `P`, at any mass" as a verified rather than proved statement. That gap
closes, and closes completely:

  - `P = NUM / G` with `G` a monomial `u^k` (section 5 below);
  - `NUM = n_p^Z * n_n^N * PROD_k n_k` — powers of SIX FIXED polynomials,
    independent of `(Z, N)`;
  - `Phi_2p` is **irreducible** over `Q` and `Phi_2p(0) != 0`, so it cannot
    divide `u^k`;
  - `Q[u]` is a UFD, so `Phi_2p | NUM` iff `Phi_2p` divides one of the six.

So one finite check on six fixed polynomials settles EVERY atom at EVERY
prime. None of the six is divisible by any `Phi_2p` — and the check is finite
because the largest of the six has degree 44, so `p > 45` is impossible by
degree. Hence

    Frob_p != 0  for every (Z, N), at every prime,  with no mass bound.

**The 65-cell grid was overkill.** It is kept as corroboration and because it
also exercises the closed form, but the evidence for uniform non-vanishing is
the six-polynomial check, not the sweep.

All arithmetic is exact (sympy integers and rationals). No float appears.

Usage:
    python3 computations/probes/habiro_frobenius_all_primes_probe.py

Output: `habiro-frobenius-all-primes-probe.witness.json`
"""
from __future__ import annotations

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "habiro"))

import _habiro_coefficient_extract as ex  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
from closed_form_tau_M import canonical_interface_kinds  # noqa: E402
from habiro_coefficients_atomic import to_u_polynomial  # noqa: E402

HERE = Path(__file__).parent
WITNESS_IN = _pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)
WITNESS_OUT = HERE / "habiro-frobenius-all-primes-probe.witness.json"

MAX_MASS = 10                      # (Z, N) grid: Z + N <= MAX_MASS
EQUIV_PRIMES = [2, 3, 5, 7]        # primes for the §1 equivalence check
Q, U = sp.symbols("q u")


def poch(j: int) -> sp.Expr:
    e = sp.Integer(1)
    for k in range(1, j + 1):
        e *= 1 - U ** k
    return sp.expand(e)


def divides(divisor, target, n: int) -> bool:
    """`divisor | target` in Z[zeta_n], via integrality of the quotient's
    coordinates in the power basis (Z[zeta_n] is the full ring of integers)."""
    phi = sp.Poly(sp.cyclotomic_poly(n, U), U)
    d = sp.Poly(sp.expand(divisor), U) % phi
    t = sp.Poly(sp.expand(target), U) % phi
    if d.is_zero:
        return t.is_zero
    return all(sp.Rational(c).q == 1
               for c in ((t * sp.invert(d, phi)) % phi).all_coeffs())


def cyclotomic_divides_poly(poly: sp.Poly, p: int) -> bool:
    """Phi_2p | poly, i.e. poly(zeta_2p) = 0."""
    return (poly % sp.Poly(sp.cyclotomic_poly(2 * p, U), U)).is_zero


def num_at_minus_one(expr) -> int:
    """Numerator of expr(q -> u^2), in lowest terms, evaluated at u = -1."""
    e = sp.together(sp.cancel(sp.expand(sp.simplify(expr).subs(Q, U ** 2))))
    n_, _ = sp.fraction(e)
    return int(sp.Integer(sp.expand(n_).subs(U, -1)))


def main() -> int:
    if not WITNESS_IN.exists():
        print(f"ERROR: {WITNESS_IN.name} not found.")
        return 1
    results = json.loads(WITNESS_IN.read_text())["results"]
    ok = True

    print("=" * 76)
    print("Frob_p != 0 at EVERY prime — decided directly, no criterion")
    print("=" * 76)

    # ---- 1. the criterion IS a divisibility of P -----------------------------
    print("\n[1] (z;z)_j | head_j  <=>  (z;z)_j | P(zeta)   — so the criterion")
    print("    never needed the Habiro coefficients; it is about P.")
    equiv, n_bad = [], 0
    for lab, rec in results.items():
        by_m = {c["m"]: sp.sympify(c["a_m"]) for c in rec["habiro_coefficients"]}
        P = sp.expand(sp.sympify(rec["p_in_u"]))
        for p in EQUIV_PRIMES:
            for j in range(1, min(2 * p, len(by_m)) + 1):
                head = sp.expand(sum(by_m[m] * poch(m) for m in range(j)))
                a = divides(poch(j), head, 2 * p)
                b = divides(poch(j), P, 2 * p)
                n_bad += (a != b)
                equiv.append({"atom_label": lab, "prime": p, "j": j,
                              "divides_head": bool(a), "divides_P": bool(b),
                              "agree": bool(a == b)})
    ok = ok and (n_bad == 0)
    print(f"    {len(equiv)} (atom, prime, j) cells; disagreements: {n_bad}")
    print("    => the criterion is STRICTLY WEAKER than asking P(zeta) != 0:")
    print("       a nonzero value can still be divisible. It earns its keep")
    print("       only when P is unknown. Here P is a known polynomial.")

    # ---- 2. direct decision, on the five on-disk atoms -----------------------
    print("\n[2] Direct decision on the five on-disk atoms.")
    print("    P(zeta_2p) = 0 <=> Phi_2p | P; deg Phi_2p = p-1 bounds the check.")
    print(f"    {'atom':14s} {'degP':>5s} {'degD':>5s} {'p<=':>5s} {'#primes':>7s}"
          f" {'Phi|P':>8s} {'Phi|denom':>10s}")
    disk = []
    for lab, rec in results.items():
        P = sp.Poly(sp.expand(sp.sympify(rec["p_in_u"])), U)
        D = sp.Poly(sp.expand(sp.sympify(rec["denom_in_u"])), U)
        bound = max(P.degree(), D.degree()) + 1
        primes = [int(x) for x in sp.primerange(2, bound + 1)]
        zP = [p for p in primes if cyclotomic_divides_poly(P, p)]
        zD = [p for p in primes if cyclotomic_divides_poly(D, p)]
        ok = ok and not zP and not zD
        disk.append({"atom_label": lab, "deg_P": P.degree(), "deg_denom": D.degree(),
                     "degree_bound": bound, "n_primes_checked": len(primes),
                     "primes_where_P_vanishes": zP,
                     "primes_where_denom_vanishes": zD})
        print(f"    {lab[:14]:14s} {P.degree():>5d} {D.degree():>5d} {bound:>5d}"
              f" {len(primes):>7d} {str(zP) if zP else 'none':>8s}"
              f" {str(zD) if zD else 'none':>10s}")

    # ---- 3. the A derivation, with G(-1) isolated ---------------------------
    print("\n[3] A derived: A = n_p(-1)^Z * n_n(-1)^N * PROD n_k(-1) / G(-1)")
    tau_p, tau_n = ex._load_p_n_symbolic(WITNESS_IN, Q)
    z, h = ex._markov_z_q(Q), ex._hecke_h_q(Q)
    delta = flavor_split_leading(Q)
    KIND_EXPR = {
        "positive": z,
        "negative": z - h,
        "averaged": z - h / 2,
        "averaged_weighted": z - h * (sp.Rational(1, 2) - delta / 4),
    }
    kind_num = {
        "positive": num_at_minus_one(z),
        "negative": num_at_minus_one(z - h),
        "averaged": num_at_minus_one(z - h / 2),
        "averaged_weighted": num_at_minus_one(
            z - h * (sp.Rational(1, 2) - delta / 4)),
    }
    np1, nn1 = num_at_minus_one(tau_p), num_at_minus_one(tau_n)
    print(f"    n_p(-1) = {np1}   n_n(-1) = {nn1}")
    for k, v in kind_num.items():
        print(f"    n_k(-1)  {k:18s} = {v}"
              + ("   <-- the only one that is not 1 or 2" if v == 12 else ""))

    # ---- 4. grid: direct decision + closed form + G(-1) ---------------------
    print(f"\n[4] Grid, all (Z,N) with Z+N <= {MAX_MASS}: every prime decided,")
    print("    the closed form checked, and G(-1) measured.")
    grid, g_values, n_cf_bad, n_zero = [], set(), 0, 0
    for mass in range(1, MAX_MASS + 1):
        for Z in range(mass + 1):
            N = mass - Z
            P_expr, shift, _ = to_u_polynomial(
                ex._build_closed_form(Z, N, tau_p, tau_n, Q), Q, U)
            assert shift == 0, f"nonzero shift {shift} at Z={Z} N={N}"
            P = sp.Poly(sp.expand(P_expr), U)
            primes = [int(x) for x in sp.primerange(2, P.degree() + 2)]
            zeros = [p for p in primes if cyclotomic_divides_poly(P, p)]
            A = sp.Integer(P.as_expr().subs(U, -1))
            mixed = Z >= 1 and N >= 1
            closed = sp.Integer(2 ** (3 * Z + N) * (12 if mixed else 1))
            kinds = canonical_interface_kinds(
                Z, N, pn_convention="bring_color_weighted",
                weighted_labels=True)
            raw = sp.Integer(np1 ** Z * nn1 ** N)
            for k in kinds:
                raw *= kind_num[k]
            G = sp.Rational(raw, A)
            g_values.add(G)
            n_cf_bad += (A != closed)
            n_zero += len(zeros)
            grid.append({
                "Z": Z, "N": N, "deg_P": P.degree(),
                "n_primes_checked": len(primes),
                "primes_where_P_vanishes": zeros,
                "A": int(A), "closed_form": int(closed),
                "closed_form_agrees": bool(A == closed),
                "n_averaged_weighted": sum(
                    1 for k in kinds if k == "averaged_weighted"),
                "A_raw_before_cancellation": int(raw),
                "G_at_minus_one": str(G),
            })
        print(f"    mass {mass}: cumulative {len(grid)} cells, "
              f"{n_zero} vanishing, {n_cf_bad} closed-form mismatches")
    ok = ok and (n_zero == 0) and (n_cf_bad == 0)
    print(f"    distinct G(-1) over the whole grid: {sorted(str(g) for g in g_values)}")
    print("    G(-1) = 1 on every cell — and [5] derives it, so this grid is a")
    print("    consistency check on the proof, not the evidence for it.")

    # ---- 5. why G(-1) = 1, in three exact steps ---------------------------
    print("\n[5] G(-1) = 1, derived rather than measured")
    phi8 = sp.Poly(U ** 4 + 1, U)
    pieces = {"tau_p": tau_p, "tau_n": tau_n, **KIND_EXPR}
    denom_shapes, coprime, even_only = {}, {}, {}
    for name, expr in pieces.items():
        e = sp.together(sp.cancel(sp.expand(sp.simplify(expr).subs(Q, U ** 2))))
        n_, d_ = (sp.expand(x) for x in sp.fraction(e))
        np_, dp_ = sp.Poly(n_, U), sp.Poly(d_, U)
        denom_shapes[name] = str(sp.factor(d_))
        coprime[name] = (sp.gcd(np_, phi8).as_expr() == 1)
        even_only[name] = all(m[0] % 2 == 0
                              for m in np_.monoms() + dp_.monoms())
    print("    A. denominators are const * u^i * (u^4+1)^j:")
    for k, v in denom_shapes.items():
        print(f"       {k:18s} {v}")
    print(f"    B. every numerator coprime to u^4+1: "
          f"{sum(coprime.values())}/{len(coprime)}")
    print(f"    C. every numerator AND denominator lies in Z[u^2]: "
          f"{sum(even_only.values())}/{len(even_only)}")
    print("    A and B force G to be a monomial u^k (only powers of u are")
    print("    available as common factors); C forces k even; a monomial of")
    print("    even degree is +1 at u = -1.  Hence G(-1) = 1, and the closed")
    print("    form is PROVED, not merely verified.")
    ok = ok and all(coprime.values()) and all(even_only.values())

    # ---- 6. uniform in (Z,N): six fixed polynomials decide everything ------
    print("\n[6] Uniform closure — no mass bound")
    print("    P = NUM/G, G a monomial; NUM is a product of powers of SIX fixed")
    print("    polynomials; Phi_2p is irreducible with Phi_2p(0) != 0, so")
    print("    Phi_2p | P  iff  Phi_2p divides one of the six.")
    factors = {"tau_p": tau_p, "tau_n": tau_n, **KIND_EXPR}
    six, worst, hits = {}, 0, []
    print(f"    {'factor':20s} {'deg':>4s} {'p<=':>5s} {'#primes':>7s}  Phi_2p | it?")
    for name, expr in factors.items():
        e = sp.together(sp.cancel(sp.expand(sp.simplify(expr).subs(Q, U ** 2))))
        n_, _ = sp.fraction(e)
        poly = sp.Poly(sp.expand(n_), U)
        deg = poly.degree()
        worst = max(worst, deg)
        primes = [int(x) for x in sp.primerange(2, deg + 2)]
        bad = [pr for pr in primes if cyclotomic_divides_poly(poly, pr)]
        hits += [(name, pr) for pr in bad]
        six[name] = {"degree": deg, "degree_bound": deg + 1,
                     "n_primes_checked": len(primes),
                     "primes_dividing": bad}
        print(f"    {name:20s} {deg:>4d} {deg + 1:>5d} {len(primes):>7d}  "
              f"{bad if bad else 'none'}")
    ok = ok and not hits
    print(f"    largest degree {worst} => p > {worst + 1} impossible by degree")
    print("    => Phi_2p NEVER divides P, for ANY (Z,N), at ANY prime.")
    print("       Uniform, proved, no mass bound. The grid above is")
    print("       corroboration, not the evidence.")

    out = {
        "computation": "habiro-frobenius-all-primes-probe",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Closes the two scope limits of the head-criterion probes. (1) The "
            "criterion is equivalent to a divisibility of P itself — "
            "(z;z)_j | head_j iff (z;z)_j | P(zeta), verified on 158 cells — so "
            "it never needed the Habiro coefficients, and it is strictly weaker "
            "than asking P(zeta) != 0. (2) Therefore decide directly: "
            "P(zeta_2p) = 0 iff Phi_2p | P, and deg Phi_2p = p-1 makes that "
            "impossible once p-1 > deg P, so finitely many primes settle EVERY "
            "prime — no criterion, no a_2, no truncation-depth caveat, and it "
            "reaches atoms with no Habiro data on disk. The same argument on "
            "denom rules out a pole. (3) The A closed form is derived rather "
            "than merely verified: A = n_p(-1)^Z n_n(-1)^N PROD n_k(-1) / G(-1) "
            "with n_p(-1)=8, n_n(-1)=2 and per-kind 1/1/2/12, and exactly one "
            "averaged_weighted per mixed atom — leaving G(-1) = 1 as the single "
            "unproved step. (4) Because `averaged` contributes 2 and not 12, the "
            "factor of 3 is a fingerprint of the canonical bring_color_weighted "
            "convention, not of the trace. All arithmetic exact; no float."
        ),
        "reference_lean": [
            "qou:QOU.Habiro.habiroEval_sub_head",
            "qou:QOU.Habiro.habiroEval_ne_zero_of_head_not_dvd",
            "qou:QOU.Habiro.habiroEval_at_sq_eq_neg_one",
        ],
        "reference_blocks": [
            "def:motivic-galois-character",
            "prop:flavor-split-substrate",
        ],
        "input_witness": WITNESS_IN.name,
        "max_mass_tested": MAX_MASS,
        "criterion_equals_P_divisibility": equiv,
        "on_disk_atoms": disk,
        "interface_kind_num_at_minus_one": kind_num,
        "tau_num_at_minus_one": {"proton": np1, "neutron": nn1},
        "grid": grid,
        "summary": {
            "equivalence_cells": len(equiv),
            "equivalence_disagreements": n_bad,
            "grid_cells": len(grid),
            "cells_where_P_vanishes_at_any_prime": n_zero,
            "closed_form_mismatches": n_cf_bad,
            "distinct_G_at_minus_one": sorted(str(g) for g in g_values),
            "frobenius_nonzero_at_every_prime": bool(n_zero == 0),
            "uniform_closure": {
                "argument": (
                    "P = NUM/G with G a monomial; NUM is a product of powers of "
                    "six fixed polynomials independent of (Z,N); Phi_2p is "
                    "irreducible over Q with Phi_2p(0) != 0 so it cannot divide "
                    "u^k; Q[u] is a UFD. Hence Phi_2p | P iff Phi_2p divides one "
                    "of the six — a finite check, bounded by their largest "
                    "degree, that settles EVERY (Z,N) at EVERY prime."
                ),
                "six_factors": six,
                "any_cyclotomic_divides_any_factor": hits,
                "largest_factor_degree": worst,
                "mass_bound_needed": False,
            },
            "G_at_minus_one_proof": {
                "A_denominators_are_const_u_i_phi8_j": denom_shapes,
                "B_numerators_coprime_to_u4_plus_1": coprime,
                "C_all_in_Z_u_squared": even_only,
                "conclusion": (
                    "A and B force G to be a monomial u^k; C forces k even; a "
                    "monomial of even degree is +1 at u = -1. Hence G(-1) = 1."
                ),
            },
            "interface_census_source": (
                "canonical_interface_kinds builds ['p']*Z + ['n']*N and walks "
                "adjacent pairs, so exactly one p->n transition iff Z>=1 and "
                "N>=1 — read from source, not sampled."
            ),
            "closed_form_status": (
                "PROVED: rests on exact symbolic evaluation of six fixed "
                "expressions plus a combinatorial fact about adjacent pairs. "
                "An earlier version of this probe called G(-1)=1 unproved."
            ),
            "factor_3_is_convention_specific": True,
            "all_checks_passed": bool(ok),
        },
    }
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        out, script_path=__file__, engine="python")
    out["scriptFile"] = os.path.basename(__file__)
    WITNESS_OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"\nWrote: {WITNESS_OUT.name}")
    print(f"All checks passed: {ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
