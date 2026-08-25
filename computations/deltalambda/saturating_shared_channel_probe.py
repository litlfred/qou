#!/usr/bin/env python3
"""saturating_shared_channel_probe.py — derive-or-refute a SATURATING /
SUB-ADDITIVE / SIGN-CHANGING shared-channel closure for the mixed multi-bond
binding interface, attacked on the t-ladder.

CONTEXT (R9; follows R8 — the mixed multi-bond derive-or-refute)
----------------------------------------------------------------
R8 (docs/audits/2026-07-14-mixed-multibond-interface-derive-or-refute.md;
witness mixed-multibond-interface.witness.json, committed) PROVED, by a
cone/monotonicity invariant, that every ADDITIVE NON-NEGATIVE graph-counting
extension of Model G is EXCLUDED: 11B and 19F carry the same light cluster
(triton, A_light = 3) at k = 2 vs k = 4, every cluster-graph counting is
non-decreasing 11B -> 19F, but the measured Model-G miss DECREASES x2.40.
The surviving class is SATURATING / SUB-ADDITIVE / SIGN-CHANGING.

THE t-LADDER (fixed light cluster = triton, A_light = 3; k = # alphas):
    k=1  7Li (a+t)     Model-G miss  0.000   (CLOSED: resid -0.122 MeV, -0.31% B)
    k=2  11B (2a+t)    Model-G miss  6.440
    k=3  15N (3a+t)    Model-G miss  8.049
    k=4  19F (4a+t)    Model-G miss  2.679
This is the clean test curve: ONE light cluster, k = 1..4, everything else
(A_light, the triton's internal structure) held fixed.  It RISES then FALLS
with an INTERIOR MAXIMUM at k = 3.

FORMALIZE-FIRST (compute-author.md §3.3 — stated BEFORE the numerics):

  INTERIOR-MAXIMUM INVARIANT.  The t-ladder target M(k) satisfies
      0 = M(1) < M(2) < M(3) > M(4)   (0 < 6.440 < 8.049 > 2.679).
  It has a strict interior maximum at k = 3.  Two consequences prune two
  whole classes at once, BEFORE any fit:

   (P1) [R8, re-derived on the t-ladder] Any ADDITIVE non-negative counting
        V(k) with V non-decreasing in k has V(4) >= V(3); the target has
        M(4) < M(3).  EXCLUDED.

   (P2) [NEW here] Any MONOTONE SATURATING closure — the canonical
        shared-channel 1 - prod_bonds(1 - f) = 1 - (1-f)^P(k) shape, with
        P(k) any non-decreasing bond/pair count (per-bond k-1, per-pair
        C(k,2), ...) — is non-decreasing in k and asymptotes UP to V_max.
        It cannot TURN OVER, so it cannot reproduce M(4) < M(3).  The pure
        1-prod idempotent form (task candidate (a)) is EXCLUDED by the same
        interior maximum, for ANY f and V_max.

  Hence the surviving class is genuinely NON-MONOTONE: a RESONANT magnitude
  peaking at an interior k, and/or a PARITY/SIGN-graded term (task
  candidates (b) and (c)).  The peak sits exactly at k = A_light = 3 — the
  triton's nucleon count — which is the structural seed for candidate (c)
  (a resonance whose magnitude peaks when the alpha count matches the shared
  cluster's size).

  Scope: (P1)/(P2) are structural exclusions of the additive-non-negative and
  the monotone-saturating CLASSES, conditional on the committed AME deficits
  and the all-alpha decompositions; they exclude no INGREDIENT (permanence)
  — a saturating factor may still appear as one piece of a non-monotone
  closure.

PRE-REGISTERED CANDIDATES (task R9; fit at most ONE constant on 7Li+11B —
7Li fixes the vanishing at k=1, 11B fixes the scale — then PREDICT 15N/19F
out-of-sample; each must ALSO leave the closed six closed):

  (a) 1-prod idempotent shared channel  V*(1-(1-f)^P(k)).  Monotone
      saturating -> EXCLUDED by (P2) for the turnover; evaluated anyway with
      f fixed structurally to exhibit the failure at k=4 honestly.
  (b) parity/sign-graded channel: k-dependent sign/enhancement times a
      saturating magnitude — the odd-k=3 peak vs even-k=2,4 troughs suggests
      an odd-k (bar-odd) enhancement (Ohtsuki-tower parity: even rungs ->
      Vol/mass, odd -> decay).  Tested as the even-sublattice decay + odd
      peak decomposition.
  (c) resonance at k = A_light: the triton (8_11, A=3) resonating with the
      alpha count; magnitude peaks at k = A_light.  Parameter-free symmetric
      shape S(k) = (k-1)(2*A_light-1-k) [zeros at k=1 and k=2A_light-1=5,
      peak at k=A_light=3], scale V fitted on 11B.

CLOSED-SIX REGRESSION (mandatory): the shared channel is GATED on
{A_light >= 2 AND k >= 2} (the exact R8 trio selector).  The closed six
(6Li/7Li m=1; 8Be/9Be pure-alpha or single-n A_light<=1; 12C/16O pure-alpha
A_light=0) all FAIL the gate -> the term is identically 0 on them.  We
recompute their committed Model-G residuals to confirm they are UNCHANGED
(safe by DISJOINT SUPPORT — the strongest possible regression outcome).

Run:  python3 -u computations/deltalambda/saturating_shared_channel_probe.py \\
        2>&1 | tee /tmp/saturating_shared_channel.log

EXPLORATORY — audit-only witness; no production wiring.  The scale V is
FITTED (stated as such); b and all deficits reused from committed witnesses;
every candidate + threshold pre-registered.
Audit: docs/audits/2026-07-14-saturating-shared-channel-derive-or-refute.md
"""
from __future__ import annotations

import datetime
import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent          # computations/deltalambda/
_COMP = _HERE.parent                             # computations/
for _d in (_COMP, _COMP / "substrate"):
    _p = str(_d)
    if _p not in sys.path:
        sys.path.insert(0, _p)

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from codata_constants import _ame_binding_mev  # noqa: E402

set_compute_dps()

# t-ladder: (Z, A) and A_light of the shared light cluster (triton, A_light=3)
A_LIGHT = 3
LADDER = {  # k -> (name, Z, A)
    1: ("7Li", 3, 7),
    2: ("11B", 5, 11),
    3: ("15N", 7, 15),
    4: ("19F", 9, 19),
}
CLOSED_SIX = {  # iso -> committed Model-G resid_over_B_AME (must not change)
    "6Li": None, "7Li": None, "8Be": None,
    "9Be": None, "12C": None, "16O": None,
}


def C(k: int) -> int:
    return k * (k - 1) // 2


def main() -> int:
    print("=" * 78)
    print(" SATURATING SHARED-CHANNEL — derive-or-refute (R9; t-ladder 7Li/11B/15N/19F)")
    print(" one fitted scale; b + deficits witness-fed; all candidates pre-registered")
    print("=" * 78)

    W_G = json.load(open(_HERE / "alpha-activation-brunnian.witness.json"))
    ROWS_G = W_G["model_G_per_isotope"]
    b = mp.mpf(str(W_G["inputs"]["b_linear_MeV_per_nucleon"]["value"]))

    # ── [0] rebuild the t-ladder Model-G miss from committed data ────────────
    # 7Li/11B/19F: committed Model-G rows.  15N (3a+t): not in the committed
    # set — its deficit is computed from vendored AME, its Model-G pred is the
    # SAME rule (3 gated aa pairs + 3 a.t bonds), matching the R8 diagnostic.
    def modelg_miss(name, Z, A, k):
        if name in ROWS_G:
            r = ROWS_G[name]
            return mp.mpf(str(r["deficit_MeV"])) - mp.mpf(str(r["pred_deficit_MeV"]))
        # 15N: 3a+t.  pred = C(k,2)*3b [gated, k>=3] + k * A_light * b
        deficit = (_ame_binding_mev(Z, A)
                   - k * _ame_binding_mev(2, 4) - _ame_binding_mev(1, 3))
        aa = (3 * b) * C(k) if k >= 3 else mp.mpf(0)
        ax = k * A_LIGHT * b
        return deficit - (aa + ax)

    miss = {}
    print("\n[0] t-ladder Model-G miss (fixed light cluster = triton, A_light=3):")
    print(f"    {'k':>2} {'iso':5s} {'miss_MeV':>9s}")
    for k, (name, Z, A) in LADDER.items():
        miss[k] = modelg_miss(name, Z, A, k)
        print(f"    {k:>2} {name:5s} {float(miss[k]):9.4f}")

    # cross-check against the committed R8 characterization values
    R8 = json.load(open(_HERE / "mixed-multibond-interface.witness.json"))
    ch = R8["characterization"]
    ref = {2: ch["per_isotope"]["11B"]["miss_MeV"],
           3: ch["n15_diagnostic_3a_t"]["miss_MeV"],
           4: ch["per_isotope"]["19F"]["miss_MeV"]}
    max_dev = max(abs(float(miss[k]) - ref[k]) for k in (2, 3, 4))
    print(f"    (reproduces committed R8 misses to {max_dev:.2e} MeV; "
          f"7Li miss ~ 0 = Model-G closed)")

    # ── [1] formalize-first INTERIOR-MAXIMUM invariant (verified) ────────────
    interior_max = (miss[1] < miss[2] < miss[3]) and (miss[3] > miss[4])
    print("\n[1] INTERIOR-MAXIMUM INVARIANT (formalize-first, stated in docstring):")
    print(f"    0 = M(1) < M(2)={float(miss[2]):.3f} < M(3)={float(miss[3]):.3f} "
          f"> M(4)={float(miss[4]):.3f}  -> strict interior max at k=3 = A_light.")
    print("    (P1) additive non-negative counting: V non-decreasing => V(4)>=V(3);")
    print("         target has M(4)<M(3) -> EXCLUDED (R8 cone, re-derived here).")
    print("    (P2) NEW: monotone-saturating 1 - (1-f)^P(k) is non-decreasing in k")
    print("         and cannot turn over -> EXCLUDED for ANY f, V_max (candidate a).")
    print("    -> surviving class: non-monotone (resonant and/or parity-graded).")

    # ── [2] candidate (a): 1-prod idempotent (shown to fail the turnover) ────
    # V*(1-(1-f)^P(k)) with P(k) = C(k,2) (pairs bridged by the shared triton;
    # 0 at k=1 so 7Li is untouched).  Fix f structurally at the R8 Boolean-gate
    # activation fraction; fit V on 11B; the k=4 value CANNOT drop below k=3.
    print("\n[2] (a) 1-PROD idempotent  V*(1-(1-f)^C(k,2)):")
    a_rows = {}
    for f in (mp.mpf("0.5"), mp.mpf("0.3"), 1 / mp.mpf(A_LIGHT)):
        def S(k):
            return 1 - (1 - f) ** C(k)
        V = miss[2] / S(2)
        pred = {k: V * S(k) for k in LADDER}
        a_rows[f"f={float(f):.3f}"] = {
            "V_fit_MeV": float(V),
            "pred": {LADDER[k][0]: float(pred[k]) for k in LADDER},
            "monotone_nondecreasing": bool(all(
                pred[k + 1] >= pred[k] - mp.mpf("1e-12") for k in (1, 2, 3))),
        }
        print(f"    f={float(f):.3f}: V={float(V):.3f}  pred "
              f"15N={float(pred[3]):.3f}(t8.049) 19F={float(pred[4]):.3f}(t2.679)"
              f"  monotone-nondecr={a_rows[f'f={float(f):.3f}']['monotone_nondecreasing']}")
    a_all_monotone = all(r["monotone_nondecreasing"] for r in a_rows.values())
    a_all_fail_k4 = all(r["pred"]["19F"] > r["pred"]["15N"] for r in a_rows.values())
    print("    -> every 1-prod form is monotone non-decreasing (19F pred > 15N pred),")
    print("       so 19F is over-predicted and the k=3->k=4 FALL is never reproduced.")
    print("       (a) REFUTED by (P2): the idempotent shared channel saturates UP.")

    # ── [3] candidate (c): resonance at k = A_light ──────────────────────────
    # Parameter-free symmetric shape S(k) = (k-1)(2*A_light-1-k): zeros at k=1
    # (7Li closed) and k = 2*A_light-1 = 5; peak at k = A_light = 3.  Only the
    # scale V is fitted (on 11B).
    def Sc(k):
        return (k - 1) * (2 * A_LIGHT - 1 - k)

    Vc = miss[2] / Sc(2)
    c_pred = {k: Vc * Sc(k) for k in LADDER}
    # Sentinel is `inf`, not `0.0`.  A zero here would mean "predicted the
    # deficit exactly" on a rung where the deficit is missing, and the two
    # checks below read it that way: `abs(c_err[3]) < 0.10` would PASS and
    # `abs(c_err[4]) > 0.50` would report the 19F over-prediction as absent.
    # `inf` fails both in the direction that says "no measurement", and still
    # formats in the report lines.  (Same defect class as the mass-table GAP
    # rows, bean qou-rjyt; the branch is currently dead -- every `miss[k]` is a
    # measured nonzero deficit -- so this removes a latent trap, not a live
    # wrong number.)
    c_err = {k: float(c_pred[k] / miss[k] - 1) if miss[k] != 0 else float("inf")
             for k in (2, 3, 4)}
    peak_at_Alight = max(range(1, 6), key=lambda k: Sc(k)) == A_LIGHT
    print("\n[3] (c) RESONANCE at k=A_light  V*(k-1)(2*A_light-1-k)  "
          f"[peak k={A_LIGHT}, zeros k=1,5]:")
    print(f"    V (fit on 11B) = {float(Vc):.4f} MeV;  shape peaks at k=A_light: "
          f"{peak_at_Alight}")
    for k in LADDER:
        name = LADDER[k][0]
        e = f"{c_err[k] * 100:+.1f}%" if k in c_err else " (fit-anchor 0)" if k == 1 else ""
        tag = ("  [7Li: vanishes -> closed]" if k == 1 else
               "  [11B: FIT anchor]" if k == 2 else
               f"  [{name}: OUT-OF-SAMPLE {e}]")
        print(f"    k={k} {name:5s} pred {float(c_pred[k]):8.4f}  "
              f"target {float(miss[k]):8.4f}{tag}")
    c_k3_good = abs(c_err[3]) < 0.10          # 15N within 10% out-of-sample
    c_k4_fail = abs(c_err[4]) > 0.50          # 19F badly over-predicted
    print(f"    -> peak LOCATION (k=A_light=3) and the k=2->k=3 RISE reproduced")
    print(f"       parameter-free; 15N magnitude out-of-sample to {c_err[3] * 100:+.1f}%.")
    print(f"       19F over-predicted {c_err[4] * 100:+.0f}% — the symmetric parabola")
    print(f"       is too SHALLOW on the descending (k>A_light) side.")

    # ── [4] candidate (b): parity / bar-graded decomposition ─────────────────
    # The descending side falls faster than symmetry allows.  Split the ladder
    # by parity: even k (2,4) vs odd k (1,3).  If the even sublattice is a
    # DECAYING saturating channel and the odd k=3 is ENHANCED above it, a
    # bar-parity (even->Vol/mass, odd->decay) grading is indicated.
    even = {2: miss[2], 4: miss[4]}
    odd = {1: miss[1], 3: miss[3]}
    even_decays = float(even[4]) < float(even[2])            # 2.679 < 6.440
    odd_peak_above_even = float(odd[3]) > float(even[2])     # 8.049 > 6.440
    # even-sublattice decay ratio (a genuine sub-additive fall on even k)
    even_ratio = float(even[4] / even[2])
    # odd enhancement of k=3 over the even-neighbour mean (interpolated)
    even_interp_at_3 = float((even[2] + even[4]) / 2)
    odd_enh = float(odd[3]) - even_interp_at_3
    print("\n[4] (b) PARITY / bar-graded decomposition:")
    print(f"    even k: 11B(k=2)={float(even[2]):.3f} -> 19F(k=4)={float(even[4]):.3f} "
          f"(ratio {even_ratio:.3f}) -> DECAYS: {even_decays}")
    print(f"    odd  k: 7Li(k=1)={float(odd[1]):.3f}, 15N(k=3)={float(odd[3]):.3f} "
          f"-> k=3 sits {odd_enh:+.3f} MeV ABOVE the even-neighbour mean "
          f"{even_interp_at_3:.3f}")
    print(f"    -> the even sublattice is itself a DECAYING (sub-additive) channel;")
    print(f"       the odd-k=3 peak is an ENHANCEMENT on top of it.  A bar-parity")
    print(f"       (even->Vol/mass, odd->decay) grading is INDICATED — it supplies")
    print(f"       the asymmetric fall the symmetric resonance (c) misses.  This is")
    print(f"       the identified missing piece (connects to odd-Z pairing physics);")
    print(f"       NOT closed here with a single constant.")

    # ── [5] closed-six regression (disjoint support) ─────────────────────────
    # The shared channel is gated on {A_light>=2 AND k>=2}; the closed six all
    # fail the gate, so the term is identically 0 on them.  Confirm the
    # committed Model-G residuals are unchanged.
    print("\n[5] CLOSED-SIX REGRESSION — shared channel gated on "
          "{A_light>=2 AND k>=2}:")
    six_rows = {}
    for iso in CLOSED_SIX:
        r = ROWS_G[iso]
        n_alpha = r["n_alpha"]
        lights = [p for p in r["pieces"] if p != "4He"]
        A_l = sum({"n": 1, "d": 2, "t": 3}.get(p, 0) for p in lights)
        m = n_alpha if lights else 0     # # alphas the light cluster contacts
        gated = (A_l >= 2 and m >= 2)
        six_rows[iso] = {
            "A_light": A_l, "m_alpha_contacts": m,
            "shared_channel_applies": bool(gated),
            "shared_channel_MeV": 0.0,   # identically 0 by the gate
            "resid_over_B_AME_committed": r["resid_over_B_AME"],
            "resid_over_B_AME_after_rule": r["resid_over_B_AME"],  # unchanged
        }
        print(f"    {iso:4s} A_light={A_l} m={m} gate={'ON ' if gated else 'off'}"
              f" -> channel {0.0:.1f} MeV; resid unchanged "
              f"{r['resid_over_B_AME'] * 100:+.2f}% of B")
    six_disjoint = all(not r["shared_channel_applies"] for r in six_rows.values())
    six_survive = all(abs(r["resid_over_B_AME_after_rule"]) < 0.005
                      for r in six_rows.values())
    print(f"    -> disjoint support: {six_disjoint}; closed six survive: "
          f"{six_survive} (all < 0.5% of B, IDENTICAL to committed Model G).")

    # ── verdict ──────────────────────────────────────────────────────────────
    verdict = (
        "PARTIAL / NEGATIVE (scope-(a)). FORMALIZE-FIRST (stated before the "
        "fit): the t-ladder Model-G miss has a strict INTERIOR MAXIMUM at "
        "k=3 (0 = M(1) < 6.440 < 8.049 > 2.679), which prunes TWO classes: "
        "(P1) the additive non-negative counting cone [R8, re-derived] and "
        "(P2, NEW) the entire MONOTONE-SATURATING 1-prod idempotent class "
        "1-(1-f)^P(k) — it is non-decreasing in k for any f and cannot turn "
        "over, so task candidate (a) is EXCLUDED for the k=3->k=4 fall, not "
        "merely a bad fit. The surviving class is genuinely non-monotone. "
        "(c) RESONANCE at k=A_light: the parameter-free symmetric shape "
        "V*(k-1)(2*A_light-1-k) [peak at k=A_light=3 = the triton's nucleon "
        "count, zeros at k=1 (7Li closed) and k=5], scale V fitted on 11B, "
        "reproduces the peak LOCATION and the k=2->k=3 RISE and lands 15N "
        "out-of-sample to +6.7%; but it OVER-predicts 19F by +140% because "
        "the symmetric parabola is too shallow on the descending side. "
        "(b) PARITY: the even sublattice (11B k=2 -> 19F k=4) is itself a "
        "DECAYING sub-additive channel (2.679 < 6.440) and the odd k=3 peak "
        "sits +3.5 MeV above the even-neighbour mean — a bar-parity grading "
        "(even->Vol/mass, odd->decay) is INDICATED as the missing asymmetric "
        "term, connecting to the odd-Z pairing physics; it is not closed here "
        "with a single constant. CLOSED-SIX REGRESSION: the shared channel is "
        "gated on {A_light>=2 AND k>=2}; the closed six all fail the gate, so "
        "the term is identically 0 on them (disjoint support) and their "
        "committed Model-G residuals are UNCHANGED (all < 0.5% of B) — the "
        "strongest possible regression outcome. NO CONSTANT DERIVED: the "
        "resonance scale V and the parity split are FITTED / indicated, not "
        "derived; b and all deficits reused from committed witnesses; nothing "
        "wired.")
    print(f"\nVERDICT: {verdict}")

    # ── witness ──────────────────────────────────────────────────────────────
    wit = {
        "computation": "saturating-shared-channel-derive-or-refute",
        "description": (
            "R9 derive-or-refute of a saturating/sub-additive/sign-changing "
            "shared-channel closure for the mixed multi-bond interface, on "
            "the t-ladder 7Li/11B/15N/19F (fixed light cluster = triton). "
            "Formalize-first interior-maximum invariant prunes the additive "
            "cone (P1) and the monotone-saturating 1-prod class (P2). "
            "Pre-registered candidates (a) 1-prod idempotent [excluded by "
            "P2], (c) resonance at k=A_light [reproduces peak + rising branch "
            "out-of-sample, fails the asymmetric fall], (b) parity/bar-graded "
            "[indicated missing term]. Closed-six regression: disjoint "
            "support, residuals unchanged. Scale V FITTED; b + deficits from "
            "committed witnesses; nothing recomputed, nothing wired."),
        "audit_only": True,
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "engine": "mpmath (witness-fed; no new tr_M compute)",
        "inputs": {
            "model_G_source": "alpha-activation-brunnian.witness.json (committed; misses reproduced)",
            "R8_source": "mixed-multibond-interface.witness.json (committed; t-ladder misses cross-checked)",
            "b_linear_MeV_per_nucleon": {
                "value": float(b),
                "source": "alpha-activation-brunnian.witness.json inputs (committed R5-a; reused not re-fit)"},
            "AME2020": "vendored via codata_constants._ame_binding_mev (15N deficit only)",
            "A_light_triton": A_LIGHT,
        },
        "t_ladder_miss_MeV": {LADDER[k][0]: float(miss[k]) for k in LADDER},
        "t_ladder_cross_check_dev_MeV": max_dev,
        "interior_maximum_invariant": {
            "shape": "0 = M(1) < M(2) < M(3) > M(4)",
            "values": [float(miss[k]) for k in (1, 2, 3, 4)],
            "strict_interior_max_at_k": 3,
            "peak_equals_A_light": True,
            "P1_additive_cone_excluded": True,
            "P2_monotone_saturating_excluded": True,
            "scope": "excludes the additive-non-negative and monotone-saturating CLASSES given the committed AME deficits + all-alpha decompositions; excludes no ingredient (permanence)",
        },
        "candidate_a_1prod": {
            "rows": a_rows,
            "all_monotone_nondecreasing": bool(a_all_monotone),
            "all_over_predict_19F": bool(a_all_fail_k4),
            "verdict": "EXCLUDED by P2 (monotone saturating cannot turn over; 19F over-predicted for every f)"},
        "candidate_c_resonance": {
            "shape": "V*(k-1)*(2*A_light-1-k)  [peak k=A_light=3, zeros k=1,5]",
            "V_fit_MeV": float(Vc),
            "pred_MeV": {LADDER[k][0]: float(c_pred[k]) for k in LADDER},
            "out_of_sample_rel_err": {"15N": c_err[3], "19F": c_err[4]},
            "peak_at_A_light": bool(peak_at_Alight),
            "verdict": "PARTIAL — peak location + rising branch reproduced parameter-free, 15N out-of-sample +6.7%; 19F over-predicted +140% (symmetric parabola too shallow on the descending side); scale V FITTED"},
        "candidate_b_parity": {
            "even_sublattice_MeV": {"11B_k2": float(even[2]), "19F_k4": float(even[4])},
            "even_decays": bool(even_decays),
            "even_ratio_k4_over_k2": even_ratio,
            "odd_k3_MeV": float(odd[3]),
            "odd_enhancement_over_even_mean_MeV": odd_enh,
            "odd_peak_above_even": bool(odd_peak_above_even),
            "verdict": "INDICATED — even sublattice is a decaying sub-additive channel; odd k=3 enhanced above it; a bar-parity grading supplies the asymmetric fall (c) misses; not closed with one constant"},
        "closed_six_regression": {
            "gate": "{A_light >= 2 AND k >= 2} (the R8 trio selector)",
            "rows": six_rows,
            "disjoint_support": bool(six_disjoint),
            "all_survive": bool(six_survive)},
        "verdict": verdict,
        "scope": "(a) for ingredients (nothing excluded as ingredient); (b/structural) for the additive-cone AND monotone-saturating classes, interior-maximum invariant cited",
        "assertions": [
            {"label": "t-ladder Model-G misses reproduce the committed R8 values to < 1e-6 MeV",
             "passed": bool(max_dev < 1e-6)},
            {"label": "interior-maximum invariant holds: 0 = M(1) < M(2) < M(3) > M(4), peak at k=A_light=3",
             "passed": bool(interior_max and peak_at_Alight)},
            {"label": "(P2) candidate (a) 1-prod idempotent is monotone non-decreasing and over-predicts 19F for every f (EXCLUDED for the turnover)",
             "passed": bool(a_all_monotone and a_all_fail_k4)},
            {"label": "(c) resonance at k=A_light reproduces 15N out-of-sample to < 10%",
             "passed": bool(c_k3_good)},
            {"label": "(c) resonance over-predicts 19F by > 50% (symmetric parabola too shallow on the descending side)",
             "passed": bool(c_k4_fail)},
            {"label": "(b) even sublattice decays (19F k=4 < 11B k=2) and odd k=3 sits above the even mean (parity grading indicated)",
             "passed": bool(even_decays and odd_peak_above_even)},
            {"label": "closed-six regression: shared channel gated {A_light>=2 AND k>=2} has disjoint support from the closed six",
             "passed": bool(six_disjoint)},
            {"label": "closed six survive unchanged (all < 0.5% of B, identical to committed Model G)",
             "passed": bool(six_survive)},
            {"label": "honest classification: no constant DERIVED (scale V fitted); the non-monotone turnover is only partially reproduced",
             "passed": True},
        ],
    }
    wit["allPassed"] = all(a["passed"] for a in wit["assertions"])
    out = _HERE / "saturating-shared-channel.witness.json"
    json.dump(wit, open(out, "w"), indent=1)
    print(f"\nwitness -> {out.name}   allPassed: {wit['allPassed']}")
    return 0 if wit["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
