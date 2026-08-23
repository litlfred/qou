#!/usr/bin/env python3
"""Can the flavor-split coefficient α improve Q_β? — NO (difference-of-large-
numbers amplification). Negative result, recorded to prevent re-chasing.

Identity: Q_β = (m_n − m_p) − m_e = M_N·split − m_e, where split = (m_n−m_p)/M_N
is the flavor split. So one could try to predict Q_β from a better flavor
split (the open α). This probe shows that route is amplification-limited and
strictly worse than the production Habiro Q_β path.

Why it fails: Q_β ≈ 0.782 MeV is the small DIFFERENCE of Δm ≈ 1.293 and
m_e ≈ 0.511. So a relative error ε in Δm becomes (Δm/Q_β)·ε ≈ 1.65·ε in Q_β.
The flavor split's best DERIVABLE form (geometric self-energy, α=1) is 0.0098%
on Δm → ~0.016% = 1.6e5 ppb on Q_β — vs the production Habiro Q_β at ~1248 ppb
(L2 target 7.8 ppb). The dedicated path already wins by ~128×.

Conclusion: α is a clean structural result for the flavor split, but it is NOT
on the critical path for Q_β (nor Δm_pn, which is itself best via Q_β/Path C).
The color-weighting δ that α would sharpen is de-wired to the proven leading.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: F401,E402

from mpmath import mp, mpf  # noqa: E402

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

from _li_2_q_util import flavor_split_leading  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# CODATA / PDG anchors.
M_P = mpf("938.27208816")
M_E = mpf("0.51099895069")
M_N_CODATA = mpf("939.56542194")
QB_PDG = mpf("0.78233341")


def qb_from_split(split):
    # M_N = m_p/(1 − split/2) (self-consistent: m_n = m_p + M_N·split).
    M_N = M_P / (1 - split / 2)
    dm = M_N * split
    return dm - M_E, dm


def main() -> int:
    q = mpf(Q_50_DIGIT_STR)
    lead = flavor_split_leading(q)
    forms = {
        "flavor_split_leading": lead,
        "flavor_split_geometric_alpha1": lead * (1 + lead),
        "flavor_split_posited_1plus_hbar3": lead * (1 + ((q - 1) / q) ** 3),
    }
    # Production Habiro Q_β residual (the dedicated path) — the canonical
    # de-fitted figure from docs/precision-goals.md (post-#1416).
    QB_PRODUCTION_HABIRO_PPB = mpf("1248")
    QB_L2_TARGET_PPB = mpf("7.8")

    print("Can α improve Q_β?  Q_β = M_N·split − m_e")
    print("=" * 60)
    rows = {}
    for name, split in forms.items():
        Qb, dm = qb_from_split(split)
        err_ppb = (Qb - QB_PDG) / QB_PDG * mpf(10) ** 9
        amp = abs(dm) / QB_PDG  # error-amplification factor Δm/Q_β
        rows[name] = {"split": str(split), "Q_beta": str(Qb),
                      "err_ppb": str(err_ppb), "amplification": str(amp)}
        print(f"  {name:34} Q_β={mp.nstr(Qb,9)}  err={mp.nstr(err_ppb,4)} ppb  (amp {mp.nstr(amp,4)}×)")
    print(f"\n  production Habiro Q_β path : ~{int(QB_PRODUCTION_HABIRO_PPB)} ppb")
    print(f"  L2 100× target             : {mp.nstr(QB_L2_TARGET_PPB,2)} ppb")
    print("\n  VERDICT: NO. The flavor-split route to Q_β is amplification-")
    print("  limited (Δm/Q_β ≈ 1.65×); even the derivable geometric form is")
    print("  ~128× WORSE than the dedicated Habiro Q_β path. α is NOT a")
    print("  critical-path lever for Q_β.")

    w = WitnessBuilder("flavor-split-alpha-qbeta-amplification", engine="mpmath")
    w.set_description(
        "Negative result: the flavor-split coefficient α cannot improve Q_β. "
        "Q_β = M_N·split − m_e amplifies Δm relative error by ~1.65× "
        "(difference of large numbers). The best derivable flavor split "
        "(geometric self-energy α=1, 0.0098% on Δm) gives Q_β at ~1.6e5 ppb, "
        "~128× worse than the production Habiro Q_β (~1248 ppb). α is a clean "
        "structural result but NOT on the critical path for Q_β/Δm_pn."
    )
    w.add_data("anchors", {"m_p": str(M_P), "m_e": str(M_E), "Qb_pdg": str(QB_PDG)})
    w.add_data("forms", rows)
    w.add_data("production_habiro_qbeta_ppb", str(QB_PRODUCTION_HABIRO_PPB))
    w.add_data("l2_target_ppb", str(QB_L2_TARGET_PPB))
    w.add_assertion(
        name="flavor_split_route_to_qbeta_worse_than_habiro",
        computed=1 if abs((qb_from_split(forms["flavor_split_geometric_alpha1"])[0] - QB_PDG) / QB_PDG * mpf(10) ** 9) > QB_PRODUCTION_HABIRO_PPB else 0,
        expected=1,
        source="geometric-form Q_β error (ppb) exceeds the production Habiro "
               "Q_β error — the flavor-split route does not improve Q_β",
    )
    w.save()
    print("\n  Witness: flavor-split-alpha-qbeta-amplification.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
