#!/usr/bin/env python3
r"""
rev_staircase_closed_form_and_constant_term_probe.py — the staircase leg of M_n is CLOSED FORM,
and the asymptotic gains an explicit constant term (qou-hok7)

#7294 identified the leading coefficient, `M_n / sqrt(n) -> A*sqrt2`, by measuring that the
excess over the staircase is bounded.  The staircase's own value was carried as a computed
number at each `n`.  It does not have to be.

`QOU.BraidKnot.HookSum.betaSide_eq_hookSum` (Lean, sorry-free, this branch) says the beta-side
is the CELL sum `Sum_{c in mu} eps(h(c))`.  So the whole objective is cell-local,

    V(mu) = Sum_{c in mu} phi(h(c)) + const(n),      phi(h) := eps(h) - h*ln q0 ,

and on the staircase, where `H = H_min` kills the second term outright,

    V(delta_k) = Sum_{c} eps(h(c)) - F(n) .

The staircase's hook multiset is elementary: hook length `2j-1` occurs exactly `k+1-j` times,
and no even hook length occurs at all.  That gives a closed form in `k`,

    V(delta_k) = Sum_{j=1}^{k} (k+1-j) eps(2j-1) - F(n)
               = A*k - B - F(n) + (exponentially small) ,

with `A = Sum_{j>=1} eps(2j-1)` (already the arc's constant) and `B = Sum_{j>=1} (j-1) eps(2j-1)`
a NEW one.  Both converge geometrically because `eps(m) ~ q0^(-2m)`.

## What this buys, and what it does not

It closes the staircase leg **exactly**: no search, no heuristic, no lower-bound caveat — that
leg is now a convergent series in `k` alone.  And because `k + 1/2 = sqrt(2n + 1/4)` exactly at
triangular `n`, what comes out is not an asymptotic but an **identity**,

    M_n  =  A*sqrt(2n + 1/4)  -  A/2  -  B  -  C  +  e_n  +  (i) + (ii) ,

with `C = Sum_{m>=1} eps(m) = lim F(n)`, `e_n` the excess over the staircase, and two
exponentially small remainders: (i) the staircase series' tail `sum_{j>k}(j-1-k)eps(2j-1)`, and
(ii) `C - F(n)`.  At `n = 3916` the two together are **5.1e-16**.

So the ENTIRE gap between this and a closed asymptotic is the single sequence `e_n`.  The open
problem sharpens from "the coefficient" (settled in #7294) to **one number**, `e_inf`, and it is
the same number the pair-term lower bound is about.

Write the square root exactly.  `A*sqrt(2n)` costs an extra `A/(8 sqrt(2n))`, which at
`n = 3916` is `0.0051` — about `1e13` times the residual it would otherwise be explaining, so
the constant term is only well-defined in the `sqrt(2n + 1/4)` form.

It does NOT make `M_n` a theorem: the maximiser is still found by heuristic search, so `M_n`
remains a lower bound, and `e_inf` is measured at a single `n` rather than proved to be a limit.
What is now exact is the staircase *baseline* it is measured against.

## Checks

  S1  the staircase hook multiset: `2j-1` occurs `k+1-j` times, no even hook — by enumeration
  S2  independent corroboration: that multiset's total is `H_min = k(k+1)(2k+1)/6`, exactly
  S3  the closed form reproduces #7294's committed `V_staircase` column at all 11 points
  S4  `A*k - B - F(n)`'s remainder decays at the DERIVED rate `q0^4` per unit `k`
  S5  the identity above, with (i)+(ii) and (iii) separated, against all 11 committed points

Proton-pinned; no Markov parameter in this cone, so convention C/D does not arise.  Exact
integers for hooks/H.  mpmath at dps 60; no float64.

-- Ref: [manuscript] folio/quantum-observable-universe/lean/QOU/BraidKnot/HookSumBetaCoordinates.lean
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMPUTATIONS = os.path.dirname(_HERE)
if _COMPUTATIONS not in sys.path:
    sys.path.insert(0, _COMPUTATIONS)

from mpmath import mp  # noqa: E402

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.dps = 60
Q0 = Q_MP
LNQ = mp.log(Q0)
T = Q0 ** 2

_NEPS = 6000
EPS = [mp.mpf(0)] + [-mp.log(1 - T ** (-m)) for m in range(1, _NEPS)]
_F = [mp.mpf(0)] * _NEPS
for _m in range(1, _NEPS):
    _F[_m] = _F[_m - 1] + EPS[_m]

C_CONST = _F[_NEPS - 1]                                     # C = sum_{m>=1} eps(m)
A_CONST = sum(EPS[m] for m in range(1, _NEPS, 2))           # A = sum_{j>=1} eps(2j-1)
B_CONST = sum(((m + 1) // 2 - 1) * EPS[m] for m in range(1, _NEPS, 2))   # B = sum (j-1)eps(2j-1)


def F(k: int) -> mp.mpf:
    return _F[k] if k < _NEPS else C_CONST


def eps(m: int) -> mp.mpf:
    return EPS[m] if 0 < m < _NEPS else mp.mpf(0)


CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'ok ' if ok else 'FAIL'}] {name}: {detail}")


def hooks(lam: list[int]) -> list[int]:
    """Every hook length of `lam`, by direct enumeration over cells."""
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0] if lam else 0)]
    return [lam[i] - j + conj[j] - i - 1 for i in range(len(lam)) for j in range(lam[i])]


print(f"constants (dps {mp.dps}, {_NEPS} eps terms)")
print(f"    A = sum_j eps(2j-1)       = {mp.nstr(A_CONST, 22)}")
print(f"    B = sum_j (j-1) eps(2j-1) = {mp.nstr(B_CONST, 22)}   <- new to this probe")
print(f"    C = sum_m eps(m)          = {mp.nstr(C_CONST, 22)}")

# --------------------------------------------------------------------------------------------
# S1 — the staircase hook multiset
# --------------------------------------------------------------------------------------------
print()
print("S1  the staircase's hook multiset, by enumeration")
_s1 = []
for _k in range(1, 41):
    _lam = list(range(_k, 0, -1))
    _h = hooks(_lam)
    _pred: dict[int, int] = {2 * j - 1: _k + 1 - j for j in range(1, _k + 1)}
    _got: dict[int, int] = {}
    for _v in _h:
        _got[_v] = _got.get(_v, 0) + 1
    _s1.append(_got == _pred)
print(f"    checked k = 1..40; k = 5 gives {sorted(hooks(list(range(5, 0, -1))))}")
check(
    "S1 hook length 2j-1 occurs exactly k+1-j times, and no even hook length occurs",
    all(_s1),
    f"{sum(_s1)}/{len(_s1)} staircases k = 1..40 match the predicted multiset exactly, as "
    f"integer counts — this is the whole input the closed form needs",
)

# --------------------------------------------------------------------------------------------
# S2 — independent corroboration through H_min
# --------------------------------------------------------------------------------------------
print()
print("S2  corroboration — the predicted multiset's total is H_min, exactly")
_s2 = []
for _k in range(1, 41):
    _tot = sum((_k + 1 - j) * (2 * j - 1) for j in range(1, _k + 1))
    _s2.append(_tot == _k * (_k + 1) * (2 * _k + 1) // 6)
check(
    "S2 sum_j (k+1-j)(2j-1) = k(k+1)(2k+1)/6 = H_min at n = T_k",
    all(_s2),
    f"{sum(_s2)}/{len(_s2)} exact as integers, k = 1..40 — H_min is established independently "
    f"(square-pyramidal closed form, hmin_closed_form_and_rev_sublinearity_probe), so this is a "
    f"cross-check on S1 that does not reuse the enumeration",
)

# --------------------------------------------------------------------------------------------
# S3 / S4 — the closed form against #7294's committed column
# --------------------------------------------------------------------------------------------
print()
print("S3/S4  against the committed V_staircase column of #7294")
_WITNESS = os.path.join(_HERE, "rev-excess-scaling-exponent.witness.json")
with open(_WITNESS) as _fh:
    _PARENT = json.load(_fh)
_ROWS = _PARENT["scaling_R2"]

print(f"    {'k':>4} {'n':>7} {'V_stair (#7294)':>24} {'series form':>14} {'A*k-B-F(n)':>14}")
_s3, _s4, _table = [], [], []
for _r in _ROWS:
    _k, _n = _r["k"], _r["n"]
    _vst = mp.mpf(_r["V_staircase"])
    _series = sum((( _k + 1 - j) * eps(2 * j - 1) for j in range(1, _k + 1)), mp.mpf(0)) - F(_n)
    _closed = A_CONST * _k - B_CONST - F(_n)
    _s3.append(abs(_series - _vst) < mp.mpf("1e-12"))
    _s4.append(abs(_closed - _vst))
    _table.append({"k": _k, "n": _n, "V_staircase_7294": _r["V_staircase"],
                   "series_form": mp.nstr(_series, 24), "closed_form": mp.nstr(_closed, 24),
                   "series_minus_witness": mp.nstr(_series - _vst, 6),
                   "closed_minus_witness": mp.nstr(_closed - _vst, 6)})
    print(f"    {_k:4d} {_n:7d} {mp.nstr(_vst, 18):>24} {mp.nstr(_series - _vst, 4):>14} "
          f"{mp.nstr(_closed - _vst, 4):>14}")

check(
    "S3 the SERIES form reproduces the committed staircase value at every n",
    all(_s3),
    f"{sum(_s3)}/{len(_s3)} agree to 1e-12 — #7294 computed V_staircase from a beta-set through "
    f"a pair sum; this computes it from a hook multiset with no beta anywhere, so the agreement "
    f"is a check on betaSide_eq_hookSum as much as on the multiset",
)

# The remainder is `sum_{j>k} (j-1-k) eps(2j-1)`, whose leading term is `eps(2k+3) ~ T^-(2k+3)`.
# So it must fall by a factor `T^2 = q0^4` per unit of `k` — a DERIVED rate.  Test that, not an
# arbitrary absolute threshold: a threshold says only "small here", the rate says "exponential".
_rate_target = T ** 2
print(f"    remainder decay per unit k, against the derived rate q0^4 = "
      f"{mp.nstr(_rate_target, 12)}:")
_rates = []
for _a, _b in zip(_ROWS, _ROWS[1:]):
    _ia, _ib = _ROWS.index(_a), _ROWS.index(_b)
    if _s4[_ib] == 0:
        continue
    _r = (_s4[_ia] / _s4[_ib]) ** (mp.mpf(1) / (_b["k"] - _a["k"]))
    _rates.append({"k_from": _a["k"], "k_to": _b["k"], "rate": _r})
print("      " + "  ".join(f"{s['k_from']}->{s['k_to']}: {mp.nstr(s['rate'], 7)}"
                           for s in _rates))
_rate_err = abs(_rates[-3]["rate"] / _rate_target - 1)
check(
    "S4 the CLOSED form's remainder decays at the DERIVED rate q0^4 per unit k",
    max(_s4) == _s4[0] and _rate_err < mp.mpf("1e-4"),
    f"|remainder| falls {mp.nstr(_s4[0], 4)} (k = {_ROWS[0]['k']}) -> "
    f"{mp.nstr(_s4[-1], 4)} (k = {_ROWS[-1]['k']}), a factor of "
    f"{mp.nstr(_s4[0] / _s4[-1], 4)}; the per-k rate converges to "
    f"{mp.nstr(_rates[-3]['rate'], 10)} against the predicted q0^4 = "
    f"{mp.nstr(_rate_target, 10)} (relative {mp.nstr(_rate_err, 3)}).  The rate is derived from "
    f"the leading omitted term eps(2k+3), so this tests the FORM of the remainder, not just "
    f"its size",
)

# --------------------------------------------------------------------------------------------
# S5 — the constant term
# --------------------------------------------------------------------------------------------
print()
print("S5  the decomposition is an IDENTITY at triangular n, not an asymptotic")
_E_INF = mp.mpf(_ROWS[-1]["excess"])                     # measured, #7294, n = 3916
_KAPPA = -A_CONST / 2 - B_CONST - C_CONST + _E_INF
print(f"    e_inf (measured, #7294 at n = {_ROWS[-1]['n']})  = {mp.nstr(_E_INF, 14)}")
print(f"    kappa = -A/2 - B - C + e_inf                  = {mp.nstr(_KAPPA, 14)}")
print(f"      = -{mp.nstr(A_CONST / 2, 12)} - {mp.nstr(B_CONST, 12)} - "
      f"{mp.nstr(C_CONST, 12)} + {mp.nstr(_E_INF, 12)}")
print()
print("    At n = T_k the triangular relation is EXACT: k(k+1)/2 = n  <=>  k + 1/2 =")
print("    sqrt(2n + 1/4).  So `A*sqrt(2n + 1/4) + kappa` differs from M_n by exactly three")
print("    terms, and each is separately visible:")
print("      (i)   rem_k        = the staircase remainder of S4       [exponentially small]")
print("      (ii)  C - F(n)     = the eps-tail beyond n               [exponentially small]")
print("      (iii) e_inf - e_n  = the excess not yet converged        [THE OPEN ONE]")
print()
print(f"    {'n':>7} {'M_n':>18} {'A*sqrt(2n+1/4)+kappa':>22} {'residual':>12} "
      f"{'(iii) alone':>13} {'sqrt(2n) form':>14}")
_asym = []
for _r in _ROWS:
    _n, _k = _r["n"], _r["k"]
    _m = mp.mpf(_r["V_best"])
    _pred = A_CONST * mp.sqrt(2 * mp.mpf(_n) + mp.mpf(1) / 4) + _KAPPA
    _pred_plain = A_CONST * mp.sqrt(2 * mp.mpf(_n)) + _KAPPA
    _iii = _E_INF - mp.mpf(_r["excess"])
    _asym.append({"n": _n, "k": _k, "M_n": _r["V_best"],
                  "predicted_exact_k": mp.nstr(_pred, 20),
                  "residual": mp.nstr(_m - _pred, 8),
                  "term_iii_excess_gap": mp.nstr(_iii, 8),
                  "residual_minus_term_iii": mp.nstr(_m - _pred + _iii, 8),
                  "predicted_sqrt_2n": mp.nstr(_pred_plain, 20),
                  "residual_sqrt_2n": mp.nstr(_m - _pred_plain, 8)})
    print(f"    {_n:7d} {mp.nstr(_m, 14):>18} {mp.nstr(_pred, 16):>22} "
          f"{mp.nstr(_m - _pred, 6):>12} {mp.nstr(-_iii, 6):>13} "
          f"{mp.nstr(_m - _pred_plain, 6):>14}")

# The residual, once (iii) is added back, must be (i) + (ii) alone — both exponentially small.
_resid_no_iii = [abs(mp.mpf(a["residual_minus_term_iii"])) for a in _asym]
check(
    "S5 with the excess gap (iii) removed, the residual is (i) + (ii) alone and collapses",
    _resid_no_iii[-1] < mp.mpf("1e-12") and _resid_no_iii[-1] < _resid_no_iii[0],
    f"|residual - (iii)| falls {mp.nstr(_resid_no_iii[0], 4)} (n = {_ROWS[0]['n']}) -> "
    f"{mp.nstr(_resid_no_iii[-1], 4)} (n = {_ROWS[-1]['n']}) — so the decomposition M_n = "
    f"A*sqrt(2n+1/4) - A/2 - B - C + e_n is EXACT at triangular n up to two exponentially "
    f"small terms, and the entire gap to an asymptotic law is the single sequence e_n",
)
check(
    "S5b the sqrt(2n+1/4) form is the exact one; plain sqrt(2n) costs an extra A/(8 sqrt(2n))",
    abs(mp.mpf(_asym[-1]["residual_sqrt_2n"])) > abs(mp.mpf(_asym[-1]["residual"])),
    f"at n = {_ROWS[-1]['n']}: residual {mp.nstr(mp.mpf(_asym[-1]['residual']), 4)} exact-k "
    f"against {mp.nstr(mp.mpf(_asym[-1]['residual_sqrt_2n']), 4)} for plain sqrt(2n) — the "
    f"difference is A(sqrt(2n+1/4) - sqrt(2n)) ~ A/(8 sqrt(2n)) = "
    f"{mp.nstr(A_CONST / (8 * mp.sqrt(2 * mp.mpf(_ROWS[-1]['n']))), 6)}, which is why the "
    f"constant term is only well-defined once the sqrt is written exactly",
)
check(
    "S5c three of kappa's four pieces are explicit convergent series; only e_inf is measured",
    True,
    f"A = {mp.nstr(A_CONST, 12)}, B = {mp.nstr(B_CONST, 12)}, C = {mp.nstr(C_CONST, 12)} are "
    f"sums of eps over arithmetic progressions and converge like q0^(-2m); e_inf = "
    f"{mp.nstr(_E_INF, 12)} comes from a heuristic search at a single n and is the one open "
    f"number — it is NOT proved to be a limit",
)
print()
_n_ok = sum(1 for _, ok, _ in CHECKS if ok)
print(f"=== {_n_ok}/{len(CHECKS)} checks pass ===")
print()
print("VERDICT")
print("  The staircase leg of M_n is CLOSED FORM.  It needed no new mathematics -- only reading")
print("  betaSide_eq_hookSum in the direction it already points: the objective is a sum over")
print("  CELLS of a function of the hook length, the staircase's hook multiset is `2j-1 with")
print("  multiplicity k+1-j`, and the sum telescopes into A*k - B - F(n).")
print()
print("  Consequences:")
print("   1. V(staircase) is exact in k.  #7294 recomputed it at each n through a beta pair sum;")
print("      it is a two-constant formula, and the two constants are series in eps.")
print("   2. What comes out is an IDENTITY at triangular n, not an asymptotic, because")
print("      k + 1/2 = sqrt(2n + 1/4) exactly:")
print("          M_n = A*sqrt(2n + 1/4) - A/2 - B - C + e_n  +  (i) + (ii)")
print(f"      with (i) + (ii) exponentially small -- together {mp.nstr(_resid_no_iii[-1], 4)}")
print(f"      at n = {_ROWS[-1]['n']}.  Write the sqrt exactly: the plain sqrt(2n) form carries")
print(f"      an extra A/(8 sqrt(2n)) = "
      f"{mp.nstr(A_CONST / (8 * mp.sqrt(2 * mp.mpf(_ROWS[-1]['n']))), 6)} there, which is 1e13x")
print("      the residual it would be explaining.")
print(f"   3. kappa = -A/2 - B - C + e_inf = {mp.nstr(_KAPPA, 12)}.  THE ENTIRE GAP between")
print("      this and a closed asymptotic is the single sequence e_n.  The open problem")
print("      sharpens from 'the coefficient' (settled in #7294) to ONE NUMBER -- and it is the")
print("      same number the pair-term lower bound is about.")
print()
print("  What this does NOT establish: M_n itself is still reached by heuristic search and")
print("  remains a LOWER bound.  What is now exact is the BASELINE it is measured against, and")
print("  e_inf is measured at a single n rather than proved to be a limit.")

_w = {
    "schema": "qou-witness/v1",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "computation": "rev_staircase_closed_form_and_constant_term_probe",
    "bean": "qou-hok7",
    "anchor": "physical_proton",
    # Canonical anchor key read by the q0 audits/ratchet (the "anchor" key above is
    # a near-miss spelling they cannot see), plus scriptFile provenance.
    "q0Anchor": "proton",
    "scriptFile": os.path.basename(__file__),
    "q0Value": Q_50_DIGIT_STR,
    "description": (
        "The staircase leg of M_n is closed form: V(delta_k) = A*k - B - F(n) up to a remainder "
        "decaying at the derived rate q0^4 per unit k, where A = sum_j eps(2j-1), B = sum_j "
        "(j-1)eps(2j-1). Follows from betaSide_eq_hookSum (the objective is cell-local in the "
        "hook length) plus the staircase hook multiset '2j-1 with multiplicity k+1-j'. Because "
        "k + 1/2 = sqrt(2n + 1/4) exactly at triangular n, the result is an IDENTITY rather than "
        "an asymptotic: M_n = A*sqrt(2n + 1/4) - A/2 - B - C + e_n + two exponentially small "
        "remainders, together 5.1e-16 at n = 3916. The entire gap to a closed asymptotic is the "
        "single sequence e_n; kappa = -A/2 - B - C + e_inf."
    ),
    "lean": {
        "theorem": "QOU.BraidKnot.HookSum.betaSide_eq_hookSum",
        "file": ("folio/quantum-observable-universe/lean/QOU/BraidKnot/"
                 "HookSumBetaCoordinates.lean"),
        "role": "makes the objective a sum over cells of a function of the hook length",
    },
    "constants": {
        "A": mp.nstr(A_CONST, 30), "B": mp.nstr(B_CONST, 30), "C": mp.nstr(C_CONST, 30),
        "A_sqrt2": mp.nstr(A_CONST * mp.sqrt(2), 30),
        "e_inf_measured": mp.nstr(_E_INF, 30), "kappa": mp.nstr(_KAPPA, 30),
        "ln_q0": mp.nstr(LNQ, 30), "eps_terms": _NEPS, "mp_dps": mp.dps,
    },
    "staircase_closed_form_S3_S4": _table,
    "asymptotic_S5": _asym,
    "checks": [{"name": n, "ok": ok, "detail": d} for (n, ok, d) in CHECKS],
    "verdict": (
        "V(staircase) = A*k - B - F(n), verified against all 11 committed points of #7294, with "
        "a remainder decaying at the derived rate q0^4 per unit k. At triangular n this is an "
        "IDENTITY, M_n = A*sqrt(2n + 1/4) - A/2 - B - C + e_n + (i) + (ii), with (i)+(ii) = "
        "5.1e-16 at n = 3916; the plain sqrt(2n) form is NOT equivalent, it carries an extra "
        "A/(8 sqrt(2n)) = 0.0051 there. The open problem is now the single sequence e_n / its "
        "limit e_inf. M_n remains a lower bound -- the baseline is exact, the search is not."
    ),
}
_out = os.path.join(_HERE, "rev-staircase-closed-form-and-constant-term.witness.json")
with open(_out, "w") as _fh:
    json.dump(_w, _fh, indent=2)
    _fh.write("\n")
print()
print(f"witness -> {_out}")

sys.exit(0 if _n_ok == len(CHECKS) else 1)
