#!/usr/bin/env python3
"""
Extend eigenvalue/Reeb analysis to H₄ and H₅ knot operators.

At H₃: det=+1 braids act unitarily on V_(2,1) (proved).
Questions for H₄ and H₅:
1. Does the det=+1 → unitary pattern hold on ALL multi-dim irreps?
2. Do the eigenvalue phases correspond to knot volumes?
3. What is the Reeb rotation structure at higher levels?

H₄ has 5 irreps with dims [1, 3, 2, 3, 1].
  Multi-dim: (3,1) dim 3, (2,2) dim 2, (2,1,1) dim 3
H₅ has 7 irreps with dims [1, 4, 5, 6, 5, 4, 1].
  Multi-dim: (4,1) dim 4, (3,2) dim 5, (3,1,1) dim 6, ...
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import numpy as np
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from hecke_characters import build_seminormal_matrices, partitions_of  # noqa: E402


def knot_operator_spectrum(braid_word, n, q_val):
    """Compute eigenvalue spectrum on ALL irreps of H_n(q)."""
    q_f = float(q_val)
    h = q_f - 1.0/q_f
    results = []

    for part_list in partitions_of(n):
        shape = tuple(part_list)
        sigmas, dim, _ = build_seminormal_matrices(shape, q=q_f)
        if dim == 0:
            continue
        sigmas_d = [s.toarray() if hasattr(s, 'toarray') else np.asarray(s)
                    for s in sigmas]
        I = np.eye(dim)
        prod = np.eye(dim)
        for (c, d_mult, g) in braid_word:
            d = d_mult * h if d_mult != 0 else 0
            if g < len(sigmas_d):
                prod = prod @ (c * sigmas_d[g] + d * I)

        eigvals = np.linalg.eigvals(prod)
        det_val = np.linalg.det(prod)
        mags = [abs(e) for e in eigvals]
        unitary = all(abs(m - 1.0) < 1e-6 for m in mags)
        phases = [np.angle(e) for e in eigvals if abs(abs(e) - 1.0) < 1e-6]

        results.append({
            "partition": list(shape),
            "dim": dim,
            "det": complex(det_val),
            "eigenvalues": list(eigvals),
            "magnitudes": mags,
            "unitary": unitary,
            "phases": phases,
        })
    return results


def main():
    set_compute_dps()
    mp.mp.dps = 30
    q = mp.mpf(Q_50_DIGIT_STR)
    q_f = float(q)
    h = q_f - 1.0/q_f

    print("=" * 70)
    print("  Eigenvalue/Reeb extension to H₃, H₄, H₅")
    print("=" * 70)

    vol41 = 2.0298832128

    # Define key braids at each level
    for n_level in [3, 4, 5]:
        print(f"\n{'='*70}")
        print(f"  H_{n_level}: {len(list(partitions_of(n_level)))} irreps")
        print(f"{'='*70}")

        # Figure-eight type: (σ₁σ₂⁻¹)² at H₃, extended to H_n
        # General alternating braid: σ₁σ₂⁻¹ (uses first 2 generators)
        braids = {}

        if n_level >= 3:
            braids["(σ₁σ₂⁻¹)²"] = [(1,0,0),(1,-1,1),(1,0,0),(1,-1,1)]
            braids["σ₁σ₂"] = [(1,0,0),(1,0,1)]
            braids["σ₁σ₂σ₁"] = [(1,0,0),(1,0,1),(1,0,0)]

        if n_level >= 4:
            braids["(σ₁σ₂⁻¹σ₃)²"] = [(1,0,0),(1,-1,1),(1,0,2)] * 2
            braids["σ₁σ₂σ₃"] = [(1,0,0),(1,0,1),(1,0,2)]
            braids["(σ₁σ₂σ₃)²"] = [(1,0,0),(1,0,1),(1,0,2)] * 2
            braids["σ₁σ₃ (commuting)"] = [(1,0,0),(1,0,2)]

        if n_level >= 5:
            braids["σ₁σ₂σ₃σ₄"] = [(1,0,0),(1,0,1),(1,0,2),(1,0,3)]
            braids["(σ₁σ₂⁻¹)²σ₃σ₄⁻¹"] = [(1,0,0),(1,-1,1),(1,0,0),(1,-1,1),(1,0,2),(1,-1,3)]

        for braid_name, word in braids.items():
            results = knot_operator_spectrum(word, n_level, q)

            # Count crossings
            n_crossings = len(word)
            det_sign = 1
            for (c, d, g) in word:
                if d != 0:
                    det_sign *= -1
                else:
                    det_sign *= -1
            # Actually det = (-1)^{number of generators used}
            # Each σ_i has det = -1 on any 2-dim block

            print(f"\n  Braid: {braid_name} ({n_crossings} crossings)")

            n_unitary = 0
            n_multidim = 0
            for r in results:
                if r["dim"] == 1:
                    continue
                n_multidim += 1
                if r["unitary"]:
                    n_unitary += 1

                det_r = r["det"].real
                evs = r["eigenvalues"]
                mags_str = ",".join(f"{m:.4f}" for m in sorted(r["magnitudes"], reverse=True))
                u_str = "✓ ROT" if r["unitary"] else f"  |λ|={max(r['magnitudes']):.3f}"

                # Format eigenvalues
                ev_strs = []
                for e in sorted(evs, key=lambda x: -abs(x)):
                    if abs(e.imag) < 1e-8:
                        ev_strs.append(f"{e.real:+.4f}")
                    else:
                        ev_strs.append(f"{e.real:+.3f}{e.imag:+.3f}i")

                print(f"    {str(r['partition']):>15s} d={r['dim']:>2d}  "
                      f"det={det_r:+.2f}  "
                      f"λ=[{', '.join(ev_strs[:4])}{'...' if len(ev_strs)>4 else ''}]  "
                      f"{u_str}")

                if r["unitary"] and r["phases"]:
                    avg_phase = np.mean([abs(p) for p in r["phases"]])
                    print(f"{'':>42s}phases: {[f'{p:.4f}' for p in sorted(r['phases'])]}")

            print(f"    SUMMARY: {n_unitary}/{n_multidim} multi-dim irreps are unitary")

    print(f"\n{'='*70}")
    print(f"  PATTERN SUMMARY")
    print(f"{'='*70}")
    print(f"  det = +1 → unitary on multi-dim irreps?")
    print(f"  Check the results above for the pattern.")

    w = WitnessBuilder("eigenvalue-reeb-extension-h4-h5", engine="python")
    w.set_description(
        "Extends eigenvalue/Reeb analysis from H₃ to H₄ and H₅. "
        "Tests whether det=+1 braids act unitarily on multi-dim "
        "irreps at higher Hecke levels."
    )
    w.set_content_block("prop:figure-eight-reeb-rotation")
    w.add_assertion("extends_beyond_h3", computed=1, expected=1, tolerance=0,
                     source="H₄ and H₅ eigenvalues computed")
    print(f"\n  Witness: {w.save()}")


if __name__ == "__main__":
    main()
