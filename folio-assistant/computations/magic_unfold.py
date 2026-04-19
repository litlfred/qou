#!/usr/bin/env python3
"""
Magic-unfold exact reduction: core-valence braid word + tr_M peel.

Per docs/magic-unfold-exact-reduction.md, the atom Markov trace at
shell closures factors exactly:

    tr_M(W_atom)  =  z^K · tr_M(W_core) · tr_M(W_valence)

where W_core lives in H_{3C} (C = core nucleon count), W_valence in
H_{3V} (V = valence), and K counts the shell-coupling crossings
Markov-peeled at σ_{3C-1} between them.

This module:

  1. atom_braid_word_core_valence(Z, N, core_Z, core_N, gluons)
     Build the atom braid word with core nucleons (strands 0..3C-1)
     FIRST, then a single shell-coupling σ_{3C-1}^K between the last
     core nucleon and the first valence nucleon, then valence
     nucleons (strands 3C..3A-1).

  2. magic_unfold_trM(Z, N, gluons)
     Detect largest magic core in (Z, N), build core + valence
     words separately, compute tr_M of each in the smaller algebra,
     combine with z-factor.

  3. validate_against_full(Z, N, gluons)
     Confirm tr_M(reordered core-valence word) matches tr_M(standard
     atom_braid_word_3A) — if yes, ordering is immaterial; if no,
     Markov peel is more subtle than naïve reorder.
"""
from __future__ import annotations

import sys
import json
import time
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0, HA as h
from canonical_plus_multibrane import z_mark
from hecke_characters import partitions_of, dim_q, qfac
from mass_at_3A_proper import (_cached_seminormal, atom_braid_word_3A)
from hecke_core import _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1


MAGIC = {2, 8, 20, 28, 50, 82, 126}


def _nucleon_body(quark_type: str) -> tuple[list, list]:
    """Strip the gluon tail from _PROTON_G0 / _NEUTRON_G0 to get the
    body-only (B₃ + quark-pair) chain."""
    if quark_type == 'p':
        g0, g1 = list(_PROTON_G0), list(_PROTON_G1)
    else:
        g0, g1 = list(_NEUTRON_G0), list(_NEUTRON_G1)
    # Strip up to two trailing (1, 0) gluon crossings (1·σ₀ post-patch).
    while g0 and (float(g0[-1][0]), float(g0[-1][1])) == (1.0, 0.0) and len(g0) > 3:
        g0.pop()
    return g0, g1


def atom_braid_word_core_valence(
        Z: int, N: int, core_Z: int, core_N: int,
        *, m_pp: int = 1, m_pn: int = 1, m_nn: int = 1,
        include_inter: bool = True
        ) -> list[tuple[float, float, int]]:
    """Reordered atom braid word: core nucleons first, then valence.

    Strand layout:
      [0 .. 3C-1]       — core nucleons (C = core_Z + core_N)
      [3C .. 3A-1]      — valence nucleons

    Generator usage:
      σ_0 .. σ_{3C-2}   — core-internal (including core inter-nucleon)
      σ_{3C-1}          — SHELL COUPLING (peel point)
      σ_{3C} .. σ_{3A-2} — valence-internal (including valence inter)

    Single gluon tail per nucleon (1·σ₀, post 2026-04-19 patch).
    """
    A = Z + N
    C = core_Z + core_N
    V_p = Z - core_Z
    V_n = N - core_N
    assert C <= A and V_p >= 0 and V_n >= 0, \
        f"core ({core_Z},{core_N}) must fit inside (Z,N)=({Z},{N})"

    word: list[tuple[float, float, int]] = []
    # Core ordering: protons first, then neutrons
    core_ordering = ['p'] * core_Z + ['n'] * core_N
    valence_ordering = ['p'] * V_p + ['n'] * V_n

    def _emit_nucleon(nuc: str, base_gen: int):
        body_g0, body_g1 = _nucleon_body(nuc)
        for (c, d) in body_g0:
            word.append((float(c), float(d), base_gen))
        for (c, d) in body_g1:
            word.append((float(c), float(d), base_gen + 1))
        word.append((1.0, 0.0, base_gen))   # 1·σ₀ gluon

    def _emit_inter(nuc_left: str, nuc_right: str, gen: int):
        if nuc_left == 'p' and nuc_right == 'p':
            c, d = 1.0, 0.0; m = m_pp
        elif nuc_left == 'n' and nuc_right == 'n':
            c, d = 1.0, -h; m = m_nn
        else:
            c, d = 1.0, -h / 2; m = m_pn
        for _ in range(m):
            word.append((c, d, gen))

    # ── CORE ────────────────────────────────────────────────
    for k, nuc in enumerate(core_ordering):
        _emit_nucleon(nuc, base_gen=3 * k)
        if include_inter and k < C - 1:
            _emit_inter(nuc, core_ordering[k + 1], gen=3 * k + 2)

    if V_p + V_n == 0:
        return word

    # ── SHELL COUPLING σ_{3C-1} ─────────────────────────────
    # Last core nucleon's top strand (3C-1) couples to first valence
    # nucleon's bottom strand (3C).  Generator between them is σ_{3C-1}.
    if include_inter and C > 0:
        last_core = core_ordering[-1]
        first_val = valence_ordering[0]
        _emit_inter(last_core, first_val, gen=3 * C - 1)

    # ── VALENCE ─────────────────────────────────────────────
    # Valence nucleons placed at strands 3C..3A-1.
    # Their internal gens are σ_{3C}..σ_{3A-2}.
    for k, nuc in enumerate(valence_ordering):
        base_gen = 3 * (C + k)
        _emit_nucleon(nuc, base_gen=base_gen)
        if include_inter and k < len(valence_ordering) - 1:
            _emit_inter(nuc, valence_ordering[k + 1], gen=3 * (C + k) + 2)

    return word


def largest_magic_core(Z: int, N: int) -> tuple[int, int]:
    """Largest (core_Z, core_N) with both coordinates in MAGIC ∪ {0}
    and ≤ (Z, N)."""
    core_Z = max((m for m in (MAGIC | {0}) if m <= Z), default=0)
    core_N = max((m for m in (MAGIC | {0}) if m <= N), default=0)
    return core_Z, core_N


def trM_plancherel_word(word: list, n_strands: int) -> float:
    """Plancherel-weighted Markov trace on an explicit n-strand word."""
    from scipy.sparse import issparse, eye as speye
    nfac = qfac(n_strands)
    total = 0.0
    for shape in partitions_of(n_strands):
        sigmas, dim, _ = _cached_seminormal(shape)
        if dim == 0:
            continue
        dq = dim_q(shape)
        if dq == 0:
            continue
        w = (dq * dq) / nfac
        sparse = bool(sigmas) and issparse(sigmas[0])
        if sparse:
            prod = speye(dim, format='csr'); I = speye(dim, format='csr')
        else:
            prod = np.eye(dim); I = np.eye(dim)
        for (c, d, g) in word:
            if g < len(sigmas):
                prod = prod @ (c * sigmas[g] + d * I)
        chi = float(prod.diagonal().sum()) if sparse else float(np.trace(prod))
        total += w * chi / dim
    return total


def validate_against_full(Z: int, N: int, core_Z: int, core_N: int,
                            *, include_inter: bool = True) -> dict:
    """Compare tr_M of the reordered core-valence word against the
    standard atom_braid_word_3A.  If they agree, ordering doesn't
    matter (braid relations absorb the permutation) — we can peel;
    if they disagree, the reorder changes the atom and magic-unfold
    is a DIFFERENT mass prediction.
    """
    A = Z + N
    n = 3 * A
    w_std = atom_braid_word_3A(Z, N, m_pp=1, m_pn=1, m_nn=1,
                                  include_inter=include_inter)
    w_cv = atom_braid_word_core_valence(
        Z, N, core_Z, core_N, include_inter=include_inter)
    trM_std = trM_plancherel_word(w_std, n)
    trM_cv = trM_plancherel_word(w_cv, n)
    return {
        "Z": Z, "N": N, "core_Z": core_Z, "core_N": core_N,
        "n_strands": n,
        "word_std_len": len(w_std), "word_cv_len": len(w_cv),
        "trM_std": trM_std, "trM_cv": trM_cv,
        "trM_diff": trM_cv - trM_std,
        "agree": abs(trM_cv - trM_std) < 1e-10,
    }


if __name__ == "__main__":
    print("=" * 110)
    print("MAGIC-UNFOLD: core-valence braid word validation")
    print(f"q0 = {Q0}, MAGIC = {sorted(MAGIC)}")
    print("=" * 110)

    ATOMS = [
        ("D",   1, 1),
        ("T",   1, 2),
        ("3He", 2, 1),
        ("4He", 2, 2),
        ("6Li", 3, 3),
    ]

    results = []
    for name, Z, N in ATOMS:
        core_Z, core_N = largest_magic_core(Z, N)
        C = core_Z + core_N
        V = (Z - core_Z) + (N - core_N)
        print(f"\n{name} (Z={Z}, N={N}, A={Z+N}) "
              f"→ core=({core_Z},{core_N})  C={C}  V={V}")
        if C == 0:
            print(f"  no magic core — skipping validation")
            continue
        for include_inter in (False, True):
            tag = "atom" if include_inter else "free"
            try:
                r = validate_against_full(
                    Z, N, core_Z, core_N, include_inter=include_inter)
                agree = "✓" if r["agree"] else "✗"
                print(f"  {tag}:  std tr_M = {r['trM_std']:+.6e}  "
                      f"core-valence tr_M = {r['trM_cv']:+.6e}  "
                      f"diff = {r['trM_diff']:+.3e}  {agree}")
                results.append({"atom": name, "path": tag, **r})
            except Exception as e:
                print(f"  {tag}:  ERR  {type(e).__name__}: {e}")
                results.append({"atom": name, "path": tag, "error": str(e)})

    witness = {
        "computation": "magic-unfold-validation",
        "description": (
            "Validation of the reordered core-valence braid word vs "
            "the standard atom_braid_word_3A.  Checks whether placing "
            "core nucleons first produces the same Markov trace — if "
            "yes, the reorder is braid-permutation-equivalent; if no, "
            "magic-unfold is a structurally different atom that must "
            "be separately physically interpreted."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": Q0, "MAGIC": sorted(MAGIC)},
        "results": results,
    }
    out = Path(__file__).parent / "magic-unfold-validation.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
