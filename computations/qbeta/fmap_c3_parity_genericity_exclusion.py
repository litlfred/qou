#!/usr/bin/env python3
"""fmap_c3_parity_genericity_exclusion.py — three converging exclusions of a
forced `c₃ = J_Hopf(1) = −2` from the convention-D two-row Markov trace (f-map
attack, bean qou-cds1).

Consolidates three feasibility probes (routes A / B / redirect) that each try to
DERIVE the c₃ identification `c₃ = −2` from the D-frame two-row Temperley–Lieb
trace structure. All three fail, for two complementary reasons, and the failure
is a proved parity invariant plus an anti-fit genericity measurement — NOT a bad
numeric probe. Exact symbolic over ℚ(q) (with √q, √5 radicals); no float.

## The target and the building blocks (all bar-EVEN except h)

`c₃ = J_Hopf(1) = −2`; the Hopf-link Jones value is `−(q²+q⁻²)` (bar-EVEN),
value `−2` at `q=1`. Building blocks under D: `y₃ᴰ=(q⁴+1)/(q²+1)²`,
`y₂₁ᴰ=q²/(q²+1)²`, `b²=1−y₂₁ᴰ`, `[2]_q=q+q⁻¹`, `Ξ=y₃ᴰ` — all bar-even;
`h=q−q⁻¹` bar-odd.

## Route A — bar-odd crossing term (REFUTED, scope-(b) parity)

The bar-odd part of the D two-row trace of any crossing power `σ^k` is divisible
by `h`, hence **vanishes at `q=1`**; `−2` (bar-even, `≠0`) is unreachable.

## Route B — Z3 carrier `G·(bar-odd carrier)` (REFUTED, same scope-(b) parity)

Any bar-even functional `G` times a bar-odd carrier (`D(q)` from KC15, or
`κ_(2,1)`) is bar-ODD, hence vanishes at `q=1`. `c₃=−2` is a bar-EVEN q=1
shadow, not a bar-odd swing.

## Redirect — bar-even channel (REFUTED, scope-(a) genericity)

`−2` at `q=1` is hit by MANY natural bar-even D-combinations (anti-fit trap:
the value pins nothing), and NO bar-even object equals the full Hopf polynomial
`V(Hopf)(q)=−(s+s⁵)` (which is not bar-even) as a q-identity.

## Net (scope-classified)

The D two-row trace/weight structure cannot force `c₃=−2` in either parity —
bar-odd by a proved invariant (scope-b), bar-even by genericity (scope-a). The
value `−2` is real (skein-derived, `JonesHopfSkein.lean`); its identification as
the N3 coupling is a q=1-value near-match. The only untouched route is the
analytic Φ_b amplitude leg (open; the corpus's Lawrence–Rozansky wall).

-- Ref: [manuscript] conj:dilogarithm-archimedean-limit (arc)
-- Ref: docs/audits/2026-08-21-fmap-c3-parity-genericity-exclusion.md
"""
from __future__ import annotations

import sympy as sp


def main() -> int:
    q = sp.symbols("q", positive=True)
    s = sp.sqrt(q)
    qi = 1 / q
    bar = lambda f: sp.simplify(f.subs(q, qi))

    y3 = (q**4 + 1) / (q**2 + 1) ** 2
    y21 = q**2 / (q**2 + 1) ** 2
    b2 = (q**4 + q**2 + 1) / (q**2 + 1) ** 2
    two = q + qi
    h = q - qi
    checks: dict[str, bool] = {}

    # --- Route A: bar-odd part of the D two-row trace of σ^k vanishes at q=1 ---
    # dimension-weighted two-row trace of σ^k: block (3) scalar q^k, block (21)
    # eigenvalues q^k and (−q⁻¹)^k, weights y3ᴰ, y21ᴰ (each of the two (21) rows).
    def trace_pow(k):
        return y3 * q**k + y21 * (q**k + (-qi) ** k)

    for k in (1, 2, 3, 4, 5):
        t = trace_pow(k)
        odd = sp.simplify((t - bar(t)) / 2)
        checks[f"A_barodd_trace_sigma{k}_vanishes_at_q1"] = sp.simplify(odd.subs(q, 1)) == 0

    # --- Route B: any bar-even G times a bar-odd carrier is bar-odd -> 0 at q=1 ---
    # bar-odd carrier proxies: h itself (bar-odd), and h*b2 (b2 bar-even).
    carriers = {"h": h, "h*b2": h * b2}
    Gs = {"1": sp.Integer(1), "y21": y21, "y3": y3, "[2]_q": two, "y3/y21": y3 / y21}
    for gname, G in Gs.items():
        for cname, C in carriers.items():
            prod = G * C
            is_odd = sp.simplify(bar(prod) + prod) == 0
            vanishes = sp.simplify(prod.subs(q, 1)) == 0
            checks[f"B_{gname}x{cname}_barodd_and_vanishes_at_q1"] = is_odd and vanishes

    # --- Redirect: bar-even genericity + no full-poly match ---
    Vhopf = -(s + s**5)  # skein-derived Hopf Jones polynomial
    checks["redirect_Vhopf_at_q1_is_-2"] = sp.simplify(Vhopf.subs(q, 1)) == -2
    checks["redirect_Vhopf_not_bar_even"] = sp.simplify(bar(Vhopf) - Vhopf) != 0
    bar_even_cands = {
        "-[2]_q": -two,
        "-(q^2+q^-2)": -(q**2 + q**-2),
        "-y3/y21": -y3 / y21,
        "-1/(2 y21)": -sp.Rational(1, 2) / y21,
    }
    n_hit = sum(1 for f in bar_even_cands.values() if sp.simplify(f.subs(q, 1)) == -2)
    checks["redirect_-2_is_generic_at_q1"] = n_hit >= 3  # many bar-even combos hit -2
    checks["redirect_no_bareven_eq_full_Vhopf"] = all(
        sp.simplify(f - Vhopf) != 0 for f in bar_even_cands.values()
    )

    for name, ok in checks.items():
        print(f"  {'PASS' if ok else 'FAIL':4s}  {name}")
    allok = all(checks.values())
    print(
        f"\nVERDICT: c₃=−2 is a bar-EVEN q=1 shadow; bar-odd routes (A,B) vanish at "
        f"q=1 (scope-b parity), bar-even route is generic (scope-a). "
        f"D-trace cannot force c₃ in any parity. {n_hit}/4 bar-even combos hit −2 "
        f"at q=1. {'ALL PASS' if allok else 'FAILURE'}"
    )
    return 0 if allok else 1


if __name__ == "__main__":
    raise SystemExit(main())
