#!/usr/bin/env python3
"""ylambda_sign_content_threshold_probe.py — sign(y_λ) is a content-threshold parity.

THE CLAIM. The Jones–Markov central coefficient is `y_λ = s_λ / Z` with the Wenzl
principal specialisation (`schur_principal_mpmath`)

    s_λ  =  Q^{n(λ)} · ∏_{x ∈ λ} (1 − Q^r·Q^{c(x)}) / (1 − Q^{h(x)}),      Q = q².

For `q > 1` (so `Q > 1`) every hook length `h(x) ≥ 1` gives `1 − Q^{h(x)} < 0`, so the
denominator contributes the fixed sign `(−1)^{|λ|}`.  A numerator factor is negative exactly
when `Q^r·Q^{c(x)} > 1`, i.e. when the cell's content sits ABOVE the threshold

    c* := −log_Q(Q^r).

Writing `P(λ) := #{x ∈ λ : c(x) < c*}` for the count of cells BELOW it, the two sign
contributions combine to

    sign(s_λ) = (−1)^{P(λ)}                                      [the claim]

and hence `sign(y_λ) = sign(Z)·(−1)^{P(λ)}`.

WHY IT MATTERS. `Mu3SlotExclusion.door_mechanism_dichotomy` (PR #4657) shows a Wedderburn
block can push the μ₃ residual submodular in exactly two ways, one of which is
"negative weight on supermodular geometry".  That mechanism is governed entirely by
sign(y_λ), which until now was known only as "sign-indefinite for n ≥ 4"
(`docs/audits/2026-05-19-weight-factor-audit.md` §W3).  This probe replaces that qualitative
statement with a combinatorial rule, which is what makes the door budget computable rather
than merely observed.

At q₀ the threshold is `c* ≈ −2.5997`, so `P(λ)` counts cells of content `≤ −3`.  Those
require `≥ 4` rows, which is why every `ℓ(λ) ≤ 3` block carries a positive weight — including
`(8,1)`, the case that refutes the naive "ℓ-parity" guess.

GATES (fail loudly):
  * the predicted sign must match the measured sign of `y_λ` for EVERY partition,
    for every `n` in the swept range — a single mismatch fails the probe;
  * no cell may sit within `1e-12` of the threshold (a near-degenerate content would make
    the parity ill-defined at finite precision; report and fail rather than round).

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


def deep_cell_count(lam, Q, QR):
    """P(λ) = #{cells whose content lies BELOW the threshold c* = −log_Q(QR)}.

    Equivalently `QR·Q^{c(x)} < 1`.  Returns (P, min_margin) where min_margin is the
    smallest `|QR·Q^c − 1|` over the diagram — the degeneracy guard.
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
    print("=" * 86)
    print(" sign(y_λ) is a content-threshold parity — verification sweep")
    print("=" * 86)
    print(f" q₀ = {mp.nstr(q0, 12)}   Q = q₀² = {mp.nstr(Q, 12)}   Q^r = {mp.nstr(QR, 12)}")
    print(f" content threshold c* = −log_Q(Q^r) = {mp.nstr(c_star, 12)}"
          f"   → cells with c ≤ {int(mp.floor(c_star))} are 'deep'")
    print(f" predicted rule:  sign(y_λ) = sign(Z)·(−1)^P(λ),  P = #deep cells\n")

    print(f" {'n':>3} {'parts':>7} {'matches':>9} {'neg y':>7} {'min |QR·Q^c−1|':>17}"
          f"  {'sign(Z)':>8}  verdict")
    print(" " + "-" * 76)

    all_ok, degen_ok, rows = True, True, []
    for n in range(N_MIN, N_MAX + 1):
        y = y_lambda_at_q0_mpmath(n, q0)
        shapes = partitions_of(n)
        # sign(Z) is a single global sign; infer it from any one block, then require
        # every block to be consistent with that same choice.
        lam0 = shapes[0]
        P0, _ = deep_cell_count(lam0, Q, QR)
        sZ = 1 if (mp.sign(y[lam0]) == (1 if P0 % 2 == 0 else -1)) else -1

        matches, n_neg, min_margin = 0, 0, None
        mismatches = []
        for lam in shapes:
            P, margin = deep_cell_count(lam, Q, QR)
            min_margin = margin if min_margin is None else min(min_margin, margin)
            pred = sZ * (1 if P % 2 == 0 else -1)
            meas = 1 if y[lam] > 0 else -1
            if y[lam] < 0:
                n_neg += 1
            if pred == meas:
                matches += 1
            else:
                mismatches.append((lam, P, pred, meas, mp.nstr(y[lam], 6)))
        ok = (matches == len(shapes))
        deg = min_margin > DEGEN_TOL
        all_ok, degen_ok = all_ok and ok, degen_ok and deg
        verdict = "OK" if (ok and deg) else ("MISMATCH" if not ok else "DEGENERATE")
        print(f" {n:>3} {len(shapes):>7} {matches:>4}/{len(shapes):<4} {n_neg:>7}"
              f" {mp.nstr(min_margin, 6):>17}  {sZ:>8}  {verdict}")
        for m in mismatches:
            print(f"      MISMATCH λ={m[0]} P={m[1]} predicted={m[2]} measured={m[3]}"
                  f" y={m[4]}")
        rows.append({"n": n, "n_partitions": len(shapes), "n_matches": matches,
                     "n_negative_y": n_neg, "sign_Z": sZ,
                     "min_threshold_margin": mp.nstr(min_margin, 20),
                     "all_match": bool(ok),
                     "mismatches": [str(m[0]) for m in mismatches]})

    print("\n" + "=" * 86)
    if all_ok and degen_ok:
        tot = sum(r["n_partitions"] for r in rows)
        print(f" RESULT: the rule holds on ALL {tot} partitions for n = {N_MIN}..{N_MAX}.")
        print("   sign(y_λ) is determined by the PARITY of the number of cells whose")
        print("   content falls below c* = −log_Q(Q^r).  Since a cell of content ≤ −3")
        print("   needs ≥ 4 rows, every λ with ℓ(λ) ≤ 3 carries a positive weight — which")
        print("   is why (8,1) is positive and the naive ℓ-parity guess fails.")
    else:
        print(" RESULT: FAILED — see mismatches above. The rule as stated is wrong.")
    print("=" * 86)

    w = WitnessBuilder("ylambda-sign-content-threshold", engine="mpmath",
                       output_dir=Path(__file__).resolve().parent)
    w.add_assertion("rule_holds_all_partitions", 1 if all_ok else 0, 1)
    w.add_assertion("no_threshold_degeneracy", 1 if degen_ok else 0, 1)
    w.add_parameter("q0", mp.nstr(q0, 30))
    w.add_parameter("Q", mp.nstr(Q, 30))
    w.add_parameter("QR", mp.nstr(QR, 30))
    w.add_parameter("c_star", mp.nstr(c_star, 30))
    w.add_data("by_n", rows)
    w.add_caveat(
        "The threshold c* = −log_Q(Q^r) is q-dependent; the concrete cut 'content ≤ −3' is "
        "specific to q₀. The PARITY RULE itself is q-independent for q > 1 — only the "
        "location of the cut moves."
    )
    w.add_caveat(
        "sign(Z) is inferred per n from one block and then required to be consistent "
        "across all blocks; the probe verifies consistency, it does not independently "
        "derive sign(Z)."
    )
    w.set_description(
        "Verifies that sign(y_λ) equals sign(Z)·(−1)^P(λ), where P(λ) counts cells of λ "
        "whose content lies below c* = −log_Q(Q^r). Derived from the Wenzl principal "
        "specialisation: for Q>1 every hook factor 1−Q^h is negative (fixed sign "
        "(−1)^|λ|), and a numerator factor 1−Q^r·Q^c is negative exactly above the "
        "threshold. Swept over every partition for n=2..12. Replaces the qualitative "
        "'sign-indefinite for n≥4' of weight-factor-audit §W3 with a combinatorial rule, "
        "which is what makes the μ₃ door budget of PR #4657 computable."
    )
    w.save()
    return 0 if (all_ok and degen_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
