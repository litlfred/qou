#!/usr/bin/env python3
"""ylambda_sign_content_threshold_probe.py — the content-threshold parity is CONVENTION-C.

RETIRED AS A LIVE RULE, 2026-08-25 (bean `qou-ulxr`).  This file no longer asserts the
sign rule; it records WHY the rule cannot be carried into convention D, and asserts the
two structural facts that replace it.  The C-frame measurement is preserved below, not
deleted — the numbers were right for the convention they were taken in.

WHAT THE PROBE USED TO CLAIM (convention C, still true THERE)
------------------------------------------------------------
With `y_λ = s_λ / Z` and the Wenzl principal specialisation

    s_λ  =  Q^{n(λ)} · ∏_{x ∈ λ} (1 − Q^r·Q^{c(x)}) / (1 − Q^{h(x)}),      Q = q²,

for `q > 1` every hook factor `1 − Q^{h(x)}` is negative, so the denominator contributes a
fixed `(−1)^{|λ|}`; a numerator factor is negative exactly when the cell's content lies
ABOVE the threshold `c* = −log_Q(Q^r)`.  Writing `P(λ)` for the count of cells BELOW it,

    sign(s_λ) = (−1)^{P(λ)}.

Under C (`r ≈ 2.5995`, `c* ≈ −2.5995`) this held on all 270 partitions for n = 2..12, and
the committed witness of 2026-08-08 recorded it with both assertions green.

WHY IT DOES NOT SURVIVE CONVENTION D — TWO INDEPENDENT REASONS
--------------------------------------------------------------
Convention D pins the Wenzl level at `r = 2` (`wenzlLevel_conventionD`), so `Q^r = Q²`.

1. THE THRESHOLD LANDS ON THE CONTENT LATTICE.  `c* = −log_Q(Q²) = −2` EXACTLY — and −2
   is an attainable content, realised at row 3, column 1 of every diagram with `ℓ(λ) ≥ 3`.
   There the test factor is `Q^r·Q^{c} = Q²·Q^{−2} = 1` exactly, so the cell is neither
   above nor below: the margin is 0, not merely small.  This is precisely the hypothesis
   `hnd : ∀ x ∈ cells, QR * val x ≠ 1` of `QOU.MassTheory.YLambdaSignThreshold.wenzl_sign`,
   whose own docstring says that without it "the parity is genuinely undefined, not merely
   hard to prove".  The Lean is untouched and still correct: it is a conditional, and under
   D its premise is UNSATISFIABLE on the `ℓ(λ) ≥ 3` stratum.  Conditional-proved is not
   premise-established.

   Under C, `c* ≈ −2.5995` sits strictly between two lattice points, so `hnd` holds
   everywhere and the rule is well-posed.  The convention change moved the threshold ONTO
   the lattice; that, and not any numerical drift, is what breaks it.

2. WHERE IT REMAINS WELL-POSED, IT IS VACUOUS.  D also forces `y_λ = 0` for every
   `ℓ(λ) ≥ 3` (`schurPrincipal_eq_zero_iff`), leaving the two-row stratum.  A cell at row
   `i`, column `j` has content `j − i`, so for `ℓ(λ) ≤ 2` the minimum content is `−1`,
   while a below-threshold cell needs `c ≤ −3`.  The threshold is therefore unreachable on
   the surviving stratum BY CONSTRUCTION, for every `n` — `P(λ) ≡ 0`, the rule predicts the
   constant `+1`, and it is correct but carries no information.

   All of the rule's discriminating power lived in cells of content `≤ −3`, which need
   `ℓ(λ) ≥ 4` — exactly the stratum D annihilates.

So there is no two-row restatement to be had: reason 2 says the surviving stratum cannot
support the rule, and reason 1 says the annihilated stratum cannot even be asked.  This
probe is a record, not a live test.

SCOPE.  Scope-(a), and about this RULE under this CONVENTION.  Nothing here refutes the
Lean, which is generic in `Q` and `QR` and remains sorry-free and correct; nothing here
says a sign rule for the two-row stratum is impossible — it says THIS threshold parity has
no content there, because the sign is constant.

WHAT THIS PROBE NOW ASSERTS (all measured under D, at q₀)
---------------------------------------------------------
  * `threshold_is_on_content_lattice`  — c* is exactly the integer −2
  * `hnd_fails_on_three_row_stratum`   — every n ≥ 3 has a λ with an exactly-on-threshold
                                          cell, so `wenzl_sign`'s premise is unsatisfiable
  * `no_deep_cells_on_surviving_stratum` — P(λ) = 0 for every ℓ(λ) ≤ 2, every n
  * `surviving_stratum_sign_is_constant` — sign(y_λ) = +1 for every surviving block

Measurement only.  Nothing is fitted and nothing is wired.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parent.parent),
                str(Path(__file__).resolve().parent.parent / "substrate")]
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

from schur_principal_mpmath import (  # noqa: E402
    _wenzl_constants, hooks_and_contents, partitions_of, y_lambda_at_q0_mpmath,
)
from q_parameter import Q_MP as Q0  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(50)
q0 = mp.mpf(str(Q0))
N_MIN, N_MAX = 2, 12
DEGEN_TOL = mp.mpf("1e-12")
SURVIVING_ROWS = 2          # convention D: Wenzl level r = 2

# The convention-C record this probe used to assert, kept verbatim so the finding is not
# lost with the rule.  Source: the committed witness of 2026-08-08T21:52:48Z.
C_FRAME_RECORD = {
    "convention": "C",
    "computed_at": "2026-08-08T21:52:48Z",
    "wenzl_level_r": "2.5995 (approx)",
    "c_star": "-2.5995 (approx) — strictly between lattice points, so hnd holds",
    "rule_holds_all_partitions": True,
    "no_threshold_degeneracy": True,
    "n_negative_y_by_n_2_to_9": [0, 0, 1, 1, 3, 4, 8, 10],
    "note": "correct for convention C. Superseded as a live rule by this probe under D; "
            "see the module docstring for the two reasons.",
}


def deep_cell_count(lam, Q, QR):
    """P(λ) = #{cells strictly BELOW the threshold}, plus the smallest |Q^r·Q^c − 1|.

    The margin is the degeneracy guard: a cell sitting exactly on the threshold makes the
    above/below split — and hence the parity — undefined.
    """
    _hs, cs = hooks_and_contents(lam)
    P, margin = 0, None
    for c in cs:
        v = QR * Q ** c
        m = abs(v - 1)
        margin = m if margin is None else min(margin, m)
        if v < 1:
            P += 1
    return P, margin


def main() -> int:
    Q, QR = _wenzl_constants(q0)
    c_star = -mp.log(QR) / mp.log(Q)
    c_star_int = mp.floor(c_star + mp.mpf("0.5"))
    on_lattice = abs(c_star - c_star_int) < mp.mpf("1e-40")

    print("=" * 88)
    print(" the content-threshold parity is a CONVENTION-C rule — retirement record")
    print("=" * 88)
    print(f" q₀ = {mp.nstr(q0, 12)}   Q = q₀² = {mp.nstr(Q, 12)}   Q^r = {mp.nstr(QR, 12)}")
    print(f" Q^r == Q² (convention D, r = 2)?  {abs(QR - Q ** 2) < mp.mpf('1e-40')}")
    print(f" c* = −log_Q(Q^r) = {mp.nstr(c_star, 20)}")
    print(f" c* is EXACTLY the integer {int(c_star_int)}?  {on_lattice}"
          "   ← if so, the above/below test is degenerate on the lattice\n")

    print(f" {'n':>3} {'parts':>6} | {'ℓ≤2':>5} {'P>0 there':>10} {'signs':>8}"
          f" | {'ℓ≥3':>5} {'min margin':>12} {'hnd':>9}")
    print(" " + "-" * 78)

    rows = []
    lattice_ok = bool(on_lattice)
    hnd_fails_all_n = True          # for every n ≥ 3
    surv_no_deep_all = True
    surv_positive_all = True

    for n in range(N_MIN, N_MAX + 1):
        y = y_lambda_at_q0_mpmath(n, q0)
        shapes = partitions_of(n)
        surv = [l for l in shapes if len(l) <= SURVIVING_ROWS]
        dead = [l for l in shapes if len(l) > SURVIVING_ROWS]

        surv_deep = 0
        surv_signs = set()
        for lam in surv:
            P, _m = deep_cell_count(lam, Q, QR)
            surv_deep += P
            surv_signs.add(1 if y[lam] > 0 else (-1 if y[lam] < 0 else 0))

        min_margin = None
        for lam in shapes:
            _P, m = deep_cell_count(lam, Q, QR)
            min_margin = m if min_margin is None else min(min_margin, m)
        hnd_holds = min_margin > DEGEN_TOL

        if surv_deep != 0:
            surv_no_deep_all = False
        if surv_signs - {1}:
            surv_positive_all = False
        if dead and hnd_holds:
            hnd_fails_all_n = False

        print(f" {n:>3} {len(shapes):>6} | {len(surv):>5} {surv_deep:>10}"
              f" {str(sorted(surv_signs)):>8} | {len(dead):>5}"
              f" {mp.nstr(min_margin, 6):>12} {'holds' if hnd_holds else 'UNSAT':>9}")

        rows.append({
            "n": n,
            "n_partitions": len(shapes),
            "n_surviving_two_row": len(surv),
            "deep_cells_on_surviving_stratum": surv_deep,
            "surviving_signs": sorted(surv_signs),
            "n_annihilated_three_row_plus": len(dead),
            "min_threshold_margin": mp.nstr(min_margin, 20),
            "hnd_satisfiable": bool(hnd_holds),
        })

    print("\n" + "=" * 88)
    print(" c* sits exactly on the content lattice, so `wenzl_sign`'s hypothesis")
    print(" `hnd : Q^r·val ≠ 1` is UNSATISFIABLE for every ℓ(λ) ≥ 3 — the parity is")
    print(" undefined there, not merely unmeasured. On the surviving two-row stratum")
    print(" every P(λ) = 0, so the rule degenerates to the constant +1.")
    print(" The rule's discriminating power required cells of content ≤ −3, i.e. ℓ ≥ 4,")
    print(" which is exactly the stratum convention D annihilates.")
    print("=" * 88)

    w = WitnessBuilder("ylambda-sign-content-threshold", engine="mpmath",
                       output_dir=Path(__file__).resolve().parent)
    w.add_assertion("threshold_is_on_content_lattice", 1 if lattice_ok else 0, 1)
    w.add_assertion("hnd_fails_on_three_row_stratum", 1 if hnd_fails_all_n else 0, 1)
    w.add_assertion("no_deep_cells_on_surviving_stratum", 1 if surv_no_deep_all else 0, 1)
    w.add_assertion("surviving_stratum_sign_is_constant", 1 if surv_positive_all else 0, 1)
    w.add_parameter("q0", mp.nstr(q0, 30))
    w.add_parameter("Q", mp.nstr(Q, 30))
    w.add_parameter("QR", mp.nstr(QR, 30))
    w.add_parameter("c_star", mp.nstr(c_star, 30))
    w.add_parameter("wenzl_level_r", "2 (convention D)")
    w.add_parameter("surviving_rows", str(SURVIVING_ROWS))
    w.add_data("by_n", rows)
    w.add_data("convention_c_record", C_FRAME_RECORD)
    w.add_caveat(
        "RETIRED AS A LIVE RULE. This witness no longer asserts sign(y_λ) = sign(Z)·(−1)^P. "
        "That rule is correct under convention C and is preserved in `convention_c_record`; "
        "under D it is undefined on ℓ(λ) ≥ 3 (threshold exactly on the content lattice) and "
        "vacuous on ℓ(λ) ≤ 2 (no cell can reach it). Do not read the C numbers as live."
    )
    w.add_caveat(
        "Scope-(a), about this rule under this convention. "
        "`QOU.MassTheory.YLambdaSignThreshold.wenzl_sign` is generic in Q and QR, remains "
        "sorry-free and correct, and is NOT refuted here — under D its hypothesis `hnd` is "
        "simply unsatisfiable on the ℓ(λ) ≥ 3 stratum. Conditional-proved is not "
        "premise-established. Nor is a two-row sign rule shown impossible; this threshold "
        "parity merely has no content there, the sign being constant."
    )
    w.set_description(
        "Records why the sign(y_λ) content-threshold parity is a convention-C phenomenon "
        "and cannot be carried into D. Under D the Wenzl level is r = 2, so Q^r = Q² and "
        "c* = −log_Q(Q^r) = −2 EXACTLY — an attainable content (row 3, col 1), present in "
        "every λ with ℓ(λ) ≥ 3, where the test factor is exactly 1 and the above/below "
        "split is undefined. That is `wenzl_sign`'s `hnd` hypothesis failing outright. On "
        "the surviving two-row stratum the minimum content is −1 while a below-threshold "
        "cell needs ≤ −3, so P(λ) ≡ 0 and the rule is the constant +1. Swept n = 2..12. "
        "Supersedes the 2026-08-08 C-frame witness, whose green assertions this replaces."
    )
    w.save()

    ok = lattice_ok and hnd_fails_all_n and surv_no_deep_all and surv_positive_all
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
