#!/usr/bin/env python3
"""Head-divisibility criterion for Habiro non-vanishing — all p at once.

The merged Lean lemma
`QOU.Habiro.habiroEval_ne_zero_of_head_not_dvd` (sorry-free) says:

    j ≤ N  and  ¬ ((ζ;ζ)_j ∣ habiroEval a ζ j)   ⟹   habiroEval a ζ N ≠ 0

i.e. if the *head* of the cyclotomic expansion is not divisible by the
Pochhammer at the same index, the whole truncated evaluation is nonzero.
Its companion `head_criterion_vacuous_of_isUnit` records the trap: when
(ζ;ζ)_j is a **unit** the divisibility holds trivially and the criterion
says nothing.

**Why j = 1 is the wrong index.** (ζ;ζ)_1 = 1 − ζ_{2p}, and
Norm(1 − ζ_n) = Φ_n(1), which is 1 unless n is a prime power. For odd p
the modulus 2p is not a prime power, so 1 − ζ_{2p} is a **unit** and the
j = 1 criterion is vacuous at every odd prime — exactly the
`head_criterion_vacuous_of_isUnit` case.

**Why j = 2 is the right index.** (ζ;ζ)_2 = (1 − ζ)(1 − ζ²), and
ζ² = ζ_p, so the second factor has norm Φ_p(1) = p. It is a non-unit at
**every** prime, so the criterion is non-vacuous everywhere.

**The closed form (odd p).** ℤ[ζ_{2p}] = ℤ[ζ_p] for odd p, and
𝔭 = (1 − ζ_p) is the unique (ramified) prime above p, with residue field
𝔽_p in which ζ_p ≡ 1 and hence ζ_{2p} ≡ −1. Since (1 − ζ) is a unit,

    (ζ;ζ)_2 ∣ H  ⟺  𝔭 ∣ H  ⟺  H(ζ ↦ −1) ≡ 0 (mod p)

and with H = a₀(ζ) + a₁(ζ)·(1 − ζ) this is an **integer** condition:

    A := a₀(−1) + 2·a₁(−1) ∈ ℤ,   criterion fires  ⟺  p ∤ A.

So a single integer A per atom decides non-vanishing at *every* odd
prime outside its finite prime divisor set — infinitely many p, with no
dependence on how deep the on-disk coefficient data goes. That is a
strictly stronger statement than the finite numerical sweep in
`habiro_frobenius_probe.py`, which can only report the primes whose
truncation lands inside the data.

p = 2 is handled separately by exact arithmetic in ℤ[i] (the argument
above assumes 2p is not a prime power, which fails at p = 2).

This script does two independent things and cross-checks them:

  1. evaluates the closed form A per atom, and
  2. brute-forces the divisibility in ℤ[u]/Φ_{2p}(u) for concrete
     primes, by inverting (ζ;ζ)_2 over ℚ and testing whether the
     quotient has integer coordinates in the power basis.

Agreement of (1) and (2) on every tested prime is the check that the
residue-field reduction above was done correctly.

All arithmetic is exact (sympy rationals / integers). No float appears.

Usage:
    python3 computations/probes/habiro_head_divisibility_probe.py

Output: `habiro-head-divisibility-probe.witness.json`
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
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

HERE = Path(__file__).parent
WITNESS_IN = _pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)
WITNESS_OUT = HERE / "habiro-head-divisibility-probe.witness.json"

# Brute-force cross-check primes. Only bounded by patience: the closed
# form is prime-independent, so this list exists to validate it, not to
# produce the result.
CHECK_PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def head_poly(coeffs: list[dict], u: sp.Symbol) -> sp.Expr:
    """H = a_0(u) + a_1(u)·(1 - u), the j = 2 head."""
    by_m = {c["m"]: sp.sympify(c["a_m"]) for c in coeffs}
    return sp.expand(by_m[0] + by_m[1] * (1 - u))


def closed_form_A(coeffs: list[dict], u: sp.Symbol) -> int:
    """A = a_0(-1) + 2·a_1(-1); criterion fires at odd p iff p ∤ A."""
    by_m = {c["m"]: sp.sympify(c["a_m"]) for c in coeffs}
    a0 = sp.Integer(sp.expand(by_m[0].subs(u, -1)))
    a1 = sp.Integer(sp.expand(by_m[1].subs(u, -1)))
    return int(a0 + 2 * a1)


def divides_in_cyclotomic(divisor: sp.Expr, target: sp.Expr,
                          n: int, u: sp.Symbol) -> bool:
    """Exact test: does `divisor` divide `target` in Z[ζ_n]?

    Z[ζ_n] is the full ring of integers of Q(ζ_n) with power basis
    1, u, …, u^{φ(n)-1}, so divisibility holds iff the quotient in
    Q(ζ_n) has integer coordinates in that basis.
    """
    phi = sp.Poly(sp.cyclotomic_poly(n, u), u)
    d = sp.Poly(divisor, u) % phi
    t = sp.Poly(target, u) % phi
    if d.is_zero:
        return t.is_zero
    inv = sp.invert(d, phi)
    quot = (t * inv) % phi
    return all(sp.Rational(c).q == 1 for c in quot.all_coeffs())


def main() -> int:
    if not WITNESS_IN.exists():
        print(f"ERROR: {WITNESS_IN.name} not found — regenerate it with "
              f"_habiro_coefficient_extract.py.")
        return 1

    u = sp.symbols("u")
    results = json.loads(WITNESS_IN.read_text())["results"]

    print("=" * 74)
    print("j = 2 head-divisibility criterion for Habiro non-vanishing")
    print("=" * 74)
    print("  criterion fires  <=>  (zeta;zeta)_2 does NOT divide the head")
    print("  fires  =>  Frob_p != 0  (habiroEval_ne_zero_of_head_not_dvd)")
    print()

    atoms_out = []
    all_agree = True

    for label, rec in results.items():
        coeffs = rec["habiro_coefficients"]
        if not rec.get("all_integral", False):
            print(f"  {label}: SKIPPED — coefficients not integral")
            continue
        if len(coeffs) < 2:
            print(f"  {label}: SKIPPED — fewer than 2 coefficients")
            continue

        A = closed_form_A(coeffs, u)
        H = head_poly(coeffs, u)
        bad = sorted(int(q) for q in sp.factorint(abs(A))) if A != 0 else None

        # --- brute-force cross-check at concrete odd primes ---
        checks = []
        for p in CHECK_PRIMES:
            n = 2 * p
            poch2 = sp.expand((1 - u) * (1 - u ** 2))
            brute_divides = divides_in_cyclotomic(poch2, H, n, u)
            predicted_divides = (A == 0) or (A % p == 0)
            agree = brute_divides == predicted_divides
            all_agree = all_agree and agree
            checks.append({
                "prime": p,
                "brute_force_divides": brute_divides,
                "closed_form_predicts_divides": predicted_divides,
                "agree": agree,
                "criterion_fires": not brute_divides,
            })

        # --- p = 2 handled separately: Z[i], 2p = 4 IS a prime power ---
        poch2_4 = sp.expand((1 - u) * (1 - u ** 2))
        p2_divides = divides_in_cyclotomic(poch2_4, H, 4, u)

        # Odd primes at which the criterion is SILENT (does not fire).
        silent = ([] if A != 0 else None) if A != 0 else None
        if A == 0:
            silent_desc = "every odd prime (A = 0 — criterion never fires)"
        else:
            odd_bad = [q for q in bad if q != 2]
            silent_desc = (
                f"only p in {odd_bad}" if odd_bad
                else "no odd prime — criterion fires at EVERY odd prime"
            )

        print(f"  {label}")
        print(f"    A = a_0(-1) + 2*a_1(-1) = {A}"
              + (f"   = {sp.factorint(abs(A))}" if A not in (0, 1, -1) else ""))
        print(f"    criterion SILENT at: {silent_desc}")
        print(f"    p = 2 (in Z[i]):     "
              f"{'silent (divides)' if p2_divides else 'FIRES (does not divide)'}")
        n_fire = sum(1 for c in checks if c["criterion_fires"])
        n_ok = sum(1 for c in checks if c["agree"])
        print(f"    brute-force cross-check: closed form agrees "
              f"{n_ok}/{len(checks)}; fires on {n_fire}/{len(checks)}")
        print()

        atoms_out.append({
            "atom_label": label,
            "Z": rec["Z"],
            "N": rec["N"],
            "n_habiro_coefficients": len(coeffs),
            "head_j2_poly": str(H),
            "closed_form_A": A,
            "A_prime_factors": bad,
            "criterion_fires_at_all_odd_primes_except": (
                [q for q in bad if q != 2] if A != 0 else "never fires (A = 0)"
            ),
            "p2_criterion_fires": not p2_divides,
            "brute_force_checks": checks,
            "closed_form_agrees_on_all_checked_primes": all(
                c["agree"] for c in checks
            ),
        })

    out = {
        "computation": "habiro-head-divisibility-probe",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "j = 2 head-divisibility criterion feeding the sorry-free Lean "
            "lemma QOU.Habiro.habiroEval_ne_zero_of_head_not_dvd. For odd p "
            "the criterion reduces to a single integer A = a_0(-1) + "
            "2*a_1(-1) per atom: it fires — hence Frob_p != 0 — at every odd "
            "prime not dividing A. j = 1 is vacuous for odd p because "
            "1 - zeta_{2p} is a unit there (Norm = Phi_{2p}(1) = 1 when 2p is "
            "not a prime power), which is the head_criterion_vacuous_of_isUnit "
            "case. The closed form is cross-checked against brute-force "
            "divisibility in Z[u]/Phi_{2p}(u) at 14 primes. All arithmetic is "
            "exact; no floating point is used anywhere in this script."
        ),
        "reference_lean": [
            "qou:QOU.Habiro.habiroEval_ne_zero_of_head_not_dvd",
            "qou:QOU.Habiro.head_criterion_vacuous_of_isUnit",
            "qou:QOU.Habiro.qPochDiag",
        ],
        "reference_blocks": [
            "def:motivic-galois-character",
            "prop:motivic-perpetual-obstruction",
        ],
        "input_witness": WITNESS_IN.name,
        "brute_force_check_primes": CHECK_PRIMES,
        "atoms": atoms_out,
        "summary": {
            "n_atoms": len(atoms_out),
            "closed_form_agrees_everywhere": all_agree,
            "n_atoms_firing_at_all_odd_primes": sum(
                1 for a in atoms_out
                if isinstance(a["criterion_fires_at_all_odd_primes_except"],
                              list)
                and not a["criterion_fires_at_all_odd_primes_except"]
            ),
            "n_atoms_firing_at_p2": sum(
                1 for a in atoms_out if a["p2_criterion_fires"]
            ),
        },
    }
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        out, script_path=__file__, engine="python")
    out["scriptFile"] = os.path.basename(__file__)
    WITNESS_OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"Wrote: {WITNESS_OUT.name}")
    print(f"Closed form agrees with brute force everywhere: {all_agree}")
    return 0 if all_agree else 1


if __name__ == "__main__":
    raise SystemExit(main())
