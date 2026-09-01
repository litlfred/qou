#!/usr/bin/env python3
"""What must the nucleon EM self-energy coupling be, IN THE FRAMEWORK'S OWN TERMS?

Bean `qou-bn8e`.  The corpus derives the charge STRUCTURE of the neutron-proton
EM self-energy difference, parameter-free and sorry-free
(`QOU/MassTheory/NeutronProtonEMSign.lean`):

    Sum_{i<j} q_i q_j  =  0     proton (uud)      chargeStructure_uud
                       = -1/3   neutron (udd)     chargeStructure_udd
    gap                = +1/3                     em_gap_eq
    sign of correction = negative                 em_correction_neg

and leaves the coupling free, saying so: "does not derive the EM coupling from
the 13 categorical drivers".  This branch adds two shape constraints (E_EM even
in mu-bar_123; pairwise linking cannot see the carrier).  What is left underived
is one positive scalar.  This states what it must equal.

  *** STILL NOT A DERIVATION.  It inverts a known residual to read off a  ***
  *** target.  Inverting a measurement for a parameter is a FIT.  Recorded ***
  *** because a target with a number can be checked rather than tuned to.  ***

TWO ERRORS THIS FILE CORRECTS, BOTH MINE, BOTH IN ITS OWN FIRST VERSION
----------------------------------------------------------------------
1. WRONG DECOMPOSITION, wrong by 121x.  The first version inverted the LATTICE
   split of m_n - m_p into QCD (+2.29) and QED (-1.00 MeV), giving k = 3.0 MeV.
   The framework does not build Delta_m that way.  Its leading traced-volume term
   `Delta_m = alpha*|Delta_Phi|` predicts the NET splitting and over-predicts it
   by +0.638% (`docs/audits/2026-07-11-np-splitting-residual-not-q0-knob.md`:
   1.301589 vs 1.293334).  The EM term is that residual -- 0.008255 MeV -- not a
   -1.00 MeV piece.  Importing an external decomposition that the framework does
   not use put the target off by two orders of magnitude.

2. EUCLIDEAN IMPORT.  The first version wrote k = alpha_EM * hbar c / r and
   solved for a length (r ~ 0.480 fm), presupposing a 1/r Coulomb law.  The
   framework's own EM corrections do not have that shape: the meson block
   (`prop:meson-em-sinh-closed-form`) writes its correction as
   `(alpha_em/pi) * (dimensionless function of hbar_q)`.  Solving for a LENGTH
   is the same "unexamined Euclidean import" that `qou-17mq` flagged for the
   kappa(A) separation law on the neighbouring front.  The target below is in
   the framework's native shape instead.

mpmath at 40 dps; no float64.  Emits no witness -- it derives nothing.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]
                       / "tools" / "qou-substrate" / "python"))

from mpmath import mp  # noqa: E402

mp.dps = 40

ALPHA_EM_INV = mp.mpf("137.035999084")   # CODATA 2018
M_P_MEV = mp.mpf("938.27208943")
CHARGE_GAP = mp.mpf(1) / 3               # DERIVED, corpus, parameter-free

# The framework's own leading prediction and its measured residual.
DM_PRED = mp.mpf("1.301589")             # alpha*|Delta_Phi|, traced-volume term
DM_CODATA = mp.mpf("1.293334")


def substrate_hbar_q():
    # `constants.Q` is `_solve_q_proton_f64` -- a float64 Newton solve -- so
    # `mp.mpf(str(Q))` would inflate a double's ~1e-16 error to this file's
    # 40 dps and read as exact.  `q_at` runs the same proton identity at the
    # requested precision.  Same pin, same anchor; only the arithmetic changes.
    from qou_substrate.constants import q_at
    q = q_at(mp.dps)
    return q, (q - 1) / q


def main() -> int:
    q, hq = substrate_hbar_q()
    alpha = 1 / ALPHA_EM_INV
    resid = DM_PRED - DM_CODATA          # what the EM term must REMOVE

    print(f"substrate q0 = {mp.nstr(q, 12)}   hbar_q = {mp.nstr(hq, 12)}")
    print("\nDERIVED (corpus, parameter-free):")
    print(f"  charge-structure gap = {mp.nstr(CHARGE_GAP, 10)}")
    print("\nFRAMEWORK-INTERNAL residual (not an external decomposition):")
    print(f"  leading Delta_m  = {mp.nstr(DM_PRED, 10)} MeV")
    print(f"  CODATA           = {mp.nstr(DM_CODATA, 10)} MeV")
    print(f"  EM term owes     = {mp.nstr(resid, 8)} MeV "
          f"({mp.nstr(100 * resid / DM_CODATA, 4)}%)")

    k = resid / CHARGE_GAP
    print(f"\nTARGET, plain coupling:   k = {mp.nstr(k, 8)} MeV")
    print(f"  (the lattice-based first version said 3.0 MeV -- "
          f"wrong by {mp.nstr(3 / k, 5)}x)")

    f_req = resid / (M_P_MEV * (alpha / mp.pi) * CHARGE_GAP)
    print("\nTARGET, framework-native shape  dE = -m_p*(alpha/pi)*f(hbar_q)*gap:")
    print(f"  f_required = {mp.nstr(f_req, 8)}")
    print(f"  hbar_q^2   = {mp.nstr(hq**2, 8)}   ->  f/hbar_q^2 = "
          f"{mp.nstr(f_req / hq**2, 6)}")

    print("\nOBSERVATION, explicitly NOT a derivation: f_required is O(hbar_q^2),")
    print("a scale that appears structurally in the mass formula's 1/hbar_q^2.")
    print(f"Right ORDER is not right VALUE -- the ratio is {mp.nstr(f_req/hq**2,6)},")
    print("not 1 -- and choosing a function to close that 16% would be exactly")
    print("the fit this file exists to keep visible.  The meson block's own")
    f_meson = 1 + mp.log(1 + hq)
    print(f"f = 1 + log(1+hbar_q) = {mp.nstr(f_meson, 8)} is off by "
          f"{mp.nstr(f_meson / f_req, 6)}x and is NOT the one to reuse: it")
    print("corrects a mass-SQUARED RATIO, a different object.")
    print("\nWHAT IS STILL NOT DERIVED: f, hence k. Only the target has moved.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
