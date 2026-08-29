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

PRECISION (2026-08-10). The first version called `float(M.volume())`, which
truncates SnapPy's result to float64 and put 15 raw float64 values into the
witness. That reached `main` because the precision gate was never run on the
PR that introduced it. Now: volumes are requested at `BITS_PREC` and carried as
`mpmath.mpf`, PDG masses are string-constructed, and everything serialized goes
through `_precision.fmt`.

The float64 volumes were correct to ~16 digits (7.327724753417753 vs
7.32772475341775212...), so the verdict is untouched — the misses are 4% and
40%. What changes is that the witness now records what SnapPy actually computed
rather than a truncation of it.

Requires SnapPy (pip install snappy_manifolds snappy). Emits a witness.
"""
from __future__ import annotations

import json

import _path_bridge  # noqa: F401
from _precision import fmt, set_compute_dps  # noqa: E402
from codata_constants import M_P_MEV_VALIDATION  # noqa: E402

import snappy  # noqa: E402
from mpmath import mpf  # noqa: E402

from pathlib import Path as _PathW  # noqa: E402 — witness output root
_HERE_W = _PathW(__file__).resolve().parent

# SnapPy's volume is computed at a requested bit precision; 230 bits ~ 69 dps,
# which covers the repo's 65-dps compute default with margin.
BITS_PREC = 230


def vol_comps(word):
    """Hyperbolic volume (mpf, high precision) and cusp count of a braid closure."""
    L = snappy.Link(braid_closure=word)
    M = L.exterior()
    # str() round-trips SnapPy's Number at full requested precision; float()
    # would discard everything past the 16th digit.
    return mpf(str(M.volume(bits_prec=BITS_PREC))), int(M.num_cusps())


def main():
    set_compute_dps()

    # Lambda_c, Lambda_b (MeV) — PDG central values, string-constructed so no
    # float64 intermediate ever exists.  The proton comes from CODATA rather
    # than a hand-typed 938.272: string-construction stops the float, but it
    # does not make a rounded literal accurate.
    mp, mLc, mLb = M_P_MEV_VALIDATION, mpf("2286.46"), mpf("5619.60")

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
        "mass ratio. Near-coincidence Vol((s1s2^-1)^5)/Vol(Borromean)=%s vs "
        "Lambda_c/proton=%s (~4%%) is DISQUALIFIED: (s1s2^-1)^5 is a KNOT "
        "(1 component), not a 3-quark baryon, and bottom (n=7) misses by ~40%%. "
        "3-component-correct candidates miss the charm ratio and closing the gap "
        "needs tuned twist count (=fit). Comparison also assumes mass~Vol "
        "(constant density), not the canonical absolute-mass law. m_c OPEN."
    ) % (fmt(uniform[5]["vol"] / v3, 4), fmt(mLc / mp, 4))

    print("uniform (s1 s2^-1)^n:")
    for n, d in uniform.items():
        tag = "3-quark link" if d["components"] == 3 else "KNOT (wrong topology)"
        print(f"  n={n}: Vol={fmt(d['vol'], 6)} comps={d['components']} [{tag}]")
    print(f"  Vol(5)/Vol(3)={fmt(uniform[5]['vol']/v3, 6)} vs Lc/p={fmt(mLc/mp, 6)} "
          f"({fmt(100*(uniform[5]['vol']/v3/(mLc/mp)-1), 3)}%)")
    print(f"  Vol(7)/Vol(3)={fmt(uniform[7]['vol']/v3, 6)} vs Lb/p={fmt(mLb/mp, 6)} "
          f"({fmt(100*(uniform[7]['vol']/v3/(mLb/mp)-1), 3)}%)")
    print("3-component-preserving charmed-baryon candidates:")
    for name, d in three_comp.items():
        print(f"  {name:24s} Vol={fmt(d['vol'], 6)} comps={d['components']} "
              f"ratio/proton={fmt(d['ratio_over_proton'], 4)}")
    print("\nVERDICT:", verdict)

    witness = {
        "schema": "witness/v1-informal",
        "description": "charm_composite_volume_probe: SnapPy complex-volume test "
                       "of composite charmed-baryon braids vs heavy-baryon masses.",
        "producer": "computations/charm_composite_volume_probe.py",
        "consumes": ["conj:complex-mass-constituent-functional"],
        "precision": {
            "engine": "snappy+mpmath",
            "dps": set_compute_dps(),
            "snappy_bits_prec": BITS_PREC,
        },
        "inputs": {
            "proton_MeV": fmt(mp),
            "Lambda_c_MeV": fmt(mLc),
            "Lambda_b_MeV": fmt(mLb),
        },
        "results": {
            "uniform_power_family": {
                str(n): {"vol": fmt(d["vol"]), "components": d["components"]}
                for n, d in uniform.items()
            },
            "three_component_candidates": {
                name: {
                    "vol": fmt(d["vol"]),
                    "components": d["components"],
                    "ratio_over_proton": fmt(d["ratio_over_proton"]),
                }
                for name, d in three_comp.items()
            },
        },
        "verdict": verdict,
        "scope": "(a) scope-limited negative under mass~Vol; SnapPy now available "
                 "for principled follow-up (variable-density / projection).",
    }
    with open(_HERE_W / "charm-composite-volume.witness.json", "w") as f:
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
    print("\nwrote computations/charm-composite-volume.witness.json")


if __name__ == "__main__":
    main()
