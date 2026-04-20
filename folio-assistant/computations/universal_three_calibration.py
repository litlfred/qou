#!/usr/bin/env python3
"""
Universal three-calibration: fit E_0's from PARTICLE masses only,
predict ALL isotope bindings with NO per-isotope tuning.

This is the proper rep-theory-clean probe.  The three E_0's are
universal constants, set once from three fundamental particle
observables {m_e, m_p, m_n} and applied to every isotope's
Flavour-B (desc, single, cross) channel decomposition.

    m(W) = E₀^desc · desc(W) + E₀^sgl · single(W) + E₀^crs · cross(W)

for any braid W.  Apply to
  • electron (σ₀³, 2 strands, 1 gen)   → should give m_e = 0.511 MeV
  • proton  (11-factor, 3 strands)     → should give m_p = 938.272
  • neutron (11-factor, udd variant)   → should give m_n = 939.565

These three fix E_0^desc, E_0^sgl, E_0^crs.  Then for each atom we
compute two braid-level masses under the same universal calibration:

    m_atom_pred  = universal E₀ · channels(atom_braid, include_inter=True)
    m_free_pred  = universal E₀ · channels(atom_braid, include_inter=False)

and define binding as the framework-consistent difference:

    B(Z, N) = m_free_pred − m_atom_pred

No per-isotope free parameters.  Residuals are genuine framework
errors, not artefacts of fitting.

(Earlier drafts used Σ m_nucleon as the free baseline; see the
commit history.  Both conventions fail catastrophically — atoms
predict anti-bound under the universal calibration — so the choice
of baseline does not affect the qualitative conclusion.)
"""
from __future__ import annotations

import sys
import json
import math
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0
from mass_endomorphism import (additive_wedderburn_volumes,
                                  Phi_q, HA, qi0, z_mark)
from hecke_core import atom_per_generator_volumes

# CODATA
M_E = 0.51099895
M_P = 938.272
M_N = 939.565


def _phi_safe(v, cap_frac=0.995):
    a = abs(v)
    if a >= q0 * cap_frac:
        return Phi_q(q0 * cap_frac)
    return Phi_q(a)


def channels_from_vols(vols: list) -> dict:
    """Flavour-B channels (desc, single, cross) from per-gen V̂ list."""
    n = len(vols)
    if n == 0:
        return {"desc": 0.0, "single": 0.0, "cross": 0.0}
    V = [v["full"] for v in vols]
    desc = 1.0
    for v in V:
        desc *= v
    desc = abs(desc)
    single = sum(_phi_safe(v) for v in V)
    cross = 0.0
    for i in range(n - 1):
        cross += z_mark ** 2 * _phi_safe(V[i] * V[i + 1])
    return {"desc": desc, "single": single, "cross": cross}


def electron_braid() -> dict:
    """e⁻ = σ₀³ on 2 strands."""
    return {0: [(1.0, 0.0)] * 3}


def proton_braid() -> dict:
    return {
        0: ([(1.0, 0.0)] * 3 + [(1.0, 0.0)]
            + [(1.0, -HA / 2)] + [(1.0, 0.0)] * 2),
        1: [(1.0, -HA)] * 3 + [(1.0, -HA / 2)],
    }


def neutron_braid() -> dict:
    return {
        0: ([(1.0, 0.0)] * 3 + [(1.0, -HA)]
            + [(1.0, -HA / 2)] + [(1.0, 0.0)] * 2),
        1: [(1.0, -HA)] * 3 + [(1.0, -HA / 2)],
    }


def particle_channels(label: str) -> dict:
    if label == "electron":
        vols = additive_wedderburn_volumes(2, electron_braid())
    elif label == "proton":
        vols = additive_wedderburn_volumes(3, proton_braid())
    elif label == "neutron":
        vols = additive_wedderburn_volumes(3, neutron_braid())
    else:
        raise ValueError(label)
    return channels_from_vols(vols)


def atom_channels(Z: int, N: int, include_inter: bool) -> dict:
    vols = atom_per_generator_volumes(Z, N, include_inter=include_inter)
    return channels_from_vols(vols)


if __name__ == "__main__":
    print("=" * 100)
    print("UNIVERSAL THREE-CALIBRATION")
    print("  fit {E_0^desc, E_0^sgl, E_0^crs} from {m_e, m_p, m_n}")
    print("  predict all isotopes with NO per-isotope tuning")
    print("=" * 100)

    # ── Set up 3×3 system from particle masses ───────
    labels = ["electron", "proton", "neutron"]
    targets = [M_E, M_P, M_N]
    A = np.zeros((3, 3))
    for i, lab in enumerate(labels):
        c = particle_channels(lab)
        A[i] = [c["desc"], c["single"], c["cross"]]
    b = np.array(targets)

    print(f"\n  {'particle':>10} {'desc':>12} {'single':>16} "
          f"{'cross':>14} {'obs_MeV':>10}")
    for i, lab in enumerate(labels):
        print(f"  {lab:>10} {A[i,0]:>12.6f} {A[i,1]:>16.4f} "
              f"{A[i,2]:>14.4f} {b[i]:>10.4f}")

    # LSQ solve — more numerically robust than np.linalg.solve when
    # the design matrix is nearly rank-deficient (e.g. proton and
    # neutron channels are structurally very similar).
    E0, *_ = np.linalg.lstsq(A, b, rcond=None)
    print(f"\n  Universal calibration (from particle masses):")
    print(f"    E_0^desc   = {E0[0]:+.6e} MeV/cat")
    print(f"    E_0^sgl    = {E0[1]:+.6e} MeV/cat")
    print(f"    E_0^crs    = {E0[2]:+.6e} MeV/cat")

    # Self-check: should reproduce m_e, m_p, m_n exactly
    for i, lab in enumerate(labels):
        pred = A[i] @ E0
        print(f"    check {lab:>10}: pred={pred:.6f} MeV  (obs {b[i]})")

    # ── Predict isotope bindings ─────────────────
    # Atom braid mass via same three E_0's
    # Then B(Z, N) = m_atom_braid − Z m_p − N m_n
    # (The free baseline is sum of isolated nucleon masses in this
    #  formula — not the 'include_inter=False' V̂.)
    print(f"\n  Isotope binding predictions (no further fitting):")
    print(f"    {'atom':>6} {'Z':>2} {'N':>2} {'A':>2} {'B_AME':>9} "
          f"{'m_free':>12} {'m_atom':>12} "
          f"{'B_pred':>9} {'err_%':>10}")

    ATOMS = [
        ("D",    1, 1,  2.22452),
        ("T",    1, 2,  8.481821),
        ("3He",  2, 1,  7.71804),
        ("4He",  2, 2, 28.295674),
        ("6Li",  3, 3, 32.0),
        ("9Be",  4, 5, 58.165),
        ("12C",  6, 6, 92.161728),
        ("16O",  8, 8, 127.619),
    ]
    print(f"\n  Binding via framework-consistent free baseline:")
    print(f"  (baseline = free atom braid with include_inter=False, "
          f"same universal calibration)")
    results = []
    for name, Z, N, B_AME in ATOMS:
        c_atom = atom_channels(Z, N, include_inter=True)
        c_free = atom_channels(Z, N, include_inter=False)
        m_atom_pred = (E0[0] * c_atom["desc"]
                        + E0[1] * c_atom["single"]
                        + E0[2] * c_atom["cross"])
        m_free_pred = (E0[0] * c_free["desc"]
                        + E0[1] * c_free["single"]
                        + E0[2] * c_free["cross"])
        B_pred = m_free_pred - m_atom_pred
        # Binding energy sign convention: B > 0 means bound; atom mass
        # < free-nucleon mass, so B = m_free - m_atom.
        err = (B_pred - B_AME) / B_AME * 100 if B_AME else float("nan")
        A_ = Z + N
        print(f"    {name:>6} {Z:>2} {N:>2} {A_:>2} {B_AME:>9.4f} "
              f"{m_free_pred:>12.4f} {m_atom_pred:>12.4f} "
              f"{B_pred:>+9.4f} "
              f"{err:>+9.4f}%")
        results.append({
            "atom": name, "Z": Z, "N": N, "A": A_,
            "B_AME_MeV": B_AME,
            "desc_atom": c_atom["desc"],
            "single_atom": c_atom["single"],
            "cross_atom": c_atom["cross"],
            "desc_free": c_free["desc"],
            "single_free": c_free["single"],
            "cross_free": c_free["cross"],
            "m_atom_pred_MeV": m_atom_pred,
            "m_free_pred_MeV": m_free_pred,
            "B_pred_MeV": B_pred,
            "err_pct": err,
        })

    witness = {
        "computation": "universal-three-calibration",
        "description": (
            "Universal rep-theory three-calibration.  Fit E_0's from "
            "three PARTICLE masses {m_e, m_p, m_n} only — NO isotope "
            "tuning — then apply unchanged to predict all isotope "
            "bindings.  Residuals are genuine framework errors, not "
            "fit artefacts.  Binding convention: B = Z·m_p + N·m_n − "
            "m_atom_pred where m_atom_pred comes from the atom braid's "
            "(desc, single, cross) channels under the universal "
            "calibration."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q0": q0, "HA": HA,
            "M_E_MeV": M_E, "M_P_MeV": M_P, "M_N_MeV": M_N,
            "E0_desc": float(E0[0]),
            "E0_single": float(E0[1]),
            "E0_cross": float(E0[2]),
        },
        "calibration_design": A.tolist(),
        "calibration_targets": b.tolist(),
        "isotope_predictions": results,
    }
    out = Path(__file__).parent / "universal-three-calibration.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
