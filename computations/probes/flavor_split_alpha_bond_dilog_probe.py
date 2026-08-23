#!/usr/bin/env python3
"""Bond-dilog derivation of the flavor-split coefficient α — RULED OUT.

The flavor split is `split = leading·(1 + α·leading)` (2nd-order structure
proven; α = 0.92925 the open coefficient). A prior probe
(flavor-split-alpha-dilog-expansion) showed the q-dilog at the *tiny* argument
`leading ≈ 0.00138` cannot soften the geometric α=1 to 0.929 (q-effect ~0.1%
vs the 7.8% gap). This probe tests the natural next idea: the dilog at the
*O(1)* bond arguments — the actual archimedean bond energy
`E = E₀·log(1/f_pn)` (+ Li_2^q spectral corrections), where the p-n bond
factor `f_pn = z − h·(½ − δ/4)` carries O(1) `z ≈ 0.5`, `h ≈ 0.21`.

RESULT — RULED OUT. The O(1) bond argument makes α *worse*, not better:
  geometric 1/(1−lead)   α=1.0014  (+7.8%, closest)
  single-log             α=0.500   (−46%)
  Li_2^q(lead)           α=0.249   (−73%)
  bond-log   (O(1) arg)  α=0.066   (−93%)
  bond-Li_2^q(O(1) arg)  α=0.033   (−96%)

Analytic reason: any single `−ln(1−a·x)` has 2nd-order Taylor ratio
`c₂/c₁² = 1/2`; normalized to the split this gives `α ∝ A` (the bond
sensitivity `A = (h/4)/(z−h/2) ≈ 0.13`), so α ≈ 0.066; the dilog is smaller
still. The O(1) argument only *rescales*. ONLY the full geometric self-energy
resummation `Σ leadingⁿ` (α=1) lands near α_true. So α is a *resummed*
self-energy, NOT a single bond-dilog at any argument — and the exact 0.929
(7.8% below geometric) is the mass-functor per-block normalization, the same
open piece (NOT fitted here, per anti-flip-flop discipline). Anchor-stable.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: F401,E402

from mpmath import mp, mpf, log, sqrt  # noqa: E402

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

from _li_2_q_util import flavor_split_leading, li_2_q  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

CODATA = mpf("1.29333236") / ((mpf("938.27208816") + mpf("939.56542194")) / 2)


def _muon_q0():
    try:
        from qou_substrate.constants import q_muon_at
        return mpf(str(q_muon_at()))
    except Exception:
        return mpf("1.1099785955541810")


def analyze(q, label):
    h = q - 1 / q
    zmkv = q**3 / (q**2 + 1)
    lead = flavor_split_leading(q)
    a_true = (CODATA / lead - 1) / lead
    f0 = zmkv - h / 2
    A = (h / 4) / f0  # O(1) bond sensitivity of f_pn to the color-weighting δ

    def alpha(C):
        return (C - 1) / lead

    forms = {
        "geometric_full_resummation": 1 / (1 - lead),
        "single_log": -log(1 - lead) / lead,
        "li2q_leading_arg": li_2_q(lead, q) / lead,
        "bond_log_O1_arg": -log(1 - A * lead) / (A * lead),
        "bond_li2q_O1_arg": li_2_q(A * lead, q) / (A * lead),
    }
    rows = {}
    for name, C in forms.items():
        a = alpha(C)
        rows[name] = {"alpha": str(a),
                      "rel_err_vs_true_pct": str((a - a_true) / a_true * 100)}
    return {"anchor": label, "q0": str(q), "A_bond_sensitivity": str(A),
            "alpha_true": str(a_true), "forms": rows}


def main() -> int:
    rp = analyze(mpf(Q_50_DIGIT_STR), "proton_q0")
    rm = analyze(_muon_q0(), "muon_q0")
    print("Bond-dilog derivation of α — RULED OUT")
    print("=" * 56)
    for r in (rp, rm):
        print(f"\n  [{r['anchor']}] α_true={mp.nstr(mpf(r['alpha_true']),7)}  "
              f"bond A={mp.nstr(mpf(r['A_bond_sensitivity']),5)}")
        for n, d in r["forms"].items():
            print(f"    {n:28} α={mp.nstr(mpf(d['alpha']),7):>10}  "
                  f"err={mp.nstr(mpf(d['rel_err_vs_true_pct']),4):>9}%")
    drift = abs(mpf(rp["alpha_true"]) - mpf(rm["alpha_true"]))
    print(f"\n  α_true anchor drift: {mp.nstr(drift,4)}")
    print("  VERDICT: bond-dilog RULED OUT. O(1)-arg log/dilog give α≈0.03–0.07")
    print("  (worse than geometric). The split is a RESUMMED self-energy (α≈1),")
    print("  not a single bond-dilog; exact 0.929 is mass-functor-limited.")

    w = WitnessBuilder("flavor-split-alpha-bond-dilog", engine="mpmath")
    w.set_description(
        "Bond-dilog derivation of the flavor-split coefficient α: RULED OUT. "
        "The dilog/log at the O(1) bond arguments (z≈0.5, h≈0.21) gives "
        "α≈0.03–0.07 (worse than the geometric self-energy α=1, which is "
        "closest at +7.8%). Any single −ln(1−a·x) has 2nd-order ratio 1/2, so "
        "normalized α ∝ bond-sensitivity A≈0.13. α is a resummed self-energy, "
        "not a single bond-dilog; exact 0.929 is mass-functor-limited, not "
        "fitted. Anchor-stable."
    )
    w.add_data("codata_dmn_over_mn", str(CODATA))
    w.add_data("proton_anchor", rp)
    w.add_data("muon_anchor", rm)
    w.add_data("alpha_true_anchor_drift", str(drift))
    w.add_assertion(
        name="bond_dilog_O1_arg_worse_than_geometric",
        computed=1 if (abs(mpf(rp["forms"]["bond_log_O1_arg"]["alpha"]) - mpf(rp["alpha_true"]))
                       > abs(mpf(rp["forms"]["geometric_full_resummation"]["alpha"]) - mpf(rp["alpha_true"]))) else 0,
        expected=1,
        source="the O(1)-argument bond-log α is farther from α_true than the "
               "geometric self-energy — the bond-dilog does not derive α",
    )
    w.save()
    print("\n  Witness: flavor-split-alpha-bond-dilog.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
