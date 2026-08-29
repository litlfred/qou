#!/usr/bin/env python3
"""What must the nucleon EM self-energy coupling be?  A TARGET, not a derivation.

Bean `qou-bn8e`.  The corpus already derives the charge STRUCTURE of the
neutron-proton EM self-energy difference, parameter-free
(`QOU/MassTheory/NeutronProtonEMSign.lean`):

    Sum_{i<j} q_i q_j  =  0     for the proton (uud)
                       = -1/3   for the neutron (udd)
    gap                =  1/3   -> the proton carries the larger self-energy

and leaves the coupling `k > 0` free, saying so explicitly: "does not derive the
EM coupling from the 13 categorical drivers".  This branch adds two shape
constraints (E_EM even in mu-bar_123; pairwise linking cannot see the carrier).
What remains underived is exactly ONE positive scalar.

This script says what that scalar must equal, and what effective pair separation
it corresponds to, so a future derivation can be FALSIFIED rather than tuned.

  *** THIS IS NOT A DERIVATION AND MUST NOT BE WIRED TO PRODUCTION. ***

It inverts an EXTERNAL input -- the lattice-QCD decomposition of m_n - m_p into
QCD and QED parts -- to read off the target.  Inverting a measurement to obtain a
parameter is a FIT (AGENTS.md anti-laundering).  It is recorded as a target
because a target with a number can be checked; it is not evidence for anything.

External input, labelled as such:
  m_n - m_p            = +1.29333 MeV   (CODATA, exact-ish)
  ... of which QED     = -1.00(16) MeV  (lattice, BMW 2015 arXiv:1406.4088)
  ... of which QCD     = +2.29(21) MeV
The QED part carries a 16% uncertainty; every target below inherits it.

mpmath at 50 dps throughout; no float64 (AGENTS.md: probes are not exempt).
Emits no witness -- it derives nothing.
"""
from mpmath import mp

mp.dps = 50

HBARC_MEV_FM = mp.mpf("197.3269804")      # CODATA 2018, exact by definition of c
ALPHA_EM_INV = mp.mpf("137.035999084")    # CODATA 2018
M_PI_MEV = mp.mpf("139.57039")            # PDG charged pion
R_PROTON_FM = mp.mpf("0.8409")            # CODATA 2018 proton charge radius

DELTA_EM_MEV = mp.mpf("-1.00")            # EXTERNAL lattice input
DELTA_EM_ERR = mp.mpf("0.16")
CHARGE_GAP = mp.mpf(1) / 3                # DERIVED, corpus: Sum qq(p) - Sum qq(n)


def target_coupling(delta_em):
    """k such that  delta_em = -k * chargeGap.  Units MeV."""
    return -delta_em / CHARGE_GAP


def separation_from_coupling(k):
    """r such that  k = alpha_EM * hbar c / r.  Units fm."""
    return (HBARC_MEV_FM / ALPHA_EM_INV) / k


def main() -> int:
    alpha = 1 / ALPHA_EM_INV
    lam_pi = HBARC_MEV_FM / M_PI_MEV

    k = target_coupling(DELTA_EM_MEV)
    k_lo = target_coupling(DELTA_EM_MEV + DELTA_EM_ERR)   # less negative -> smaller k
    k_hi = target_coupling(DELTA_EM_MEV - DELTA_EM_ERR)
    r = separation_from_coupling(k)
    r_lo, r_hi = separation_from_coupling(k_hi), separation_from_coupling(k_lo)

    print("DERIVED (corpus, parameter-free):")
    print(f"  charge-structure gap  Sum qq(p) - Sum qq(n) = {mp.nstr(CHARGE_GAP, 10)}")
    print("\nEXTERNAL INPUT (lattice; this is what makes the rest a target, not a result):")
    print(f"  QED part of m_n - m_p = {mp.nstr(DELTA_EM_MEV, 4)} +- "
          f"{mp.nstr(DELTA_EM_ERR, 3)} MeV")
    print("\nTARGET the coupling must hit:")
    print(f"  k  = {mp.nstr(k, 8)} MeV        [{mp.nstr(k_lo, 6)}, {mp.nstr(k_hi, 6)}]")
    print(f"  r  = {mp.nstr(r, 8)} fm         [{mp.nstr(r_lo, 6)}, {mp.nstr(r_hi, 6)}]"
          "   (if k = alpha_EM * hbar c / r)")

    print("\nCOMPARISON with the two length scales the framework already has:")
    for name, length in (("proton charge radius", R_PROTON_FM),
                         ("pion Compton wavelength lambda-bar_pi", lam_pi)):
        k_pred = alpha * HBARC_MEV_FM / length
        d_pred = -k_pred * CHARGE_GAP
        ratio = d_pred / DELTA_EM_MEV
        print(f"  {name:38s} = {mp.nstr(length, 6)} fm")
        print(f"      -> k = {mp.nstr(k_pred, 6)} MeV, "
              f"delta_EM = {mp.nstr(d_pred, 6)} MeV, "
              f"{mp.nstr(ratio, 4)}x the target")

    print("\nREADING.  Neither scale reproduces the target: the charge radius")
    print("under-predicts by ~1.7x and lambda-bar_pi by ~2.9x. So a future")
    print("derivation of k is FALSIFIABLE -- if the framework's intra-nucleon")
    print("geometry hands back either of these lengths, it is wrong, and by a")
    print("factor this probe states in advance.")
    print("\nWhat is NOT claimed: that r above is the right length, that the")
    print("1/r Coulomb form is right, or that k is derived. Choosing a length to")
    print("match would be the fit this probe exists to make visible.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
