#!/usr/bin/env python3
# polynomial_q_not_applicable: mpmath evaluation at q0 plus exact partition sums; no symbolic-q output.
"""C3 probe: the 'quenched' bond functional  tr_z(log|L|)  in place of  log tr_z(L).

Context (bean qou-slz5, owner 2026-10-10: "explore C, leave as open problem").
The live binding law is  B = -alpha * log(tr_z(W_atom)/tr_z(W_free)) = -alpha * sum_k log(z + d_k)
(bond letter L_k = sigma + d_k on a generator used once).  On every faithful positive Markov
trace, z in [0, h] with h = q - 1/q, the nn factor z - h is <= 0, so that law is not real.

C3 replaces log-of-trace by trace-of-log, block by block:

    B_C3 = -alpha * sum_lambda mu_lambda * (1/f^lambda) * log|det rho_lambda(W_atom) / det rho_lambda(W_free)|.

Because det is multiplicative for ANY word (not only a chain), and each bond letter is invertible
or at least diagonalisable with eigenvalues  q + d  and  -1/q + d, this collapses per bond to

    g(d; z) = p_plus * log|q + d| + p_minus * log|1/q - d|,
    p_plus = (z + 1/q)/(q + 1/q),   p_minus = 1 - p_plus,

where p_plus is the trace-weighted fraction of the q-eigenspace of sigma_i (fixed by tr(1) = 1 and
tr(sigma_i) = z).  B_C3 = -alpha * sum_k g(d_k; z).

This script (no float64; mpmath throughout):
  1. derives g in closed form and CHECKS it against an explicit block sum over all lambda |- n,
     n = 3..7, using the Ocneanu closed-form weights (QOU.SchurWeyl.ocneanuWeight; proved to be the
     z-Markov trace at general n in FullTowerTraceWindow.lean) and the eigenvalue multiplicities
     m_pm = (f +- chi_cl(transposition))/2, chi_cl/f = 2*sum(contents)/(n(n-1));
  2. tabulates the per-bond C3 binding for pp, nn, pn (colour-weighted and colour-blind) across the
     faithful window and at z_D for comparison;
  3. records structural facts that hold exactly:  g_pp = -g_nn  for every z  (sigma and sigma^-1 have
     reciprocal eigenvalues),  and  g_pp = g_nn = 0  exactly at the self-dual point z = h/2.

Scope (a): this measures a candidate functional.  It is not adopted, and nothing here is compared
with AME data.  Witness: c3-quenched-bond-logdet-probe.witness.json
"""
from __future__ import annotations

import sys
import time
from itertools import product
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))

from q_parameter import Q_MP  # noqa: E402  proton-pinned 50-digit q0
from _li_2_q_util import flavor_split_leading  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 70


def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def cells(lam):
    return [(i, j) for i, r in enumerate(lam) for j in range(r)]


def hook(lam, i, j):
    conj = [sum(1 for r in lam if r > c) for c in range(lam[0])]
    return (lam[i] - j) + (conj[j] - i) - 1


def num_syt(lam):
    n = sum(lam)
    p = mp.factorial(n)
    for (i, j) in cells(lam):
        p /= hook(lam, i, j)
    return int(mp.nint(p))


def ocneanu_weight(q, z, lam):
    """Per-character weight w_lambda (sum_lambda f^lambda w_lambda = 1), OcneanuWeight.lean."""
    num = mp.mpf(1)
    den = mp.mpf(1)
    for (i, j) in cells(lam):
        num *= q ** (2 * i) * (q ** 2 - 1 - q * z) + q ** (2 * j + 1) * z
        den *= q ** (2 * hook(lam, i, j)) - 1
    return num / den


def g_closed(q, z, d):
    pp = (z + 1 / q) / (q + 1 / q)
    return pp * mp.log(abs(q + d)) + (1 - pp) * mp.log(abs(1 / q - d))


def g_blocksum(q, z, d, n):
    tot = mp.mpf(0)
    norm = mp.mpf(0)
    trsig = mp.mpf(0)
    for lam in partitions(n):
        f = num_syt(lam)
        csum = sum(j - i for (i, j) in cells(lam))
        chi_cl = mp.mpf(f) * 2 * csum / (n * (n - 1))
        mplus = (f + chi_cl) / 2
        mminus = (f - chi_cl) / 2
        w = ocneanu_weight(q, z, lam)
        norm += f * w
        trsig += w * (q * mplus - mminus / q)
        tot += w * (mplus * mp.log(abs(q + d)) + mminus * mp.log(abs(1 / q - d)))
    return tot, norm, trsig


def main() -> int:
    t0 = time.time()
    q = mp.mpf(str(Q_MP))
    h = q - 1 / q
    delta = flavor_split_leading(q)
    zD = q ** 3 / (q ** 2 + 1)
    letters = {
        "pp (sigma)": mp.mpf(0),
        "nn (sigma^-1)": -h,
        "pn colour-weighted": -h * (mp.mpf(1) / 2 - delta / 4),
        "pn colour-blind": -h / 2,
    }
    zs = {"0 (Molien)": mp.mpf(0), "h/4": h / 4, "h/2 (self-dual)": h / 2,
          "3h/4": 3 * h / 4, "h (edge)": h, "z_D (outside, comparison)": zD}

    # 1. closed form vs explicit block sums
    worst = mp.mpf(0)
    worst_norm = mp.mpf(0)
    worst_tr = mp.mpf(0)
    for (zn, z), (ln, d), n in product(zs.items(), letters.items(), range(3, 8)):
        if zn.startswith("z_D"):
            continue
        tot, norm, trsig = g_blocksum(q, z, d, n)
        worst = max(worst, abs(tot - g_closed(q, z, d)))
        worst_norm = max(worst_norm, abs(norm - 1))
        worst_tr = max(worst_tr, abs(trsig - z))

    # 2. table
    rows = []
    for zn, z in zs.items():
        row = {"z": zn, "z_value": mp.nstr(z, 15)}
        for ln, d in letters.items():
            row[ln] = mp.nstr(-g_closed(q, z, d), 15)  # binding per bond, units of alpha
        rows.append(row)

    # 3. structural facts
    anti = max(abs(g_closed(q, z, 0) + g_closed(q, z, -h)) for z in zs.values())
    self_dual = max(abs(g_closed(q, h / 2, 0)), abs(g_closed(q, h / 2, -h)))
    pn_cw_mid = -g_closed(q, h / 2, letters["pn colour-weighted"])

    w = WitnessBuilder("c3-quenched-bond-logdet-probe", engine="mpmath", start_time=t0)
    w.set_description(
        "C3 candidate binding functional: trace-of-log per Wedderburn block, "
        "B_C3 = -alpha * sum_k [p+ log|q+d_k| + p- log|1/q-d_k|], p+ = (z+1/q)/(q+1/q). "
        "Closed form checked against explicit Ocneanu block sums n=3..7. Scope (a): "
        "candidate measured, not adopted, no AME comparison.")
    w.add_parameter("q0", mp.nstr(q, 20))
    w.add_parameter("h", mp.nstr(h, 20))
    w.add_parameter("delta", mp.nstr(delta, 20))
    w.add_parameter("compute_dps", mp.mp.dps)
    w.add_data("binding_per_bond_units_of_alpha", rows)
    w.add_data("closed_vs_blocksum_max_abs_diff", mp.nstr(worst, 5))
    w.add_data("pn_colour_weighted_at_self_dual", mp.nstr(pn_cw_mid, 15))
    w.add_assertion(name="closed_form_matches_block_sum_n3_to_7",
                    computed=1 if worst < mp.mpf(10) ** -55 else 0, expected=1, tolerance=0,
                    source=f"max |closed - blocksum| = {mp.nstr(worst, 5)}")
    w.add_assertion(name="ocneanu_weights_normalised", computed=1 if worst_norm < mp.mpf(10) ** -55 else 0,
                    expected=1, tolerance=0, source=f"max |sum f w - 1| = {mp.nstr(worst_norm, 5)}")
    w.add_assertion(name="ocneanu_weights_give_tr_sigma_z", computed=1 if worst_tr < mp.mpf(10) ** -55 else 0,
                    expected=1, tolerance=0, source=f"max |tr(sigma) - z| = {mp.nstr(worst_tr, 5)}")
    w.add_assertion(name="pp_equals_minus_nn_every_z", computed=1 if anti < mp.mpf(10) ** -60 else 0,
                    expected=1, tolerance=0, source=f"max |g_pp + g_nn| = {mp.nstr(anti, 5)}")
    w.add_assertion(name="pp_nn_vanish_at_self_dual", computed=1 if self_dual < mp.mpf(10) ** -60 else 0,
                    expected=1, tolerance=0, source=f"max |g| at z=h/2 = {mp.nstr(self_dual, 5)}")
    out = w.save()

    print("C3 binding per bond (units of alpha), B = -g:")
    for r in rows:
        print(" ", r)
    print("closed vs blocksum:", mp.nstr(worst, 5), " norm:", mp.nstr(worst_norm, 5),
          " tr:", mp.nstr(worst_tr, 5))
    print("|g_pp + g_nn| max:", mp.nstr(anti, 5), "  self-dual |g|:", mp.nstr(self_dual, 5))
    print("pn colour-weighted at h/2:", mp.nstr(pn_cw_mid, 15))
    print("witness:", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
