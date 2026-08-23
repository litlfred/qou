#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical/intermediate-sympy witness; no symbolic-q polynomial in output.
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.

Canonical Markov trace + PROPER Φ_q tower.

Combines:
  • CANONICAL single-brane Markov trace (markov_trace_canonical.
    tr_M_element) — matches prop:categorical-mass-markov exactly.
  • PROPER Φ_q tower over exceptional divisors per
    prop:mass-endomorphism-tower — NO H_3 per-generator shortcut.

Per the prop's formula at jet level n:

  𝔪^{(n)}(ρ) = |Π V̂_i^{(n)}|
             + Σ_i     Φ_q(|V̂_i^{(n)}|)
             + z² Σ_{(i,j) ∈ 𝒫_n}  Φ_q(|V̂_i^{(n)} V̂_j^{(n)}|)

where V̂_i is the "additive Wedderburn traced volume at generator i"
and 𝒫_n is the set of independent pair blow-up centres.

Key definitional upgrade vs hecke_core.atom_per_generator_volumes:

  Old (H_3 shortcut):
    Vs = z_mark·a + b   (std-rep 2-param accumulator)
    V_f = w_sym·sp + w_std·Vs + w_alt·ap   (H_3 Wedderburn weights)

  New (canonical via Jucys–Murphy):
    L_k = T_{k-1} T_{k-2} ... T_1 T_1 ... T_{k-1}  ∈ H_n(q)
    L_k acts diagonally on Young basis |T⟩ with eigenvalue q^{2 c_T(k)}
    (c_T(k) = content of cell containing k).
    V̂_i := Markov-trace-weighted average of L_{i+1} eigenvalue over
           all λ ⊢ n, SYTs T, weighted by Plancherel measure.

    V̂_i^{canonical}  =  Σ_{λ ⊢ n}  w_λ  ·  (1/d_λ)  Σ_{T ∈ SYT(λ)}
                            q^{2 c_T(i+1)}

  At q = 1: this gives the classical content average — consistent
  with the semisimple decomposition.  At q ≠ 1 it carries the full
  q-deformation naturally, unlike the H_3 shortcut which only knows
  about the three H_3 reps.

𝒫_n choice: per the audit + empirical probe (rem:mass-endomorphism-
jet-tower, adjacent_vs_full_probe), the prop's adjacent-only
restriction empirically under-performs.  We offer a `pair_mode`
switch:
  "adjacent"  — prop's original (|i−j| = 1 only)
  "full"      — all pairs (empirically best at A ≥ 6)

Binding:
  B(Z, N) = E_0 · ( 𝔪^{(n)}(W_free) − 𝔪^{(n)}(W_atom) )
  with E_0 calibrated by the **proton tower** as
  E_0 = m_p_CODATA / m_proton_tower (MeV per categorical unit), per
  `calibrate_E0_tower` below — NOT the β-decay Q-value 0.78233341 MeV
  (that is the calibration used by `crt_markov.py` and other
  Markov-trace scripts; this module is a separate calibration.)

The canonical Markov trace (tr_M_element) is used ONLY as a sanity
check / comparison — the tower formula itself is a sum of Φ_q terms
with V̂_i as arguments.  These are separate paths:

  (A) binding_canonical.binding_canonical:
        B = E_0 · (|tr_M(W_free)| − |tr_M(W_atom)|)
        pure single-brane Markov, no Φ_q.
  (B) binding_canonical_tower (this module):
        B = E_0 · (𝔪^{(n)}(free) − 𝔪^{(n)}(atom))
        where 𝔪 uses V̂_i computed via JM eigenvalues (canonical),
        fed into prop's |Π| + Σ Φ_q + z² Σ Φ_q cross-term formula.

(B) is the "canonical-with-proper-tower" the paper ultimately wants.
(A) is the base-level Markov-trace defect only.

SCOPE — this module is CURRENTLY A SKELETON:
The per-generator V̂_i definition used below is a provisional
"JM-averaged product of (c_k · eigenvalue + d_k) factors at
position i", not the rigorous canonical-H_{3A} Wedderburn V̂.
The rigorous definition requires per-irrep seminormal matrix
products at each generator position (like build_seminormal_matrices
+ accumulate per position), which is computationally expensive at
H_{3A} for heavy atoms.  Current skeleton gives NUMERIC TOWER
SCALES (calibrated via proton) but not yet AME-accurate binding —
the residual gap is the V̂ definition itself.

Use this module as the INFRASTRUCTURE for future canonical-V̂
implementations: JM eigenvalue caching, Plancherel averaging,
proton tower calibration, tower formula.  Plug in a corrected V̂
definition (per-irrep seminormal matrix chain) to close the gap.

Future: the full multi-brane tower Σ_n 𝔪^{(n)} over all jet levels
(conj:mass-endomorphism), summing exceptional-divisor Φ_q
contributions at each level.  This module does ONE level (n = 3A);
multi-level extension requires per-level V̂ propagation via the
Kähler differential action on H_n(q) — still open.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import math
import json
import time
from pathlib import Path
from datetime import datetime, timezone
from itertools import combinations

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0, Q_INV as QI, HA as H0
from experimental_constants import M_P_MEV
from mass_endomorphism import Phi_q, z_mark
from hecke_characters import (partitions_of, dim_q, qfac,
                                standard_young_tableaux)
from hecke_3a_weights import partitions_of_n
from mass_at_3A_proper import atom_braid_word_3A


# ── Jucys–Murphy eigenvalue averages ─────────────────────────

def _syt_content(shape: tuple[int, ...], syt: dict[int, int],
                   cells: list[tuple[int, int]], entry: int) -> int:
    """Content c(cell of `entry` in SYT) = col − row."""
    cell_idx = syt[entry]
    row, col = cells[cell_idx]
    return col - row


def jm_eigenvalue_avg(n: int, k: int) -> float:
    """Plancherel-weighted average of q^{2 c_T(k)} over all λ ⊢ n, T ∈ SYT(λ).

    V̂_{k−1}^canonical  =  Σ_λ w_λ · (1/d_λ) Σ_{T ∈ SYT(λ)} q^{2 c_T(k)}

    Matches the Jucys-Murphy eigenvalue of L_k in Plancherel-averaged
    irrep, giving the canonical per-generator "value" for the tower.
    """
    if n < 1:
        return 1.0
    nfac = qfac(n)
    total = 0.0
    for shape in partitions_of(n):
        dq = dim_q(shape)
        if dq == 0:
            continue
        # Use SYT enumeration from hecke_characters
        syts, cells, _contents = standard_young_tableaux(shape)
        d_cl = len(syts)
        if d_cl == 0:
            continue
        w_lam = (dq * dq) / nfac
        # Average q^{2 c_T(k)} over SYTs of shape λ
        sum_eig = 0.0
        for syt in syts:
            c = _syt_content(shape, syt, cells, k)
            sum_eig += Q0 ** (2 * c)
        total += w_lam * sum_eig / d_cl
    return total


_JM_CACHE: dict[tuple[int, int], float] = {}


def cached_jm_avg(n: int, k: int) -> float:
    key = (n, k)
    if key not in _JM_CACHE:
        _JM_CACHE[key] = jm_eigenvalue_avg(n, k)
    return _JM_CACHE[key]


# ── Per-λ eigenvalue multiplicities m_±(λ, i) ─────────────────
#
# In the seminormal basis, σ_i acts on each SYT |T⟩ as:
#   +q          if entries (i, i+1) are in the same ROW of T
#   −q^{-1}     if entries (i, i+1) are in the same COLUMN of T
#   2×2 block   otherwise (T and T' related by swap(i, i+1) give
#               a 2-dim block with eigenvalues {q, −q^{-1}} — each
#               contributes 1 to m_+ and 1 to m_-)
#
# So m_+(λ, i) + m_-(λ, i) = d_λ,
#    m_+(λ, i) = #{T: (i,i+1) same row} + (#{2×2 blocks})
#    m_-(λ, i) = #{T: (i,i+1) same col} + (#{2×2 blocks})
#    (each 2×2 block contributes 1 to m_+ and 1 to m_-, total 2)


_MPM_CACHE: dict[tuple[tuple, int], tuple[int, int]] = {}
_MPM_DISK_DIR = Path(__file__).parent / ".cache" / "eigen_mult"


def _load_mpm_disk(n: int) -> dict:
    """Load cached (shape, i) → (m_+, m_-) for all λ ⊢ n from disk.

    Keys in the JSON file follow the format "shape_csv:i" where
    shape_csv is the comma-separated partition (no brackets) — see
    _save_mpm_disk.  Returns dict keyed by (tuple[int, ...], int) →
    tuple[int, int], matching the in-memory _MPM_CACHE signature.
    """
    _MPM_DISK_DIR.mkdir(parents=True, exist_ok=True)
    f = _MPM_DISK_DIR / f"n{n}.json"
    if not f.exists():
        return {}
    try:
        raw = json.loads(f.read_text())
        out = {}
        for k, v in raw.items():
            shape_str, i_str = k.split(":")
            shape = (tuple(int(x) for x in shape_str.split(","))
                      if shape_str else ())
            out[(shape, int(i_str))] = (int(v[0]), int(v[1]))
        return out
    except Exception:
        return {}


def _save_mpm_disk(n: int):
    """Persist all cached mults for λ ⊢ n.

    Keys stored as "a,b,c:i" where a,b,c is the comma-joined shape
    (no brackets) and i the generator index.
    """
    _MPM_DISK_DIR.mkdir(parents=True, exist_ok=True)
    f = _MPM_DISK_DIR / f"n{n}.json"
    payload = {}
    for (shape, i), (mp, mm) in _MPM_CACHE.items():
        if sum(shape) != n:
            continue
        shape_str = ",".join(str(x) for x in shape) if shape else ""
        key = f"{shape_str}:{i}"
        payload[key] = [int(mp), int(mm)]
    try:
        f.write_text(json.dumps(payload))
    except Exception:
        pass


def eigen_multiplicities(shape: tuple[int, ...], i: int) -> tuple[int, int]:
    """m_+(λ, i), m_-(λ, i) for generator σ_i on irrep λ.

    Returns (m_plus, m_minus) satisfying m_plus + m_minus = d_λ.
    """
    key = (shape, i)
    if key in _MPM_CACHE:
        return _MPM_CACHE[key]
    syts, cells, _contents = standard_young_tableaux(shape)
    m_same_row = 0
    m_same_col = 0
    m_2x2 = 0
    # For each SYT, check if entries (i+1, i+2) are same row/col/other
    # (Note: our generator index 0-based maps to entries (i+1, i+2) in
    # the 1-indexed SYT filling.)
    entry_a = i + 1
    entry_b = i + 2
    for syt in syts:
        cell_a = cells[syt[entry_a]]
        cell_b = cells[syt[entry_b]]
        if cell_a[0] == cell_b[0]:
            m_same_row += 1
        elif cell_a[1] == cell_b[1]:
            m_same_col += 1
        else:
            m_2x2 += 1  # will be counted as part of a block
    # 2×2 blocks pair up: each SYT not same-row/col IS part of a pair.
    # But our counting counts each SYT separately; the block contributes
    # 1 to m_+ and 1 to m_- total, but the pair has 2 SYTs, so we split:
    # each SYT in a pair contributes ½ to m_+ and ½ to m_-.
    # Using integer arithmetic: m_+ += m_2x2 / 2, same for m_-.
    # Since m_2x2 is always even (SYTs pair up), this is clean:
    m_plus = m_same_row + m_2x2 // 2
    m_minus = m_same_col + m_2x2 // 2
    _MPM_CACHE[key] = (m_plus, m_minus)
    return m_plus, m_minus


# ── Per-(i, λ) V̂_i^λ via eigenvalue factorization ─────────
#
# For each generator position i and irrep λ, the accumulated matrix
# product M_i^λ = Π_k (c_k σ_i^λ + d_k I) has trace
#   tr_λ(M_i) = m_+(λ, i) · Π_k (c_k q + d_k)
#             + m_-(λ, i) · Π_k (-c_k/q + d_k)
# because σ_i^λ has exactly two eigenvalues {q, -q^{-1}} with
# multiplicities m_±.  Normalize: V̂_i^λ = tr_λ(M_i) / d_λ.
#
# No matrix products needed!  Just scalar products of (c q + d) and
# (-c/q + d) factors at each generator position, multiplied by the
# pre-cached multiplicities.

def per_irrep_V_hat(Z: int, N: int, shape: tuple[int, ...], *,
                      include_inter: bool = True,
                      m_pp: int = 1, m_pn: int = 1,
                      m_nn: int = 1) -> list[float]:
    """V̂_i^λ = tr_λ(M_i^λ) / d_λ for each generator i.

    Uses eigenvalue factorization — O(num_factors) per (i, λ).
    """
    from hecke_characters import dim_q as _dim_q
    A = Z + N
    n_strands = 3 * A
    word = atom_braid_word_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                                include_inter=include_inter)
    n_gens = n_strands - 1
    word_by_gen: list[list[tuple[float, float]]] = [[]
                                                      for _ in range(n_gens)]
    for (c, d, g) in word:
        if 0 <= g < n_gens:
            word_by_gen[g].append((c, d))

    d_cl = len(standard_young_tableaux(shape)[0])
    if d_cl == 0:
        return [0.0] * n_gens

    V = [0.0] * n_gens
    for i in range(n_gens):
        factors = word_by_gen[i]
        if not factors:
            V[i] = 1.0  # identity at this position
            continue
        # Eigenvalue-factored trace
        prod_pos = 1.0  # Π (c_k q + d_k)
        prod_neg = 1.0  # Π (-c_k q^{-1} + d_k)
        for (c, d) in factors:
            prod_pos *= c * Q0 + d
            prod_neg *= -c * QI + d
        m_plus, m_minus = eigen_multiplicities(shape, i)
        tr_lam = m_plus * prod_pos + m_minus * prod_neg
        V[i] = tr_lam / d_cl
    return V


# ── Legacy provisional per_gen_V_hat (kept for comparison) ───

def per_gen_V_hat_canonical(Z: int, N: int, *,
                              include_inter: bool = True,
                              m_pp: int = 1, m_pn: int = 1,
                              m_nn: int = 1) -> list[float]:
    """Canonical V̂_i list for the atom braid.

    V̂_i is the Plancherel-averaged JM eigenvalue at position i+1,
    weighted by the per-generator crossing product at position i.

    For each generator i in the chain walk (matching
    atom_braid_word_3A convention), we:
      1. Collect the (c_k, d_k) factors applied at position i.
      2. Multiply them symbolically (c_k q + d_k) at SYM rep and
         (-c_k q^{-1} + d_k) at ALT rep, use JM eigenvalue at std.
      3. Plancherel-average over all λ ⊢ 3A-strand Young lattice.

    Simplified: V̂_i = (per-gen word value) · (JM eigenvalue average
    at position i+1).

    Returns list of length 3A − 1 (atom) or 2A (free).
    """
    A = Z + N
    if A < 1:
        return []
    n_strands = 3 * A
    word = atom_braid_word_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                                include_inter=include_inter)
    if include_inter:
        n_gens = n_strands - 1
    else:
        # Free baseline: 2A generators (2 per nucleon, disjoint).
        # Map them to positions 0..2A-1 by the atom_braid_word_3A
        # convention's base_g0 = 3k, base_g1 = 3k+1.
        n_gens = n_strands - 1  # keep same indexing; inter gens
                                 # have empty word

    # Aggregate crossing coefficients per generator
    V = [0.0] * n_gens
    word_by_gen: list[list[tuple[float, float]]] = [[]
                                                      for _ in range(n_gens)]
    for (c, d, g) in word:
        if 0 <= g < n_gens:
            word_by_gen[g].append((c, d))

    for i in range(n_gens):
        factors = word_by_gen[i]
        if not factors:
            # Trivial at this generator (e.g., inter position in free
            # baseline).  V̂ = 1 (identity element's JM average is
            # q^0 = 1 on the trivial SYT cell).
            V[i] = 1.0
            continue
        # Multiply (c_k · σ_i + d_k) factors.  In a single-partition
        # 1-dimensional projection (sym rep or alt rep), σ_i acts as
        # scalar eigenvalue q or -q^{-1}.  Take the Markov-weighted
        # blend via the JM eigenvalue average.
        # Product in sym (λ = (n)): each factor gives c·q + d.
        prod_sym = 1.0
        prod_alt = 1.0
        for (c, d) in factors:
            prod_sym *= c * Q0 + d
            prod_alt *= -c * QI + d
        # Canonical V̂_i: Plancherel-weighted average of per-rep product.
        # Weights: w_sym = 1/[n]_q (from q-hook formula at λ = (n)),
        # w_alt  = 1/[n]_q (same at λ = (1^n)).
        # For k=i+1, the JM eigenvalue at position k in sym-shape is
        # q^{2(k-1)} (content = k-1 for the single-row), and in
        # alt-shape is q^{-2(k-1)}.
        # The proper canonical V̂ uses cached_jm_avg at position i+1:
        jm_avg = cached_jm_avg(n_strands, i + 1)
        # Blend: average of sym-product and alt-product, JM-weighted
        V[i] = 0.5 * (prod_sym + prod_alt) * jm_avg / Q0 ** (2 * 0)
        # Normalization: divide by Q0^{2·0} = 1 (placeholder; refine)
    return V


# ── Tower mass from canonical V̂ ─────────────────────────────

def canonical_tower_mass(V: list[float], *,
                           pair_mode: str = "full",
                           cap_frac: float = 0.98,
                           term: str = "tower_term") -> dict:
    """Φ_q tower mass from canonical V̂_i, with saturation-safe Φ_q.

    pair_mode ∈ {"adjacent", "full"}:
      "adjacent"  prop's original form (|i−j| = 1)
      "full"      all pairs (empirically best on stable A ≥ 6)

    Returns {desc, single, cross, total}.
    """
    from mass_at_3A_proper import _tower_spec
    _spec = _tower_spec(term, cap_frac)
    n = len(V)
    desc = 1.0
    for v in V:
        desc *= v
    desc = abs(desc)
    single = sum(_spec(abs(v)) for v in V)
    cross = 0.0
    if pair_mode == "adjacent":
        for i in range(n - 1):
            cross += z_mark ** 2 * _spec(abs(V[i] * V[i + 1]))
    elif pair_mode == "full":
        for i in range(n):
            for j in range(i + 1, n):
                cross += z_mark ** 2 * _spec(abs(V[i] * V[j]))
    else:
        raise ValueError(pair_mode)
    return {"desc": desc, "single": single, "cross": cross,
             "total": desc + single + cross}


_E0_TOWER_CACHE: dict[str, float] = {}


def calibrate_E0_tower(pair_mode: str = "full") -> float:
    """Proton-tower calibration: E_0 such that canonical_tower_mass
    on free proton (Z=1, N=0) matches 938.272 MeV.

    Matches hecke_core.E_0_CALIBRATION_MEV's SPIRIT but in the
    canonical-V̂ tower basis.  Cached.
    """
    key = pair_mode
    if key in _E0_TOWER_CACHE:
        return _E0_TOWER_CACHE[key]
    V_p = per_gen_V_hat_canonical(1, 0, include_inter=False)
    if not V_p:
        return 1.0
    # MASS context (absolute proton mass vs 938.272 MeV), so this one keeps
    # the historical phi_q per `_li_2_q_util`'s binding/mass rule. The Lean
    # towerTerm discipline is applied to the binding_* consumers below.
    m_p = canonical_tower_mass(V_p, pair_mode=pair_mode, term="phi_q")
    if m_p["total"] <= 0 or not math.isfinite(m_p["total"]):
        return 1.0
    # NOTE: alt-calibration (diagnostic). CAL-3 canonical E_0 is
    # `hecke_core.E_0_CALIBRATION_MEV` = Q_β(n). This proton-tower-
    # anchored variant is retained for per-block comparison only.
    E0 = float(M_P_MEV) / m_p["total"]
    _E0_TOWER_CACHE[key] = E0
    return E0


def binding_per_irrep_tower(Z: int, N: int, *, m_pp=1, m_pn=1, m_nn=1,
                              E_0: float | None = None,
                              pair_mode: str = "full",
                              verbose: bool = False,
                           term: str = "tower_term") -> dict:
    """Canonical-with-proper-tower via per-irrep V̂ + Plancherel sum.

    For each λ ⊢ 3A:
      1. Compute V̂_i^λ = tr_λ(M_i^λ)/d_λ via eigenvalue factorization.
      2. Per-λ tower mass 𝔪^λ = |Π V̂_i^λ| + Σ Φ_q(V̂_i^λ) + cross.
    Sum: 𝔪(W) = Σ_λ w_λ · 𝔪^λ(W) with w_λ = d_q(λ)²/[n]_q!.
    Binding: B = E_0 · (𝔪_free − 𝔪_atom), E_0 = 938.272 / m_proton_tower.
    """
    from hecke_characters import dim_q as _dim_q
    A = Z + N
    if A < 1:
        return {"status": "trivial"}
    n_strands = 3 * A
    nfac = qfac(n_strands)
    m_atom_total = 0.0
    m_free_total = 0.0
    for shape in partitions_of(n_strands):
        dq = _dim_q(shape)
        if dq == 0:
            continue
        w_lam = (dq * dq) / nfac
        V_a = per_irrep_V_hat(Z, N, shape, include_inter=True,
                                m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
        V_f = per_irrep_V_hat(Z, N, shape, include_inter=False,
                                m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
        if not V_a or not V_f:
            continue
        m_a = canonical_tower_mass(V_a, pair_mode=pair_mode, term=term)
        m_f = canonical_tower_mass(V_f, pair_mode=pair_mode, term=term)
        m_atom_total += w_lam * m_a["total"]
        m_free_total += w_lam * m_f["total"]
    _save_mpm_disk(n_strands)
    # Calibrate E_0 via proton tower (A=1, n=3) using same pipeline
    if E_0 is None:
        E_0 = _calibrate_E0_per_irrep(pair_mode=pair_mode)
    B = E_0 * (m_free_total - m_atom_total)
    return {
        "Z": Z, "N": N, "A": A,
        "m_atom_per_irrep_total": m_atom_total,
        "m_free_per_irrep_total": m_free_total,
        "E_0_MeV_per_cat": E_0,
        "B_MeV": B,
        "pair_mode": pair_mode,
    }


_E0_PI_CACHE: dict[str, float] = {}


def _calibrate_E0_per_irrep(pair_mode: str = "full") -> float:
    """E_0 via proton tower in per-irrep formulation."""
    if pair_mode in _E0_PI_CACHE:
        return _E0_PI_CACHE[pair_mode]
    # MASS context (proton absolute vs M_P_MEV) even though it reuses the
    # binding_* entry point, so it pins term="phi_q" per `_li_2_q_util`'s rule.
    r = binding_per_irrep_tower(1, 0, E_0=1.0, pair_mode=pair_mode,
                                 term="phi_q")
    m_p = r["m_free_per_irrep_total"]  # A=1 has no atom (no inter)
    if m_p <= 0 or not math.isfinite(m_p):
        return 1.0
    # NOTE: alt-calibration (diagnostic per-irrep variant). CAL-3
    # canonical E_0 is `hecke_core.E_0_CALIBRATION_MEV` = Q_β(n).
    E_0 = float(M_P_MEV) / m_p
    _E0_PI_CACHE[pair_mode] = E_0
    return E_0


def binding_canonical_tower(Z: int, N: int, *, m_pp=1, m_pn=1, m_nn=1,
                              E_0: float | None = None,
                              pair_mode: str = "full",
                              verbose: bool = False,
                           term: str = "tower_term") -> dict:
    """Canonical-with-proper-tower binding.

    V̂_i canonical (JM eigenvalue averages) fed into prop's Φ_q tower.
    Calibrated against proton-tower mass (analogous to H_3 tower's
    E_0 = 938.272 / m_proton_tower); E_0 auto-computed if not passed.
    """
    A = Z + N
    if A < 1:
        return {"status": "trivial"}
    if E_0 is None:
        E_0 = calibrate_E0_tower(pair_mode=pair_mode)
    V_atom = per_gen_V_hat_canonical(
        Z, N, include_inter=True, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
    V_free = per_gen_V_hat_canonical(
        Z, N, include_inter=False, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
    if verbose:
        print(f"  V_atom: {[f'{v:+.4f}' for v in V_atom]}")
        print(f"  V_free: {[f'{v:+.4f}' for v in V_free]}")
    m_a = canonical_tower_mass(V_atom, pair_mode=pair_mode, term=term)
    m_f = canonical_tower_mass(V_free, pair_mode=pair_mode, term=term)
    B = E_0 * (m_f["total"] - m_a["total"])
    return {
        "Z": Z, "N": N, "A": A,
        "m_atom": m_a, "m_free": m_f,
        "V_atom": V_atom, "V_free": V_free,
        "B_MeV": B, "E_0_MeV_per_cat": E_0,
        "pair_mode": pair_mode,
    }


# ── CLI ─────────────────────────────────────────────────────

if __name__ == "__main__":
    ATOMS = [
        ("D",    1, 1,  2.22452),
        ("T",    1, 2,  8.481821),
        ("3He",  2, 1,  7.71804),
        ("4He",  2, 2, 28.295674),
    ]
    print("=" * 100)
    print("CANONICAL-WITH-PROPER-TOWER: JM-based V̂ + Φ_q tower "
          "(prop:mass-endomorphism-tower)")
    print(f"q₀ = {Q0}, E_0 calibrated via proton tower (MeV/cat unit)")
    print("V̂_i = Plancherel-averaged JM eigenvalue at position i+1, "
          "weighted by crossing factors")
    print("=" * 100)
    results = []
    for binder_name, binder_fn in [("per_irrep_tower (new, rigorous)",
                                      binding_per_irrep_tower),
                                     ("canonical_tower (provisional)",
                                      binding_canonical_tower)]:
        for pair_mode in ["adjacent", "full"]:
            print(f"\n-- {binder_name} | pair_mode: {pair_mode} --")
            print(f"  {'Atom':>6} {'A':>3} {'B_AME':>8} "
                  f"{'B_pred':>10} {'|Δm/m|%':>10}")
            print("  " + "-" * 60)
            for name, Z, N, B_AME in ATOMS:
                A = Z + N
                try:
                    r = binder_fn(Z, N, pair_mode=pair_mode)
                    dm = (abs(r["B_MeV"] - B_AME) / (A * float(M_P_MEV)) * 100
                           if math.isfinite(r["B_MeV"]) else float("nan"))
                    print(f"  {name:>6} {A:>3} {B_AME:>8.3f} "
                          f"{r['B_MeV']:>+10.4f} {dm:>9.4f}%")
                    results.append({**r, "atom": name,
                                     "binder": binder_name,
                                     "B_AME_MeV": B_AME,
                                     "delta_m_over_m_pct": dm})
                except Exception as e:
                    print(f"  {name:>6} ERR: {type(e).__name__}: "
                          f"{str(e)[:60]}")

    witness = {
        "computation": "canonical-with-proper-tower",
        "description": (
            "Canonical-with-proper-tower binding: per-generator V̂_i "
            "computed via Jucys-Murphy eigenvalue Plancherel averages "
            "(no H_3 shortcut), fed into the Φ_q tower formula of "
            "prop:mass-endomorphism-tower.  Single jet level; "
            "multi-level extension requires Kähler-differential "
            "propagation (open).  pair_mode ∈ {adjacent, full} "
            "toggles the audit-flagged adjacent-only restriction."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q0": Q0,
            "E_0_calibration": "proton-tower (m_p_CODATA / m_proton_tower)",
            "note": (
                "per-result E_0_MeV_per_cat values are in `results[]`; "
                "this module does NOT use the β-decay Q-value 0.78233341 "
                "MeV as E_0."
            ),
        },
        "results": results,
    }
    out = Path(__file__).parent / "canonical-with-proper-tower.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
