#!/usr/bin/env python3
"""
Per-generator spectral coordinates V̂_i for any atom.

Computes the Hoefsmit seminormal eigenvalues of the per-generator
transfer matrices on V_(2,1) for any atomic braid word. These are
the spectral coordinates that enter the mass-endomorphism tower.

Generic infra — works for any (Z,N).
"""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import json
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from canonical_braid_crossings import (  # noqa: E402
    atom_canonical_crossings, d_for_ctype,
)


def spectral_coordinates(Z, N):
    """Compute per-generator spectral coordinates V̂_i for atom (Z,N)."""
    set_compute_dps()
    q = float(Q_50_DIGIT_STR[:20])
    h = q - 1 / q
    d1 = q**3 / (q**2 + 1)
    d2 = -1 / q / (q**2 + 1)
    b = float(((q**4 + q**2 + 1) / (q**2 + 1)**2) ** 0.5)

    # Hoefsmit seminormal V_(2,1) of H_3. The off-diagonal generator must
    # use diagonal entries (d2, d1) — NOT (d1, d2) — to satisfy the braid
    # relation σ₀σ₁σ₀ = σ₁σ₀σ₁ (verified symbolically; the swapped form
    # fails it). The (d1, d2) ordering was a latent bug.
    sigma0 = np.array([[q, 0], [0, -1 / q]])
    sigma1 = np.array([[d2, b], [b, d1]])

    crossings = atom_canonical_crossings(Z, N)

    gen_products = {}
    for gen, ctype in crossings:
        sigma = sigma0 if gen % 2 == 0 else sigma1
        # Every ctype resolves through the canonical `d_for_ctype`. The
        # private if/elif this replaces had `else: M = eye(2)`, which did not
        # approximate an unrecognised crossing -- it DELETED it. When
        # `averaged_weighted` was added for the colour-weighted p-n interface
        # (qou-gdtb), every Z>=1,N>=1 atom silently lost its one interface
        # crossing from the spectral coordinate, with no error raised.
        M = sigma + float(d_for_ctype(ctype, h)) * np.eye(2)

        if gen not in gen_products:
            gen_products[gen] = np.eye(2)
        gen_products[gen] = gen_products[gen] @ M

    result = {}
    for gen in sorted(gen_products.keys()):
        eigvals = np.linalg.eigvals(gen_products[gen])
        V_hat = float(np.max(np.abs(eigvals)))
        converges = V_hat < q  # Li₂^q converges for |V| < q
        result[gen] = {
            "V_hat": V_hat,
            "eigenvalues": [complex(e) for e in eigvals],
            "li2q_converges": converges,
        }

    return crossings, result


def main():
    t0 = time.perf_counter()
    atoms = [
        (1, 0, "proton"),
        (0, 1, "neutron"),
        (1, 1, "deuteron"),
        (1, 2, "tritium"),
        (2, 1, "He-3"),
        (2, 2, "He-4"),
    ]

    all_results = {}
    for Z, N, name in atoms:
        try:
            crossings, specs = spectral_coordinates(Z, N)
            n_cross = len(crossings)
            n_gen = len(specs)
            converges = all(s["li2q_converges"] for s in specs.values())
            max_V = max(s["V_hat"] for s in specs.values())

            all_results[name] = {
                "Z": Z, "N": N,
                "crossings": n_cross,
                "generators": n_gen,
                "max_V_hat": max_V,
                "li2q_all_converge": converges,
                "per_generator": {
                    str(g): {"V_hat": s["V_hat"], "converges": s["li2q_converges"]}
                    for g, s in specs.items()
                },
            }

            status = "✓ converges" if converges else "✗ DIVERGES"
            print(f"{name:10s} (Z={Z},N={N}): {n_cross} crossings, "
                  f"{n_gen} gens, max V̂={max_V:.4f} {status}")
        except Exception as e:
            print(f"{name:10s}: ERROR — {e}")

    wb = WitnessBuilder("spectral-coordinates-all-atoms", start_time=t0)
    wb.data["atoms"] = all_results
    # THE RETRACTION LIVES HERE NOW, NOT ONLY IN THE ARTIFACT.
    #
    # This finding was RETRACTED on 2026-05-27 — by hand, on the committed
    # witness, without touching this producer. So re-running it for ANY reason
    # emitted the withdrawn claim again, with `RETRACTED` and
    # `retraction_reason` simply absent, and the corpus silently un-retracted
    # itself. Observed 2026-08-24 during a staleness drain: `data_keys 4 -> 2`,
    # `finding` back to "DIVERGES", which is precisely what the retraction says
    # is wrong.
    #
    # Nothing in the staleness family objects to that. The producer's hash
    # matches its own bytes, so the witness reads as perfectly healthy; only
    # `witness_shape_guard`'s key-count rule caught it, and a bare RETRACTED
    # flag with no accompanying reason would have been 4 -> 3 and might have
    # stayed under tolerance.
    #
    # A retraction applied only to an artifact is not a retraction — it is a
    # note that survives exactly until someone re-runs the thing.
    wb.data["RETRACTED"] = True
    wb.data["retraction_reason"] = (
        "V̂ values computed here are Hoefsmit matrix-product eigenvalues "
        "(grow > 1 with crossing count), NOT the additive Wedderburn traced "
        "volumes V̂_i^full (bounded < 1) used in the mass-endomorphism tower. "
        "Li₂^q CONVERGES at the correct V̂_i^full values. Retracted "
        "2026-05-27. See session discussion."
    )
    wb.data["finding"] = (
        "RETRACTED — Li₂^q CONVERGES at correct V̂_i^full < 1 for A≥2 "
        "(max V̂ > 1 for deuteron+). The binding energy formula "
        "B = m_e × C_knot × |sum| uses the interface operator, NOT the Li₂^q "
        "blow-up expansion. C_knot = 35/6 + 2ℏ² (0.015%) is an empirical "
        "identification; its derivation requires the interface operator's "
        "eigenvalue structure, not the Li₂^q convergent series."
    )
    wb.add_assertion(
        "proton_converges",
        computed=1 if all_results.get("proton", {}).get("li2q_all_converge") else 0,
        expected=1,
        tolerance=0,
    )
    wb.save()
    print(f"\n✓ Witness: spectral-coordinates-all-atoms.witness.json")


if __name__ == "__main__":
    main()
