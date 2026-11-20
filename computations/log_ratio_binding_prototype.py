#!/usr/bin/env python3
"""Prototype: extensive binding on the LOG-RATIO of the Markov trace.

EXPLORATORY (no production rewire). Owner directive 2026-06-10, next-step 1+2:
prototype `B ∝ E_0·log(tr_free/tr_atom)` and test the bond topology (A−1 chain
vs C(A,2) all-pairs).

## Motivation (from the GS-filtration finding)

`gs_filtration_binding_components.py` showed the bonds suppress the Markov
trace MULTIPLICATIVELY: `tr_atom ≈ tr_free · f^{bonds}`, f ≈ 0.39. So the
canonical-binding LINEAR difference `Δtr = tr_free·(1 − f^{bonds})` SATURATES
(intensive, bounded), which is why `B = Q_β·Δtr` undershoots by 5–40× and the
undershoot grows with A. The EXTENSIVE invariant is the log-ratio:

    L(K) ≡ log(tr_M(W_free) / tr_M(W_atom)) = bonds · |log f|

This probe evaluates the **log-ratio binding** at the canonical energy scale
`E_0 = m_e/(q_0(q_0−1)) ≈ 4.186 MeV` (NOT Q_β — see the energy-scale finding):

    B_logratio(K) = E_0 · L(K)

and compares to B_AME, against the linear `B = Q_β·Δtr` baseline. It also
reports the per-bond energy under the A−1 (chain, as-wired) and C(A,2)
(all-pairs, physical) bond counts, to scope next-step 2 (bond topology).

## Honest expectation

This is a STRUCTURAL form test, NOT a Δ_λ closure. The per-bond |log f| is not
universal (varies with p/n composition; ⁴He is alpha-magic), so B_logratio will
NOT hit B_AME exactly. The claim under test is only that the log-ratio form is
within O(1–2×) — a qualitative leap over the linear form's 5–40×, confirming
the functional-form diagnosis. No 7th ansatz.

## 🛑 The `within 3×` assertion now FAILS, and the bound is not being widened

Re-running this producer after the NO-FLOAT64 fix below also refreshed a witness
that was **68 days stale** — committed 2026-06-15 against an upstream
`binding-canonical.witness.json` last regenerated 2026-08-22. Refreshing it:

* corrected the nucleon traces (D `tr_free` 0.98353 → 1.13172, ⁴He 0.96732 →
  1.28078), and
* added three nuclei the old run never saw (⁶Li, ⁷Li, ⁷Be).

The headline `max(miss, 1/miss)` moves **2.363 → 3.2592**, so the assertion's
own `within 3×` bound is violated at ⁴He. The bound is left as it is: widening it
is the forbidden move, and here it would hide a real change in what the corpus
claims. The failure is the corrected upstream data speaking, not a regression
introduced by the precision fix — verified by diffing the old and new rows.

The qualitative conclusion in the verdict string is unaffected: the log-ratio
form still collapses a 5.1–35.5× undershoot to 0.79–3.26×, and the all-pairs
estimate to 0.61–1.63×. It is the *quantitative* `3×` claim that no longer holds.

Output: log-ratio-binding-prototype.witness.json
"""
from __future__ import annotations

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# NO-FLOAT64 (bean qou-ywie).  This producer computed the log-ratio binding
# entirely in float64: it imported the FLOAT `q_parameter.Q`, downcast m_e and
# Q_beta with float(), parsed the upstream 50-digit traces with float(), and
# took math.log of their ratio.  It is the corpus's log-ratio channel -- one of
# only two extensive candidates (bean qou-ge9f) -- and its binding is an
# accumulation over A-1 bonds, which is exactly what float64 degrades.  Same
# defect and same fix as derived_bond_graph_binding (#6338, bean qou-vsqh).
set_compute_dps()

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []


def _energy_scales():
    # Read the 50-DIGIT q0 string, not `q_parameter.Q`, which is a Python float
    # (measured: 1.1099785827513808, 17 digits) -- `mp.mpf(str(Q))` would
    # preserve float64 faithfully and create no precision that is not there.
    from q_parameter import Q_50_DIGIT_STR
    from experimental_constants import Q_NEUTRON_MEV as Qb
    try:
        from codata_constants import M_E_MEV as me
    except Exception:
        me = "0.51099895"  # noqa: P31 — except-fallback; primary path imports codata_constants.M_E_MEV
    q0 = mp.mpf(Q_50_DIGIT_STR)
    me = me if isinstance(me, mp.mpf) else mp.mpf(str(me))
    Qb = Qb if isinstance(Qb, mp.mpf) else mp.mpf(str(Qb))
    return me, Qb, _qbeta_e0.order_zero_scaled(me, q0)


def main() -> int:
    t0 = time.time()
    me, Qb, E0 = _energy_scales()

    bc = record_upstream(HERE / "binding-canonical.witness.json", _UPSTREAM_RECORDS)
    res = [r for r in bc["data"]["results"] if r.get("status") == "solved"]

    rows = []
    raw_rows = []          # the mpf values, for statistics and display
    for r in res:
        Z, N, A = r["Z"], r["N"], r["A"]
        # The upstream witness records these to 50 digits; float() was throwing
        # 33 of them away before the log was taken.
        ta = mp.mpf(r["tr_M_atom"].strip("()").split("+")[0])
        tf = mp.mpf(r["tr_M_free"].strip("()").split("+")[0])
        B_ame = mp.mpf(str(r["B_AME_MeV"]))
        B_lin = mp.mpf(str(r["B_MeV"]))               # = Q_β·Δtr (baseline)
        L = mp.log(tf / ta)                            # log-ratio (extensive)
        B_log = E0 * L                                 # log-ratio binding @ E_0
        chain = A - 1                                  # bonds as wired (chain)
        allpairs = A * (A - 1) // 2                    # physical bonds C(A,2)
        miss_lin = B_ame / B_lin
        miss_log = B_ame / B_log
        B_ap = E0 * L * allpairs / chain if chain else None
        miss_ap = B_ame / B_ap if chain else None
        rows.append({
            "atom": r["atom"], "Z": Z, "N": N, "A": A,
            "B_AME_MeV": fmt(B_ame),
            "tr_atom": fmt(ta), "tr_free": fmt(tf),
            "log_ratio_L": fmt(L),
            # linear baseline
            "B_linear_Qbeta": fmt(B_lin),
            "miss_linear_x": fmt(miss_lin),
            # log-ratio form at E_0
            "B_logratio_E0": fmt(B_log),
            "miss_logratio_x": fmt(miss_log),
            # per-bond energy under the two topologies
            "bonds_chain_Am1": chain,
            "bonds_allpairs_C_A_2": allpairs,
            "L_per_bond_chain": fmt(L / chain) if chain else None,
            "Bame_per_bond_chain_MeV": fmt(B_ame / chain) if chain else None,
            "Bame_per_bond_allpairs_MeV": fmt(B_ame / allpairs) if allpairs else None,
            # all-pairs log-ratio estimate: scale L by C(A,2)/(A-1)
            "B_logratio_E0_allpairs_est": fmt(B_ap) if chain else None,
            "miss_logratio_allpairs_x": fmt(miss_ap) if chain else None,
        })
        raw_rows.append({"atom": r["atom"], "A": A, "B_ame": B_ame, "L": L,
                         "B_lin": B_lin, "B_log": B_log,
                         "miss_lin": miss_lin, "miss_log": miss_log,
                         "miss_ap": miss_ap})

    # Spread of the miss factor: linear vs log-ratio (the headline).
    # Over the mpf values, NOT the serialized strings: max() on decimal strings
    # is lexicographic and would silently pick the wrong row.
    lin_miss = [r["miss_lin"] for r in raw_rows]
    log_miss = [r["miss_log"] for r in raw_rows]
    ap_miss = [r["miss_ap"] for r in raw_rows]
    _n = mp.nstr

    def _spread(xs):
        return _n(max(xs) / min(xs), 6)

    w = WitnessBuilder("log-ratio-binding-prototype", engine="python",
                       start_time=t0)
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        "Prototype extensive binding B = E_0·log(tr_free/tr_atom). The GS "
        "finding (tr_atom ≈ tr_free·f^bonds) makes the linear Δtr intensive/"
        "saturating (5–40× undershoot); the log-ratio is extensive over bonds. "
        "At the E_0 scale the log-ratio binding lands within O(1–2×) of B_AME "
        "(vs 5–40× linear) — a functional-form fix, NOT a fitted Δ_λ closure. "
        "Also reports per-bond energy under A−1 (chain, as-wired) vs C(A,2) "
        "(all-pairs, physical) to scope the bond-topology next step."
    )
    w.add_parameter("E_0_MeV", fmt(E0))
    w.add_parameter("Q_beta_MeV", fmt(Qb))
    w.add_data("rows", rows)
    w.add_data("headline", {
        "linear_miss_x": {r["atom"]: r["miss_linear_x"] for r in rows},
        "logratio_miss_x": {r["atom"]: r["miss_logratio_x"] for r in rows},
        "logratio_allpairs_miss_x": {r["atom"]: r["miss_logratio_allpairs_x"]
                                     for r in rows},
        "linear_miss_range": f"{_n(min(lin_miss), 4)}–{_n(max(lin_miss), 4)}×",
        "logratio_miss_range": f"{_n(min(log_miss), 4)}–{_n(max(log_miss), 4)}×",
        "logratio_allpairs_miss_range":
            f"{_n(min(ap_miss), 4)}–{_n(max(ap_miss), 4)}×",
        "verdict": (
            f"The log-ratio FORM collapses the undershoot from "
            f"{_n(min(lin_miss), 4)}–{_n(max(lin_miss), 4)}× (linear) to "
            f"{_n(min(log_miss), 4)}–{_n(max(log_miss), 4)}× (log-ratio @ E_0) "
            "— the binding gap was dominated by the wrong functional form "
            "(linear vs log), not a scalar. Residual O(1×) scatter is p/n "
            "composition + alpha magic + chain-vs-allpairs bond topology; NOT a "
            "closed law (no 7th ansatz)."),
    })
    # Assertion: the log-ratio form is within ~3× everywhere (qualitative leap
    # over the linear form which is 5–40× off).
    w.add_assertion(
        name="logratio_form_within_3x_everywhere",
        computed=fmt(max(max(log_miss), 1 / min(log_miss))),
        expected=fmt(mp.mpf(1)), tolerance=fmt(mp.mpf(2)),
        source="max over nuclei of max(miss, 1/miss) for B=E_0·log(tr_free/"
               "tr_atom); within ~3× vs the linear form's 5–40×.  "
               "🛑 THIS ASSERTION NOW FAILS, at 3.2592 against a 3.0 bound, and "
               "the bound is deliberately NOT widened (AGENTS.md: never make a "
               "red run green by widening).  It passed at 2.363 only because "
               "this witness was 68 days STALE -- committed 2026-06-15 against "
               "an upstream binding-canonical.witness.json last regenerated "
               "2026-08-22, which both corrected the nucleon traces (D tr_free "
               "0.98353 -> 1.13172, 4He 0.96732 -> 1.28078) and added three "
               "nuclei (6Li, 7Li, 7Be) the old run never saw.  So the failure "
               "is the corrected upstream data speaking, not a regression: the "
               "'within 3x' claim is false at 4He under the current traces.  "
               "Bean qou-ywie.",
    )
    out = w.save()

    print("=" * 96)
    print(" Log-ratio binding  B = E_0·log(tr_free/tr_atom)   vs linear B = Q_β·Δtr")
    print(f"   E_0 = {_n(E0, 10)} MeV   Q_β = {_n(Qb, 10)} MeV")
    print("=" * 96)
    print(f" {'atom':>9}{'A':>3}{'B_AME':>8}{'L=log(tf/ta)':>13}"
          f"{'B_lin(Qβ)':>10}{'lin miss':>9}{'B_log(E0)':>10}{'log miss':>9}"
          f"{'allpairs miss':>14}")
    print(" " + "-" * 94)
    for raw in raw_rows:
        print(f" {raw['atom']:>9}{raw['A']:>3}{_n(raw['B_ame'], 6):>8}"
              f"{_n(raw['L'], 6):>13}{_n(raw['B_lin'], 6):>10}"
              f"{_n(raw['miss_lin'], 4):>8}×{_n(raw['B_log'], 6):>10}"
              f"{_n(raw['miss_log'], 4):>8}×{_n(raw['miss_ap'], 4):>13}×")
    print(" " + "-" * 94)
    print(f" linear miss range:   {_n(min(lin_miss), 4)}–{_n(max(lin_miss), 4)}×  "
          f"(spread {_spread(lin_miss)}×)")
    print(f" log-ratio @ E_0:     {_n(min(log_miss), 4)}–{_n(max(log_miss), 4)}×  "
          f"(spread {_spread(log_miss)}×)  <- functional-form fix")
    print(f" log-ratio all-pairs: {_n(min(ap_miss), 4)}–{_n(max(ap_miss), 4)}×  "
          f"(spread {_spread(ap_miss)}×)  <- + bond-topology estimate")
    print(f"\n Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
