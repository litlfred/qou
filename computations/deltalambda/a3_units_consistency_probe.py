#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a3_units_consistency_probe.py — the "1.6× A=3 near-miss" is dimensionally ill-posed AND
scale-ambiguous: repairing the pun leaves a gap spanning 1.66× overshoot .. 3.53× undershoot across
the unpinned C_knot=5.85. NOT a single "honest gap" (an earlier version's 3.53× was an over-claim,
corrected here). Corrects the corpus (#4364 / three-walls) AND the corpus-convention numbers in §2–3c
of this PR's earlier probes.

THE PUN (found in borromean_h9_magnitude_lift_probe.py:188)
-----------------------------------------------------------
That probe prints `target μ₃ = 0.4708 (dimensionless, read as MeV)` and then computes
`c₃/μ₃ = 0.63 → "~1.6× short"`. But the two quantities have DIFFERENT DIMENSIONS:

  * μ₃ = M(3) = ρ_strong(3) − ρ_grad(3) is DIMENSIONLESS — a ratio coefficient
    (ρ_strong(A) = B(A)/B(²H), ρ_grad(A) = [A]_q!/[2]_q!; ρ_strong(2)=1 confirms it is a pure ratio).
  * c₃ = E₀·(1−τ_Borr) is a genuine ENERGY in MeV (E₀ = m_e/(q₀(q₀−1)) ≈ 4.19 MeV).

Comparing 0.297 MeV to 0.4708 (dimensionless) as "0.63×" silently sets B(²H) = 1 MeV. The correct
conversion into the dimensionless simplex decomposition is c₃ ↦ c₃/B(²H):

  c₃(ratio) = c₃_MeV / B(²H) = 0.297 / 2.224566 = 0.13351.

THE GAP IS SCALE-AMBIGUOUS (self-correction of an earlier over-claim)
--------------------------------------------------------------------
An earlier version of this probe "corrected" the pun by dividing c₃ by the AME deuteron
(c₃/B_AME(²H) = 0.1335 ⇒ 3.53× undershoot) and reported 3.53× as "the honest gap." THAT WAS AN
OVER-CLAIM: it silently picked one of two defensible normalizations. The categorical binding scale is
NOT pinned to AME — the master formula B = m_e·|Σ_λ y_λ χ^λ sgn f^λ| predicts the DEUTERON itself at
only B_cat(²H) = 0.380 MeV vs AME 2.2246 (a −82.9% undershoot; C_knot = B_AME/B_cat = 5.852, EXPLICITLY
a FITTED deficit ratio = the open Δ_λ gate, `binding_energy_categorical_deuteron.py`). So there are two
normalizations, differing by exactly C_knot:

  A. c₃ / B_AME(²H) = 0.1335   ⇒ gap μ₃/that = 3.53×  UNDERshoot
  B. c₃ / B_cat(²H) = 0.781    ⇒ gap that/μ₃ = 1.66×  OVERshoot   (E₀/m_e cancels — scale-consistent)

Normalization B is the more principled one (the model's dimensionless ratio ρ_strong = B(A)/B(²H)
cancels the categorical scale, so the cluster should be divided by the model's OWN deuteron), but
NEITHER is rigorous: c₃ (a Borromean E₀·deficit, #4364) and B_cat(²H) (the master per-λ sum) are
DIFFERENT computations, so the true gap is not cleanly either. The robust statement:

  THE "1.6× A=3 NEAR-MISS" IS NOT A ROBUST NEAR-MISS. Once the dimensionally-ill-posed
  MeV-vs-dimensionless comparison (line 188) is repaired, the gap swings from a 1.66× OVERSHOOT to a
  3.53× UNDERSHOOT across the full C_knot = 5.85 factor — i.e. it is an artifact of the UNPINNED
  categorical binding scale. The one unambiguous object is C_knot itself: the master formula undershoots
  the deuteron by 5.85×, an explicitly FITTED (not derived) deficit ratio — THE open Δ_λ gate.

CONSEQUENCE — "how to improve binding": the fix is deriving C_knot (equivalently the Δ_λ magnitude)
from the categorical structure. It is currently a FIT (B_AME/(m_e·|sum|)); six ansätze + three walls
have failed to derive it. The A=3 "near-miss" gave a false sense of proximity — the real gate is the
5.85× deuteron deficit, unpinned. scope-(a) calibration; no fit.

STRICT anti-fit: c₃, μ₃, B_AME, B_cat consumed as fixed inputs; nothing wired. The corpus files (#4364,
three-walls, borromean_h9_magnitude_lift_probe.py:188) carry the pun — flagged for coordination. Exact
(mpmath). EXPLORATORY — audit + witness only.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

BH2 = mp.mpf("2.224566")         # B(²H) MeV (AME)
BCAT = mp.mpf("0.380132118905")  # categorical deuteron, master formula m_e·|Σ y_λ χ^λ sgn f^λ|
C3_MEV = mp.mpf("0.297")         # 3-body Borromean cluster, MeV (E₀·deficit, #4364)
MU3 = mp.mpf("0.4708")           # dimensionless 3-body simplex coefficient (AME ratio units)


def main() -> int:
    c_knot = BH2 / BCAT                              # deuteron deficit ratio (FITTED = Δ_λ gate)
    punned_gap = MU3 / C3_MEV                        # corpus: 0.297 MeV vs 0.4708 dimensionless
    # normalization A: divide c₃ by the AME deuteron
    c3_ratio_A = C3_MEV / BH2
    gap_A = MU3 / c3_ratio_A                          # 3.53× UNDERshoot
    # normalization B: divide c₃ by the CATEGORICAL deuteron (E₀/m_e cancels — scale-consistent)
    c3_ratio_B = C3_MEV / BCAT
    gap_B = c3_ratio_B / MU3                          # 1.66× OVERshoot
    norm_ratio = c3_ratio_B / c3_ratio_A             # = C_knot exactly

    result = {
        "the_pun": {
            "site": "borromean_h9_magnitude_lift_probe.py:188 — 'target μ₃ = 0.4708 (dimensionless, "
                    "read as MeV)'",
            "mu3_dimensionless": mp.nstr(MU3, 6),
            "c3_MeV": mp.nstr(C3_MEV, 6),
            "punned_gap_mu3_over_c3": mp.nstr(punned_gap, 6) + " ('1.6× near-miss')",
            "why_ill_posed": "c₃ is a genuine energy (E₀·deficit, E₀=m_e/(q₀(q₀−1))≈4.19 MeV); μ₃ is "
                             "dimensionless (ρ_strong−ρ_grad). Comparing them sets B(²H)=1 MeV.",
        },
        "the_open_gate_C_knot": {
            "B_cat_deuteron_MeV": mp.nstr(BCAT, 8),
            "B_AME_deuteron_MeV": mp.nstr(BH2, 8),
            "C_knot": mp.nstr(c_knot, 6),
            "status": "the master formula B=m_e·|Σ y_λ χ^λ sgn f^λ| undershoots the DEUTERON by 5.85×; "
                      "C_knot=B_AME/B_cat is an EXPLICITLY FITTED deficit ratio (not derived) = the "
                      "open Δ_λ gate (binding_energy_categorical_deuteron.py).",
        },
        "scale_ambiguity": {
            "normA_c3_over_B_AME": mp.nstr(c3_ratio_A, 8),
            "gap_A_undershoot": mp.nstr(gap_A, 6) + "× UNDERshoot",
            "normB_c3_over_B_cat": mp.nstr(c3_ratio_B, 8),
            "gap_B_overshoot": mp.nstr(gap_B, 6) + "× OVERshoot",
            "normalizations_differ_by_C_knot": bool(abs(norm_ratio - c_knot) < mp.mpf("1e-6")),
            "reading": "the two defensible normalizations differ by exactly C_knot=5.85, so the 'gap' "
                       "swings from a 1.66× OVERSHOOT (÷categorical deuteron, scale-consistent) to a "
                       "3.53× UNDERSHOOT (÷AME deuteron). The '1.6× near-miss' is NOT robust — it is an "
                       "artifact of the UNPINNED categorical binding scale. Neither normalization is "
                       "rigorous: c₃ (Borromean E₀·deficit) and B_cat (master per-λ sum) are different "
                       "computations.",
        },
        "verdict": {
            "classification": "scope-(a) CALIBRATION + SELF-CORRECTION: the '1.6× A=3 near-miss' is "
                              "dimensionally ill-posed (c₃ MeV vs μ₃ dimensionless, line 188). Repairing "
                              "it does NOT give a single 'honest gap' — it gives a SCALE-AMBIGUOUS range "
                              "spanning C_knot=5.85 (1.66× overshoot .. 3.53× undershoot), because the "
                              "categorical binding scale is unpinned. (An earlier version of this probe "
                              "reported 3.53× as 'the honest gap'; that picked one normalization and was "
                              "an over-claim, corrected here.) The one unambiguous object is C_knot "
                              "itself — the 5.85× deuteron deficit, explicitly FITTED = the open Δ_λ "
                              "gate.",
            "how_to_improve_binding": "derive C_knot (the Δ_λ magnitude) from the categorical structure. "
                                      "It is currently a FIT B_AME/(m_e·|sum|); six ansätze + three walls "
                                      "have failed. The A=3 'near-miss' gave a false sense of proximity.",
            "anti_fit": "c₃, μ₃, B_AME, B_cat consumed as fixed inputs; nothing wired. Corpus files "
                        "(#4364, three-walls, borromean probe:188) carry the pun — flagged for coord.",
        },
    }

    this = Path(__file__).resolve()
    witness = {
        "schema": "witness/v1",
        "producer": str(this.relative_to(ROOT)),
        "computation": "a3-units-consistency",
        "description": (
            "The '1.6× A=3 magnitude near-miss' is dimensionally ill-posed AND scale-ambiguous. The "
            "3-body cluster c₃=0.297 is a genuine ENERGY (E₀·deficit) compared directly to the "
            "DIMENSIONLESS μ₃=0.4708 (borromean probe:188 admits 'μ₃ dimensionless, read as MeV'). "
            "Repairing the pun does NOT give one 'honest gap': the categorical binding scale is unpinned "
            "— the master formula undershoots the DEUTERON by 5.85× (C_knot=B_AME/B_cat, an explicitly "
            "FITTED deficit ratio = the open Δ_λ gate). Normalizing c₃ by the AME deuteron gives a 3.53× "
            "UNDERSHOOT; by the categorical deuteron (scale-consistent, E₀/m_e cancels) a 1.66× "
            "OVERSHOOT — the two differ by exactly C_knot=5.85. So the near-miss is an artifact of the "
            "unpinned scale, not a robust proximity. (Self-correction: an earlier version reported 3.53× "
            "as 'the honest gap' — that picked one normalization and over-claimed.) The unambiguous "
            "object is C_knot itself; deriving it (the Δ_λ magnitude) is 'how to improve binding' and is "
            "currently a FIT (six ansätze + three walls failed). scope-(a) calibration; no fit; nothing "
            "wired; exact (mpmath). Corpus files carry the pun — flagged for coordination."),
        "audit_only": True,
        "tier": "scope-(a) units-consistency + scale-ambiguity calibration (self-correction); no fit",
        "scriptHash": hashlib.sha256(this.read_bytes()).hexdigest()[:16],
        "result": result,
        "context": {
            "axis": "Δ_λ / A=3 magnitude — units consistency of the target",
            "builds_on": "borromean_h9_magnitude_lift_probe.py:188 (the pun), #4364, three-walls, "
                         "this PR's mu3/a3/a4 probes",
            "no_fit": True,
        },
    }
    try:
        witness["scriptCommitSha"] = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", str(this)],
            cwd=this.parent, text=True).strip() or "uncommitted"
    except Exception:
        witness["scriptCommitSha"] = "uncommitted"
    out = HERE / "a3-units-consistency.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str) + "\n")

    print("=== the '1.6× A=3 near-miss' is dimensionally ill-posed AND scale-ambiguous ===")
    print(f"PUN (borromean probe:188): c₃ = {mp.nstr(C3_MEV,4)} MeV  vs  μ₃ = {mp.nstr(MU3,4)} "
          f"(DIMENSIONLESS)  →  punned gap {mp.nstr(punned_gap,5)}× ('1.6× near-miss')")
    print()
    print(f"OPEN GATE: master formula undershoots the DEUTERON — B_cat={mp.nstr(BCAT,5)} vs "
          f"B_AME={mp.nstr(BH2,5)} MeV  ⇒  C_knot = {mp.nstr(c_knot,5)} (FITTED = Δ_λ gate)")
    print()
    print(f"  norm A  c₃/B_AME = {mp.nstr(c3_ratio_A,5)}   → gap μ₃/that = {mp.nstr(gap_A,5)}× UNDERshoot")
    print(f"  norm B  c₃/B_cat = {mp.nstr(c3_ratio_B,5)}   → gap that/μ₃ = {mp.nstr(gap_B,5)}× OVERshoot "
          f"(scale-consistent)")
    print(f"  the two normalizations differ by EXACTLY C_knot = {mp.nstr(norm_ratio,5)}")
    print()
    print("VERDICT (scope-a, SELF-CORRECTION of an earlier 3.53× over-claim): the near-miss is NOT "
          "robust — repairing the pun leaves a scale-ambiguous range (1.66× overshoot .. 3.53× "
          "undershoot) spanning the unpinned C_knot=5.85. The real open object is C_knot itself — "
          "deriving it (the Δ_λ magnitude) is 'how to improve binding', currently a FIT. Nothing wired.")
    print(f"witness -> {out.name}")

    assert result["scale_ambiguity"]["normalizations_differ_by_C_knot"], "norms must differ by C_knot"
    assert gap_A > 3 and gap_A < 4, "AME-normalized gap must be ~3.5× undershoot"
    assert gap_B > 1 and gap_B < 2, "categorical-normalized gap must be ~1.66× overshoot"
    assert c_knot > 5 and c_knot < 6, "C_knot must be ~5.85"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
