#!/usr/bin/env python3
"""The Z=1..20 mass table, regenerated in convention D. (bean qou-1jw9)

AUTHORISED by the owner 2026-08-29: "recompute Phi_1 (and anything else
convention C -> D)", after the measurement in phi1_convention_d_probe.py showed
the carried Phi_1 is a convention-C artifact that convention D cannot reach.

WHAT CHANGES, AND WHY EACH IS A DERIVATION RATHER THAN A CARRY.

  Phi_2, Phi_3 -- no longer carried from the recovered witness at all. Both are
  now COMPUTED from the strand content and the crossing values proved
  sorry-free in HeckeLinearReduction.lean:

      Phi_3 = (-2Z - N(N-1)) * ln q          [= 2(2C(Z,2) - C(N,2) - Z^2) ln q]
      Phi_2 = Z*N * ln(1 + h^2/4)

  Each reproduced all 19 non-hydrogen carried values exactly
  (phi_allpairs_reconstruction.py), so replacing the carry with the derivation
  is value-neutral for these two. Both are CONVENTION-FREE -- neither uses the
  Markov parameter z -- so the C->D move does not touch them.

  Phi_1 -- recomputed. It is the only invariant that uses z, hence the only one
  the convention ruling can move. Computed here in convention D only
  (z = q^3/(q^2+1)), under the ALL-PAIRS chain structure the theorem's own
  prose specifies ("chaining the crossing matrices of all strands j > i" =
  for strand i, cross with every strand j > i), minimised over orderings per
  def:atomic-braid's ground-state rule.

THE MINIMISATION IS EXPONENTIAL AND IS NOT BRUTE-FORCED. C(40,20) = 1.4e11 at
Ca. This uses swap hill-climbing with restarts over nuclear arrangements. It is
VALIDATED, not assumed: on the five atoms where exhaustive enumeration is
feasible (He, Li, Be, B, C -- up to 924 arrangements) the local search finds the
exact global minimum in all five cases. For heavier atoms the result is a local
minimum that may not be global; every row records which regime it is in.

H IS EXCLUDED from the accuracy statistics. def:atomic-braid gives hydrogen a
special pe crossing (B_3-dressed eigenvalues), which this construction does not
implement, and its carried Phi_3 = +10 ln q is outside the Table-1 accounting.

NO FITTING. alpha = m_e * 8G, beta_2 = -2[3]_q and beta_3 = h_A^2 are the
published coefficients evaluated at q0; the AME2020 column is used only to
report error, never to choose anything.
"""
from __future__ import annotations

import random
import sys
from math import comb
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
set_compute_dps(50)

from qou_substrate.constants import Q as Q_PROTON  # noqa: E402

Q = mp.mpf(str(Q_PROTON))
H = Q - 1 / Q
Z_D = Q ** 3 / (Q ** 2 + 1)
M_E, M_P, M_N = mp.mpf("0.51099895"), mp.mpf("938.27208816"), mp.mpf("939.56542052")
ALPHA = M_E * 8 * mp.catalan
BETA2 = -2 * (Q ** 2 + 1 + Q ** -2)
BETA3 = H ** 2

TBL = {("p", "p"): (1, mp.mpf(0)), ("n", "n"): (1, -H), ("p", "n"): (1, -H / 2),
       ("p", "e"): (1, -H), ("n", "e"): (0, mp.mpf(1)), ("e", "e"): (1, mp.mpf(0))}
EXACT_UPTO = 924          # arrangements we are willing to enumerate exhaustively


def cr(a, b):
    return TBL[(a, b)] if (a, b) in TBL else TBL[(b, a)]


def V(chain):
    a, b = mp.mpf(0), mp.mpf(1)
    for c, d in chain:
        c = mp.mpf(c)
        a, b = a * (c * H + d) + b * c, a * c + b * d
    return Z_D * a + b


def phi1(seq):
    n = len(seq)
    t = mp.mpf(0)
    for i in range(n):
        ch = [cr(seq[i], seq[j]) for j in range(i + 1, n)]
        if ch:
            t += mp.log(abs(V(ch)))
    return t


def nuc_to_seq(nuc):
    s = []
    for c in nuc:
        s.extend(["e", "p"]) if c == "p" else s.append("n")
    return s


def minimise(Z, N, restarts=4, seed=0):
    """Swap hill-climbing; validated against exhaustive search on Z<=6."""
    rng = random.Random(seed)
    base = list("p" * Z + "n" * N)
    k = min(Z, N)
    starts = [list("pn" * k) + list("n" * (N - k)) + list("p" * (Z - k))]
    for _ in range(restarts - 1):
        c = base[:]
        rng.shuffle(c)
        starts.append(c)
    best = None
    for st in starts:
        cur, cv = st[:], phi1(nuc_to_seq(st))
        improved = True
        while improved:
            improved = False
            for i in range(len(cur)):
                for j in range(i + 1, len(cur)):
                    if cur[i] == cur[j]:
                        continue
                    cand = cur[:]
                    cand[i], cand[j] = cand[j], cand[i]
                    v = phi1(nuc_to_seq(cand))
                    if v < cv:
                        cur, cv, improved = cand, v, True
        if best is None or cv < best[0]:
            best = (cv, cur[:])
    return best


# (atom, Z, N, M_obs AME2020 as recorded, M_pred as published in convention C)
ROWS = [
    ("H", 1, 0, "938.78313", "938.910"),      ("He", 2, 2, "3728.4013", "3734.624"),
    ("Li", 3, 4, "6535.367", "6534.188"),     ("Be", 4, 5, "8394.7937", "8378.704"),
    ("B", 5, 6, "10255.103", "10237.301"),    ("C", 6, 6, "11177.9292", "11168.874"),
    ("N", 7, 7, "13043.7816", "13029.983"),   ("O", 8, 8, "14899.1693", "14890.701"),
    ("F", 9, 10, "17696.901", "17690.792"),   ("Ne", 10, 10, "18622.8354", "18615.219"),
    ("Na", 11, 12, "21414.8301", "21418.256"), ("Mg", 12, 12, "22341.908", "22342.658"),
    ("Al", 13, 14, "25133.1432", "25143.149"), ("Si", 14, 14, "26060.3443", "26067.918"),
    ("P", 15, 16, "28851.873", "28872.696"),  ("S", 16, 16, "29781.8", "29797.187"),
    ("Cl", 17, 18, "32573.283", "32597.913"), ("Ar", 18, 22, "37224.719", "37273.796"),
    ("K", 19, 20, "36294.464", "36324.625"),  ("Ca", 20, 20, "37213.777", "37248.739"),
]


def main() -> int:
    lnq = mp.log(Q)
    print(f"convention D:  z = q^3/(q^2+1) = {mp.nstr(Z_D, 16)}")
    print(f"q0 (proton pin) = {mp.nstr(Q, 18)}")
    print(f"alpha = m_e*8G = {mp.nstr(ALPHA, 12)}   beta2 = {mp.nstr(BETA2, 12)}"
          f"   beta3 = h_A^2 = {mp.nstr(BETA3, 12)}\n")
    print(f"{'atom':>5} {'Z':>3} {'N':>3} {'Phi_1 (D)':>13} {'Phi_2':>11} "
          f"{'Phi_3':>12} {'M_pred D':>12} {'M_obs':>12} {'err %':>9} "
          f"{'vs C-pub':>10} {'regime':>7}")
    print("-" * 122)
    errs = []
    for el, Z, N, mobs, mpub in ROWS:
        p1, _ = minimise(Z, N)
        p2 = Z * N * mp.log(1 + H ** 2 / 4)
        p3 = mp.mpf(-2 * Z - N * (N - 1)) * lnq
        corr = ALPHA * (p1 + BETA2 * p2 + BETA3 * p3)
        base = Z * M_P + N * M_N + Z * M_E
        pred = base + corr
        obs = mp.mpf(mobs)
        err = (pred - obs) / obs * 100
        shift = pred - mp.mpf(mpub)
        regime = "exact" if comb(Z + N, Z) <= EXACT_UPTO else "local"
        if el != "H":
            errs.append(abs(err))
        print(f"{el:>5} {Z:>3} {N:>3} {mp.nstr(p1,8):>13} {mp.nstr(p2,7):>11} "
              f"{mp.nstr(p3,8):>12} {mp.nstr(pred,10):>12} {mobs:>12} "
              f"{mp.nstr(err,4):>9} {mp.nstr(shift,6):>10} {regime:>7}")
    mean = mp.fsum(errs) / len(errs)
    print(f"\n  convention D, H excluded: mean |err| = {mp.nstr(mean,6)} %   "
          f"max = {mp.nstr(max(errs),6)} %   over {len(errs)} rows")
    print(f"  published convention-C table reported mean 0.0745925 %, max 0.190854 %")
    print("\n  'exact' = the ordering minimum is the global one (exhaustive search")
    print("  feasible); 'local' = hill-climbing minimum, validated against exhaustive")
    print("  search on all five feasible atoms but not proved global here.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
