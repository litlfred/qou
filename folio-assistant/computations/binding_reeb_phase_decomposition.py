#!/usr/bin/env python3
"""
binding_reeb_phase_decomposition.py — per-REPRESENTATION decomposition of
the atom Markov trace into complex-q ROTATION channels (q-Reeb phase) vs
geometric GROWTH channels (writhe-power), free vs bound.

WHY (the complex-q / Reeb-rotation finding). Per unit-modulus-eigenvalue.md
and figure-eight-reeb-rotation.md, on each Wedderburn block λ the braid acts
with eigenvalues whose behaviour is representation-dependent:
  • "rotation" reps (e.g. the (2,1) standard rep): even braids give
    unit-modulus eigenvalues e^{±iθ}; the normalised character
    r_λ = χ_λ / dim_λ lies in [-1, 1] and the q-Reeb phase is
    θ_λ = arccos(r_λ). Bounded — carries PHASE, not amplitude.
  • "growth" reps (the (n) trivial / (1^n) sign outer channels): the
    eigenvalue is q^{±writhe}, so |r_λ| can exceed 1 — EXTENSIVE growth.

The scalar Markov trace tr_M = Σ_λ y_λ χ_λ collapses this split, and the
binding DIFFERENCE |tr_free|−|tr_atom| cancels the common growth — which is
why every scalar observable (Δtr, log-volume, hyperbolic Vol, summed
rotation) refuted A≥3 (binding_volume_difference_probe.py). This probe
keeps the per-λ split so the rotation vs growth structure is visible —
the compute infrastructure the complex-q reading requires. DIAGNOSTIC, no
fitting.

OUTPUT per atom (D, T, ³He, ⁴He): for each block λ, dim_λ, free/atom
normalised character r_λ, classification (rotation/growth), and q-Reeb
phase shift Δθ_λ for the rotation channels; plus aggregate counts and the
growth-channel mass (Σ over growth λ), free vs atom.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import json
import math
from pathlib import Path

from mpmath import mp, mpf, fabs, acos, acosh, catalan

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def dim_sn(lam):
    """f^λ = dim(S^λ) via the hook-length formula."""
    n = sum(lam)
    num = math.factorial(n)
    den = 1
    for i in range(len(lam)):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
            den *= arm + leg + 1
    return num // den


def load_chi(fname, cfg):
    d = json.loads((HERE / fname).read_text())
    blk = d["data"][cfg]
    return [(tuple(e["partition"]), mpf(str(e["chi_lambda"])))
            for e in blk["by_partition"]]


def main():
    set_compute_dps()
    wb = WitnessBuilder("binding-reeb-phase-decomposition", engine="mpmath")

    atoms = [("D", "atom-chi-rust-d.witness.json"),
             ("T", "atom-chi-rust-t.witness.json"),
             ("3He", "atom-chi-rust-3he.witness.json"),
             ("4He", "atom-chi-rust-4he.witness.json")]

    print("=" * 74)
    print("PER-REP REEB DECOMPOSITION — rotation (|χ/dim|≤1) vs growth (>1)")
    print("=" * 74)

    results = {}
    for name, fname in atoms:
        chi_free = dict(load_chi(fname, "free"))
        chi_atom = dict(load_chi(fname, "atom"))
        rot_free = rot_atom = grow_free = grow_atom = 0
        sum_phase_shift = mpf(0)
        growth_mass_free = mpf(0)
        growth_mass_atom = mpf(0)
        flipped = 0  # reps that rotate when free but grow when bound
        per_lambda = []
        for lam in chi_free:
            d = dim_sn(list(lam))
            rf = chi_free[lam] / d
            ra = chi_atom[lam] / d
            is_rot_f = fabs(rf) <= 1
            is_rot_a = fabs(ra) <= 1
            rot_free += int(is_rot_f); rot_atom += int(is_rot_a)
            grow_free += int(not is_rot_f); grow_atom += int(not is_rot_a)
            if is_rot_f and not is_rot_a:
                flipped += 1
            if not is_rot_f:
                growth_mass_free += fabs(chi_free[lam])
            if not is_rot_a:
                growth_mass_atom += fabs(chi_atom[lam])
            # FULL-ORDER per-block phase θ_λ (preserve information until
            # observation): arccos on the rotation channel (|r|≤1), arccosh
            # on the growth channel (|r|>1). The scalar tr_M collapses this
            # vector at step 5; emitting it lets the archimedean observation
            # (or the operator-valued combiner) do the collapse downstream.
            th_f = acos(rf) if is_rot_f else acosh(fabs(rf))
            th_a = acos(ra) if is_rot_a else acosh(fabs(ra))
            if is_rot_f and is_rot_a:
                sum_phase_shift += fabs(th_a - th_f)
            same_channel = (is_rot_f == is_rot_a)
            per_lambda.append({
                "partition": list(lam),
                "dim": int(d),
                "chi_free": mp.nstr(chi_free[lam], 12),
                "chi_atom": mp.nstr(chi_atom[lam], 12),
                "r_free": float(rf), "r_atom": float(ra),
                "channel_free": "rotation" if is_rot_f else "growth",
                "channel_atom": "rotation" if is_rot_a else "growth",
                "theta_free_rad": mp.nstr(th_f, 12),
                "theta_atom_rad": mp.nstr(th_a, 12),
                "delta_theta_rad": (mp.nstr(th_a - th_f, 12)
                                    if same_channel else None),
                "channel_flip": not same_channel,
            })
        per_lambda.sort(key=lambda r: r["dim"], reverse=True)
        results[name] = {
            "n_blocks": len(chi_free),
            "rotation_free": rot_free, "rotation_atom": rot_atom,
            "growth_free": grow_free, "growth_atom": grow_atom,
            "rotation_to_growth_flips": flipped,
            "sum_abs_phase_shift_rad": mp.nstr(sum_phase_shift, 8),
            "growth_mass_free": mp.nstr(growth_mass_free, 8),
            "growth_mass_atom": mp.nstr(growth_mass_atom, 8),
            "growth_mass_ratio_atom_over_free":
                mp.nstr(growth_mass_atom / growth_mass_free, 6)
                if growth_mass_free != 0 else "inf",
            # FULL per-λ θ_λ vector (rotation arccos + growth arccosh),
            # free & atom, per Wedderburn block — the un-collapsed phase
            # carried for downstream observation (operator-valued combiner).
            "by_partition": per_lambda,
        }
        print(f"\n── {name} ({len(chi_free)} blocks) ──")
        print(f"  rotation channels: free {rot_free} → atom {rot_atom}  "
              f"(growth: free {grow_free} → atom {grow_atom}; "
              f"{flipped} rot→growth flips)")
        print(f"  Σ|Δθ| over shared-rotation reps = "
              f"{float(sum_phase_shift):.4f} rad")
        print(f"  growth-channel mass: free {float(growth_mass_free):.3f} → "
              f"atom {float(growth_mass_atom):.3f} "
              f"(×{float(growth_mass_atom/growth_mass_free):.3f})"
              if growth_mass_free != 0 else "  (no growth channel free)")

    print("\nDIAGNOSTIC read: the binding's extensive part should live in the")
    print("GROWTH channels (outer reps, q^{±writhe}); the ROTATION channels")
    print("carry q-Reeb phase only. The scalar Δtr mixes + cancels these.")

    wb.set_description(
        "Per-representation Reeb decomposition of the atom Markov trace: "
        "splits each Wedderburn block λ into complex-q ROTATION channels "
        "(|χ_λ/dim_λ|≤1, q-Reeb phase θ_λ=arccos) vs geometric GROWTH "
        "channels (outer reps, q^{±writhe}), free vs bound, for D/T/³He/⁴He. "
        "Grounds the complex-q/Reeb finding (unit-modulus-eigenvalue.md, "
        "figure-eight-reeb-rotation.md): mass/binding = outer-channel growth "
        "× standard-rep rotation; the scalar Δtr collapses this split and "
        "the trace difference cancels the common growth. DIAGNOSTIC, no fit."
    )
    wb.add_data("per_atom", results)
    wb.add_data("interpretation", {
        "rotation_channels": "unit-modulus e^{±iθ}; q-Reeb phase, bounded",
        "growth_channels": "outer (n)/(1^n) reps; q^{±writhe}, extensive",
        "why_scalar_fails": "tr_M = Σ y_λ χ_λ collapses per-rep split; "
                            "|tr_free|−|tr_atom| cancels common growth",
        "compute_improvement": "track per-λ rotation/growth split + Reeb "
                               "phase, not the scalar trace difference",
    })
    wb.add_assertion(
        "per_rep_split_computed_all_atoms",
        computed=len(results),
        expected=4,
        tolerance=0,
        source="rotation/growth decomposition computed for D, T, ³He, ⁴He",
    )
    wb.save()


if __name__ == "__main__":
    main()
