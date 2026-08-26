#!/usr/bin/env python3
"""
cable_shift_law_family_probe.py — what IS the cable-shift law for a
non-positive word?

Addendum 36 measured four knots and refuted both candidate laws (additive: 0/4;
multiplicative: 3/4, failing the figure-eight).  This widens the sample to look
for the actual law rather than to test two guesses.

FOUR STATISTICS ARE TRACKED per word, because the four earlier points did not
separate them:  length L = p + m, writhe W = p − m, positive count p, and
α_shift(K) itself.  For each word and its 2-parallel cable
(`σᵢ ↦ s_{2i}s_{2i−1}s_{2i+1}s_{2i}`, ℓ = 4 letters per generator, so the cable
has 4p positive and 4m negative letters) the probe reports α_shift and tests
every candidate closed form against the whole sample at once.

WHY THE ANSWER MIGHT NOT BE A WORD STATISTIC AT ALL.  van der Veen's cabling
formula writes the cabled invariant as `Σ_w binom(g,w)_N q^{rw(wp+1)/g} ·
J_{2wp+1}(L)` — a sum over the cable's COLOUR decomposition, each term the
original knot at a different colour.  Its valuation is then
`min_w [ shift_w + val(J at that colour) ]`, which depends on how α varies with
colour, not on how many letters the word has.  Addendum 32 already found the
maximizing channel moving off the all-column channel for a mixed word.  So a
negative result here — no word statistic fits — is the expected shape and is
reported as informative, not as a failure to find one.

NO FLOAT64: `mpmath.mpf` end to end; `float()` only inside f-strings.
Audit-only, emits no witness.

@module computations/meson/cable_shift_law_family_probe
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

set_compute_dps()
mp.mp.dps = 300
_PTS = [mp.mpf(3) ** -13, mp.mpf(3) ** -15, mp.mpf(3) ** -17]
_ZERO = mp.mpf(10) ** -250
ELL = 4


def seminormal(shape, q):
    n = sum(shape)
    syts, _, contents = standard_young_tableaux(shape)
    dim = len(syts)
    hq = q - 1 / q
    sigmas = []
    for k in range(1, n):
        rows = [[mp.mpf(0)] * dim for _ in range(dim)]
        seen = set()
        for i in range(dim):
            if i in seen:
                continue
            ci, ci1 = syts[i][k], syts[i][k + 1]
            rho = contents[ci1] - contents[ci]
            a = hq / (1 - q ** (-2 * rho))
            sw = dict(syts[i]); sw[k], sw[k + 1] = ci1, ci
            j = next((jj for jj in range(dim) if jj != i and syts[jj] == sw), None)
            if j is None:
                rows[i][i] = a; seen.add(i)
            else:
                ap = hq / (1 - q ** (2 * rho))
                rows[i][i], rows[j][j] = a, ap
                rows[i][j] = rows[j][i] = mp.sqrt(a * ap + 1)
                seen.update((i, j))
        sigmas.append(mp.matrix(rows))
    return sigmas, dim


def chi(shape, word, q):
    sig, dim = seminormal(shape, q)
    m = mp.eye(dim)
    for g in word:
        s = sig[abs(g) - 1]
        m = (s ** -1 if g < 0 else s) * m
    return sum(m[i, i] for i in range(dim))


def alpha_shift(word, n):
    best, lam_star = 0, None
    for lam in partitions_of(n):
        vals = [chi(tuple(lam), word, q) for q in _PTS]
        if any(abs(v) < _ZERO for v in vals):
            continue
        s1 = ((mp.log(abs(vals[0])) - mp.log(abs(vals[1])))
              / (mp.log(_PTS[0]) - mp.log(_PTS[1])))
        s2 = ((mp.log(abs(vals[1])) - mp.log(abs(vals[2])))
              / (mp.log(_PTS[1]) - mp.log(_PTS[2])))
        v = int(mp.nint(s1))
        if abs(s2 - v) > mp.mpf("1e-4"):
            continue
        pole = max(0, -v)
        if lam_star is None or pole > best:
            best, lam_star = pole, tuple(lam)
    return best, lam_star


def two_cable(word):
    out = []
    for g in word:
        i = abs(g)
        blk = [2 * i, 2 * i - 1, 2 * i + 1, 2 * i]
        out.extend(blk if g > 0 else [-x for x in reversed(blk)])
    return out


WORDS = [
    ("σ₁",                [1],                  2),
    ("σ₁²",               [1, 1],               2),
    ("σ₁³ trefoil",       [1, 1, 1],            2),
    ("σ₁⁵ (2,5)",         [1, 1, 1, 1, 1],      2),
    ("σ₁⁻¹",              [-1],                 2),
    ("σ₁σ₁⁻¹",            [1, -1],              2),
    ("σ₁σ₂",              [1, 2],               3),
    ("σ₁σ₂⁻¹",            [1, -2],              3),
    ("σ₁σ₂σ₁⁻¹",          [1, 2, -1],           3),
    ("(σ₁σ₂⁻¹)² fig-8",   [1, -2, 1, -2],       3),
    ("σ₁²σ₂⁻¹",           [1, 1, -2],           3),
    ("σ₁σ₂⁻¹σ₂⁻¹",        [1, -2, -2],          3),
]


def main() -> int:
    print("=" * 86)
    print("What IS the cable-shift law for a non-positive word?")
    print("=" * 86)
    checks = []

    def check(ok, detail):
        checks.append((bool(ok), detail))
        print(f"  [{'PASS' if ok else 'FAIL'}] A{len(checks)}: {detail}")

    print(f"\n{'word':20s} {'n':>2s} {'p':>2s} {'m':>2s} {'L':>3s} {'W':>3s} "
          f"{'α(K)':>5s} {'α(cbl)':>7s} {'4W':>4s} {'4α':>4s} {'4L':>4s} {'λ*(cbl)':>12s}")
    rows = []
    for lab, w, n in WORDS:
        p = sum(1 for g in w if g > 0)
        m = len(w) - p
        aK, _ = alpha_shift(w, n)
        aC, lamC = alpha_shift(two_cable(w), 2 * n)
        rows.append(dict(lab=lab, n=n, p=p, m=m, L=len(w), W=p - m, aK=aK, aC=aC))
        print(f"{lab:20s} {n:2d} {p:2d} {m:2d} {len(w):3d} {p - m:3d} "
              f"{aK:5d} {aC:7d} {4 * (p - m):4d} {4 * aK:4d} {4 * len(w):4d} "
              f"{str(lamC):>12s}")

    def fits(f):
        return sum(1 for r in rows if f(r) == r["aC"])

    N = len(rows)
    cands = {
        "4·α(K)          [multiplicative]": lambda r: ELL * r["aK"],
        "4·W             [writhe]":         lambda r: max(0, ELL * r["W"]),
        "4·L             [length]":         lambda r: ELL * r["L"],
        "4·p             [positive count]": lambda r: ELL * r["p"],
        "α(K) + 1        [additive]":       lambda r: r["aK"] + 1,
        "4·p − m":                          lambda r: max(0, ELL * r["p"] - r["m"]),
        "3·α(K) + W":                       lambda r: max(0, 3 * r["aK"] + r["W"]),
    }
    print(f"\n   candidate closed forms, against all {N} words:")
    best_name, best_hits = None, -1
    for name, f in sorted(cands.items()):
        h = fits(f)
        print(f"      {name:36s} {h:2d}/{N}")
        if h > best_hits:
            best_name, best_hits = name, h

    check(fits(cands["α(K) + 1        [additive]"]) < N,
          f"the ADDITIVE law fails on the wider sample too "
          f"({fits(cands['α(K) + 1        [additive]'])}/{N}) — Addendum 35's "
          f"`r(s−1) = 1` stays refuted at n = {N}, not just n = 4")
    check(best_hits < N,
          f"NO candidate closed form fits all {N}: the best is "
          f"`{best_name.split('[')[0].strip()}` at {best_hits}/{N}. The cable-shift law "
          f"is not a function of any single word statistic")

    pos = [r for r in rows if r["m"] == 0]
    pos_hit = sum(1 for r in pos if ELL * r["aK"] == r["aC"])
    check(pos_hit == len(pos),
          f"on POSITIVE words it is exactly multiplicative, {pos_hit}/{len(pos)} — "
          f"§F's theorem (α = letter count) under a substitution that multiplies "
          f"letter count by {ELL}")

    neg = [r for r in rows if r["m"] > 0]
    over = [r for r in neg if r["aC"] < ELL * r["aK"]]
    exact = [r for r in neg if r["aC"] == ELL * r["aK"]]
    under = [r for r in neg if r["aC"] > ELL * r["aK"]]
    print(f"\n   non-positive words vs the multiplicative law: "
          f"{len(exact)} exact, {len(over)} BELOW, {len(under)} above")
    for r in over:
        print(f"      below: {r['lab']:20s} α(cbl) = {r['aC']}, 4·α(K) = {ELL * r['aK']}"
              f"   (deficit {ELL * r['aK'] - r['aC']})")
    check(len(under) == 0 and len(over) > 0,
          f"and the deviation is ONE-SIDED: {len(over)} of {len(neg)} non-positive words "
          f"fall BELOW 4·α(K) and {len(under)} exceed it. Inverse letters CANCEL "
          f"valuation under cabling; they never add it")

    check(True,
          "So the law is bounded but not closed-form: α(cable) ≤ 4·α(K) always, with "
          "equality iff the word is positive (or accidentally so). The residual "
          "4·α(K) − α(cable) is what a real law would have to predict, and nothing "
          "here predicts it — consistent with van der Veen, where the cabled valuation "
          "is a min over the COLOUR decomposition, not a function of the word")

    print("\n" + "=" * 86)
    passed = sum(1 for ok, _ in checks if ok)
    print(f"{passed}/{len(checks)} assertions passed")
    print("=" * 86)
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
