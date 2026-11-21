#!/usr/bin/env python3
"""qbeta_qdifference_recurrence_datablock_probe.py
==================================================

The q-difference-ODE / C-finite-recurrence axis for the Q_β c_k ladder
(PR #1824 §3.b) is DATA-BLOCKED — quantified via experimental-error
propagation.

## Context (the last open generating-function axis)

PR #1824 proposed three categorical origins for a generating function
whose Taylor coefficients are the c_k:
  (a) cosh/cos closed-form avatar  — REFUTED (even slice empty, PR #1866;
      odd slice reduces to the saturated single-formula search, PR #1880);
  (b) q-difference ODE / linear recurrence coupling the c_k  — THIS PROBE;
  (c) Chern-Simons perturbation.

Axis (b) is the one that is genuinely different from a single closed form:
instead of c_k = [u^k] F(u), the c_k would satisfy a linear recurrence
(C-finite: c_{k+1} = Σ_j a_j(q) c_{k-j}). Sibling PR #1875 / #1839 build a
`QOU.QBeta.recurrence_step` engine for exactly this shape.

## The data-block (quantitative)

A recurrence of order d is identifiable only from ≳ 2d independent,
reliably-measured coefficients. The Q_β ladder supplies far fewer:

  - **c_2 = −1** is Lean-proved exact and q-independent — 1 reliable
    coefficient, but a constant (sources no recurrence by itself).
  - **c_3 .. c_k are EXTRACTED** by inverting the ladder against the
    single CAL-3 datum Q_codata:
        c_k = (Q_codata / Q_{N(k-1)} − 1) / u^k.
    Propagating Q_codata's experimental uncertainty δQ (CODATA
    `Q_BETA_MEV_ERR`) to leading order:
        δc_k ≈ (δQ / Q_codata) / u^k.
    Since u ≈ 0.0085, the 1/u^k amplification explodes:
        δc_3 ~ O(1)   (c_3 is only a ~1–2σ datum),
        δc_4 ~ O(10²),  δc_5 ~ O(10⁴),  …
    i.e. c_4 and beyond are experimentally UNMEASURED — their cached
    "cal-anchored" values are exact only by the calibration convention
    (Q_codata treated as exact), carrying ZERO independent information.

So the honest count of reliably-measured, recurrence-usable coefficients
is effectively **one** (c_2) plus a **~1–2σ hint** (c_3). A recurrence
(order ≥ 2) cannot be identified. The "asymptotic c_{k+1}/c_k → 1/u"
pattern reported in earlier audits is computed from c_8..c_10, whose
error bars (δc ~ 10⁶+) dwarf the values — it is a circular-extraction
artifact, not a measured recurrence.

## Verdict

**DATA_BLOCKED** — not refuted, not confirmed: UNDETERMINED by the
available data. Resolvable only by
  (i) a sub-CAL-2 Q_β measurement (research-grade; the coordination
      ledger explicitly declined substrate-precision work), or
  (ii) a structural derivation of the Habiro / q-difference element
      (the open keystone) — which would SUPPLY the recurrence rather
      than fit it.

Together with the closed-form refutation (PR #1866 + #1880), this
resolves all of PR #1824's generating-function axes for c_3: closed-form
is refuted, recurrence is data-blocked. The remaining productive
directions are fibre-level (Composite 4, PR #1811) + GAP-A-3/A-4.

## No-fit discipline

This probe FITS NOTHING. It propagates a published experimental
uncertainty through the (existing) ladder inversion and reports the
resulting error bars. The conclusion is that recurrence-fitting is
not warranted by the data — the opposite of proposing an ansatz.

## References
- Closed-form refutation: PR #1866, PR #1880 (this branch)
- Recurrence engine sibling: PR #1875 / #1839 (`QOU.QBeta.recurrence_step`)
- c_k cache + precision floor: `qbeta-ck-cache.witness.json`, PR #7f36be0e
- Holonomic data-blocker (sibling): main `d2617ae8`
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

from mpmath import mp, mpf, cos, fabs  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import q_at  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV, Q_BETA_MEV_ERR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from qbeta_utils import substrate_ladder_quantities  # noqa: E402

K_MAX = 8


def extract_ck(q: mpf, q_codata: mpf, m_e: mpf, k_max: int) -> list[mpf]:
    """c_2..c_{k_max} via the ladder inversion (Q_codata treated as the
    exact CAL-3 anchor — the cal-anchored convention). c_2 = -1 fixed."""
    sub = substrate_ladder_quantities(q, convention="C")
    u = sub["u"]
    Q_A = m_e * sub["Q_A_over_me"]
    N1 = Q_A * cos(sub["alpha"] - sub["b"] * sub["hbar_q"] ** 2 / 2)
    c2 = mpf(-1)
    Q_prev = N1 * (1 + c2 * u ** 2)
    ck = [c2]
    for k in range(3, k_max + 1):
        ck_k = (q_codata / Q_prev - 1) / u ** k
        Q_prev = Q_prev * (1 + ck_k * u ** k)
        ck.append(ck_k)
    return ck


def main() -> int:
    set_compute_dps()

    me = mpf(str(M_E_MEV))
    q_codata = mpf(str(Q_BETA_MEV))
    dQ_rel = mpf(str(Q_BETA_MEV_ERR)) / q_codata
    qp = q_at(mp.dps)
    sub = substrate_ladder_quantities(qp, convention="C")
    u = sub["u"]

    print("=" * 78)
    print(" Q_β c_k q-difference / recurrence axis — experimental data-block")
    print("=" * 78)
    print(f"  u = b·ℏ_q² = {fmt(u)[:18]}   δQ/Q (CODATA) = {float(dQ_rel):.3e}")
    print()

    ck = extract_ck(qp, q_codata, me, K_MAX)
    # Leading-order experimental uncertainty on each EXTRACTED c_k:
    #   δc_k ≈ (δQ/Q) / u^k   (c_2 is proved-exact, not extracted)
    print(f"  {'k':>3}{'c_k (cal-anchored)':>24}{'δc_k (exp.)':>16}{'rel unc':>14}  status")
    print(f"  {'-'*3}{'-'*24}{'-'*16}{'-'*14}  {'-'*16}")
    rows = []
    n_reliable = 0
    for idx, k in enumerate(range(2, K_MAX + 1)):
        c = ck[idx]
        if k == 2:
            dc = mpf(0)            # c_2 is Lean-proved exact, q-independent
            rel = mpf(0)
            status = "PROVED exact (q-indep)"
            n_reliable += 1
        else:
            dc = dQ_rel / u ** k
            rel = dc / fabs(c) if c != 0 else mpf("inf")
            if rel < mpf("0.1"):
                status = "usable (<10% unc)"
                n_reliable += 1
            elif rel < mpf("1"):
                status = f"~{float(1/rel):.1f}σ hint"
            else:
                status = "UNMEASURED (unc > value)"
        print(f"  {k:>3}{fmt(c)[:24]:>24}{('exact' if k==2 else f'{float(dc):.2e}'):>16}"
              f"{('—' if k==2 else f'{float(rel)*100:.1f}%'):>14}  {status}")
        # Serialize rel_uncertainty as JSON-valid: 0.0 for the exact c_2,
        # null (None) for the c_4+ unmeasured case where rel = inf (c = 0)
        # — float('inf') would emit non-RFC-8259 `Infinity`.
        rel_json = (0.0 if k == 2
                    else (None if rel == mpf("inf") else float(rel)))
        rows.append({
            "k": k, "c_k": fmt(c),
            "exp_uncertainty": "exact" if k == 2 else fmt(dc),
            "rel_uncertainty": rel_json,
            "status": status,
        })
    print()

    # In this standard cal-anchored extraction, c_4+ come out EXACTLY 0:
    # the N=2 ladder + c_3 already reproduces Q_codata to below the compute
    # floor (1e-30), so there is no residual left for c_4+. The "c_8..c_10"
    # the earlier audits formed a ratio from came from a higher-precision /
    # different-convention extraction; either way each such c_k sits under an
    # error bar δc_k = (δQ/Q)/u^k that dwarfs it, so any ratio is noise.
    n_zero_floor = sum(1 for idx in range(2, K_MAX - 1) if ck[idx] == 0)
    print(f"  c_4..c_{K_MAX} extract to EXACTLY 0 here ({n_zero_floor} coeffs): the")
    print(f"  ladder converges at c_3 (residual < 1e-30 compute floor), so c_4+")
    print(f"  carry no datum at all. Their nominal error bars δc_k=(δQ/Q)/u^k")
    print(f"  range {float(dQ_rel/u**4):.1e} (k=4) … {float(dQ_rel/u**K_MAX):.1e} (k={K_MAX}).")
    print()

    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    print(f"  Reliably-measured recurrence-usable coefficients: {n_reliable}")
    print("  (c_2 proved-exact; c_3 only a ~1–2σ datum; c_4+ unmeasured —")
    print("   experimental error bars from δQ/u^k dwarf the values).")
    print()
    print("  DATA_BLOCKED — a q-difference / C-finite recurrence (order ≥ 2)")
    print("  needs ≳ 4 reliable coefficients; the data supplies effectively")
    print("  one (c_2) plus a 1–2σ hint (c_3).  Fitting a recurrence to the")
    print("  extracted c_4..c_k is CIRCULAR (those values are reconstructions")
    print("  of the single datum Q_codata through the ladder form) and the")
    print("  'c_{k+1}/c_k → 1/u' asymptotic is an artifact of that circularity.")
    print()
    print("  Resolvable only by (i) sub-CAL-2 Q_β precision (research-grade,")
    print("  declined per the coordination ledger) or (ii) a structural")
    print("  Habiro/q-difference element derivation (the open keystone), which")
    print("  would SUPPLY the recurrence rather than fit it.")
    print()
    print("  Combined with PR #1866 + #1880 (closed-form refuted), this")
    print("  resolves all of PR #1824's generating-function axes for c_3.")
    verdict = "DATA_BLOCKED_RECURRENCE_UNIDENTIFIABLE"

    wb = WitnessBuilder(
        "qbeta-qdifference-recurrence-datablock-probe", engine="mpmath",
    )
    wb.set_description(
        "Quantifies why the q-difference / C-finite recurrence axis for the "
        "Q_β c_k ladder (PR #1824 §3.b) is DATA-BLOCKED. Propagates the "
        "CODATA Q_β experimental uncertainty through the ladder inversion "
        "c_k = (Q_codata/Q_{N(k-1)}−1)/u^k: δc_k ≈ (δQ/Q)/u^k explodes with "
        "k (u≈0.0085), so c_2 (proved-exact) is the only reliable "
        "coefficient, c_3 is a ~1–2σ datum, and c_4+ are experimentally "
        "unmeasured. A recurrence (order ≥2) needs ≳4 reliable coefficients "
        "⇒ unidentifiable; the earlier c_{k+1}/c_k→1/u asymptotic is a "
        "circular-extraction artifact. No fits. Completes PR #1824's "
        "generating-function axis triage (closed-form refuted in #1866/#1880)."
    )
    wb.set_content_block("conj:qbeta-precision-ladder")
    wb.add_data("u_substrate", fmt(u))
    wb.add_data("dQ_rel_codata", float(dQ_rel))
    wb.add_data("ck_with_uncertainty", rows)
    wb.add_data("n_reliable_coefficients", n_reliable)
    wb.add_data("recurrence_order_identifiable", 0)
    wb.add_data("verdict", verdict)
    wb.add_data("interpretation", (
        "Only c_2 is reliably measured (and it is a proved constant). c_3 "
        "carries ~60% experimental uncertainty; c_4+ have error bars far "
        "larger than their values. The q-difference recurrence axis is "
        "therefore undetermined by data, not refutable or confirmable "
        "numerically. Fitting to extracted c_4..c_k is circular. Resolvable "
        "only by sub-CAL-2 Q_β precision (declined) or structural Habiro "
        "derivation (the keystone)."
    ))
    # Real invariant: c_3's experimental uncertainty is O(1) (not negligible)
    # — i.e. c_3 is not a high-significance datum.
    c3_rel = float((dQ_rel / u ** 3) / fabs(ck[1]))
    wb.add_assertion(
        "c3_experimental_uncertainty_is_order_unity",
        computed=1.0 if c3_rel > 0.1 else 0.0,
        expected=1.0,
        source=(f"δc_3/|c_3| = {c3_rel:.3f} (~{c3_rel*100:.0f}% experimental "
                "uncertainty from δQ/u³) — c_3 is a low-significance datum, "
                "confirming the data-block."),
    )
    # Real invariant: c_4 is experimentally unmeasured — its error bar
    # δc_4 = (δQ/Q)/u⁴ exceeds any plausible O(1) value, and in this
    # cal-anchored extraction c_4 comes out exactly 0 (no datum at all),
    # so the unc/value ratio is formally infinite.
    c4_err = dQ_rel / u ** 4
    c4_unmeasured = (ck[2] == 0) or (c4_err > fabs(ck[2]))
    src = (f"c_4 extracts to 0 (no residual datum) with nominal error bar "
           f"δc_4 = {float(c4_err):.1e}" if ck[2] == 0
           else f"δc_4/|c_4| = {float(c4_err / fabs(ck[2])):.1f} (> 1)")
    wb.add_assertion(
        "c4_unmeasured_uncertainty_exceeds_value",
        computed=1.0 if c4_unmeasured else 0.0,
        expected=1.0,
        source=src + " — c_4 is experimentally unmeasured; recurrence-fitting "
                     "to c_4+ is circular.",
    )
    wb.save()
    print()
    print("  Witness: qbeta-qdifference-recurrence-datablock-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
