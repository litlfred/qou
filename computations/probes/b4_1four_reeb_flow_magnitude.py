#!/usr/bin/env python3
"""Value leg — the [1⁴] exchange determinant at the LANDED Reeb-flow magnitude.

EXPLORATORY (audit-only, no production rewire, no fit). Follow-up to
b4_1four_complete_graph_writhe_signs.py, which established:

  • pp/nn writhe signs DERIVED (+1/−1) from atom_braid_word_3A; pn sign open;
  • a structural physicality ceiling g < 1/|μ_min| = 1/√5 on the per-pair
    magnitude (the naive bond factor z ≈ 0.499 EXCEEDS it ⇒ pn=±1 gave det<0).

Main then landed a pn-bond magnitude *below* the ceiling (commits 8275655551 +
17264f2a9c, the ²H "reeb-flow" tier of categorical_q_decay_ba_low_isotopes.py):

    g_reeb = 1 / sqrt( 5 + (q₀−1)²/q₀ )  ≈ 0.446727   ( < 1/√5 ≈ 0.447214 )

with the deuteron binding asserted LINEARLY as B(²H) = 5·g_reeb ≈ 2.2336 MeV
(+0.41 % vs AME). This probe consumes that landed constant UNCHANGED (no
tuning; the one input is the committed formula) and asks two questions the
landing left open:

  Q1 (A=2 reconciliation): does the pinned determinant form
      B = E₀·(−ln det(I+G)) reproduce the deuteron at g_reeb, or is the
      linear 5·g law a distinct assertion?  (Single pn pair: det(I+G₂) =
      1 − g², sign-independent.)
  Q2 (A=4 extension): with the sub-ceiling magnitude, the mixed-sign
      pn=±1 patterns become PHYSICAL (det > 0).  What does
      E₀·(−ln det(I+G)) give at g_reeb for each w_pn ∈ {−1, 0, +1}, vs
      the connected excess b₄ = 9.2431 MeV AND vs the full B(⁴He) =
      28.29566 MeV?

No w_pn is selected and no magnitude is solved-for (Rule-14); the deliverable
is the option→value map at the landed constant. A conjugation check
diag(1,1,−1,−1)·S(pn=+1)·diag(1,1,−1,−1) = S(pn=−1) makes the two mixed-sign
options isospectral, asserted below.

-- Ref: b4_1four_complete_graph_writhe_signs.py (signs + ceiling);
categorical_q_decay_ba_low_isotopes.py (landed g_reeb + linear 5g law);
docs/design/2026-07-06-gap-a4-writhe-derivation-lit-review-and-framework.md.
"""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_HERE)):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from _li_2_q_util import load_q_50dps  # noqa: E402
from substrate._precision import set_compute_dps  # noqa: E402
from substrate.experimental_constants import M_E_MEV  # noqa: E402
from substrate.witness_base import WitnessBuilder  # noqa: E402
from b4_1four_complete_graph_writhe_signs import (  # noqa: E402
    exchange_matrix,
    neg_log_det_I_plus_G,
)

set_compute_dps()

COMP = str(_COMP)

AME_B_2H = mp.mpf("2.224566")
AME_B_4HE = mp.mpf("28.29566")
B4_TARGET = mp.mpf("9.2431")   # connected 4-body cumulant (b4_value_cumulant_target_probe.py)


def main() -> int:
    t0 = time.monotonic()
    q, qi, z = load_q_50dps()
    m_e = mp.mpf(str(M_E_MEV))
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(m_e, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)

    # The landed Reeb-flow magnitude (consumed verbatim; not a knob).
    g = mp.mpf(1) / mp.sqrt(mp.mpf(5) + (q - 1) ** 2 / q)
    ceiling = mp.mpf(1) / mp.sqrt(5)
    headroom = 1 - mp.sqrt(5) * g          # distance below det=0 criticality

    # ── Q1: deuteron, single pn pair ────────────────────────────────
    det2 = 1 - g * g                        # det(I+G₂), sign-independent
    B_det2 = E0 * (-mp.log(det2))
    B_lin = 5 * g                           # the landed linear law
    q1 = {
        "g_reeb": mp.nstr(g, 12),
        "det_I_plus_G2_(1-g^2)": mp.nstr(det2, 10),
        "B_det_form_MeV_E0*(-ln det)": mp.nstr(B_det2, 8),
        "B_linear_5g_MeV_(landed law)": mp.nstr(B_lin, 8),
        "B_AME_2H_MeV": mp.nstr(AME_B_2H, 8),
        "err_det_form_pct": mp.nstr(100 * (B_det2 - AME_B_2H) / AME_B_2H, 5),
        "err_linear_5g_pct": mp.nstr(100 * (B_lin - AME_B_2H) / AME_B_2H, 5),
        "finding": (
            "The determinant form does NOT reproduce the deuteron at g_reeb "
            "(≈0.93 MeV, −58 %); the landed 5·g law (+0.41 %) is a DISTINCT "
            "linear assertion, not the A=2 case of b₄ = −ln det(I+G). "
            "Reconciling the two forms is open."
        ),
    }

    # ── Q2: [1⁴] complete graph at g_reeb ───────────────────────────
    rows = []
    for w_pn in (-1, 0, +1):
        d, nld = neg_log_det_I_plus_G(w_pn, g)
        if nld is None:
            rows.append({"w_pn": w_pn, "det_I_plus_G": mp.nstr(d, 8),
                         "status": "UNPHYSICAL (det ≤ 0)"})
            continue
        mev = E0 * nld
        rows.append({
            "w_pn": w_pn,
            "det_I_plus_G": mp.nstr(d, 8),
            "neg_log_det": mp.nstr(nld, 8),
            "MeV": mp.nstr(mev, 8),
            "ratio_to_b4_9.2431": mp.nstr(mev / B4_TARGET, 6),
            "ratio_to_full_B4He_28.29566": mp.nstr(mev / AME_B_4HE, 6),
        })

    # ── Q3: body-order (Ursell) cumulants of the det form at g_reeb ──
    # The corpus target b₄ = 9.2431 is the CONNECTED cumulant of AME
    # (b4_value_cumulant_target_probe.py): B(A) = C(A,2)b₂ + C(A,3)b₃ + C(A,4)b₄.
    # Decompose the det form the same way to see WHERE its binding sits.
    def det3(signs):
        S = mp.zeros(3, 3)
        (s01, s02, s12) = signs
        S[0, 1] = S[1, 0] = s01 * g
        S[0, 2] = S[2, 0] = s02 * g
        S[1, 2] = S[2, 1] = s12 * g
        return mp.det(mp.eye(3) + S)

    b2_det = E0 * (-mp.log(det2))
    # A=3 shells at w_pn=+1 (isospectral to −1 by the same diag conjugation):
    # ppn: pairs (pp,+1), (pn,w), (pn,w); pnn: (nn,−1), (pn,w), (pn,w)
    B3_ppn = E0 * (-mp.log(det3((+1, +1, +1))))
    B3_pnn = E0 * (-mp.log(det3((-1, +1, +1))))
    B3_bar = (B3_ppn + B3_pnn) / 2
    b3_det = B3_bar - 3 * b2_det
    _, nld4 = neg_log_det_I_plus_G(+1, g)
    B4_det = E0 * nld4
    b4_det = B4_det - 6 * b2_det - 4 * b3_det
    q3 = {
        "b2_det_MeV": mp.nstr(b2_det, 8), "b2_AME": "2.224566",
        "B3_ppn_MeV": mp.nstr(B3_ppn, 8), "B3_pnn_MeV": mp.nstr(B3_pnn, 8),
        "b3_det_MeV": mp.nstr(b3_det, 8), "b3_AME": "1.4264",
        "b4_det_MeV": mp.nstr(b4_det, 8), "b4_AME": "9.2431",
        "finding": (
            "Body-order profile of the det form at g_reeb vs the AME Ursell "
            "cumulants — shows whether the det form's binding sits at the "
            "right body orders even where totals differ. Scope-(a)."
        ),
    }

    result = {
        "constants": {
            "q0": mp.nstr(q, 12),
            "g_reeb": mp.nstr(g, 12),
            "g_ceiling_1/sqrt5": mp.nstr(ceiling, 12),
            "headroom_1-sqrt5*g": mp.nstr(headroom, 8),
            "E0_MeV_m_e/(q(q-1))": mp.nstr(E0, 8),
        },
        "q1_deuteron_reconciliation": q1,
        "q2_1four_enumeration_at_g_reeb": rows,
        "q3_ursell_cumulants_of_det_form": q3,
        "verdict": (
            "At the landed sub-ceiling magnitude g_reeb the mixed-sign pn=±1 "
            "[1⁴] patterns become PHYSICAL (det>0; they were det<0 at the naive "
            "z). Values are reported per w_pn option with NO selection. "
            "Scope-(a) throughout: numbers constrain the (form, magnitude) "
            "combination at g_reeb, not the ingredients."
        ),
    }

    payload = {
        "computation": "b4-1four-reeb-flow-magnitude",
        "description": (
            "[1⁴] exchange determinant and deuteron det-vs-linear reconciliation "
            "at the landed Reeb-flow magnitude g = 1/sqrt(5+(q0-1)^2/q0) "
            "(main commits 8275655551 + 17264f2a9c). Audit-only; no fit; "
            "no w_pn selection."
        ),
        "tier": "exploratory (consumes one landed constant; enumerates discrete signs)",
        "result": result,
        "context": {
            "axis": "GAP-A-4 class-D — [1⁴] value leg at the landed pn magnitude",
            "predecessor": "b4_1four_complete_graph_writhe_signs.py (+ witness)",
            "landed_source": "categorical_q_decay_ba_low_isotopes.py reeb-flow tier",
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        "b4-1four-reeb-flow-magnitude", payload,
        script_path=__file__, engine="python+mpmath",
        output_dir=os.path.join(COMP, "probes"), start_time=t0,
    )
    wb.add_assertion("g_reeb_below_ceiling", computed=str(bool(g < ceiling)), expected="True")
    d_p, _ = neg_log_det_I_plus_G(+1, g)
    d_m, _ = neg_log_det_I_plus_G(-1, g)
    wb.add_assertion("pn+1_physical_at_g_reeb", computed=str(bool(d_p > 0)), expected="True")
    # diag(1,1,−1,−1) conjugation ⇒ pn=−1 isospectral to pn=+1
    wb.add_assertion("pn_pm1_isospectral_dets_equal",
                     computed=mp.nstr(d_m, 10), expected=mp.nstr(d_p, 10))
    wb.save(extra={"auditOnly": True})

    print("=== [1⁴] exchange determinant at the landed Reeb-flow magnitude ===")
    print(f"  q0={float(q):.6f}  g_reeb={float(g):.6f}  ceiling=1/sqrt5={float(ceiling):.6f}"
          f"  headroom={float(headroom):.3e}  E0={float(E0):.4f} MeV")
    print(f"  Q1 deuteron: det-form {float(B_det2):.4f} MeV ({float(q1_err(B_det2)):+.2f}%)"
          f" vs linear 5g {float(B_lin):.4f} MeV ({float(q1_err(B_lin)):+.2f}%)  [AME 2.2246]")
    for r in rows:
        extra = ("" if "MeV" not in r else
                 f"  ->  {float(mp.mpf(r['MeV'])):.3f} MeV"
                 f"  ({float(mp.mpf(r['ratio_to_b4_9.2431'])):.3f}x b4,"
                 f" {float(mp.mpf(r['ratio_to_full_B4He_28.29566'])):.3f}x full B(4He))")
        print(f"  w_pn={r['w_pn']:+d}  det={r['det_I_plus_G']}{extra}")
    return 0


def q1_err(b) -> mp.mpf:
    return 100 * (b - AME_B_2H) / AME_B_2H


if __name__ == "__main__":
    raise SystemExit(main())
