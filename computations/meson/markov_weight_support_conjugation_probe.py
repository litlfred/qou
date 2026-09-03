#!/usr/bin/env python3
"""Where does the bar-fixed sector leave the convention-D support? At A = 2.

Bean qou-7p7d.  Answers, in the D frame, "which is the simplest isotope at which
a third channel first appears" — and corrects a convention-C reading of the
deuteron SDP that says something different.

THE SETUP
=========
The Frobenius Gram of the per-nucleus operator-selection program is diagonal,
`G_λμ = tr_M(P_λ P_μ) = δ_λμ · tr_M(P_λ)`, and `tr_M(P_λ) = y_λ(q₀)` — the
Wedderburn–Jones–Markov weight (`deuteron_real_sdp.py` lines 18–21).  So the
Gram's signature is nothing but the sign pattern of `y_λ`, and the SDP's
well-posedness is a statement about that pattern.

WHAT THE COMMITTED DEUTERON WITNESS SAYS, AND WHY IT NO LONGER HOLDS
====================================================================
`computations/deuteron-real-sdp.witness.json` reports, at n = 6:

    frobenius_gram_indefinite      : true
    forbidden_blocks_negative_norm : (3,1,1,1), (2,2,1,1), (1^6)
    diagnostic                     : "Real SDP UNBOUNDED at q_0 — Frobenius
                                      Gram is indefinite (negative-norm blocks
                                      forbidden)."
    symmetry_note                  : "Every negative-norm forbidden block is the
                                      conjugate λ↦λ′ of a dominant positive
                                      block with tr_M(P_λ) sign-flipped — the
                                      §7b bar-involution / Type-B-folding
                                      signature."

That is **convention C**.  Its eleven Gram entries are all nonzero, whereas
convention D — canonical since the 2026-08-09 excision, reaffirmed as owner
ruling R1 on 2026-08-15 — caps the weights at two rows: `y_λ = 0` for
`ℓ(λ) > 2`.  All three "negative-norm" blocks have `ℓ ≥ 4`, so under D they are
not negative; they are **absent**.

Measured here: under D there are **no negative weights at any n tested**.  The
Gram is positive semidefinite with a large kernel.  The SDP is still ill-posed,
but as a **singularity** (bean `qou-cds2`), not an indefiniteness — a different
defect with a different fix, and the §7b "folding signature" reading does not
survive the convention change.

WHAT REPLACES IT
================
The D support is exactly the two-row partitions (`⌊n/2⌋ + 1` of them).
Conjugation `λ ↦ λ′` is the combinatorial shadow of the bar involution.  A
two-row `λ` of `n ≥ 6` has `λ₁ ≥ 3`, so `ℓ(λ′) = λ₁ ≥ 3` and `λ′` is in the
kernel: **conjugation maps the whole support into the kernel.**

At `n = 3` it does not, because the unique self-conjugate partition of 3 is the
staircase `(2,1)`, which has two rows and therefore a nonzero weight.  The
unique self-conjugate partition of 6 is `(3,2,1)`, which has three rows.

So the bar-fixed sector sits **inside** the supported sector at `A = 1` and
**outside** it from `A = 2` on.  The third row is where the weight dies, and the
self-conjugate partition first needs a third row at `n = 6`.

`A = 2` — the deuteron — is therefore the first isotope at which this changes,
and it is independently the first isotope carrying a colour-weighted p–n
interface letter (`atom_letter_colour_spectrum_probe.py`: one at `A = 2`, none
at `A = 1`).

SCOPE — (a), scope-limited, per AGENTS.md
=========================================
MEASURED: the D weights, their support, their signs, and the image of the
support under conjugation, at `n = 3, 6, 9, 12`.

NOT claimed: that no bar symmetry of the D weights exists.  One candidate
identity is tested below — `y_λ(1/q₀) = y_{λ′}(q₀)` — and it FAILS by an amount
of order the weights themselves.  A failed candidate is not an exclusion: the
correct bar statement for Markov weights may carry signs, or transform the
Markov parameter `z` as well, and neither is tested here.

Nor is any topological claim made.  "Third channel" here means the third ROW of
a partition, which is where the D row cap bites; it is not a claim about a third
`Geom` case, an essential torus, or a JSJ piece.  Those live in
`docs/audits/2026-08-25-vol-trm-division-of-labour-is-sound.md` and are not
established by anything measured here.

NO FLOAT64: mpmath throughout at the compute dps; `float()` only for display.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402

Q0 = mp.mpf(str(Q_50_DIGIT_STR))
ZERO = mp.mpf("1e-40")
LEVELS = [(1, 3), (2, 6), (3, 9), (4, 12)]


def conjugate(p: tuple[int, ...]) -> tuple[int, ...]:
    """Conjugate (transpose) partition."""
    if not p:
        return ()
    return tuple(sum(1 for x in p if x > j) for j in range(p[0]))


def main() -> int:
    wb = WitnessBuilder("markov-weight-support-conjugation",
                        engine="python-exact")
    wb.set_description(
        "Convention-D Wedderburn-Jones-Markov weights y_lambda at n = 3, 6, 9, "
        "12: support, signs, and the image of the support under partition "
        "conjugation. No weight is negative at any n, so the deuteron SDP "
        "witness's 'indefinite Frobenius Gram' and its 'Type-B folding "
        "signature' note are convention-C artifacts; under D the Gram is PSD "
        "with a kernel. Conjugation maps the entire support into the kernel "
        "from n = 6 (A = 2) on, but not at n = 3, because the self-conjugate "
        "partition first acquires a third row at n = 6.")

    print(f"q0 = {mp.nstr(Q0, 30)}   dps = {mp.mp.dps}\n")

    per_level = {}
    for A, n in LEVELS:
        y = {p: mp.mpf(str(v)) for p, v in y_lambda_at(n, Q0).items()}
        support = sorted(p for p, v in y.items() if abs(v) > ZERO)
        negative = sorted(p for p, v in y.items() if v < -ZERO)
        selfconj = sorted(p for p in y if conjugate(p) == p)
        selfconj_supported = [p for p in selfconj if abs(y[p]) > ZERO]
        conj_all_in_kernel = all(
            abs(y.get(conjugate(p), mp.mpf(0))) <= ZERO for p in support)
        per_level[f"n={n}"] = {
            "A": A, "n": n,
            "blocks": len(y),
            "supported": len(support),
            "support": [list(p) for p in support],
            "negative": [list(p) for p in negative],
            "self_conjugate": [list(p) for p in selfconj],
            "self_conjugate_supported": [list(p) for p in selfconj_supported],
            "max_rows_in_support": max(len(p) for p in support),
            "conjugation_maps_support_into_kernel": conj_all_in_kernel,
        }
        print(f"=== A={A}  n={n} ===")
        print(f"  blocks {len(y):>3}   supported {len(support):>2}   "
              f"negative {len(negative)}   max rows in support "
              f"{max(len(p) for p in support)}")
        print(f"  support            {[list(p) for p in support]}")
        print(f"  self-conjugate     {[list(p) for p in selfconj]}"
              f"   of which supported: "
              f"{[list(p) for p in selfconj_supported]}")
        print(f"  conj(support) is entirely in the kernel: "
              f"{conj_all_in_kernel}")

    # The one candidate bar identity, tested and reported as failing.
    print("\n=== candidate bar identity  y_l(1/q0) == y_l'(q0)  ===")
    bar_gaps = {}
    for A, n in LEVELS:
        y = {p: mp.mpf(str(v)) for p, v in y_lambda_at(n, Q0).items()}
        yi = {p: mp.mpf(str(v)) for p, v in y_lambda_at(n, 1 / Q0).items()}
        worst, at = mp.mpf(0), None
        for p in y:
            gap = abs(yi.get(p, mp.mpf(0)) - y.get(conjugate(p), mp.mpf(0)))
            if gap > worst:
                worst, at = gap, p
        bar_gaps[f"n={n}"] = {"worst_gap": mp.nstr(worst, 25),
                              "at_partition": list(at) if at else None}
        print(f"  n={n:>2}  worst gap {mp.nstr(worst, 10):>14}  at {at}")

    # ── assertions ────────────────────────────────────────────────────────
    # A1 — THE CORRECTION: no negative weight anywhere under D. This is what
    #      makes the committed witness's "indefinite" verdict convention-C.
    tot_neg = sum(len(v["negative"]) for v in per_level.values())
    wb.add_assertion(
        name="no_negative_weights_under_convention_D",
        computed=str(tot_neg), expected="0", tolerance="0", unit="count",
        source="y_lambda_at (convention D since 2026-08-09; owner ruling R1)")

    # A2 — CONTROL that the D row cap is actually in force. If this failed the
    #      run would be convention C and A1 would be meaningless.
    max_rows = max(v["max_rows_in_support"] for v in per_level.values())
    wb.add_assertion(
        name="control_row_cap_two_rows_in_force",
        computed=str(max_rows), expected="2", tolerance="0", unit="rows",
        source="convention D: y_lambda = 0 for ell(lambda) > 2")

    # A3 — CONTROL on the support size: the two-row partitions of n number
    #      floor(n/2)+1. A support that did not match would mean the weights
    #      are not the D ones whatever the row cap says.
    ok_counts = all(v["supported"] == v["n"] // 2 + 1
                    for v in per_level.values())
    wb.add_assertion(
        name="control_support_is_the_two_row_partitions",
        computed="1" if ok_counts else "0", expected="1", tolerance="0",
        unit="boolean", source="count of two-row partitions of n is n//2 + 1")

    # A4 — THE TRANSITION, negative half: at A=1 conjugation does NOT send the
    #      support into the kernel.
    wb.add_assertion(
        name="A1_conjugation_does_not_empty_support",
        computed="1" if not per_level["n=3"][
            "conjugation_maps_support_into_kernel"] else "0",
        expected="1", tolerance="0", unit="boolean",
        source="(2,1) is self-conjugate with two rows, so y != 0")

    # A5 — THE TRANSITION, positive half: from A=2 on, it does.
    from_A2 = all(per_level[f"n={n}"]["conjugation_maps_support_into_kernel"]
                  for A, n in LEVELS if A >= 2)
    wb.add_assertion(
        name="from_A2_conjugation_maps_support_into_kernel",
        computed="1" if from_A2 else "0", expected="1", tolerance="0",
        unit="boolean",
        source="two-row lambda of n>=6 has lambda_1>=3, so ell(lambda')>=3")

    # A6 — the mechanism, stated as a check rather than asserted in prose: the
    #      self-conjugate partition is supported at A=1 and at no larger A.
    sc_supported = {v["A"]: len(v["self_conjugate_supported"])
                    for v in per_level.values()}
    wb.add_assertion(
        name="self_conjugate_supported_only_at_A1",
        computed=str(sum(1 for A, k in sc_supported.items() if k > 0)),
        expected="1", tolerance="0", unit="count",
        source="staircase (2,1) at n=3 has 2 rows; (3,2,1) at n=6 has 3")

    # A7 — the candidate bar identity FAILS, and by an amount of order the
    #      weights themselves. Recorded as a measured negative, scope (a).
    worst_overall = max(mp.mpf(v["worst_gap"]) for v in bar_gaps.values())
    wb.add_assertion(
        name="candidate_bar_identity_fails_at_order_unity",
        computed="1" if worst_overall > mp.mpf("1e-3") else "0",
        expected="1", tolerance="0", unit="boolean",
        source="y_l(1/q0) vs y_l'(q0); ONE candidate form, not an exclusion")

    wb.add_data("q0", mp.nstr(Q0, 50))
    wb.add_data("per_level", per_level)
    wb.add_data("candidate_bar_identity_gaps", bar_gaps)
    wb.add_caveat(
        "The committed deuteron-real-sdp.witness.json is convention C: its "
        "eleven Gram entries are all nonzero, while D zeroes every partition "
        "with more than two rows. Its 'indefinite', 'forbidden negative-norm "
        "blocks' and 'Type-B folding signature' fields are C-frame and are NOT "
        "corrected by this probe -- only shown not to describe D.")
    wb.add_caveat(
        "'Third channel' here means the third ROW of a partition. No claim is "
        "made about a third Geom case, an essential torus, or a JSJ piece.")
    wb.save()
    print("\nwitness written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
