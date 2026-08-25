#!/usr/bin/env python3
"""qbeta_c3_crossanchor_swing_provenance_probe.py — what the c_3 "cross-anchor
swing" actually measures, and why three different percentages are all in the
corpus for it.

Bean `qou-cwin` follow-up. The figure `2.98 %` is cited across ~6 audit docs as
*the* c_3 cross-anchor swing, and is load-bearing: it is the evidence for the
NEAR-MATCH / REFUTED-as-real-q verdict (a true Taylor coefficient would be
anchor-independent). It does not reproduce from the current anchor pair.

WHAT THIS ESTABLISHES

1. **The current cross-anchor swing is 2.3748 %** (proton-normalised), or
   2.4571 % normalised by the candidate `-2`. Not 2.98 %.

2. **2.98 % is STALE, not mis-normalised.** It comes from a superseded muon
   value `c_3 = -2.0097`, explicitly labelled *"muon-pin (stale, pre-#1422)"*
   in `2026-05-31-c-3-categorical-derivation-attempt.md`. Today's extraction
   at the muon anchor is `-2.02020024` (this probe; independently in registry
   §9g). The muon value moved; the percentage did not follow.

3. **2.98 % and 2.88 % are the SAME stale gap under two normalisations** —
   `|c_p - c_m^stale| / 2` vs `|c_p - c_m^stale| / |c_p|`. Both are live in
   the corpus. This is the same normalisation trap as `c_2` vs `c̃_2` and as
   the `3.47 %` / `3.35 %` pair: a quantity differing only by denominator,
   read as a discrepancy.

4. **A NUMERICAL COINCIDENCE that will mislead the next reader.** The stale
   muon extraction `-2.00973976` and the *candidate model* `J_Hopf - ℏ_q²
   = -2.00981718` agree to **four decimals** while being different objects
   (they differ at 7.7e-5). The corpus writes both as "-2.0097"/"-2.0098". An
   earlier pass of this very investigation identified the stale value AS the
   model on that resemblance, and was wrong. Do not identify them by eye.

WHAT THIS DOES NOT ESTABLISH. The **verdict is unchanged.** c_3 remains a
q₀-dependent NEAR-MATCH, REFUTED as a real-q fibre element: the corrected
swing 2.3748 % is smaller than the quoted 2.98 % but still enormous next to
the 10⁻⁵⁰ compute precision, so it supports the same conclusion. This is a
scope-(a) correction to the *evidence*, not a change to the finding. No tier
moves, no value is wired or un-wired.

Anchors: proton (experimental, default per the 2026-08-07 directive) and muon
(ideal CAL-2). Every quantity is computed inside one layer — `c3_target_at`
takes the substrate quantities from its `q` argument and the CODATA Q-value
and m_e are anchor-independent physical constants, so there is no straddle.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import c3_target_at, substrate_ladder_quantities  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

#: The superseded muon-anchor `c_3` the 2.98 % / 2.88 % figures were computed
#: from. Source: `docs/audits/2026-05-22-exploration-c3-q-beta.md`
#: (`c_3_empirical_additive`), labelled stale in
#: `docs/audits/2026-05-31-c-3-categorical-derivation-attempt.md`.
C3_MUON_STALE = mp.mpf("-2.0097397609790")


def main() -> int:
    me = mp.mpf(M_E_MEV)
    Q_codata = mp.mpf(str(Q_BETA_MEV))
    qp, qm = q_at(), q_muon_at()
    cp, cm = c3_target_at(qp, Q_codata, me), c3_target_at(qm, Q_codata, me)

    # The candidate model, for the coincidence check only.
    model = -2 - substrate_ladder_quantities(qm)["hbar_q"] ** 2

    print("=" * 78)
    print(" c_3 cross-anchor swing — what 2.98 % actually measures")
    print("=" * 78)
    print(f"\n  extracted c_3, proton anchor : {mp.nstr(cp, 20)}")
    print(f"  extracted c_3, muon anchor   : {mp.nstr(cm, 20)}")
    print(f"  superseded muon value        : {mp.nstr(C3_MUON_STALE, 20)}  (pre-#1422)")

    def pct(x, denom):
        return abs(x) / abs(denom) * 100

    cur_p, cur_2 = pct(cp - cm, cp), pct(cp - cm, 2)
    old_p, old_2 = pct(cp - C3_MUON_STALE, cp), pct(cp - C3_MUON_STALE, 2)

    print(f"\n  {'swing':<34}{'/|c_p|':>12}{'/2':>12}")
    print("  " + "-" * 58)
    print(f"  {'CURRENT  (c_p vs c_m)':<34}{float(cur_p):>11.4f}%{float(cur_2):>11.4f}%")
    print(f"  {'STALE    (c_p vs pre-#1422 muon)':<34}{float(old_p):>11.4f}%{float(old_2):>11.4f}%")
    print("\n  The corpus's 2.88 % and 2.98 % are the STALE row's two columns.")
    print("  Neither is the current swing, which is 2.3748 % / 2.4571 %.")

    coincidence = abs(C3_MUON_STALE - model)
    print(f"\n  Coincidence guard: stale muon extraction vs the candidate model")
    print(f"    stale extraction  {mp.nstr(C3_MUON_STALE, 12)}")
    print(f"    J_Hopf - hbar_q^2 {mp.nstr(model, 12)}")
    print(f"    |difference|      {mp.nstr(coincidence, 6)}  — agree to 4 decimals,")
    print("    DIFFERENT objects. Do not identify them by eye; an earlier pass")
    print("    of this investigation did exactly that and was wrong.")

    print(f"""
{'=' * 78}
 Reading
{'=' * 78}

  2.98 % is stale, not mis-normalised: the muon-anchor c_3 moved from
  -2.0097 (pre-#1422) to -2.02020024, and the percentage did not follow.
  The current cross-anchor swing is 2.3748 % (proton-normalised).

  The VERDICT IS UNCHANGED. c_3 stays a q_0-dependent NEAR-MATCH, refuted as
  a real-q fibre element: 2.3748 % is smaller than the quoted 2.98 % but still
  vast next to the 1e-50 compute precision, so the same conclusion follows.
  Scope-(a) correction to the evidence, not to the finding.
""")

    wb = WitnessBuilder("qbeta-c3-crossanchor-swing-provenance", engine="mpmath")
    wb.set_description(
        "Resolves the provenance of the c_3 'cross-anchor swing 2.98 %' cited "
        "across ~6 audit docs and in the qbeta-ck-truncation-canonical "
        "authorNote. It does not reproduce from the current anchor pair: the "
        "figure was computed against a superseded muon-anchor c_3 = -2.0097 "
        "(pre-#1422), whereas today's muon extraction is -2.02020024. The "
        "current swing is 2.3748 % proton-normalised (2.4571 % normalised by "
        "the candidate -2). The corpus's 2.88 % and 2.98 % are the SAME stale "
        "gap under the two normalisations — the same trap as c_2/c-tilde_2 and "
        "as the 3.47 %/3.35 % pair. Also records a coincidence guard: the "
        "stale muon extraction (-2.00973976) and the candidate model "
        "J_Hopf - hbar_q^2 (-2.00981718) agree to four decimals while being "
        "different objects, which misled an earlier pass of this same "
        "investigation. VERDICT UNCHANGED: c_3 remains a q_0-dependent "
        "NEAR-MATCH refuted as a real-q fibre element; this is a scope-(a) "
        "correction to the evidence, not to the finding. No tier moves."
    )
    wb.add_data("ladder_frame", "u")
    wb.add_data("anchors", {
        "proton": {"q": fmt(qp), "c3": fmt(cp)},
        "muon": {"q": fmt(qm), "c3": fmt(cm)},
    })
    wb.add_data("superseded_muon_c3", fmt(C3_MUON_STALE))
    wb.add_data("swing_current", {
        "absolute": fmt(abs(cp - cm)),
        "pct_normalised_by_c3_proton": fmt(cur_p),
        "pct_normalised_by_candidate_2": fmt(cur_2),
    })
    wb.add_data("swing_stale_as_published", {
        "absolute": fmt(abs(cp - C3_MUON_STALE)),
        "pct_normalised_by_c3_proton": fmt(old_p),
        "pct_normalised_by_candidate_2": fmt(old_2),
    })
    wb.add_data("coincidence_guard", {
        "stale_muon_extraction": fmt(C3_MUON_STALE),
        "candidate_model_J_minus_hbar_sq": fmt(model),
        "abs_difference": fmt(coincidence),
    })
    wb.add_data("verdict_unchanged", True)

    wb.add_assertion(
        name="published_2_98_pct_does_not_reproduce_from_current_anchors",
        computed=str(int(mp.fabs(cur_2 - mp.mpf("2.98")) > mp.mpf("0.1")
                         and mp.fabs(cur_p - mp.mpf("2.98")) > mp.mpf("0.1"))),
        expected="1", tolerance=0,
        source=f"current swing is {mp.nstr(cur_p, 6)} % (proton-normalised) or "
               f"{mp.nstr(cur_2, 6)} % (candidate-normalised); neither is 2.98 %.",
    )
    wb.add_assertion(
        name="published_figures_reproduce_from_the_SUPERSEDED_muon_value",
        computed=str(int(mp.fabs(old_2 - mp.mpf("2.98")) < mp.mpf("0.01")
                         and mp.fabs(old_p - mp.mpf("2.88")) < mp.mpf("0.01"))),
        expected="1", tolerance=0,
        source=f"against the pre-#1422 muon c_3 = {mp.nstr(C3_MUON_STALE, 12)} the "
               f"gap is {mp.nstr(old_2, 6)} % normalised by 2 and "
               f"{mp.nstr(old_p, 6)} % normalised by |c_3 proton| — i.e. exactly "
               "the corpus's 2.98 % and 2.88 %. They are one stale gap under two "
               "normalisations, not two measurements.",
    )
    wb.add_assertion(
        name="stale_extraction_and_candidate_model_are_distinct_objects",
        computed=str(int(coincidence > 0)), expected="1", tolerance=0,
        source=f"|{mp.nstr(C3_MUON_STALE, 12)} - {mp.nstr(model, 12)}| = "
               f"{mp.nstr(coincidence, 6)}. They agree to four decimals and the "
               "corpus writes both as '-2.0097'/'-2.0098'. Identifying them by "
               "eye is a live hazard — an earlier pass of this investigation did "
               "so and had to retract.",
    )
    out = wb.save()
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
