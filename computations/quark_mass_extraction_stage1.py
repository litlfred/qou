#!/usr/bin/env python3
"""Operational quark-mass extraction, stage 1 — m_d - m_u scoping (EXPLORATORY).

Programme (sm-params-quark-masses, bean qou-m3vl): the framework never
defines m_q; it derives the observables the Standard-Model extraction
procedures consume, and runs the equivalent extraction. The cleanest
target is the isospin-breaking difference m_d - m_u, whose experimental
source is the neutron-proton splitting Delta_pn after removing the
electromagnetic self-energy:

    delta_QCD  =  Delta_pn + E_EM(p self-energy)   ~   beta * (m_d - m_u)

with E_EM > 0 (the charged proton's EM self-energy raises m_p, so the
observed splitting understates the strong part) and beta ~ O(1) a
sigma-term-style scheme coefficient.

Stage-1 finding (the honest content of this probe): the framework
derives Delta_pn, and its ONLY derived EM mechanism is the Coulomb
crossing ratio tanh(ln q0) multiplying a STRONG BOND scale — an
inter-nucleon object (the A=3 mirror-split mechanism,
docs/audits/2026-06-03-charge-coulomb-tn3he-derived.md). The
INTRA-nucleon EM self-energy needed here is exactly the corpus's open
two-like-charge EM-linking invariant — THE SAME open object that owns
the remaining 69% of the 3He mirror residual. One missing invariant
blocks both. No fit is performed; external lattice EM values appear
only as comparators, never as inputs.
"""

from __future__ import annotations

import sys

import _path_bridge  # noqa: F401
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from mpmath import mp, mpf, tanh, log  # noqa: E402

sys.path.insert(0, ".")
from canonical_mass import proton_neutron_mass_mev  # noqa: E402

# Comparators only (NOT inputs): FLAG/BMW-era lattice QED+QCD splitting
# of Delta_pn, and PDG MS-bar(2 GeV) m_d - m_u. Quoted coarsely; the
# probe's claims do not depend on their precise values.
LATTICE_E_EM_MEV = 0.8       # EM self-energy contribution ~ +0.6..1.0
PDG_MD_MINUS_MU_MEV = 2.5    # ~ 4.7 - 2.2


def main() -> None:
    set_compute_dps()
    m_p, m_n = (mpf(str(x)) for x in proton_neutron_mass_mev())
    delta_pn = m_n - m_p
    coul_ratio = tanh(log(Q_MP))

    # Framework-scheme strong part under three E_EM hypotheses:
    #   0 (no EM removal), the corpus inter-nucleon scale orientation
    #   (tanh(ln q0) * Delta_pn-scale, NOT a derived self-energy), and
    #   the external lattice comparator.
    e_em_orientation = coul_ratio * delta_pn
    rows = {
        "E_EM = 0 (no removal)": delta_pn,
        "E_EM = tanh(ln q0)*Delta_pn (scale orientation only)":
            delta_pn + e_em_orientation,
        "E_EM = lattice comparator 0.8 MeV (external)":
            delta_pn + mpf(str(LATTICE_E_EM_MEV)),
    }

    wb = WitnessBuilder("quark-mass-extraction-stage1", engine="mpmath")
    wb.set_description(
        "EXPLORATORY stage-1 scoping of the operational m_d - m_u "
        "extraction (sm-params-quark-masses, bean qou-m3vl): "
        "delta_QCD = Delta_pn + E_EM. Finding: the framework derives "
        "Delta_pn, but its only derived EM mechanism (tanh(ln q0) x "
        "strong bond) is inter-nucleon; the intra-nucleon EM "
        "self-energy is the SAME open two-like-charge EM-linking "
        "invariant that owns the 3He mirror residual. One invariant "
        "blocks both. Lattice/PDG numbers are comparators, not inputs; "
        "no fit.")
    wb.add_data("framework", {
        "m_p_MeV": mp.nstr(m_p, 15),
        "m_n_MeV": mp.nstr(m_n, 15),
        "Delta_pn_MeV": mp.nstr(delta_pn, 12),
        "tanh_ln_q0": mp.nstr(coul_ratio, 12),
    })
    wb.add_data("delta_QCD_framework_scheme_MeV", {
        k: mp.nstr(v, 10) for k, v in rows.items()
    })
    wb.add_data("comparators_external", {
        "lattice_E_EM_MeV": str(LATTICE_E_EM_MEV),
        "pdg_md_minus_mu_MeV": str(PDG_MD_MINUS_MU_MEV),
        "note": ("delta_QCD ~ beta*(m_d - m_u) with beta ~ O(1) "
                 "scheme-dependent; magnitudes agree at the ~2x level "
                 "under the external comparator, as expected for a "
                 "scheme quantity — no precision claim is made."),
    })
    wb.add_data("honest_gap", (
        "The extraction is well-posed but blocked on ONE corpus object: "
        "the intra-nucleon EM self-energy (two-like-charge EM-linking "
        "invariant). That is the same open invariant as the remaining "
        "69% of the 3He mirror split (a3-mirror-residual-"
        "reconciliation). Deriving it closes both this extraction and "
        "the A=3 mirror residual simultaneously. Until then the "
        "framework-scheme delta_QCD is bounded below by Delta_pn and "
        "no m_d - m_u value is claimed."))
    wb.set_content_block("prose:sm-params-quark-masses")
    wb.add_assertion(
        name="delta_pn_derived_positive",
        computed=mp.nstr(delta_pn, 15), expected="1.29", tolerance="0.02",
        unit="MeV",
        source="Framework-derived neutron-proton splitting (canonical facade).")
    wb.add_assertion(
        name="lower_bound_below_pdg_comparator",
        computed=int(delta_pn < mpf(str(PDG_MD_MINUS_MU_MEV))),
        expected=1, tolerance="0", unit="bool",
        source=("Sanity: the no-removal lower bound sits below the PDG "
                "comparator, consistent with E_EM > 0."))
    out = wb.save()

    print(f"Delta_pn (framework) = {mp.nstr(delta_pn, 10)} MeV")
    for k, v in rows.items():
        print(f"  delta_QCD | {k}: {mp.nstr(v, 8)} MeV")
    print(f"comparator m_d - m_u (PDG, scheme-dependent): ~{PDG_MD_MINUS_MU_MEV} MeV")
    print("finding: blocked on the SAME open EM-linking invariant as the 3He residual")
    print(f"witness -> {out}")


if __name__ == "__main__":
    main()
