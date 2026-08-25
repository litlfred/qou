#!/usr/bin/env python3
"""young_seminormal — local Hecke seminormal (Young's rule) at MPFR.

The LOCAL recoupling primitive for the scalable atom-config χ
(F-matrix step [a], audit docs/audits/2026-06-09-large-A-chi-bottleneck-
scaling-plan.md §8). Young's seminormal form IS the S_n recoupling /
F-matrix — applying it per generator (sparse, 2×2) lets a transfer
matrix build χ^λ without ever materialising the full d_λ Hoefsmit
matrix (the wall that makes char_fast / chi_q_atomic infeasible at A≥6).

Convention (reverse-engineered + verified against char_fast, which ≡
pyhecke_native): symmetric seminormal, σ_i² = (q−q⁻¹)σ_i + 1. For SYT t,
with δ = c(i+1) − c(i) (content difference of the boxes holding i, i+1):

  δ = +1 (same row):  σ_i v_t = q v_t
  δ = −1 (same col):  σ_i v_t = −q⁻¹ v_t
  |δ| ≥ 2:            on {v_t, v_u}, u = s_i·t (swap values i,i+1):
      diag_t = (q−q⁻¹)/(1 − q^{−2δ}),  diag_u = (q−q⁻¹) − diag_t,
      off    = sqrt(diag_t·diag_u + 1)   (symmetric; sign is a gauge,
               immaterial for the character / trace).

Validated: χ^λ via this rule ≡ char_fast (hence pyhecke_native) — see
`_self_test`. Characters are gauge-invariant, so the off-diagonal sign
convention does not matter for χ.

NO float64: all arithmetic is mpmath at the 50-dps floor.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys  # noqa: E402
from functools import lru_cache  # noqa: E402
from pathlib import Path  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402


@lru_cache(maxsize=64)
def _boxes(shape: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    """Row-major box coordinates (row, col) for a Young diagram."""
    return tuple((r, c) for r, row in enumerate(shape) for c in range(row))


@lru_cache(maxsize=64)
def standard_tableaux(shape: tuple[int, ...]) -> tuple[dict, ...]:
    """All SYT of `shape` as dicts {value: box_index} (row-major box
    index), in a deterministic order. Matches char_fast's basis labels.
    """
    boxes = _boxes(shape)
    n = len(boxes)
    # adjacency: which box indices are "fillable" given a set of filled ones
    # (a box is fillable if the box above and to the left are filled).
    above = {}
    left = {}
    pos = {b: i for i, b in enumerate(boxes)}
    for i, (r, c) in enumerate(boxes):
        above[i] = pos.get((r - 1, c))
        left[i] = pos.get((r, c - 1))

    results: list[dict] = []

    def rec(filled: frozenset, assign: dict, val: int):
        if val > n:
            results.append(dict(assign))
            return
        for i in range(n):
            if i in filled:
                continue
            if (above[i] is None or above[i] in filled) and \
               (left[i] is None or left[i] in filled):
                assign[val] = i
                rec(filled | {i}, assign, val + 1)
                del assign[val]

    rec(frozenset(), {}, 1)
    return tuple(results)


@lru_cache(maxsize=64)
def _content_by_index(shape: tuple[int, ...]) -> tuple[int, ...]:
    """content (col − row) per row-major box index."""
    return tuple(c - r for (r, c) in _boxes(shape))


def seminormal_sigma(shape: tuple[int, ...], i: int, q: "mp.mpf"):
    """ρ_shape(σ_i) as an mpmath matrix (1-based i), via Young's rule.

    Builds the FULL matrix — for VALIDATION on small shapes only. The
    scalable transfer matrix calls the local action, not this.
    """
    syts = standard_tableaux(shape)
    cont = _content_by_index(shape)
    dim = len(syts)
    index = {tuple(sorted(t.items())): k for k, t in enumerate(syts)}
    M = mp.matrix(dim, dim)
    qi = 1 / q
    for k, t in enumerate(syts):
        bi, bj = t[i], t[i + 1]
        delta = cont[bj] - cont[bi]
        if delta == 1:        # same row
            M[k, k] = q
        elif delta == -1:     # same column
            M[k, k] = -qi
        else:                 # 2x2 block with u = s_i t (NON-symmetric form)
            u = dict(t)
            u[i], u[i + 1] = t[i + 1], t[i]
            ku = index[tuple(sorted(u.items()))]
            if k < ku:        # set the 2x2 once, from the lower-index member
                diag_t = (q - qi) / (1 - q ** (-2 * delta))
                diag_u = (q - qi) - diag_t
                M[k, k] = diag_t
                M[ku, ku] = diag_u
                # Young's NON-symmetric seminormal: off-diagonals (1) and
                # (diag_t·diag_u + 1) so eigenvalues are q, −q⁻¹ (trace
                # q−q⁻¹, det −1) AND the braid relations hold (no sqrt /
                # sign ambiguity, unlike the symmetric form).
                M[k, ku] = mp.mpf(1)
                M[ku, k] = diag_t * diag_u + 1
            # if k > ku the block was already set when the partner (ku) was
            # processed; nothing to do.
    return M


def chi_young(shape: tuple[int, ...], word, q: "mp.mpf") -> "mp.mpf":
    """χ^shape(word) via local Young's rule (full matrix; validation use)."""
    syts = standard_tableaux(shape)
    dim = len(syts)
    M = mp.eye(dim)
    cache: dict[int, "mp.matrix"] = {}
    for (c, d, g) in word:
        gi = g + 1  # word gens are 0-based; seminormal_sigma is 1-based
        if gi not in cache:
            cache[gi] = seminormal_sigma(shape, gi, q)
        sg = cache[gi]
        F = mp.matrix(dim, dim)
        cc, dd = mp.mpf(c), mp.mpf(d)
        for a in range(dim):
            for b in range(dim):
                F[a, b] = cc * sg[a, b] + (dd if a == b else 0)
        M = M * F
    return mp.fsum(M[a, a] for a in range(dim))


def _self_test() -> int:
    """Validate χ via Young's rule ≡ char_fast (≡ pyhecke_native), all λ⊢6."""
    from char_fast import chi_lambda_fast_mp
    from lr_coefficients import partitions_of
    from mass_at_3A_proper import atom_braid_word_3A
    from q_parameter import Q_50_DIGIT_STR
    set_compute_dps()
    q = mp.mpf(Q_50_DIGIT_STR)
    word = atom_braid_word_3A(1, 1)  # deuteron H_6 word (color-weighted pn)
    max_rel = mp.mpf(0)
    for lam in partitions_of(6):
        lam = tuple(lam)
        cy = chi_young(lam, word, q)
        cf = chi_lambda_fast_mp(lam, word, q).real
        rel = abs(cy - cf) / (1 + abs(cf))  # abs-with-floor (χ can be ~0)
        max_rel = max(max_rel, rel)
    ok = max_rel < mp.mpf(10) ** -12
    print(f"  young_seminormal χ ≡ char_fast on deuteron word (all λ⊢6): "
          f"max_rel={mp.nstr(max_rel, 4)}  {'OK' if ok else 'MISMATCH'}")
    # also a non-atom braid word, all λ⊢6, to exercise σ_i⁻¹ / averaged
    h = float(q - 1 / q)
    probe = [(1.0, 0.0, 0), (1.0, -h, 1), (1.0, -h / 2, 2),
             (1.0, 0.0, 3), (1.0, -h, 4)]
    max_rel2 = mp.mpf(0)
    for lam in partitions_of(6):
        lam = tuple(lam)
        cyp = chi_young(lam, probe, q); cfp = chi_lambda_fast_mp(lam, probe, q).real
        rel = abs(cyp - cfp) / (1 + abs(cfp))
        max_rel2 = max(max_rel2, rel)
    ok2 = max_rel2 < mp.mpf(10) ** -12
    print(f"  young_seminormal χ ≡ char_fast on mixed σ/σ⁻¹/avg word: "
          f"max_rel={mp.nstr(max_rel2, 4)}  {'OK' if ok2 else 'MISMATCH'}")
    return 0 if (ok and ok2) else 1


if __name__ == "__main__":
    sys.exit(_self_test())
