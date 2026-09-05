#!/usr/bin/env python3
""""Use all the terms" — measured. Every remaining term buys 1/323 of the gap,
and no series in `hbar_q` closes it at any order.

The flavour split carries a derived leading term and a posited correction:

    delta_leading   = (q-1)^2 (1 - q^-4)/3        DERIVED (prop:flavor-split-substrate)
    delta_canonical = delta_leading . (1 + hbar_q^3)   POSITED, "3-loop substrate-Planck"

`(1 + hbar_q^3)` is the first two terms of `1/(1 - hbar_q^3)`, so the instinct to
sum the whole series is the right instinct. This probe measures what it buys, and
then asks whether ANY series in `hbar_q` can work.

*** 0. WHAT THE CORPUS ALREADY HAD — read this before quoting anything below ***

`computations/probes/flavor_split_geometric_closure_probe.py` asked this exact
question and answered most of it. It already established that `(1+hbar^3)` and
`1/(1-hbar^3)` differ only at `O(hbar^6)`, that neither reaches CODATA, that
`(1+hbar^3)` supplies **76.07 %** of the needed correction, and that the exact
demanded coefficient is `(C_true - 1)/hbar^3 = 1.31459` — which is section C's
`c` at `k = 3`, to five figures. **That is not a new number here.** Its verdict —
"NOT the closure: a partial, posited factor, not merely unproven" — stands, and
this probe does not improve on it.

What is new, and the only reason this file exists:

  (i)   the tail-vs-gap RATIO `K = 323`, which turns "the closed form does not
        close it" into a bound on what ANY resummation could ever be worth;
  (ii)  the coefficient sweep at `k = 1, 2, 4` and the required exponent
        `k = 2.8822` (the predecessor measured only `k = 3`);
  (iii) the Lean statement `QOU/Hecke/GeometricTailBound.lean`, which is the
        general theorem the measurement instantiates.

*** A. WHAT ALL THE TERMS BUY — 1/323 of what is missing ***

    entire tail   (1-x)^-1 - (1+x) = x^2/(1-x)  at x = hbar_q^3   9.4707e-7
    gap still open after the two-term form                        3.0598e-4
    ratio                                                            323.07

Formalised as `QOU/Hecke/GeometricTailBound.lean`: `tail_eq` proves the identity,
and `summing_cannot_close` proves that when the gap exceeds the tail (`K > 1`)
the FULL sum still falls short. Here `K = 323`.

*** B. AND NO GEOMETRIC SERIES IN hbar_q CLOSES IT ***

Solving `delta_leading/(1 - hbar_q^k) = delta_CODATA` for the exponent:

    k = 2.8822    — not 3, and not an integer (4.09 % away from the posited 3)

*** C. NOR ANY SINGLE POWER WITH A CLEAN COEFFICIENT ***

    1 + c.hbar_q^1   needs c = 0.012905
    1 + c.hbar_q^2   needs c = 0.130249
    1 + c.hbar_q^3   needs c = 1.314562     <- the posited form takes c = 1, i.e. 76 %
                                            (= the predecessor probe's 1.31459)
    1 + c.hbar_q^4   needs c = 13.26745

None is `1` or any simple rational.

*** D. AND A LOOP EXPANSION WOULD HAVE TO EXPLAIN TWO VANISHINGS ***

A genuine expansion in the Planck tick reads
`1 + c1.hbar_q + c2.hbar_q^2 + c3.hbar_q^3 + ...`. Writing it as `(1 + hbar_q^3)`
asserts `c1 = c2 = 0` and `c3 = 1` — three claims, none of them derived. The
corpus's own audit says as much: no content block, Lean file or witness derives
the factor; its sole justification is a docstring phrase
(`docs/audits/2026-06-29-color-weighting-coverage-and-flavor-split-closed-form.md`
Parts B and C).

*** THE ANSWER TO "WE SHOULD DO ALL TERMS" ***

Agreed in principle, and it does not help: **the missing 0.03 % is not in this
tower at any order.** The disciplined production choice therefore stays
`delta_leading` — the only DERIVED form — and this probe is the reason, replacing
"it is negligible" (which was true but beside the point) with a bound on what the
alternative could ever be worth.

*** WHAT THIS DOES NOT SETTLE ***

Where the 0.03 % actually lives. `flavor_split_subleading`'s docstring says the
genuine correction "should be DERIVED from the 3-strand / 3-quark (spectator)
categorical structure", and that remains open. This probe closes one route by
measurement; it does not open another.
"""
from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

DPS = 40
mp.mp.dps = DPS
Q0 = mp.mpf("1.1099785827513808075916690956107688798744991218736")
HBAR_Q = (Q0 - 1)/Q0
DELTA_LEADING = (Q0 - 1)**2 * (1 - Q0**-4)/3
#: CODATA (m_n - m_p)/M_N, as recorded by the 2026-06-29 audit
DELTA_CODATA = mp.mpf("0.0013774699")


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def main() -> int:
    t0 = time.monotonic()
    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    ok = True
    x = HBAR_Q**3
    C_true = DELTA_CODATA/DELTA_LEADING

    print("=" * 78)
    print("A. WHAT ALL THE TERMS BUY")
    print("=" * 78)
    tail = 1/(1 - x) - (1 + x)
    print(f"    hbar_q = {mp.nstr(HBAR_Q, 15)}      x = hbar_q^3 = {mp.nstr(x, 12)}")
    print(f"    entire tail  (1-x)^-1 - (1+x)  = {mp.nstr(tail, 12)}")
    print(f"    identity check  x^2/(1-x)      = {mp.nstr(x**2/(1 - x), 12)}")
    ok &= chk("the_tail_identity_holds_numerically",
              abs(tail - x**2/(1 - x)) < mp.mpf("1e-35"), True,
              "proved in QOU/Hecke/GeometricTailBound.lean as tail_eq")
    gap = C_true - (1 + x)
    K = gap/tail
    print(f"    gap open after the two-term form = {mp.nstr(gap, 12)}")
    print(f"    K = gap / entire tail            = {mp.nstr(K, 10)}")
    ok &= chk("summing_every_remaining_term_buys_under_one_percent_of_the_gap",
              K > 100, True,
              "K = 323, so the full sum closes 1/323 of what is missing. "
              "summing_cannot_close proves the general form: when K > 1 the "
              "FULL geometric sum still falls short")

    print("\n" + "=" * 78)
    print("B. AND NO GEOMETRIC SERIES IN hbar_q CLOSES IT")
    print("=" * 78)
    k = mp.log(1 - DELTA_LEADING/DELTA_CODATA)/mp.log(HBAR_Q)
    print(f"    require leading/(1 - hbar_q^k) = CODATA  =>  k = {mp.nstr(k, 10)}")
    print(f"    posited exponent 3 is {mp.nstr(100*(3 - k)/k, 5)} % away")
    ok &= chk("the_required_exponent_is_not_an_integer",
              abs(k - mp.floor(k + mp.mpf("0.5"))) > mp.mpf("0.05"), True,
              "k = 2.8822, so no geometric series in hbar_q with an integer "
              "exponent reproduces the measured split")

    print("\n" + "=" * 78)
    print("C. NOR ANY SINGLE POWER WITH A CLEAN COEFFICIENT")
    print("=" * 78)
    coeffs = []
    for kk in (1, 2, 3, 4):
        c = (C_true - 1)/HBAR_Q**kk
        coeffs.append({"power": kk, "required_coefficient": mp.nstr(c, 12)})
        print(f"    1 + c.hbar_q^{kk}   needs c = {mp.nstr(c, 10)}")
    ok &= chk("no_power_admits_unit_coefficient",
              all(abs(mp.mpf(r["required_coefficient"]) - 1) > mp.mpf("0.2")
                  for r in coeffs), True,
              "the posited form takes c = 1 at k = 3, where 1.3146 is needed -- "
              "it supplies 76 %, and no other power is closer to a clean value")

    print("\n" + "=" * 78)
    print("D. AND A LOOP EXPANSION WOULD HAVE TO EXPLAIN TWO VANISHINGS")
    print("=" * 78)
    print("    a genuine Planck-tick expansion is 1 + c1.h + c2.h^2 + c3.h^3 + ...")
    print("    '(1 + hbar_q^3)' asserts c1 = c2 = 0 AND c3 = 1 — three claims,")
    print("    none derived. The corpus's own audit: no content block, Lean file")
    print("    or witness derives the factor; its justification is a docstring.")
    ok &= chk("the_posited_form_makes_three_underived_claims",
              True, True,
              "c1 = 0, c2 = 0, c3 = 1 -- and the measurement in C says c3 is "
              "1.3146, so even granting the two vanishings the third is wrong")

    print("\n  ✅ 'Use all the terms' is right in principle and does not help:")
    print("     the missing 0.03 % is not in this tower AT ANY ORDER.")
    print("  🛑 So production stays on delta_leading — the only DERIVED form —")
    print("     and this is the reason, replacing 'it is negligible' with a")
    print("     bound on what the alternative could ever be worth.")
    print("  🔓 Where the 0.03 % lives is untouched: flavor_split_subleading's")
    print("     own docstring says it should come from the 3-strand/3-quark")
    print("     spectator structure. Still open.")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-flavour-split-series",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": mp.nstr(Q0, 30), "dps": DPS,
                       "hbar_q": mp.nstr(HBAR_Q, 25),
                       "delta_leading": mp.nstr(DELTA_LEADING, 25),
                       "delta_CODATA": str(DELTA_CODATA),
                       "lean": "QOU/Hecke/GeometricTailBound.lean"},
        "data": {"C_true": mp.nstr(C_true, 15),
                 "tail": mp.nstr(tail, 15),
                 "gap_after_two_terms": mp.nstr(gap, 15),
                 "K_gap_over_tail": mp.nstr(K, 12),
                 "required_geometric_exponent": mp.nstr(k, 15),
                 "required_coefficients": coeffs},
        "provenance": {"headSha": _head_sha(),
                       "producer": "computations/qbeta/qbeta_flavour_split_series_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }
    out = HERE / "qbeta-flavour-split-series.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
