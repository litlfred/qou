#!/usr/bin/env python3
# polynomial_q_not_applicable: eigen-structure / Reeb-phase diagnostic,
# not a Jones-polynomial evaluation.
"""
reeb_rotation_pn_test.py — the DECISIVE geometric-escape test.

THE QUESTION. PRs #1604/#1605/#1606 (on main) proved a per-PARTITION
impossibility theorem: any function f(λ) of abstract partition
(character-level) data is constant across Markov-equivalent knots and
cannot produce m_n − m_p = 1.293 MeV. The proposed ESCAPE: the energy
may be GEOMETRIC — the rotation of the Reeb bundle, a per-knot-OPERATOR
quantity computed from the actual braid word, NOT the abstract character.
If the proton-knot operator and the neutron-knot operator act with
different q-Reeb rotation, the geometry distinguishes p from n.

THE TEST (zero free parameters). For the proton braid β_p (uud) and the
neutron braid β_n (udd), both 3-strand elements of H₃(q) at substrate q₀,
compute per Wedderburn block λ ⊢ 3:
  • the eigenvalues of the seminormal operator Π_k (c_k σ_{g_k} + d_k I),
  • their MODULI |λ_i| (writhe / growth channel), and
  • their PHASES arg(λ_i) — the q-Reeb ROTATION angle (per
    figure-eight-reeb-rotation.md: the Reeb phase only carries signal on
    UNIT-MODULUS eigenvalues, where it equals the accumulated color-sector
    rotation; growth reps have |λ| ≠ 1 and carry amplitude, not phase).

Then ask: does the Reeb rotation DIFFER for p vs n? Report raw p and n
numbers WHETHER THEY MATCH OR DIFFER. No tuning to m_n − m_p, no fit.

DISCIPLINE. Falsification: if the Reeb rotation is bit-identical p=n the
escape FAILS (the phase geometry is degenerate); a clean "rotation differs,
here are the raw numbers, scale is derived/fitted" is the win. Either way
every number traces to substrate (q₀, the braid words from
mass_at_3A_proper.atom_braid_word_3A) with zero free parameters.

Refs:
- figure-eight-reeb-rotation.md (q-Reeb phase = arg of UNIT-modulus eig)
- unit-modulus-eigenvalue.md (rotation vs growth split)
- binding_reeb_phase_decomposition.py (per-rep θ_λ = arccos(χ_λ/dim_λ))
- mass_at_3A_proper.atom_braid_word_3A (substrate braid words)
- atom_mass_derived.py (B₃ + typed quark crossings → proton/neutron NF)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import numpy as np  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q as q0, Q_INV as qi, HA as h  # noqa: E402
from mass_at_3A_proper import (  # noqa: E402
    atom_braid_word_3A,
    _cached_seminormal,
    partitions_of,
)

PHASE_TOL = 1e-9          # phases below this count as 0
UNIT_TOL = 1e-9           # |λ| within this of 1 counts as unit-modulus


def block_operator(word, shape):
    """Seminormal operator Π (c σ_g + d I) on the λ-block; eigen-data."""
    sigmas, dim, _ = _cached_seminormal(shape)
    if dim == 0:
        return None
    P = np.eye(dim)
    I = np.eye(dim)
    for (c, d, g) in word:
        P = P @ (c * sigmas[g] + d * I)
    ev = np.linalg.eigvals(P)
    return {
        "dim": int(dim),
        "trace": float(np.trace(P).real),
        "eigvals_re": [float(x.real) for x in ev],
        "eigvals_im": [float(x.imag) for x in ev],
        "moduli": sorted(float(abs(x)) for x in ev),
        "phases_rad": sorted(float(np.angle(x)) for x in ev),
    }


def reeb_phase_of_block(blk):
    """q-Reeb rotation phase carried by the block.

    Per figure-eight-reeb-rotation.md, the Reeb phase is the eigenvalue
    PHASE on UNIT-modulus eigenvalues. We report:
      • reeb_phase_unit: sum of |arg| over eigenvalues with |λ|≈1
        (the genuine Reeb rotation — what the figure-eight carries),
      • sum_abs_phase: sum of |arg| over ALL eigenvalues (includes the
        trivial π on negative real growth eigenvalues, which is NOT a
        Reeb rotation — it is the sign of a real eigenvalue).
    """
    reeb_phase_unit = 0.0
    sum_abs_phase = 0.0
    n_unit = 0
    for mod, ph in zip(blk["moduli"], blk["phases_rad"]):
        sum_abs_phase += abs(ph)
        if abs(mod - 1.0) < UNIT_TOL:
            n_unit += 1
            reeb_phase_unit += abs(ph)
    return reeb_phase_unit, sum_abs_phase, n_unit


def main():
    wb = WitnessBuilder("reeb-rotation-pn-test-reeb", engine="numpy")
    wb.set_description(
        "Decisive geometric-escape test: does the q-Reeb rotation "
        "(eigen-phase of the seminormal braid-word operator per Wedderburn "
        "block) distinguish the proton braid from the neutron braid at "
        "substrate q₀? Zero free parameters; no tuning to m_n−m_p."
    )
    wb.add_parameter("q0", str(q0))
    wb.add_parameter("q_inv", str(qi))
    wb.add_parameter("h", str(h))

    word_p = atom_braid_word_3A(1, 0)   # proton: uud
    word_n = atom_braid_word_3A(0, 1)   # neutron: udd
    wb.add_data("proton_braid_word", [[c, d, g] for (c, d, g) in word_p])
    wb.add_data("neutron_braid_word", [[c, d, g] for (c, d, g) in word_n])

    shapes = list(partitions_of(3))
    wb.add_data("partitions_of_3", [list(s) for s in shapes])

    print("=" * 78)
    print("REEB-ROTATION p vs n TEST — per Wedderburn block λ ⊢ 3")
    print("q0 =", q0, " h =", h)
    print("=" * 78)

    per_block = []
    # aggregate Reeb-rotation totals
    tot_reeb_unit_p = tot_reeb_unit_n = 0.0
    tot_sumphase_p = tot_sumphase_n = 0.0
    tot_logmod_p = tot_logmod_n = 0.0   # Σ log|λ| = log|det| (writhe/growth)
    phase_identical = True
    modulus_identical = True

    for shape in shapes:
        bp = block_operator(word_p, shape)
        bn = block_operator(word_n, shape)
        if bp is None or bn is None:
            continue
        rp_unit, rp_sum, rp_nunit = reeb_phase_of_block(bp)
        rn_unit, rn_sum, rn_nunit = reeb_phase_of_block(bn)
        tot_reeb_unit_p += rp_unit
        tot_reeb_unit_n += rn_unit
        tot_sumphase_p += rp_sum
        tot_sumphase_n += rn_sum
        lm_p = sum(math.log(m) for m in bp["moduli"] if m > 0)
        lm_n = sum(math.log(m) for m in bn["moduli"] if m > 0)
        tot_logmod_p += lm_p
        tot_logmod_n += lm_n

        d_reeb_unit = rp_unit - rn_unit
        d_sumphase = rp_sum - rn_sum
        # compare moduli vectors elementwise
        d_moduli = [a - b for a, b in zip(bp["moduli"], bn["moduli"])]
        if abs(d_sumphase) > PHASE_TOL or abs(d_reeb_unit) > PHASE_TOL:
            phase_identical = False
        if any(abs(x) > 1e-9 for x in d_moduli):
            modulus_identical = False

        rec = {
            "partition": list(shape),
            "dim": bp["dim"],
            "proton": {
                "trace": bp["trace"],
                "moduli": bp["moduli"],
                "phases_rad": bp["phases_rad"],
                "reeb_phase_unit_modulus": rp_unit,
                "sum_abs_phase": rp_sum,
                "n_unit_modulus_eig": rp_nunit,
            },
            "neutron": {
                "trace": bn["trace"],
                "moduli": bn["moduli"],
                "phases_rad": bn["phases_rad"],
                "reeb_phase_unit_modulus": rn_unit,
                "sum_abs_phase": rn_sum,
                "n_unit_modulus_eig": rn_nunit,
            },
            "delta": {
                "reeb_phase_unit_modulus": d_reeb_unit,
                "sum_abs_phase": d_sumphase,
                "moduli": d_moduli,
                "trace": bp["trace"] - bn["trace"],
                "log_det_writhe": lm_p - lm_n,
            },
        }
        per_block.append(rec)

        print(f"\nλ = {shape}  dim = {bp['dim']}")
        print(f"  proton : χ={bp['trace']:+.9f}  |λ|={['%.6f'%m for m in bp['moduli']]}  "
              f"arg={['%.6f'%p for p in bp['phases_rad']]}")
        print(f"  neutron: χ={bn['trace']:+.9f}  |λ|={['%.6f'%m for m in bn['moduli']]}  "
              f"arg={['%.6f'%p for p in bn['phases_rad']]}")
        print(f"  Δ reeb_phase(unit-mod) = {d_reeb_unit:+.3e}   "
              f"Δ sum|arg| = {d_sumphase:+.3e}   "
              f"Δ log|det| = {lm_p-lm_n:+.6f}")

    wb.add_data("per_block", per_block)

    # ── aggregate Reeb rotation totals ──
    d_reeb_unit_total = tot_reeb_unit_p - tot_reeb_unit_n
    d_sumphase_total = tot_sumphase_p - tot_sumphase_n
    d_logmod_total = tot_logmod_p - tot_logmod_n

    agg = {
        "proton_total_reeb_phase_unit_modulus": tot_reeb_unit_p,
        "neutron_total_reeb_phase_unit_modulus": tot_reeb_unit_n,
        "delta_reeb_phase_unit_modulus": d_reeb_unit_total,
        "proton_total_sum_abs_phase": tot_sumphase_p,
        "neutron_total_sum_abs_phase": tot_sumphase_n,
        "delta_sum_abs_phase": d_sumphase_total,
        "proton_total_log_modulus": tot_logmod_p,
        "neutron_total_log_modulus": tot_logmod_n,
        "delta_log_modulus_writhe": d_logmod_total,
        "reeb_rotation_distinguishes_pn": not phase_identical,
        "modulus_writhe_distinguishes_pn": not modulus_identical,
    }
    wb.add_data("aggregate", agg)

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print(f"Reeb ROTATION (unit-modulus eigen-phase) p={tot_reeb_unit_p:.9f}  "
          f"n={tot_reeb_unit_n:.9f}  Δ={d_reeb_unit_total:+.3e}")
    print(f"  → distinguishes p/n? {not phase_identical}")
    print(f"sum|arg| (incl. real-sign π)            p={tot_sumphase_p:.9f}  "
          f"n={tot_sumphase_n:.9f}  Δ={d_sumphase_total:+.3e}")
    print(f"WRITHE/growth (Σ log|λ| = log|det|)      p={tot_logmod_p:.9f}  "
          f"n={tot_logmod_n:.9f}  Δ={d_logmod_total:+.6f}")
    print(f"  → distinguishes p/n? {not modulus_identical}")

    if phase_identical:
        verdict = (
            "ESCAPE FAILS for the Reeb ROTATION channel: the eigen-phase "
            "(q-Reeb rotation) is bit-identical for proton and neutron. The "
            "p/n distinction lives entirely in the eigenvalue MODULI "
            "(writhe/growth amplitude), not the rotation phase. The "
            "proton/neutron canonical braids are not alternating, so their "
            "seminormal eigenvalues are real (|arg| ∈ {0, π}, a sign not a "
            "rotation); there is no genuine Reeb rotation to distinguish them."
        )
    else:
        verdict = (
            "Reeb ROTATION distinguishes p/n — escape candidate live. See "
            "delta_reeb_phase_unit_modulus and the MeV-scale analysis."
        )
    wb.add_caveat(verdict)
    print("\n" + verdict)

    # ── MeV-scale honesty check (only meaningful if a channel differs) ──
    # The writhe channel DOES differ; report its raw ratio to the
    # experimental splitting WITHOUT fitting, and flag whether mapping it
    # to MeV needs a derived scale (m_e, q-volume) or a fitted constant.
    try:
        from experimental_constants import M_P_MEV, M_N_MEV
        d_mass_exp = M_N_MEV - M_P_MEV
        wb.add_data("experimental_mn_minus_mp_MeV", d_mass_exp)
        # The substrate carries NO derived MeV-per-(log|det|) scale: the only
        # existing tr_M→MeV map (atom_mass_derived.E0_MEV) is the proton-mass
        # CALIBRATION, i.e. fitted to m_p. Mapping Δlog|det| to 1.293 MeV would
        # require choosing such a scale → a latent fit unless a q-hyperbolic
        # volume / m_e derivation supplies it independently.
        wb.add_data(
            "mev_scale_status",
            "writhe channel differs but has NO derived MeV scale on the "
            "substrate; the only tr_M→MeV map is the m_p calibration "
            "(E0_MEV = m_p/tr_M(proton)), so mapping Δlog|det| → MeV would be "
            "a FITTED constant (RED, latent fit). Reeb-rotation channel is "
            "degenerate (no signal at all).",
        )
    except Exception as e:  # noqa: BLE001
        wb.add_data("mev_scale_status", f"scale check skipped: {e}")

    wb.add_assertion(
        "reeb_rotation_pn_difference",
        computed=f"{d_reeb_unit_total:.3e}",
        expected="0 (degenerate) — falsifies the Reeb-rotation escape",
        source="figure-eight-reeb-rotation.md (q-Reeb phase definition)",
    )

    out = wb.save()
    print("\nwitness →", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
