#!/usr/bin/env python3
"""
Recursive three-calibration on the mass tower.

Two flavours:

  FLAVOUR B (JET — user preference).  Split the tower functional into
  its three natural channels (descended product, single-generator
  Φ_q, pair-cross z²Φ_q) and assign one E_0 to each.  At each jet
  level n, the same three E_0's apply with an ℏ_q² damping per level:

    B(Z, N) = Σ_n ℏ_q^{2n} · [E₀^desc · Δdesc^(n)
                              + E₀^sgl  · Δsgl^(n)
                              + E₀^crs  · Δcrs^(n)]

  where Δ denotes "free minus bound" difference.  Fit 3 base E_0's
  from {B(D), B(T), B(³He)} and predict heavier atoms.

  FLAVOUR A (per-nucleon).  Decompose per-generator V̂ into sym/std/
  alt Wedderburn blocks (from additive_wedderburn_volumes).  Sum
  per-block defects with Markov-stab weighting z^k over nucleon
  positions:

    B(Z, N) = Σ_{k=1}^A z^{k-1} · Σ_{b} E₀^{b,(0)} · Δ^b_k

  Fit 3 base E_0^{b,(0)} from 3 atoms; predict the rest.

Both flavours use the SAME number of free parameters (3) and the
existing Wedderburn machinery.  If either reproduces the full atom
chain within AME (~0.1%), the recursive 3-calibration is complete.
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
from mass_endomorphism import (Phi_q, HA, qi0, z_mark,
                                  w_sym, w_std, w_alt)
from hecke_core import atom_per_generator_volumes

HBAR_Q = (q0 - 1.0) / q0
HBAR_Q_SQ = HBAR_Q * HBAR_Q


def _phi_safe(v, cap_frac=0.995):
    a = abs(v)
    if a >= q0 * cap_frac:
        return Phi_q(q0 * cap_frac)
    return Phi_q(a)


# ══ Flavour B: per-jet-level three-channel calibration ══

def tower_channels_from_V(vols: list) -> dict:
    """Split the tower mass functional into its three channels.

    vols: list of {std, sym, alt, full} per generator.
    Returns {desc, single, cross} using V̂_full.
    """
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


def atom_channel_defect(Z: int, N: int) -> dict:
    """Δ(desc, single, cross) = free − atom (level 0, flavour B)."""
    v_atom = atom_per_generator_volumes(Z, N, include_inter=True)
    v_free = atom_per_generator_volumes(Z, N, include_inter=False)
    c_atom = tower_channels_from_V(v_atom)
    c_free = tower_channels_from_V(v_free)
    return {
        "d_desc":   c_free["desc"]   - c_atom["desc"],
        "d_single": c_free["single"] - c_atom["single"],
        "d_cross":  c_free["cross"]  - c_atom["cross"],
    }


def flavour_B_predict(Z: int, N: int, E0: np.ndarray,
                         n_levels: int = 4) -> float:
    """Binding prediction via Flavour B recursion.

    E0 = [E₀^desc, E₀^sgl, E₀^crs].  Tower summed over jet levels 0..n-1
    with ℏ_q² damping per level.
    """
    d = atom_channel_defect(Z, N)
    delta_vec = np.array([d["d_desc"], d["d_single"], d["d_cross"]])
    total = 0.0
    for n in range(n_levels):
        total += (HBAR_Q_SQ ** n) * float(E0 @ delta_vec)
    return total


# ══ Flavour A: per-nucleon recursion ══

def per_nucleon_block_defects(Z: int, N: int) -> dict:
    """Per-nucleon per-block defects.

    Split the atom's per-generator Wedderburn blocks into A nucleon
    groups (3 gens per nucleon in atom case; 2 gens per nucleon in
    free case).  Per nucleon k: sum |sp_i - sp_i_free|, etc., across
    that nucleon's generators.
    """
    A = Z + N
    v_atom = atom_per_generator_volumes(Z, N, include_inter=True)
    v_free = atom_per_generator_volumes(Z, N, include_inter=False)

    # Map generators to nucleons.  Atom: 3A-1 gens; nucleon k has gens
    # [3k, 3k+1, 3k+2] when k < A, gen 3A-1 is shared.  Simplification:
    # assign gens [3k, 3k+1] to nucleon k (leaving inter-nucleon gens
    # separately).
    #
    # Free: 2A gens, each nucleon has 2 gens (k: [2k, 2k+1]).
    per_nuc_atom = [[] for _ in range(A)]
    per_nuc_free = [[] for _ in range(A)]
    for i, v in enumerate(v_atom):
        k = min(i // 3, A - 1)
        per_nuc_atom[k].append(v)
    for i, v in enumerate(v_free):
        k = min(i // 2, A - 1)
        per_nuc_free[k].append(v)

    defects = []
    for k in range(A):
        def _block_sum(vols, block):
            return sum(abs(v.get(block, 0.0)) for v in vols)
        d_sym = (_block_sum(per_nuc_free[k], "sym")
                  - _block_sum(per_nuc_atom[k], "sym"))
        d_std = (_block_sum(per_nuc_free[k], "std")
                  - _block_sum(per_nuc_atom[k], "std"))
        d_alt = (_block_sum(per_nuc_free[k], "alt")
                  - _block_sum(per_nuc_atom[k], "alt"))
        defects.append({"k": k, "d_sym": d_sym, "d_std": d_std,
                          "d_alt": d_alt})
    return defects


def flavour_A_predict(Z: int, N: int, E0: np.ndarray) -> float:
    """Binding prediction via Flavour A recursion.

    E0 = [E₀^sym,(0), E₀^std,(0), E₀^alt,(0)].  Per-nucleon defects
    weighted by z^k (Markov-stab recursion).
    """
    defs = per_nucleon_block_defects(Z, N)
    total = 0.0
    for d in defs:
        weight = z_mark ** d["k"]
        delta = np.array([d["d_sym"], d["d_std"], d["d_alt"]])
        total += weight * float(E0 @ delta)
    return total


# ══ Calibration fit ══

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


def build_design_flavour_B(atoms: list, n_levels: int = 4) -> tuple:
    """A matrix (rows=atoms, cols=[desc, single, cross]) and b vector."""
    A_mat = np.zeros((len(atoms), 3))
    b_vec = np.zeros(len(atoms))
    for i, (name, Z, N, B_AME) in enumerate(atoms):
        d = atom_channel_defect(Z, N)
        # Sum of ℏ_q^{2n} for n=0..n_levels-1 (geometric factor)
        geom = sum(HBAR_Q_SQ ** n for n in range(n_levels))
        A_mat[i] = geom * np.array([d["d_desc"], d["d_single"],
                                       d["d_cross"]])
        b_vec[i] = B_AME
    return A_mat, b_vec


def build_design_flavour_A(atoms: list) -> tuple:
    """A matrix (rows=atoms, cols=[sym, std, alt]) and b vector."""
    A_mat = np.zeros((len(atoms), 3))
    b_vec = np.zeros(len(atoms))
    for i, (name, Z, N, B_AME) in enumerate(atoms):
        defs = per_nucleon_block_defects(Z, N)
        coefs = np.zeros(3)
        for d in defs:
            w = z_mark ** d["k"]
            coefs += w * np.array([d["d_sym"], d["d_std"], d["d_alt"]])
        A_mat[i] = coefs
        b_vec[i] = B_AME
    return A_mat, b_vec


def fit_and_predict(atoms_train, atoms_test, flavour: str,
                      n_levels: int = 4) -> dict:
    if flavour == "B":
        A_tr, b_tr = build_design_flavour_B(atoms_train, n_levels)
        A_te, b_te = build_design_flavour_B(atoms_test, n_levels)
    elif flavour == "A":
        A_tr, b_tr = build_design_flavour_A(atoms_train)
        A_te, b_te = build_design_flavour_A(atoms_test)
    else:
        raise ValueError(flavour)
    E0, *_ = np.linalg.lstsq(A_tr, b_tr, rcond=None)
    pred_tr = A_tr @ E0
    pred_te = A_te @ E0
    return {
        "flavour": flavour,
        "E0": E0.tolist(),
        "train_names": [a[0] for a in atoms_train],
        "train_obs": b_tr.tolist(),
        "train_pred": pred_tr.tolist(),
        "train_resid_pct":
            [(p - o) / o * 100 if o else float("nan")
              for p, o in zip(pred_tr, b_tr)],
        "test_names": [a[0] for a in atoms_test],
        "test_obs": b_te.tolist(),
        "test_pred": pred_te.tolist(),
        "test_resid_pct":
            [(p - o) / o * 100 if o else float("nan")
              for p, o in zip(pred_te, b_te)],
        "design_train": A_tr.tolist(),
        "design_test": A_te.tolist(),
    }


if __name__ == "__main__":
    print("=" * 100)
    print("RECURSIVE THREE-CALIBRATION")
    print(f"q₀ = {q0:.6f}, ℏ_q = {HBAR_Q:.4f}, "
          f"ℏ_q² = {HBAR_Q_SQ:.6f}, z = {z_mark:.4f}")
    print("=" * 100)

    TRAIN = ATOMS[:3]     # D, T, 3He
    TEST = ATOMS[3:]      # 4He, 6Li, 9Be, 12C, 16O

    for flavour, name in [("B", "JET tower (preferred)"),
                            ("A", "PER-NUCLEON recursion")]:
        print(f"\n{'=' * 80}")
        print(f"FLAVOUR {flavour}: {name}")
        print("=" * 80)
        try:
            result = fit_and_predict(TRAIN, TEST, flavour)
        except Exception as e:
            print(f"  ERR: {type(e).__name__}: {str(e)[:100]}")
            continue

        print(f"\n  Fitted E_0 (flavour {flavour}):")
        labels = (["E₀^desc", "E₀^single", "E₀^cross"] if flavour == "B"
                   else ["E₀^sym", "E₀^std", "E₀^alt"])
        for lab, val in zip(labels, result["E0"]):
            print(f"    {lab:>10} = {val:+.6e} MeV/cat")

        print(f"\n  TRAIN (exact fit, 3 obs / 3 unk):")
        print(f"    {'atom':>6} {'B_AME':>10} {'B_pred':>10} {'resid%':>10}")
        for n, o, p, r in zip(result["train_names"],
                                result["train_obs"],
                                result["train_pred"],
                                result["train_resid_pct"]):
            print(f"    {n:>6} {o:>10.4f} {p:>10.4f} {r:>+9.4f}%")

        print(f"\n  TEST (predictions on heavy atoms):")
        print(f"    {'atom':>6} {'B_AME':>10} {'B_pred':>10} {'resid%':>10}")
        test_errs = []
        for n, o, p, r in zip(result["test_names"],
                                result["test_obs"],
                                result["test_pred"],
                                result["test_resid_pct"]):
            print(f"    {n:>6} {o:>10.4f} {p:>10.4f} {r:>+9.4f}%")
            test_errs.append(abs(r))
        if test_errs:
            print(f"\n  Mean |test resid|% = {sum(test_errs)/len(test_errs):.4f}%")
            print(f"  Max  |test resid|% = {max(test_errs):.4f}%")

    # Witness: assemble both flavours
    witness = {
        "computation": "recursive-three-calibration",
        "description": (
            "Recursive three-calibration of the mass tower.  Flavour B "
            "(JET): fits three E_0's on the (desc, single, cross) "
            "channels of the per-level tower functional, with ℏ_q² "
            "damping per jet level.  Flavour A (per-nucleon): fits "
            "three E_0's on the sym/std/alt Wedderburn blocks per "
            "nucleon with z^k Markov-stab recursion over nucleon "
            "positions.  Both use only 3 free parameters fitted from "
            "{D, T, ³He}; predictions on {⁴He, ⁶Li, ⁹Be, ¹²C, ¹⁶O} "
            "test whether the 3-scale model is complete."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q0": q0, "HA": HA,
            "hbar_q": HBAR_Q, "hbar_q_sq": HBAR_Q_SQ,
            "z_markov": z_mark,
            "atoms_train": [list(a) for a in TRAIN],
            "atoms_test":  [list(a) for a in TEST],
        },
        "flavour_B_jet": fit_and_predict(TRAIN, TEST, "B"),
        "flavour_A_nucleon": fit_and_predict(TRAIN, TEST, "A"),
    }
    out = Path(__file__).parent / "recursive-three-calibration.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
