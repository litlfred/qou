#!/usr/bin/env python3
"""charm_composite_volume_probe.py — SnapPy test of the composite-braid
complex-volume reading of heavy-flavour baryon masses.

Follow-up to docs/audits/2026-08-02-charm-mass-tower-negative.md, which
established (scope-(b)) that the charm mass cannot be the CARRIER T(3,5)'s
complex volume (torus knot: Vol=0, CS rational) and must, if anything, be the
COMPOSITE charmed-hadron braid's complex volume.

Construction (parameter-free, framework-motivated): the proton is the Borromean
baryon = closure of (s1 s2^-1)^3. Generation windings are n=3,5,7, so the
uniform generation-power family (s1 s2^-1)^n is the natural non-tuned candidate;
a 3-component-preserving variant adds winding to one strand while keeping the
braid permutation trivial (3 quarks = 3 components).

VERDICT (see below): NO parameter-free composite-braid volume reproduces the
charmed-baryon mass ratio. The one near-coincidence -- Vol((s1 s2^-1)^5) /
Vol(Borromean) = 2.33 vs Lambda_c/proton = 2.44 (4%) -- is DISQUALIFIED:
(s1 s2^-1)^5 is a KNOT (1 component), not a 3-quark baryon, and the next data
point (bottom, n=7) misses by 40%. The topologically-correct 3-component
candidates do not hit the charm ratio without tuning the twist count (= fit).
The comparison also assumes mass ~ Vol (constant density), which is NOT the
canonical absolute-mass law. => charm mass stays OPEN; report as a coincidence,
not a result.

Requires SnapPy (pip install snappy_manifolds snappy). Emits a witness.
"""
import json

import snappy


def vol_comps(word):
    L = snappy.Link(braid_closure=word)
    M = L.exterior()
    return float(M.volume()), int(M.num_cusps())


def main():
    mp, mLc, mLb = 938.272, 2286.46, 5619.60  # proton, Lambda_c, Lambda_b (MeV)

    uniform = {}
    for n in (3, 5, 7, 9):
        v, c = vol_comps([1, -2] * n)
        uniform[n] = {"vol": v, "components": c}

    v3 = uniform[3]["vol"]
    three_comp = {}
    for name, w in {
        "borromean.s1^2": [1, -2] * 3 + [1, 1],
        "borromean.s1^4": [1, -2] * 3 + [1, 1, 1, 1],
        "borromean.s1^2 s2^2": [1, -2] * 3 + [1, 1, 2, 2],
        "borromean.s1^2 s2^-2": [1, -2] * 3 + [1, 1, -2, -2],
    }.items():
        v, c = vol_comps(w)
        three_comp[name] = {"vol": v, "components": c, "ratio_over_proton": v / v3}

    verdict = (
        "NO parameter-free composite-braid volume reproduces the charmed-baryon "
        "mass ratio. Near-coincidence Vol((s1s2^-1)^5)/Vol(Borromean)=%.3f vs "
        "Lambda_c/proton=%.3f (~4%%) is DISQUALIFIED: (s1s2^-1)^5 is a KNOT "
        "(1 component), not a 3-quark baryon, and bottom (n=7) misses by ~40%%. "
        "3-component-correct candidates miss the charm ratio and closing the gap "
        "needs tuned twist count (=fit). Comparison also assumes mass~Vol "
        "(constant density), not the canonical absolute-mass law. m_c OPEN."
    ) % (uniform[5]["vol"] / v3, mLc / mp)

    print("uniform (s1 s2^-1)^n:")
    for n, d in uniform.items():
        tag = "3-quark link" if d["components"] == 3 else "KNOT (wrong topology)"
        print(f"  n={n}: Vol={d['vol']:.4f} comps={d['components']} [{tag}]")
    print(f"  Vol(5)/Vol(3)={uniform[5]['vol']/v3:.4f} vs Lc/p={mLc/mp:.4f} "
          f"({100*(uniform[5]['vol']/v3/(mLc/mp)-1):+.1f}%)")
    print(f"  Vol(7)/Vol(3)={uniform[7]['vol']/v3:.4f} vs Lb/p={mLb/mp:.4f} "
          f"({100*(uniform[7]['vol']/v3/(mLb/mp)-1):+.1f}%)")
    print("3-component-preserving charmed-baryon candidates:")
    for name, d in three_comp.items():
        print(f"  {name:24s} Vol={d['vol']:.4f} comps={d['components']} "
              f"ratio/proton={d['ratio_over_proton']:.3f}")
    print("\nVERDICT:", verdict)

    witness = {
        "schema": "witness/v1-informal",
        "description": "charm_composite_volume_probe: SnapPy complex-volume test "
                       "of composite charmed-baryon braids vs heavy-baryon masses.",
        "producer": "computations/charm_composite_volume_probe.py",
        "consumes": ["conj:complex-mass-constituent-functional"],
        "inputs": {"proton_MeV": mp, "Lambda_c_MeV": mLc, "Lambda_b_MeV": mLb},
        "results": {"uniform_power_family": uniform,
                    "three_component_candidates": three_comp},
        "verdict": verdict,
        "scope": "(a) scope-limited negative under mass~Vol; SnapPy now available "
                 "for principled follow-up (variable-density / projection).",
    }
    with open("computations/charm-composite-volume.witness.json", "w") as f:
        json.dump(witness, f, indent=2)
    print("\nwrote computations/charm-composite-volume.witness.json")


if __name__ == "__main__":
    main()
