#!/usr/bin/env python3
"""MEASURE `binding_energy(1, 1)` after the UIC Pass-2 sign-gate drop.

Bean `qou-21oc`; PR #7253.  The post-drop deuteron value in
`docs/audits/2026-09-02-binding-energy-first-corrected-value.md` was written
**by arithmetic** on that document's own three-term decomposition and marked
"derived, NOT measured":

    binding_energy = unified_iterative_correction    (term 1, gate touches this)
                   + sdp_cross_channel_contribution  (term 2)
                   + binding_from_frobenius_pairing  (term 3)

    derived:  -17.6908290020795 + 0.0 + 1.876634106  =  -15.8141948960795

That terms 2 and 3 are gate-independent was established by **reading**
`binding_energy`, never by running it.  This script is the first run of the
public function since the drop, i.e. the first test of that reading.

TIER.  Every number here is at the production default
`k_exact = k_max = K_PARTITION_MAX = 11`.  The UIC total is strongly
`k_exact`-dependent (43x across the tiers), so a bare figure is meaningless --
the widely-quoted "4.6x" gate factor is the `k_exact = 4` tier and is 2.4x too
large for this one, where the factor is 1.934x.

PRECISION.  `binding_energy` returns `float(B)` by public contract (bean
`qou-sv7h`), so any comparison through the public return is a **53-bit**
comparison and is labelled as such below.  The accumulator's own total is
carried as `mpf` and is read from `per_step[-1]['raw_total_MeV']`; all
arithmetic here is `mpmath.mpf`, with `float()` only inside f-strings.

This script writes NO witness: it re-runs committed producers and reports, and
a witness write would dirty sibling files it never targeted.

RESULT, 2026-09-13, kernel live (`pyhecke_native 0.9.0`), COMPUTE_DPS = 70,
tier `k_exact = k_max = 11`, 2361.9 s total:

    term 1  unified_iterative_correction    -17.69082900207954470792...   413.6 s
    term 2  sdp_cross_channel_contribution    0.0          (float)          0.0 s
    term 3  binding_from_frobenius_pairing   +1.87663410614413633433...   768.3 s
    sum of terms (mpf)                      -15.81419489593540837358...
    binding_energy(1, 1)  (public float)    -15.81419489593541          1180.0 s

THE READING WAS RIGHT: terms 2 and 3 are gate-independent, now measured rather
than inferred, and the additive decomposition holds.  The measured cell differs
from the audit's DERIVED `-15.8141948960795` by `+1.44091626e-10` MeV (relative
`9.11e-12`), and that offset is ENTIRELY the banner's own quoting precision --
term 3 quoted at 10 s.f. contributes `+1.44136334e-10` and term 1 at 15 s.f.
contributes `-4.47079e-14`, summing to `+1.44091626e-10` with a remainder of
`-9.3e-61` (the 60-dps floor).  It is not a discrepancy.

Two checks that fall out of the same run: the public float sits `-1.57e-15` from
the mpf sum (relative `9.94e-17` < `2^-53`), i.e. exactly the cast at the return;
and the measured terms reproduce the ORIGINAL gated total,
`-9.14773623102088124311 + 1.87663410614413633433 = -7.27110212487674490878`,
against the `-7.271102125` the 2026-09-02 audit printed.

Against AME2020 `+2.22456607 MeV` the `|ratio|` goes `3.26855x -> 7.10889x` and
the residual `9.4956682 -> 18.038761 MeV`.  WORSE, and that is the honest
outcome: the drop buys honesty, not accuracy.

Wall: ~2 UIC runs at the production default, ~40 min total.  Launch as
    python3 -u computations/binding_energy_ungated_deuteron_measurement.py \
        2>&1 | tee /tmp/binding_energy_ungated_deuteron_measurement.log
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import _path_bridge  # noqa: F401, E402 -- MUST follow the sys.path insert above
import mpmath as mp  # noqa: E402

from _precision import COMPUTE_DPS, fmt, set_compute_dps  # noqa: E402

set_compute_dps()

import hecke_core_legacy as H  # noqa: E402

# The value the audit banner carries as DERIVED, as an exact decimal string.
DERIVED_STR = "-15.8141948960795"
# The three terms the audit's decomposition asserts, as exact decimal strings.
DERIVED_TERM1_STR = "-17.6908290020795"
DERIVED_TERM2_STR = "0.0"
DERIVED_TERM3_STR = "1.876634106"

T0 = time.time()


def _say(msg):
    print(f"[{time.time() - T0:8.1f}s] {msg}", flush=True)


def _rel(a, b):
    """Relative difference |a-b|/|b| as mpf; b is the reference."""
    if b == 0:
        return mp.mpf("nan") if a != 0 else mp.mpf(0)
    return abs(a - b) / abs(b)


def main():
    _say(f"COMPUTE_DPS = {COMPUTE_DPS}, mp.dps = {mp.mp.dps}")
    _say(f"_HAS_LP_KERNEL = {H._HAS_LP_KERNEL}  (False => fallback arm, ~6.3 h)")
    _say(f"K_PARTITION_MAX = {H.K_PARTITION_MAX}  "
         f"(tier: k_exact = k_max = {H.K_PARTITION_MAX})")
    if not H._HAS_LP_KERNEL:
        _say("REFUSING: the Rust kernel is absent.  The 942 s reference run "
             "was kernel-live; a fallback run is a different measurement and "
             "must not be compared against the derived cell.")
        return 2

    # ---- Phase A: the public function, exactly as the audit cell names it ----
    _say("Phase A: binding_energy(1, 1) -- the public call.  ~942 s expected.")
    a0 = time.time()
    b_public = H.binding_energy(1, 1)
    a_wall = time.time() - a0
    _say(f"Phase A done in {a_wall:.1f} s")
    _say(f"  binding_energy(1,1) = {b_public!r}   (float64, 53-bit)")

    # ---- Phase B: the three terms, so a mismatch is attributable ----
    _say("Phase B: the three terms separately.  UIC re-runs, ~425 s.")
    b0 = time.time()
    t1_float, per_step = H.unified_iterative_correction(
        1, 1, return_per_step=True,
        k_max=H.K_PARTITION_MAX, k_exact=H.K_PARTITION_MAX)
    t1_wall = time.time() - b0
    last = per_step[-1]
    t1_mpf = last.get("raw_total_MeV")
    t1_gated = last.get("gated_total_DISPROVED_SELECTION_MeV")
    _say(f"  term 1 (UIC) in {t1_wall:.1f} s")
    _say(f"    ungated, mpf   = {fmt(t1_mpf) if t1_mpf is not None else 'ABSENT'}")
    _say(f"    ungated, float = {t1_float!r}")
    _say(f"    gated  (DISPROVED selection, historical) = "
         f"{fmt(t1_gated) if t1_gated is not None else 'ABSENT'}")

    c0 = time.time()
    t2, _sdp_pairs = H.sdp_cross_channel_contribution(1, 1)
    _say(f"  term 2 (sdp_cross_channel) in {time.time() - c0:.1f} s : "
         f"{t2!r}  type={type(t2).__name__}")

    d0 = time.time()
    t3 = H.binding_from_frobenius_pairing(1, 1)
    if isinstance(t3, tuple):
        t3 = t3[0]
    _say(f"  term 3 (frobenius_pairing) in {time.time() - d0:.1f} s : "
         f"{t3!r}  type={type(t3).__name__}")

    # ---- Comparison.  mpf throughout; float() only for display. ----
    t1m = mp.mpf(t1_mpf) if t1_mpf is not None else mp.mpf(str(t1_float))
    t2m = mp.mpf(t2)
    t3m = mp.mpf(t3)
    sum_terms = t1m + t2m + t3m

    derived = mp.mpf(DERIVED_STR)
    measured_public = mp.mpf(b_public)      # exact value of the returned double

    print("", flush=True)
    print("=" * 72, flush=True)
    print("MEASURED vs DERIVED -- binding_energy(1, 1), "
          "k_exact = k_max = 11 (production default)", flush=True)
    print("=" * 72, flush=True)
    print(f"  derived  (audit banner arithmetic) : {DERIVED_STR}", flush=True)
    print(f"  measured (public float64 return)   : {b_public!r}", flush=True)
    print(f"  measured (sum of terms, mpf)       : {fmt(sum_terms)}", flush=True)
    print(f"  rel diff measured-public vs derived: "
          f"{mp.nstr(_rel(measured_public, derived), 12)}", flush=True)
    print(f"  abs diff measured-public vs derived: "
          f"{mp.nstr(measured_public - derived, 12)} MeV", flush=True)
    print("", flush=True)
    print("  term-by-term (derived -> measured):", flush=True)
    for name, dstr, meas in (
            ("1 unified_iterative_correction", DERIVED_TERM1_STR, t1m),
            ("2 sdp_cross_channel_contribution", DERIVED_TERM2_STR, t2m),
            ("3 binding_from_frobenius_pairing", DERIVED_TERM3_STR, t3m)):
        d = mp.mpf(dstr)
        print(f"    term {name:34s} {dstr:>22s} -> {mp.nstr(meas, 20):>24s}"
              f"   reldiff {mp.nstr(_rel(meas, d), 6)}", flush=True)
    print("", flush=True)
    print(f"  public return - sum(terms)         : "
          f"{mp.nstr(measured_public - sum_terms, 12)} MeV   "
          f"(nonzero here is the float64 cast at the public return, "
          f"not a term)", flush=True)

    # AME2020 deuteron binding, as published text (9 s.f.), NOT re-fmt'd.
    ame = mp.mpf("2.22456607")
    print("", flush=True)
    print(f"  AME2020 2H binding                 : +{mp.nstr(ame, 9)} MeV",
          flush=True)
    print(f"  |ratio| measured / AME             : "
          f"{mp.nstr(abs(measured_public / ame), 6)}x", flush=True)
    print(f"  residual |measured - AME|          : "
          f"{mp.nstr(abs(measured_public - ame), 8)} MeV", flush=True)
    print("=" * 72, flush=True)

    tol = mp.mpf("1e-12")
    agree = _rel(measured_public, derived) < tol
    print(f"VERDICT: measured {'MATCHES' if agree else 'DOES NOT MATCH'} the "
          f"derived cell at rel < {mp.nstr(tol, 2)} "
          f"(53-bit comparison: the public return is a float).", flush=True)
    _say(f"total wall {time.time() - T0:.1f} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
