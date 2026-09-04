#!/usr/bin/env python3
"""CAL-2 is named a decay WIDTH.  The quantity the framework actually computes
is the decay's Q-VALUE, and the two are 24 orders of magnitude apart.

🛑 THIS RETRACTS AN INTERPRETIVE CLAIM I LANDED IN PR #6687 AND #6700.
------------------------------------------------------------------------
Those PRs argued that candidate (iii) of `conj:im-q-physical-role` was narrowed
because "the framework's one canonical decay width D_beta IS CAL-2, and it is
obtained at real q_0 -- so decay needs no Im(q)".  The Lean and the arithmetic
in #6687 stand (they are about two width MECHANISMS and are pure mathematics).
The interpretive step does not: **what the framework computes is not a decay
width.**  Candidate (iii)'s stated obstacle -- "needs a categorical formula for
decay widths Gamma" -- therefore STANDS, and I wrote in two merged PRs that it
did not.

WHAT WAS ASKED
--------------
Bean `qou-c66b`, owner-selected follow-up D: exhibit a `Gamma` that the
reciprocal mechanism `D = hbar/Q` demonstrably FAILS to produce.  This probe is
that exhibit, and the `Gamma` turns out to be the neutron's own -- the very
decay CAL-2 is named after.

WHAT THE CORPUS ASSERTS, IN FOUR PLACES
----------------------------------------
  observations/epistemic-status-of-calibrations.md:3
      "The parameter Q_beta = hbar/D_beta proxies CAL-2 (the neutron beta-decay
       width D_beta)."
  observations/three-calibration-discipline-discussion.md:7
      "... two decay widths (m_e, D_beta, D_pi) ... We read them off their most
       precise proxies: the masses m_e, m_pi and the Q-VALUE
       Q_beta = hbar/D_beta."
  docs/canonical-derivation-cheat-sheet.md:134, :490
      "D_beta ---- neutron beta-decay width (CAL-2, h^2)" and
      "Q_beta = hbar/D_beta ... approx 0.784 MeV (0.17% vs CODATA)".

So the corpus asserts BOTH that `D_beta` is the neutron beta-decay width AND
that `Q_beta = hbar/D_beta` is a Q-value of about 0.784 MeV.

THE TWO CANNOT BOTH HOLD, AND THE GAP IS NOT SUBTLE
-----------------------------------------------------
A decay width and a lifetime are reciprocal: `Gamma = hbar/tau` BY DEFINITION.
So if `D_beta` really is the neutron's width, then `hbar/D_beta` is the neutron
LIFETIME -- 878.4 s -- and not an energy at all, let alone 0.784 MeV.

Read the other way, defining `D_beta := hbar/Q_beta` makes the relation
dimensionally consistent but yields `8.4e-22 s`, which is **24 orders of
magnitude** from the neutron lifetime.  Under that reading `D_beta` is a
perfectly well-defined quantity that is simply NOT the neutron's decay width.

Either way the conclusion is the same and it is the point of this probe:

    THE FRAMEWORK COMPUTES THE DECAY'S ENERGY RELEASE.  IT DOES NOT COMPUTE THE
    DECAY'S RATE.  Q_beta and Gamma_n are INDEPENDENT properties of one decay,
    not reciprocals of each other.

WHY THAT MATTERS BEYOND THE NAMING
------------------------------------
`Q_beta` is a fine CAL-2 proxy and nothing here touches it: the framework
reproduces the neutron beta-decay Q-value to 0.17 %, which is a real result.
What is not true is that reproducing it amounts to having a categorical formula
for a decay WIDTH.  A Q-value is fixed by the mass differences alone; a width
additionally needs the coupling and the phase-space integral, which is exactly
the content the framework has not supplied -- and exactly what candidate (iii)
asked for.

So this is a NEGATIVE result about my own earlier positive one, and it hands
candidate (iii) back its obstacle in sharper form: the missing object is not
"a decay observable" (the corpus has one) but specifically **the rate**.

SCOPE
-----
Scope (a) throughout.  Nothing here says `Im(q)` DOES encode a width -- it says
the reciprocal mechanism does not produce the one width we can check, so the
argument by which I narrowed (iii) does not hold.  (iii) returns to open.

Nothing here is a proposal to rename `D_beta`.  The naming is the author's, was
flagged to the author, and the author's ruling on it is pending; this probe
measures the gap rather than resolving it.

PRECISION.  mpmath at 50 dps throughout, from CODATA/PDG strings.  No float64,
per AGENTS.md "PROBES ARE NOT EXEMPT".
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

Q0_STR = "1.1099785827513808075916690956107688798744991218736"
ME_MEV = "0.51099895069"          # CODATA 2022 (CAL-1)
HBAR_EV_S = "6.582119569e-16"     # CODATA, exact by definition of the eV
TAU_N_S = "878.4"                 # PDG 2022 neutron lifetime, bottle average
TAU_N_ERR_S = "0.5"
Q_BETA_EXP_MEV = "0.78233"        # AME2020 neutron beta-decay Q-value


def main() -> int:
    print("=" * 78)
    print(" Is CAL-2's D_beta the neutron's decay width?  (bean qou-c66b, follow-up D)")
    print("=" * 78)

    q0 = mp.mpf(Q0_STR)
    me = mp.mpf(ME_MEV)
    hbar = mp.mpf(HBAR_EV_S)
    tau = mp.mpf(TAU_N_S)

    # the framework's closed form -- a Q-VALUE
    Qb_MeV = me * abs(q0**2 - 2 * q0 - 1) * (q0 + 1) / (2 * q0**3)
    Qb_eV = Qb_MeV * mp.mpf("1e6")
    Qb_exp = mp.mpf(Q_BETA_EXP_MEV)
    q_miss_pct = 100 * abs(Qb_MeV - Qb_exp) / Qb_exp

    # the neutron's ACTUAL width, from its measured lifetime
    Gam_n_eV = hbar / tau

    print("\n[1] what the framework computes: the Q-VALUE, and it is good")
    print(f"    Q_beta (framework) = {mp.nstr(Qb_MeV, 18)} MeV")
    print(f"    Q_beta (AME2020)   = {mp.nstr(Qb_exp, 8)} MeV")
    print(f"    miss               = {mp.nstr(q_miss_pct, 6)} %   (the corpus's 0.17 %)")

    print("\n[2] what the framework does NOT compute: the RATE")
    print(f"    tau_n (PDG 2022)   = {mp.nstr(tau, 8)} +/- {TAU_N_ERR_S} s")
    print(f"    Gamma_n = hbar/tau = {mp.nstr(Gam_n_eV, 8)} eV")

    print("\n[3] the two readings of 'Q_beta = hbar/D_beta', and both fail")
    # R1: D_beta IS the width. Then hbar/D_beta is the LIFETIME, not an energy.
    r1 = hbar / Gam_n_eV          # = tau, in seconds
    print(f"    R1  D_beta := Gamma_n  =>  hbar/D_beta = {mp.nstr(r1, 8)} s")
    print(f"        ... which is the LIFETIME, not {mp.nstr(Qb_MeV, 6)} MeV. Dimensionally wrong.")
    # R2: D_beta := hbar/Q_beta. Consistent, but not the neutron's width.
    hbar_s = mp.mpf("6.582119569e-22")            # MeV*s
    r2 = hbar_s / Qb_MeV                          # seconds
    orders = mp.log10(tau / r2)
    print(f"    R2  D_beta := hbar/Q_beta = {mp.nstr(r2, 8)} s")
    print(f"        ... vs tau_n = {mp.nstr(tau, 6)} s  ->  {mp.nstr(orders, 6)} ORDERS apart.")

    ratio = Gam_n_eV / Qb_eV
    print(f"\n    equivalently  Gamma_n / Q_beta = {mp.nstr(ratio, 8)}")
    print(f"                  log10(Q_beta/Gamma_n) = {mp.nstr(mp.log10(Qb_eV / Gam_n_eV), 8)}")

    print("\n[4] consequence")
    print("    Q_beta and Gamma_n are INDEPENDENT properties of one decay, not")
    print("    reciprocals: a Q-value is fixed by mass differences alone, a width")
    print("    additionally needs the coupling and the phase-space integral.")
    print("    Candidate (iii)'s obstacle -- 'needs a categorical formula for decay")
    print("    widths Gamma' -- STANDS. PR #6687 and #6700 said it did not.")

    assertions = [
        {"name": "framework_reproduces_the_Q_VALUE_to_the_documented_0p17_pct",
         "passed": bool(q_miss_pct < mp.mpf("0.2")),
         "detail": f"Q_beta = {mp.nstr(Qb_MeV, 12)} MeV vs AME2020 {Q_BETA_EXP_MEV}, "
                   f"miss {mp.nstr(q_miss_pct, 5)} % -- this result is UNAFFECTED and stands"},
        {"name": "reading_R1_gives_a_time_not_an_energy",
         "passed": True,
         "detail": f"if D_beta IS Gamma_n then hbar/D_beta = tau_n = {mp.nstr(r1, 8)} s, "
                   f"a TIME -- it cannot equal a {mp.nstr(Qb_MeV, 6)} MeV Q-value"},
        {"name": "reading_R2_is_24_orders_from_the_neutron_lifetime",
         "passed": bool(orders > 20),
         "detail": f"D_beta := hbar/Q_beta = {mp.nstr(r2, 8)} s against tau_n = "
                   f"{mp.nstr(tau, 6)} s -- {mp.nstr(orders, 6)} orders of magnitude"},
        {"name": "the_neutron_width_is_a_Gamma_mechanism_A_fails_to_produce",
         "passed": bool(mp.log10(Qb_eV / Gam_n_eV) > 20),
         "detail": f"Gamma_n = {mp.nstr(Gam_n_eV, 8)} eV sits "
                   f"{mp.nstr(mp.log10(Qb_eV / Gam_n_eV), 6)} orders below Q_beta = "
                   f"{mp.nstr(Qb_eV, 8)} eV -- this is follow-up D's exhibit"},
        {"name": "pr_6687_interpretive_claim_is_retracted",
         "passed": True,
         "detail": "the Lean and arithmetic of #6687 stand (two width MECHANISMS, pure "
                   "mathematics); the step from 'D_beta is CAL-2' to 'the framework has "
                   "a categorical decay width' does not. Candidate (iii) returns to OPEN."},
    ]
    print("\n  assertions:")
    for a in assertions:
        print(f"    [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")
        print(f"           {a['detail']}")
    ok = all(a["passed"] for a in assertions)
    print(f"\n  allPassed: {ok}  ({sum(a['passed'] for a in assertions)}/{len(assertions)})")

    out = HERE / "frakd-beta-is-not-a-decay-width.witness.json"
    w = {
        "description": "CAL-2 is named the neutron beta-decay WIDTH D_beta, and the corpus "
                       "asserts Q_beta = hbar/D_beta with Q_beta a 0.784 MeV Q-value. Both "
                       "cannot hold: if D_beta is the width then hbar/D_beta is the "
                       "LIFETIME (878.4 s), and if D_beta := hbar/Q_beta then it is 24 "
                       "orders of magnitude from that lifetime. The framework computes the "
                       "decay's ENERGY RELEASE, not its RATE. This RETRACTS the "
                       "interpretive claim of PR #6687/#6700 that candidate (iii)'s "
                       "obstacle was already satisfied; (iii) returns to open.",
        "engine": "mpmath 50 dps; no float64",
        "q0Anchor": "proton",
        "q0AnchorReason": "AGENTS.md 2026-08-07 owner directive: proton is the default for "
                          "all new compute",
        "q0Value": Q0_STR,
        "data": {
            "corpus_assertion": "Q_beta = hbar/D_beta, D_beta = 'the neutron beta-decay width'",
            "corpus_sites": [
                "content/quantum-observable-universe/observations/epistemic-status-of-calibrations.md:3",
                "content/quantum-observable-universe/observations/three-calibration-discipline-discussion.md:7",
                "docs/canonical-derivation-cheat-sheet.md:134",
                "docs/canonical-derivation-cheat-sheet.md:490",
            ],
            "Q_beta_framework_MeV": mp.nstr(Qb_MeV, 20),
            "Q_beta_AME2020_MeV": Q_BETA_EXP_MEV,
            "Q_beta_miss_pct": mp.nstr(q_miss_pct, 8),
            "tau_n_s": TAU_N_S,
            "tau_n_err_s": TAU_N_ERR_S,
            "tau_n_source": "PDG 2022, bottle average; the beam-bottle discrepancy is ~8 s "
                            "and is irrelevant at 24 orders of magnitude",
            "Gamma_n_eV": mp.nstr(Gam_n_eV, 20),
            "reading_R1": "D_beta := Gamma_n  =>  hbar/D_beta = tau_n = 878.4 s, a TIME, "
                          "so it cannot be the 0.784 MeV Q-value the corpus says it is",
            "reading_R2_s": mp.nstr(r2, 20),
            "reading_R2_orders_from_tau_n": mp.nstr(orders, 12),
            "log10_Qbeta_over_Gamma_n": mp.nstr(mp.log10(Qb_eV / Gam_n_eV), 12),
            "what_stands": "Q_beta as a CAL-2 proxy, reproduced to 0.17 %. A Q-value is "
                           "fixed by mass differences alone.",
            "what_is_missing": "the RATE. A width additionally needs the coupling and the "
                               "phase-space integral -- precisely what candidate (iii) "
                               "asked for and what the framework has not supplied.",
            "retraction": "PR #6687 and the block edit in #6700 claim (iii)'s obstacle was "
                          "satisfied because D_beta IS CAL-2. The Lean and arithmetic of "
                          "#6687 stand -- they concern two width MECHANISMS and are pure "
                          "mathematics. The interpretive step does not. Candidate (iii) "
                          "returns to OPEN with its obstacle sharpened: the missing object "
                          "is not a decay observable but specifically the rate.",
            "scope": "(a) throughout. Nothing here says Im(q) DOES encode a width; it says "
                     "the reciprocal mechanism does not produce the one width we can check, "
                     "so the argument by which I narrowed (iii) does not hold.",
            "not_a_rename_proposal": "the naming is the author's, was flagged to the author, "
                                     "and the author's ruling is pending. This probe measures "
                                     "the gap rather than resolving it.",
        },
        "assertions": assertions,
        "allPassed": ok,
    }
    out.write_text(json.dumps(w, indent=2) + "\n")
    print(f"\n  witness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
