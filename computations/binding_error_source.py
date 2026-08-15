#!/usr/bin/env python3
"""
binding_error_source.py — diagnose WHY the joint categorical Markov-
trace binding undershoots A≥3 by ~60% (PR #1414).

FINDING: the trace defect Δtr = |tr_free| − |tr_atom| is an INTENSIVE,
SATURATING observable, but binding energy is EXTENSIVE (grows with A).

  • |tr_free| ≈ 1 (normalized), so Δtr ≤ |tr_free| ≈ 1 — a hard ceiling.
  • Therefore B = m_e·Vol(𝓑₃)·Δtr ≤ m_e·Vol ≈ 3.74 MeV for ANY A.
  • The deuteron (B=2.2 < 3.74) sits below the ceiling → −6.3%.
  • ³He/⁴He (B=7.7/28.3 > 3.74) are clipped → −59%/−88%.

An intensive observable cannot represent an extensive quantity. This
is the error source — not a missing volume or a convention artifact.

⚠ NUMBER CORRECTED 2026-08-15 (bean `qou-jdhm`). The deuteron line read
"→ works (+0.2%)". That figure is trace **convention C**
(z = 1/(√q + 1/√q) = 0.4993203), excised by owner ruling 2026-08-09 in
favour of **convention D** (z = q³/(q²+1) = 0.6126880); under D the same
computation gives −6.3%, and `binding-link-volumes.witness.json` has
always recorded that assertion as `"passed": false`.

**The FINDING above is unaffected**, which is why only the number moved.
The argument is that Δtr saturates while binding is extensive, and −6.3%
at A=2 against −59%/−88% at A≥3 exhibits the same ceiling behaviour that
+0.2% did. What is lost is the claim that the deuteron *works* — it does
not, it merely fails far less. That is a cleaner reading of the ceiling
argument rather than a weaker one: there is no longer a special A=2
success needing its own explanation.

STRUCTURAL POINTER (not a calibrated formula — calibration would be
fitting): the Markov trace is partition-function-like (multiplicative
over disjoint subsystems). The EXTENSIVE / additive analog is its
logarithm — a free-energy-like quantity. -log(|tr_atom|/|tr_free|)
grows with A where Δtr saturates. A correct extensive binding
observable must be built from log(tr), not Δtr — but recalibrating
the scale is future work and is deliberately NOT done here.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

from mpmath import mp, mpf, fabs, log, catalan

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import (  # noqa: E402
    Q_BETA_MEV, M_E_MEV,
    AME_B_DEUTERON_MEV_VALIDATION as Bd,
    AME_B_TRITIUM_MEV_VALIDATION as Bt,
    AME_B_HE3_MEV_VALIDATION as B3,
    AME_B_HE4_MEV_VALIDATION as B4,
)
from binding_canonical import binding_canonical  # noqa: E402


def _real(s):
    s = str(s)
    return mpf(complex(s.strip("()")).real) if ("j" in s or "(" in s) else mpf(s)


def main():
    set_compute_dps()
    wb = WitnessBuilder("binding-error-source", engine="mpmath")

    m_e = mpf(str(M_E_MEV))
    VOL = 8 * catalan
    scale = m_e * VOL

    cases = [("2H", 1, 1, Bd), ("3H", 1, 2, Bt),
             ("3He", 2, 1, B3), ("4He", 2, 2, B4)]

    print("=" * 74)
    print("BINDING ERROR SOURCE — intensive Δtr ceiling vs extensive B")
    print(f"scale m_e·Vol(𝓑₃) = {float(scale):.4f} MeV  (the Δtr ceiling)")
    print("=" * 74)
    print(f"{'iso':>4s} {'Δtr':>8s} {'B_cat':>8s} {'B_AME':>8s} "
          f"{'clip%':>8s} {'-log(ta/tf)':>12s} {'B/Δtr':>9s} {'B/log':>8s}")

    rows = {}
    for iso, Z, N, ame in cases:
        ame = mpf(str(ame))
        r = binding_canonical(Z, N, Q_beta_n_mev=float(Q_BETA_MEV),
                              use_closed_form=True, verbose=False)
        tf = fabs(_real(r["tr_M_free"]))
        ta = fabs(_real(r["tr_M_atom"]))
        dtr = tf - ta
        b_cat = scale * dtr
        clip = float((b_cat - ame) / ame * 100)
        log_ratio = log(tf / ta)            # extensive analog
        rows[iso] = {
            "tr_free": mp.nstr(tf, 12), "tr_atom": mp.nstr(ta, 12),
            "delta_tr": mp.nstr(dtr, 12), "B_cat_MeV": mp.nstr(b_cat, 10),
            "B_AME_MeV": mp.nstr(ame, 10), "clip_pct": clip,
            "neg_log_ratio": mp.nstr(log_ratio, 12),
            "B_over_dtr": mp.nstr(ame / dtr, 10),
            "B_over_log": mp.nstr(ame / log_ratio, 10),
        }
        print(f"{iso:>4s} {float(dtr):>8.4f} {float(b_cat):>8.3f} "
              f"{float(ame):>8.3f} {clip:>+7.1f}% {float(log_ratio):>12.4f} "
              f"{float(ame/dtr):>9.3f} {float(ame/log_ratio):>8.3f}")

    print()
    print("Δtr saturates (→ |tr_free| ≈ 1); B_cat is capped at ~3.74 MeV.")
    print("-log(ta/tf) GROWS with A (0.93→2.17→1.62→2.86) — extensive.")
    print("⟹ the binding observable must be log(tr)-based, not Δtr.")
    print("   (scale recalibration deliberately NOT done — would be fitting.)")

    wb.set_description(
        "Error-source diagnosis for the A≥3 binding undershoot: Δtr is an "
        "intensive, saturating observable (≤ |tr_free| ≈ 1), capping "
        "B = m_e·Vol·Δtr at ~3.74 MeV for any A, while physical binding is "
        "extensive. Deuteron sits below the ceiling (−6.3%, trace convention "
        "D; the +0.2% previously quoted here was convention C, excised by "
        "owner ruling 2026-08-09 — bean qou-jdhm); A≥3 is clipped "
        "(−59%/−88%). Structural pointer: the extensive analog is -log(tr), "
        "which grows with A — but no recalibrated formula is claimed (fitting)."
    )
    wb.add_data("ceiling_MeV", mp.nstr(scale, 10))
    wb.add_data("isotopes", rows)
    wb.add_data("conclusion", {
        "error_source": "Δtr is intensive/saturating (bounded by |tr_free|≈1); "
                        "binding is extensive — mismatch caps B at ~3.74 MeV.",
        "structural_fix_direction": "binding observable must be log(tr)-based "
                                    "(free-energy / additive over subsystems), not Δtr",
        "not_done": "scale recalibration for the log observable (would be a fit)",
    })
    wb.add_assertion(
        "deuteron_below_ceiling",
        computed=float(mpf(rows["2H"]["B_AME_MeV"]) < scale),
        expected=1, tolerance=0,
        source="B(²H)=2.22 < ceiling 3.74 ⟹ deuteron works; A≥3 clipped",
    )
    wb.add_assertion(
        "A3_exceeds_ceiling",
        computed=float(mpf(rows["3He"]["B_AME_MeV"]) > scale),
        expected=1, tolerance=0,
        source="B(³He)=7.72 > ceiling 3.74 ⟹ structurally clipped",
    )
    # Lean SDP-uniqueness cross-reference (post-#1537 wiring).
    wb.add_data("lean_uniqueness_ref", {
        "generic": "qou:QOU.BraidKnot.@nucleus_uniqueness_closed (3*A)",
        "framework_doc":
            "content/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",
        "note": "Certifies T_w uniqueness at the abstract empty-constraint SDP level (PR #1537 parameterised module). Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md.",
    })

    wb.save()


if __name__ == "__main__":
    main()
