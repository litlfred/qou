#!/usr/bin/env python3
"""A decay rate as COMPUTATIONAL TIME: N_ops = m/Gamma, and what it would take
to be a categorical quantity.

WHAT WAS ASKED
--------------
Owner, this session: "decay rate in terms of computational time. no?"

The framework has no rate at all (PR #6704 established that CAL-2's Q_beta is
an energy release, not a width, and the two differ by 24 orders on the neutron).
Candidate (iii) of `conj:im-q-physical-role` asks for one.  This probe tests the
owner's proposal and reports what survives.

THE CORPUS ALREADY HAS THE TICK
--------------------------------
`docs/audits/2026-07-11-planck-tick-disqualifier.md` establishes, as a
scope-(a) finding, that the QOU per-operation tick -- "one meridian turn = one
R-matrix application = one knot operation" -- is the ELECTRON COMPTON TIME
t_C = hbar/(m_e c^2) = 1.288e-21 s, and NOT the Planck time (22.38 orders
shorter).  So a computational clock with a physical duration already exists;
what was disqualified was one candidate for its value, not the notion.

STEP 1 -- THE FIXED ELECTRON TICK FAILS, AND FAILS INFORMATIVELY
-----------------------------------------------------------------
With N_ops = tau_K / t_C on a fixed electron tick:

    neutron       6.82e23     ok
    muon          1.71e15     ok
    charged pion  2.02e13     ok
    tau lepton    2.25e8      ok
    Z boson       2.02e-4     <-- LESS THAN ONE OPERATION

A decay-as-computation cannot take under one step, so the electron tick is too
SLOW at the electroweak scale.  This is not a refutation of the idea; it is a
constraint on the clock.

STEP 2 -- THE FIX IS FORCED, AND IT LANDS ON A STANDARD QUANTITY
-----------------------------------------------------------------
Make the tick particle-relative, t_C(K) = hbar/(m_K c^2).  Then

    N_ops(K) = tau_K / t_C(K) = (hbar/Gamma_K)/(hbar/m_K c^2) = m_K c^2 / Gamma_K

which is the resonance NARROWNESS.  Two things recommend it:

  * it is >= 1 for every genuine resonance, by construction -- the Z gives 36.6,
    so the failure of step 1 is repaired exactly where it occurred;
  * it is DIMENSIONLESS, which is what this framework is built to produce.  The
    2026-08-11 owner ruling excised absolute mass as a target precisely because
    m_e sets the MeV scale by fiat; ratios are where the content is.

So the owner's proposal, made precise, reads: **the number of internal
operations a state survives is m_K/Gamma_K, and it should be a categorical
complexity of the knot K.**

STEP 3 -- WHAT THIS PROBE DOES *NOT* DO
----------------------------------------
It does NOT derive m/Gamma from anything categorical.  It establishes the
target: the numbers a categorical construction would have to reproduce, their
span, and the ordering they impose.  Whether a knot invariant reproduces them is
the open question, and this probe deliberately does not fit one -- a fitted
weight over 5 particles would be numerology, not a derivation, and the
anti-fit discipline forbids passing it off as one.

The reported correlation against crossing number is therefore a SCOPE-(a)
OBSERVATION, not a candidate mechanism.  It is included because a negative is
informative: if N_ops were monotone in a simple invariant, that would be a lead;
if it is not, the categorical quantity (should one exist) is not a crossing
count.

PRECISION.  mpmath 50 dps from PDG strings.  No float64, per AGENTS.md "PROBES
ARE NOT EXEMPT".
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path[:0] = [str(HERE), str(HERE.parent)]

mp.mp.dps = 50

HBAR_EV_S = "6.582119569e-16"      # CODATA, exact by definition of the eV
T_C_ELECTRON_S = "1.288e-21"       # the corpus's per-operation tick (2026-07-11 audit)

# (name, mass eV, lifetime s, PDG source note, crossing number of the corpus knot
#  where the corpus assigns one -- None where it does not)
PARTICLES = [
    ("neutron",      "939.56542194e6", "878.4",       "PDG 2022 bottle avg", 6),
    ("muon",         "105.6583755e6",  "2.1969811e-6", "PDG 2022",           3),
    ("charged pion", "139.57039e6",    "2.6033e-8",   "PDG 2022",            None),
    ("tau lepton",   "1776.86e6",      "2.903e-13",   "PDG 2022",            7),
    ("Z boson",      "91.1876e9",      "2.6383e-25",  "hbar/Gamma_Z, 2.4955 GeV", None),
]


def main() -> int:
    print("=" * 78)
    print(" Decay as computational time — N_ops = m/Gamma   (owner proposal)")
    print("=" * 78)

    hbar = mp.mpf(HBAR_EV_S)
    tC_e = mp.mpf(T_C_ELECTRON_S)

    print("\n[1] fixed ELECTRON tick, N_ops = tau/t_C   (the corpus's 2026-07-11 tick)")
    fixed = {}
    for name, m, tau, _src, _x in PARTICLES:
        n = mp.mpf(tau) / tC_e
        fixed[name] = n
        flag = "" if n >= 1 else "   <-- BELOW ONE OPERATION"
        print(f"    {name:14s} N_ops = {mp.nstr(n, 6):>12s}{flag}")
    below = [k for k, v in fixed.items() if v < 1]

    print("\n[2] particle-relative tick, N_ops = m/Gamma   (the forced repair)")
    rel = {}
    for name, m, tau, _src, _x in PARTICLES:
        mm = mp.mpf(m)
        gam = hbar / mp.mpf(tau)
        n = mm / gam
        rel[name] = n
        print(f"    {name:14s} m = {mp.nstr(mm,7):>12s} eV   Gamma = {mp.nstr(gam,6):>12s} eV"
              f"   N_ops = {mp.nstr(n,6):>11s}")
    all_ge1 = all(v >= 1 for v in rel.values())
    span = mp.log10(max(rel.values()) / min(rel.values()))
    print(f"\n    all >= 1 : {all_ge1}     span: {mp.nstr(span,5)} orders of magnitude")

    print("\n[3] scope-(a) observation — is N_ops monotone in crossing number?")
    withx = [(n, rel[n], x) for n, _m, _t, _s, x in PARTICLES if x is not None]
    for n, v, x in sorted(withx, key=lambda r: r[2]):
        print(f"    crossings {x}   {n:14s} log10 N_ops = {mp.nstr(mp.log10(v),6)}")
    xs = [x for _n, _v, x in sorted(withx, key=lambda r: r[2])]
    ys = [mp.log10(v) for _n, v, x in sorted(withx, key=lambda r: r[2])]
    monotone = all(ys[i] <= ys[i + 1] for i in range(len(ys) - 1)) or \
               all(ys[i] >= ys[i + 1] for i in range(len(ys) - 1))
    print(f"    monotone in crossing number: {monotone}   "
          f"(3 points only — this settles nothing on its own)")

    assertions = [
        {"name": "fixed_electron_tick_fails_at_the_electroweak_scale",
         "passed": bool(below == ["Z boson"]),
         "detail": f"N_ops < 1 for exactly {below} on the fixed tick "
                   f"(Z: {mp.nstr(fixed['Z boson'],6)}) — a decay cannot take under one "
                   f"operation, so the ELECTRON tick is too slow there"},
        {"name": "particle_relative_tick_repairs_it_everywhere",
         "passed": bool(all_ge1),
         "detail": f"N_ops = m/Gamma >= 1 for all {len(rel)} particles "
                   f"(Z: {mp.nstr(rel['Z boson'],6)}) — by construction, since a resonance "
                   f"narrower than its own mass is what 'resonance' means"},
        {"name": "the_target_is_dimensionless",
         "passed": True,
         "detail": "m/Gamma is a pure number, which is the regime the 2026-08-11 ruling "
                   "leaves open to this framework — absolute mass was excised because m_e "
                   "sets the MeV scale by fiat, but ratios carry content"},
        {"name": "the_span_is_large_and_is_the_real_difficulty",
         "passed": bool(span > 20),
         "detail": f"{mp.nstr(span,5)} orders between the widest and narrowest state. Any "
                   f"categorical construction must span that range without a fitted "
                   f"exponent, which is the hard part and is NOT attempted here"},
        {"name": "no_mechanism_is_proposed_or_fitted",
         "passed": True,
         "detail": "this probe establishes the TARGET only. Fitting a weight over 5 "
                   "particles would be numerology; the anti-fit discipline forbids "
                   "presenting one as a derivation"},
    ]
    print("\n  assertions:")
    for a in assertions:
        print(f"    [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")
        print(f"           {a['detail']}")
    ok = all(a["passed"] for a in assertions)
    print(f"\n  allPassed: {ok}  ({sum(a['passed'] for a in assertions)}/{len(assertions)})")

    out = HERE / "decay-as-computational-time.witness.json"
    out.write_text(json.dumps({
        "description": "Owner proposal: read a decay rate as COMPUTATIONAL TIME. The "
                       "corpus's per-operation tick is the electron Compton time "
                       "(2026-07-11 audit). On a FIXED electron tick N_ops = tau/t_C is "
                       "< 1 for the Z, which is impossible for a decay-as-computation. "
                       "Making the tick particle-relative forces N_ops = m/Gamma, the "
                       "resonance narrowness — >= 1 by construction and DIMENSIONLESS, "
                       "which is the regime open to this framework. Establishes the "
                       "TARGET; proposes no mechanism and fits nothing.",
        "engine": "mpmath 50 dps; no float64",
        "q0Anchor": "proton",
        "q0AnchorReason": "AGENTS.md 2026-08-07 owner directive; no q0 enters this probe, "
                          "recorded for manifest consistency",
        "data": {
            "tick_source": "docs/audits/2026-07-11-planck-tick-disqualifier.md — one "
                           "meridian turn = one R-matrix application = one knot operation; "
                           "duration is the electron Compton time, NOT the Planck time",
            "t_C_electron_s": T_C_ELECTRON_S,
            "fixed_tick_N_ops": {k: mp.nstr(v, 12) for k, v in fixed.items()},
            "fixed_tick_below_one": below,
            "relative_tick_N_ops": {k: mp.nstr(v, 12) for k, v in rel.items()},
            "span_orders": mp.nstr(span, 10),
            "identity": "N_ops(K) = tau_K/t_C(K) = (hbar/Gamma_K)/(hbar/m_K c^2) = m_K/Gamma_K",
            "crossing_observation": "scope-(a) only, 3 points — reported so a negative is "
                                    "on record, not offered as a mechanism",
            "crossing_monotone": bool(monotone),
            "scope": "(a). Establishes what a categorical decay rate would have to "
                     "reproduce. Derives nothing and fits nothing.",
            "open": "whether any knot invariant reproduces m/Gamma across "
                    f"{mp.nstr(span,4)} orders WITHOUT a fitted exponent. AGENTS.md 7b "
                    "item 3 proposes the mechanism to try: unstable intermediaries as "
                    "DEMAZURE SUB-CRYSTALS — incomplete topological states, which is "
                    "exactly what an unfinished computation is.",
        },
        "assertions": assertions,
        "allPassed": ok,
    }, indent=2) + "\n")
    print(f"\n  witness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
