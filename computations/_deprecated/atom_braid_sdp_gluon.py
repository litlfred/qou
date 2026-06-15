#!/usr/bin/env python3
"""
SDP-optimal per-nucleon gluon braid builder — P2.1 of the 1-ppm
workplan.

The baseline atom_braid_word_3A (mass_at_3A_proper.py) applies a
UNIFORM 2·σ₀ gluon tail to every nucleon.  The integer-LP-gluon
computation (integer-lp-gluon.py / integer-lp-gluon.witness.json)
found that only the proton optimum is 2·σ₀; the neutron optimum is
L₊ → L₋ = σ₀σ₁σ₁σ₀ under q₀.  Applying 2·σ₀ to neutrons therefore
introduces a known error.

This module provides:

  atom_braid_word_3A_sdp_gluon(Z, N, ...)
    — identical to atom_braid_word_3A except the gluon tail of each
      NEUTRON nucleon is σ₀σ₁σ₁σ₀ instead of σ₀σ₀, respecting the
      integer-LP (= SDP-feasibility) optimum.

The integer-LP in integer-lp-gluon.py is an SDP in disguise: the
stability predicate is G · NF ≥ 0 with G the H_3(q) Gram matrix,
which is a linear PSD-feasibility constraint on the certificate NF.
(True matrix-SDP would write NF·NF^T ⪰ 0; our NF is a 6-vector, so
the feasibility check collapses to the componentwise Gram-positivity
LP.)  We therefore re-use the same integer-LP optima directly.

Usage in the JM tower:

    from atom_braid_sdp_gluon import atom_braid_word_3A_sdp_gluon
    word = atom_braid_word_3A_sdp_gluon(Z, N, ...)
    # Substitute for atom_braid_word_3A in syt_cell_tower.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import HA as h
from hecke_core import _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1


# ── Per-nucleon "body" chains stripped of the trailing gluon pair ──
# _PROTON_G0 / _NEUTRON_G0 end with two (1, 0) σ₀ crossings per
# hecke_core.nucleon_gen_chains.  We remove those and re-apply the
# per-nucleon SDP optimum.

def _strip_gluon_tail(chain: list[tuple[float, float]]
                       ) -> list[tuple[float, float]]:
    """Remove the two trailing (1, 0) σ gluon crossings from a chain.

    Defensive: only strips if the tail actually matches (1.0, 0.0)
    twice; otherwise returns the chain unchanged.
    """
    if len(chain) < 2:
        return list(chain)
    last_two = [(float(c), float(d)) for (c, d) in chain[-2:]]
    if last_two == [(1.0, 0.0), (1.0, 0.0)]:
        return list(chain[:-2])
    return list(chain)


_PROTON_G0_BODY = _strip_gluon_tail(_PROTON_G0)
_PROTON_G1_BODY = list(_PROTON_G1)
_NEUTRON_G0_BODY = _strip_gluon_tail(_NEUTRON_G0)
_NEUTRON_G1_BODY = list(_NEUTRON_G1)


def nucleon_word_3A_sdp(quark_type: str, base_gen: int
                          ) -> list[tuple[float, float, int]]:
    """Emit the full per-nucleon braid word with the SDP-optimal
    gluon tail.

    quark_type: 'p' (proton uud) or 'n' (neutron udd).
    base_gen:   3k for the k-th nucleon (0-indexed).

    Returns a list of (c, d, gen_idx) triples.

    Proton: preserves the exact old nucleon_gen_chains / atom_braid_word_3A
      ordering (body_g0 + σ₀σ₀ gluon, then body_g1).  Proton word is
      IDENTICAL to atom_braid_word_3A.

    Neutron: body_g0 + body_g1 first, then the integer-LP-optimal
      gluon L₊ L₋ = σ₀σ₁σ₁σ₀ at (base_gen, base_gen+1).  This differs
      structurally from the uniform 2·σ₀ tail applied by the current
      atom_braid_word_3A.
    """
    word: list[tuple[float, float, int]] = []
    if quark_type == 'p':
        # Match old: body_g0 + gluon σ₀σ₀ baked INTO _PROTON_G0, then body_g1
        for (c, d) in _PROTON_G0:
            word.append((float(c), float(d), base_gen))
        for (c, d) in _PROTON_G1:
            word.append((float(c), float(d), base_gen + 1))
    else:
        # body_g0 (no gluon), body_g1 (no gluon), then L₊ L₋ tail
        for (c, d) in _NEUTRON_G0_BODY:
            word.append((float(c), float(d), base_gen))
        for (c, d) in _NEUTRON_G1_BODY:
            word.append((float(c), float(d), base_gen + 1))
        # L₊ L₋ = σ₀ σ₁ σ₁ σ₀
        word.append((1.0, 0.0, base_gen))
        word.append((1.0, 0.0, base_gen + 1))
        word.append((1.0, 0.0, base_gen + 1))
        word.append((1.0, 0.0, base_gen))

    return word


def atom_braid_word_3A_sdp_gluon(Z: int, N: int, *,
                                     m_pp: int = 1, m_pn: int = 1,
                                     m_nn: int = 1,
                                     include_inter: bool = True
                                     ) -> list[tuple[float, float, int]]:
    """Full 3A-strand braid word with per-nucleon SDP-optimal gluons.

    Drop-in replacement for
    mass_at_3A_proper.atom_braid_word_3A that uses
    nucleon_word_3A_sdp per nucleon.  Inter-nucleon crossings are
    identical to atom_braid_word_3A (gen 3k+2, pp/nn/pn per the
    ordering), gated by include_inter.
    """
    A = Z + N
    word: list[tuple[float, float, int]] = []
    ordering = ['p'] * Z + ['n'] * N
    for k, nuc in enumerate(ordering):
        base_gen = 3 * k
        word.extend(nucleon_word_3A_sdp(nuc, base_gen))
        if include_inter and k < A - 1:
            i_inter = 3 * k + 2
            next_nuc = ordering[k + 1]
            if nuc == 'p' and next_nuc == 'p':
                base_cross = (1.0, 0.0)
                m_this = m_pp
            elif nuc == 'n' and next_nuc == 'n':
                base_cross = (1.0, -h)
                m_this = m_nn
            else:
                base_cross = (1.0, -h / 2)
                m_this = m_pn
            c, d = base_cross
            for _ in range(m_this):
                word.append((c, d, i_inter))
    return word


# ── Quick sanity check ───────────────────────────────────────

if __name__ == "__main__":
    # Proton: word should be identical to atom_braid_word_3A for Z=1, N=0
    from mass_at_3A_proper import atom_braid_word_3A
    wp_old = atom_braid_word_3A(1, 0, include_inter=False)
    wp_new = atom_braid_word_3A_sdp_gluon(1, 0, include_inter=False)
    assert wp_old == wp_new, (
        f"Proton word mismatch:\n  old={wp_old}\n  new={wp_new}")
    print(f"Proton word (Z=1, N=0): len={len(wp_old)}  IDENTICAL ✓")

    # Neutron: word should differ — neutron gluon is now L₊L₋
    wn_old = atom_braid_word_3A(0, 1, include_inter=False)
    wn_new = atom_braid_word_3A_sdp_gluon(0, 1, include_inter=False)
    print(f"\nNeutron word (Z=0, N=1):")
    print(f"  old ({len(wn_old)} factors, uniform 2·σ₀ tail):")
    for t in wn_old:
        print(f"    {t}")
    print(f"  new ({len(wn_new)} factors, L₊L₋ tail):")
    for t in wn_new:
        print(f"    {t}")

    # D
    wD_old = atom_braid_word_3A(1, 1, include_inter=True)
    wD_new = atom_braid_word_3A_sdp_gluon(1, 1, include_inter=True)
    print(f"\nD word (Z=1, N=1):  old={len(wD_old)} new={len(wD_new)} "
          f"(+{len(wD_new)-len(wD_old)} factors)")
