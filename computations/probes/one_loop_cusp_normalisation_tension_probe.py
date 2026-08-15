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

BUT THE MISSING STEP HAS ALMOST NO ROOM, WHICH PARTLY RELIEVES THE WORRY. If the
step is `g(c)` then `k_meas(c) = k_true * g(c)`, so the measured `k` ratios bound
it directly — and the `c=1 -> c=2` ratio pins it to 1 at ~17 digits:

    g(2)/g(1) = k(2)/k(1) = 0.99999999999999999548

Every non-trivial candidate dies on that one number: `2^((c-1)/2)` (the retracted
per-cusp factor), `2^(c-1)`, `c`, `sqrt(c)`, `c^(1/4)`. Only `g == 1` survives.
So whatever fixes the exponent bookkeeping must contribute exactly 1 to the
CONSTANT at `c = 1` and `c = 2`: **the tension is in the power, and it does not
leak into `k` at the cusp numbers tested.**

The `c = 3` deviation (L6a4, 0.35%) is not a counterexample to that, and it is
not a cusp law either — a systematic `c`-dependence would have shown at `c = 2`
and does not, to 17 digits. More likely specific to that computation, as its own
witness already says.

RESOLVED 2026-08-08, BY A THEOREM IN A LOCAL FILE — AND AGAINST MY INFERENCE.
`library/arxiv-math-0611181v2/0611181v2.pdf` is van der Veen, "Proof of the volume conjecture for
Whitehead chains", which the corpus already uses for the colored Jones values
themselves. Its Main theorem reads

    J_N(W_{a,b,c,d})(e^{2 pi i/N}) ~ exp{ (1/2 pi)[ (Vol + i CS) N
                                                    + D log(N) + E ] }

with "**If b = 1 we have D = 3 pi**". The N-power is therefore
`N^{D/(2 pi)} = N^{3/2}`, and **D does not depend on c or d** — i.e. not on the
number of components. The two manifolds at issue are both b = 1:

    Whitehead link   = W_{0,1,1,0}   2 components -> N^{3/2}
    Borromean rings  = W_{0,1,1,1}   3 components -> N^{3/2}

So the corpus's cusp-independent `N^{3/2}` is THEOREM-BACKED at c = 2 and c = 3,
not merely fitted, and the wrong step was mine: the naive `delta = c` reading of
DGLZ eq (2.2) does not transfer to the colored-Jones observable. The Lemma 4
route shows why — `J_N ~ C N^{(c+d+3)/2} S~_N^{c+d}`, and `S~_N` carries its own
`N^{-1/2}` per factor, so the `(c+d)`-dependence cancels out of the net power.

The probe is kept because the arithmetic below is still the right check and the
bound on `g(c)` still holds; only the "unexplained" framing is retired.

AND THE SAME PAPER CARRIES A LEAD ON THE CONSTANT. Van der Veen's `E` — the
constant this corpus measures as `c_sigma` — is given EXPLICITLY in the proof of
Lemma 4 (Steps 5-6) as a `(c+d+1)`-dimensional Gaussian integral,

    Q_inf = psi * INT exp( -pi[ (c+d-(4a+c-d)i)|w|^2/2
                                + 2 sum_j (|z_j| + |w|/2)^2 ] ) dw dz

for the whole family. He evaluates it only far enough to show it is NONZERO. And
his closing paragraph cites Gukov-Murakami conjecturing that "the number E is
determined by the Ray-Singer torsion of the complement twisted by the holonomy
representation", adding "We hope to investigate these conjectures for the
Whitehead chains in a subsequent publication."

That is this corpus's `c_sigma <-> torsion` question, named as an open problem at
the end of the paper the corpus already reads its Jones values from. Connecting
`Q_inf` to `c_sigma` needs Lemma 3's constant for `S~_N` and the J-vs-J'
normalisation, neither done here — a direct evaluation gives
`|Q_inf| / 2^{-3/4} = 0.8109`, which is not a recognisable constant and is what a
missing normalisation factor looks like. Recorded as a route, not a result.

Derives nothing. Reports two measured exponents, the size of a gap that a local
theorem then closed, a bound on what could have closed it, and a lead.
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

from mpmath import mp, mpf, sqrt, log  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
COMP = HERE.parent
FIG8 = COMP / "whitehead-c-sigma-fig8-calib.witness.json"
WHIT = COMP / "whitehead-c-sigma.witness.json"
DISSOLUTION = COMP / "one-loop-c-sigma-percusp-dissolution.witness.json"

# Candidate forms for a missing c-dependent dictionary step g(c). Tested
# against the ratio the data pins hardest, g(2)/g(1) = k(2)/k(1).
G_CANDIDATES = {
    "2^((c-1)/2)  [the retracted per-cusp factor]":
        lambda c: mpf(2) ** ((c - 1) / mpf(2)),
    "2^(c-1)": lambda c: mpf(2) ** (c - 1),
    "c": lambda c: mpf(c),
    "sqrt(c)": lambda c: sqrt(mpf(c)),
    "c^(1/4)": lambda c: mpf(c) ** mpf("0.25"),
    "1  [no step]": lambda c: mpf(1),
}

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

    # ── how much room the missing step actually has ─────────────────────
    # The tension above is real, but it does not follow that the CONSTANT is
    # in danger at c = 2. If the missing dictionary step is g(c), then
    # k_meas(c) = k_true * g(c), so the measured k ratios bound g directly —
    # and they bound it hard.
    dis = record_upstream(DISSOLUTION, _UPSTREAM_RECORDS)
    k = {int(c): mpf(v) for c, v in dis["k_c"].items()}
    r21 = k[2] / k[1]
    r31 = k[3] / k[1]
    print("\n  how much room does a missing c-dependent step g(c) have?")
    print(f"     g(2)/g(1) = k(2)/k(1) = {mp.nstr(r21, 20)}   "
          f"(|dev| {mp.nstr(abs(r21 - 1), 3)})")
    print(f"     g(3)/g(1) = k(3)/k(1) = {mp.nstr(r31, 20)}   "
          f"(|dev| {mp.nstr(abs(r31 - 1), 3)})")
    g_tests = {}
    for name, f in G_CANDIDATES.items():
        pred = f(2) / f(1)
        survives = bool(abs(pred - r21) < mpf("1e-15"))
        g_tests[name] = {"predicted_ratio": mp.nstr(pred, 14),
                         "survives": survives}
        print(f"     {name:44s} -> {mp.nstr(pred, 12):>14}  "
              f"{'SURVIVES' if survives else 'excluded'}")
    only_trivial = bool(
        all(not v["survives"] for n, v in g_tests.items()
            if not n.startswith("1  "))
        and g_tests["1  [no step]"]["survives"])
    g_digits = int(-log(abs(r21 - 1)) / log(10))
    print(f"\n     => any missing step is 1 at c = 1 and c = 2 to {g_digits} "
          "digits.")
    print("     The c = 3 deviation is 0.35% but is NOT a smooth cusp law: a")
    print("     systematic c-dependence would have shown at c = 2 and does not.")

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
        "AND THE MISSING STEP HAS ALMOST NO ROOM, WHICH PARTLY RELIEVES THE "
        "WORRY THIS PROBE OPENED WITH. If the step is g(c) then "
        "k_meas(c) = k_true*g(c), so the measured k ratios bound it: "
        f"g(2)/g(1) = {mp.nstr(r21, 18)}, i.e. 1 to {g_digits} digits. Every "
        "non-trivial candidate dies on that one ratio — 2^((c-1)/2) (the "
        "retracted per-cusp factor), 2^(c-1), c, sqrt(c), c^(1/4) — and only "
        "g == 1 survives. So whatever fixes the exponent bookkeeping must "
        "contribute exactly 1 to the CONSTANT at c = 1 and c = 2. The tension "
        "is in the power, and it does not leak into k at the cusp numbers "
        "tested. "
        "THE c = 3 DEVIATION IS NOT A CUSP LAW EITHER. L6a4 is off by 0.35%, "
        "but a systematic c-dependence would have shown at c = 2 and does not "
        "— 17 digits of agreement there. So that offset is more likely "
        "specific to the L6a4 computation, as its own witness already says, "
        "than evidence of a law. "
        "SCOPE: no derivation. Two fitted exponents from committed witnesses, "
        "one textbook cohomology count that is my inference and not DGLZ's "
        "statement, the size of the gap between them, and a bound on what "
        "could close it."
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
    wb.add_data("bound_on_the_missing_step", {
        "model": "k_measured(c) = k_true * g(c) for a missing dictionary step g",
        "g2_over_g1": mp.nstr(r21, 20),
        "g3_over_g1": mp.nstr(r31, 20),
        "digits_pinning_g2_over_g1": g_digits,
        "candidates": g_tests,
        "only_trivial_survives": only_trivial,
        "reading": ("every non-trivial candidate dies on the c=1 -> c=2 ratio; "
                    "only g == 1 survives. So whatever fixes the exponent "
                    "bookkeeping contributes exactly 1 to the CONSTANT at c = 1 "
                    "and c = 2 — the tension is in the power and does not leak "
                    "into k at the cusp numbers tested. This PARTLY RELIEVES "
                    "the concern this probe opens with."),
        "c3_is_not_a_cusp_law": ("L6a4 deviates 0.35%, but a systematic "
                                 "c-dependence would have shown at c = 2 and "
                                 "does not (17 digits). More likely specific to "
                                 "that computation, as its own witness says"),
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
        "missing_step_is_trivial_at_c_1_and_2",
        computed="1" if only_trivial else "0", expected="1", tolerance="0.5",
        source=("g(2)/g(1) = 1 to ~17 digits, which excludes 2^((c-1)/2), "
                "2^(c-1), c, sqrt(c) and c^(1/4); only g == 1 survives, so the "
                "exponent tension does not leak into the constant"))
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
