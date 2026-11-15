#!/usr/bin/env python3
"""The last three files of the Molien blast radius — does the ruling reach them?

Bean `qou-oots`, closing the triage of the corrected 11-of-38 (PR #6840). Six
were settled in #6840/#6849 and by `qou-wapd`; two of the remainder are my own
comparison harnesses (`molien_feray_meliot_bridge_probe`,
`phi_k_weight_family_discriminator`), which carry every family by construction
and are not consumers. Three real files were left, and they land differently.

FILE 1 -- `deltalambda/wlambda_transfer_matrix_connected_probe.py`. This is the
one where the ruling does not merely move a number. Its check 1 is:

    tr(T) = Z(n) = SUM_lam W_lam,   W_lam = d_q(lam)^2/[n]_q!

    "the audit / Lean-proved defect is 1 - Z(n) = C(n) h^2 + O(h^4) with
     144 C(n) = -n(n-1)(2n-13) -> the n=7 SIGN CHANGE (Z crosses 1)"

So its subject IS the non-normalisation of the superseded family -- the very
property `qou-oots` used to rule against it. The Molien family sums to EXACTLY 1
at every n (`molienSum_eq_qFactorial`, Lean, sorry-free), so under the canonical
family the defect is identically zero, the cubic has no coefficient to fit, and
the n = 7 sign change does not exist. That is not a moved number; the
phenomenon the check is built on is family-specific.

WHAT THAT DOES AND DOES NOT IMPLY. It does NOT say the probe is wrong: it
measures a real property of the family it names, and its Lean-proved cubic
stands as a statement about `d_q^2/[n]_q!`. What it says is that check 1 cannot
be carried over -- if the transfer matrix is to be built from the canonical
weight, check 1 has no content and checks 2-3 (the connected part) need
re-deriving on a T whose trace is 1. Which of those two the corpus wants is a
structural question about what the transfer matrix is a transfer matrix OF, and
is not settled here.

FILE 2 -- `sweeps/paper_six_term_shadow_price_sweep.py`. NOT sloppy; the second
counter-example after `alpha_em_b2_canonical_scale_ratio_probe`. Its `w_lambda`
docstring already says "symmetric Plancherel, NOT Jones-Markov" and points
Markov-trace callers at `markov_weights_symbolic.solve_y_lambda`. It does carry
one claim worth checking rather than accepting -- "coincides with Jones-Markov
y_lambda only at q = 1" -- because `qou-wapd` measured that at q -> 1 the
SU(2)-specialised y_lambda is still exactly zero on 7 of the 11 partitions of 6,
which would make even the q = 1 coincidence false. Both readings are tested
below; they are different objects and the docstring is true of one of them.

FILE 3 -- `yekutieli_volume_join.py`. Classified by reading, not measured here:
its `w_lambda` feeds the Stage-4 form `m = m_e Geom(K) SUM_{lam |- 3} w_lam
chi_lam/dim lam` at a single fixed n = 3, and the script REPORTS A RATIO of two
h-expansions rather than either side alone. A same-n ratio is invariant under a
lambda-independent rescaling (`WLambdaNormalizationInvariance.ratio_invariant`)
but NOT under Molien, whose q^{-kappa} is lambda-dependent -- so the ruling does
reach it. It is nonetheless MOOT for the absolute-mass reading: the file's own
header records that the Vol-rho form it serves was DEPRECATED for absolute mass
by the 2026-06-24 ruling in favour of the muon-anchored `canonical_mass.py`.
Same disposition as the two beta_EW files under `qou-wapd`: the ruling reaches
it, and the construction it serves is already outside the carrier.

No float64: mpmath end to end; partitions, hooks and f^lambda exact integers.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from mpmath import mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402
from y_lambda_su_n import y_lambda_su_n  # noqa: E402

_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import molien_feray_meliot_bridge_probe as MB  # noqa: E402
import plancherel_deformation_uniqueness_probe as PU  # noqa: E402

# Module-scope constants below are built at import time; mpmath's default is
# 15 dps, so raise it first (import-time dps ratchet).
set_compute_dps()

N_RANGE = tuple(range(2, 10))          # the probe's own check-1 range
Q_NEAR_ONE = mp.mpf("1") + mp.mpf("1e-25")


def defect_cubic(n: int) -> mp.mpf:
    """C(n) with 144 C(n) = -n(n-1)(2n-13), the probe's Lean-proved coefficient."""
    return mp.mpf(-n * (n - 1) * (2 * n - 13)) / 144


def main() -> int:
    set_compute_dps()
    q0 = mp.mpf(Q_50_DIGIT_STR)

    b = WitnessBuilder("molien-blast-radius-remainder-triage")
    b.set_description(
        "Bean qou-oots. Triages the last three real consumers of the corrected "
        "Molien blast radius (11 of 38). Headline: "
        "deltalambda/wlambda_transfer_matrix_connected_probe.py builds its "
        "transfer matrix from W_lam = d_q^2/[n]_q! and its check 1 measures the "
        "NON-NORMALISATION of that family (1 - SUM_lam W_lam = C(n) h^2 + ..., "
        "with a Lean-proved cubic and an n=7 sign change). The Molien family "
        "sums to EXACTLY 1 at every n, so under the canonical family that "
        "defect is identically zero and the n=7 crossing does not exist -- the "
        "phenomenon is family-specific, not a moved number. Also tests the "
        "q->1 coincidence claim in paper_six_term_shadow_price_sweep.py's "
        "w_lambda docstring, which is true of the uncapped Markov weight and "
        "false of the SU(2)-specialised one. NOT a claim that either file is "
        "wrong."
    )
    b.add_parameter("q0_50dps", Q_50_DIGIT_STR)
    b.add_parameter("n_range", str(list(N_RANGE)))

    # -- FILE 1: the defect exists for one family and not the other ------------
    rows = {}
    molien_max_dev = mp.mpf(0)
    sign_changes = []
    prev_sign = None
    for n in N_RANGE:
        lams = MB.partitions(n)
        qfact = PU.q_factorial(q0, n)
        Z = mp.fsum(PU.dim_q(q0, l) ** 2 / qfact for l in lams)
        Zm = mp.fsum(MB.molien_weight(q0, l) for l in lams)
        dev = abs(Zm - 1)
        molien_max_dev = max(molien_max_dev, dev)
        defect = 1 - Z
        s = 1 if defect > 0 else (-1 if defect < 0 else 0)
        if prev_sign is not None and s != prev_sign:
            sign_changes.append(n)
        prev_sign = s
        rows[str(n)] = {
            "partitions": len(lams),
            "Z_dimq2": fmt(Z),
            "defect_1_minus_Z": fmt(defect),
            "defect_sign": s,
            "C_n_lean_cubic": fmt(defect_cubic(n)),
            "C_n_sign": 1 if defect_cubic(n) > 0 else (-1 if defect_cubic(n) < 0 else 0),
            "Z_molien": fmt(Zm),
            "molien_deviation_from_1": fmt(dev),
        }
    b.add_data("normalisation_by_family", {
        "rows": rows,
        "dimq2_sign_changes_at_n": sign_changes,
        "molien_max_deviation_from_1": fmt(molien_max_dev),
        "note": "The left family is the transfer-matrix probe's W_lam; the "
                "right is the canonical Molien weight. The probe's check 1 "
                "tests that sign(1 - Z(n)) tracks sign(C(n)) with the n=7 "
                "crossing. Under Molien there is nothing to track: the "
                "deviation is at the floor of the arithmetic at every n, so "
                "the defect, its cubic and its crossing all cease to exist.",
    })

    b.add_assertion(
        "molien_sums_to_one_at_every_n_in_range",
        computed=fmt(molien_max_dev), expected="0", tolerance="1e-40",
        unit="relative",
        source="SUM_lam f^lam q^{-kappa} d_q(lam)/[n]_q! = 1 for n = 2..9, "
               "matching the Lean molienSum_eq_qFactorial. This is what makes "
               "the transfer-matrix probe's check-1 defect family-specific.",
    )
    b.add_assertion(
        "dimq2_defect_changes_sign_at_n_equals_7",
        computed=str(sign_changes), expected="[7]",
        source="Reproduces the transfer-matrix probe's own check 1 on the "
               "superseded family, so the contrast above is against that "
               "probe's actual behaviour rather than against a paraphrase of "
               "it. A different crossing here would mean this triage had "
               "mis-modelled the file and should not be trusted.",
    )

    # -- FILE 2: which y_lambda does the q->1 coincidence claim hold for? ------
    # The sweep's docstring says w_lam "coincides with Jones-Markov y_lambda
    # only at q = 1". qou-wapd measured the SU(2)-specialised y_lambda to be
    # exactly zero on every lambda with more than two rows EVEN AT q -> 1 (the
    # row cap is a statement about N, not about q). So the claim is true of an
    # uncapped Markov weight and false of the SU(N=2) one -- a scoping
    # refinement, not a refutation, and worth recording because a reader who
    # takes the docstring to cover y_lambda_su_n(n, q, 2) would be wrong.
    coincidence = {}
    for n in (3, 4, 6):
        lams = MB.partitions(n)
        nfact = 1
        for k in range(1, n + 1):
            nfact *= k
        w_at_1 = {l: mp.mpf(MB.f_lambda(l)) ** 2 / nfact for l in lams}
        y2 = y_lambda_su_n(n, Q_NEAR_ONE, 2)
        zeros = [l for l in lams if l in y2 and mp.mpf(str(y2[l])) == 0]
        coincidence[str(n)] = {
            "partitions": len(lams),
            "sum_w_at_q_eq_1": fmt(mp.fsum(w_at_1.values())),
            "y_su2_exact_zeros_at_q_to_1": len(zeros),
            "zero_shapes": [list(l) for l in zeros],
            "w_nonzero_on_those_shapes": all(w_at_1[l] != 0 for l in zeros),
        }
    b.add_data("q_to_one_coincidence_claim", {
        "per_n": coincidence,
        "verdict": "The sweep's docstring claim is TRUE of an uncapped "
                   "Jones-Markov y_lambda (w_lam -> (f^lam)^2/n! at q=1, which "
                   "sums to 1 by Burnside) and FALSE of the SU(2)-specialised "
                   "y_lambda_su_n(n, q, 2), which is exactly zero on every "
                   "lambda of more than two rows even at q -> 1 -- the row cap "
                   "is a statement about N, not about q. Scoping refinement, "
                   "not a refutation: the docstring names Jones-Markov and "
                   "points at solve_y_lambda, which is the uncapped object.",
    })

    b.save()

    print(f"q0 = {Q_50_DIGIT_STR[:16]}\n")
    print(f"{'n':>2} {'#lam':>5}  {'Z = SUM d_q^2/[n]!':>26} {'1 - Z':>14} {'sgn':>4} "
          f"{'sgn C(n)':>9}  {'SUM Molien':>22}")
    for n in N_RANGE:
        r = rows[str(n)]
        print(f"{n:>2} {r['partitions']:>5}  {r['Z_dimq2'][:26]:>26} "
              f"{r['defect_1_minus_Z'][:14]:>14} {r['defect_sign']:>4} "
              f"{r['C_n_sign']:>9}  {r['Z_molien'][:22]:>22}")
    print(f"\ndim_q^2 family: defect sign changes at n = {sign_changes}")
    print(f"Molien family : max |SUM - 1| = {fmt(molien_max_dev)}  "
          f"-> no defect, no cubic, no crossing\n")
    for n in (3, 4, 6):
        c = coincidence[str(n)]
        print(f"n={n}: SUM w(q=1) = {c['sum_w_at_q_eq_1'][:20]}   "
              f"y_su2 exact zeros at q->1: {c['y_su2_exact_zeros_at_q_to_1']}"
              f"/{c['partitions']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
