#!/usr/bin/env python3
"""Cross-check the QOU trefoil + figure-eight colored-Jones towers against
Masbaum's PUBLISHED formulas (bean xcyc, re-scoped).

Source (owner-uploaded, arxiv egress blocked in sandbox):
  G. Masbaum, "Skein-theoretical derivation of some formulas of Habiro",
  Algebr. Geom. Topol. 3 (2003) 537-556, arXiv:math/0306345.

IMPORTANT provenance correction: this paper is about TWIST KNOTS K_p (Fig 3;
K_1 = left-handed trefoil, K_{-1} = figure eight), NOT the Borromean rings.
The Borromean rings are not twist knots, so math/0306345 carries no Borromean
formula — the earlier "Masbaum Borromean c_k" framing was a mis-attribution
(the actual simple-links reference is Habiro [H1], RIMS Kokyuroku 1172,
unavailable here). What this paper DOES give is an independent published
cross-check for the two QOU corpus knots.

Masbaum conventions (his p.539, Thm 5.1, Rmk 5.2):
  a = A^2,  {n} = a^n - a^{-n},  q = a^2 = A^4,  (x)_n = prod_{i<n}(1 - x q^i).
  J'_{K_p}(N) = sum_n f_{K_p,n} {N-n}{N-n+1}...{N+n}/{N}
             = sum_n ftilde_{K_p,n} (q^{1-N})_n (q^{1+N})_n,
      ftilde_{K_p,n} = (-1)^n q^{-n(n+1)/2} f_{K_p,n}.
  Left trefoil  K_1:   f_{K_1,n} = (-1)^n a^{n(n+3)},  ftilde = q^n.
  Figure eight K_{-1}: f_{K_{-1},n} = 1,               ftilde = (-1)^n q^{-n(n+1)/2}.

Checks (numeric, mpmath 40 dps, at several random/real q on |q|!=1):

  [FE]  the corpus/Lean 4_1 Habiro double-Pochhammer tower
        (QOU.BraidKnot.HabiroNewtonLadder.coloredJones41, mirrored here in
        q-notation) == Masbaum's J'_{K_{-1}}(N).  (Re-confirms the 4_1
        ladder of PR #3263 against the literature; all cyclotomic
        coefficients 1.)
  [TR]  the corpus/Lean trefoil Rosso-Jones tower
        (QOU.BraidKnot.AJTrefoil.coloredJonesTrefoil, w with q=w^4,
        mirrored here) == Masbaum's J'_{K_1}(N) with q_Masbaum = q_corpus.
        This upgrades the trefoil tower from a self-anchored convention to
        a literature match (Masbaum's left-handed K_1).

Both towers are the REDUCED (unknot-normalized) J'.  Audit-only.
"""
from __future__ import annotations

import sys
import time

import mpmath as mp
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def qpoch(x, q, n):
    """(x)_n = prod_{i=0}^{n-1} (1 - x q^i)."""
    out = mp.mpf(1)
    for i in range(n):
        out *= 1 - x * q**i
    return out


# ---- Masbaum published towers (q-form, Rmk 5.2) ------------------------
def masbaum_fig8(q, N):
    # ftilde_{K_{-1},n} = (-1)^n q^{-n(n+1)/2}
    return mp.fsum((-1) ** n * q ** (mp.mpf(-n * (n + 1)) / 2)
                   * qpoch(q ** (1 - N), q, n) * qpoch(q ** (1 + N), q, n)
                   for n in range(N))


def masbaum_trefoil(q, N):
    # ftilde_{K_1,n} = q^n  (left-handed trefoil)
    return mp.fsum(q ** n * qpoch(q ** (1 - N), q, n) * qpoch(q ** (1 + N), q, n)
                   for n in range(N))


# ---- QOU corpus towers (mirrors of the Lean defs), reduced J' ----------
def qint_w(v, k):
    return (v ** k - v ** (-k)) / (v - 1 / v)


def corpus_fig8(q, N):
    # coloredJones41: sum_k habiroTerm; habiroTerm = q^{Nk} (q^{-N-1};q^{-1})_k (q^{-N+1};q)_k
    tot = mp.mpf(0)
    for k in range(N):
        p1 = mp.mpf(1)
        for j in range(k):
            p1 *= 1 - q ** (-(N + 1 + j))
        p2 = mp.mpf(1)
        for j in range(k):
            p2 *= 1 - q ** (j + 1) * q ** (-N)
        tot += q ** (N * k) * p1 * p2
    return tot


def corpus_trefoil(w, N):
    # coloredJonesTrefoil (Rosso-Jones), q = w^4, reduced J_1 = 1
    n = N - 1
    num = mp.fsum(((-1) ** ((n - j) % 2)
                   * w ** (2 * j * (j + 1) - n * (n + 2))) ** 3
                  * qint_w(w ** 2, 2 * j + 1) for j in range(n + 1))
    return w ** (-3 * n * (n + 2)) * num / qint_w(w ** 2, N)


def main() -> int:
    t0 = time.monotonic()
    print("=" * 74)
    print(" Masbaum math/0306345 cross-check — QOU 4_1 + trefoil towers")
    print("=" * 74)
    print(" (paper is TWIST KNOTS, not Borromean — provenance corrected)\n")

    qs = [mp.mpf("1.10998"), mp.mpf("1.37"), mp.mpf("0.813"), mp.mpf(2)]
    NMAX = 7

    # [FE]
    worst_fe = mp.mpf(0)
    for q in qs:
        for N in range(1, NMAX + 1):
            worst_fe = max(worst_fe, abs(corpus_fig8(q, N) - masbaum_fig8(q, N)))
    okFE = worst_fe < mp.mpf("1e-30")
    print(f"  [FE] corpus 4_1 Habiro tower == Masbaum J'_{{K_-1}}: "
          f"worst |Δ| = {mp.nstr(worst_fe, 4)}  {'PASS' if okFE else 'FAIL'}")

    # [TR] q = w^4 ; try direct (q) and mirror (1/q) to fix the convention
    worst_tr = mp.mpf('inf')
    which = None
    for label, qmap in (("q_M = q_corpus", lambda q: q),
                        ("q_M = 1/q_corpus (mirror)", lambda q: 1 / q)):
        w_worst = mp.mpf(0)
        for q in qs:
            w = q ** (mp.mpf(1) / 4)
            for N in range(1, NMAX + 1):
                w_worst = max(w_worst,
                              abs(corpus_trefoil(w, N) - masbaum_trefoil(qmap(q), N)))
        if w_worst < worst_tr:
            worst_tr = w_worst
            which = label
    okTR = worst_tr < mp.mpf("1e-30")
    print(f"  [TR] corpus trefoil Rosso-Jones == Masbaum J'_{{K_1}}: "
          f"worst |Δ| = {mp.nstr(worst_tr, 4)} via {which}  "
          f"{'PASS' if okTR else 'FAIL'}")

    ok = okFE and okTR
    verdict = (
        ("Both QOU corpus towers match Masbaum's published twist-knot "
         f"formulas exactly (40 dps, N<= {NMAX}, {len(qs)} anchors): the 4_1 "
         "Habiro double-Pochhammer tower = J'_{K_-1} (all cyclotomic "
         f"coefficients 1), and the trefoil Rosso-Jones tower = J'_{{K_1}} "
         f"({which}). The trefoil convention is now literature-anchored "
         "(Masbaum's left-handed K_1), not merely self-anchored. "
         "PROVENANCE: math/0306345 is twist knots, carries NO Borromean "
         "formula — the Borromean cross-check needs Habiro [H1], unavailable.")
        if ok else
        "MISMATCH — investigate convention before claiming a literature match."
    )
    print(f"\n  VERDICT: {verdict}")
    print(f"  ({time.monotonic()-t0:.1f}s)")

    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("aj-masbaum-crosscheck", engine="mpmath",
                            start_time=t0)
        wb.set_description(
            "Cross-check of the QOU 4_1 (HabiroNewtonLadder) and trefoil "
            "(AJTrefoil Rosso-Jones) colored-Jones towers against Masbaum "
            "arXiv:math/0306345 Thm 5.1 / Rmk 5.2 twist-knot formulas "
            "(K_-1 = fig-8, K_1 = left trefoil). Provenance note: the paper "
            "is twist knots, not Borromean rings."
        )
        wb.add_data("reference", "Masbaum, AGT 3 (2003) 537-556, arXiv:math/0306345")
        wb.add_data("trefoil_convention_match", which)
        wb.add_data("worst_delta_fig8", mp.nstr(worst_fe, 6))
        wb.add_data("worst_delta_trefoil", mp.nstr(worst_tr, 6))
        wb.add_data("provenance_correction",
                    "math/0306345 = twist knots, NOT Borromean; Borromean ref is Habiro [H1]")
        wb.add_data("verdict", verdict)
        wb.add_assertion("fig8_matches_masbaum", okFE, True)
        wb.add_assertion("trefoil_matches_masbaum", okTR, True)
        out = wb.save()
        print(f"  Witness: {out}")
    except Exception as exc:  # noqa: BLE001
        print(f"  (witness skipped: {exc})")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent / "substrate"))
    sys.exit(main())
