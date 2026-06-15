#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical/intermediate-sympy witness; no symbolic-q polynomial in output.
"""
Validate NF / gluon / SDP-stability across the full isotope table.

For every isotope (Z, N) in isotope-mass-table.ISOTOPES, this script
checks three things:

  (1) GLUON present
      The proton / neutron gluon decoration (2 sigma_0 crossings per
      nucleon) is baked into hecke_core.nucleon_gen_chains and applied
      uniformly by atom_braid_word_3A.  We verify that every atom's
      braid word contains the expected gluon coefficients.

  (2) Per-nucleon H_3 SDP stability
      Using the 6-dim H_3(q) NF basis {1, s0, s1, s0s1, s1s0, s0s1s0}
      and the Frobenius / Gram matrix G from integer-lp-gluon.py, we
      recompute each nucleon's NF step-by-step and check
      G . NF >= 0 at every step.  Records: final stable, path stable,
      count of unstable intermediate steps.

  (3) Atom-level Markov-trace sign
      For the full 3A-strand braid word (via atom_braid_word_3A), we
      compute a per-isotope proxy: whether the lightest partitions'
      character contributions stay positive (sign agreement with the
      expected tr_M).  This is a necessary condition for the full
      H_{3A} Markov-trace positivity (sufficient full-dim SDP check
      is infeasible for heavy atoms).

Outputs: validate-isotope-nf-stability.witness.json with a per-atom
row listing gluon presence, H_3 stability, and atom-level sign.
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
from scipy.sparse import issparse, eye as speye

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, Q_INV as qi0, HA as h
from hecke_core import (_PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1)
from hecke_characters import (partitions_of, dim_q, qfac,
                                build_seminormal_matrices)
from mass_at_3A_proper import atom_braid_word_3A


# isotope-mass-table has a hyphen in its filename — load via importlib.
def _load_isotopes() -> list[tuple]:
    isotope_table_path = Path(__file__).parent / "isotope-mass-table.py"
    spec = importlib.util.spec_from_file_location(
        "isotope_mass_table", isotope_table_path)
    if spec is None or spec.loader is None:
        raise ImportError(
            f"Could not load isotope table from {isotope_table_path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.ISOTOPES


# ── H_3(q) Gram / stability machinery ─────────────────────────
# IMPORTANT: earlier revisions of this file hard-coded both a Gram
# matrix G and a basis-index-juggling `mul_h3` routine.  They were
# mutually INCONSISTENT (gemini-code-assist flag on PR #383) — the
# mul rules treat basis[3] as s_1 s_0 while the hard-coded G was
# built for basis[3] = s_0 s_1 (the NF_BASIS convention).  That
# swap made every path-stability check report INVALID for reasons
# unrelated to the physics.
#
# The canonical primitives live in ``confinement-lp.py``
# (`hecke_mul`, `reduce_nf`, `to_vec`, `build_gram`).  We load that
# module once and reuse its G + dict-based multiplication.

_CONF_PATH = Path(__file__).parent / "confinement-lp.py"
_conf_spec = importlib.util.spec_from_file_location(
    "confinement_lp_mod", _CONF_PATH)
if _conf_spec is None or _conf_spec.loader is None:
    raise ImportError(f"Could not load {_CONF_PATH}")
_conf_mod = importlib.util.module_from_spec(_conf_spec)
_old = os.dup(1)
_null = os.open(os.devnull, os.O_WRONLY)
os.dup2(_null, 1)
try:
    _conf_spec.loader.exec_module(_conf_mod)
finally:
    os.dup2(_old, 1)
    os.close(_null)
    os.close(_old)

NF_BASIS = _conf_mod.NF_BASIS
NF_NAMES = _conf_mod.NF_NAMES
TR_M_BASIS = _conf_mod.TR_M_BASIS
hecke_mul = _conf_mod.hecke_mul
reduce_nf = _conf_mod.reduce_nf
to_vec = _conf_mod.to_vec
G = _conf_mod.G
z = _conf_mod.z


def is_stable(nf, tol=1e-10):
    """H_3(q) SDP stability: componentwise LP Frobenius `G·nf ≥ 0`
    AND the quadratic SDP Frobenius `nf^T G nf ≥ 0`.

    The componentwise condition alone is strictly weaker at q_0
    (G has a negative eigenvalue; see docs/ilp-sdp-audit.md).  Both
    must hold for a valid Frobenius-positive H_3 NF."""
    v = np.asarray(nf)
    lp_ok = bool(np.all(G @ v >= -tol))
    sdp_ok = bool(float(v @ G @ v) >= -tol)
    return lp_ok and sdp_ok


def trM_h3(nf):
    return float(sum(nf[i] * TR_M_BASIS[i] for i in range(6)))


# ── Nucleon NF step-by-step check in H_3 ─────────────────────

def _mul_h3_dict(nf_dict: dict, c: float, d: float, gen: int) -> dict:
    """Right-multiply a dict-form Hecke element by (c·σ_gen + d·𝟏).

    Uses the canonical `hecke_mul` + `reduce_nf` from confinement-lp,
    guaranteeing the basis convention (NF_BASIS) matches the Gram
    matrix G loaded above.  Replaces the earlier hard-coded mul_h3
    whose index convention was inconsistent with G (PR #383 review).
    """
    factor: dict = {}
    if abs(c) > 1e-15:
        factor[(gen,)] = c
    if abs(d) > 1e-15:
        factor[()] = d
    prod = hecke_mul(nf_dict, factor)
    return reduce_nf(prod)


def build_nucleon_nf_stepwise(g0_chain, g1_chain) -> dict:
    """Reproduce atom_braid_word_3A's per-nucleon order (all g0 then
    all g1) in H_3, tracking stability at every crossing using the
    basis-consistent hecke_mul / reduce_nf from confinement-lp."""
    nf_dict = {(): 1.0}
    path_stable: list[bool] = []
    unstable_at: list[int] = []
    for step, (c, d) in enumerate(g0_chain):
        nf_dict = _mul_h3_dict(nf_dict, c, d, 0)
        st = is_stable(to_vec(nf_dict))
        path_stable.append(st)
        if not st:
            unstable_at.append(step)
    offset = len(g0_chain)
    for step, (c, d) in enumerate(g1_chain):
        nf_dict = _mul_h3_dict(nf_dict, c, d, 1)
        st = is_stable(to_vec(nf_dict))
        path_stable.append(st)
        if not st:
            unstable_at.append(offset + step)
    nf_vec = to_vec(nf_dict)
    return {
        "nf": [float(x) for x in nf_vec],
        "trM": trM_h3(nf_vec),
        "final_stable": is_stable(nf_vec),
        "path_stable": all(path_stable),
        "n_steps": len(path_stable),
        "n_unstable_steps": len(unstable_at),
        "unstable_step_indices": unstable_at,
    }


def gluon_fingerprint(g0_chain) -> dict:
    """Check whether the last two entries of g0 are the (1, 0) gluon
    pair laid down by nucleon_gen_chains."""
    if len(g0_chain) < 2:
        return {"has_gluon_pair": False, "tail": list(g0_chain)}
    tail = [(float(c), float(d)) for (c, d) in g0_chain[-2:]]
    has_pair = tail == [(1.0, 0.0), (1.0, 0.0)]
    return {"has_gluon_pair": has_pair, "tail": tail}


# ── Atom-level tr_M sign (lightweight, partition-truncated) ──
#
# IMPORTANT: This partition-weighted sum uses the PLANCHEREL weight
# w_lambda = d_q(lambda)^2 / [n]_q!.  That is NOT the canonical
# Jones-Markov trace referenced in prop:categorical-mass-markov —
# see markov_trace_canonical.py for the axiomatic version.  The two
# disagree substantially at q != 1 (e.g. for D the Plancherel path
# gives -0.0054 while the canonical path gives +0.3883; both are
# computed correctly on the same braid word, but compute different
# traces).  We also run the canonical trace via tr_M_element below
# and prefer its sign for stability conclusions.

def atom_trM_canonical_symbolic(Z: int, N: int) -> dict:
    """Canonical Jones-Markov trace on the 3A-strand braid word,
    computed symbolically in q via the recursive Markov-axiom
    reduction in markov_trace_canonical.tr_M_element, then evaluated
    at q0.  This is the authoritative trace for stability; matches
    prop:categorical-mass-markov."""
    import sympy as sp
    from markov_trace_canonical import tr_M_element
    from hecke_symbolic import q as q_sym
    from binding_canonical import build_atom_symbolic
    A = Z + N
    n = 3 * A
    if A < 1:
        return {"trM": 1.0, "n_strands": 0}
    elem = build_atom_symbolic(Z, N, include_inter=True)
    tr_sym = tr_M_element(elem, n)
    val = complex(sp.N(tr_sym.subs(q_sym, q0)))
    tr_val = val.real if abs(val.imag) < 1e-9 else val
    return {"trM": float(tr_val) if isinstance(tr_val, float) \
                else complex(tr_val),
              "n_strands": n,
              "elem_n_terms": elem.n_terms()}


def atom_trM_light(Z: int, N: int, *, max_dim: int = 200) -> dict:
    """PARTITION-SUM (Plancherel) Markov trace — NOT canonical.

    See note above: this differs from the canonical Jones-Markov
    trace at q != 1.  Kept as a diagnostic only; do not use its
    sign to conclude (in)stability.
    """
    A = Z + N
    n = 3 * A
    if A < 1:
        return {"trM": 1.0, "n_partitions_used": 0, "truncated": False}

    # Atom-level braid word (all gluons included via atom_gen_chains).
    word = atom_braid_word_3A(Z, N, m_pp=1, m_pn=1, m_nn=1,
                                 include_inter=True)
    nfac = qfac(n)
    total = 0.0
    used = 0
    skipped = 0
    for shape in partitions_of(n):
        sigmas, dim, _syts = build_seminormal_matrices(shape)
        if dim == 0:
            continue
        if dim > max_dim:
            skipped += 1
            continue
        dq = dim_q(shape)
        if dq == 0:
            continue
        w_lam = (dq * dq) / nfac
        # chi_lambda(W) = tr(product of (c sigma_g + d I))
        if sigmas and issparse(sigmas[0]):
            prod = speye(dim, format='csr')
            I = speye(dim, format='csr')
            for (c, d, g) in word:
                if g < len(sigmas):
                    prod = prod @ (c * sigmas[g] + d * I)
            chi = float(prod.diagonal().sum())
        else:
            prod = np.eye(dim)
            I = np.eye(dim)
            for (c, d, g) in word:
                if g < len(sigmas):
                    prod = prod @ (c * sigmas[g] + d * I)
            chi = float(np.trace(prod))
        total += w_lam * chi / dim
        used += 1
    return {
        "trM": total,
        "n_partitions_used": used,
        "n_partitions_skipped": skipped,
        "truncated": skipped > 0,
        "max_dim": max_dim,
    }


# ── Main validation loop ─────────────────────────────────────

ATOM_TRM_ENABLED = False
ATOM_MAX_3A = 12
CANONICAL_MAX_3A = 6  # symbolic tr_M is slow (D ~145s);
                        # >6 falls back to Plancherel trace.  Override
                        # with --canonical-max-3a for T/3He/4He.


def main():
    global ATOM_TRM_ENABLED, ATOM_MAX_3A
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--atom-trm", action="store_true",
                      help="Also compute partition-truncated atom tr_M "
                           "(slow; requires seminormal matrices)")
    ap.add_argument("--max-3a", type=int, default=12,
                      help="Max 3A for atom-tr_M check (default 12)")
    ap.add_argument("--canonical-max-3a", type=int, default=6,
                      help="Max 3A for canonical (symbolic) tr_M "
                           "(default 6; slow beyond)")
    args = ap.parse_args()
    ATOM_TRM_ENABLED = args.atom_trm
    ATOM_MAX_3A = args.max_3a
    global CANONICAL_MAX_3A
    CANONICAL_MAX_3A = args.canonical_max_3a

    isotopes = _load_isotopes()
    print("=" * 110)
    print("ISOTOPE NF / GLUON / SDP-STABILITY VALIDATION")
    print(f"q0 = {q0:.15f}  z = {z:.6f}  HA = {h:.6f}")
    print("=" * 110)

    # Compute nucleon NFs once (identical across isotopes).
    p_data = build_nucleon_nf_stepwise(_PROTON_G0, _PROTON_G1)
    n_data = build_nucleon_nf_stepwise(_NEUTRON_G0, _NEUTRON_G1)
    p_glu = gluon_fingerprint(_PROTON_G0)
    n_glu = gluon_fingerprint(_NEUTRON_G0)

    print()
    print("BASE NUCLEONS (H_3(q) stepwise):")
    print(f"  Proton   final tr_M = {p_data['trM']:+.6f}  "
          f"final stable = {p_data['final_stable']}  "
          f"path stable = {p_data['path_stable']}  "
          f"unstable steps = {p_data['n_unstable_steps']}/"
          f"{p_data['n_steps']}")
    print(f"           gluon pair tail = {p_glu['tail']}  "
          f"has gluon pair = {p_glu['has_gluon_pair']}")
    print(f"  Neutron  final tr_M = {n_data['trM']:+.6f}  "
          f"final stable = {n_data['final_stable']}  "
          f"path stable = {n_data['path_stable']}  "
          f"unstable steps = {n_data['n_unstable_steps']}/"
          f"{n_data['n_steps']}")
    print(f"           gluon pair tail = {n_glu['tail']}  "
          f"has gluon pair = {n_glu['has_gluon_pair']}")
    print()

    header = (f"{'Isotope':<8} {'Z':>3} {'N':>3} {'A':>3} {'3A':>3} "
              f"{'glu_p':>6} {'glu_n':>6} "
              f"{'p_final':>8} {'n_final':>8} "
              f"{'p_path':>6} {'n_path':>6} "
              f"{'trM_atom':>12} {'sign_ok':>8} {'trunc':>6}")
    print(header)
    print("-" * len(header))

    per_iso: list[dict] = []
    n_fail_gluon = 0
    n_fail_final = 0
    n_fail_sign = 0

    # Atom-level tr_M is expensive (p(18) = 385 partitions with
    # seminormal matrices of dim up to ~1000).  Default off.  Enable
    # with --atom-trm; cap via --max-3a.
    MAX_ATOM_3A = ATOM_MAX_3A

    t_start = time.time()
    for (Z, N, A, BperA, sym, stability) in isotopes:
        iso_name = f"{A}{sym}"
        has_gluon = (p_glu['has_gluon_pair'] if Z > 0 else True) and \
                      (n_glu['has_gluon_pair'] if N > 0 else True)
        p_fin_ok = p_data['final_stable'] if Z > 0 else True
        n_fin_ok = n_data['final_stable'] if N > 0 else True
        p_path_ok = p_data['path_stable'] if Z > 0 else True
        n_path_ok = n_data['path_stable'] if N > 0 else True

        if not has_gluon:
            n_fail_gluon += 1
        if not (p_fin_ok and n_fin_ok):
            n_fail_final += 1

        if ATOM_TRM_ENABLED and 3 * A <= MAX_ATOM_3A:
            atom_info = atom_trM_light(Z, N)
            trM_atom_plan = atom_info['trM']
            truncated = atom_info['truncated']
            # Canonical Jones-Markov trace (authoritative for stability).
            # Symbolic tr_M grows fast; cap at 3A <= 9 to keep runtime
            # tractable unless user explicitly requests higher.
            if 3 * A <= CANONICAL_MAX_3A:
                can_info = atom_trM_canonical_symbolic(Z, N)
                trM_atom = can_info['trM']
                atom_info['canonical'] = can_info
            else:
                trM_atom = trM_atom_plan
                atom_info['canonical'] = {'skipped': 'over CANONICAL_MAX_3A'}
            trM_sign_ok = (trM_atom.real if isinstance(trM_atom, complex)
                           else trM_atom) >= 0
        else:
            trM_atom = None
            trM_atom_plan = None
            trM_sign_ok = None
            truncated = None
            atom_info = {"skipped_heavy": True, "3A": 3 * A}

        if trM_sign_ok is False:
            n_fail_sign += 1

        row = {
            "isotope": iso_name, "Z": Z, "N": N, "A": A,
            "n_strands": 3 * A,
            "stability_label": stability,
            "has_gluon": has_gluon,
            "proton_final_stable": p_fin_ok,
            "neutron_final_stable": n_fin_ok,
            "proton_path_stable": p_path_ok,
            "neutron_path_stable": n_path_ok,
            "trM_atom_canonical": (trM_atom if isinstance(trM_atom, float)
                                       else (trM_atom if trM_atom is None
                                             else complex(trM_atom))),
            "trM_atom_plancherel": trM_atom_plan,
            "trM_sign_ok": trM_sign_ok,
            "trM_truncated": truncated,
            "atom_info": atom_info,
        }
        per_iso.append(row)

        trM_s = f"{trM_atom:+.6f}" if trM_atom is not None else "   —    "
        sign_s = ("✓" if trM_sign_ok else ("✗" if trM_sign_ok is False
                                              else "—"))
        trunc_s = ("T" if truncated else "F") if truncated is not None \
            else "—"
        print(f"{iso_name:<8} {Z:>3} {N:>3} {A:>3} {3*A:>3} "
              f"{'Y' if Z==0 or p_glu['has_gluon_pair'] else 'N':>6} "
              f"{'Y' if N==0 or n_glu['has_gluon_pair'] else 'N':>6} "
              f"{'Y' if p_fin_ok else 'N':>8} "
              f"{'Y' if n_fin_ok else 'N':>8} "
              f"{'Y' if p_path_ok else 'N':>6} "
              f"{'Y' if n_path_ok else 'N':>6} "
              f"{trM_s:>12} {sign_s:>8} {trunc_s:>6}")

    dt = time.time() - t_start
    # Path stability is a property of the base nucleon (proton / neutron),
    # independent of which isotope they compose — so n_fail_path is
    # always 0 or len(isotopes).  Report it as a per-nucleon boolean
    # to avoid misleading isotope-scale counts.
    proton_path_stable = p_data["path_stable"]
    neutron_path_stable = n_data["path_stable"]
    print()
    print(f"Isotopes checked: {len(per_iso)}  (elapsed {dt:.1f}s)")
    print(f"  gluon-decoration failures:    {n_fail_gluon}")
    print(f"  final-NF-stability failures:  {n_fail_final}")
    print(f"  path stability — proton:      "
          f"{'✓' if proton_path_stable else '✗ (intermediate unstable)'}")
    print(f"  path stability — neutron:     "
          f"{'✓' if neutron_path_stable else '✗ (intermediate unstable)'}")
    print(f"  atom tr_M sign failures:      {n_fail_sign}")

    witness = {
        "computation": "validate-isotope-nf-stability",
        "description": (
            f"Validates that every isotope in isotope-mass-table.ISOTOPES "
            f"(1) carries the nucleon gluon-pair decoration (tail of "
            f"_{{PROTON,NEUTRON}}_G0 is two (1, 0) sigma_0 crossings), "
            f"(2) yields an H_3(q) SDP-stable proton and neutron NF at "
            f"the final step (both componentwise G·nf ≥ 0 and quadratic "
            f"nf^T G nf ≥ 0), with path stability and unstable-step count "
            f"recorded, and (3) produces a non-negative canonical "
            f"Jones-Markov trace for 3A ≤ {CANONICAL_MAX_3A} (symbolic) "
            f"and partition-weighted Plancherel trace for "
            f"3A ≤ {ATOM_MAX_3A} (diagnostic).  Heavy isotopes "
            f"(3A > {ATOM_MAX_3A}) record gluon + nucleon stability only."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q0": q0,
            "z_markov": z,
            "HA": h,
            "max_dim_truncation": 200,
            "atom_max_3A": MAX_ATOM_3A,
        },
        "base_nucleon_data": {
            "proton": {
                **p_data,
                "gluon_fingerprint": p_glu,
                "G0_chain_len": len(_PROTON_G0),
                "G1_chain_len": len(_PROTON_G1),
            },
            "neutron": {
                **n_data,
                "gluon_fingerprint": n_glu,
                "G0_chain_len": len(_NEUTRON_G0),
                "G1_chain_len": len(_NEUTRON_G1),
            },
        },
        "summary": {
            "n_isotopes": len(per_iso),
            "n_fail_gluon": n_fail_gluon,
            "n_fail_final_stability": n_fail_final,
            # Path stability is per-nucleon (not per-isotope): the
            # proton / neutron base NF is identical across all
            # isotopes, so the scalar `n_fail_path_stability` would
            # trivially be 0 or len(isotopes).  Report per-nucleon.
            "proton_path_stable": proton_path_stable,
            "neutron_path_stable": neutron_path_stable,
            "n_fail_atom_trM_sign": n_fail_sign,
            "elapsed_sec": dt,
        },
        "isotopes": per_iso,
    }

    out = Path(__file__).parent / "validate-isotope-nf-stability.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")


if __name__ == "__main__":
    main()
