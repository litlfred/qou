#!/usr/bin/env python3
r"""
rev_coefficient_slack_is_the_pair_term_probe.py — the 1.71x bracket is ONE discarded term, and
it has a name (qou-hok7)

The Theta(sqrt n) coefficient of `REV_n` is bracketed and not identified:

    5.0959  =  A*sqrt2        the STAIRCASE limit, proved (#7010) — a lower bound
      ?     =  lim M_n/sqrt n the true value — OPEN
    8.7277  =  C*sqrt2        the row-tangent bound's lower band edge (#7185, #7270)

#7279 measured the achievable side at ~5.22 and concluded "most of that 1.7x width is slack in the
BOUND, not in the shapes". That is where it stopped, and it is not enough to act on: it says the
bound is loose without saying WHICH STEP is loose. This probe answers that, and the answer is a
single term.

## The claim

    C = A + E_2,        E_2 := sum_{d>=1} eps(2d)

— trivially, because the odds and the evens partition the positive integers, `A` being the odd
half. So the bracket's own ratio is

    (C*sqrt2) / (A*sqrt2)  =  C/A  =  1.712...

with NO sqrt2 and NO n in it. The two ends of the bracket are the same expression with `C` in
place of `A`, and the difference between them is exactly `E_2` per row.

`E_2` is not an abstract remainder. It is the **staircase's pair term**: the staircase `delta_k`
has beta-numbers `(2k-1, 2k-3, ..., 1)`, so every beta-gap is even, and

    P_stair(k) = sum_{d=1}^{k-1} (k-d) eps(2d)  ~  k * E_2.

The row-tangent bound reaches `C*sqrt2` by using `R_lambda <= (l-1)C`, which **discards the pair
term entirely**. So the bound's 1.71x slack is not diffuse: it is the one-body bound being applied
with the two-body term thrown away, and the shapes that actually maximise do not throw it away.

## Why that is actionable rather than merely tidy

It relocates the open problem. "Find the coefficient" becomes "prove a pair-term LOWER bound that
survives the energy trade-off" — and the trade-off is real, not a formality: `P` is small exactly
when the beta-numbers are widely separated, which is exactly when `H` (hence `E`) is large. A
bound that keeps any nontrivial pair floor lands at or below `A*sqrt2 * (1 + excess)`, i.e. within
a few percent of the achievable side, instead of 71% above it.

## Checks

  R1  `C = A + E_2` to full working precision (the odd/even partition)
  R2  the bracket ratio IS `C/A`, with no `sqrt2` and no `n`
  R3  the staircase decomposition: one-body/k -> C, pair/k -> E_2, R/k -> A
  R4  the staircase attains `H_min` at triangular `n`, so its `E` is exactly 0 (exact integers)
  R5  what #7279's search data do and do NOT say about the excess

Proton-pinned (`Q_50_DIGIT_STR`); no Markov parameter enters this cone, so the convention-C/D
question does not arise. Exact integers for `n`/`H`; mpmath at 40 dps for the eps sums. No float64.
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMPUTATIONS = os.path.dirname(_HERE)
if _COMPUTATIONS not in sys.path:
    sys.path.insert(0, _COMPUTATIONS)

from mpmath import mp  # noqa: E402

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

from hmin_closed_form_and_rev_sublinearity_probe import H_min_closed  # noqa: E402

mp.dps = 80
Q0 = Q_MP
LNQ = mp.log(Q0)
T = Q0 ** 2

# eps_m = -log(1 - q0^{-2m}) ~ q0^{-2m}, so the tail is geometric in q0^{-2} = 0.8116...
# _NEPS is chosen so the first DROPPED term is below the working precision; asserted in R1.
_NEPS = 12000
EPS = [mp.mpf(0)] + [-mp.log(1 - T ** (-m)) for m in range(1, _NEPS)]
_F = [mp.mpf(0)] * _NEPS
for _m in range(1, _NEPS):
    _F[_m] = _F[_m - 1] + EPS[_m]

C_CONST = _F[_NEPS - 1]
A_CONST = sum(EPS[m] for m in range(1, _NEPS, 2))       # odd m
E2_CONST = sum(EPS[m] for m in range(2, _NEPS, 2))      # even m


def F(k: int) -> mp.mpf:
    """`F(k) = sum_{m<=k} eps_m`, saturated at `C` beyond the tabulated range (the tail is below
    working precision there — see the R1 assertion)."""
    return _F[k] if k < _NEPS else C_CONST


def eps(m: int) -> mp.mpf:
    return EPS[m] if m < _NEPS else mp.mpf(0)


CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'ok ' if ok else 'FAIL'}] {name}: {detail}")


# --------------------------------------------------------------------------------------------
# R1 — C = A + E_2
# --------------------------------------------------------------------------------------------
print("R1  C = A + E_2 (the odd/even partition of the positive integers)")
print(f"    C   = sum_m eps_m        = {mp.nstr(C_CONST, 20)}")
print(f"    A   = sum_odd eps_m      = {mp.nstr(A_CONST, 20)}")
print(f"    E_2 = sum_{{d>=1}} eps_2d = {mp.nstr(E2_CONST, 20)}")
_resid = C_CONST - A_CONST - E2_CONST
_tail = eps(_NEPS - 1)
# The tolerance is DERIVED, not chosen: three sums of ~_NEPS mpf additions each accumulate at
# most ~3*_NEPS ulps, and one ulp at this magnitude is ~10^{-(dps-1)}. A tolerance picked to fit
# the observed residual would be testing the threshold rather than the identity.
_ULP = mp.mpf(10) ** (-(mp.dps - 1))
_TOL = 3 * _NEPS * _ULP
print(f"    residual C - A - E_2     = {mp.nstr(_resid, 6)}")
print(f"    rounding bound 3*N*ulp   = {mp.nstr(_TOL, 6)}   (derived from dps={mp.dps}, "
      f"N={_NEPS})")
print(f"    last tabulated eps_m     = {mp.nstr(_tail, 6)}   (0 = the tail has vanished at "
      f"working precision)")
check(
    "R1 C = A + E_2 to the precision the arithmetic can deliver",
    abs(_resid) < _TOL and _tail == 0,
    f"residual {mp.nstr(_resid, 4)} against a derived rounding bound {mp.nstr(_TOL, 4)}; the "
    f"series tail has underflowed to exactly 0, so truncation is not the binding error",
)

# --------------------------------------------------------------------------------------------
# R2 — the bracket ratio IS C/A
# --------------------------------------------------------------------------------------------
print()
print("R2  the bracket ratio is C/A — no sqrt2, no n")
SQRT2 = mp.sqrt(2)
lo = A_CONST * SQRT2
hi = C_CONST * SQRT2
ratio = hi / lo
print(f"    A*sqrt2 (staircase floor, proved #7010)   = {mp.nstr(lo, 12)}")
print(f"    C*sqrt2 (row-tangent band edge, #7185)    = {mp.nstr(hi, 12)}")
print(f"    ratio                                     = {mp.nstr(ratio, 12)}")
print(f"    C/A                                       = {mp.nstr(C_CONST / A_CONST, 12)}")
print(f"    1 + E_2/A                                 = {mp.nstr(1 + E2_CONST / A_CONST, 12)}")
check(
    "R2 ratio = C/A = 1 + E_2/A",
    abs(ratio - C_CONST / A_CONST) < mp.mpf("1e-35")
    and abs(ratio - (1 + E2_CONST / A_CONST)) < mp.mpf("1e-35"),
    f"{mp.nstr(ratio, 10)} — the whole 1.71x bracket is the single term E_2 = "
    f"{mp.nstr(E2_CONST, 10)} per row",
)
# The recorded band edges, as a guard against this probe drifting from the ones in the corpus.
check(
    "R2 band edges match the recorded 5.0959 / 8.7277",
    abs(lo - mp.mpf("5.0959")) < mp.mpf("5e-4") and abs(hi - mp.mpf("8.7277")) < mp.mpf("5e-4"),
    f"A*sqrt2 {mp.nstr(lo, 8)} vs 5.0959; C*sqrt2 {mp.nstr(hi, 8)} vs 8.7277",
)


# --------------------------------------------------------------------------------------------
# R3 — the staircase decomposition
# --------------------------------------------------------------------------------------------
def staircase_beta(k: int) -> list[int]:
    """beta-numbers of delta_k = (k, k-1, ..., 1): all odd, 2k-1 down to 1."""
    return [2 * k - 1 - 2 * i for i in range(k)]


def staircase_parts(k: int) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    """(one-body, pair, R) for the staircase at n = T_k."""
    b = staircase_beta(k)
    one = sum((F(v) for v in b), mp.mpf(0))
    pair = sum(((k - d) * eps(2 * d) for d in range(1, k)), mp.mpf(0))
    n = k * (k + 1) // 2
    return one, pair, one - pair - F(n)


print()
print("R3  the staircase decomposition — one-body/k -> C, pair/k -> E_2, R/k -> A")
print(f"    {'k':>6} {'one-body/k':>16} {'pair/k':>16} {'R/k':>16}")
_rows = []
for k in (50, 100, 200, 400, 800, 1600):
    one, pair, R = staircase_parts(k)
    _rows.append((k, one / k, pair / k, R / k))
    print(f"    {k:6d} {mp.nstr(one / k, 12):>16} {mp.nstr(pair / k, 12):>16} "
          f"{mp.nstr(R / k, 12):>16}")

# Richardson on the k-doubling pairs: f(k) = c + a/k  =>  2 f(2k) - f(k) -> c.
k1, o1, p1, r1 = _rows[-2]
k2, o2, p2, r2 = _rows[-1]
one_lim = 2 * o2 - o1
pair_lim = 2 * p2 - p1
R_lim = 2 * r2 - r1
print(f"    Richardson (k = {k1} -> {k2}):")
print(f"      one-body/k -> {mp.nstr(one_lim, 14)}   vs C   = {mp.nstr(C_CONST, 14)}")
print(f"      pair/k     -> {mp.nstr(pair_lim, 14)}   vs E_2 = {mp.nstr(E2_CONST, 14)}")
print(f"      R/k        -> {mp.nstr(R_lim, 14)}   vs A   = {mp.nstr(A_CONST, 14)}")
check(
    "R3 one-body/k -> C",
    abs(one_lim - C_CONST) / C_CONST < mp.mpf("1e-6"),
    f"{mp.nstr(one_lim, 10)} vs {mp.nstr(C_CONST, 10)}, rel "
    f"{mp.nstr(abs(one_lim - C_CONST) / C_CONST, 4)}",
)
check(
    "R3 pair/k -> E_2 (the term the bound discards)",
    abs(pair_lim - E2_CONST) / E2_CONST < mp.mpf("1e-6"),
    f"{mp.nstr(pair_lim, 10)} vs {mp.nstr(E2_CONST, 10)}, rel "
    f"{mp.nstr(abs(pair_lim - E2_CONST) / E2_CONST, 4)}",
)
check(
    "R3 R/k -> A = C - E_2",
    abs(R_lim - A_CONST) / A_CONST < mp.mpf("1e-6"),
    f"{mp.nstr(R_lim, 10)} vs {mp.nstr(A_CONST, 10)}, rel "
    f"{mp.nstr(abs(R_lim - A_CONST) / A_CONST, 4)}",
)

# --------------------------------------------------------------------------------------------
# R4 — the staircase attains H_min at triangular n, so its E is exactly 0
# --------------------------------------------------------------------------------------------
print()
print("R4  H(delta_k) = H_min(T_k) exactly, so E(delta_k) = 0 and V = R there")


def H_of_beta(b: list[int]) -> int:
    """H = sum beta(beta+1)/2 - sum_{i<j}(beta_i - beta_j), exact integers (b sorted desc).

    This is identity (II), now a Lean theorem: `QOU.BraidKnot.HookSum.two_mul_sum_hookZ_betaForm`
    (and independently `sum_hookZ_betaForm_of_hookMultiset`), PR #7282.
    """
    L = len(b)
    pair = sum((L - 1 - 2 * i) * v for i, v in enumerate(b))
    return sum(v * (v + 1) // 2 for v in b) - pair


_h_ok = True
_h_detail = []
for k in (1, 2, 3, 5, 8, 13, 21, 34, 55):
    n = k * (k + 1) // 2
    Hs = H_of_beta(staircase_beta(k))
    Hm = H_min_closed(n)
    # P_k = k(k+1)(2k+1)/6, the square-pyramidal number — H_min_closed's value at triangular n.
    Pk = k * (k + 1) * (2 * k + 1) // 6
    ok = (Hs == Hm == Pk)
    _h_ok = _h_ok and ok
    _h_detail.append((k, n, Hs, Hm, Pk, ok))
    print(f"    k={k:3d}  n={n:5d}  H(delta_k)={Hs:8d}  H_min={Hm:8d}  P_k={Pk:8d}  "
          f"{'ok' if ok else 'MISMATCH'}")
check(
    "R4 staircase attains H_min at every triangular n tested",
    _h_ok,
    "9 values of k, exact integer arithmetic — so E(delta_k) = 0 and the staircase's value is "
    "its R, with no energy paid",
)

# --------------------------------------------------------------------------------------------
# R5 — what #7279's search data do and do NOT say
# --------------------------------------------------------------------------------------------
print()
print("R5  the excess over the staircase, re-read")
# Recorded in #7279 (rev_coefficient_lower_bound_probe.py). Exact integers for n; the two
# R-values are that probe's own output, carried here as Fractions of a decimal string so no
# float64 enters. This block RE-READS a prior measurement; it does not re-run the search.
_SEARCH = [
    # n,   k,  staircase R,   best found R
    (36, 8, "17.63209", "17.773921"),
    (78, 12, "31.91046", "32.601639"),
    (136, 16, "46.29905", "47.515487"),
    (300, 24, "75.12050", "77.075526"),
    (630, 35, "114.75740", "117.133810"),
]
print(f"    {'n':>6} {'stair R':>12} {'best R':>12} {'abs excess':>12} {'excess/sqrt n':>14}")
_exc = []
for n, k, s, b in _SEARCH:
    sm, bm = mp.mpf(s), mp.mpf(b)
    e = bm - sm
    _exc.append((n, e, e / mp.sqrt(n)))
    print(f"    {n:6d} {s:>12} {b:>12} {mp.nstr(e, 8):>12} {mp.nstr(e / mp.sqrt(n), 8):>14}")

_peak = max(range(len(_exc)), key=lambda i: _exc[i][2])
_turns = _peak < len(_exc) - 1
print(f"    excess/sqrt n peaks at n = {_exc[_peak][0]} and then "
      f"{'FALLS' if _turns else 'does not fall'}")
check(
    "R5 the excess column turns over at the largest n — which is NOT evidence of a limit",
    _turns,
    "excess/sqrt n rises to n=300 then falls at n=630. The search is a HEURISTIC local search "
    "whose quality degrades with n (its own #7279 header says a failure to find a better shape "
    "does not lower the upper bound), so a turnover at the LARGEST n is more likely search "
    "degradation than a mathematical fact. Do not read the excess as converging to ~1.02, and "
    "do not read it as vanishing either — 5 points, all at triangular n, cannot separate a "
    "multiplicative excess from an additive O(sqrt n) one",
)

# --------------------------------------------------------------------------------------------
print()
_n_ok = sum(1 for _, ok, _ in CHECKS if ok)
print(f"=== {_n_ok}/{len(CHECKS)} checks pass ===")
print()
print("VERDICT")
print("  The 1.71x bracket is ONE discarded term. C = A + E_2 exactly (odd/even partition), so")
print("  the bracket's ratio is C/A = 1.712 with no sqrt2 and no n in it, and E_2 IS the")
print("  staircase's pair term (R3: pair/k -> E_2). The row-tangent bound reaches C*sqrt2 by")
print("  using R <= (l-1)C, which throws the pair term away; the maximising shapes do not.")
print()
print("  So the open problem is NOT 'search harder for a better shape'. It is: prove a pair-term")
print("  LOWER bound that survives the energy trade-off (P is small exactly when the betas are")
print("  widely separated, which is exactly when H, hence E, is large). Any nontrivial pair")
print("  floor lands the bound near A*sqrt2 instead of 71% above it.")
print()
print("  NOT established here: that the true coefficient IS A*sqrt2. R5 says the 5-point search")
print("  data cannot decide whether the excess over the staircase is multiplicative (~1.02) or")
print("  additive, and its turnover at the largest n is probably the search weakening.")

_out = {
    "schema": "qou-witness/v1",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "computation": os.path.basename(__file__),
    "bean": "qou-hok7",
    "anchor": "physical_proton",
    # Canonical anchor key read by the q0 audits/ratchet (the "anchor" key above is
    # a near-miss spelling they cannot see), plus scriptFile provenance.
    "q0Anchor": "proton",
    "scriptFile": os.path.basename(__file__),
    "q0Value": Q_50_DIGIT_STR,
    "description": (
        "The Theta(sqrt n) coefficient bracket [A*sqrt2, C*sqrt2] has ratio exactly C/A = 1.712, "
        "and C - A = E_2 is the staircase's pair term — the term the row-tangent bound discards "
        "when it uses R <= (l-1)C. Relocates the open problem from shape-search to a pair-term "
        "lower bound."
    ),
    "constants": {
        "C": mp.nstr(C_CONST, 30),
        "A": mp.nstr(A_CONST, 30),
        "E_2": mp.nstr(E2_CONST, 30),
        "C_over_A": mp.nstr(C_CONST / A_CONST, 30),
        "A_sqrt2_staircase_floor": mp.nstr(A_CONST * SQRT2, 30),
        "C_sqrt2_band_edge": mp.nstr(C_CONST * SQRT2, 30),
        "ln_q0": mp.nstr(LNQ, 30),
    },
    "staircase_limits": {
        "one_body_per_row": mp.nstr(one_lim, 20),
        "pair_per_row": mp.nstr(pair_lim, 20),
        "R_per_row": mp.nstr(R_lim, 20),
        "richardson_from_k": [k1, k2],
    },
    "hmin_at_triangular": [
        {"k": k, "n": n, "H_staircase": Hs, "H_min": Hm, "P_k": Pk, "equal": ok}
        for (k, n, Hs, Hm, Pk, ok) in _h_detail
    ],
    "search_excess_reread": [
        {"n": n, "abs_excess": mp.nstr(e, 12), "excess_over_sqrt_n": mp.nstr(r, 12)}
        for (n, e, r) in _exc
    ],
    "checks": [{"name": n, "ok": ok, "detail": d} for (n, ok, d) in CHECKS],
    "verdict": (
        "The bracket's 1.71x width is the single term E_2 per row, discarded by the bound's "
        "R <= (l-1)C step. Open problem relocated to a pair-term lower bound under the energy "
        "trade-off. NOT established: that the true coefficient is A*sqrt2."
    ),
}
_path = os.path.join(_HERE, "rev-coefficient-slack-is-the-pair-term.witness.json")
with open(_path, "w", encoding="utf-8") as fh:
    json.dump(_out, fh, indent=2)
    fh.write("\n")
print()
print(f"witness -> {_path}")

sys.exit(0 if _n_ok == len(CHECKS) else 1)
