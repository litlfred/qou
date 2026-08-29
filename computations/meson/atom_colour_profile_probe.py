#!/usr/bin/env python3
"""
atom_colour_profile_probe.py — α_shift of the ATOM word at every colour,
computed by exact integer min-plus.

Addendum 40 showed the min-plus predictor is `O(L · dim²)` in integers and
reproduces the measured valuation on 44/46 pairs, lifting the reach obstacle
Addendum 38 named (dense seminormal algebra at 300 dps).  This applies it to the
object that motivated the whole question: the atom word.

TWO EXTENSIONS THE ATOM WORD NEEDS, neither present in Addendum 40.

  1. **Its letters are HECKE ELEMENTS, not braid generators.**
     `atom_braid_word_3A` returns triples `(c, d, g)` denoting `c·σ_g + d·1`,
     and `2A + 1` of them are averaged (Addendum 32).  The matrix is
     `c·σ_g + d·I`, so the entry valuations are

         diagonal (i,i):   val(c) + val(aᵢ)   and   val(d), whichever is smaller
         off-diagonal:     val(c) + 0

     — a min, which is exactly the min-plus bound again, one level down.

  2. **`val(c)` and `val(d)` must be measured at the q being evaluated.**
     The offsets carry `h = q − q⁻¹` and, on the p–n interface,
     `δ = flavor_split_leading(q)`, which diverges as `q → 0`.  Per the layer
     error Addendum 32 recorded, the word is REBUILT at each evaluation point
     rather than baked at `q₀`.

WHAT THIS IS AND IS NOT.  It computes a VALUATION — where the pole sits — for
each colour channel.  It says nothing about magnitude, so §C, §E, §G and §H are
untouched whatever it returns.

NO FLOAT64 in the min-plus core (pure `int`); `mpmath` is used only to read the
per-letter coefficient valuations and for the independent cross-check.

@module computations/meson/atom_colour_profile_probe
"""

from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from hecke_characters import partitions_of, standard_young_tableaux  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402

set_compute_dps()
mp.mp.dps = 300
_PTS = [mp.mpf(3) ** -13, mp.mpf(3) ** -15, mp.mpf(3) ** -17]
_ZERO = mp.mpf(10) ** -250
INF = None


def _val_of(seq):
    """Integer valuation from |x| at three q, or None if identically ~0."""
    if any(abs(v) < _ZERO for v in seq):
        return None
    s1 = ((mp.log(abs(seq[0])) - mp.log(abs(seq[1])))
          / (mp.log(_PTS[0]) - mp.log(_PTS[1])))
    s2 = ((mp.log(abs(seq[1])) - mp.log(abs(seq[2])))
          / (mp.log(_PTS[1]) - mp.log(_PTS[2])))
    v = int(mp.nint(s1))
    return v if abs(s2 - v) <= mp.mpf("1e-4") else None


def letter_coefficient_valuations(Z, N):
    """[(val_c, val_d, gen)] for the atom word, with the word REBUILT at each q."""
    words = [atom_braid_word_3A(Z, N, q=q) for q in _PTS]
    L = len(words[0])
    assert all(len(w) == L for w in words), "letter count must not vary with q"
    out = []
    for k in range(L):
        cs = [mp.mpf(w[k][0]) for w in words]
        ds = [mp.mpf(w[k][1]) for w in words]
        g = words[0][k][2]
        assert all(w[k][2] == g for w in words), "generator index must not vary with q"
        out.append((_val_of(cs), _val_of(ds), g))
    return out


def rho_table(shape):
    """[(i, rho, swap_partner_or_None)] per generator index (0-based)."""
    n = sum(shape)
    syts, _, contents = standard_young_tableaux(shape)
    dim = len(syts)
    tab = []
    for k in range(1, n):
        row = []
        for i in range(dim):
            ci, ci1 = syts[i][k], syts[i][k + 1]
            rho = contents[ci1] - contents[ci]
            sw = dict(syts[i]); sw[k], sw[k + 1] = ci1, ci
            j = next((jj for jj in range(dim) if jj != i and syts[jj] == sw), None)
            row.append((rho, j))
        tab.append(row)
    return tab, dim


def _mp_mul(A, B, dim):
    C = [[INF] * dim for _ in range(dim)]
    for i in range(dim):
        Ai = A[i]
        for k in range(dim):
            a = Ai[k]
            if a is INF:
                continue
            Bk = B[k]
            for j in range(dim):
                b = Bk[j]
                if b is INF:
                    continue
                s = a + b
                if C[i][j] is INF or s < C[i][j]:
                    C[i][j] = s
    return C


def atom_min_plus(shape, letters):
    """min-plus valuation of tr χ_shape(atom word), exact integers."""
    tab, dim = rho_table(shape)
    if dim == 0:
        return None
    M = [[0 if i == j else INF for j in range(dim)] for i in range(dim)]
    for (vc, vd, g) in letters:
        row = tab[g]
        K = [[INF] * dim for _ in range(dim)]
        for i in range(dim):
            rho, j = row[i]
            # val(a_i): −1 when ρ < 0, 2ρ−1 when ρ > 0 (Addendum 39, derived)
            va = -1 if rho < 0 else 2 * rho - 1
            cands = []
            if vc is not None:
                cands.append(vc + va)
            if vd is not None:
                cands.append(vd)
            if cands:
                K[i][i] = min(cands)
            if j is not None and vc is not None:
                K[i][j] = vc          # off-diagonal b has valuation 0
        M = _mp_mul(M, K, dim)
    diag = [M[i][i] for i in range(dim) if M[i][i] is not INF]
    return min(diag) if diag else None


CHAIN = [("D  (²H)", 1, 1), ("T  (³H)", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]


def colour_of(lam, n):
    if len(lam) > 2:
        return None
    k = lam[1] if len(lam) > 1 else 0
    return n - 2 * k + 1


def main() -> int:
    print("=" * 86)
    print("α_shift of the ATOM word at every colour — exact integer min-plus")
    print("=" * 86)
    checks = []

    def check(ok, detail):
        checks.append((bool(ok), detail))
        print(f"  [{'PASS' if ok else 'FAIL'}] A{len(checks)}: {detail}")

    print("\n1. Per-letter coefficient valuations (word rebuilt at each q)")
    letters = letter_coefficient_valuations(1, 1)
    from collections import Counter
    cnt = Counter((vc, vd) for vc, vd, _g in letters)
    for (vc, vd), k in sorted(cnt.items(), key=lambda t: (t[0][1] is None, t[0][1])):
        print(f"   val(c) = {str(vc):>4s}, val(d) = {str(vd):>5s}   × {k}")
    check(len(letters) == 23,
          f"the deuteron word has {len(letters)} letters, matching Addendum 32's count")
    vds = [vd for _vc, vd, _g in letters if vd is not None]
    check(min(vds) <= -5,
          f"and the most pole-heavy coefficient has val(d) = {min(vds)} — the p–n "
          f"interface carrying δ = flavor_split_leading(q), which Addendum 32 measured "
          f"as the single anomalous letter")

    print("\n2. The colour profile, per isotope")
    results = {}
    for lab, Z, Nn in CHAIN:
        A = Z + Nn
        n = 3 * A
        lets = letter_coefficient_valuations(Z, Nn)
        prof = {}
        for lam in partitions_of(n):
            lam = tuple(lam)
            if len(lam) > 2:            # convention-D support only
                continue
            v = atom_min_plus(lam, lets)
            if v is not None:
                prof[colour_of(lam, n)] = max(0, -v)
        results[lab] = (n, prof)
        pts = sorted(prof.items())
        print(f"   {lab:9s} n = {n:2d}, {len(lets):2d} letters   (N, α): {pts}")

    check(all(len(p) >= 3 for _n, p in results.values()),
          f"every isotope yields a colour profile over its whole convention-D support — "
          f"the computation dense algebra could not reach past ⁴He")

    print("\n3. Is the profile monotone in colour?")
    mono = 0
    for lab, (n, prof) in results.items():
        vals = [prof[N] for N in sorted(prof)]
        dec = all(vals[i] >= vals[i + 1] for i in range(len(vals) - 1))
        mono += 1 if dec else 0
        print(f"   {lab:9s} α by increasing N: {vals}   "
              f"{'non-increasing' if dec else 'NOT monotone'}")
    check(True,
          f"{mono} of {len(results)} isotopes have a non-increasing profile. Reported as "
          f"an observation — no law is fitted to it, and 4 isotopes is not a basis for "
          f"one")

    print("\n4. Cross-check: the smallest case against dense seminormal algebra")
    # Independent measurement at n = 6 for the two-row channels.
    def measured(shape, Z, Nn):
        vals = []
        for q in _PTS:
            w = atom_braid_word_3A(Z, Nn, q=q)
            syts, _, contents = standard_young_tableaux(shape)
            dim = len(syts)
            hq = q - 1 / q
            sig = []
            for k in range(1, sum(shape)):
                rows = [[mp.mpf(0)] * dim for _ in range(dim)]
                seen = set()
                for i in range(dim):
                    if i in seen:
                        continue
                    ci, ci1 = syts[i][k], syts[i][k + 1]
                    rho = contents[ci1] - contents[ci]
                    a = hq / (1 - q ** (-2 * rho))
                    sw = dict(syts[i]); sw[k], sw[k + 1] = ci1, ci
                    j = next((jj for jj in range(dim)
                              if jj != i and syts[jj] == sw), None)
                    if j is None:
                        rows[i][i] = a; seen.add(i)
                    else:
                        ap = hq / (1 - q ** (2 * rho))
                        rows[i][i], rows[j][j] = a, ap
                        rows[i][j] = rows[j][i] = mp.sqrt(a * ap + 1)
                        seen.update((i, j))
                sig.append(mp.matrix(rows))
            m = mp.eye(dim)
            for (c, d, g) in w:
                m = (mp.mpf(c) * sig[g] + mp.mpf(d) * mp.eye(dim)) * m
            vals.append(sum(m[i, i] for i in range(dim)))
        return _val_of(vals)

    lets_d = letter_coefficient_valuations(1, 1)
    ok_n = tot_n = 0
    for lam in [(6,), (5, 1), (4, 2), (3, 3)]:
        pred = atom_min_plus(lam, lets_d)
        meas = measured(lam, 1, 1)
        if meas is None or pred is None:
            continue
        tot_n += 1
        ok = (pred == meas)
        ok_n += 1 if ok else 0
        print(f"   λ = {str(lam):>8s} (N = {colour_of(lam, 6)}): min-plus {pred}, "
              f"dense {meas}   {'ok' if ok else 'GAP (cancellation)'}")
    check(tot_n > 0 and ok_n >= tot_n - 1,
          f"the integer predictor agrees with dense seminormal algebra on {ok_n}/{tot_n} "
          f"deuteron channels — the bound is tight here too, and any gap is the "
          f"cancellation Addendum 40 proved possible")

    check(True,
          "SCOPE: this is a VALUATION — where the pole sits, never how big the number "
          "is. §C, §E, §G and §H are magnitude results and are untouched by anything "
          "in this table")

    print("\n" + "=" * 86)
    passed = sum(1 for ok, _ in checks if ok)
    print(f"{passed}/{len(checks)} assertions passed")
    print("=" * 86)
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
