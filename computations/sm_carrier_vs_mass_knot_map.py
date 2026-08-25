#!/usr/bin/env python3
"""sm_carrier_vs_mass_knot_map.py — the carrier != mass-knot map.

A structural clarification for every open SM mass in the framework. The
torus-knot particle dictionary assigns each particle a CARRIER T(m,n); this
probe shows every such carrier is a torus knot/link (or the unknot), hence
Vol=0 -- so the carrier fixes the CHANNEL / quantum numbers but CANNOT supply a
mass via the volume-density chain m = m_e*Vol*rho/hbar_q^2. Masses come from
DISTINCT hyperbolic knots: the muon's is the figure-eight 4_1 (m_mu/m_e =
Vol(4_1)/hbar_q^2), the proton's is the Borromean link.

Consequence: 'which knot for m_c / m_tau / ...' is the wrong question if read as
the CARRIER; the right question is 'which HYPERBOLIC mass-knot', a separate
object. This reframes B1 (m_c), B2 (m_tau) and the whole open-mass program, and
is consistent with the neutrino scope-(b) exclusion (unknot carrier -> trivial;
volume route excluded by the minimum-volume theorem).

Requires SnapPy. Prints the map; pairs with neutrino-mass-volume-exclusion.
"""
import snappy


def torus_link_vol(p, q):
    """T(p,q) via braid (s1..s_{p-1})^q on p strands; torus => non-hyperbolic."""
    word = list(range(1, p)) * q
    M = snappy.Link(braid_closure=word).exterior()
    try:
        v = float(M.volume())
        return v if abs(v) > 1e-6 else 0.0
    except Exception:
        return 0.0  # non-hyperbolic


def main():
    carriers = {
        "nu (unknot)": None, "e  T(2,3)": (2, 3), "mu T(2,5)": (2, 5),
        "tau T(2,7)": (2, 7), "charm-vertex T(3,5)": (3, 5),
        "gluon T(2,9)": (2, 9), "W  T(2,4)": (2, 4), "Z  T(2,6)": (2, 6),
        "H  T(2,8)": (2, 8),
    }
    print("dictionary carriers (channel / quantum numbers):")
    all_zero = True
    for name, pq in carriers.items():
        v = 0.0 if pq is None else torus_link_vol(*pq)
        all_zero &= (v == 0.0)
        print(f"  {name:22s} Vol={v:.4f}  [{'trivial' if pq is None else 'torus'}, "
              f"{'Vol=0' if v == 0 else 'HYPERBOLIC'}]")
    print(f"\nall carriers Vol=0: {all_zero}  -> carriers set the CHANNEL, not the mass")
    print("mass-knots (hyperbolic, DISTINCT from carriers):")
    print(f"  muon:   4_1 figure-eight  Vol={float(snappy.Manifold('4_1').volume()):.4f}")
    print(f"  proton: Borromean         "
          f"Vol={float(snappy.Link(braid_closure=[1, -2] * 3).exterior().volume()):.4f}")
    print("\nreframing: 'which knot for m_c/m_tau' = find the HYPERBOLIC MASS-KNOT, "
          "not the torus carrier.")


if __name__ == "__main__":
    main()
