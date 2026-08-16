#!/usr/bin/env python3
"""α via an archimedean Li_2^q convergent expansion — derive-or-bracket the
second-order flavor-split coefficient.

Context. The proton-neutron flavor split is `split = leading·(1 + α·leading)`
(second-order structure rigorously derived from the multiplicative quark-pair
factorization; see docs/audits/2026-06-29-flavor-split-partial-derivation.md).
The leading `flavor_split_leading = ℏ_q²·h_q·[2]_q/3` is PROVEN. The coefficient
α = (C_true−1)/leading = 0.92925 (C_true = CODATA/leading) is the single open
piece. It is anchor-stable (proton-q₀ vs muon-q₀ drift 5.8e-8) — a real O(1)
constant, not noise.

This probe writes α as a CONVERGENT archimedean expansion using the symmetric
q-dilogarithm Li_2^q(z) = Σ_{n≥1} z^n/(n·[n]_q) (the archimedean realization
functor's evaluator; _li_2_q_util.li_2_q) and evaluates principled self-energy
forms at BOTH anchors. Scope-(a): a measurement of which derivable form is
closest, NOT a fit of 0.929.

KEY RESULT. The geometric / q-dilog SELF-ENERGY form gives α = 1 (parameter-
free, convergent, 0.0097% vs CODATA — better than the deprecated posited
(1+ℏ_q³)'s 0.0305%). The q-deformation does NOT soften α=1 down to the
experimental 0.929: at the small argument leading≈0.00138, [n]_q ≈ n to ~0.1%,
so the q-geometric (α=1.0007) is indistinguishable from the classical
geometric (α=1.0014) — it cannot supply the 7.8% softening needed. So:
  • α = 1 (geometric self-energy) is the DERIVABLE archimedean prediction;
  • the residual 7.8% to the experimental 0.929 is NOT a q-dilog effect at the
    `leading` argument — it requires a separate O(1) structural ingredient
    (e.g. a dilog of an O(1) crossing argument z/h), which we deliberately do
    NOT fit (anti-flip-flop discipline).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: F401,E402

from mpmath import mp, mpf, log, e  # noqa: E402

mp.dps = 50

from _li_2_q_util import flavor_split_leading, li_2_q  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

CODATA = mpf("1.29333236") / ((mpf("938.27208816") + mpf("939.56542194")) / 2)


def _muon_q0() -> "mpf":
    """The documented muon anchor, imported — never retyped.

    The fallback here was `mpf("1.1099785955541810")` — a hand-typed copy of the
    value `q_muon_at()` derives, correct when written and with no way to stay
    correct. A duplicated constant in an `except` branch is the worst kind: it
    is silent, it fires only when the import is unavailable, and the substrate
    derives its value from Vol(4_1) and m_mu/m_e, so any refinement of either
    silently strands the copy. That has already happened once in this corpus,
    to the hand-typed `Q_MUON` constants (bean qou-khac).

    Raising beats guessing. If the substrate is not importable, this probe cannot
    know the anchor, and saying so is more useful than quietly answering with a
    pin that was retired.
    """
    try:
        from qou_substrate.constants import q_muon_at
        return mpf(str(q_muon_at()))
    except Exception as exc:  # noqa: BLE001 — re-raised with the reason
        raise RuntimeError(
            "muon q0 unavailable: qou_substrate.constants.q_muon_at could not be "
            "imported, and this probe will not substitute a hand-typed pin "
            "(qou-khac). Put tools/qou-substrate/python on PYTHONPATH."
        ) from exc


def _qint(n: int, q):
    return (q ** n - q ** (-n)) / (q - 1 / q)


def candidates(lead, q):
    """Principled archimedean correction factors C; full_split = lead·C."""
    return {
        "geometric_1_over_1_minus_lead": 1 / (1 - lead),
        "q_geom_sum_lead_n_over_qint_n": 1 + sum(lead ** n / _qint(n, q) for n in range(1, 60)),
        "li2q_lead_over_lead": li_2_q(lead, q) / lead,
        "neg_log_1_minus_lead_over_lead": (-log(1 - lead)) / lead,
        "exp_lead": e ** lead,
    }


def analyze(q, label):
    lead = flavor_split_leading(q)
    C_true = CODATA / lead
    a_true = (C_true - 1) / lead
    rows = {}
    for k, C in candidates(lead, q).items():
        a = (C - 1) / lead
        rows[k] = {
            "alpha": str(a),
            "alpha_rel_err_vs_true_pct": str((a - a_true) / a_true * 100),
            "full_split_rel_err_vs_codata_pct": str((lead * C - CODATA) / CODATA * 100),
        }
    return {"anchor": label, "q0": str(q), "leading": str(lead),
            "C_true": str(C_true), "alpha_true": str(a_true), "candidates": rows}


def main() -> int:
    qp = mpf(Q_50_DIGIT_STR)
    qm = _muon_q0()
    res_p = analyze(qp, "proton_q0")
    res_m = analyze(qm, "muon_q0")
    a_p = mpf(res_p["alpha_true"]); a_m = mpf(res_m["alpha_true"])

    print("α via archimedean Li_2^q convergent expansion")
    print("=" * 64)
    for res in (res_p, res_m):
        print(f"\n  [{res['anchor']}]  α_true = {mp.nstr(mpf(res['alpha_true']),10)}")
        for k, r in res["candidates"].items():
            print(f"    {k:34} α={mp.nstr(mpf(r['alpha']),9):>11}  "
                  f"split-err={mp.nstr(mpf(r['full_split_rel_err_vs_codata_pct']),3)}%")
    print(f"\n  α_true anchor drift (proton vs muon): {mp.nstr(abs(a_p - a_m),4)}")
    print("  VERDICT: geometric self-energy α=1 is the derivable archimedean")
    print("  form (0.0097% vs CODATA). q-dilog softening at argument `leading`")
    print("  (~0.1%) CANNOT explain the 7.8% gap to the experimental α=0.929.")
    print("  The residual needs a separate O(1) ingredient — NOT fitted here.")

    w = WitnessBuilder("flavor-split-alpha-dilog-expansion", engine="mpmath")
    w.set_description(
        "α (second-order flavor-split coefficient) via archimedean Li_2^q "
        "convergent expansions, both anchors. Geometric/q-dilog self-energy "
        "gives α=1 (0.0097%, parameter-free, convergent); the q-deformation at "
        "the small argument leading≈0.00138 is ~0.1% and CANNOT soften α=1 to "
        "the experimental α_true=0.929 (needs 7.8%). α=1 is the derivable "
        "prediction; the residual is a separate O(1) ingredient, NOT fitted."
    )
    w.add_data("codata_dmn_over_mn", str(CODATA))
    w.add_data("proton_anchor", res_p)
    w.add_data("muon_anchor", res_m)
    w.add_data("alpha_true_anchor_drift", str(abs(a_p - a_m)))
    w.add_assertion(
        name="geometric_self_energy_alpha_is_one_and_q_softening_too_small",
        computed=1 if (abs(mpf(res_p["candidates"]["geometric_1_over_1_minus_lead"]["alpha"]) - 1) < mpf("0.01")
                       and abs(mpf(res_p["candidates"]["q_geom_sum_lead_n_over_qint_n"]["alpha"])
                               - mpf(res_p["candidates"]["geometric_1_over_1_minus_lead"]["alpha"])) < mpf("1e-3")) else 0,
        expected=1,
        source="geometric self-energy α≈1; q-deformation moves α by < 1e-3 "
               "(too small for the 7.8% gap to experimental 0.929)",
    )
    w.save()
    print("\n  Witness: flavor-split-alpha-dilog-expansion.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
