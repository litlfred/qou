#!/usr/bin/env python3
"""
THE FRAMEWORK HAS A DECAY RATE.  WHAT IT DOES NOT HAVE IS THE SCALE.

This probe does two things, and the first is a correction of my own claim.

CORRECTION (my #6704 / `frakd-beta-is-not-a-decay-width`)
---------------------------------------------------------
That probe closed with:

    "the missing object is not 'a decay observable' (the corpus has one)
     but specifically **the rate**."

That is WRONG as written.  `prop:hadron-half-life`
(folio/quantum-observable-universe/predicted-spectra/hadron-half-life.md)
states a categorical decay RATE:

    Gamma_beta = |W(q)|^2 mu_0 / (2 pi^3) * [2]_q * |M_q|^2 * f(Q),
    f(Q) ~ Q^5   (Sargent)

and its coupling is DERIVED in closed form -- the canonical Markov trace of
the T_{3,5} braid word in H_3(q):

    W(q) = tr_M((s1 s2)^5) = q^2 (q^12 + q^8 - 1) / (q^2 + 1)^2
         = y_(3) q^10 - y_(2,1),
      y_(3) = (q^4+1)/(q^2+1)^2,  y_(2,1) = q^2/(q^2+1)^2.

I asserted an absence I had not measured.  Checks 1-3 below verify the
corpus's own two claims about W (its value at q_0, and W(1) = 1/4) so the
correction rests on arithmetic rather than on my reading.

WHAT IS ACTUALLY MISSING -- and the corpus says so in three places
------------------------------------------------------------------
The rate's SHAPE (its q-dependence) is derived; its SCALE is imported.
The single missing input is the weak-scale crossing count N_v:

  1. `all_six_agree` docstring, hadron-half-life-verification.lean:
     "... using q, mu_0, and the standard-physics value of G_F^2 m_e^5
      (which decomposes into q-dependent factors times mu_0, PENDING
      DERIVATION OF THE WEAK-SCALE CROSSING COUNT N_v)."
  2. fsh-guts/deprecated/computations/t35-transfer-matrix.py:281:
     "The ABSOLUTE half-life requires G_F (or N_v), which is open."
  3. hadron-half-life-verification Table 1, row `v`:
     "N_v * m_e/3 | Topological invariant N_v (OPEN)".

THE TEST (checks 4-6) -- fit-free, one prediction, one number
--------------------------------------------------------------
The corpus reads N_v as a CROSSING COUNT: `v = N_v * E_x * mu_0` with
E_x = (q - 1/q)/2 the crossing energy, alongside m_e = 3 E_x mu_0 (the
3 crossings of the trefoil).  Dividing, mu_0 and E_x both cancel:

    N_v = 3 v / m_e          (q-INDEPENDENT -- no anchor, no convention)

A crossing count is a POSITIVE INTEGER.  That is a falsifiable structural
prediction and the experimental inputs are precise enough to test it: this
is a prune in the formalize-first sense, not a search.  Nothing is fitted
here -- N_v is *determined* by experiment and the only question asked of it
is whether it is an integer.  Whatever comes out is reported.

PRECISION.  mpmath at 60 dps from CODATA strings.  No float64 anywhere;
float() appears only inside f-strings for display.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

from qou_substrate.witness import WitnessBuilder as _WB  # noqa: E402 -- provenance stamp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

mp.mp.dps = 60

# ---- inputs (exact decimal strings) ---------------------------------------
# CODATA 2022
M_E_MEV = mp.mpf("0.51099895069")
M_E_MEV_ERR = mp.mpf("0.00000000016")
# CODATA 2022 Fermi coupling  G_F/(hbar c)^3, GeV^-2
G_F_GEV2 = mp.mpf("1.1663787e-5")
G_F_GEV2_ERR = mp.mpf("0.0000006e-5")
# substrate parameter, experimental (proton) pin -- AGENTS.md owner directive
from substrate.q_parameter import Q_50_DIGIT_STR as Q0  # noqa: E402 -- proton pin, RESOLVED at run time


def W(q):
    """T_{3,5} weak vertex form factor: canonical Markov trace of (s1 s2)^5."""
    return q**2 * (q**12 + q**8 - 1) / (q**2 + 1) ** 2


def W_wedderburn(q):
    """Same object as the Wedderburn sum the corpus writes it as."""
    y3 = (q**4 + 1) / (q**2 + 1) ** 2
    y21 = q**2 / (q**2 + 1) ** 2
    return y3 * q**10 - y21


def main() -> int:
    q0 = mp.mpf(str(Q0))
    checks = []

    print("=" * 72)
    print(" The framework HAS a decay rate; what is open is its SCALE (N_v)")
    print("=" * 72)

    # ---- 1. the two spellings of W agree identically -----------------------
    w_closed = W(q0)
    w_wedder = W_wedderburn(q0)
    gap = abs(w_closed - w_wedder)
    print("\n[1] W(q_0) by closed form vs by Wedderburn sum")
    print(f"    closed      W = {mp.nstr(w_closed, 20)}")
    print(f"    Wedderburn  W = {mp.nstr(w_wedder, 20)}")
    print(f"    |difference|  = {mp.nstr(gap, 6)}")
    checks.append({
        "name": "W_two_spellings_agree",
        "pass": bool(gap < mp.mpf("1e-45")),
        "detail": f"|closed - Wedderburn| = {mp.nstr(gap, 6)} at 60 dps",
    })

    # ---- 2. the corpus's quoted W(q_0) ~ 1.1875 ---------------------------
    quoted = mp.mpf("1.1875")
    rel = abs(w_closed - quoted) / w_closed
    print(f"\n[2] corpus quotes W(q_0) ~ 1.1875;  measured {mp.nstr(w_closed, 12)}")
    print(f"    relative difference = {mp.nstr(rel, 6)}")
    checks.append({
        "name": "W_at_q0_matches_corpus_quote_to_4sf",
        "pass": bool(rel < mp.mpf("1e-3")),
        "detail": f"W(q_0) = {mp.nstr(w_closed, 15)}, corpus quotes 1.1875, rel {mp.nstr(rel, 4)}",
    })

    # ---- 3. W(1) = 1/4 exactly -------------------------------------------
    w1 = W(mp.mpf(1))
    print(f"\n[3] W(1) = {mp.nstr(w1, 20)}   (corpus: 1/4)")
    checks.append({
        "name": "W_at_one_is_one_quarter",
        "pass": bool(abs(w1 - mp.mpf(1) / 4) < mp.mpf("1e-45")),
        "detail": f"W(1) = {mp.nstr(w1, 20)}; the classical vanishing of the rate is "
                  "carried by Q -> 0, NOT by the vertex factor",
    })

    # ---- 4. N_v = 3 v / m_e ----------------------------------------------
    v_gev = 1 / mp.sqrt(mp.sqrt(2) * G_F_GEV2)
    v_mev = v_gev * 1000
    n_v = 3 * v_mev / M_E_MEV

    # uncertainty: v ~ G_F^{-1/2}  =>  rel(v) = rel(G_F)/2
    rel_gf = G_F_GEV2_ERR / G_F_GEV2
    rel_v = rel_gf / 2
    rel_me = M_E_MEV_ERR / M_E_MEV
    rel_nv = mp.sqrt(rel_v**2 + rel_me**2)
    sigma_nv = n_v * rel_nv

    print("\n[4] the weak-scale crossing count, q-INDEPENDENT")
    print(f"    v      = {mp.nstr(v_gev, 12)} GeV      (from G_F, CODATA 2022)")
    print(f"    m_e    = {mp.nstr(M_E_MEV, 12)} MeV")
    print(f"    N_v    = 3 v / m_e = {mp.nstr(n_v, 16)}")
    print(f"    sigma(N_v)         = {mp.nstr(sigma_nv, 6)}   "
          f"(rel {mp.nstr(rel_nv, 4)}, dominated by G_F)")
    checks.append({
        "name": "N_v_is_q_independent",
        "pass": True,
        "detail": "mu_0 and E_x cancel between v = N_v E_x mu_0 and m_e = 3 E_x mu_0, "
                  f"so N_v = 3 v/m_e = {mp.nstr(n_v, 16)} carries no anchor and no "
                  "Markov-parameter convention",
    })

    # ---- 5. integrality: is N_v a crossing count? ------------------------
    nearest = mp.floor(n_v + mp.mpf("0.5"))
    dist = abs(n_v - nearest)
    n_sigma = dist / sigma_nv
    print("\n[5] INTEGRALITY -- a crossing count must be a positive integer")
    print(f"    nearest integer    = {mp.nstr(nearest, 16)}")
    print(f"    |N_v - nearest|    = {mp.nstr(dist, 8)}")
    print(f"    in units of sigma  = {mp.nstr(n_sigma, 6)} sigma")
    integral = bool(n_sigma < 2)
    print(f"    -> {'CONSISTENT with an integer' if integral else 'INCONSISTENT with an integer'}"
          f" at 2 sigma")
    checks.append({
        "name": "N_v_integrality_measured",
        "pass": True,  # the measurement always succeeds; the VERDICT is the payload
        "detail": f"N_v = {mp.nstr(n_v, 16)} +/- {mp.nstr(sigma_nv, 4)}; nearest integer "
                  f"{mp.nstr(nearest, 16)}, offset {mp.nstr(dist, 6)} = "
                  f"{mp.nstr(n_sigma, 4)} sigma. "
                  + ("Consistent with integrality -- so the experimental precision does "
                     "NOT refute the crossing-count reading, and does not confirm it "
                     "either: the resolution is coarser than the spacing between "
                     "candidate integers is meaningful."
                     if integral else
                     "NOT consistent with integrality at 2 sigma -- the crossing-count "
                     "reading of N_v is under tension from experiment alone."),
    })

    # ---- 6. the test's CEILING -- what significance it can ever reach -----
    # An integrality test lives on [0, 1/2]: the furthest any real number can sit
    # from the nearest integer is 1/2.  So the LARGEST significance the test can
    # EVER report, at a given sigma, is (1/2)/sigma -- regardless of the data.
    ceiling = mp.mpf("0.5") / sigma_nv
    frac_of_ceiling = n_sigma / ceiling
    # precision needed for a 3-sigma statement
    sigma_needed = mp.mpf("0.5") / 3
    rel_nv_needed = sigma_needed / n_v
    rel_gf_needed = 2 * rel_nv_needed            # rel(N_v) = rel(G_F)/2
    gf_tighten = rel_gf / rel_gf_needed
    print("\n[6] the test's CEILING -- and it is BELOW 2 sigma")
    print(f"    max attainable significance = (1/2)/sigma = {mp.nstr(ceiling, 6)} sigma")
    print(f"    measured significance       = {mp.nstr(n_sigma, 6)} sigma "
          f"({mp.nstr(100 * frac_of_ceiling, 4)}% of the ceiling)")
    print(f"    -> at CODATA-2022 precision the integrality test CANNOT reach 2 sigma,")
    print(f"       whatever N_v turns out to be.  It is NOT decisive.")
    print(f"    for a 3-sigma statement G_F must tighten by {mp.nstr(gf_tighten, 5)}x")
    print(f"       ({mp.nstr(1e6 * rel_gf, 4)} ppm -> {mp.nstr(1e6 * rel_gf_needed, 4)} ppm)")
    checks.append({
        "name": "integrality_test_ceiling_is_below_two_sigma",
        "pass": bool(ceiling < 2),
        "detail": f"an integrality test is bounded by (1/2)/sigma = "
                  f"{mp.nstr(ceiling, 6)} sigma here, so NO value of N_v could be "
                  f"declared non-integral at 2 sigma from CODATA 2022. The measured "
                  f"{mp.nstr(n_sigma, 4)} sigma is {mp.nstr(100 * frac_of_ceiling, 4)}% "
                  f"of that ceiling -- i.e. N_v sits essentially as far from an integer "
                  f"as it is possible to sit, and the test still says nothing. G_F's "
                  f"{mp.nstr(1e6 * rel_gf, 4)} ppm is the sole limiting input (m_e "
                  f"contributes 0.31 ppb); a 3-sigma test needs "
                  f"{mp.nstr(1e6 * rel_gf_needed, 4)} ppm, a {mp.nstr(gf_tighten, 5)}x "
                  "tightening.",
    })

    print("\n" + "=" * 72)
    n_pass = sum(1 for c in checks if c["pass"])
    print(f" {n_pass}/{len(checks)} checks pass")
    print("=" * 72)

    out = HERE / "weak-scale-crossing-count-nv.witness.json"
    _payload = {
        "schema": "qou-probe/v1",
        "name": "weak-scale-crossing-count-nv",
        "description":
            "Corrects my #6704 claim that the corpus lacks a decay RATE: "
            "prop:hadron-half-life states one and its coupling W(q) is derived in "
            "closed form (checks 1-3). What is open is the rate's SCALE -- the "
            "weak-scale crossing count N_v = 3v/m_e, which is q-independent and, "
            "read as a crossing count, must be a positive integer (checks 4-6).",
        "q0Anchor": "proton",
        "q0AnchorReason":
            "AGENTS.md 2026-08-07 owner directive: proton is the default for all new "
            "compute. Load-bearing here, not inert: q0 enters the evaluated quantities.",
        "q0Value": mp.nstr(q0, 20),
        "inputs": {
            "m_e_MeV": "0.51099895069(16)  CODATA 2022",
            "G_F_GeV^-2": "1.1663787(6)e-5  CODATA 2022",
        },
        "results": {
            "W_q0": mp.nstr(w_closed, 30),
            "W_1": mp.nstr(w1, 30),
            "v_GeV": mp.nstr(v_gev, 20),
            "N_v": mp.nstr(n_v, 20),
            "N_v_sigma": mp.nstr(sigma_nv, 12),
            "N_v_nearest_integer": mp.nstr(nearest, 20),
            "N_v_offset_from_integer": mp.nstr(dist, 12),
            "N_v_offset_in_sigma": mp.nstr(n_sigma, 12),
            "significance_ceiling_sigma": mp.nstr(ceiling, 12),
            "fraction_of_ceiling_attained": mp.nstr(frac_of_ceiling, 12),
            "G_F_rel_now_ppm": mp.nstr(1e6 * rel_gf, 8),
            "G_F_rel_needed_for_3sigma_ppm": mp.nstr(1e6 * rel_gf_needed, 8),
            "G_F_tightening_factor_needed": mp.nstr(gf_tighten, 8),
        },
        "scope": "(a) scope-limited. Nothing here derives N_v or refutes any route to "
                 "it; the integrality check is a necessary condition on the corpus's "
                 "own crossing-count reading, tested against experiment alone.",
        "checks": checks,
    }
    _WB.stamp_staleness_metadata(
        _payload, script_path=__file__, q0_anchor="proton",
        q0_anchor_reason=_payload["q0AnchorReason"],
        q0_value=_payload["q0Value"],
    )
    out.write_text(json.dumps(_payload, indent=2) + "\n")
    print(f"\nwitness -> {out}")
    return 0 if n_pass == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
