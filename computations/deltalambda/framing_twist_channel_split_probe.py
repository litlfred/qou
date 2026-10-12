#!/usr/bin/env python3
"""Ribbon twist on the spin factor only: does it split deuteron from singlet?

Bean ``qou-ulj0`` (stepping stone 4 of ``qou-slz5``).  Exact arithmetic only:
``fractions.Fraction`` for the representation-theory checks, ``mpmath`` at
``mp.dps = 60`` at the proton-pinned ``q0`` (``q_parameter.Q_MP``) for numbers.
No float anywhere in a computation.

Setting (six-quark Schur--Weyl, two-row shapes).  Two-nucleon spin ``S`` is the
two-row block ``(3+S, 3-S)`` of ``H_6(q)``; the same for isospin ``T``.

    deuteron  (S,T) = (1,0):  spin (4,2)  x  isospin (3,3)
    singlet   (S,T) = (0,1):  spin (3,3)  x  isospin (4,2)

With one Markov trace on both copies the two channels have equal trace
``w(4,2) w(3,3)`` (the Pauli lock of bean ``qou-7zob``; ``ChannelSwapSplitting``).

"Twist on the spin factor only" is the algebra element ``theta_spin (x) 1`` where
``theta`` is central in ``H_6`` and acts on the ``lambda``-block by a scalar:

  * full twist  Delta^2 = (s1 s2 s3 s4 s5)^6  acts by  q^{2 c(lambda)}   (checked here
    on explicit seminormal matrices -- section 1);
  * ribbon element  theta = q^{c(lambda)}  (``KeystoneModularTwist.theta``), Delta^2 = theta^2.

c(4,2) = 5, c(3,3) = 3, and for two-row (n-k, k):  4 c = 2S(2S+2) + n(n-4), i.e.
c = S(S+1) + const(n): the twist ratio between channels is q^{k (C(1) - C(0))}, k = 1
(ribbon) or 2 (full twist), INDEPENDENT of z.

Comparison facts (AME deuteron binding, singlet unbound) are printed for context only,
labelled COMPARISON; nothing is tuned to them.
"""
from __future__ import annotations

import sys
from fractions import Fraction
from itertools import permutations
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parent.parent),
                str(Path(__file__).resolve().parent.parent / "substrate")]
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 60
N = 6
SHAPES = {"(4,2)": (4, 2), "(3,3)": (3, 3)}


# ---------------------------------------------------------------- tableaux
def cells(lam):
    return [(i, j) for i, r in enumerate(lam) for j in range(r)]


def standard_tableaux(lam):
    """Standard tableaux as tuples pos[k] = (row, col) of entry k (0-based)."""
    n = sum(lam)
    out = []

    def rec(filled, pos):
        if len(pos) == n:
            out.append(tuple(pos))
            return
        for i, r in enumerate(lam):
            j = filled[i]
            if j < r and (i == 0 or filled[i - 1] > j):
                filled[i] += 1
                pos.append((i, j))
                rec(filled, pos)
                pos.pop()
                filled[i] -= 1

    rec([0] * len(lam), [])
    return out


def content_sum(lam):
    return sum(j - i for (i, j) in cells(lam))


# ------------------------------------------------- seminormal representation
def seminormal(lam, qv, one):
    """Young seminormal matrices of sigma_1..sigma_{n-1} for H_n(q),
    eigenvalues q, -q^{-1}.  Field-generic (Fraction or mpf)."""
    tabs = standard_tableaux(lam)
    idx = {t: a for a, t in enumerate(tabs)}
    dim = len(tabs)
    n = sum(lam)
    qi = one / qv
    mats = []
    for i in range(n - 1):
        M = [[0 * one for _ in range(dim)] for _ in range(dim)]
        for t in tabs:
            a = idx[t]
            (r1, c1), (r2, c2) = t[i], t[i + 1]
            d = (c2 - r2) - (c1 - r1)
            qd = qv ** d
            diag = qd * (qv - qi) / (qd - one / qd)
            M[a][a] = diag
            if r1 != r2 and c1 != c2:
                t2 = list(t)
                t2[i], t2[i + 1] = t2[i + 1], t2[i]
                b = idx[tuple(t2)]
                # partner diag is (q - q^-1) - diag; 2x2 block needs det = -1
                partner = (qv - qi) - diag
                if r2 > r1:      # i+1 lower in t: ascending direction, coefficient 1
                    M[b][a] = one
                else:
                    M[b][a] = diag * partner + one
        mats.append(M)
    return mats, dim


def mm(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def eye(n, one):
    return [[one if i == j else 0 * one for j in range(n)] for i in range(n)]


def is_scalar(M, s):
    n = len(M)
    return all(M[i][j] == (s if i == j else 0) for i in range(n) for j in range(n))


def check_rep_and_twist(lam, qv, one):
    mats, dim = seminormal(lam, qv, one)
    I = eye(dim, one)
    qi = one / qv
    ok = True
    for i, S in enumerate(mats):     # Hecke relation (s-q)(s+q^-1)=0
        A = [[S[r][c] - qv * I[r][c] for c in range(dim)] for r in range(dim)]
        B = [[S[r][c] + qi * I[r][c] for c in range(dim)] for r in range(dim)]
        ok &= is_scalar(mm(A, B), 0 * one)
    for i in range(len(mats) - 1):   # braid relation
        a, b = mats[i], mats[i + 1]
        ok &= mm(mm(a, b), a) == mm(mm(b, a), b)
    for i in range(len(mats)):       # far commutation
        for j in range(i + 2, len(mats)):
            ok &= mm(mats[i], mats[j]) == mm(mats[j], mats[i])
    run = I
    for S in mats:
        run = mm(run, S)
    D2 = I
    for _ in range(sum(lam)):
        D2 = mm(D2, run)
    twist_scalar = is_scalar(D2, qv ** (2 * content_sum(lam)))
    return ok, twist_scalar, dim


# --------------------------------------------------------- Ocneanu weights
def hook(lam, i, j):
    arm = lam[i] - j - 1
    leg = sum(1 for r in lam[i + 1:] if r > j)
    return arm + leg + 1


def ocneanu(lam, qv, zv):
    """Frame-general Ocneanu weight (prop:markov-z-reconciliation), h = q - 1/q."""
    h = qv - 1 / qv
    num = den = mp.mpf(1)
    for (i, j) in cells(lam):
        c, hk = j - i, hook(lam, i, j)
        num *= zv * qv ** c - (zv - h) * qv ** (-c)
        den *= qv ** hk - qv ** (-hk)
    return num / den


def main() -> int:
    print("=" * 76)
    print("  RIBBON TWIST ON THE SPIN FACTOR ONLY -- DEUTERON vs SINGLET")
    print("=" * 76)

    # 1. representation-theory checks, exact over Q at two rational q
    rep_ok = twist_ok = True
    for qv in (Fraction(11, 10), Fraction(7, 5)):
        for name, lam in SHAPES.items():
            ok, tw, dim = check_rep_and_twist(lam, qv, Fraction(1))
            print(f"  q={qv}: {name} dim={dim} relations={ok} "
                  f"Delta^2 = q^(2*{content_sum(lam)}) scalar={tw}")
            rep_ok &= ok
            twist_ok &= tw

    # 2. content sums and the two-row Casimir law
    c42, c33 = content_sum((4, 2)), content_sum((3, 3))
    casimir_ok = all(
        4 * content_sum((N - k, k)) == (N - 2 * k) * (N - 2 * k + 2) + N * (N - 4)
        for k in range(0, N // 2 + 1))
    print(f"\n  c(4,2) = {c42}, c(3,3) = {c33}; 4c = 2S(2S+2)+n(n-4) for all k: {casimir_ok}")

    # 3. numbers at q0
    from q_parameter import Q_MP
    q0 = mp.mpf(Q_MP)
    h = q0 - 1 / q0
    zD = q0 ** 3 / (q0 ** 2 + 1)
    zs = {"0": mp.mpf(0), "h/2": h / 2, "h": h, "z_D": zD}
    rows = []
    sym_zero = True
    closed_ok = ratio_z_indep = True
    tol = mp.mpf(10) ** -50
    for k, label in ((1, "ribbon theta = q^c"), (2, "full twist Delta^2 = q^(2c)")):
        t42, t33 = q0 ** (k * c42), q0 ** (k * c33)
        print(f"\n  -- {label}: theta(4,2) = {mp.nstr(t42, 15)}, theta(3,3) = {mp.nstr(t33, 15)}")
        print(f"     channel ratio D/S = q0^{k*(c42-c33)} = {mp.nstr(t42 / t33, 20)}")
        print(f"     normalised split (D-S)/(D+S) = tanh({k} ln q0) = "
              f"{mp.nstr((t42 - t33) / (t42 + t33), 20)}")
        for zl, zv in zs.items():
            w42, w33 = ocneanu((4, 2), q0, zv), ocneanu((3, 3), q0, zv)
            D = t42 * w42 * w33          # spin (4,2) twisted, isospin (3,3) untwisted
            S = t33 * w33 * w42          # spin (3,3) twisted, isospin (4,2) untwisted
            # symmetric twist (both factors): degenerate
            Dsym, Ssym = t42 * w42 * t33 * w33, t33 * w33 * t42 * w42
            sym_zero &= abs(Dsym - Ssym) < tol * abs(Dsym)
            # carrier traces (ChannelSwapSplitting mechanism)
            dtr_d = t42 * w42 - w33      # twisted spin carrier vs untwisted isospin carrier, deuteron
            dtr_s = t33 * w33 - w42
            split = D - S
            closed = (t42 - t33) * w42 * w33
            closed_ok &= abs(split - closed) < tol * abs(closed)
            ratio_z_indep &= abs(D / S - q0 ** (k * (c42 - c33))) < tol
            rows.append({
                "twist": label, "z": zl,
                "w42": mp.nstr(w42, 30), "w33": mp.nstr(w33, 30),
                "r_z": mp.nstr(w42 / w33, 30),
                "D": mp.nstr(D, 30), "S": mp.nstr(S, 30),
                "split": mp.nstr(split, 30),
                "closed_form_residual": mp.nstr(abs(split - closed), 5),
                "ratio_D_over_S": mp.nstr(D / S, 30),
                "carrier_tr_diff_deuteron": mp.nstr(dtr_d, 30),
                "carrier_tr_diff_singlet": mp.nstr(dtr_s, 30),
            })
            print(f"     z={zl:4s}: w42={mp.nstr(w42, 12)} w33={mp.nstr(w33, 12)} "
                  f"r(z)={mp.nstr(w42 / w33, 12)}  D-S={mp.nstr(split, 15)}  "
                  f"D/S={mp.nstr(D / S, 15)}")

    print(f"\n  split = (theta42 - theta33) w42 w33 to 1e-50: {closed_ok}")
    print(f"  D/S independent of z: {ratio_z_indep}")
    print(f"  symmetric twist (both factors) gives D - S = 0 (rel 1e-50): {sym_zero}")
    print("\n  q -> 1 limit: theta -> 1 on both S=0,1 (integer spin, sign (-1)^{2S} = +1),")
    print("  so the split is a pure q-deformation effect; it vanishes classically.")
    print("\n  COMPARISON (context only, nothing tuned): AME2020 deuteron S=1,T=0 bound,"
          " B = 2.224566 MeV;\n  singlet S=0,T=1 unbound (virtual state). Which sign"
          " of D-S maps to 'deuteron binds'\n  depends on the trace->energy map and on the"
          " twist orientation (Delta^2 vs Delta^-2): NOT fixed here.")

    w = WitnessBuilder("framing-twist-channel-split", engine="mpmath+fraction",
                       output_dir=Path(__file__).resolve().parent)
    w.add_assertion("seminormal_relations_hold_exact", 1 if rep_ok else 0, 1)
    w.add_assertion("full_twist_acts_by_q_pow_2c_exact", 1 if twist_ok else 0, 1)
    w.add_assertion("two_row_casimir_law_n6", 1 if casimir_ok else 0, 1)
    w.add_assertion("split_closed_form_1e-50", 1 if closed_ok else 0, 1)
    w.add_assertion("channel_ratio_z_independent", 1 if ratio_z_indep else 0, 1)
    w.add_assertion("symmetric_twist_no_split", 1 if sym_zero else 0, 1)
    w.add_parameter("q0", mp.nstr(q0, 50))
    w.add_parameter("q0_anchor", "proton (q_parameter.Q_MP)")
    w.add_parameter("mp_dps", str(mp.mp.dps))
    w.add_parameter("content_sum_42", str(c42))
    w.add_parameter("content_sum_33", str(c33))
    w.add_data("rows", rows)
    w.save()
    ok = rep_ok and twist_ok and casimir_ok and closed_ok and ratio_z_indep and sym_zero
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
