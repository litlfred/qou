"""Cross-check for the all-n Temperley-Lieb weight-vanishing lemma.

Establishes, exactly and symbolically over Q(q), the three arithmetic facts the
Lean file `QOU/QBeta/WenzlWeightVanishing.lean` is stated against:

  1. Convention D's Markov parameter `z_D = q^3/(q^2+1)` is exactly Wenzl's
     level `r = 2`:  `Q^r = q*z/(1 - Q + q*z) = q^4 = Q^2` with `Q = q^2`.
     (Already recorded in `schur_principal_mpmath._wenzl_constants`; reproduced
     here from scratch so the Lean statement rests on a re-derivation.)

  2. The level-2 hook-content principal specialisation
        s_lam = Q^{n(lam)} * prod_{x in lam} (1 - Q^{2 + c(x)}) / (1 - Q^{h(x)})
     normalised by `Z = sum_mu f^mu s_mu` reproduces the corpus weights:
       - the n = 3 triple  (q^4+1)/(q^2+1)^2,  q^2/(q^2+1)^2,  0   [PR #5185]
       - the Lean closed form `yw = [n-2k+1]_q / [2]_q^n`
         (`TemperleyLiebTower.yw`) for every two-row lam, n = 2..7.

  3. `sum (dim V_lam)^2` over lam with >= 3 rows equals `n! - Catalan(n)`,
     i.e. the measured coranks 1, 10, 78, 588 at n = 3, 4, 5, 6  [PR #5207].

NO FLOAT64 ANYWHERE: everything is sympy exact over Q(q).
"""

from __future__ import annotations

import json
import math
from itertools import count

import sympy as sp
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

q = sp.symbols("q", positive=True)
Q = q**2


def partitions(n: int, cap: int | None = None):
    if cap is None:
        cap = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, cap), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def cells(lam):
    return [(i, j) for i, row in enumerate(lam) for j in range(row)]


def hook(lam, i, j):
    arm = lam[i] - j - 1
    leg = sum(1 for r in lam if r > j) - i - 1
    return arm + leg + 1


def n_partition(lam):
    return sum(i * row for i, row in enumerate(lam))


def f_lambda(lam):
    n = sum(lam)
    prod = 1
    for (i, j) in cells(lam):
        prod *= hook(lam, i, j)
    return math.factorial(n) // prod


def schur_principal(lam, r):
    """Q^{n(lam)} * prod (1 - Q^{r+c}) / (1 - Q^h) -- the corpus closed form."""
    num, den = sp.Integer(1), sp.Integer(1)
    for (i, j) in cells(lam):
        num *= 1 - Q ** (r + j - i)
        den *= 1 - Q ** hook(lam, i, j)
    return sp.cancel(Q ** n_partition(lam) * num / den)


def y_lambda(n, r=2):
    s = {lam: schur_principal(lam, r) for lam in partitions(n)}
    Z = sp.cancel(sum(s[lam] * f_lambda(lam) for lam in s))
    return {lam: sp.cancel(s[lam] / Z) for lam in s}, Z


def qint(m):
    """Balanced quantum integer [m]_q = (q^m - q^-m)/(q - q^-1)."""
    return sp.cancel((q**m - q ** (-m)) / (q - q ** (-1)))


def catalan(n):
    return math.comb(2 * n, n) // (n + 1)


# --- 0. the Lean file's definitions agree with the corpus arm/leg ones ------
# WenzlWeightVanishing.lean states hook/content/nPart via YoungDiagram's
# `rowLen` and `colLen`, not via arm/leg. That transcription is the one place
# a silent divergence could hide, so it is checked rather than eyeballed.

def row_len(lam, i):
    return lam[i] if i < len(lam) else 0


def col_len(lam, j):
    return sum(1 for r in lam if r > j)


def hook_lean(lam, i, j):
    """(rowLen i - j) + (colLen j - i) - 1, exactly as the Lean `hook`."""
    return (row_len(lam, i) - j) + (col_len(lam, j) - i) - 1


def n_part_lean(lam):
    """sum over cells of the 0-indexed row index, exactly as the Lean `nPart`."""
    return sum(i for (i, j) in cells(lam))


_checked = 0
for _n in range(1, 9):
    for _lam in partitions(_n):
        assert n_part_lean(_lam) == n_partition(_lam), f"nPart {_lam}"
        for (_i, _j) in cells(_lam):
            assert hook_lean(_lam, _i, _j) == hook(_lam, _i, _j), f"hook {_lam} {_i},{_j}"
            assert (_j - _i) == (_j - _i)  # content: Lean `j - i`, identical
            _checked += 1
print(f"0. Lean rowLen/colLen definitions == corpus arm/leg, {_checked} cells  OK")

report = {"lean_definition_transcription": {"cells_checked": _checked, "all_match": True}}

# --- 1. z_D is Wenzl level r = 2 -------------------------------------------
z_D = q**3 / (q**2 + 1)
QR = sp.cancel(q * z_D / (1 - Q + q * z_D))
report["wenzl_level"] = {
    "z_D": str(sp.factor(z_D)),
    "Q_to_the_r": str(sp.factor(QR)),
    "equals_Q_squared": bool(sp.simplify(QR - Q**2) == 0),
}
assert sp.simplify(QR - Q**2) == 0, "z_D is not Wenzl level 2"
print(f"1. Q^r = {sp.factor(QR)} = Q^2  ->  r = 2 exactly   OK")

# --- 2a. n = 3 against PR #5185's symbolic solve ----------------------------
y3, _Z3 = y_lambda(3)
expected3 = {
    (3,): (q**4 + 1) / (q**2 + 1) ** 2,
    (2, 1): q**2 / (q**2 + 1) ** 2,
    (1, 1, 1): sp.Integer(0),
}
n3 = {}
for lam, want in expected3.items():
    got = y3[lam]
    ok = sp.simplify(got - want) == 0
    n3["".join(map(str, lam))] = {"got": str(sp.factor(got)), "matches_5185": bool(ok)}
    assert ok, f"n=3 mismatch at {lam}: {sp.factor(got)} vs {sp.factor(want)}"
report["n3_vs_pr5185"] = n3
print("2a. n=3 weights reproduce PR #5185 exactly                  OK")

# --- 2b. two-row closed form yw = [n-2k+1]_q / [2]_q^n ----------------------
two_row = []
bracket2 = q + 1 / q
for n in range(2, 8):
    ys, _ = y_lambda(n)
    for lam, val in ys.items():
        if len(lam) <= 2:
            k = lam[1] if len(lam) == 2 else 0
            want = sp.cancel(qint(n - 2 * k + 1) / bracket2**n)
            ok = sp.simplify(val - want) == 0
            two_row.append({"n": n, "lam": list(lam), "matches_yw": bool(ok)})
            assert ok, f"yw mismatch n={n} lam={lam}"
        else:
            assert sp.simplify(val) == 0, f"expected 0 at {lam}"
report["two_row_vs_lean_yw"] = {
    "checked": len(two_row),
    "all_match": all(t["matches_yw"] for t in two_row),
}
print(f"2b. {len(two_row)} two-row weights match Lean `yw`          OK")

# --- 2c. vanishing is exactly the >= 3-row set ------------------------------
van = []
for n in range(1, 9):
    ys, _ = y_lambda(n)
    for lam, val in ys.items():
        is_zero = sp.simplify(val) == 0
        assert is_zero == (len(lam) >= 3), f"vanishing mismatch n={n} lam={lam}"
    van.append({"n": n, "partitions": len(ys)})
report["vanishing_iff_three_rows"] = {"n_range": [1, 8], "all_ok": True, "levels": van}
print("2c. y_lam = 0 <=> lam has >= 3 rows, n = 1..8               OK")

# --- 3. corank arithmetic ---------------------------------------------------
cor = []
for n in range(3, 9):
    dead = sum(f_lambda(lam) ** 2 for lam in partitions(n) if len(lam) >= 3)
    want = math.factorial(n) - catalan(n)
    assert dead == want, f"corank mismatch at n={n}"
    cor.append({"n": n, "sum_dim_sq_ge3rows": dead, "n_fact_minus_catalan": want})
report["corank"] = cor
print("3. corank = n! - Catalan(n) from the >= 3-row blocks, n=3..8 OK")
print("   ", [c["sum_dim_sq_ge3rows"] for c in cor])

out = "computations/probes/wenzl-level-two-vanishing.json"
# Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
# `os.replace` it into position. `open(..., "w")` TRUNCATES before the
# dump runs, so any exception in between leaves the committed witness
# empty or partial -- the shape that emptied 22 witnesses to zero bytes
# in one `producer_importability_audit` run. `os.replace` is atomic on
# POSIX within a filesystem, hence a SIBLING temp file.
_wpath_sidu = out
_wtmp_sidu = str(_wpath_sidu) + ".tmp"
with open(_wtmp_sidu, "w") as fh:
    json.dump(report, fh, indent=2, sort_keys=True)
_os_sidu.replace(_wtmp_sidu, _wpath_sidu)
print(f"\nwrote {out}")
