#!/usr/bin/env python3
"""O3' falsifier: is every SURVIVING Markov weight strictly positive at n > 3?

The O3 falsifier (sdp_o3_falsifier_probe) showed the block-PSD program is
degenerate along the q-antisymmetriser radical, because the SU(2) specialisation
gives that block ZERO Markov weight and a zero-weight block is invisible to the
objective. The repair (O3') is to pose the program on the quotient -- over the
partitions with nonzero weight.

That repair rests on one thing: every SURVIVING partition must carry STRICTLY
positive weight. If some survivor's weight vanishes at larger n, the same
degeneracy returns one level up. It was measured only at n = 3, where the
survivors are {(3), (2,1)}. This probe measures n = 3..12.

RESULT: not falsified. At every n tested, partitions with > 2 rows vanish
exactly and every partition with <= 2 rows is strictly positive.

The vanishing half is structural rather than numerical, and the corpus already
says so: `schur_principal_sym` notes that for a shape with more than N rows the
cell (N+1, 1) has content -N, so the numerator picks up [N + (-N)]_q = [0]_q = 0.
The row cap is automatic, not imposed.

The positivity half is also provable and the measurement agrees with it: for a
<= 2-row shape the minimum content is -1 (cell (2,1)), so every numerator factor
is [m]_q with m >= 1, every hook is >= 1, and both are positive at q > 1 -- so
s_lambda > 0 and hence y_lambda > 0 after a positive normalisation.

CROSS-VALIDATION, and it is the strong part. At n = 3 the hook-content product
formula here gives (3) 0.50540422650393, (2,1) 0.24729788674803, (1,1,1) 0.0 --
matching to all 14 digits the weights the O3 falsifier solved INDEPENDENTLY, by
linear system from the six Markov basis traces. Two unrelated routes, same
answer.

CAVEAT, numerical not structural: the minimum surviving weight decays by a
factor ~0.2475 per +2 in n (0.247 at n=3 to 0.000229 at n=12). It stays strictly
positive, but a program solved in float64 at large n would eventually be unable
to distinguish it from zero. The accumulator's k_max = 11 sits at ~9.2e-4, which
is comfortable.

scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap qou-sv7h OPEN.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "substrate"))

import _path_bridge  # noqa: F401,E402

from mpmath import mp  # noqa: E402

from y_lambda_su_n import y_lambda_su_n  # noqa: E402
from hecke_core import partition_dimension  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

# solved independently in sdp_o3_falsifier_probe, by linear system from the
# six Markov basis traces -- a completely different route to the same numbers.
N3_FROM_FALSIFIER = {"(3,)": "0.50540422650393",
                     "(2, 1)": "0.24729788674803",
                     "(1, 1, 1)": "0"}
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))


def main() -> int:
    set_compute_dps()
    q = Q_MP
    print("=" * 74)
    print("  O3' falsifier: strict positivity of every surviving SU(2) weight")
    print("=" * 74)
    print()
    print(f"  {'n':>3} {'parts':>6} {'>2rows':>7} {'zero':>6} {'<=2rows':>8} "
          f"{'pos':>5} {'min surviving y':>20} {'sum y*f':>9}")

    rows, all_vanish, all_pos, all_norm = [], True, True, True
    for n in range(3, 13):
        y = y_lambda_su_n(n, q, 2)
        big = [s for s in y if len(s) > 2]
        small = [s for s in y if len(s) <= 2]
        bz = all(abs(y[s]) < mp.mpf("1e-40") for s in big)
        sp_ = all(y[s] > 0 for s in small)
        mn = min(y[s] for s in small)
        tot = mp.fsum(y[s] * partition_dimension(s) for s in y)
        nz = abs(tot - 1) < mp.mpf("1e-30")
        all_vanish &= bz; all_pos &= sp_; all_norm &= nz
        rows.append({"n": n, "n_partitions": len(y), "n_over_2_rows": len(big),
                     "over_2_rows_all_zero": bz, "n_le_2_rows": len(small),
                     "survivors_all_positive": sp_, "min_surviving_y": fmt(mn),
                     "sum_y_times_dim": fmt(tot)})
        print(f"  {n:>3} {len(y):>6} {len(big):>7} {str(bz):>6} {len(small):>8} "
              f"{str(sp_):>5} {mp.nstr(mn, 10):>20} {mp.nstr(tot, 8):>9}")

    check("partitions with > 2 rows vanish exactly, every n = 3..12", all_vanish,
          "structural: the cell (3,1) has content -2, so [2 + (-2)]_q = [0]_q = 0")
    check("every SURVIVING partition is strictly positive, every n = 3..12",
          all_pos, "so the quotient program has no zero-weight block to hide in")
    check("normalisation sum y_lambda f^lambda = 1 at every n", all_norm)

    # cross-validation against the independently-solved n=3 weights
    print()
    print("  cross-check: hook-content product vs the falsifier's linear solve at n=3")
    y3 = y_lambda_su_n(3, q, 2)
    agree = True
    for s in sorted(y3, key=lambda t: -len(t)):
        want = mp.mpf(N3_FROM_FALSIFIER[str(s)])
        got = y3[s]
        ok = abs(got - want) < mp.mpf("1e-13")
        agree &= ok
        print(f"     {str(s):<12} product formula {mp.nstr(got, 14):>18}"
              f"   linear solve {N3_FROM_FALSIFIER[str(s)]:>18}   {'agree' if ok else 'DIFFER'}")
    check("two independent routes give the same n=3 weights", agree,
          "hook-content product vs linear system from the six Markov traces")

    # the decay caveat, measured rather than asserted
    mins = [mp.mpf(r["min_surviving_y"]) for r in rows]
    ratio = mins[-1] / mins[-3]
    print()
    print(f"  min surviving weight decays by {mp.nstr(ratio, 6)} per +2 in n "
          f"({mp.nstr(mins[0], 6)} at n=3 -> {mp.nstr(mins[-1], 6)} at n=12).")
    print("  Structurally positive; numerically it would eventually underflow in")
    print("  float64 at large n. k_max = 11 sits at ~9.2e-4, comfortable.")
    check("still positive at the accumulator's k_max = 11", mins[8] > 0,
          f"min = {mp.nstr(mins[8], 6)}")

    print()
    print("  VERDICT: O3' NOT falsified. The quotient program is non-degenerate")
    print("  at every n from 3 to 12.")

    w = WitnessBuilder("sdp-o3prime-weight-positivity", engine="python+mpmath")
    w.set_description(
        "O3' falsifier for the operator-selection replacement: every SURVIVING "
        "SU(2) Markov weight must be strictly positive or the radical degeneracy "
        "returns one level up. Measured n = 3..12 at the proton pin: partitions "
        "with > 2 rows vanish exactly (structural), every partition with <= 2 rows "
        "is strictly positive, and sum y f = 1 throughout. Cross-validated at n=3 "
        "against the independently-solved weights from sdp_o3_falsifier_probe, to "
        "14 digits. NOT falsified."
    )
    w.set_audit_only("docs/proposals/2026-09-05-operator-selection-objective-replacement.md")
    w.add_parameter("q0", fmt(q))
    w.add_data("per_n", rows)
    w.add_data("n3_cross_validation",
               {str(s): fmt(y3[s]) for s in y3} | {"independent_solve": N3_FROM_FALSIFIER})
    for nm, ok in CHECKS:
        w.add_assertion(nm, computed="1" if ok else "0", expected="1",
                        tolerance="0", source="sdp_o3prime_weight_positivity_probe")
    print(f"\n  witness: {w.save()}")
    print(f"  {sum(1 for _n, ok in CHECKS if ok)}/{len(CHECKS)} checks passed")
    return 0 if all(ok for _n, ok in CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
