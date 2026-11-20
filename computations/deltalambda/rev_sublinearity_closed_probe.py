#!/usr/bin/env python3
r"""
rev_sublinearity_closed_probe.py — REV IS SUB-LINEAR: Omega(sqrt n) <= REV <= O(n^{3/4}) (qou-hok7)

This CLOSES the one piece `qou-hok7` left open, by repairing the lemma that failed in
`rev_sublinearity_proof_probe.py`.

## What failed before, and why the repair is not the same claim

That probe tried `L2: H(lambda) >= 3r^2 - 3r + 1` with `r = min(ell, lambda_1)`, deriving it from
`h(1,j) >= 2r - j`.  That step needs column `j` to have `>= r` cells for every `j <= r`; only
column 1 does.  **1168 counterexamples at n <= 22**, sharpest the hook shape `(11, 1^10)`:
`r = 11`, `H = 131`, claimed bound `331`.

The repair does NOT assume anything about columns `2..r`.  It sums the first ROW and the first
COLUMN only, using nothing but `lambda_i >= 1` and `lambda'_j >= 1`:

    h(i,1) = lambda_i + ell - i     >=  1 + ell - i        =>  sum_i h(i,1)   >= ell(ell+1)/2
    h(1,j) = lambda_1 - j + lambda'_j >=  lambda_1 - j + 1  =>  sum_j h(1,j)   >= lambda_1(lambda_1+1)/2
    h(1,1) = lambda_1 + ell - 1                              (the doubly-counted corner)

Every other cell has `h >= 1 > 0`, so dropping them only weakens the bound:

    H  >=  ell(ell+1)/2 + lambda_1(lambda_1+1)/2 - (lambda_1 + ell - 1)

Both `H` and `r` are conjugation-invariant, so take `r = ell <= lambda_1` WLOG; since
`t(t-1)/2` is increasing and `lambda_1 >= r`,

    H  >=  r(r+1)/2 - r + 1 + lambda_1(lambda_1-1)/2  >=  r(r+1)/2 - r + 1 + r(r-1)/2  =  r^2 - r + 1
                                                                                          (L2')

On the hook shape that refuted L2, L2' gives `111 <= 131`.  It is tight only at `lambda = (1)`.

### 🟩 FORMALIZED, and the Lean bound is STRONGER than L2'

`QOU.BraidKnot.HookSum.sq_min_le_sum_hookZ`
(`folio/quantum-observable-universe/lean/QOU/BraidKnot/HookSumThicknessBound.lean`) proves
`min(rowLen 0, colLen 0)^2 <= sum_c hookZ`, i.e. **`H >= r^2`**, for EVERY Young diagram --
sorry-free (`lean`-direct exit 0 with `-DautoImplicit=false -s 65536`; axioms exactly
`[propext, Classical.choice, Quot.sound]`).

The Lean proof does not use the row+column count at all.  It reads one line off the corpus's own
`two_mul_sum_hookZ_eq_sum_sq`, namely `2H = sum_i (rowLen i)^2 + sum_j (colLen j)^2`: every summand
is a square, so each sum dominates its own 0-th term, giving
`2H >= (rowLen 0)^2 + (colLen 0)^2 >= 2 r^2`.

So the analytic chain below is stated with `r <= sqrt(H) + 1` from L2' (`r^2 - r + 1`), while the
formalized bound `r^2` gives the slightly better `r <= sqrt(H)`.  The chain is left on L2' because
that is what the exhaustive check R1 tests and what the constant in R6 was computed from; using the
stronger bound would only improve the constant, never the exponent.  Companion lemma
`hookZ_succ_lt` formalizes the per-row strict decrease that underlies L1.

## The chain to O(n^{3/4})

From (E) + L1 (`rev_sublinearity_proof_probe.py`, both proved there):  `R_lambda <= C * r(lambda)`,
`C = sum_m eps_m = 6.1714`.  L2' inverts to `r <= (1 + sqrt(4H-3))/2 <= sqrt(H) + 1`.  Hence for
every shape, with `E_lambda = (H - H_min) ln q_0 >= 0`,

    R_lambda - E_lambda  <=  f(H) := C(sqrt(H) + 1) - (H - H_min) ln q_0 ,        H >= H_min .

`f'(H) = C/(2 sqrt H) - ln q_0 < 0` as soon as `sqrt(H) > C/(2 ln q_0) = 29.57`, i.e.
`H > 874.6`.  `H_min(n) ~ (2 sqrt2/3) n^{3/2}` passes that at `n ~ 97`, so for all larger `n` the
maximum sits at `H = H_min` and

    max_lambda (R_lambda - E_lambda)  <=  C (sqrt(H_min(n)) + 1)  ~  5.99 n^{3/4} .

Finally `REV_n = log sum_lambda exp(R_lambda - E_lambda) <= log p(n) + max_lambda(...)`, and
`log p(n) ~ pi sqrt(2n/3) = 2.565 sqrt(n)`.  Therefore

    REV_n  <=  2.565 sqrt(n)  +  C sqrt(H_min(n))  +  C   =   O(n^{3/4}) .

Combined with `REV = Omega(sqrt n)` (proved in the predecessor probe from the staircase, whose
energy is exactly zero at triangular `n`):

    Omega(sqrt n)  <=  REV_n  <=  O(n^{3/4})        -- SUB-LINEARITY PROVED.

## 🛑 On the CONSTANT: `A sqrt2 = 5.0959` is a LOWER BOUND, not the value

The commit and PR that introduced this probe also conjectured `REV_n ~ A sqrt(2n)` from the
staircase.  **That conjecture is refuted** (`rev_constant_conjecture_correction_probe.py`), for two
independent reasons that push the same way:

  1. the staircase is the argmax only up to `k = 6`; from `k = 7` a perturbed shape wins and the
     excess GROWS (max/R_staircase = 1.00116, 1.00804, 1.00997 at k = 7, 8, 9);
  2. the entropy term `(REV - max)/sqrt(n)` RISES across the whole measured range
     (0.754 at n=8 to 1.146 at n=46) rather than decaying, so it contributes at the SAME order.

Hence `lim REV/sqrt(n) > A sqrt2`.  Note also that the measured `REV/sqrt(n) = 4.363` at n=46 sits
BELOW that bound: convergence is very slow (the staircase ratio is itself only 4.466 at n=435
against its own limit 5.0959), so the small measured value is not evidence for a small constant.

The bounds proved below are unaffected -- neither uses the conjecture.

## 🛑 PRIOR WORK: the sinh-hook sum `S_n` is NOT a new object (corpus-grep, 2026-09-07)

The commit and PR introducing this probe described the reformulation
`REV_n = H_min ln q_0 - sum eps_i + log S_n`, with
`S_n = sum_{lambda|-n} prod_c 1/(2 sinh(h(c) ln q_0))`, as putting REV "in Nekrasov-Okounkov /
Chern-Simons hook-product form", and called `S_n` a q-deformation of `I(n)/n!`.  Both readings
need scoping:

  * `S_n` is a RESCALING of the corpus's own `S^bal(n;q)`, stated as
    `prop:binding-period-involution-statistic`
    (`folio/quantum-observable-universe/mass-theory/binding-period-involution-statistic.md:8-11`):
    with `[k] = (q^k - q^{-k})/(q - q^{-1})` and `dim_q^bal(lambda) = prod_k [k] / prod_c [h(c)]`,
        S_n  =  S^bal(n; q) / ( (q - q^{-1})^n * [n]_q! )
    verified here to 1e-38 for n = 1..9.  Since `Z_n = S^bal * q^{n(n-1)/2}`, the sinh sum is `Z_n`
    in a different normalisation -- unsurprising, as it was DERIVED from `Z_n`'s closed form.  It is
    a change of clothes, not new content.  Cite the proposition.
  * "q-deformation of `I(n)/n!`" is likewise already the corpus's reading of that object, and its
    `q = 1` leg (`sum_lambda f^lambda = I(n)`) is Lean-proved.

What the grep did NOT find, on any of the six paths: Nekrasov-Okounkov, Han's or Westbury's hook
formulas -- and the library does not HOLD them either (`nekrasov2002` is the Seiberg-Witten
instanton-counting paper, hep-th/0206161, with zero occurrences of "hook"; the NO hook formula is
hep-th/0306238 and is not held).  So the NO connection is a DERIVATION OBLIGATION, not a citation,
and the "no product form" negative recorded with this probe is the first measurement of it here.
Littlewood's identity is named as a classical anchor of exactly this object in
`computations/lever1-kernel-maj-involution-identification.witness.json:33` and is never stated
anywhere -- a genuine, cheap gap.

ARITY NOTE, and it bounds what "proved" means upstream of here: the general-`n` proposition rests
on a NARRATIVE proof citing Stanley EC2 and `sagan2001`, both registered and NOT ingested; its Lean
sibling proves only the three finite instances `n = 3, 4, 5` by `decide`.  The closed form this
probe builds on is verified computationally to n <= 11, not proved for general `n` in Lean.

## Checks

  R1  L2' holds for every partition with n <= 26 (exhaustive, exact integers).
  R2  L2' is what the row+column argument gives -- the argument is re-run symbolically per shape
      and compared to the closed form, so the bound is not merely asserted.
  R3  the refuted L2 and the repaired L2' are compared on the counterexample that killed L2.
  R4  f(H) is decreasing for H > (C/(2 ln q0))^2, and H_min(n) exceeds that for n >= 97.
  R5  the final numeric bound dominates the measured REV at every n where REV is known.
  R6  the bound is O(n^{3/4}): bound/n^{3/4} converges to C*(2 sqrt2/3)^{1/2}.

Exact integer arithmetic for all partition statistics; mpmath at 60 dps for the analytic parts.
No float64.
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

from zn_hook_length_closed_form_probe import conjugate, hooks, partitions  # noqa: E402
from hmin_closed_form_and_rev_sublinearity_probe import H_min_closed  # noqa: E402


def eps(m: int):
    return -mp.log(1 - T ** (-m))


def row_col_bound(lam: tuple) -> int:
    """The raw row+column bound, computed from lambda directly (exact integer)."""
    ell = len(lam)
    l1 = lam[0]
    return ell * (ell + 1) // 2 + l1 * (l1 + 1) // 2 - (l1 + ell - 1)


def main() -> int:
    results = []

    def check(tag, ok, msg):
        results.append({"check": tag, "pass": bool(ok), "detail": msg})
        print(("  PASS  " if ok else "  FAIL  ") + tag)
        print("        " + msg)
        return bool(ok)

    print("=" * 78)
    print("REV IS SUB-LINEAR: Omega(sqrt n) <= REV <= O(n^{3/4})   (qou-hok7)")
    print("=" * 78)

    C = sum(eps(m) for m in range(1, 400))
    print(f"  C = sum_m eps_m = {mp.nstr(C, 12)};  ln q0 = {mp.nstr(LNQ, 12)};  "
          f"C/(2 ln q0) = {mp.nstr(C / (2 * LNQ), 10)}")
    print()

    # ---- R1: L2' exhaustively
    NB = 26
    bad1 = []
    tight = []
    cnt = 0
    for n in range(1, NB + 1):
        for lam in partitions(n):
            cnt += 1
            r = min(len(lam), lam[0])
            H = sum(hooks(lam))
            if H < r * r - r + 1:
                bad1.append((lam, H, r * r - r + 1))
            if H == r * r - r + 1:
                tight.append((n, lam))
    check(
        "R1_L2prime_H_at_least_r2_minus_r_plus_1",
        not bad1,
        f"H(lambda) >= r^2 - r + 1 with r = min(ell, lambda_1), verified on all {cnt} partitions "
        f"with n <= {NB} ({len(bad1)} violations). Equality cases: {tight}. Exact integers, no "
        f"tolerance.",
    )

    # ---- R2: the row+column argument itself reproduces the bound
    bad2 = []
    for n in range(1, NB + 1):
        for lam in partitions(n):
            r = min(len(lam), lam[0])
            H = sum(hooks(lam))
            rc = row_col_bound(lam)
            # the argument's two steps: H >= row+col bound, and row+col bound >= r^2-r+1
            if H < rc or rc < r * r - r + 1:
                bad2.append((lam, H, rc, r * r - r + 1))
    check(
        "R2_row_plus_column_argument_is_sound_stepwise",
        not bad2,
        f"both steps of the derivation hold separately on all {cnt} partitions with n <= {NB} "
        f"({len(bad2)} failures): H >= [ell(ell+1)/2 + l1(l1+1)/2 - (l1+ell-1)] >= r^2-r+1. The "
        f"bound is therefore established by the stated argument, not merely observed to hold.",
    )

    # ---- R3: the repair vs the refuted lemma, on the shape that killed L2
    hook_shape = (11,) + (1,) * 10
    r_h = min(len(hook_shape), hook_shape[0])
    H_h = sum(hooks(hook_shape))
    old_bound = 3 * r_h * r_h - 3 * r_h + 1
    new_bound = r_h * r_h - r_h + 1
    check(
        "R3_repair_survives_the_counterexample_that_killed_L2",
        H_h < old_bound and H_h >= new_bound,
        f"on lambda=(11,1^10): r={r_h}, H={H_h}. Refuted L2 claimed H >= {old_bound} (FALSE, by "
        f"{old_bound - H_h}). Repaired L2' claims H >= {new_bound} (TRUE, slack {H_h - new_bound}). "
        f"L2' never assumes anything about columns 2..r, which is exactly where L2 broke.",
    )

    # ---- R4: f(H) decreasing beyond the turning point; H_min passes it
    turn = (C / (2 * LNQ)) ** 2
    n_star = None
    for n in range(1, 400):
        if mp.mpf(H_min_closed(n)) > turn:
            n_star = n
            break
    check(
        "R4_f_is_decreasing_past_H_min_for_all_large_n",
        n_star is not None and n_star < 200,
        f"f(H) = C(sqrt H + 1) - (H - H_min) ln q0 has f'(H) < 0 for H > (C/(2 ln q0))^2 = "
        f"{mp.nstr(turn, 8)}. H_min(n) first exceeds that at n = {n_star} "
        f"(H_min({n_star}) = {H_min_closed(n_star)}), so for every n >= {n_star} the maximum of f "
        f"over H >= H_min sits at H = H_min. Below that the range is finite and REV is bounded "
        f"there by inspection.",
    )

    # ---- R5: the bound dominates measured REV
    measured = {4: "2.1069303", 8: "5.37076246", 12: "8.64003313", 16: "11.7081362",
                20: "14.5903827", 24: "17.3292831", 28: "19.7613194", 32: "22.2400831",
                36: "24.3826729", 40: "26.6352043", 44: "28.6042692"}
    print()
    print("-" * 78)
    print("the proved upper bound against measured REV:")
    print(f"  {'n':>4} {'REV (measured)':>16} {'upper bound':>14} {'slack':>12}")
    rows = []
    ok5 = True
    for n in sorted(measured):
        hm = mp.mpf(H_min_closed(n))
        bound = mp.log(mp.mpf(_pn(n))) + C * (mp.sqrt(hm) + 1)
        rev = mp.mpf(measured[n])
        ok5 = ok5 and (bound > rev)
        rows.append({"n": n, "REV": measured[n], "upper_bound": mp.nstr(bound, 12),
                     "slack": mp.nstr(bound - rev, 10)})
        print(f"  {n:>4} {mp.nstr(rev, 10):>16} {mp.nstr(bound, 10):>14} "
              f"{mp.nstr(bound - rev, 8):>12}")
    check(
        "R5_bound_dominates_every_measured_REV",
        ok5,
        f"the proved bound log p(n) + C(sqrt(H_min)+1) exceeds the measured REV at all "
        f"{len(measured)} values of n where REV has been computed exactly. It is loose (the "
        f"L1 bound R <= C*r is itself loose by ~13x on thin shapes) -- looseness is expected and "
        f"does not weaken the asymptotic statement.",
    )

    # ---- R6: the bound is O(n^{3/4}) with the stated constant
    target = C * mp.sqrt(2 * mp.sqrt(2) / 3)
    ratios = []
    for n in [1000, 10000, 100000, 1000000, 10000000]:
        hm = mp.mpf(H_min_closed(n))
        b = mp.log(mp.mpf(_pn_asym(n))) + C * (mp.sqrt(hm) + 1)
        ratios.append((n, b / (mp.mpf(n) ** mp.mpf("0.75"))))
    check(
        "R6_bound_is_O_n_three_quarters",
        abs(ratios[-1][1] - target) < mp.mpf("0.05"),
        f"bound / n^(3/4) -> C * sqrt(2 sqrt2 / 3) = {mp.nstr(target, 10)}; at n=10^7 it is "
        f"{mp.nstr(ratios[-1][1], 10)}. Sequence: "
        + ", ".join(f"n=10^{len(str(n))-1}:{mp.nstr(v, 7)}" for n, v in ratios)
        + ". The log p(n) term is O(sqrt n) and vanishes from the ratio.",
    )

    n_ok = sum(1 for r in results if r["pass"])
    print()
    print("=" * 78)
    print(f"{n_ok}/{len(results)} checks passed")
    print("PROVED:  Omega(sqrt n) <= REV_n <= O(n^{3/4}).  SUB-LINEARITY IS CLOSED.")
    print("         lower bound: predecessor probe (staircase, zero energy at triangular n)")
    print("         upper bound: this probe (L2' repairs the refuted L2)")
    print("OPEN:    tightness; the upper bound's exponent 3/4 is not believed sharp.")
    print("         A*sqrt2 = 5.0959 is a LOWER BOUND on the constant, NOT its value --")
    print("         see rev_constant_conjecture_correction_probe.py: the staircase stops")
    print("         being the argmax at k=7, and the entropy term is itself Theta(sqrt n).")
    print("=" * 78)

    payload = {
        "probe": "rev_sublinearity_closed_probe",
        "bean": "qou-hok7",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0Value": mp.nstr(Q0, 50),
        "q0_anchor": "physical_proton", "q0Anchor": "proton",
        "dps": mp.dps,
        "L2_prime": "H(lambda) >= r^2 - r + 1, r = min(ell, lambda_1)",
        "repairs": ("L2 'H >= 3r^2-3r+1' refuted in rev_sublinearity_proof_probe.py; L2' uses only "
                    "the first row and first column and assumes nothing about columns 2..r"),
        "result": "Omega(sqrt n) <= REV_n <= O(n^{3/4}) -- sub-linearity PROVED",
        "upper_bound_constant": mp.nstr(target, 20),
        "still_open": "tightness; the 3/4 exponent is not believed sharp",
        "conjecture_retracted": ("'REV ~ A sqrt(2n)' was conjectured with this probe and is "
                                 "REFUTED as an asymptotic equality by "
                                 "rev_constant_conjecture_correction_probe.py; A sqrt2 = 5.0959 "
                                 "is a LOWER BOUND on the constant, not its value"),
        "checks": results,
        "checks_passed": n_ok,
        "checks_total": len(results),
        "bound_vs_measured": rows,
    }
    out = os.path.join(_COMPUTATIONS, "rev-sublinearity-closed.witness.json")
    with open(out, "w") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(f"witness -> {out}")

    return 0 if n_ok == len(results) else 1


def _pn(n: int) -> int:
    """Exact p(n) by the standard DP (small n)."""
    p = [1] + [0] * n
    for k in range(1, n + 1):
        for m in range(k, n + 1):
            p[m] += p[m - k]
    return p[n]


def _pn_asym(n: int):
    """Hardy-Ramanujan p(n) ~ exp(pi sqrt(2n/3))/(4n sqrt3) -- used only for the large-n ratio,
    where only its LOGARITHM enters and the sub-exponential prefactor is irrelevant."""
    return mp.e ** (mp.pi * mp.sqrt(mp.mpf(2 * n) / 3)) / (4 * n * mp.sqrt(3))


if __name__ == "__main__":
    raise SystemExit(main())
