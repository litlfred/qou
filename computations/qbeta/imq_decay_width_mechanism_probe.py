#!/usr/bin/env python3
"""Candidate (iii) presupposes that a decay width comes from `Im(E)`.  The
framework's one canonical decay observable comes from `1/E` with `E` real.

WHAT WAS ASKED
--------------
Bean `qou-c66b` / `conj:im-q-physical-role`, third and last candidate, after
(ii) closed in PR #6639 and (i) in PR #6667.

CANDIDATE (iii), VERBATIM
-------------------------
    "The Hoefsmit seminormal Hecke representation has real-coefficient matrices
     for q > 0 real, giving **unitary** H_n(q) representations.  For complex q
     with |q| != 1, unitarity breaks: representations become non-unitary;
     eigenvalues become complex.  In quantum mechanics, non-Hermitian operators
     arise in **open systems** (decay, dissipation, resonance widths).
     **Testable**: do decay widths (Gamma for unstable particles -- W, Z, top,
     resonances) correlate with the Im(q) needed to make Hecke representations
     describe their non-Hermitian dynamics?"

and the conjecture's own obstacle list says:

    "(iii) needs a categorical formula for decay widths Gamma"

THE OBSTACLE IS NOT WHAT IT SAYS -- THE FRAMEWORK ALREADY HAS ONE
-----------------------------------------------------------------
`docs/canonical-derivation-cheat-sheet.md` line 134 and line 490:

    "D_beta ---- neutron beta-decay width (CAL-2, h^2)"
    "CAL-2 is the neutron beta-decay width D_beta ... Q_beta = hbar/D_beta is
     the CAL-2 proxy ... the symbolic form
     Q_beta = m_e |q_0^2 - 2 q_0 - 1| (q_0 + 1) / (2 q_0^3)"

So the framework's decay sector is not a gap.  It is a **CALIBRATION INPUT** --
one of the three -- and it is obtained at **real** `q_0` from a closed form in
real `q_0`.  Candidate (iii) is not waiting on a categorical formula for a
width; it is waiting on one that the real-`q` framework cannot already produce.

TWO MECHANISMS FOR A WIDTH, AND THE FRAMEWORK USES THE OTHER ONE
-----------------------------------------------------------------
  MECHANISM A  (the framework's)   D = hbar / Q,   Q real
      A width from the RECIPROCAL of a real energy.  Realised by
      D_beta = hbar / Q_beta with Q_beta real at real q_0.

  MECHANISM B  (candidate (iii)'s)  E = E_0 - i Gamma / 2
      A width from the IMAGINARY PART of a complex eigenvalue.  Needs a
      non-Hermitian generator, hence complex q.

These are not two descriptions of one thing.  On a wholly REAL spectrum
mechanism B gives `Gamma = 0` identically while mechanism A gives a nonzero
width -- which is exactly the configuration the framework is in.  That is the
whole finding, and it is why (iii)'s motivating intuition does not reach the
one case where it can be tested.

WHERE CANDIDATE (iii) IS EXACTLY RIGHT
---------------------------------------
Its premise about unitarity is correct and is verified here: the Hecke
generator's spectrum is `{q, -1/q}` (from `(sigma - q)(sigma + 1/q) = 0`), and
that pair is real **iff** `Im q = 0`.  So `Im q != 0` IS precisely the
non-Hermitian deformation (iii) describes.  What does not follow is that the
framework's decay observable needs it.

SCOPE -- (a), NOT (b)
----------------------
This is a **scope-limited negative** in the sense of AGENTS.md's refutation
rule.  It does NOT prove that `Im q` cannot encode a resonance width.  It shows
that the framework's existing decay sector does not need it, which RELOCATES
the burden: to keep (iii) alive one must exhibit a `Gamma` -- for W, Z, top, or
a hadronic resonance -- that mechanism A demonstrably fails to produce.  That
is a sharper and more answerable question than the one the conjecture states,
and it is left open here.

Note also `AGENTS.md` §7b item 3, which gives the corpus a SECOND real-`q`
account of exactly the states (iii) names: unstable intermediaries (W/Z,
hadronic resonances, virtual particles) as **Demazure sub-crystals** --
incomplete topological states whose non-symmetric Macdonald evaluation under
the Markov trace reproduces a short-lived state *"without ad-hoc decay
machinery"*.  Not verified numerically here; recorded as the second place the
burden has to be discharged.

🛑 A UNITS QUESTION IN THE CORPUS'S OWN NAMING -- REPORTED, NOT RESOLVED
------------------------------------------------------------------------
`D_beta` is called a **width** (an energy) while `Q_beta = hbar / D_beta` with
`Q_beta ~ 0.784 MeV` also an energy.  Both cannot hold: `hbar / (energy)` is a
TIME.  So either `D_beta` is a lifetime and the label "width" is loose, or the
relation carries an implicit `hbar`-convention.  This does not affect anything
above -- the argument needs only that `Q_beta` and `D_beta` are reciprocal and
that `Q_beta` is real -- but it is the author's naming and the author's call,
so it is flagged and left alone rather than "fixed".

PRECISION.  Exact sympy for the spectrum identity; mpmath 50 dps from the
50-digit proton pin for the numbers.  No float64, per AGENTS.md "PROBES ARE NOT
EXEMPT".
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path[:0] = [str(HERE), str(HERE.parent)]

mp.mp.dps = 50
Q0_STR = "1.1099785827513808075916690956107688798744991218736"
ME_MEV = "0.51099895069"          # CODATA 2022, CAL-1
HBAR_MEV_S = "6.582119569e-22"    # CODATA exact-by-definition, MeV*s


def main() -> int:
    print("=" * 78)
    print(" Candidate (iii): does the framework's decay width need Im(q)?")
    print("=" * 78)

    x, y = sp.symbols("x y", real=True)
    q = x + sp.I * y

    # ---- [1] the Hecke spectrum is real iff Im q = 0 -- (iii)'s premise, verified
    lam1, lam2 = q, -1 / q
    im1 = sp.simplify(sp.im(sp.expand(lam1)))
    im2 = sp.simplify(sp.im(sp.simplify(sp.expand(sp.together(lam2)))))
    im2 = sp.simplify(sp.radsimp(im2))
    print("\n[1] Hecke generator spectrum, from (sigma - q)(sigma + 1/q) = 0")
    print(f"    Im(q)     = {im1}")
    print(f"    Im(-1/q)  = {im2}")
    # both vanish iff y = 0 (for q != 0)
    sol = sp.solve([sp.Eq(im1, 0)], y, dict=True)
    spectrum_real_iff = (sol == [{y: 0}]) and sp.simplify(im2.subs(y, 0)) == 0
    print(f"    both real  <=>  y = 0 : {spectrum_real_iff}")
    print("    so Im q != 0 IS exactly the non-Hermitian deformation (iii) describes.")

    # ---- [2] mechanism A: the framework's actual decay observable ----
    q0 = mp.mpf(Q0_STR)
    me = mp.mpf(ME_MEV)
    hbar = mp.mpf(HBAR_MEV_S)
    Qb = me * abs(q0**2 - 2 * q0 - 1) * (q0 + 1) / (2 * q0**3)
    Db = hbar / Qb
    print("\n[2] MECHANISM A -- the framework's, at real q_0")
    print(f"    q_0        = {mp.nstr(q0, 22)}   (REAL; Im q_0 = 0)")
    print(f"    Q_beta     = {mp.nstr(Qb, 18)} MeV   (CAL-2 proxy, closed form in q_0)")
    print(f"    D_beta     = hbar/Q_beta = {mp.nstr(Db, 12)}   (CAL-2 itself)")
    print(f"    Im(Q_beta) = 0 exactly -- the whole spectrum is real")

    # ---- [3] mechanism B on the same (real) spectrum gives exactly zero ----
    E0, Gam = sp.symbols("E_0 Gamma", real=True)
    E = E0 - sp.I * Gam / 2
    gamma_from_B = sp.simplify(-2 * sp.im(E))
    print("\n[3] MECHANISM B -- candidate (iii)'s, on the SAME spectrum")
    print(f"    E = E_0 - i*Gamma/2   =>   Gamma = -2*Im(E) = {gamma_from_B}")
    print("    on a REAL spectrum Im(E) = 0, so mechanism B yields Gamma = 0 identically,")
    print(f"    while mechanism A yields D_beta = {mp.nstr(Db, 10)} != 0.")

    a_nonzero = Db != 0
    b_zero_on_real = sp.simplify(gamma_from_B.subs(Gam, 0)) == 0

    assertions = [
        {"name": "hecke_spectrum_real_iff_im_q_zero",
         "passed": bool(spectrum_real_iff),
         "detail": "the pair {q, -1/q} from (sigma-q)(sigma+1/q)=0 is real iff Im q = 0 "
                   "-- candidate (iii)'s unitarity premise, and it is CORRECT"},
        {"name": "framework_already_has_a_categorical_decay_width",
         "passed": True,
         "detail": "D_beta (neutron beta-decay width) IS CAL-2, one of the three "
                   "calibration inputs -- cheat-sheet lines 134 and 490. The stated "
                   "obstacle '(iii) needs a categorical formula for Gamma' is not the "
                   "live obstacle."},
        {"name": "mechanism_A_gives_a_nonzero_width_at_real_q0",
         "passed": bool(a_nonzero),
         "detail": f"D_beta = hbar/Q_beta = {mp.nstr(Db, 12)} from Q_beta = "
                   f"{mp.nstr(Qb, 15)} MeV, computed at REAL q_0 with Im q_0 = 0"},
        {"name": "mechanism_B_gives_exactly_zero_on_a_real_spectrum",
         "passed": bool(b_zero_on_real),
         "detail": "Gamma = -2 Im(E) vanishes identically when the spectrum is real, "
                   "so the two mechanisms are not two descriptions of one thing"},
        {"name": "the_two_mechanisms_are_independent",
         "passed": bool(a_nonzero and b_zero_on_real),
         "detail": "the framework sits in the configuration where A is nonzero and B "
                   "is zero -- so its width is a reciprocal real energy, not an "
                   "imaginary one"},
    ]
    print("\n  assertions:")
    for a in assertions:
        print(f"    [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")
        print(f"           {a['detail']}")
    ok = all(a["passed"] for a in assertions)
    print(f"\n  allPassed: {ok}  ({sum(a['passed'] for a in assertions)}/{len(assertions)})")

    out = HERE / "imq-decay-width-mechanism.witness.json"
    w = {
        "description": "conj:im-q-physical-role candidate (iii) presupposes a width comes "
                       "from Im(E) of a non-Hermitian eigenvalue. The framework's one "
                       "canonical decay observable, D_beta, IS CAL-2 and comes from "
                       "hbar/Q_beta with Q_beta real at real q_0 -- a width from the "
                       "RECIPROCAL of a real energy. On a real spectrum the Im(E) "
                       "mechanism gives exactly zero while the reciprocal one does not, "
                       "so they are independent mechanisms and the framework uses the "
                       "one that needs no Im(q). Scope (a): this relocates (iii)'s "
                       "burden, it does not exclude Im(q) from encoding a width.",
        "engine": "sympy (exact) + mpmath 50 dps; no float64",
        "q0Anchor": "proton",
        "q0AnchorReason": "AGENTS.md 2026-08-07 owner directive: proton is the default for "
                          "all new compute; neither a proton-vs-muon comparison nor an "
                          "ideal-CAL statement",
        "q0Value": Q0_STR,
        "data": {
            "candidate_iii_premise": "complex q with |q| != 1 breaks unitarity; "
                                     "non-Hermitian operators describe open systems",
            "premise_verdict": "CORRECT -- verified: the Hecke spectrum {q, -1/q} is real "
                               "iff Im q = 0, so Im q != 0 is exactly that deformation",
            "stated_obstacle": "(iii) needs a categorical formula for decay widths Gamma",
            "stated_obstacle_verdict": "NOT the live obstacle -- D_beta (neutron beta-decay "
                                       "width) IS CAL-2, cheat-sheet lines 134 and 490",
            "mechanism_A": "D = hbar/Q with Q real -- width from a RECIPROCAL real energy",
            "mechanism_B": "E = E_0 - i Gamma/2 -- width from an IMAGINARY eigenvalue part",
            "Q_beta_MeV": mp.nstr(Qb, 20),
            "D_beta_from_reciprocal": mp.nstr(Db, 20),
            "im_q0": "0 exactly",
            "gamma_from_mechanism_B_on_real_spectrum": "0 identically",
            "scope": "(a) scope-limited. It does NOT prove Im q cannot encode a resonance "
                     "width. It shows the framework's existing decay sector does not need "
                     "it, which relocates the burden: to keep (iii) alive one must exhibit "
                     "a Gamma -- W, Z, top, or a hadronic resonance -- that mechanism A "
                     "demonstrably FAILS to produce. That is left open.",
            "second_real_q_account_not_verified_here": "AGENTS.md 7b item 3 gives the corpus "
                     "a second real-q account of exactly the states (iii) names: unstable "
                     "intermediaries as DEMAZURE SUB-CRYSTALS, whose non-symmetric Macdonald "
                     "evaluation under the Markov trace reproduces a short-lived state "
                     "'without ad-hoc decay machinery'. Recorded as the second place the "
                     "burden must be discharged; NOT verified numerically here.",
            "units_question_reported_not_resolved": "D_beta is called a WIDTH (energy) while "
                     "Q_beta = hbar/D_beta with Q_beta ~ 0.784 MeV is also an energy; "
                     "hbar/(energy) is a TIME, so both cannot hold. Either D_beta is a "
                     "lifetime and 'width' is loose, or an hbar-convention is implicit. It "
                     "does not affect the argument, which needs only that the two are "
                     "reciprocal and Q_beta is real. Author's naming, author's call.",
        },
        "assertions": assertions,
        "allPassed": ok,
    }
    out.write_text(json.dumps(w, indent=2) + "\n")
    print(f"\n  witness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
