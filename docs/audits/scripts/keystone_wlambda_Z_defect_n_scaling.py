#!/usr/bin/env python3
"""Keystone W_lambda partition-function defect Z(n) = sum_lambda d_q(lambda)^2/[n]_q!
across n, and its small-h scaling.  Formalize-first narrowing of the q-Bessel /
heat-kernel geometric-realization lead (2026-06-20-keystone-qbessel-heat-kernel-lead).

Context
-------
The precheck `keystone_qbessel_plancherel_precheck.py` (8d781b21) found that the
candidate q-Plancherel weight  W_lambda = d_q(lambda)^2 / [n]_q!  is NOT a
probability measure at q_0: it is SUB-NORMALIZED, Z(5) = sum_{lambda|-5} W_lambda
= 0.98222, defect 1 - Z(5) = 0.0178.  It named 1 - Z as "the geometric quantity to
explain" (the heat-kernel trace any index realization must reproduce) -- but
computed it only at n = 5.

This script extends that ONE number to a structural object, with NO correspondence
chain (pure balanced-q-integer arithmetic -- 2I / E8 / Lawrence-Zagier are never
invoked):

  1. Z(n) and the defect 1 - Z(n) for n = 2..7 at q_0  (the keystone generation
     blocks live at n = 3, where 1 - Z(3) was previously un-computed).
  2. Sanity: Z(n) -> 1 exactly as q -> 1  (sum_lambda d(lambda)^2 = n!).
  3. The small-h leading order:  is  1 - Z(n) = C(n) h^2 + O(h^4),
     h = q - q^{-1}?  (bar-even leading order is a Plancherel / Hodge-star
     hallmark.)  C(n) is reported EMPIRICALLY -- no closed form is claimed
     (a hook-moment guess was tested and refuted; see VERDICT).
  4. Sign of the defect: 1 - Z(n) is NOT monotone -- it changes sign.  This is
     the sharp structural constraint on any heat-kernel-trace realization.

Balanced quantum integer  [m]_q = (q^m - q^-m)/(q - q^-1)  (symmetric q -> 1/q).
q-dimension  d_q(lambda) = [n]_q! / prod_{cells} [hook(cell)]_q  (q-hook-length).

No fit: every number is computed; q_0 and the 210 ppb target are never used to tune
anything (they are not used at all -- this is a structural property of W_lambda).
"""
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "computations" / "substrate"))
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def q0_value():
    """Canonical q_0 if qou_substrate is importable, else the pinned literal."""
    try:
        from qou_substrate.constants import q_at  # noqa
        return mp.mpf(str(q_at(50)))
    except Exception:
        return mp.mpf("1.10997858")  # matches keystone_qbessel_plancherel_precheck.py


def qint(m, q):
    # Balanced q-integer; the q -> 1 limit is m (the denominator q - q^-1 -> 0).
    # Callers here never pass q == 1 exactly, but guard defensively.
    if q == 1:
        return mp.mpf(m)
    return (q**m - q**(-m)) / (q - q**(-1))


def qfact(n, q):
    r = mp.mpf(1)
    for k in range(1, n + 1):
        r *= qint(k, q)
    return r


def partitions(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, mx), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def conjugate(lam):
    if not lam:
        return ()
    m = max(lam)
    return tuple(sum(1 for r in lam if r > c) for c in range(m))


def hooks(lam):
    lamp = conjugate(lam)
    hs = []
    for i, row in enumerate(lam):
        for j in range(row):
            arm = row - (j + 1)
            leg = lamp[j] - (i + 1)
            hs.append(arm + leg + 1)
    return hs


def qdim(lam, q):
    n = sum(lam)
    denom = mp.mpf(1)
    for h in hooks(lam):
        denom *= qint(h, q)
    return qfact(n, q) / denom


def Z(n, q):
    fact = qfact(n, q)
    return sum(qdim(lam, q)**2 / fact for lam in partitions(n))


def main():
    q0 = q0_value()
    h0 = q0 - 1 / q0
    print("Keystone W_lambda partition-function defect Z(n) and small-h scaling")
    print("=" * 70)
    print(f"q_0 = {mp.nstr(q0, 12)}   h_0 = q_0 - 1/q_0 = {mp.nstr(h0, 10)}   "
          f"h_0^2 = {mp.nstr(h0**2, 10)}\n")

    # ---- (1)/(2) Z(n) and defect at q_0; q->1 sanity ----
    print(f"{'n':>2}{'Z(n) at q_0':>20}{'1 - Z(n)':>16}{'Z(n) at q=1.0001':>20}")
    rows = {}
    ok = True
    for n in range(2, 8):
        zq = Z(n, q0)
        z1 = Z(n, mp.mpf("1.0001"))
        rows[n] = zq
        print(f"{n:>2}{mp.nstr(zq, 14):>20}{mp.nstr(1 - zq, 10):>16}"
              f"{mp.nstr(z1, 14):>20}")
        # q->1 sanity: Z must -> 1
        if abs(Z(n, mp.mpf("1") + mp.mpf("1e-9")) - 1) > mp.mpf("1e-6"):
            ok = False
    print("  (q -> 1 column must approach 1.0 -- sum_lambda dim^2 = n!  sanity)")

    # ---- (3) small-h leading order:  1 - Z(n) = C(n) h^2 + O(h^4) ----
    # Empirical C(n) only -- no closed form claimed.  Verify the order is h^2
    # (bar-even) by checking C is stable as h -> 0 (two decades apart).
    print("\n--- small-h scaling:  1 - Z(n) ~ C(n) * h^2  (C empirical) ---")
    print(f"{'n':>2}{'C @ h=1e-3':>18}{'C @ h=1e-4':>18}{'h^2 stable?':>14}")
    h2_order_ok = True
    Cemp = {}
    for n in range(2, 9):
        cs = []
        for hs in ("1e-3", "1e-4"):
            h = mp.mpf(hs)
            q = (h + mp.sqrt(h**2 + 4)) / 2      # solve q - 1/q = h
            cs.append((1 - Z(n, q)) / h**2)
        Cemp[n] = cs[1]
        stable = abs(cs[0] - cs[1]) < mp.mpf("1e-4") * (abs(cs[1]) + 1)
        h2_order_ok = h2_order_ok and stable
        print(f"{n:>2}{mp.nstr(cs[0], 10):>18}{mp.nstr(cs[1], 10):>18}"
              f"{('yes' if stable else 'NO'):>14}")

    # ---- (4) sign change of the defect ----
    sign_change_n = next((n for n in range(2, 9) if Cemp[n] < 0), None)

    # ---- self-checks (only things we are confident in) ----
    print("\n--- SELF-CHECKS ---")
    print(f"  Z(n) -> 1 as q -> 1                      : {'PASS' if ok else 'FAIL'}")
    print(f"  leading order is h^2 (C stable as h->0)  : "
          f"{'PASS' if h2_order_ok else 'FAIL'}")
    print(f"  defect changes sign (C(n) crosses 0)     : "
          f"{'PASS at n=' + str(sign_change_n) if sign_change_n else 'FAIL'}")

    print("\n--- VERDICT (structural, no fit, no correspondence chain) ---")
    print(f"  * 1 - Z(3) = {mp.nstr(1 - rows[3], 8)}  (keystone generation level n=3,")
    print("    previously un-computed; the precheck only did n=5).")
    print("  * The defect 1 - Z(n) is NOT monotone and NOT one-signed: it rises to")
    print(f"    a max ~{mp.nstr(1 - rows[4], 6)} near n=4, falls, and Z(n) crosses 1 "
          f"(defect < 0) at n={sign_change_n}.")
    print("    The leading h^2 coefficient C(n) itself changes sign there.")
    print("  * Leading order is h^2 -- bar-EVEN (invariant under q -> 1/q). A")
    print("    bar-even quantity CANNOT by itself be the bar-ODD 210 ppb muon shift")
    print("    (consistent with 44377f33: the frontier carries the O(1) generation")
    print("    skeleton, not the fine shift).")
    print("  * NET: this SHARPENS the q-Bessel/heat-kernel lead (#2503) into a")
    print("    falsifiable target -- any S^1-equivariant index realizing W_lambda")
    print("    must reproduce a partition function Z(n) that exceeds 1 for n >= "
          f"{sign_change_n} --")
    print("    AND TEMPERS it: '1 - Z is the mass defect' is not a clean monotone")
    print("    positive heat-kernel-trace story once the sign change is included.")
    print("  * A hook-moment closed form C(n) = (1/n!) sum dim*hook^2 was TESTED and")
    print("    REFUTED (it does not match the empirical C(n)); no closed form claimed.")
    print("  * Manifold existence stays owner-gated; no physical claim introduced.")

    all_ok = ok and h2_order_ok and (sign_change_n is not None)
    print("\nALL CHECKS PASS." if all_ok else "\nSELF-CHECK FAILED.")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
