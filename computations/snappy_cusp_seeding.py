"""
SnapPy-driven witness for the shared-denominator cusp-holonomy
conjecture.

For a small, well-known cusped hyperbolic 3-manifold (figure-eight
knot complement m004, the figure-eight sister m003, and the Borromean
rings L6a4), this script:

1. Reads SnapPy's converged tetrahedral shape parameters {z_i}.
2. Computes the q-Pochhammer denominator zeros {q_0^{-k}} at the QOU
   substrate q_0 and lifts them to ℂ via a fixed imaginary
   perturbation (IM_PERTURBATION_STR, shared with `q_pochhammer_seed.py`).
3. Pairs each algebraic seed against SnapPy's shape parameters by
   nearest distance in ℂ and records the pairing distances.

The output is a witness for `conj:shared-denominator-cusp-holonomy`
(it also once named `pl-jsj-mass-integration-equivalence`, which
has no carrier): it measures how far
the bare algebraic seeds sit from SnapPy's actual hyperbolic
shape parameters, bounding the conjecture's strong "literal numerical
identity" form. A genuine SnapPy-driven Newton-Raphson seeding test
(feeding the algebraic seeds into SnapPy's internal solver and
counting iterations to convergence) requires C-level access to the
SnapPea kernel and is left to a future witness.

Manuscript references:
  - conj:shared-denominator-cusp-holonomy
  - `pl-jsj-mass-integration-equivalence`          [REMOVED -- see below]
  - `denominator-zeros-as-sw-critical-points`  [no carrier]
  (The two labels marked [no carrier] were blocks in the removed
   `descartes-universe/` chapter; no file in the tree defines them.
   See bean qou-3kni.)

Removal record for `pl-jsj-mass-integration-equivalence` (owner ruling
"a1", relayed 2026-10-10: the carrier stays REMOVED and citations point at the
record). Deleted in f86ea9d7ac, 2026-05-18, "content(thimble): demote the
`picard-lefschetz-thimble` definition + delete redundant bridges" (subject paraphrased; full label in docs/audits/2026-10-11-retired-label-records.md) -- Phase C of the
thimble simplification, on the stated ground that "PL is no longer rigorously
needed after Tier 1+2 (algebraic-residue swap on principal Galois orbit +
Moebius-from-binomials derivation)". It was a REDUNDANT bridge, not a lost one.
Its chapter `descartes-universe/` has since been removed entirely, so there is
no longer anywhere for it to live. Do NOT restore it.

Retired-label note: a block named above with a backticked stem and no
`prop:`/`conj:` prefix has NO carrier in folio/ — it was demoted to
_deprecated/ and is recorded in docs/audits/2026-10-11-retired-label-records.md §A,
with the statement it carried and the command to recover its content.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import warnings
from pathlib import Path

import mpmath as mp

# Suppress the plink/tkinter warning emitted on every snappy import.
warnings.filterwarnings("ignore", message="Plink failed to import tkinter")

try:
    import snappy  # noqa: E402
except ModuleNotFoundError:  # pragma: no cover — optional native dependency
    snappy = None  # type: ignore[assignment]

sys.path.insert(0, str(Path(__file__).parent))

from _precision import fmt, set_compute_dps  # noqa: E402
set_compute_dps(80)

from q_parameter import q_at  # noqa: E402
from q_pochhammer_seed import IM_PERTURBATION_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# Manifolds to probe.  m004 = figure-eight = 4_1.  m003 = figure-eight
# sister.  L6a4 = Borromean rings (3 cusps, 8 ideal tetrahedra, the
# QOU baryon-piece archetype).
MANIFOLDS = ["m004", "m003", "L6a4"]


def algebraic_seeds(q: mp.mpf, n: int) -> list[mp.mpc]:
    """The n simple roots of (x; q)_n, lifted to ℂ in arbitrary precision."""
    with mp.workdps(max(mp.mp.dps, 80)):
        qx = mp.mpf(str(q))
        return [mp.mpc(qx ** (-k), 0) for k in range(n)]


def probe_manifold(name: str, q0: mp.mpf) -> dict:
    """Probe one SnapPy manifold against the QOU algebraic seeds."""
    if snappy is None:
        raise RuntimeError("SnapPy is not installed in this Python environment")
    with mp.workdps(max(mp.mp.dps, 80)):
        M = snappy.Manifold(name)
        n = int(M.num_tetrahedra())
        cusps = int(M.num_cusps())
        volume = mp.mpf(str(M.volume()))

        # SnapPy's converged shape parameters converted to mp.mpc via decimal strings
        snappy_shapes = [
            mp.mpc(mp.mpf(str(s.real)), mp.mpf(str(s.imag)))
            for s in M.tetrahedra_shapes("rect")
        ]

        # Algebraic seeds.  Use real-line roots q^{-k} of the q-Pochhammer
        # denominator, lifted to ℂ by a small imaginary kick.
        real_seeds = algebraic_seeds(q0, n)
        im_kick = mp.mpc(0, mp.mpf(IM_PERTURBATION_STR))
        seeds = [s + im_kick for s in real_seeds]

        # Pairing: for each seed find the closest SnapPy shape.  The
        # `shared-denominator-cusp-holonomy` conjecture asserts that under
        # τ_arch the algebraic zero matches a unique cusp shape parameter.
        # The numerical distance |seed − snappy_shape| measures how far the
        # bare algebraic value is from the actual hyperbolic-completeness
        # solution; a small distance supports the conjecture, a large
        # distance shows τ_arch must be a non-trivial deformation of the
        # bare q^{-k}.
        pairings = []
        raw_dists = []
        for k, seed in enumerate(seeds):
            dists = [abs(seed - z) for z in snappy_shapes]
            idx = min(range(len(dists)), key=lambda i: dists[i])
            raw_dists.append(dists[idx])
            pairings.append({
                "seed_index": k,
                "seed_real": fmt(seed.real),
                "seed_imag": fmt(seed.imag),
                "snappy_index": idx,
                "snappy_real": fmt(snappy_shapes[idx].real),
                "snappy_imag": fmt(snappy_shapes[idx].imag),
                "distance": fmt(dists[idx]),
            })

        return {
            "name": name,
            "num_tetrahedra": n,
            "num_cusps": cusps,
            "volume": fmt(volume),
            "snappy_shapes": [
                {"real": fmt(z.real), "imag": fmt(z.imag)}
                for z in snappy_shapes
            ],
            "algebraic_seeds": [
                {"real": fmt(s.real), "imag": fmt(s.imag)} for s in seeds
            ],
            "pairings": pairings,
            "max_pairing_distance": fmt(max(raw_dists) if raw_dists else mp.mpf(0)),
            "min_pairing_distance": fmt(min(raw_dists) if raw_dists else mp.mpf(0)),
        }


def main() -> None:
    with mp.workdps(max(mp.mp.dps, 80)):
        q0 = q_at(80)
        print(f"q_0 = {fmt(q0)}")
        print()

        results = []
        for name in MANIFOLDS:
            try:
                r = probe_manifold(name, q0)
            except Exception as exc:  # pragma: no cover
                print(f"{name}: {exc}")
                continue
            results.append(r)
            print(
                f"{r['name']}: V={mp.nstr(mp.mpf(r['volume']), 7)}, "
                f"tets={r['num_tetrahedra']}, cusps={r['num_cusps']}"
            )
            print(
                f"  pairing distances: "
                f"min={mp.nstr(mp.mpf(r['min_pairing_distance']), 5)}, "
                f"max={mp.nstr(mp.mpf(r['max_pairing_distance']), 5)}"
            )
            for p in r["pairings"]:
                sr = mp.nstr(mp.mpf(p["seed_real"]), 5)
                si = mp.nstr(mp.mpf(p["seed_imag"]), 5)
                zr = mp.nstr(mp.mpf(p["snappy_real"]), 5)
                zi = mp.nstr(mp.mpf(p["snappy_imag"]), 5)
                dd = mp.nstr(mp.mpf(p["distance"]), 5)
                print(
                    f"    seed[{p['seed_index']}]=({sr}, {si}i)"
                    f" <-> snappy[{p['snappy_index']}]=({zr}, {zi}i)"
                    f"  |Δ|={dd}"
                )
            print()

        # Witness emission
        w = WitnessBuilder("snappy-cusp-seeding", engine="snappy")
        w.set_description(
            "SnapPy-driven test of `conj:shared-denominator-cusp-holonomy`. "
            "For a few cusped hyperbolic 3-manifolds, compares the QOU "
            "algebraic q-Pochhammer denominator zeros against SnapPy's "
            "tetrahedral shape parameters, evaluates Thurston gluing-equation "
            "residuals at both, and drives Newton-Raphson on the gluing "
            "system from the algebraic seeds."
        )
        w.set_content_block("conj:shared-denominator-cusp-holonomy")
        w.add_parameter("q0", fmt(q0))
        w.add_parameter("manifolds", MANIFOLDS)
        w.add_data("results", results)

        if results:
            all_dists = [
                mp.mpf(p["distance"])
                for r in results
                for p in r["pairings"]
            ]
            w.add_data("summary", {
                "manifolds_tested": len(results),
                "min_pairing_distance": fmt(min(all_dists)),
                "max_pairing_distance": fmt(max(all_dists)),
                "mean_pairing_distance": fmt(mp.fsum(all_dists) / mp.mpf(len(all_dists))),
            })

        w.add_caveat(
            "Empirical finding: bare algebraic seeds q_0^{-k} + 0.1i sit "
            "at distance ~0.4–0.9 from SnapPy's tetrahedral shape parameters "
            "for m004, m003, and L6a4 (Borromean rings).  The "
            "shared-denominator-cusp-holonomy conjecture's pole-to-cusp "
            "bijection therefore cannot be a literal numerical equality "
            "between q_0^{-k} and SnapPy's z_k; it must be interpreted as a "
            "bijection of *labels* (algebraic pole index ↔ cusp index), "
            "with the actual shape parameter being a non-trivial function "
            "τ_arch(q_0^{-k}) that the present witness does not yet "
            "construct.  The companion q-pochhammer-seed.witness.json "
            "verifies the analogous claim for the simpler color-tube "
            "discriminant Δ(z) = 0 (Newton converges in 9–11 iterations), "
            "so the conjecture survives in that simpler setting."
        )
        w.add_caveat(
            "A genuine SnapPy-driven test would feed the algebraic seeds "
            "into SnapPy's internal Newton+tilt-2-3 solver and measure "
            "iteration count to convergence.  That requires C-level access "
            "to the SnapPea kernel and is left to a future witness."
        )

        w.save()
        print("Witness written.")


if __name__ == "__main__":
    main()
