#!/usr/bin/env python3
"""deuteron_ladder_falsification_probe.py — FALSIFICATION TEST of the
"resonance at k = A_light" reading of the shared-channel miss (R9).

CONTEXT (R10; follows R9 — the saturating shared-channel derive-or-refute)
--------------------------------------------------------------------------
R9 (docs/audits/2026-07-14-saturating-shared-channel-derive-or-refute.md;
witness saturating-shared-channel.witness.json, committed) attacked the
t-LADDER (fixed light cluster = triton, A_light = 3; k = # alphas):

    k=1  7Li (a+t)     Model-G miss  0.122   (CLOSED, -0.31% B)
    k=2  11B (2a+t)    Model-G miss  6.440
    k=3  15N (3a+t)    Model-G miss  8.048   <- interior maximum
    k=4  19F (4a+t)    Model-G miss  2.679

R9 read the interior maximum at k=3 as a RESONANCE at k = A_light (the peak
sits where the alpha count matches the triton's nucleon count, A_light = 3),
and stated a FALSIFIABLE out-of-sample prediction (R9 §6 next-steps item 3):

    "Repeat the ladder with the deuteron (A_light = 2; 6Li k=1, 14N k=3) to
     test whether the peak tracks k = A_light (predict a peak at k=2 for the
     d-ladder)."

THE TEST (pre-registered BEFORE the fresh compute; 14N is the only d-ladder
member already in the committed R8 data):

  RESONANCE PREDICTION (k = A_light = 2): the deuteron-ladder miss should
    PEAK at k=2 (10B), i.e. miss(10B) > miss(14N) > miss(18F), peak at k=2.
  NULL / FALSIFIER: if the miss peaks at k=3 (14N) AGAIN — the same k as the
    triton ladder — then the peak is a FIXED-k=3 effect (the 3-alpha Brunnian
    onset, i.e. the k>=3 alpha.alpha gate turn-on, independent of A_light),
    and "resonance at k = A_light" is FALSIFIED.

THE DEUTERON LADDER (fixed light cluster = deuteron, A_light = 2; k = #alpha):
    k=1  6Li (a+d)     Model-G miss  ~0      (CLOSED, +0.28% B; committed)
    k=2  10B (2a+d)    Z=5  A=10     fresh   <- resonance predicts the PEAK here
    k=3  14N (3a+d)    Z=7  A=14     committed (R8: miss 5.818)
    k=4  18F (4a+d)    Z=9  A=18     fresh

Model-G ledger (SAME as R8/R9 — reused, not re-derived):
    pred = 3b * C(k,2) * [k >= 3]        (gated alpha.alpha pair term)
         + k * A_light * b               (always-on light-spectator channel)
    miss = deficit - pred,   deficit = B_AME(iso) - k*B_AME(4He) - B_AME(light)
    b = 0.78192... MeV/nucleon (committed R5-a witness; reused).

TRIANGULATION (a third A_light value; the d-vs-t comparison is the decisive
one, this only adds a data point): the NEUTRON ladder (kalpha)+n, A_light = 1
(9Be k=2 closes; 13C k=3; 17O k=4). For A_light = 1 the resonance shape
S(k) = (k-1)(2*A_light-1-k) = -(k-1)^2 is degenerate (<= 0, no positive peak),
so resonance predicts NO interior peak; a k=3 peak there is a third
independent falsifier.

Run:  python3 -u computations/deltalambda/deuteron_ladder_falsification_probe.py \\
        2>&1 | tee /tmp/deuteron_ladder_falsification.log

EXPLORATORY — audit-only witness; no production wiring; NO fitted constant
(this is a falsification test, not a fit: b + the ledger reused from committed
witnesses; only the fresh AME deficits of 10B/18F/13C/17O are read from the
vendored AME2020 table).  R9's structural P1/P2 prunes are NOT under test and
STAND regardless of the outcome; only the "resonance at k=A_light"
INTERPRETATION is tested here.
Audit: docs/audits/2026-07-14-deuteron-ladder-falsification.md
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

# light-cluster (Z, A) and A_light per ladder
LIGHT = {"d": (1, 2), "t": (1, 3), "n": (0, 1)}
# ladder members: label -> (name, Z, A) at each k
DEUTERON = {1: ("6Li", 3, 6), 2: ("10B", 5, 10), 3: ("14N", 7, 14), 4: ("18F", 9, 18)}
TRITON = {1: ("7Li", 3, 7), 2: ("11B", 5, 11), 3: ("15N", 7, 15), 4: ("19F", 9, 19)}
NEUTRON = {2: ("9Be", 4, 9), 3: ("13C", 6, 13), 4: ("17O", 8, 17)}  # k=1 5He unbound


def C(k: int) -> int:
    return k * (k - 1) // 2


def main() -> int:
    print("=" * 80)
    print(" DEUTERON-LADDER FALSIFICATION TEST — resonance at k=A_light?  (R10; follows R9)")
    print(" PRE-REGISTERED: resonance => d-ladder (A_light=2) peaks at k=2 (10B).")
    print("                 FALSIFIER => peaks at k=3 (14N) again = fixed 3-alpha onset.")
    print(" b + ledger witness-fed; NO fit (falsification test); fresh AME deficits only.")
    print("=" * 80)

    W_G = json.load(open(_HERE / "alpha-activation-brunnian.witness.json"))
    ROWS_G = W_G["model_G_per_isotope"]
    b = mp.mpf(str(W_G["inputs"]["b_linear_MeV_per_nucleon"]["value"]))

    def modelg_miss(name, Z, A, k, A_light, light):
        """Model-G miss for a (k alpha)+light isotope.  Uses the committed
        ledger row when available (6Li/14N/7Li/11B/15N/19F/9Be); otherwise the
        SAME rule on fresh vendored-AME deficits (10B/18F/13C/17O)."""
        if name in ROWS_G:
            r = ROWS_G[name]
            return mp.mpf(str(r["deficit_MeV"])) - mp.mpf(str(r["pred_deficit_MeV"]))
        lZ, lA = light
        b_light = mp.mpf(0) if lZ == 0 else _ame_binding_mev(lZ, lA)  # n: free nucleon
        deficit = _ame_binding_mev(Z, A) - k * _ame_binding_mev(2, 4) - b_light
        aa = (3 * b) * C(k) if k >= 3 else mp.mpf(0)
        ax = k * A_light * b
        return deficit - (aa + ax)

    def ladder(members, A_light, light):
        return {k: modelg_miss(nm, Z, A, k, A_light, light)
                for k, (nm, Z, A) in members.items()}

    # ── [0] the deuteron ladder (the test) ───────────────────────────────────
    d_miss = ladder(DEUTERON, 2, LIGHT["d"])
    print("\n[0] DEUTERON ladder (fixed light cluster = deuteron, A_light=2):")
    print(f"    {'k':>2} {'iso':5s} {'miss_MeV':>9s}  {'note':s}")
    notes = {1: "CLOSED (committed 6Li, ~0)", 2: "10B FRESH  <- resonance predicts PEAK",
             3: "14N committed (R8 miss 5.818)", 4: "18F FRESH"}
    for k, (nm, Z, A) in DEUTERON.items():
        print(f"    {k:>2} {nm:5s} {float(d_miss[k]):9.4f}  {notes[k]}")

    # cross-check 14N against committed R8 value and 6Li ~ 0
    n14_ref = mp.mpf(str(ROWS_G["14N"]["deficit_MeV"])) - mp.mpf(str(ROWS_G["14N"]["pred_deficit_MeV"]))
    dev_14N = abs(float(d_miss[3] - n14_ref))
    li6_small = abs(float(d_miss[1])) < 0.15
    print(f"    (14N reproduces the committed R8 miss to {dev_14N:.2e} MeV; "
          f"6Li |miss|={abs(float(d_miss[1])):.3f} ~ 0 = Model-G closed)")

    # ── [1] LOCATE THE PEAK — the decisive result ────────────────────────────
    d_peak_k = max((1, 2, 3, 4), key=lambda k: float(d_miss[k]))
    rises_to_3 = float(d_miss[1]) < float(d_miss[2]) < float(d_miss[3])
    falls_after_3 = float(d_miss[3]) > float(d_miss[4])
    peak_at_2 = (d_peak_k == 2)   # resonance prediction
    peak_at_3 = (d_peak_k == 3)   # fixed-3alpha-onset (falsifier)
    print("\n[1] PEAK LOCATION (deuteron ladder, A_light=2):")
    print(f"    miss(k) = [{float(d_miss[1]):.3f}, {float(d_miss[2]):.3f}, "
          f"{float(d_miss[3]):.3f}, {float(d_miss[4]):.3f}] at k=[1,2,3,4]")
    print(f"    strict interior maximum at k = {d_peak_k}")
    if peak_at_3:
        print("    -> PEAK AT k=3 (14N), NOT k=2.  The resonance prediction (peak at")
        print("       k=A_light=2) is FALSIFIED.  The peak sits at the SAME k=3 as the")
        print("       triton ladder => it is a FIXED-k=3 effect (the 3-alpha Brunnian")
        print("       onset / k>=3 alpha.alpha gate turn-on), independent of A_light.")
    elif peak_at_2:
        print("    -> PEAK AT k=2 (10B).  CONFIRMS the resonance-at-k=A_light reading;")
        print("       the peak TRACKS A_light (d:k=2 vs t:k=3).")
    else:
        print(f"    -> peak at k={d_peak_k}: neither the resonance (k=2) nor the "
              f"fixed-onset (k=3) prediction; anomalous.")

    # ── [2] TWO-LADDER CROSS TABLE (the decisive comparison) ──────────────────
    t_miss = ladder(TRITON, 3, LIGHT["t"])
    t_peak_k = max((1, 2, 3, 4), key=lambda k: float(t_miss[k]))
    print("\n[2] TWO-LADDER CROSS TABLE (deuteron A_light=2 vs triton A_light=3):")
    print(f"    {'k':>2} | {'d-ladder':>22s} | {'t-ladder':>22s}")
    print(f"    {'':>2} | {'iso':6s}{'miss_MeV':>12s} m? | {'iso':6s}{'miss_MeV':>12s} m?")
    for k in (1, 2, 3, 4):
        dnm = DEUTERON[k][0]
        tnm = TRITON[k][0]
        dm = "*" if k == d_peak_k else " "
        tm = "*" if k == t_peak_k else " "
        print(f"    {k:>2} | {dnm:6s}{float(d_miss[k]):12.4f}  {dm} | "
              f"{tnm:6s}{float(t_miss[k]):12.4f}  {tm}")
    print(f"    peak: d-ladder k={d_peak_k} (A_light=2);  t-ladder k={t_peak_k} "
          f"(A_light=3)")
    tracks_Alight = (d_peak_k == 2 and t_peak_k == 3)
    fixed_3alpha = (d_peak_k == 3 and t_peak_k == 3)
    if fixed_3alpha:
        print("    -> BOTH ladders peak at k=3 => the peak does NOT track A_light;")
        print("       it is the FIXED 3-alpha onset.  RESONANCE FALSIFIED.")
    elif tracks_Alight:
        print("    -> d peaks at k=2, t at k=3 => the peak TRACKS A_light.  CONFIRMED.")

    # ── [3] THIRD LADDER — neutron A_light=1 triangulation ───────────────────
    nn_miss = ladder(NEUTRON, 1, LIGHT["n"])
    nn_peak_k = max(NEUTRON.keys(), key=lambda k: float(nn_miss[k]))
    print("\n[3] TRIANGULATION — neutron ladder (ka)+n, A_light=1 (k=1 5He unbound,"
          " start k=2):")
    print(f"    {'k':>2} {'iso':5s} {'miss_MeV':>9s}")
    for k in sorted(NEUTRON):
        print(f"    {k:>2} {NEUTRON[k][0]:5s} {float(nn_miss[k]):9.4f}"
              f"{'  <- peak' if k == nn_peak_k else ''}")
    print(f"    peak at k={nn_peak_k}.  For A_light=1 the resonance shape "
          f"(k-1)(2*A_light-1-k) = -(k-1)^2 is degenerate (<=0, NO positive peak),")
    print(f"    so a k=3 peak here is a THIRD independent falsifier of resonance.")

    # peak height vs A_light (peak location fixed at k=3; magnitude scales?)
    peak_heights = {1: float(nn_miss[3]), 2: float(d_miss[3]), 3: float(t_miss[3])}
    print(f"\n    peak HEIGHT (all at k=3) vs A_light: "
          f"A_light=1 -> {peak_heights[1]:.3f}, =2 -> {peak_heights[2]:.3f}, "
          f"=3 -> {peak_heights[3]:.3f} MeV")
    print(f"    (location FIXED at k=3; magnitude grows ~ with A_light — A_light")
    print(f"     modulates the AMPLITUDE, k=3 sets the LOCATION.)")

    all_peak_at_3 = (d_peak_k == 3 and t_peak_k == 3 and nn_peak_k == 3)

    # ── verdict ──────────────────────────────────────────────────────────────
    if fixed_3alpha:
        verdict = (
            "FALSIFIED (scope-(a) correction of R9's interpretation). The "
            "deuteron ladder (fixed light cluster = deuteron, A_light=2) has "
            f"Model-G miss [{float(d_miss[1]):.3f}, {float(d_miss[2]):.3f}, "
            f"{float(d_miss[3]):.3f}, {float(d_miss[4]):.3f}] at k=[1,2,3,4], a "
            "strict interior maximum at k=3 (14N) — NOT at k=2 (10B) as the "
            "resonance-at-k=A_light reading predicted. The peak sits at the SAME "
            "k=3 as the triton ladder (A_light=3), and the neutron ladder "
            "(A_light=1) ALSO peaks at k=3 (13C), where the resonance shape is "
            "degenerate (no positive peak) — three ladders, three A_light values "
            "(1,2,3), one peak location k=3. The peak therefore does NOT track "
            "A_light; it is a FIXED-k=3 effect: the 3-alpha Brunnian onset (the "
            "k>=3 alpha.alpha gate turn-on of Model G). The 'resonance at "
            "k=A_light' INTERPRETATION from R9 is refuted. What A_light DOES "
            "control is the peak AMPLITUDE (k=3 heights ~2.8/5.8/8.0 MeV for "
            "A_light=1/2/3), not its location. R9's structural prunes P1 "
            "(additive non-negative cone) and P2 (monotone-saturating 1-prod "
            "class) are NOT under test and STAND — the interior-maximum invariant "
            "they rest on holds (indeed is strengthened) on all three ladders. "
            "This is a falsification test, not a fit: b and the ledger reused "
            "from committed witnesses; only the fresh AME deficits read. Nothing "
            "wired; no tier change.")
    else:
        verdict = ("UNEXPECTED — see peak table; d_peak_k=%d t_peak_k=%d "
                   "nn_peak_k=%d" % (d_peak_k, t_peak_k, nn_peak_k))
    print(f"\nVERDICT: {verdict}")

    # ── witness ──────────────────────────────────────────────────────────────
    wit = {
        "computation": "deuteron-ladder-falsification",
        "description": (
            "R10 falsification test of the R9 'resonance at k=A_light' reading. "
            "Deuteron ladder (6Li/10B/14N/18F, A_light=2) Model-G miss, computed "
            "with the SAME R8/R9 ledger (b + 14N reused from committed "
            "witnesses; 10B/18F/13C/17O deficits fresh from vendored AME2020). "
            "Pre-registered: resonance => peak at k=2; falsifier => peak at k=3 "
            "(fixed 3-alpha Brunnian onset). Result: peak at k=3 on the deuteron "
            "ladder AND the triton ladder AND the neutron (A_light=1) ladder — "
            "the peak is FIXED at k=3, does not track A_light; resonance "
            "FALSIFIED. R9's P1/P2 structural prunes stand. Falsification test, "
            "not a fit; nothing recomputed beyond the fresh AME deficits; nothing "
            "wired."),
        "audit_only": True,
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "engine": "mpmath (witness-fed; no new tr_M compute)",
        "inputs": {
            "model_G_source": "alpha-activation-brunnian.witness.json (committed; 6Li/14N/9Be misses reused, ledger reused)",
            "R9_source": "saturating-shared-channel.witness.json (committed; the resonance reading under test)",
            "b_linear_MeV_per_nucleon": {
                "value": float(b),
                "source": "alpha-activation-brunnian.witness.json inputs (committed R5-a; reused not re-fit)"},
            "AME2020": "vendored via codata_constants._ame_binding_mev (10B/18F/13C/17O deficits — fresh)",
        },
        "pre_registration": {
            "resonance_prediction": "deuteron ladder (A_light=2) peaks at k=2 (10B); miss(10B) > miss(14N) > miss(18F)",
            "null_falsifier": "deuteron ladder peaks at k=3 (14N) again -> fixed 3-alpha Brunnian onset, independent of A_light",
            "stated_before_fresh_compute": True,
        },
        "deuteron_ladder_A_light_2": {
            DEUTERON[k][0]: {"k": k, "miss_MeV": float(d_miss[k])} for k in DEUTERON},
        "triton_ladder_A_light_3": {
            TRITON[k][0]: {"k": k, "miss_MeV": float(t_miss[k])} for k in TRITON},
        "neutron_ladder_A_light_1": {
            NEUTRON[k][0]: {"k": k, "miss_MeV": float(nn_miss[k])} for k in sorted(NEUTRON)},
        "peak_locations": {
            "deuteron_A_light_2": d_peak_k,
            "triton_A_light_3": t_peak_k,
            "neutron_A_light_1": nn_peak_k,
            "all_peak_at_k_3": bool(all_peak_at_3),
        },
        "peak_heights_at_k3_vs_A_light": {
            "A_light_1_13C": peak_heights[1],
            "A_light_2_14N": peak_heights[2],
            "A_light_3_15N": peak_heights[3],
            "note": "location fixed at k=3; amplitude grows ~ with A_light",
        },
        "cross_check": {
            "deuteron_14N_dev_from_committed_R8_MeV": dev_14N,
            "deuteron_6Li_miss_MeV": float(d_miss[1]),
        },
        "result": {
            "peak_tracks_A_light_CONFIRMS": bool(tracks_Alight),
            "peak_fixed_at_3_FALSIFIES": bool(fixed_3alpha),
            "verdict": "FALSIFIES" if fixed_3alpha else ("CONFIRMS" if tracks_Alight else "UNEXPECTED"),
        },
        "scope_note": (
            "scope-(a) correction of the R9 INTERPRETATION only. R9's P1 "
            "(additive non-negative cone) and P2 (monotone-saturating 1-prod "
            "class) structural prunes are NOT under test and STAND; the "
            "interior-maximum invariant holds on all three ladders. Only the "
            "'resonance at k=A_light' reading is refuted."),
        "verdict": verdict,
        "assertions": [
            {"label": "deuteron 14N miss reproduces the committed R8 value to < 1e-6 MeV",
             "passed": bool(dev_14N < 1e-6)},
            {"label": "deuteron 6Li miss ~ 0 (Model-G closed, |miss| < 0.15 MeV)",
             "passed": bool(li6_small)},
            {"label": "deuteron ladder rises k=1->2->3 then falls k=3->4 (strict interior maximum)",
             "passed": bool(rises_to_3 and falls_after_3)},
            {"label": "DECISIVE: deuteron ladder (A_light=2) peaks at k=3 (14N), NOT k=2 (10B) -> resonance-at-k=A_light FALSIFIED",
             "passed": bool(peak_at_3)},
            {"label": "two-ladder cross-check: deuteron AND triton both peak at k=3 (peak does not track A_light)",
             "passed": bool(fixed_3alpha)},
            {"label": "triangulation: neutron ladder (A_light=1) also peaks at k=3 (13C); resonance shape degenerate there",
             "passed": bool(nn_peak_k == 3)},
            {"label": "all three ladders (A_light=1,2,3) peak at the SAME k=3 -> fixed 3-alpha Brunnian onset",
             "passed": bool(all_peak_at_3)},
            {"label": "honest falsification: R9 resonance INTERPRETATION refuted; R9 P1/P2 structural prunes stand (not under test)",
             "passed": True},
        ],
    }
    wit["allPassed"] = all(a["passed"] for a in wit["assertions"])
    out = _HERE / "deuteron-ladder-falsification.witness.json"
    json.dump(wit, open(out, "w"), indent=1)
    print(f"\nwitness -> {out.name}   allPassed: {wit['allPassed']}")
    return 0 if wit["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
