#!/usr/bin/env python3
"""neutrino_mass_volume_exclusion.py — scope-(b) exclusion of the volume-density
mass mechanism for the neutrino mass scale.

The framework assigns the neutrino the UNKNOT (def:neutrino-knot): Vol=0, CS=0,
all knot invariants trivial -> zero mass at leading order, no nonzero-mass
mechanism. This probe shows the obvious rescue (a small perturbation to a
hyperbolic carrier) is structurally excluded:

- Minimum-volume theorem: the figure-eight 4_1 = 2*Lobachevsky(pi/3) ~ 2.0299 is
  the smallest-volume hyperbolic KNOT complement (Cao-Meyerhoff: the figure-eight
  and its sister are the minimum-volume cusped hyperbolic 3-manifolds).
- So m(K) = m_e * Vol(K) * rho(K) / hbar_q^2 with any hyperbolic K and density
  rho ~ O(1) gives mass >= ~260 MeV (calibrating the scale on the proton).
- The heaviest neutrino mass is ~0.05 eV = 5e-8 MeV.

=> gap ~ 5e9 (~10^10). No O(1) density closes it; a density ~1e-10 is absurd.
The volume-density chain CANNOT produce the neutrino mass scale -- scope-(b),
cite the minimum-volume invariant. Neutrino masses require a mechanism OUTSIDE
the volume-density chain (seesaw-like suppression / a different small parameter),
which the corpus does not have. m_nu stays OPEN; the mechanism CLASS is narrowed.

Requires SnapPy. Emits a witness.
"""
import json

import snappy

from pathlib import Path as _PathW  # noqa: E402 — witness output root
_HERE_W = _PathW(__file__).resolve().parent


def main():
    v41 = float(snappy.Manifold("4_1").volume())          # min hyperbolic knot vol
    vbor = float(snappy.Link(braid_closure=[1, -2] * 3).exterior().volume())
    mp = 938.272                                           # proton (MeV), Borromean
    mev_per_vol = mp / vbor                                # scale, density ~ O(1)
    m_nu_MeV = 0.05e-6                                     # heaviest nu ~0.05 eV
    min_mass_hyp = v41 * mev_per_vol
    gap = min_mass_hyp / m_nu_MeV

    print(f"Vol(4_1) min hyperbolic knot   = {v41:.6f}")
    print(f"scale (proton/Borromean)       = {mev_per_vol:.2f} MeV per Vol*rho unit")
    print(f"min mass from any hyperbolic K = {min_mass_hyp:.1f} MeV")
    print(f"heaviest neutrino mass         = {m_nu_MeV:.2e} MeV")
    print(f"gap                            = {gap:.2e}")
    print("VERDICT: volume-density mechanism scope-(b) EXCLUDED for neutrino masses.")

    witness = {
        "schema": "witness/v1-informal",
        "description": "neutrino_mass_volume_exclusion: min-hyperbolic-volume "
                       "theorem excludes the volume-density chain at the neutrino "
                       "mass scale.",
        "producer": "computations/neutrino_mass_volume_exclusion.py",
        "consumes": ["def:neutrino-knot"],
        "results": {
            "vol_min_hyperbolic_knot_4_1": v41,
            "scale_MeV_per_vol": mev_per_vol,
            "min_mass_from_hyperbolic_knot_MeV": min_mass_hyp,
            "heaviest_neutrino_mass_MeV": m_nu_MeV,
            "gap": gap,
        },
        "verdict": (
            "scope-(b) EXCLUSION (cite: 4_1 is the minimum-volume hyperbolic knot, "
            f"Vol=2*Cl_2(pi/3)~{v41:.4f}; Cao-Meyerhoff). Any hyperbolic-carrier "
            "volume-density mass is >= ~260 MeV with O(1) density, ~10^10 above the "
            "~0.05 eV neutrino scale. The unknot carrier is trivial (Vol=CS=0). "
            "Neutrino masses need a mechanism OUTSIDE the volume-density chain; the "
            "corpus has none. m_nu OPEN, mechanism class narrowed."
        ),
        "scope": "(b) structural: proved minimum-volume invariant, density O(1).",
    }
    with open(_HERE_W / "neutrino-mass-volume-exclusion.witness.json", "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        import os as _os  # noqa: E402 -- provenance stamp
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)
    print("wrote computations/neutrino-mass-volume-exclusion.witness.json")


if __name__ == "__main__":
    main()
