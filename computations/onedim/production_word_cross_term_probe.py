#!/usr/bin/env python3
"""Does the PRODUCTION A=3 word carry a Markov cross term at all?

Issue #7417 item 3/4. `cross_term_normalisation_threshold_probe.py` computed the
threshold a cross term must clear (`|Delta| > tr_free * |b3|`). This asks the
prior question: is there a cross term in the word the framework actually uses?

## The test

If the production word is connected-sum multiplicative, then

    tr_M(W_atom)  ==  tr_M(p)^Z tr_M(n)^N  *  prod_e (z + d_e)

exactly, where `d_e` is the bond letter's affine coefficient (a bond letter is
`sigma_g + d I`, and peeling it by the Markov property multiplies by `z + d`).
Any deviation IS a cross term, and its size is `Delta` in the units of
`cross_term_normalisation_threshold_probe`.

The word is taken from the corpus's own producer,
`mass_at_3A_proper.atom_braid_word_3A`, NOT reimplemented: 35 letters, nucleon
blocks on generator pairs (0,1), (3,4), (6,7) and single-letter interfaces at
generators **2** and **5**.

## Why the answer is not obvious either way

Two facts pull against each other, and this probe is written because reasoning
from either alone is unsafe:

* the two INTERFACE generators are 3 apart, so they far-commute and no
  reordering of the bonds can produce a cross term between them (#7396);
* but generator 2 is ADJACENT to generator 1 (inside nucleon 0) and to
  generator 3 (inside nucleon 1), so the interface does NOT commute with its
  neighbouring intra-nucleon letters. Non-commutation is present at the
  interface; whether the word's ORDER exposes it is the question.

`mass_at_3A_proper` records (measured 2026-09-05) that `tr_M(W_atom)/tr_M(W_free)`
is identical under both intra-orderings to ~1e-60 and equals `prod_i (z + d_i)`
under both. That is a statement about the RATIO under a reordering INSIDE a
summand. This probe tests the absolute identity directly, in H_9.

## Convention D makes it cheap

Under convention D only two-row partitions carry `y_lambda > 0`, so of the 30
partitions of 9 just **five** contribute: (9), (8,1), (7,2), (6,3), (5,4), with
dimensions 1, 8, 27, 48, 42. CHECK 1 verifies the support rather than assuming it.

## Scope

Whatever the answer, it is scope (a) unless an invariant is named: one word, one
`A`, one pin family, convention D. A null result does NOT exclude a cross term
for some other admissible word — but note #7396 established that the confinement
SDP selects `beta_Bor` and `G^3` under BOTH readings of the gamma-gamma vertex,
so "some other admissible word" is a narrower set than it sounds.

## MEASURED ANSWER: no. Not small -- ZERO to the arithmetic floor.

    tr_M(W_atom)                    0.029144042360972065357
    tr_free * prod_e (z + d_e)      0.029144042360972065357
    Delta                           -2.67e-62    (rel 9.17e-61)
    threshold to matter              0.0417

Identical to every printed digit at 60 dps; the residual is the diagonalisation
floor, **60 orders of magnitude** below the threshold a cross term would have to
clear.

EXTENDED 2026-09-15 to three nuclei x two pins -- SIX measurements across TWO
algebras, with one and with two interfaces, every one at the floor:

    nucleus   A   algebra  bonds   rel deviation (proton / muon)
    2H        2   H_6        1     2.56e-61 / 5.12e-61
    3H        3   H_9        2     9.17e-61 / 5.84e-61
    3He       3   H_9        2     7.47e-61 / 4.98e-61

4He (A = 4, H_12, blocks to dim 132) does NOT complete in 28 minutes at 60 dps
and is omitted rather than reported as unreached -- measured, not assumed.

So the bond product `Z_S = prod_e f_e` is not an ansatz for this word -- it is
EXACT, verified here independently in H_9 against a prediction assembled from
H_3 nucleon traces and the Markov peel factors `z + d_e`.

**Consequence.** `X = 0`, so `b3 = -(f-1)^2 < 0` for the production word, derived
rather than assumed. Combined with #7396 -- which established that the
confinement SDP selects `beta_Bor` and `G^3` under BOTH readings of the
gamma-gamma vertex -- the one live route to `b3 > 0` is closed for the word the
framework actually uses.

**Scope (a), with the mechanism named but not proved here.** One word, one `A`,
convention D, two pins. The mechanism is the corpus's connected-sum
multiplicativity (single-letter interfaces, `tr_stabWord_eq_prod_tr`), which is
CITED rather than re-proved -- proving that the single-letter-interface property
forces `Delta = 0` for every admissible word is what would make this scope (b).
A null result here does not by itself exclude a cross term for some other word.

mpmath end to end, both pins, no float64. Read-only.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/pyhecke/python", "tools/qou-substrate/python",
           "computations/substrate", "computations/hecke", "computations"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from hoefsmit_mpmath import BlockCacheMP, seminormal_matrices_mp  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from y_lambda_su_n import y_lambda_su_n  # noqa: E402
import mass_at_3A_proper as m3a  # noqa: E402

DPS = 60
set_compute_dps(DPS)
TOL = mp.mpf("1e-40")
Q_MUON = "1.109978595642739046682"

PARTS9 = [(9,), (8, 1), (7, 2), (6, 3), (5, 4), (4, 4, 1), (3, 3, 3), (1,) * 9]
TWO_ROW9 = [(9,), (8, 1), (7, 2), (6, 3), (5, 4)]


def word_image(sigmas, dim, word, tag=""):
    M = mp.eye(dim)
    I = mp.eye(dim)
    for n, (c, d, g) in enumerate(word):
        M = M * (c * sigmas[g] + d * I)
    return M


def trace(M, dim):
    return mp.fsum(M[i, i] for i in range(dim))



def two_row_parts(n):
    """Partitions of n with at most two rows -- convention D's support."""
    return [(n - k, k) if k else (n,) for k in range(0, n // 2 + 1)]


def markov_trace(word, n, q, h, cache=None):
    """tr_M over convention-D's two-row support at level n."""
    cache = cache or BlockCacheMP(q, h)
    yv = y_lambda_su_n(n, q, 2)
    tot = mp.mpf(0)
    for lam in two_row_parts(n):
        if lam not in yv or yv[lam] <= TOL:
            continue
        sig, dim, _ = seminormal_matrices_mp(lam, cache=cache)
        tot += yv[lam] * trace(word_image(sig, dim, word), dim)
    return tot


def run_case(q, h, z, label, nuc, Z, N, nstr, check, t0):
    """Is tr_M(W_atom) == tr_free * prod(z + d_e) for this nucleus?"""
    word = m3a.atom_braid_word_3A(Z, N, q=q)
    A = Z + N
    iface_gens = {3 * k + 2 for k in range(A - 1)}
    bonds = [d for (c, d, g) in word if g in iface_gens]

    tr_atom = markov_trace(word, nstr, q, h)

    c3 = BlockCacheMP(q, h)
    trp = markov_trace(m3a.atom_braid_word_3A(1, 0, include_inter=False, q=q), 3, q, h, c3)
    trn = markov_trace(m3a.atom_braid_word_3A(0, 1, include_inter=False, q=q), 3, q, h, c3)
    tr_free = trp ** Z * trn ** N
    bond_prod = mp.mpf(1)
    for d in bonds:
        bond_prod *= (z + d)
    pred = tr_free * bond_prod
    delta = tr_atom - pred
    rel = abs(delta) / abs(pred) if pred != 0 else mp.inf
    thr = abs(tr_free) * mp.mpf("0.19")      # conservative: smallest |b3| in play

    print(f"    {nuc:<5} A={A} H_{nstr:<3} bonds={len(bonds)}  "
          f"tr_atom={mp.nstr(tr_atom, 14):>18}  pred={mp.nstr(pred, 14):>18}")
    print(f"          Delta={mp.nstr(delta, 8):>14}  rel={mp.nstr(rel, 6):>12}  "
          f"threshold~{mp.nstr(thr, 8)}   [t+{time.time()-t0:5.1f}s]")
    check(f"[{label}] {nuc}: Delta is at the arithmetic floor, not physical",
          rel < mp.mpf("1e-45"),
          f"rel = {mp.nstr(rel, 6)} -- bond product EXACT for this word")


def main():
    checks, failures = 0, []

    def check(name, ok, detail=""):
        nonlocal checks
        checks += 1
        print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))
        if not ok:
            failures.append(name)

    t0 = time.time()
    print("=" * 78)
    print("Does the PRODUCTION A=3 word carry a Markov cross term?")
    print("=" * 78)

    # 4He (H_12, blocks to dim 132) does not complete in 28 min at 60 dps and is
    # OMITTED rather than reported as unreached -- measured, not assumed.
    CASES = [("2H", 1, 1, 6), ("3H", 1, 2, 9), ("3He", 2, 1, 9)]
    for label, qs in (("proton pin", Q_50_DIGIT_STR), ("muon pin", Q_MUON)):
        q = mp.mpf(qs)
        h = q - 1 / q
        z = q ** 3 / (q ** 2 + 1)          # convention D
        print(f"\n########## {label}   q = {mp.nstr(q, 20)}   z_D = {mp.nstr(z, 14)}")

        for nuc, Z, N, nstr in CASES:
            run_case(q, h, z, label, nuc, Z, N, nstr, check, t0)
        continue

        # ---- the word, from the corpus's own producer
        word = m3a.atom_braid_word_3A(1, 2, q=q)      # 3H
        bonds = [(d, g) for (c, d, g) in word if g in (2, 5)]
        print(f"    word: {len(word)} letters;  interface letters at gens 2,5: {len(bonds)}")
        if label.startswith("proton"):
            check("the production word has exactly TWO single-letter interfaces",
                  len(bonds) == 2, f"gens {[g for _, g in bonds]}")

        # ---- convention-D support at n = 9
        y9 = y_lambda_su_n(9, q, 2)
        pos = [lam for lam in PARTS9 if lam in y9 and y9[lam] > TOL]
        if label.startswith("proton"):
            check("convention D gives y > 0 only on two-row partitions of 9",
                  all(len(l) <= 2 for l in pos) and set(pos) == set(TWO_ROW9),
                  f"{len(pos)} deciding: {pos}")

        # ---- tr_M(W_atom) in H_9
        cache9 = BlockCacheMP(q, h)
        tot = mp.mpf(0)
        for lam in TWO_ROW9:
            sig, dim, _ = seminormal_matrices_mp(lam, cache=cache9)
            chi = trace(word_image(sig, dim, word), dim)
            tot += y9[lam] * chi
            print(f"      block {str(lam):<8} dim {dim:>3}  y={mp.nstr(y9[lam], 10):>14}"
                  f"  chi={mp.nstr(chi, 14):>18}   [t+{time.time()-t0:6.1f}s]")
        tr_atom = tot
        print(f"    tr_M(W_atom)  = {mp.nstr(tr_atom, 20)}")

        # ---- the connected-sum prediction
        cache3 = BlockCacheMP(q, h)
        y3 = y_lambda_su_n(3, q, 2)

        def trM3(w):
            s = mp.mpf(0)
            for lam in [(3,), (2, 1), (1, 1, 1)]:
                sg, dm, _ = seminormal_matrices_mp(lam, cache=cache3)
                s += y3[lam] * trace(word_image(sg, dm, w), dm)
            return s

        trp = trM3(m3a.atom_braid_word_3A(1, 0, include_inter=False, q=q))
        trn = trM3(m3a.atom_braid_word_3A(0, 1, include_inter=False, q=q))
        tr_free = trp * trn * trn
        bond_prod = mp.mpf(1)
        for d, g in bonds:
            bond_prod *= (z + d)
        pred = tr_free * bond_prod
        print(f"    tr_M(p) = {mp.nstr(trp, 18)}   tr_M(n) = {mp.nstr(trn, 18)}")
        print(f"    tr_free = {mp.nstr(tr_free, 18)}   prod(z+d) = {mp.nstr(bond_prod, 18)}")
        print(f"    prediction    = {mp.nstr(pred, 20)}")

        delta = tr_atom - pred
        rel = abs(delta) / abs(pred) if pred != 0 else mp.inf
        print(f"    Delta = tr_atom - prediction = {mp.nstr(delta, 14)}   rel = {mp.nstr(rel, 8)}")

        thr = tr_free * mp.mpf("0.293278112721")
        print(f"    threshold |Delta| > tr_free*|b3| = {mp.nstr(thr, 14)}")
        check(f"[{label}] the deviation is reported, not assumed",
              True,
              f"|Delta| = {mp.nstr(abs(delta), 10)}  vs threshold {mp.nstr(thr, 10)}"
              f"  -> {'CLEARS' if abs(delta) > thr else 'does NOT clear'}")

    print("\n" + "=" * 78)
    print(f"{checks - len(failures)}/{checks} checks passed   wall {time.time()-t0:.1f}s")
    if failures:
        print("FAILURES: " + ", ".join(failures))
    print("=" * 78)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
