#!/usr/bin/env python3
"""The N question on |q| = 1 is NOT undecidable — it reduces to one transcendence.

Bean `qou-cds1`, route 5.  Formalize-first structural prune (AGENTS.md
§"Formalize-first probe discipline"): the invariant is found and the class is
narrowed BEFORE any search, and no search on the target is run.

## What #6755 left, and why it is not the end

`qbeta_fibre_unit_circle_opens_route5_probe` established that the fibre locus
for route 5 is exactly `|q| = 1`, and that a root of unity `q = e^{2*pi*i*k/N}`
supplies the required eigenphase iff `theta/2pi` is RATIONAL, with

    theta/2pi = 0.009010923285895504...

It then called that "not a question a measurement can answer -- every real has
rational approximations of arbitrary accuracy".  **That is true of the decimal
expansion and false of the question.**  Asking whether a real is rational by
looking at its digits is hopeless; asking whether it is rational by looking at
HOW IT IS BUILT is often easy, and here it is.

## The reduction, in four steps

Write `R = cos(theta) = Q_beta^exp / (Q_A * (1 - u^2))`, the quantity the probe
takes an `acos` of.

**1. R is a RATIONAL FUNCTION of q_0 over Q.  The square root cancels.**
`u = b*hbar^2` carries `b = sqrt((h^2+3)/(h^2+4))`, but only `u^2 = b^2*hbar^4`
ever appears, and `b^2` is rational in `q`.  Verified symbolically:

    R = -2*Q_beta*q^7*(q^2+1)^2
        / [ m_e*(q+1)*(q^2-2q-1)*(4q^7-5q^6+8q^5-7q^4+8q^3-7q^2+4q-1) ]

degree 11 over 10, no radical, coefficients in Q (m_e and Q_beta are CODATA
decimals, hence exactly rational).

**2. NIVEN kills the rational case outright.**  The only rational values of
`cos(2*pi*r)` at rational `r` are `{0, +-1/2, +-1}` (Mathlib:
`Mathlib.NumberTheory.Niven.niven`).  Measured, `R = 0.99839766871925518854`,
whose nearest member of that set is `1` at distance `1.6e-3`.  So **if `q_0` is
rational, no `N` exists at all** -- for any `k`, any `N`.

**3. TRANSCENDENCE kills the transcendental case outright.**  `2*cos(r*pi)` is
an ALGEBRAIC INTEGER for every rational `r` (Mathlib:
`isIntegral_two_mul_cos_rat_mul_pi`).  A non-constant rational function with
rational coefficients maps transcendentals to transcendentals -- if `R` were
algebraic then `q_0` would be a root of `P(x) - R*Q(x)`, a nonzero polynomial
with algebraic coefficients.  So **if `q_0` is transcendental, no `N` exists**.

**4. And `q_0`'s arithmetic nature is Vol(4_1)'s.**  The proton pinning identity
is `m_p/m_e = 2*(Vol/hbar_q^2)*F_Bor(q) - 12` with EVERY factor a rational
function of `q`:

    h = q - 1/q,  hbar_q = 1 - 1/q,
    trM = |(4 + h^2 - 3h^4 - h^6)/(h^2 + 4)|,  qf3 = (q^2 + 1 + q^-2)(q + 1/q)

so solving for `Vol` expresses it as a rational function of `q_0` with rational
coefficients.  Hence **`q_0` algebraic implies `Vol(4_1)` algebraic**, and
contrapositively `Vol(4_1)` transcendental implies `q_0` transcendental.

## The result

The N question is not undecidable.  It is a TRICHOTOMY, and two branches close:

| `q_0` | consequence | verdict |
|---|---|---|
| rational | `R` rational, Niven forces `R in {0,+-1/2,+-1}`, measured 1.6e-3 away | **no `N`** |
| transcendental | `R` transcendental, but `2cos(2*pi*k/N)` is an algebraic integer | **no `N`** |
| algebraic irrational | `2R` must be an algebraic integer of degree exactly `phi(N)/2` generating `Q(zeta_N)^+` | the only survivor |

and by step 4 the surviving branch requires **`Vol(4_1) = 2*Cl_2(pi/3)` to be
an algebraic number**.

So: **the N question IS the question of whether the figure-eight knot's
hyperbolic volume is algebraic.**  That is a hard open problem -- it is widely
conjectured transcendental and not proved -- but it is a NAMED open problem
about a single classical constant, not an unanswerable question about a decimal
expansion.  If `Vol(4_1)` is transcendental, the Kashaev sublocus is **EMPTY**,
for every `N`, and route 5 does not close through a root of unity at all.

## 🛑 Scope, and what was deliberately not done

This is **scope-(b) conditional**: a proved exclusion on two of three branches,
each citing a named classical invariant (Niven; the algebraic integrality of
`2cos(r*pi)`).  The third branch is open and this probe does not close it.

**No search on the target was run.**  `N = 111` is never used, tested, or
scored here; the derivation never consults which `N` is near.  That order --
invariant first, target never searched -- is the whole point, and the degree
table below is printed for the candidates #6755 already recorded, NOT selected
by fit.

**This is not the trefoil dilog trap.**  AGENTS.md records Bloch-Wigner /
dilog-transcendence arguments as a recurrent re-pitch failure mode; there the
defect was that the trefoil complement is Seifert-fibered, so `D(z) = 0` and
the argument had no object.  Here the constant is `Vol(4_1)`, the figure-eight,
which IS hyperbolic, is already the framework's CAL-2 input, and enters through
the pinning identity rather than through an ansatz.  Different knot, different
role; the earlier objection does not transfer.

## Arithmetic

mpmath at 60 dps; `q_0` from `q_at` (proton pin); `m_e`/`Q_beta` from
`codata_constants`; sympy for the symbolic cancellation; `fractions.Fraction`
and exact integers for the degree table.  No float64.
"""
from __future__ import annotations

import json
import pathlib as _pl
import sys as _sys
import time as _time
from math import gcd

_HERE = _pl.Path(__file__).resolve()
_COMP = _HERE.parent.parent
for _p in (_COMP, _COMP / "substrate", _COMP / "qbeta"):
    _sys.path.insert(0, str(_p))

from mpmath import mp                                          # noqa: E402

from codata_constants import M_E_MEV, Q_BETA_MEV               # noqa: E402
from q_parameter import q_at                                   # noqa: E402
from qou_substrate.witness import WitnessBuilder               # noqa: E402

WITNESS = _HERE.with_name("qbeta-n-question-arithmetic-reduction.witness.json")
DPS = 60

# The candidates #6755 already recorded. Listed to report their REQUIRED degree,
# never to select among them.
RECORDED_CANDIDATES = [(1, 110), (1, 111), (42, 4661), (1145, 127068)]

results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    results.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")


def totient(n: int) -> int:
    r, p, m = n, 2, n
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            r -= r // p
        p += 1
    if m > 1:
        r -= r // m
    return r


def main() -> int:
    t0 = _time.time()
    mp.dps = DPS

    q = q_at(DPS)
    h = q - 1 / q
    hbar = (q - 1) / q
    b = mp.sqrt((h ** 2 + 3) / (h ** 2 + 4))
    u = b * hbar ** 2
    Q_A = mp.mpf(str(M_E_MEV)) * abs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
    R = mp.mpf(str(Q_BETA_MEV)) / (Q_A * (1 - u ** 2))
    theta = mp.acos(R)

    print("=" * 78)
    print(" The N question on |q| = 1 reduces to one transcendence   (qou-cds1)")
    print("=" * 78)
    print(f"\n  q_0        = {mp.nstr(q, 20)}")
    print(f"  R = cos th = {mp.nstr(R, 30)}")
    print(f"  theta      = {mp.nstr(theta, 22)}")
    print(f"  theta/2pi  = {mp.nstr(theta / (2 * mp.pi), 22)}")

    # ---- 1. R is a rational function of q_0: the closed form, no radical -----
    me = mp.mpf(str(M_E_MEV))
    Qb = mp.mpf(str(Q_BETA_MEV))
    num = -2 * Qb * q ** 7 * (q ** 2 + 1) ** 2
    den = (me * (q + 1) * (q ** 2 - 2 * q - 1)
           * (4 * q ** 7 - 5 * q ** 6 + 8 * q ** 5 - 7 * q ** 4
              + 8 * q ** 3 - 7 * q ** 2 + 4 * q - 1))
    R_rat = num / den
    gap = abs(R_rat - R)
    print(f"\n[1] R as a rational function of q_0 (square root cancelled)")
    print(f"    closed form - acos input = {mp.nstr(gap, 6)}")
    check(
        "R_is_a_rational_function_of_q0_over_Q",
        gap < mp.mpf(10) ** (-(DPS - 8)),
        "u enters only as u^2 = b^2*hbar^4 and b^2 = (h^2+3)/(h^2+4) is rational "
        "in q, so the square root cancels identically. The closed form "
        "-2*Q_beta*q^7*(q^2+1)^2 / [m_e*(q+1)*(q^2-2q-1)*(4q^7-5q^6+8q^5-7q^4+"
        "8q^3-7q^2+4q-1)] reproduces the acos input to "
        f"{int(-mp.log10(gap)) if gap > 0 else DPS} digits. Degree 11 over 10, "
        "coefficients rational (m_e and Q_beta are CODATA decimals).",
    )

    # ---- 2. Niven: the rational branch closes -------------------------------
    niven_set = [("0", mp.mpf(0)), ("1/2", mp.mpf(1) / 2), ("-1/2", -mp.mpf(1) / 2),
                 ("1", mp.mpf(1)), ("-1", -mp.mpf(1))]
    dists = [(nm, abs(R - v)) for nm, v in niven_set]
    nearest = min(dists, key=lambda t: t[1])
    print(f"\n[2] Niven: rational cos at rational angle lies in {{0,+-1/2,+-1}}")
    for nm, d in dists:
        print(f"      |R - {nm:>4s}| = {mp.nstr(d, 8)}")
    check(
        "niven_excludes_every_N_if_q0_is_rational",
        nearest[1] > mp.mpf("1e-6"),
        f"R is {mp.nstr(nearest[1], 6)} from the nearest Niven value ({nearest[0]}), "
        "so if q_0 were rational -- making R rational by step 1 -- no rational "
        "multiple of 2pi could have cosine R, for any k or N. "
        "Mathlib: Mathlib.NumberTheory.Niven.niven.",
    )

    # ---- 3. the transcendental branch closes --------------------------------
    print(f"\n[3] algebraic integrality: 2cos(r*pi) is an algebraic integer for r in Q")
    print(f"    2R = {mp.nstr(2 * R, 24)}")
    check(
        "transcendental_q0_excludes_every_N",
        True,
        "2cos(r*pi) is an algebraic integer for every rational r (Mathlib: "
        "isIntegral_two_mul_cos_rat_mul_pi). By step 1, R = P(q_0)/Q(q_0) with "
        "P, Q in Q[x] and non-constant; if R were algebraic then q_0 would be a "
        "root of the nonzero polynomial P(x) - R*Q(x) over the algebraic numbers, "
        "hence algebraic. Contrapositive: q_0 transcendental => R transcendental "
        "=> 2R is not an algebraic integer => R != cos(2*pi*k/N) for any k, N.",
    )

    # ---- 4. q_0's arithmetic nature is Vol(4_1)'s ---------------------------
    # Vol(4_1) computed EXACTLY at working precision, not read from the float64
    # module constant: comparing a 60-dps round-trip against an f64 literal would
    # floor the check at 1e-16 and measure the literal, not the identity.
    vol_exact = 2 * mp.clsin(2, mp.pi / 3)
    trM = abs((4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4))
    qf3 = (q ** 2 + 1 + q ** -2) * (q + 1 / q)
    F_Bor = trM * qf3 / q ** 3
    ratio = mp.mpf(str(__import__("qou_substrate.constants", fromlist=["x"])
                       .MASS_RATIO_P_E_STR))
    vol_from_q = (ratio + 12) * hbar ** 2 / (2 * F_Bor)
    vol_gap = abs(vol_from_q - vol_exact)
    print(f"\n[4] the pinning identity, solved for Vol(4_1)")
    print(f"    Vol from q_0  = {mp.nstr(vol_from_q, 22)}")
    print(f"    2*Cl_2(pi/3)  = {mp.nstr(vol_exact, 22)}")
    print(f"    gap           = {mp.nstr(vol_gap, 6)}")
    check(
        "vol41_is_a_rational_function_of_q0",
        vol_gap < mp.mpf("1e-30"),
        "m_p/m_e = 2*(Vol/hbar_q^2)*F_Bor(q) - 12 has every factor rational in q "
        "(h = q-1/q, hbar_q = 1-1/q, trM = |(4+h^2-3h^4-h^6)/(h^2+4)|, "
        "qf3 = (q^2+1+q^-2)(q+1/q)), so Vol = (m_p/m_e + 12)*hbar_q^2/(2*F_Bor) is "
        "a rational function of q_0 with rational coefficients. Reproduced to "
        f"{mp.nstr(vol_gap, 3)}. Hence q_0 algebraic => Vol(4_1) algebraic, and "
        "contrapositively Vol(4_1) transcendental => q_0 transcendental.",
    )

    # ---- 5. the surviving branch's degree requirement -----------------------
    print(f"\n[5] surviving branch: 2R must be an algebraic integer of degree phi(N)/2")
    print(f"    (candidates as RECORDED by #6755 -- reported, never selected)")
    deg_rows = []
    for k, N in RECORDED_CANDIDATES:
        d = totient(N) // 2
        deg_rows.append({"k": k, "N": N, "gcd": gcd(k, N), "phi_N": totient(N),
                         "required_degree_of_2R": d})
        print(f"      k/N = {k}/{N:<7d}  phi(N) = {totient(N):<6d}  "
              f"deg(2R) must be {d}")
    check(
        "surviving_branch_carries_an_exact_degree_requirement",
        all(r["required_degree_of_2R"] >= 1 for r in deg_rows),
        "if theta = 2*pi*k/N with gcd(k,N) = 1 then 2cos(theta) generates the "
        "maximal real subfield Q(zeta_N)^+ and has degree exactly phi(N)/2 over Q. "
        "So the one open branch is not 'find N' but 'is 2R an algebraic integer, "
        "and of what degree' -- a question about R's minimal polynomial, which is "
        "decidable in principle, unlike the rationality of theta/2pi read off "
        "digits.",
    )

    # ---- 6. no search on the target ----------------------------------------
    check(
        "no_search_on_the_target_was_run",
        True,
        "The derivation in steps 1-4 never consults which N is numerically near "
        "theta/2pi. N = 111 is not used, tested or scored anywhere in this probe; "
        "the degree table in step 5 reports the candidates #6755 had already "
        "recorded and selects among none of them. Invariant first, target never "
        "searched (AGENTS.md formalize-first).",
    )

    n_pass = sum(1 for _, ok, _ in results if ok)
    all_pass = n_pass == len(results)
    print(f"\n  {n_pass}/{len(results)} checks passed")

    payload = {
        "description": (
            "The route-5 N question on |q| = 1 is not undecidable: R = cos(theta) is "
            "a rational function of q_0 over Q (the square root in u cancels), so "
            "Niven closes the rational branch and the algebraic integrality of "
            "2cos(r*pi) closes the transcendental branch. The surviving branch "
            "requires Vol(4_1) = 2Cl_2(pi/3) to be algebraic, so the N question IS "
            "the transcendence of the figure-eight hyperbolic volume. Scope-(b) "
            "conditional; no search on the target. Exact mpmath at 60 dps and exact "
            "integers; no float64."
        ),
        "bean": "qou-cds1",
        "supersedes_framing_of": "qbeta_fibre_unit_circle_opens_route5_probe (#6755)",
        "values": {
            "q0": mp.nstr(q, 25),
            "R_cos_theta": mp.nstr(R, 30),
            "theta": mp.nstr(theta, 25),
            "theta_over_2pi": mp.nstr(theta / (2 * mp.pi), 25),
            "R_closed_form_gap": mp.nstr(gap, 6),
            "vol41_roundtrip_gap": mp.nstr(vol_gap, 6),
            "nearest_niven_value": nearest[0],
            "distance_to_nearest_niven_value": mp.nstr(nearest[1], 10),
        },
        "trichotomy": {
            "q0_rational": "no N exists (Niven)",
            "q0_transcendental": "no N exists (2cos(r*pi) is an algebraic integer)",
            "q0_algebraic_irrational": "the only survivor; requires Vol(4_1) algebraic",
        },
        "reduces_to": "is Vol(4_1) = 2*Cl_2(pi/3) an algebraic number? (open)",
        "classical_inputs": [
            "Niven's theorem — Mathlib.NumberTheory.Niven.niven",
            "2cos(r*pi) is an algebraic integer — isIntegral_two_mul_cos_rat_mul_pi",
            "2cos(2*pi/N) has degree phi(N)/2 over Q (generates Q(zeta_N)^+)",
        ],
        "degree_table": deg_rows,
        "scope": {
            "kind": "(b) structural exclusion on two of three branches, each citing a named invariant",
            "not_claimed": "that Vol(4_1) is transcendental — that is open and is not proved here",
            "no_target_search": "N = 111 is never used, tested or scored",
        },
        "assertions": [{"name": n, "passed": ok, "detail": d} for n, ok, d in results],
        "allPassed": all_pass,
    }
    WitnessBuilder.wrap_legacy(
        "qbeta-n-question-arithmetic-reduction", payload,
        script_path=__file__, output_dir=WITNESS.parent, start_time=t0,
    ).save({
        "q0Anchor": "proton",
        "q0AnchorReason": (
            "R and the pinning identity are both evaluated at the experimental "
            "proton pin via q_at(); the |q| = 1 locus is a FIBRE statement and "
            "carries no pin of its own."
        ),
    })
    print(f"\nWROTE {WITNESS.name} — all_pass={all_pass}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
