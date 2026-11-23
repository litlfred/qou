#!/usr/bin/env python3
"""order_conjugation_probe.py: is nucleon order an independent input? (issue #8960)

Owner, 2026-11-21: "P-n-p-n seems chosen, not derived" / "Order is from GB
reduction?"; card choice "1+2 now, then 3". This is step 2.

Claim tested. Swapping neighbouring nucleons k, k+1 is conjugation by the cable
crossing P_k = swapWord k (QOU/Mass/BlockRelabelConjugation.lean, permutation
level, sorry-free). If P_k moves each nucleon word rigidly to its new block
(the braid-level identity P_k sigma_{3k+a} P_k^-1 = sigma_{3k+3+a}, a < 2, plus
fixing far letters), then the relabelled atom word is P_k W P_k^-1 and its
Markov trace equals tr(W). The bonds go along as P_k b P_k^-1, which joins
strands that are no longer neighbours.

Checks, all on the production letters of `atom_braid_word_3A` (the superseded
single-crossing bond letters; this probe asks about ORDER, not about which
bond letter is right):
  1. braid identity, per letter, in every irrep of H_9: chi_lam(P s_g P^-1 X)
     against chi_lam(s_{g'} X) for X in a set of test words;
  2. relabelled word W' = [nucleon words at their new blocks] + [P b P^-1 per
     bond] against W, every chi_lam;
  3. the naive chain in the new order (neighbour bond letters re-attached to
     the new neighbours), reported for contrast. Nothing is selected.
Precision: mpmath at the producer dps, letters exactly as production builds them.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parents[1]
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
import _path_bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
DPS = 50
import mpmath as mp  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from chi_general_word import chi_all_lambda_any  # noqa: E402
from tr_m_atom_via_transfer import _trM  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_MP as Q0, Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

T0 = time.time()


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


ONE, ZERO = mp.mpf(1), mp.mpf(0)
Q = mp.mpf(Q_50_DIGIT_STR)
H = Q - 1 / Q


def pos(g):
    return (ONE, ZERO, g)


def inv(g):
    return (ONE, -H, g)  # sigma^-1 = sigma - h


def swap_word(k):
    """swapWord k of BlockRelabelConjugation.lean, positive crossings."""
    b = 3 * k
    return [pos(g) for g in (b + 2, b + 1, b, b + 3, b + 2, b + 1, b + 4, b + 3, b + 2)]


def swap_inv(k):
    return [inv(g) for (_, _, g) in reversed(swap_word(k))]


def conj(k, word):
    return swap_word(k) + list(word) + swap_inv(k)


def chis(word, n):
    return chi_all_lambda_any(word, n, dps=DPS)


def worst_gap(a, b):
    return max(abs(mp.mpf(a[l]) - mp.mpf(b[l])) for l in a)


def split_atom(Z, N):
    """Per-block nucleon words and the bond letters of the production word."""
    A = Z + N
    free = list(atom_braid_word_3A(Z, N, include_inter=False))
    atom = list(atom_braid_word_3A(Z, N, include_inter=True))
    per = len(free) // A
    blocks = [free[k * per:(k + 1) * per] for k in range(A)]
    bonds, fi = [], 0
    for L in atom:
        if fi < len(free) and L == free[fi]:
            fi += 1
        else:
            bonds.append(L)
    return blocks, bonds, atom


def shift(word, d):
    return [(c, e, g + d) for (c, e, g) in word]


def main():
    mp.mp.dps = DPS + 10
    n = 9
    y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, Q0).items()}
    out = {"braid_identity": [], "atoms": []}

    # 1. braid identity per letter, k = 0 (blocks 0,1) and k = 1 (blocks 1,2).
    tests = [[], [pos(2)], [pos(5), inv(1)], [pos(0), pos(4), inv(7)], [pos(3), pos(6), pos(2)]]
    for k in (0, 1):
        b = 3 * k
        cases = [(b, b + 3), (b + 1, b + 4), (b + 3, b), (b + 4, b + 1)]
        cases += [(g, g) for g in range(n - 1) if g < b - 1 or g > b + 6]
        for g, g2 in cases:
            gap = max(worst_gap(chis(conj(k, [pos(g)]) + X, n), chis([pos(g2)] + X, n)) for X in tests)
            out["braid_identity"].append({"k": k, "g": g, "image": g2, "worst_chi_gap": mp.nstr(gap, 5)})
            log(f"  P_{k} s_{g} P_{k}^-1 vs s_{g2}: worst chi gap {mp.nstr(gap, 5)}")

    # 2 and 3. relabelled atoms.
    for (Z, N, name) in [(1, 2, "3H"), (2, 1, "3He")]:
        blocks, bonds, W = split_atom(Z, N)
        kinds = ["p"] * Z + ["n"] * N
        tW = _trM(chis(W, n), y)
        for k in (0, 1):
            new_kinds = kinds[:]
            new_kinds[k], new_kinds[k + 1] = kinds[k + 1], kinds[k]
            # nucleon words at their new blocks
            moved = []
            for m in range(3):
                d = 3 if m == k else (-3 if m == k + 1 else 0)
                moved += shift(blocks[m], d)
            Wp = moved + [w for L in bonds for w in conj(k, [L])]
            cW, cWp, cPWP = chis(W, n), chis(Wp, n), chis(conj(k, W), n)
            g_rel = worst_gap(cW, cWp)
            g_conj = worst_gap(cW, cPWP)
            # 3. naive chain: new order, bond letters re-attached to new neighbours
            new_blocks = [None] * 3
            for m in range(3):
                tgt = k + 1 if m == k else (k if m == k + 1 else m)
                new_blocks[tgt] = shift(blocks[m], 3 * (tgt - m))
            letter = {}
            for i, L in enumerate(bonds):
                letter["".join(sorted(kinds[i] + kinds[i + 1], reverse=True))] = L
            naive = []
            for m in range(3):
                naive += new_blocks[m]
                if m < 2:
                    c, e, _ = letter["".join(sorted(new_kinds[m] + new_kinds[m + 1], reverse=True))]
                    naive.append((c, e, 3 * m + 2))
            t_naive = _trM(chis(naive, n), y)
            row = {"atom": name, "order": "".join(kinds), "swap_k": k, "new_order": "".join(new_kinds),
                   "tr_W": mp.nstr(tW, 40),
                   "relabelled_vs_W_worst_chi_gap": mp.nstr(g_rel, 5),
                   "PWP_vs_W_worst_chi_gap": mp.nstr(g_conj, 5),
                   "naive_chain_new_order_tr": mp.nstr(t_naive, 40),
                   "naive_minus_W_tr": mp.nstr(t_naive - tW, 10)}
            out["atoms"].append(row)
            log(f"  {name} {''.join(kinds)} -> {''.join(new_kinds)}: relabelled vs W {mp.nstr(g_rel, 5)}, "
                f"PWP vs W {mp.nstr(g_conj, 5)}, naive chain tr {mp.nstr(t_naive, 12)} vs {mp.nstr(tW, 12)}")

    worst_id = max(mp.mpf(r["worst_chi_gap"]) for r in out["braid_identity"])
    worst_rel = max(mp.mpf(r["relabelled_vs_W_worst_chi_gap"]) for r in out["atoms"])
    wb = WitnessBuilder("he4-order-conjugation", engine="mpmath (chi_general_word)", output_dir=HERE)
    wb.set_description(
        "PROBE (issue #8960, step 2). Tests whether nucleon order is an independent input: "
        "swapping neighbouring nucleons is conjugation by the cable crossing P_k "
        "(BlockRelabelConjugation.lean). Checks the braid identity P s_g P^-1 = s_{g'} per letter "
        "in every irrep of H_9, and that the relabelled 3H/3He word equals W in every character. "
        "Bond letters are the superseded single-crossing production letters; the question is "
        "order only. The naive new-order chain is reported for contrast; nothing is selected.")
    wb.add_data("braid_identity", out["braid_identity"])
    wb.add_data("atoms", out["atoms"])
    wb.add_assertion("cable_crossing_moves_letters", computed=worst_id, expected=0,
                     tolerance=mp.mpf("1e-50"))
    wb.add_assertion("relabelled_word_equals_W_in_every_character", computed=worst_rel, expected=0,
                     tolerance=mp.mpf("1e-50"))
    wb.save({"q0Anchor": "proton"})
    log("witness written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
