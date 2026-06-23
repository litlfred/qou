#!/usr/bin/env python3
"""Numerical confirmation of the Lean lemma WLambdaNormalizationInvariance.lean.

Formalize-first companion: the Lean file PROVES (sorry-free, generic field) that
the geometric W_lambda = d_q^2/D^2 (Beasley-Witten/RT Plancherel, PR #2524) and
the keystone W_lambda = d_q^2/[n]_q! differ by ONE lambda-independent global
factor F/D^2 (F=[n]_q!, D^2=sum d_q^2), so:

  * same-block (same-n) RATIOS are normalization-INVARIANT  (ratio_invariant)
  * the geometric weight sums to 1; the keystone weight sums to Z = D^2/F  (!=1)

This script confirms those identities numerically at the substrate q_0 for the
keystone generation block n=5 (electron (3,1,1), muon (3,2), both |- 5) and
quantifies the ONLY place the C1 choice can move a number: an absolute /
un-normalized use, where the shift is exactly Z(n).

No fit: every number is the balanced-q-integer q-dimension; q_0 tunes nothing.
Mirrors qdim() from keystone_wlambda_Z_defect_n_scaling.py (same hook-length q-dim).
"""
import mpmath as mp

mp.mp.dps = 50


def q0_value():
    try:
        from qou_substrate.constants import q_at  # noqa
        return mp.mpf(str(q_at(50)))
    except Exception:
        return mp.mpf("1.10997858")


def qint(m, q):
    if q == 1:
        return mp.mpf(m)
    return (q ** m - q ** (-m)) / (q - q ** (-1))


def qfact(n, q):
    r = mp.mpf(1)
    for k in range(1, n + 1):
        r *= qint(k, q)
    return r


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
            hs.append((row - (j + 1)) + (lamp[j] - (i + 1)) + 1)
    return hs


def qdim(lam, q):
    n = sum(lam)
    denom = mp.mpf(1)
    for h in hooks(lam):
        denom *= qint(h, q)
    return qfact(n, q) / denom


# partitions of 5 (the keystone generation block)
PARTS5 = [(5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)]
ELECTRON = (3, 1, 1)
MUON = (3, 2)


def main():
    q0 = q0_value()
    n = 5
    F = qfact(n, q0)                       # [5]_q!
    d = {lam: qdim(lam, q0) for lam in PARTS5}
    D2 = sum(d[lam] ** 2 for lam in PARTS5)  # global dimension
    Z = D2 / F                              # keystone normalization sum (defect)

    wPlanch = {lam: d[lam] ** 2 / D2 for lam in PARTS5}
    wKey = {lam: d[lam] ** 2 / F for lam in PARTS5}

    print("Keystone W_lambda normalization-invariance — numerical confirmation")
    print("=" * 70)
    print(f"q_0 = {mp.nstr(q0, 12)}   n = {n}")
    print(f"[5]_q! = F = {mp.nstr(F, 12)}   D^2 = sum d_q^2 = {mp.nstr(D2, 12)}")
    print(f"global factor F/D^2 = {mp.nstr(F / D2, 12)}   Z = D^2/F = {mp.nstr(Z, 12)}\n")

    # (1) sum_one + key_sum_eq_Z
    s_pl = sum(wPlanch.values())
    s_ky = sum(wKey.values())
    print("--- normalization sums (Lean: wPlanch_sum_one, wKey_sum_eq_Z) ---")
    print(f"  sum wPlanch = {mp.nstr(s_pl, 20)}   (should be 1)")
    print(f"  sum wKey    = {mp.nstr(s_ky, 20)}   (should be Z = {mp.nstr(Z, 12)})")
    ok_sum = abs(s_pl - 1) < mp.mpf("1e-40") and abs(s_ky - Z) < mp.mpf("1e-40")

    # (2) ratio_invariant on the muon/electron generation pair
    r_pl = wPlanch[MUON] / wPlanch[ELECTRON]
    r_ky = wKey[MUON] / wKey[ELECTRON]
    r_bare = d[MUON] ** 2 / d[ELECTRON] ** 2
    print("\n--- same-block ratio muon (3,2) / electron (3,1,1)  (Lean: ratio_invariant) ---")
    print(f"  wPlanch ratio = {mp.nstr(r_pl, 30)}")
    print(f"  wKey    ratio = {mp.nstr(r_ky, 30)}")
    print(f"  bare d^2 ratio= {mp.nstr(r_bare, 30)}   (Lean: ratio_eq_qdim_ratio)")
    diff = abs(r_pl - r_ky)
    print(f"  |wPlanch ratio - wKey ratio| = {mp.nstr(diff, 6)}  "
          f"=> C1 choice changes the generation RATIO by this (≈0).")
    ok_ratio = diff < mp.mpf("1e-40") and abs(r_pl - r_bare) < mp.mpf("1e-40")

    # (3) the ONLY place C1 moves a number: an absolute / un-normalized use
    print("\n--- absolute (un-normalized) use: the only shift, = Z(n) ---")
    print(f"  wPlanch(muon)/wKey(muon) = {mp.nstr(wPlanch[MUON] / wKey[MUON], 12)} = F/D^2")
    print(f"  an absolute W_lambda value shifts by F/D^2 = {mp.nstr(F / D2, 12)} "
          f"(i.e. 1/Z, a {mp.nstr((1/Z - 1) * 100, 4)}% change at n=5)")
    print("  (per-n: Z-defect 1-Z = 0.0126 at n=3, sign-flips at n=7 — defect script).")

    print("\n--- VERDICT ---")
    print("  The C1 normalization fork (d_q^2/D^2 vs d_q^2/[n]_q!) is a NO-OP for the")
    print("  same-n muon/electron generation RATIO (ratio_invariant, confirmed to 1e-40).")
    print("  It moves a number ONLY for an absolute / cross-n use, by exactly Z(n).")
    print("  => #2524's geometric reframing is, for the generation ratio observable,")
    print("     EXPOSITION (true-Plancherel renaming), not a new/falsifiable prediction.")
    print("  No fit; nothing wired; matches the Lean lemma WLambdaNormalizationInvariance.")

    all_ok = ok_sum and ok_ratio
    print("\nALL CHECKS PASS." if all_ok else "\nCHECK FAILED.")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
