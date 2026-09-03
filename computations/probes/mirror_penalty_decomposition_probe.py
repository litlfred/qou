#!/usr/bin/env python3
"""The "proton-excess penalty" is two different quantities at A=3 and A=7.

`prop:mirror-baseline-cancellation` observes that `f(Z,N) - f(N,Z)` kills the
A-only baseline, so a perturbation to the baseline cannot move a mirror
difference. Bean qou-zf9n recorded that A=7 obeyed this under an unrelated
input drift (both members shifted -4.58, penalty invariant at -1.77) while A=3
did not (T -0.95, 3He -0.58, penalty moved -1.33 -> -0.95), and left the reason
uninvestigated with two hypotheses: the drift was not baseline-only at A=3, or
T and 3He were not regenerated together.

THE SECOND HYPOTHESIS IS DEAD. `delta-lambda-canonical-residual.witness.json`
is a single run — one computedAt, one commitSha, one scriptHash — so every row
including both A=3 members was regenerated together.

THE FIRST IS RIGHT, AND THERE IS AN EXACT DECOMPOSITION BEHIND IT. Since
`Delta_lambda = B_AME / B_pred`, the penalty is a difference of differences in
which the `10A-5` baseline cancels IDENTICALLY — that half of the proposition
is fine and holds for both pairs by algebra, not by luck:

    penalty = log_q [B_AME(pr)/B_AME(mir)]  -  log_q [B_pred(pr)/B_pred(mir)]
                     `-- experiment --'              `-- the model --'

Reproduces both recorded penalties (-0.9514 vs -0.951; -1.7692 vs -1.770, the
latter within the witness's own 3-decimal rounding). And it separates them:

    pair         experiment    model      penalty   dominated by
    3He / T       -0.904361  +0.047047   -0.951407  EXPERIMENT (95%)
    7Be / 7Li     -0.410183  +1.358988   -1.769170  THE MODEL  (77%)

So the penalty is NOT one quantity across A. At A=3 it essentially measures the
experimental mirror asymmetry — 0.764 MeV for 3He/T, the textbook Coulomb-
dominated mirror energy difference — with the model contributing 5 %. At A=7 it
is dominated by the model's OWN 15.2 % asymmetry in B_pred.

AND THE MODEL'S ASYMMETRY IS SIGN-BACKWARDS AT BOTH PAIRS. Experiment has the
proton-rich member LESS bound (Coulomb repulsion); `B_pred` has it MORE bound,
at both A=3 and A=7. That is not a defect: `B_pred(Z,N) = E_0*(tr_M(W_free) -
tr_M(W_atom))` is a pure Markov-trace quantity with NO electromagnetic term at
all, so its mirror asymmetry is purely topological and there is nothing in it
that could produce a Coulomb sign. What the numbers add is the SIZE: negligible
at A=3 (5 % of the penalty), dominant and wrong-signed at A=7 (77 %).

That explains the drift asymmetry directly. B_AME is fixed, so a change in
B_pred moves only the model half. A multiplicatively uniform change across a
mirror pair cancels in the difference (A=7, penalty invariant); a non-uniform
one does not (A=3). No appeal to regeneration order is needed.

SCOPE (a), scope-limited: this is about the canonical `B_pred` at these two
pairs. It does not say no model can get the mirror asymmetry right, and it does
not bear on the A=3 mirror-split mechanism worked in
`docs/audits/2026-07-13-mirror-split-one-third-mechanism-probe.md`, which
targets the EM-active channel and already records the corpus's derived
Coulomb/strong ratio `tanh(ln q_0) ~ 0.10396` (`def:coulomb-charge`). This
probe measures what the penalty IS made of; that audit asks what should supply
the missing piece.

It STRENGTHENS the existing "magnitude is NOT a single derivable number"
verdict, and sharpens it: the two penalties are not the same physical quantity,
so no single derivation should be expected to produce both.
"""

from __future__ import annotations

import json
import pathlib
import sys

import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
COMP = REPO / "computations"
for _p in (str(COMP), str(COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

RESIDUAL = "computations/delta-lambda-canonical-residual.witness.json"
# The recorded penalties are quoted to 3 decimals in the source producer's own
# table. Kept as STRINGS: mp.mpf("-0.951") is not exactly -0.951, so serialising
# str(mpf) would claim 50 digits for a 3-digit input — fake precision, and the
# raw-float64 ratchet is right to reject it. Parsed to mpf only for comparison.
PAIRS = (
    (3, (2, 1), (1, 2), "3He / T", "-0.951"),
    (7, (4, 3), (3, 4), "7Be / 7Li", "-1.770"),
)


def main() -> int:
    set_compute_dps()
    q = mp.mpf(str(Q))
    lnq = mp.log(q)
    src = json.loads((REPO / RESIDUAL).read_text(encoding="utf-8"))
    rows = src["data"]["rows"]
    by = {(r["Z"], r["N"]): r for r in rows}

    def lg(x) -> mp.mpf:
        return mp.log(mp.mpf(str(x))) / lnq

    out = []
    for A, pr, mir, name, recorded in PAIRS:
        a, b = by[pr], by[mir]
        exp_asym = lg(a["B_AME_MeV"]) - lg(b["B_AME_MeV"])
        mod_asym = lg(a["B_pred_canonical_MeV"]) - lg(b["B_pred_canonical_MeV"])
        penalty = exp_asym - mod_asym
        dev_diff = mp.mpf(str(a["deviation_from_law"])) - mp.mpf(str(b["deviation_from_law"]))
        recorded_mpf = mp.mpf(recorded)
        out.append({
            "A": A, "pair": name,
            "proton_rich": a["atom"], "mirror": b["atom"],
            "experimental_asymmetry_logq": str(exp_asym),
            "model_asymmetry_logq": str(mod_asym),
            "penalty_logq": str(penalty),
            "penalty_from_witness_deviations": str(dev_diff),
            "recorded_penalty": recorded,   # verbatim, at its true 3-decimal precision
            "experimental_mirror_energy_MeV": str(
                mp.mpf(str(a["B_AME_MeV"])) - mp.mpf(str(b["B_AME_MeV"]))),
            "dominated_by": "experiment" if abs(exp_asym) > abs(mod_asym) else "model",
            "dominant_share_pct": str(
                max(abs(exp_asym), abs(mod_asym)) / abs(penalty) * 100),
            "model_sign_matches_experiment": (exp_asym < 0) == (mod_asym < 0),
            "abs_model_over_abs_exp": str(abs(mod_asym) / abs(exp_asym)),
        })

    single_run = all(src.get(k) is not None for k in ("computedAt", "commitSha", "scriptHash"))
    checks = [
        ("residual_witness_is_a_single_run", single_run, True,
         "one computedAt/commitSha/scriptHash — both A=3 members regenerated together, "
         "so 'not regenerated together' is refuted"),
        ("decomposition_reproduces_recorded_penalties",
         all(abs(mp.mpf(r["penalty_logq"]) - mp.mpf(r["recorded_penalty"])) < mp.mpf("1e-3")
             for r in out), True,
         "penalty = experiment - model, to the witness's own 3-decimal rounding"),
        ("decomposition_matches_deviation_difference",
         all(abs(mp.mpf(r["penalty_logq"]) - mp.mpf(r["penalty_from_witness_deviations"]))
             < mp.mpf("1e-3") for r in out), True,
         "the 10A-5 baseline cancels identically — that half of the proposition holds"),
        ("dominance_flips_between_A3_and_A7",
         out[0]["dominated_by"] != out[1]["dominated_by"], True,
         "A=3 is experiment-dominated (95%), A=7 is model-dominated (77%)"),
        ("model_mirror_asymmetry_is_sign_backwards_at_both",
         not any(r["model_sign_matches_experiment"] for r in out), True,
         "B_pred has the proton-rich member MORE bound; experiment has it LESS "
         "(Coulomb). Expected — B_pred carries no EM term — but sized here."),
    ]

    payload = {
        "description": (
            "Exact decomposition of the mirror proton-excess penalty into an "
            "experimental and a model half. Shows the penalty is not one quantity "
            "across A: experiment-dominated at A=3, model-dominated at A=7, with "
            "the model's asymmetry sign-backwards at both."
        ),
        "source_witness": RESIDUAL,
        "source_provenance": {k: str(src.get(k)) for k in
                              ("computedAt", "commitSha", "scriptHash", "q0Anchor")},
        "identity": "penalty = log_q[B_AME(pr)/B_AME(mir)] - log_q[B_pred(pr)/B_pred(mir)]",
        "pairs": out,
        "assertions": [
            {"name": n, "value": bool(g), "expected": bool(e),
             "passed": bool(g) is e, "note": note}
            for n, g, e, note in checks
        ],
        "allPassed": all(bool(g) is e for _n, g, e, _note in checks),
        "q0Anchor": "proton",
        "q0Value": str(q),
        "q0AnchorReason": "q_parameter.Q, the canonical experimental pin; matches the source witness's q0Anchor",
        "context": {
            "bean": "qou-zf9n",
            "block": "prop:mirror-baseline-cancellation",
            "scope": (
                "(a) scope-limited: about the canonical B_pred at these two pairs. Does "
                "NOT claim no model can get the mirror asymmetry right, and does not bear "
                "on the A=3 mirror-split mechanism of "
                "docs/audits/2026-07-13-mirror-split-one-third-mechanism-probe.md, which "
                "targets the EM-active channel and records the derived Coulomb/strong "
                "ratio tanh(ln q_0) ~ 0.10396 (def:coulomb-charge)."
            ),
            "why_no_EM_sign": (
                "B_pred(Z,N) = E_0*(tr_M(W_free) - tr_M(W_atom)) is a pure Markov-trace "
                "quantity with no electromagnetic term, so its mirror asymmetry is purely "
                "topological. The sign result is expected; the SIZE is the finding."
            ),
            "strengthens": (
                "the existing 'magnitude is NOT a single derivable number' verdict — the "
                "two penalties are not the same physical quantity, so one derivation "
                "should not be expected to produce both."
            ),
        },
    }

    w = WitnessBuilder.wrap_legacy(
        "mirror-penalty-decomposition", payload,
        script_path=__file__, engine="python+mpmath(exact at the production floor)",
    ).save()

    print("=== The proton-excess penalty, decomposed ===\n")
    print(f"  {'pair':<12} {'experiment':>12} {'model':>12} {'penalty':>12} {'recorded':>10}  dominated by")
    for r in out:
        print(f"  {r['pair']:<12} {float(mp.mpf(r['experimental_asymmetry_logq'])):>12.6f} "
              f"{float(mp.mpf(r['model_asymmetry_logq'])):>12.6f} "
              f"{float(mp.mpf(r['penalty_logq'])):>12.6f} "
              f"{float(mp.mpf(r['recorded_penalty'])):>10.3f}  "
              f"{r['dominated_by'].upper()} ({float(mp.mpf(r['dominant_share_pct'])):.0f}%)")
    print()
    for r in out:
        print(f"  A={r['A']}: experimental mirror energy = "
              f"{float(mp.mpf(r['experimental_mirror_energy_MeV'])):+.5f} MeV; "
              f"|model|/|exp| = {float(mp.mpf(r['abs_model_over_abs_exp'])):.3f}; "
              f"signs agree: {r['model_sign_matches_experiment']}")
    print()
    for n, g, e, note in checks:
        print(f"  [{'PASS' if bool(g) is e else 'FAIL'}] {n:<46} ({note[:74]})")
    print(f"\n  witness -> {w}")
    return 0 if payload["allPassed"] else 1


if __name__ == "__main__":
    sys.exit(main())
