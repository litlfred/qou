#!/usr/bin/env python3
"""Colour-arena missed-block COUNT growth — the structural backbone of
"no finite colour arena" (formalize-first, item 1).

Context.  The production nuclear-mass trace is the FULL Hecke / Wenzl
principal specialization  s_lambda(1, q, q^2, ...)  — nonzero for EVERY
partition lambda (no row cutoff).  A finite colour arena C^N realizes the
N-variable specialization  s_lambda(1, q, ..., q^{N-1}), which by the Schur
row-bound

      s_lambda(x_1, ..., x_N) = 0   <=>   rows(lambda) > N

KILLS every partition with more than N rows.  So a finite C^N "misses" the
trace content carried by the > N-row Wedderburn blocks.

The companion audit `2026-06-16-keystone-arena-is-full-hecke-not-su3.md`
records the EMPIRICAL *weighted* miss-share growing with A
(0.2% -> 1.1% -> 3.4% @ He-4, ~6.0% @ He-5).  Two data points are not a
theorem.  THIS script establishes the part that IS a theorem: the
*block-count* backbone.

  PROVABLE (this script + the Lean file ColourArenaBlockCount.lean):
    (B1) row-bound          s_lambda(N vars)=0  <=>  rows(lambda) > N
    (B2) injection bound    #missed(n, N)  >=  p(n - N - 1)
         via  mu  |->  (column of height N+1) ++ mu
    (B3) monotone in n      #missed(n, N)  <=  #missed(n+1, N)
         via  lambda |-> add one box to row 1
    (B4) unbounded growth   #missed(n, N) -> infinity   (from B2, p -> infinity)
    (B5) captured fraction   #captured(n, N) / p(n) -> 0  for every fixed N
         (captured = rows <= N is polynomial in n; p(n) is super-polynomial)

  NOT PROVABLE structurally (correctly stays empirical):
    the *weighted* miss-share monotonicity 3.4% -> 6.0%.  It depends on q_0
    (principal-specialization weights) and the nucleus-specific characters
    chi_lambda(beta_A), whose signs oscillate with the braid.  The count
    backbone B1-B5 forces "no finite C^N suffices for all A"; the precise
    percentage is the weighted FACE of that structural fact, not a corollary.

Run:  python3 docs/audits/scripts/colour_arena_missed_block_count.py
Exit 0 iff every structural assertion B1-B5 holds on the tested range.
"""
import sys

import sympy as sp

q = sp.symbols("q")


# --------------------------------------------------------------------------
# partitions
# --------------------------------------------------------------------------
def partitions(n, mx=None):
    """All partitions of n as weakly-decreasing tuples (largest part <= mx)."""
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def p(n):
    """Partition count p(n)  (p(n)=0 for n<0, p(0)=1)."""
    if n < 0:
        return 0
    return sum(1 for _ in partitions(n))


def rows(lam):
    return len(lam)


def n_missed(n, N):
    """#{lambda |- n : rows(lambda) > N}  (blocks a colour-C^N arena kills)."""
    return sum(1 for lam in partitions(n) if rows(lam) > N)


def n_captured(n, N):
    """#{lambda |- n : rows(lambda) <= N}  (blocks a colour-C^N arena keeps)."""
    return sum(1 for lam in partitions(n) if rows(lam) <= N)


# --------------------------------------------------------------------------
# (B1) Schur row-bound  s_lambda(N vars)=0 iff rows>N  (principal spec)
# --------------------------------------------------------------------------
def schur_kvar_principal(lam, k):
    """s_lambda(1, q, ..., q^{k-1}) via the bialternant; 0 iff rows(lam) > k."""
    if len(lam) > k:
        return sp.Integer(0)
    xs = [q ** i for i in range(k)]
    l = list(lam) + [0] * (k - len(lam))
    num = sp.Matrix(k, k, lambda i, j: xs[j] ** (l[i] + k - 1 - i))
    den = sp.Matrix(k, k, lambda i, j: xs[j] ** (k - 1 - i))
    return sp.simplify(num.det() / den.det())


def check_row_bound():
    ok = True
    for n in (5, 6):
        for lam in partitions(n):
            r = rows(lam)
            for k in (2, 3):
                is_zero = schur_kvar_principal(lam, k) == 0
                if is_zero != (r > k):
                    ok = False
                    print(f"    ROW-BOUND FAIL lam={lam} k={k} zero={is_zero} rows={r}")
    return ok


# --------------------------------------------------------------------------
# (B2) injection  mu |-> prependColumn(N, mu) = (1,)*(N+1) + mu
#      lands in missed(|mu|+N+1, N) and is injective => #missed >= p(n-N-1)
# --------------------------------------------------------------------------
def prepend_column(N, mu):
    """Prepend a first column of height N+1: rows become rows(mu)+N+1 > N."""
    return tuple([1] * (N + 1) + list(mu))


def check_injection_bound(N_vals, n_max):
    ok = True
    for N in N_vals:
        for n in range(N + 1, n_max + 1):
            # build the injected image from all partitions of n-(N+1)
            src = list(partitions(n - (N + 1)))
            img = [prepend_column(N, mu) for mu in src]
            # each image is a partition of n with > N rows
            for lam in img:
                assert sum(lam) == n, (lam, n)
                if rows(lam) <= N:
                    ok = False
                    print(f"    IMG not missed: N={N} lam={lam}")
            # injective: distinct sources -> distinct images
            if len(set(img)) != len(src):
                ok = False
                print(f"    INJECTION not injective at N={N} n={n}")
            # the bound itself
            missed = n_missed(n, N)
            bound = p(n - N - 1)
            if missed < bound:
                ok = False
                print(f"    BOUND FAIL N={N} n={n} missed={missed} < p(n-N-1)={bound}")
    return ok


# --------------------------------------------------------------------------
# (B3) monotone in n  via  lambda |-> add one box to row 1
# --------------------------------------------------------------------------
def add_box_row1(lam):
    if not lam:
        return (1,)
    return (lam[0] + 1,) + tuple(lam[1:])


def check_monotone(N_vals, n_max):
    ok = True
    for N in N_vals:
        prev = None
        for n in range(N + 1, n_max + 1):
            m = n_missed(n, N)
            if prev is not None and m < prev:
                ok = False
                print(f"    MONOTONE FAIL N={N} n={n} missed={m} < prev={prev}")
            # the injection witness: every missed(n) maps into missed(n+1)
            for lam in partitions(n):
                if rows(lam) > N:
                    img = add_box_row1(lam)
                    if sum(img) != n + 1 or rows(img) <= N:
                        ok = False
                        print(f"    add_box_row1 broke N={N} lam={lam}")
            prev = m
    return ok


# --------------------------------------------------------------------------
# (B5) captured fraction -> 0
# --------------------------------------------------------------------------
def captured_fraction(n, N):
    return sp.Rational(n_captured(n, N), p(n))


def main():
    print("=" * 72)
    print("COLOUR-ARENA MISSED-BLOCK COUNT  (structural backbone, formalize-first)")
    print("=" * 72)

    print("\n(B1) Schur row-bound  s_lambda(N vars)=0 <=> rows>N  (n=5,6, N=2,3)")
    b1 = check_row_bound()
    print(f"     => {b1}")

    N_vals = (2, 3, 4)
    n_max = 14

    print(f"\n(B2) injection bound  #missed(n,N) >= p(n-N-1)   "
          f"(N in {N_vals}, n<= {n_max})")
    b2 = check_injection_bound(N_vals, n_max)
    print(f"     => {b2}")

    print(f"\n(B3) monotone in n   #missed(n,N) non-decreasing  (N in {N_vals})")
    b3 = check_monotone(N_vals, n_max)
    print(f"     => {b3}")

    print("\n     missed-block COUNT  #{lambda|-n : rows>N}  (grows with A; n=3A):")
    print("       n  |  N=2   N=3   N=4   | p(n)")
    print("     -----+---------------------+------")
    for n in range(3, n_max + 1):
        row = "  ".join(f"{n_missed(n, N):4d}" for N in N_vals)
        print(f"     {n:4d} | {row}  | {p(n):4d}")

    # (B4) unbounded: the count strictly exceeds any bound as n grows
    b4 = all(n_missed(n_max, N) > n_missed(N + 2, N) for N in N_vals)
    print(f"\n(B4) unbounded growth  #missed(n_max) > #missed(small)  => {b4}")

    print("\n(B5) captured (rows<=N) fraction  #captured(n,N)/p(n) -> 0:")
    print("       n  |   N=2      N=3      N=4")
    print("     -----+--------------------------")
    fracs = {N: [] for N in N_vals}
    for n in range(3, n_max + 1):
        cells = []
        for N in N_vals:
            f = captured_fraction(n, N)
            fracs[N].append(float(f))
            cells.append(f"{float(f):7.4f}")
        print(f"     {n:4d} |  " + "  ".join(cells))
    # captured fraction is (eventually) decreasing for each fixed N
    b5 = all(fracs[N][-1] < fracs[N][0] for N in N_vals)
    print(f"     captured-fraction(n_max) < captured-fraction(3)  => {b5}")

    print("\n" + "=" * 72)
    print("HONEST SPLIT (formalize-first verdict)")
    print("=" * 72)
    print("  PROVABLE (theorem): B1-B5 — the colour-C^N arena misses an")
    print("    UNBOUNDED (-> infinity) and (in n) monotone number of Wedderburn")
    print("    blocks.  No finite N suffices for all A => 'no finite colour arena'")
    print("    is upgraded from 2-3 data points to a block-count theorem.")
    print("  EMPIRICAL (correctly NOT a theorem): the *weighted* miss-share")
    print("    3.4% @He-4 -> 6.0% @He-5 is q_0- and braid-dependent (the")
    print("    principal-spec weights x oscillating chi_lambda(beta_A)); it is the")
    print("    weighted FACE of the count backbone, not forced to be monotone.")

    all_ok = b1 and b2 and b3 and b4 and b5
    assert all_ok, "a structural assertion B1-B5 failed"
    print("\nALL STRUCTURAL ASSERTIONS B1-B5 VERIFIED.")
    sys.exit(0)


if __name__ == "__main__":
    main()
