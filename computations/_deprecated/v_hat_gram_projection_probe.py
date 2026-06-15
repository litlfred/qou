#!/usr/bin/env python3
"""
V-hat-within-level Candidate #2: Gram-projected atom NF.

The 6×6 H_3(q) Gram matrix G has a negative eigenvalue at q₀ (−0.74).
Any H_3 NF vector x with the negative-eigenspace component non-zero
violates the quadratic Frobenius positivity xᵀG x ≥ 0.

This module computes the 6D atom NF for D / T / 3He (by concatenating
the per-nucleon-generator Hecke products in the H_3 quotient), checks
the quadratic form on each, and projects onto the G-positive
eigenspace G+ := Σ_{λ_i > 0} v_i v_iᵀ.  It then compares the
canonical Markov trace |tr_M(x)| against |tr_M(P+ x)| and reports the
delta.  If the projection materially changes |tr_M|, then
Frobenius-positivity enforcement at the atom-NF level is a structural
lever; if it barely moves the trace, the scalar-over-PSD issue is
not rate-limiting for this pipeline.

Focused probe — atom NF only (not per-generator); single-shot result.
"""
from __future__ import annotations

import sys
import json
import time
import importlib.util
import os
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0

# Load confinement-lp for the canonical 6×6 Gram + NF primitives.
_CONF = Path(__file__).parent / "confinement-lp.py"
_spec = importlib.util.spec_from_file_location("_conf", _CONF)
_mod = importlib.util.module_from_spec(_spec)
_old = os.dup(1); _null = os.open(os.devnull, os.O_WRONLY); os.dup2(_null, 1)
try:
    _spec.loader.exec_module(_mod)
finally:
    os.dup2(_old, 1); os.close(_null); os.close(_old)

G = np.asarray(_mod.G)
TR_M = np.asarray(_mod.TR_M_BASIS)
NF_BASIS = _mod.NF_BASIS
hecke_mul = _mod.hecke_mul
reduce_nf = _mod.reduce_nf
to_vec = _mod.to_vec

from hecke_core import atom_gen_chains, _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1
from q_parameter import HA as h


# ── Gram eigendecomposition + positive projector ────────────

eig_vals, eig_vecs = np.linalg.eigh(G)  # symmetric
# G+ = Σ_{λ > 0} v v^T (positive eigenspace projector)
pos_mask = eig_vals > 1e-12
P_pos = eig_vecs[:, pos_mask] @ eig_vecs[:, pos_mask].T


def atom_nf_6d(Z: int, N: int) -> list[float]:
    """Build the 6D H_3 NF of the atom braid word by successive
    multiplication of per-nucleon generator chains via hecke_mul.

    The atom braid word is (B₃ + uud pairs + gluon)_k * (B₃ + udd
    pairs + gluon)_k chained over all Z + N nucleons.  We use the
    g0/g1 chains from atom_gen_chains, applied sequentially in H_3
    (note: this collapses the 3A-strand braid to a single H_3
    product, which is the standard approximation used in the scalar
    pipeline).
    """
    # Start with identity.
    nf_dict = {(): 1.0}
    g0_chain, g1_chain = atom_gen_chains(Z, N)
    # Apply g0 chain: multiply by (c σ_0 + d) each step.
    for (c, d) in g0_chain:
        factor = {(0,): float(c), (): float(d)}
        nf_dict = reduce_nf(hecke_mul(nf_dict, factor))
    # Apply g1 chain: multiply by (c σ_1 + d) each step.
    for (c, d) in g1_chain:
        factor = {(1,): float(c), (): float(d)}
        nf_dict = reduce_nf(hecke_mul(nf_dict, factor))
    return list(map(float, to_vec(nf_dict)))


def report(Z: int, N: int, name: str) -> dict:
    x = np.asarray(atom_nf_6d(Z, N))
    x_proj = P_pos @ x
    xTGx = float(x @ G @ x)
    xprojTGxproj = float(x_proj @ G @ x_proj)
    trM = float(x @ TR_M)
    trM_proj = float(x_proj @ TR_M)
    pos_frac = float(np.linalg.norm(x_proj) / np.linalg.norm(x)) \
        if np.linalg.norm(x) > 0 else 0.0
    return {
        "atom": name, "Z": Z, "N": N,
        "x": x.tolist(), "x_proj": x_proj.tolist(),
        "xTGx": xTGx, "xprojTGxproj": xprojTGxproj,
        "trM": trM, "trM_proj": trM_proj,
        "delta_trM": trM_proj - trM,
        "pos_subspace_norm_frac": pos_frac,
    }


if __name__ == "__main__":
    print("=" * 100)
    print("CANDIDATE #2: Gram-projected atom NF probe")
    print(f"q0 = {Q0}")
    print("=" * 100)
    print(f"\nGram eigenvalues: {eig_vals}")
    print(f"  positive eigenspace dim = {int(pos_mask.sum())} / 6")
    print()

    ATOMS = [
        ("D",   1, 1,  2.22452),
        ("T",   1, 2,  8.481821),
        ("3He", 2, 1,  7.71804),
    ]

    print(f"  {'Atom':>5} {'xTGx (pre)':>14} {'xTGx (post)':>14} "
          f"{'tr_M (pre)':>14} {'tr_M (post)':>14} "
          f"{'Δ tr_M':>12} {'|x+|/|x|':>10}")
    print("  " + "-" * 98)

    results = []
    for name, Z, N, B_AME in ATOMS:
        r = report(Z, N, name)
        r["B_AME_MeV"] = B_AME
        mag = "pre-Frob-valid" if r["xTGx"] >= -1e-9 else "pre-INVALID"
        print(f"  {name:>5} {r['xTGx']:>+14.6e} {r['xprojTGxproj']:>+14.6e} "
              f"{r['trM']:>+14.6e} {r['trM_proj']:>+14.6e} "
              f"{r['delta_trM']:>+12.4e} {r['pos_subspace_norm_frac']:>10.4f}  [{mag}]")
        results.append(r)

    witness = {
        "computation": "v-hat-gram-projection-probe",
        "description": (
            "V-hat-within-level Candidate #2: project atom NF onto the "
            "positive eigenspace of G (Frobenius-positive cone) and "
            "report how much the canonical Markov trace moves.  If the "
            "projection changes tr_M materially, Frobenius-positivity "
            "enforcement at the atom-NF level is a structural lever; "
            "otherwise the scalar-over-PSD mismatch is not rate-"
            "limiting for the unified_lift pipeline."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q0": Q0,
            "gram_eigenvalues": eig_vals.tolist(),
            "positive_subspace_dim": int(pos_mask.sum()),
        },
        "results": results,
    }
    out = Path(__file__).parent / "v-hat-gram-projection-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
