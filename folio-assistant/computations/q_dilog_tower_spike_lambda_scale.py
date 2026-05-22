#!/usr/bin/env python3
"""Spike: q-dilog tower search for λ_scale.

Per PR #888 + PR #904 conclusion, the q-dilog tower is the
remaining first-principles route for deriving λ_scale ≈ 2.4599527869
(equivalently Vol_eff = 18.0259...). Bring-Bloch PSLQ over
hyperbolic-knot Bloch-Wigner values exhausted at tier 5 (52-knot
basis through 11-crossing, coefficient ≤ 10^30, dps=100, no
relation). This spike tests whether a substrate-natural q-dilog
basis at q_0 admits an integer relation to the target.

Basis design:
  - Li_2^q evaluated at substrate-natural arguments
  - Φ_q evaluated at the same arguments
  - Classical Bloch constants (G = Catalan)
  - q-integer products (small powers)

Substrate-natural arguments:
  - φ⁻¹ = 1/φ = (√5 − 1)/2 ≈ 0.618    (Mobius fixed point per
    conj:mobius-golden-fixed-points; q² + q − 1 = 0)
  - 1/φ² = φ⁻² ≈ 0.382
  - 3/7 = A(a=3/7) Möbius value at q = 1
  - (4 − q_0)/(4 q_0 + 3) ≈ 0.388     (CAL-4 ansatz, included for
    comparison only — known fitted)
  - 1/[2]_q at q_0 ≈ 0.477             (substrate q-integer)
  - h_q = q_0 − 1/q_0 ≈ 0.209           (substrate)
  - h_q² ≈ 0.0437

Targets:
  - λ_scale_p = 2.4599527869
  - Vol_eff_p = 18.025931... (= λ_scale_p · 8G)
  - 18.025931 − 8G = 10.698... (the "additive secondary class"
    candidate from PR #701 R&D 4 Option B search)

PSLQ at 60 dps, max coefficient 10^20 (smaller than bring_bloch's
10^30 — different basis, smaller search space).

Output: q-dilog-tower-spike-lambda-scale.witness.json

If PSLQ returns a non-trivial relation: a candidate substrate-pure
derivation of λ_scale. If it returns nothing across all argument
slices: another negative empirical result, narrowing the search
space further.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _li_2_q_util import li_2_q
from _phi_q_util import phi_q
from q_parameter import Q_50_DIGIT_STR
from witness_base import WitnessBuilder


def main():
    mp.mp.dps = 60

    Q0 = mp.mpf(Q_50_DIGIT_STR)
    Q0_inv = 1 / Q0
    h_q = Q0 - Q0_inv
    G = mp.catalan
    PHI = (1 + mp.sqrt(5)) / 2
    PHI_INV = 1 / PHI
    PHI_INV2 = 1 / (PHI * PHI)

    # Substrate q-integers
    def qint(n: int) -> mp.mpf:
        return (Q0**n - Q0**(-n)) / (Q0 - Q0_inv)

    qint2 = qint(2)
    qint3 = qint(3)
    qint4 = qint(4)

    # Targets
    lambda_p = mp.mpf("2.4599527869")
    vol_eff = lambda_p * 8 * G
    secondary = vol_eff - 8 * G

    print(f"q_0 (60 dps) = {mp.nstr(Q0, 40)}")
    print(f"h_q          = {mp.nstr(h_q, 20)}")
    print(f"target λ_p   = {mp.nstr(lambda_p, 12)}")
    print(f"target Vol_p = {mp.nstr(vol_eff, 12)}")
    print()

    # ── Substrate-natural argument list ────────────────────────────
    args = {
        "1/phi":     PHI_INV,
        "1/phi^2":   PHI_INV2,
        "3/7":       mp.mpf(3) / 7,
        "1/[2]_q":   1 / qint2,
        "h_q":       h_q,
        "h_q^2":     h_q * h_q,
        "-h_q":     -h_q,
        "-h_q^2":   -h_q * h_q,
    }

    # ── Evaluate Li_2^q and Φ_q at each argument ───────────────────
    basis_entries: list[tuple[str, mp.mpf]] = []
    for name, z in args.items():
        try:
            v_li = li_2_q(z, Q0, Q0_inv)
            basis_entries.append((f"Li2q({name})", v_li))
        except Exception as e:
            print(f"Li2q({name}) failed: {e}")
        try:
            v_phi = phi_q(z, Q0_inv)
            if mp.isfinite(v_phi):
                basis_entries.append((f"Phi_q({name})", v_phi))
        except Exception as e:
            print(f"Phi_q({name}) failed: {e}")

    # ── Add classical anchors ──────────────────────────────────────
    classical = {
        "1":      mp.mpf(1),
        "G":      G,
        "[2]_q":  qint2,
        "[3]_q":  qint3,
        "[4]_q":  qint4,
        "phi":    PHI,
        "h_q":    h_q,
    }
    for name, val in classical.items():
        basis_entries.append((name, val))

    # Report basis
    print(f"Basis size: {len(basis_entries)}")
    print(f"{'name':<22s}  value")
    for name, val in basis_entries:
        print(f"  {name:<20s}  {mp.nstr(val, 12)}")
    print()

    # ── PSLQ against each target ───────────────────────────────────
    results = []
    for target_name, target_val in [
        ("lambda_p", lambda_p),
        ("Vol_eff_p", vol_eff),
        ("secondary (Vol_eff - 8G)", secondary),
    ]:
        print(f"PSLQ for target {target_name} = {mp.nstr(target_val, 12)}")
        # Build vector [target, b1, b2, ...]; PSLQ finds integer
        # relation a0*target + Σ a_i * b_i = 0
        vec = [target_val] + [v for _, v in basis_entries]
        try:
            relation = mp.pslq(vec, maxcoeff=10**20, tol=mp.mpf(10)**(-50))
            if relation is None:
                print(f"  → no relation found at coeff ≤ 10^20")
                results.append({"target": target_name, "relation": None})
                continue
            # Decode
            if relation[0] == 0:
                print(f"  → trivial: target coefficient is 0; skipping")
                results.append({"target": target_name, "relation": "trivial"})
                continue
            # Express target as -1/a0 * Σ a_i * b_i
            scale = -1 / mp.mpf(relation[0])
            terms = []
            for (name, _), a_i in zip(basis_entries, relation[1:]):
                if a_i == 0:
                    continue
                coef = scale * mp.mpf(a_i)
                terms.append((name, int(a_i), coef))
            print(f"  → {target_name} = -1/{relation[0]} · Σ a_i · b_i")
            for name, a_i, coef in terms:
                print(f"      + {a_i:>+8d} · {name}   ({mp.nstr(coef, 8)})")
            results.append({
                "target": target_name,
                "a0": int(relation[0]),
                "terms": [(name, int(a_i)) for (name, _), a_i in zip(basis_entries, relation[1:]) if a_i != 0],
            })
        except Exception as e:
            print(f"  → PSLQ failed: {e}")
            results.append({"target": target_name, "error": str(e)})
        print()

    # ── Witness ────────────────────────────────────────────────────
    w = WitnessBuilder("q-dilog-tower-spike-lambda-scale", engine="mpmath")
    w.set_description(
        "Spike search for a substrate-pure q-dilog-tower derivation "
        "of λ_scale ≈ 2.4599527869. Basis: Li_2^q + Φ_q evaluated at "
        "substrate-natural arguments {1/φ, 1/φ², 3/7, 1/[2]_q, h_q, "
        "−h_q, h_q², −h_q²} + classical anchors. PSLQ at 60 dps, "
        "maxcoeff 10^20. Companion to PR #888 + #904: hyperbolic-knot "
        "Bloch basis exhausted; this is the q-dilog leg."
    )
    w.set_content_block("conj:lambda-scale-bring-bloch-identity")
    w.add_parameter("q0_dps", 60)
    w.add_parameter("pslq_maxcoeff", 10**20)
    w.add_data("basis_size", len(basis_entries))
    w.add_data("basis_names", [n for n, _ in basis_entries])
    w.add_data("targets_tested", ["lambda_p", "Vol_eff_p", "secondary"])
    w.add_data("results", [
        {"target": r["target"],
         "relation_found": ("a0" in r),
         "trivial": r.get("relation") == "trivial",
         "terms": r.get("terms") if "terms" in r else None}
        for r in results
    ])
    any_nontrivial = any("a0" in r and r.get("relation") != "trivial" for r in results)
    w.add_assertion(
        "no_nontrivial_relation_found_or_documented",
        computed=float(not any_nontrivial),
        expected=1.0,
        # If a relation IS found, this assertion "fails" — but that's
        # the positive case we hope for; the test plan records the
        # finding rather than blocking CI.
    )
    out = w.save()
    print(f"Witness: {out.name}")


if __name__ == "__main__":
    main()
