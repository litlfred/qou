"""The 4He all-pairs word of ../he4_gg_all_pairs, rebuilt for the TL engines.

Same placement rule (bond (i,j) after block max-j-so-far), same transport T_ij
(sigma_{3i+2} .. sigma_{3j-2} up, inverses down for "over"; swapped for "under"),
bond G^3 = (sigma_{3j-1} sigma_{3j}^-1)^3, or its mirror (sigma_{3j-1}^-1 sigma_{3j})^3.
"""
from __future__ import annotations

ROUTES_HE4 = {
    "D+D pairing a": [(0, 2), (1, 3), (0, 1), (2, 3), (1, 2), (0, 3)],
    "D+D pairing b": [(1, 2), (0, 3), (0, 1), (2, 3), (0, 2), (1, 3)],
    "3H+p": [(1, 2), (2, 3), (1, 3), (0, 1), (0, 2), (0, 3)],
    "3He+n": [(0, 1), (1, 2), (0, 2), (2, 3), (1, 3), (0, 3)],
}


def tG3(R, i, j, variant, mirror):
    gens = list(range(3 * i + 2, 3 * j - 1))
    up, dn = (R.S, R.I) if variant == "over" else (R.I, R.S)
    return [up(g) for g in gens] + R.V3(3 * j - 1, mirror) + [dn(g) for g in reversed(gens)]


def build(R, blocks, bonds, variant, mirror=False):
    A = len(blocks)
    after = {k: [] for k in range(A)}
    J = 0
    for i, j in bonds:
        J = max(J, j)
        after[J] += tG3(R, i, j, variant, mirror)
    w = []
    for k in range(A):
        w += [(a, b, g + 3 * k) for a, b, g in blocks[k]] + after[k]
    return w


def rest_after_N0(w, n0):
    """Drop block 0 (towerTr_disjoint: it sits in H_2, everything else uses sigma_{>=2})."""
    rest = [(a, b, g - 2) for a, b, g in w[n0:]]
    assert min(g for _, _, g in rest) >= 0
    return rest


def conv_word(R, Nk, k, variant="over", mirror=False):
    """rho_k word: k external strands each bonded to the nucleon on strands k..k+2."""
    w = []
    for s in range(k - 1, -1, -1):
        gens = list(range(s, k - 1))
        up, dn = (R.S, R.I) if variant == "over" else (R.I, R.S)
        w += [up(g) for g in gens] + R.V3(k - 1, mirror) + [dn(g) for g in reversed(gens)]
    return w + [(a, b, g + k) for a, b, g in Nk]
