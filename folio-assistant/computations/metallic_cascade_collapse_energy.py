#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical-only astrophysical energy budget.
"""
Metallic-cascade collapse energetics — does a star crossing the silver
rung release a supernova-scale burst?

Owner question (2026-06-09): "when a star goes nova … star gets dense
enough, q changes enough for phase transitions — cascading burst of
energy, then strong steady release. Is this what happens?  What is the
component matter before and after?  Can we predict the energy released
and compare to data?"

This script computes the QOU answer with no fitting:

  1. LATENT HEAT of the silver crossing.  At q = δ_silver the
     Borromean and Hopf-diquark binding branches
     (prop:borromean-hopf-energy-crossover) differ by
         ΔE(δ_s) = V_B/ℏ_q(δ_s)² − (3/2)(δ_s + δ_s⁻¹)   [Skein units]
     per baryon number; the Skein→MeV conversion is the m_p anchor.

  2. CASCADE ENERGY for a collapsing core of mass M_core: every baryon
     that crosses the rung releases ΔE(δ_s); E = N_b·ΔE.

  3. COMPARISON with the observed core-collapse budget (SN 1987A):
     neutrino burst ~(2–5)×10⁵³ erg over ~13 s, kinetic ~10⁵¹ erg,
     photons ~10⁴⁹ erg; standard accounting attributes the burst to
     the gravitational binding energy of the proto-neutron star.

  4. PARITY-CLASS bookkeeping of the pre/post composition using the
     PROVED #2074 closed form sign(ρ_alt) = (−1)^T,
     T = 11A + A(A−1)/2 + Z: the Fe core, the neutronization step, and
     the ⁵⁶Ni → ⁵⁶Co → ⁵⁶Fe decay chain that powers the "steady
     release" (the light curve), classified by (A mod 4, Z parity)
     admissibility.

  5. WHERE the rung sits — imported from metallic_q_rho_calibration
     (Maps A/B/C).  Under the shallow (Map C) placement the crossing
     happens inside the heaviest proto-neutron stars a few hundred ms
     after bounce → a DELAYED SECOND ν̄_e BURST, the same observable
     shape as the Sagert et al. (2009) QCD-transition mechanism.
     Under the deep (Map A/B) placement no supernova core crosses;
     the cascade happens only inside black-hole-forming collapse.

Tiered exploratory probe — nothing wired to production.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

from metallic_q_rho_calibration import (
    M_SUN_G, M_B_G, MEV_TO_ERG, Q0, RUNGS, SKEIN_TO_MEV, V_B,
    alpha_for, delta_n, hbar_q, map_a_rho, map_b_rho_c, map_c_rho_c,
    powerlaw_rho,
)

mp.mp.dps = 50
HERE = Path(__file__).parent

DELTA_S = delta_n(2)

# observed core-collapse budget (SN 1987A, standard literature values)
SN1987A = {
    "neutrino_burst_erg": "2e53–5e53 (≈3e53 central; ~13 s; Kamiokande-II"
                          " 11 + IMB 8 + Baksan 5 events)",
    "kinetic_erg": "1e51–1.5e51",
    "photons_erg": "~1e49",
    "standard_attribution": (
        "gravitational binding energy of the proto-neutron star "
        "(~3/5 GM²/R with relativistic corrections ≈ 3e53 erg), "
        "radiated as neutrinos of all flavors"
    ),
}


def latent_heat_silver_mev() -> mp.mpf:
    """Borromean − Hopf binding-branch gap per baryon AT q = δ_silver."""
    gap_skein = V_B / hbar_q(DELTA_S) ** 2 \
        - mp.mpf(3) / 2 * (DELTA_S + 1 / DELTA_S)
    return gap_skein * SKEIN_TO_MEV


def cascade_energy_erg(m_core_msun: mp.mpf) -> mp.mpf:
    n_b = m_core_msun * M_SUN_G / M_B_G
    return n_b * latent_heat_silver_mev() * MEV_TO_ERG


# ── #2074 parity-class bookkeeping ────────────────────────────────────

ALLOWED_CLASSES = {(0, 0), (1, 1), (2, 1), (3, 0)}  # (A mod 4, Z mod 2)


def parity_class(A: int, Z: int) -> dict:
    cls = (A % 4, Z % 2)
    return {
        "A": A, "Z": Z, "A_mod_4": cls[0],
        "Z_parity": "even" if cls[1] == 0 else "odd",
        "alt_block_positive": cls in ALLOWED_CLASSES,
    }


COMPOSITION = {
    "before_collapse": [
        {"layer": "envelope", "species": "¹H, ⁴He", "classes": [
            parity_class(1, 1), parity_class(4, 2)]},
        {"layer": "shells", "species": "¹²C, ¹⁶O, ²⁰Ne, ²⁸Si", "classes": [
            parity_class(12, 6), parity_class(16, 8),
            parity_class(20, 10), parity_class(28, 14)]},
        {"layer": "core (Chandrasekhar ≈1.4 M☉)", "species": "⁵⁶Fe",
         "classes": [parity_class(56, 26)]},
    ],
    "after_collapse": [
        {"layer": "remnant", "species": (
            "proto-neutron star: bulk neutron-rich matter (n + ~10% p,e); "
            "under the shallow q↔ρ maps the inner core is past the silver "
            "rung: Hopf-diquark (CFL) condensate"), "classes": []},
        {"layer": "ejecta (steady release)", "species":
            "⁵⁶Ni → ⁵⁶Co → ⁵⁶Fe (radioactive light curve)", "classes": [
            parity_class(56, 28), parity_class(56, 27),
            parity_class(56, 26)]},
    ],
    "neutronization_step": {
        "reaction": "e⁻ + p → n + ν_e  (Z → Z−1 at fixed A)",
        "parity_effect": (
            "flips Z parity ⇒ at A ≡ 0 (mod 4) it moves a nucleus OUT of "
            "the #2074 spectrally-positive class (e.g. ⁵⁶Fe (0,even) "
            "allowed → ⁵⁶Mn (0,odd) disallowed): in QOU terms the "
            "e-capture cascade forces the matter out of the nuclear "
            "admissible classes into bulk braid restructuring"
        ),
        "examples": [parity_class(56, 26), parity_class(56, 25)],
        "caveat": (
            "the parity class flags spectral positivity (structural "
            "admissibility), NOT a lifetime ordering — ⁵⁶Ni (allowed) "
            "decays faster than ⁵⁶Co (disallowed); exploratory "
            "cross-link only"
        ),
    },
}


def main() -> None:
    dE = latent_heat_silver_mev()
    cores = {}
    for m in ("1.2", "1.4", "1.8", "2.0"):
        cores[m + " M_sun"] = mp.nstr(cascade_energy_erg(mp.mpf(m)), 5)

    # rung placements (from the calibration maps)
    silver_placement = {
        "A_kinetic_rho0": mp.nstr(map_a_rho(DELTA_S), 6),
        "B_crossover_rel_rho0": mp.nstr(map_b_rho_c(True), 6),
        "B_crossover_nonrel_rho0": mp.nstr(map_b_rho_c(False), 6),
        "C_coral_tube_rp_rho0": mp.nstr(map_c_rho_c(mp.mpf("0.8414")), 6),
        "C_coral_tube_1fm_rho0": mp.nstr(map_c_rho_c(mp.mpf("1.0")), 6),
    }

    # second-burst scenario (shallow map): only the inner core crosses
    second_burst = {
        "mechanism": (
            "under Map C the proto-NS central density crosses "
            "ρ(δ_silver) a few hundred ms after bounce as the core "
            "deleptonizes and contracts; the crossing is FIRST-ORDER "
            "(Milnor μ̄(123): 1→0, conj:color-superconductivity-"
            "borromean) ⇒ a micro-collapse + second shock + second "
            "ν̄_e-dominated burst — the same observable shape as the "
            "QCD-phase-transition mechanism of Sagert et al. 2009 "
            "(arXiv:0809.4225) / Dasgupta et al. 2009 (0912.2568)"
        ),
        "inner_core_crossing_msun": "0.5–1.0",
        "energy_erg": {
            "0.5 M_sun": mp.nstr(cascade_energy_erg(mp.mpf("0.5")), 5),
            "1.0 M_sun": mp.nstr(cascade_energy_erg(mp.mpf("1.0")), 5),
        },
        "detectability": (
            "few ×10⁵² erg released on ~ms timescale, ν̄_e-dominated: "
            "clearly resolvable by IceCube/Super-K/Hyper-K for a "
            "galactic event (the corpus's strangelet-merger block "
            "already cites ~50 Mpc reach for 2.4e51 erg bursts)"
        ),
    }

    witness = {
        "description": (
            "Metallic-cascade collapse energetics: latent heat of the "
            "silver (Borromean→CFL) crossing per baryon, cascade energy "
            "for collapsing cores, comparison with the observed "
            "SN 1987A budget, #2074 parity-class bookkeeping of the "
            "pre/post composition, and the delayed-second-burst "
            "discriminator between the shallow and deep q↔ρ maps."
        ),
        "computed_at": datetime.now(timezone.utc).isoformat(),
        "script": "metallic_cascade_collapse_energy.py",
        "latent_heat_silver": {
            "gap_skein": mp.nstr(V_B / hbar_q(DELTA_S) ** 2
                                 - mp.mpf(3) / 2 * (DELTA_S + 1 / DELTA_S), 8),
            "per_baryon_MeV": mp.nstr(dE, 8),
            "note": (
                "branch gap of prop:borromean-hopf-energy-crossover "
                "evaluated AT q = δ_silver; Skein→MeV via the m_p anchor "
                f"(1 Skein = {mp.nstr(SKEIN_TO_MEV, 8)} MeV)"
            ),
        },
        "cascade_energy_erg": cores,
        "sn1987a_observed": SN1987A,
        "budget_comparison": {
            "full_core_cascade_vs_neutrino_burst": (
                f"{mp.nstr(cascade_energy_erg(mp.mpf('1.4')), 4)} erg "
                "(1.4 M☉ cascade) vs ~3e53 erg observed — the cascade "
                "is ~20% of the standard gravitational-binding budget: "
                "an ADDITIVE QOU contribution currently hidden inside "
                "the factor-~2 uncertainty of the 25-event 1987A sample"
            ),
            "discriminator": (
                "a future galactic SN with O(10⁴) detected neutrinos "
                "resolves a 20% excess; the sharper signature is the "
                "second-burst TIMING structure (below)"
            ),
        },
        "rung_placement_silver_rho0": silver_placement,
        "scenario_split": {
            "shallow_maps_C": (
                "heaviest proto-NS cross silver → delayed second ν̄_e "
                "burst + ~6e52 erg/M☉ extra; ordinary SNe below the "
                "rung show NO excess"
            ),
            "deep_maps_A_B": (
                "no SN core ever crosses silver (ρ_c ≥ 64 ρ0): cascade "
                "fires only inside BH-forming collapse, energy swallowed "
                "by the horizon → prediction: NO second burst in any SN; "
                "consistent with non-detection to date"
            ),
        },
        "second_burst": second_burst,
        "composition": COMPOSITION,
        "steady_release": {
            "observed": (
                "light curve = ⁵⁶Ni → ⁵⁶Co → ⁵⁶Fe radioactive chain "
                "(6.1 d / 77.2 d), NOT core physics; late-time NS "
                "cooling is core physics"
            ),
            "qou_reading": (
                "post-cascade CFL remnant cools with the gap "
                "Δ_CFL ≈ 2.5 MeV suppressing ν emission below "
                "T ≈ 2.9e10 K (prop:cfl-neutron-star-observables "
                "cooling plateau) — the 'strong steady release' phase"
            ),
        },
        "limitations": [
            "only the silver rung has a corpus-defined latent heat "
            "(Borromean−Hopf branch gap); φ and φ² crossings are not "
            "modeled (no corpus EOS for hyperonic/gCFL branch jumps)",
            "cascade energy assumes EVERY baryon in M_core crosses; "
            "partial crossings scale linearly",
            "SN 1987A numbers are standard-literature values, not "
            "corpus outputs",
            "parity-class bookkeeping is an exploratory cross-link to "
            "the #2074 closed form, not a stability claim",
        ],
    }
    out = HERE / "metallic-cascade-collapse-energy.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"Saved witness: {out}", file=sys.stderr)

    print(f"latent heat at silver: {mp.nstr(dE, 6)} MeV/baryon")
    print("cascade energy:", json.dumps(cores, indent=2))
    print("silver placement (ρ0):", json.dumps(silver_placement, indent=2))


if __name__ == "__main__":
    main()
