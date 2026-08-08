#!/usr/bin/env python3
"""The N-power is cusp-INDEPENDENT in the corpus and cusp-DEPENDENT in DGLZ.

Beans qou-fl4t / qou-pn5j. Follow-through on the retraction recorded in
`docs/audits/2026-08-08-prefactor-form-what-is-actually-assumed.md`: the DGLZ
`/2` is a normalisation choice and cannot be lifted as the corpus's `k`. That
retraction named where the remaining `c >= 2` risk lives — the normalisation —
and this probe makes the specific tension concrete instead of leaving it as a
worry.

WHAT DGLZ SAY ABOUT THE N-POWER. Their eq (2.1) carries an explicit `hbar`-power,

    Z^(rho)(M; hbar) = exp( S_0/hbar - (1/2) delta(rho) log hbar + ... )

    delta(rho) = h1 - h0 ,   hi := dim H^i(M; E_rho)              (2.2)

so `Z ~ hbar^(-delta/2)`, and with `hbar = 2 pi i / N` that is `Z ~ N^(delta/2)`.

STANDARD COUNT (my inference, NOT read from DGLZ): for a hyperbolic 3-manifold
with `c` cusps at the discrete faithful representation with adjoint coefficients,
`h0 = 0` (irreducible) and `h1 = c` ("half lives, half dies" / the complex
dimension of the character variety near the geometric point). So

    delta = c        =>   Z ~ N^(c/2) ,    a CUSP-DEPENDENT power.

`delta` is `h1 - h0`, an Euler-characteristic-shaped quantity, which is exactly
the sort of thing that has no business being assumed cusp-independent.

WHAT THE CORPUS MEASURES. `c_sigma` is extracted as

    c_sigma := lim_N |J'_N| * N^(-p) * exp(-Vol*N/(2 pi))

with `p = 3/2` at EVERY cusp number, and `p` is fitted, not assumed:

    4_1   (c=1)   p = 1.49999998391397      whitehead-c-sigma-fig8-calib
    L5a1  (c=2)   p = 1.4999992078609055    whitehead-c-sigma

Both 3/2. If `delta = c` fed through to the observable power with a
`c`-independent offset, `c = 2` would need `N^2`, not `N^(3/2)`.

WHY THE CORPUS'S VALUE IS NOT IN DOUBT. The exponent is self-certifying. A wrong
`p` does not shift `c_sigma` by a constant — it makes the limit DIVERGE (`p` too
small) or VANISH (`p` too large), because the discrepancy is a positive power of
`N -> infinity`. `c_sigma(L5a1)` converges to 20 digits. So `p = 3/2` is right at
`c = 2` as a matter of measurement, whatever the bookkeeping says. This probe
quantifies that: it shows how fast the limit would run away under the
alternative power, so "it converges" is a number rather than an assertion.

WHAT IS ACTUALLY OPEN. The two statements are both solid and they do not sit
together without a `c`-dependent step nobody has written down — plausibly in the
colored-Jones normalisation for a LINK (`c` components each coloured by `N`, and
the eq (4.4) ratio against the solid torus), which differs from a knot in ways
this corpus has never worked out.

That is the concrete form of the `c >= 2` normalisation gap, and it is the
independent reason the retraction was right: constants cannot be transported
between the corpus's `c_sigma` and DGLZ's `S_1`/`s_1` until this is done.

Derives nothing. Reports two measured numbers, one textbook count, and the size
of the gap between them.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent
                       / "substrate"))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

_UPSTREAM_RECORDS: list = []

from mpmath import mp, mpf, log  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
COMP = HERE.parent
FIG8 = COMP / "whitehead-c-sigma-fig8-calib.witness.json"
WHIT = COMP / "whitehead-c-sigma.witness.json"

# cusp counts of the two manifolds whose N-exponent was actually fitted
CUSPS = {"4_1": 1, "L5a1": 2}


def main() -> int:
    set_compute_dps()
    f8 = record_upstream(FIG8, _UPSTREAM_RECORDS)
    wh = record_upstream(WHIT, _UPSTREAM_RECORDS)

    def dig(obj, key):
        """Pull a key from anywhere in a witness (layouts differ)."""
        stack = [obj]
        while stack:
            o = stack.pop()
            if isinstance(o, dict):
                if key in o:
                    return o[key]
                stack.extend(o.values())
            elif isinstance(o, list):
                stack.extend(o)
        raise KeyError(key)

    p_meas = {"4_1": mpf(str(dig(f8, "p_fit"))),
              "L5a1": mpf(str(dig(wh, "p_exponent")))}

    print("=" * 78)
    print(" the N-power: cusp-independent in the corpus, cusp-dependent in DGLZ")
    print("=" * 78)
    print("\n  DGLZ (2.1)/(2.2):  Z ~ hbar^(-delta/2) ~ N^(delta/2),")
    print("                     delta = h1 - h0")
    print("  standard count  :  hyperbolic, c cusps, geometric rep, adjoint")
    print("                     coefficients  =>  h0 = 0, h1 = c,  so delta = c")
    print("                     (MY inference, not read from DGLZ)\n")

    rows = {}
    for name, c in CUSPS.items():
        p = p_meas[name]
        naive = mpf(c) / 2 + 1     # delta/2 plus the c-independent offset that
        #                            reproduces 3/2 at c = 1
        rows[name] = {
            "cusps": c,
            "p_measured": mp.nstr(p, 16),
            "p_minus_three_halves": mp.nstr(p - mpf(3) / 2, 4),
            "naive_dglz_power_delta_over_2_plus_1": mp.nstr(naive, 6),
            "discrepancy": mp.nstr(naive - p, 6),
        }
        print(f"  {name:6s} c={c}   p measured = {mp.nstr(p, 16):>20s}   "
              f"(p - 3/2 = {mp.nstr(p - mpf(3)/2, 3)})")
        print(f"  {'':6s}        naive delta/2 + 1 = {mp.nstr(naive, 6):>12s}"
              f"        discrepancy = {mp.nstr(naive - p, 4)}")

    p_const = bool(abs(p_meas["4_1"] - p_meas["L5a1"]) < mpf("1e-5"))
    tension = bool(abs(rows["L5a1"]["discrepancy"] and
                       (mpf(rows["L5a1"]["naive_dglz_power_delta_over_2_plus_1"])
                        - p_meas["L5a1"])) > mpf("0.1"))

    # How fast a wrong power runs away — this is why the measurement is safe.
    print("\n  why the measured p is not in doubt: a wrong power does not shift")
    print("  c_sigma by a constant, it makes the limit run away as a power of N.")
    gap = mpf(rows["L5a1"]["naive_dglz_power_delta_over_2_plus_1"]) - p_meas["L5a1"]
    runaway = {}
    for N in (100, 1000, 10000):
        fac = mpf(N) ** gap
        runaway[f"N={N}"] = mp.nstr(fac, 8)
        print(f"     at N = {N:>6d}, the alternative power differs by "
              f"N^{mp.nstr(gap, 4)} = {mp.nstr(fac, 8)}")
    print("  c_sigma(L5a1) instead converges to 20 digits, so p = 3/2 is")
    print("  correct at c = 2 as a matter of measurement.")

    verdict = (
        "THE N-POWER IS MEASURED CUSP-INDEPENDENT AND DGLZ MAKES IT "
        "CUSP-DEPENDENT; NOBODY HAS RECONCILED THEM. DGLZ eq (2.1) carries "
        "hbar^(-delta/2) with delta = h1 - h0 (2.2), and for a hyperbolic "
        "manifold with c cusps at the geometric rep with adjoint coefficients "
        "the standard count is h0 = 0, h1 = c, so delta = c and Z ~ N^(c/2). "
        "The corpus extracts c_sigma with N^(-p) at p = 3/2 for every cusp "
        f"number, and p is FITTED, not assumed: {mp.nstr(p_meas['4_1'], 12)} at "
        f"c = 1 and {mp.nstr(p_meas['L5a1'], 12)} at c = 2. Whatever "
        "c-independent offset reproduces 3/2 at c = 1 would demand 2 at c = 2. "
        "THE MEASUREMENT IS THE SOLID SIDE. A wrong exponent does not bias "
        "c_sigma by a constant; it makes the limit diverge or vanish as a power "
        f"of N. At N = 10000 the alternative power differs by a factor of "
        f"{runaway['N=10000']}, and c_sigma(L5a1) converges to 20 digits "
        "regardless. So p = 3/2 holds at c = 2 empirically, and the naive "
        "delta = c reading does not transfer to the observable. "
        "WHERE THE MISSING STEP MUST BE. Most likely the colored-Jones "
        "normalisation for a LINK — c components each coloured by N, and the "
        "eq (4.4) ratio against the solid torus — which differs from the knot "
        "case in ways this corpus has never worked out. "
        "WHY THIS MATTERS BEYOND BOOKKEEPING: it is the independent reason the "
        "'the DGLZ /2 is the corpus's k' claim had to be retracted. Constants "
        "cannot be moved between c_sigma and S_1/s_1 while a c-dependent power "
        "in the dictionary is unaccounted for. It also locates the c >= 2 risk "
        "precisely, in the same place the retracted 2^((c-1)/2) per-cusp factor "
        "and L6a4's unexplained 0.35% both sit. "
        "SCOPE: no derivation. Two fitted exponents from committed witnesses, "
        "one textbook cohomology count that is my inference and not DGLZ's "
        "statement, and the size of the gap between them."
        if (p_const and tension) else
        "NO TENSION FOUND on this data — re-read the exponents before citing "
        "this probe.")
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("one-loop-cusp-normalisation-tension", engine="mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)
    wb.set_description(
        "Makes the c >= 2 normalisation gap concrete. DGLZ eq (2.1)/(2.2) give "
        "Z ~ N^(delta/2) with delta = h1 - h0, which for a hyperbolic manifold "
        "with c cusps at the geometric rep is delta = c — a cusp-DEPENDENT "
        "power. The corpus extracts c_sigma with a cusp-INDEPENDENT N^(-3/2), "
        "and the exponent is fitted rather than assumed (1.49999998 at c=1, "
        "1.4999992 at c=2). The measurement is the solid side: a wrong exponent "
        "makes the limit diverge or vanish as a power of N rather than biasing "
        "it by a constant, and c_sigma(L5a1) converges to 20 digits. So a "
        "c-dependent step is missing from the dictionary between the corpus's "
        "c_sigma and DGLZ's S_1/s_1 — most plausibly in the colored-Jones "
        "normalisation for a link. This is the independent reason constants "
        "cannot be transported between the two. Derives nothing.")
    wb.set_audit_only(
        "docs/audits/2026-08-08-prefactor-form-what-is-actually-assumed.md")
    wb.add_data("dglz_prediction", {
        "eq_2_1_power": "Z ~ hbar^(-delta/2) ~ N^(delta/2)",
        "eq_2_2": "delta(rho) = h1 - h0,  hi = dim H^i(M; E_rho)",
        "standard_count": ("hyperbolic, c cusps, discrete faithful rep, "
                           "adjoint coefficients: h0 = 0, h1 = c => delta = c"),
        "count_is_my_inference": ("DGLZ state (2.2) but do not evaluate h1 for "
                                  "a cusped manifold anywhere in the paper; the "
                                  "h1 = c count is standard but is MINE here, "
                                  "not theirs"),
        "consequence": "a CUSP-DEPENDENT observable power",
    })
    wb.add_data("corpus_measurement", rows)
    wb.add_data("exponent_is_self_certifying", {
        "why": ("a wrong p does not bias c_sigma by a constant — the "
                "discrepancy is a positive power of N -> infinity, so the limit "
                "diverges or vanishes instead of converging"),
        "alternative_power_runaway_factor": runaway,
        "observed": ("c_sigma(L5a1) converges to 20 digits at p = 3/2, so 3/2 "
                     "is correct at c = 2 as a matter of measurement"),
    })
    wb.add_data("what_is_missing", (
        "a c-dependent step in the dictionary between the corpus's c_sigma "
        "normalisation and DGLZ's S_1/s_1. Most plausibly the colored-Jones "
        "normalisation for a LINK: c components each coloured by N, and the "
        "eq (4.4) ratio against the solid torus. Never worked out here."))
    wb.add_data("bears_on", [
        "the retraction of 'the DGLZ /2 is the corpus's k' — constants cannot "
        "be transported while this is open",
        "the retracted 2^((c-1)/2) per-cusp factor, which lived here",
        "L6a4's unexplained 0.35% at c = 3, which sits in the same territory",
    ])
    wb.add_data("scope", (
        "no derivation and no new measurement. Two fitted exponents read from "
        "committed witnesses, one cohomology count that is an inference rather "
        "than a DGLZ statement, and the size of the gap."))
    wb.add_assertion(
        "measured_N_power_is_cusp_independent",
        computed="1" if p_const else "0", expected="1", tolerance="0.5",
        source=("p = 3/2 fitted at both c = 1 and c = 2, agreeing to better "
                "than 1e-5 — not assumed at either"))
    wb.add_assertion(
        "naive_dglz_count_disagrees_at_c_equals_2",
        computed="1" if tension else "0", expected="1", tolerance="0.5",
        source=("delta = c with a c-independent offset reproduces 3/2 at c = 1 "
                "and demands 2 at c = 2, a gap of 1/2 in the exponent — so the "
                "dictionary needs a c-dependent step that is not written down"))
    out = wb.save()
    print(f"  witness -> {out.name}")
    return 0 if (p_const and tension) else 1


if __name__ == "__main__":
    raise SystemExit(main())
