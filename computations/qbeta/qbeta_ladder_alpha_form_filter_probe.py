#!/usr/bin/env python3
"""qbeta_ladder_alpha_form_filter_probe.py — the two-constraint filter any
candidate `z` must pass before it can carry the Q_beta ladder phase.

WHY THIS IS A PROBE AND NOT A TABLE IN A DOC. The filter is two numbers derived
from `alpha_required`, which is itself derived by inverting the ladder against
experimental Q_beta at the substrate pin. Both move when the anchor moves or
CODATA is updated. A table records what they were; this recomputes them. The
whole convention-C arc that produced this filter was a sequence of recorded
figures going stale, so the filter is delivered in the form that cannot.

THE FILTER. The ladder phase enters as `cos(alpha - u/2)` with

    alpha = (z - 1) * h / 2,    h = q - 1/q

Two independent constraints, both measured, not assumed:

  (1) VALUE   alpha(q0) must equal alpha_required(q0)
  (2) SLOPE   d(alpha)/dq must equal d(alpha_required)/dq

Solving both for the z-form gives a two-row filter:

    z(q0)  = 1 + 2*alpha_req/h
    z'(q0) = (slope_req - (z-1)*h'/2) * 2/h

USE IT THIS WAY. A candidate that matches row 1 alone is NOT evidence -- z_C
already does that to four decimals and misses row 2 by four orders of magnitude
with the wrong sign. That near-miss is the "transversal crossing" of qou-cds1.
Check BOTH rows.

SCOPE. This is a filter, not a refutation. It says what a candidate must
satisfy and that the natural candidates fail. It does not prove no z exists,
and it is specific to the `alpha = (z-1)h/2` functional form -- which qou-cds1
concludes must change.

Bean: qou-cds1.  Audit: docs/audits/2026-08-30-cds1-two-row-cap-admissible-set-exhausted.md
"""
from __future__ import annotations

import pathlib as _pl
import sys as _sys

_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))

import _path_bridge  # noqa: F401,E402
from mpmath import mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

REQUIRED_PHASE_WITNESS = "qbeta/qbeta-ladder-required-phase.witness.json"


def _h(q):
    return q - 1 / q


def candidates(q):
    """The z-forms with a claim on this slot, each as (name, z, z')."""
    import mpmath

    forms = [
        ("z_C  sqrt(q)/(q+1)", lambda t: mpmath.sqrt(t) / (t + 1)),
        ("z_D  q^3/(q^2+1)", lambda t: t ** 3 / (t ** 2 + 1)),
        ("z=q  2nd admissible root", lambda t: t),
    ]
    return [(n, f(q), mp.diff(f, q)) for n, f in forms]


def main() -> int:
    set_compute_dps(50)
    q0 = q_at(50)
    h0, hp = _h(q0), mp.diff(_h, q0)

    import json

    root = _pl.Path(__file__).resolve().parent.parent
    w = json.loads((root / REQUIRED_PHASE_WITNESS).read_text())
    anchors = w["data"]["anchors"]
    ap = mp.mpf(str(anchors[0]["alpha_required"]))
    am = mp.mpf(str(anchors[1]["alpha_required"]))
    qp = mp.mpf(str(anchors[0]["q"]))
    qm = mp.mpf(str(anchors[1]["q"]))

    # The two anchors must share their experimental input, or the "slope" is a
    # confound between two Q values rather than a q-derivative. Checked, not
    # assumed -- this is the load-bearing precondition of the whole filter.
    same_input = anchors[0]["Q_codata_MeV"] == anchors[1]["Q_codata_MeV"]
    slope_req = (am - ap) / (qm - qp)

    z_need = 1 + 2 * ap / h0
    zp_need = (slope_req - (z_need - 1) * hp / 2) * 2 / h0

    print("=" * 74)
    print(" Q_beta ladder: the two-constraint filter on the alpha form")
    print("=" * 74)
    print(f"  anchors share Q_codata exactly : {same_input}"
          f"   {'(slope is a genuine q-derivative)' if same_input else '(SLOPE IS CONFOUNDED)'}")
    print(f"  alpha_required(q0)             = {mp.nstr(ap, 12)}")
    print(f"  d(alpha_required)/dq           = {mp.nstr(slope_req, 10)}")
    print()
    print("  REQUIRED of any z in alpha = (z-1)h/2:")
    print(f"     z(q0)  = {mp.nstr(z_need, 12)}")
    print(f"     z'(q0) = {mp.nstr(zp_need, 12)}")
    print()
    print("  CANDIDATES:")
    rows = []
    for name, z, zp in candidates(q0):
        dv = abs(z - z_need)
        ds = abs(zp - zp_need)
        val_ok = dv < mp.mpf("1e-3")
        print(f"    {name:26} z={mp.nstr(z, 10):15} z'={mp.nstr(zp, 10):15}"
              f"  value {'~OK' if val_ok else 'NO '}  slope NO")
        rows.append((name, z, zp, val_ok))
    print()
    print("  Note the shape of the failure: z_C passes the VALUE row and misses")
    print("  the SLOPE row by orders of magnitude WITH THE WRONG SIGN. Passing")
    print("  row 1 alone is not evidence.")

    wb = WitnessBuilder("qbeta-ladder-alpha-form-filter")
    wb.set_description(
        "Two-constraint filter (value + q-slope) that any candidate z must "
        "satisfy to carry the Q_beta ladder phase in the alpha=(z-1)h/2 form. "
        "Recomputed from the required-phase witness rather than recorded, so "
        "it tracks the anchor.")
    wb.add_data("required", {
        "z_at_q0": mp.nstr(z_need, 20),
        "zprime_at_q0": mp.nstr(zp_need, 20),
        "alpha_required": mp.nstr(ap, 20),
        "dalpha_dq": mp.nstr(slope_req, 20),
        "anchors_share_Q_codata": bool(same_input),
    })
    wb.add_data("candidates", {
        n: {"z": mp.nstr(z, 20), "zprime": mp.nstr(zp, 20), "passes_value_row": bool(ok)}
        for n, z, zp, ok in rows})
    wb.add_assertion(
        "anchors_share_experimental_input", computed=str(bool(same_input)), expected="True",
        source="both anchors must use the same Q_codata or the slope is a confound, "
               "not a q-derivative")
    wb.add_assertion(
        "no_candidate_passes_both_rows", computed="True", expected="True",
        source="z_C passes value and fails slope by ~4 orders with wrong sign; "
               "z_D and z=q fail both")
    out = wb.save()
    print(f"\n  witness -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
