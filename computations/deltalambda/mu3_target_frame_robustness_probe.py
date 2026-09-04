#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mu3_target_frame_robustness_probe.py — is the μ₃ (A=3 magnitude) TARGET frame-robust,
or is the "1.6× A=3 magnitude gap" an artefact of the subtracted-baseline convention?

Context (all consumed as structure/targets; nothing re-derived, nothing inverted)
---------------------------------------------------------------------------------
The A=3 magnitude gate is stated as a 1.6× near-miss: the derived 3-body cluster
c₃ = +0.297 MeV = 0.63× μ₃ (`BorromeanMagnitudeLift` #4364), where the TARGET is the
3-body simplex coefficient of the graded-subtracted residual
(`deltalambda_kappa_interface_residual_simplex_probe.py`, #4320):

    M(A)   = ρ_strong(A) − ρ_grad(A),     ρ_grad(A) = [A]_q!/[2]_q! = ∏_{k=3}^{A} [k]_q
    μ₂ = M(2) = 0  (deuteron self-reference, DERIVED)
    μ₃ = M(3) − 3·μ₂ = M(3) = ρ_strong(3) − ρ_grad(3) ≈ +0.4708.

THE FRAGILITY THIS PROBE MEASURES
---------------------------------
μ₃ = ρ_strong(3) − ρ_grad(3) is a SMALL residual (≈0.47) that is the DIFFERENCE of two
O(3.5) quantities (ρ_strong(3)≈3.81, ρ_grad(3)≈3.34). That is exactly the structure
that made g₂ = 1 + r frame-flattered (r swung 12× under equally-motivated conventions,
PR #4319 thread): a small difference of large numbers inherits an AMPLIFIED sensitivity
to any convention that shifts the subtracted baseline —

    relative-sensitivity(μ₃ ← ρ_grad(3)) = ρ_grad(3)/μ₃ ≈ 3.34/0.47 ≈ 7×,

so a 1% change in the baseline moves μ₃ by ≈7%. Every sibling is trying to CLOSE the
1.6× gap ASSUMING μ₃ is the target. This probe asks the orthogonal question no sibling
is asking: does μ₃ (hence the "1.6× gap") swing under equally-legitimate choices of the
subtracted A-scaling baseline, the way g₂'s r did?

THE KNOBS (what is frame-INDEPENDENT vs convention-DEPENDENT)
------------------------------------------------------------
  * frame-INDEPENDENT (physical): the AME ratios ρ_strong(A)=B(A)/B(²H) — fixed data.
  * convention-DEPENDENT knob 1 (BIG): which categorical A-scaling is the subtracted
    baseline ρ_grad. Three legitimate, deuteron-normalized (ρ_grad(2)=1) choices:
      (G) graded coinvariant dimension  ρ_grad(A)=∏[k]_q,  [k]_q=1+q+…+q^{k-1} (CORPUS/#4300)
      (Q) balanced quantum dimension    ρ_grad(A)=∏[k]_q^bal, [k]^bal=q^{k-1}+…+q^{-(k-1)}
      (C) classical dimension (q→1)     ρ_grad(A)=∏ k
  * convention-DEPENDENT knob 2 (small): ρ_strong isospin/Coulomb correction —
    corrected 3.8128 (#3986/#3990) vs raw B(³H)/B(²H)=8.482/2.224≈3.814.

HONEST NUANCE (not overclaiming): the CORPUS choice (G) is the more-motivated one — it is
literally THE graded coinvariant dimension (the coinvariant-algebra Poincaré series,
#4300); (Q) is a quantum dimension and (C) the classical limit. They are DIFFERENT
categorical objects, not interchangeable definitions of one object. So this is NOT the
g₂ situation of several equivalent-looking definitions of the SAME object. What it IS: the
framework does not force the subtracted "smooth part" to be the graded dimension rather
than the quantum/classical dimension; a different principled starting baseline gives a
different μ₃. The measured spread quantifies how baseline-CLASS-relative the target is.

Pre-registered verdict rule (report honestly either way):
  * μ₃ spread ≪ the 1.6× gap  ⇒ target well-defined; the gate is a real 1.6× (scope-a +).
  * μ₃ spread ≳ the 1.6× gap  ⇒ the "1.6× A=3 magnitude gap" is baseline-class-relative,
    not absolute — closure attempts must state their baseline; a reviewer choosing (Q)/(C)
    sees a different gap. Scope-(a) caveat, NOT a refutation of the principled (G) route.

STRICT anti-fit: ρ_strong, c₃, AME, CODATA enter ONLY as fixed targets — never inverted
into a canonical weight; no q, no baseline solved from the data. Exact (mpmath).
EXPLORATORY — audit + witness only; no fit, nothing wired.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

import mpmath as mp

mp.mp.dps = 60

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

# --- substrate q0 sourced from the jet-filtration witness, which now RESOLVES its
# --- own pin (proton) rather than freezing the superseded muon literal (qou-1c4y) ----
JET_WITNESS = HERE / "deltalambda-jet-filtration-magnitude.witness.json"
_jw = json.loads(JET_WITNESS.read_text())
Q0 = mp.mpf(str(_jw["parameters"]["q0"]))          # whatever the upstream resolved

# --- derived cluster prediction + AME targets (consumed only; never inverted) ----------
C3_CLUSTER = mp.mpf("0.297")                        # BorromeanMagnitudeLift #4364, 0-fit
RHO_STRONG_CORR = {2: mp.mpf(1), 3: mp.mpf("3.8128"), 4: mp.mpf("13.0316")}   # #3986/#3990
RHO_STRONG_RAW = {2: mp.mpf(1),                                               # raw AME ratios
                  3: mp.mpf("8.482") / mp.mpf("2.224"),
                  4: mp.mpf("28.296") / mp.mpf("2.224")}


def q_unbal(k, q):
    """graded / coinvariant [k]_q = 1 + q + … + q^{k-1} (Poincaré series factor)."""
    return sum(q ** j for j in range(k))


def q_bal(k, q):
    """balanced quantum [k]_q = q^{k-1} + q^{k-3} + … + q^{-(k-1)} = (q^k−q^{-k})/(q−q^{-1})."""
    return sum(q ** (k - 1 - 2 * j) for j in range(k))


def q_classical(k, q):
    """classical dimension k (q→1 limit)."""
    return mp.mpf(k)


BASELINES = {
    "G_graded_coinvariant": (q_unbal, "∏[k]_q, [k]=1+q+…+q^{k-1}  (CORPUS, #4300 graded dim)"),
    "Q_balanced_quantum":   (q_bal,   "∏[k]_q^bal, [k]=q^{k-1}+…+q^{-(k-1)}  (quantum dim)"),
    "C_classical":          (q_classical, "∏k  (q→1 classical dim)"),
}


def rho_grad(qint, A, q):
    """ρ_grad(A) = ∏_{k=3}^{A} [k]_q ;  ρ_grad(2)=empty product=1 (deuteron self-reference)."""
    r = mp.mpf(1)
    for k in range(3, A + 1):
        r *= qint(k, q)
    return r


def simplex(M):
    """exact 0-parameter simplex (Mayer) coefficients over derived C(A,k) counts."""
    from math import comb
    mu2 = M[2]                                    # C(2,2)=1
    mu3 = M[3] - comb(3, 2) * mu2                 # C(3,2)=3
    mu4 = M[4] - comb(4, 2) * mu2 - comb(4, 3) * mu3   # C(4,2)=6, C(4,3)=4
    return mu2, mu3, mu4


def run(rho_strong, label):
    rows = {}
    exact = {}   # keep exact mp.mpf values for aggregation; strings are for serialization only
    for key, (qint, desc) in BASELINES.items():
        rg = {A: rho_grad(qint, A, Q0) for A in (2, 3, 4)}
        M = {A: rho_strong[A] - rg[A] for A in (2, 3, 4)}
        mu2, mu3, mu4 = simplex(M)
        exact[key] = {"mu3": mu3, "mu4": mu4, "gap_factor": mu3 / C3_CLUSTER}
        rows[key] = {
            "desc": desc,
            "rho_grad3": mp.nstr(rg[3], 10), "rho_grad4": mp.nstr(rg[4], 10),
            "mu2": mp.nstr(mu2, 6), "mu3": mp.nstr(mu3, 10), "mu4": mp.nstr(mu4, 10),
            "mu2_is_zero": bool(abs(mu2) < mp.mpf("1e-40")),
            "mu3_sign_pos": bool(mu3 > 0), "mu4_sign_neg": bool(mu4 < 0),
            "gap_ratio_c3_over_mu3": mp.nstr(C3_CLUSTER / mu3, 8),
            "gap_factor_mu3_over_c3": mp.nstr(mu3 / C3_CLUSTER, 8),
            # amplification: relative sensitivity of μ₃ to a shift in the baseline ρ_grad(3)
            "amplification_rhograd3_over_mu3": mp.nstr(rg[3] / mu3, 8),
        }
    # aggregate from the EXACT mpf values (never from the nstr-rounded strings)
    mu3s = [exact[k]["mu3"] for k in BASELINES]
    mu4s = [exact[k]["mu4"] for k in BASELINES]
    gaps = [exact[k]["gap_factor"] for k in BASELINES]
    return {
        "rho_strong_convention": label,
        "per_baseline": rows,
        "mu3_min": mp.nstr(min(mu3s), 8), "mu3_max": mp.nstr(max(mu3s), 8),
        "mu3_spread_factor": mp.nstr(max(mu3s) / min(mu3s), 6),
        "mu4_min": mp.nstr(min(mu4s), 8), "mu4_max": mp.nstr(max(mu4s), 8),
        "mu4_spread_factor": mp.nstr(min(mu4s) / max(mu4s), 6),  # both negative
        "gap_factor_min": mp.nstr(min(gaps), 6), "gap_factor_max": mp.nstr(max(gaps), 6),
        "signs_robust_mu3pos_mu4neg": bool(all(rows[k]["mu3_sign_pos"] and rows[k]["mu4_sign_neg"]
                                               for k in BASELINES)),
        # boolean computed from EXACT mpf (not re-parsed strings): does the μ₃ baseline-class
        # spread exceed the corpus-G gap factor it targets?
        "mu3_spread_exceeds_corpus_gap": bool((max(mu3s) / min(mu3s))
                                              > exact["G_graded_coinvariant"]["gap_factor"]),
        # exact mp.mpf values (NOT nstr-rounded) for downstream knob computations in main()
        "_exact": exact,
    }


def main() -> int:
    corr = run(RHO_STRONG_CORR, "isospin/Coulomb-corrected (#3986/#3990)")
    raw = run(RHO_STRONG_RAW, "raw AME B(A)/B(²H)")

    # ρ_strong-convention knob (small): μ₃ under corrected vs raw, corpus baseline (G).
    # Read EXACT mp.mpf values (not nstr-rounded strings) so the "exact (mpmath)" claim holds.
    mu3_corr_G = corr["_exact"]["G_graded_coinvariant"]["mu3"]
    mu3_raw_G = raw["_exact"]["G_graded_coinvariant"]["mu3"]
    rho_strong_knob_pct = mp.nstr(100 * abs(mu3_raw_G - mu3_corr_G) / mu3_corr_G, 4)

    gap_factor_corpus = corr["_exact"]["G_graded_coinvariant"]["gap_factor"]
    spread_exceeds_gap = corr["mu3_spread_exceeds_corpus_gap"]   # exact-mpf boolean from run()
    corr.pop("_exact", None)   # drop the non-serializable exact-mpf helper before it enters the witness
    raw.pop("_exact", None)

    # --- the FRAME-INDEPENDENT statement: accuracy on the physical ratio B(³H)/B(²H) ---------
    # The corpus model's total A=3 prediction is ρ_grad_G(3) + c₃ (graded baseline + derived
    # 3-body cluster; C(3,3)=1 so the cluster enters M(3) directly). The absolute miss Δ against
    # the physical ratio ρ_strong(3) is baseline-INDEPENDENT data on one side, and it is the SAME
    # Δ whether framed as a fraction of the full ratio (physical) or of the small residual μ₃
    # (the '1.6× gap'). The residual framing merely amplifies the same Δ by ρ_strong(3)/μ₃.
    rg3_G = q_unbal(3, Q0)                                   # ρ_grad_G(3)
    model_full_ratio = rg3_G + C3_CLUSTER                   # corpus model's B(³H)/B(²H) prediction
    rho3 = RHO_STRONG_CORR[3]
    delta_abs = rho3 - model_full_ratio                     # absolute miss (ratio units)
    mu3_G = mu3_corr_G
    frame_independent = {
        "physical_observable": "B(³H)/B(²H) = ρ_strong(3)",
        "rho_strong3": mp.nstr(rho3, 8),
        "model_prediction_rho_grad_plus_c3": mp.nstr(model_full_ratio, 8),
        "absolute_miss_delta": mp.nstr(delta_abs, 8),
        "miss_pct_of_physical_ratio": mp.nstr(100 * delta_abs / rho3, 6),
        "miss_pct_of_residual_mu3": mp.nstr(100 * delta_abs / mu3_G, 6),
        "framing_amplification_rho3_over_mu3": mp.nstr(rho3 / mu3_G, 6),
        "reading": "the '1.6× gap on μ₃' (model reaches 0.63·μ₃) is the SAME absolute miss Δ as a "
                   "~4.6% shortfall on the physical ratio B(³H)/B(²H); the residual framing "
                   "amplifies Δ by ρ_strong(3)/μ₃ ≈ 8×. The frame-INDEPENDENT accuracy statement is "
                   "the % on the physical ratio, not the multiplicative gap on the small residual.",
    }

    verdict = {
        "mu3_baseline_class_spread_factor": corr["mu3_spread_factor"],
        "the_1p6x_gap_factor_corpus_G": mp.nstr(gap_factor_corpus, 6),
        "baseline_spread_exceeds_the_gap": spread_exceeds_gap,
        "rho_strong_correction_knob_pct_of_mu3": rho_strong_knob_pct,
        "signs_robust": corr["signs_robust_mu3pos_mu4neg"],
        "classification":
            "scope-(a) CAVEAT (not a refutation): μ₃ (hence the '1.6× A=3 magnitude gap') "
            "is baseline-CLASS-relative. The SIGNS (μ₃>0, μ₄<0) are robust across the graded / "
            "quantum / classical A-scalings, but the MAGNITUDE μ₃ swings by the reported spread "
            "factor — comparable to or exceeding the 1.6× gap itself. Because μ₃ = ρ_strong(3) − "
            "ρ_grad(3) is a small difference of two O(3.5) numbers, it inherits an ≈7× amplified "
            "sensitivity to the subtracted baseline (the same fragility as g₂=1+r). The corpus "
            "baseline (G) is the more-motivated one (it IS the graded coinvariant dimension, "
            "#4300), so this does NOT refute the (G) route — it flags that closure attempts must "
            "state they close the gap to the graded-dimension-referenced μ₃; a reviewer picking "
            "the quantum-dimension (Q) reference sees a different gap.",
        "anti_fit": "ρ_strong / c₃ / AME / CODATA consumed only as fixed targets; no q, no "
                    "baseline inverted. μ₂=0 (deuteron self-ref) preserved by every baseline. "
                    "Nothing wired.",
    }

    result = {
        "substrate": {"q0": mp.nstr(Q0, 40), "source": "jet-filtration witness (deltalambda-jet-filtration-magnitude), q0Anchor=proton. Label corrected 2026-09-04 from 'muon-canonical' (bean qou-9ugp): the upstream resolves to the proton pin 1.1099785827513808..., so this witness named a layer it does not evaluate at while stamping q0Anchor=proton one field away."},
        "c3_cluster_prediction_MeV": mp.nstr(C3_CLUSTER, 6),
        "corrected_rho_strong": corr,
        "raw_rho_strong": raw,
        "frame_independent_full_ratio": frame_independent,
        "verdict": verdict,
    }

    payload = {
        "computation": "mu3-target-frame-robustness",
        "description": (
            "Frame-robustness of the μ₃ (A=3 magnitude) target. μ₃ = ρ_strong(3) − ρ_grad(3) "
            "is a small residual (≈0.47) that is a difference of two O(3.5) numbers, so — like "
            "g₂=1+r — it inherits an ≈7× amplified sensitivity to the subtracted baseline. "
            "Measured across three legitimate deuteron-normalized A-scaling baselines (graded "
            "coinvariant dimension = CORPUS #4300, balanced quantum dimension, classical q→1) "
            "the SIGNS (μ₃>0, μ₄<0) are robust but μ₃'s MAGNITUDE swings by a factor comparable "
            "to / exceeding the 1.6× gap the closure attempts target. Hence the '1.6× A=3 "
            "magnitude gap' is baseline-CLASS-relative, not absolute. scope-(a) CAVEAT (not a "
            "refutation of the principled graded-dimension route): closure attempts must state "
            "their baseline. Anti-fit STRICT; nothing wired; exact (mpmath)."),
        "audit_only": True,
        "tier": "scope-(a) frame-robustness measurement (baseline-class spread of the μ₃ target); "
                "no fit; nothing wired",
        "result": result,
        "context": {
            "axis": "Δ_λ / A=3 magnitude gate — is the target frame-robust?",
            "builds_on": "#4320 (simplex μ₃), #4364 (c₃=0.63μ₃ lift), #4300 (graded dim), "
                         "damping-wall (sign robustness), the g₂/r frame-artifact thread (#4319)",
            "no_fit": True,
        },
    }

    # ---- witness (schema/v1, matching the sibling deltalambda probes) ----
    this = Path(__file__).resolve()
    witness = {
        "schema": "witness/v1",
        "producer": str(this.relative_to(ROOT)),   # repo-root-relative (matches sibling Δ_λ witnesses)
        "computation": payload["computation"],
        "description": payload["description"],
        "audit_only": True,
        "tier": payload["tier"],
        "scriptHash": hashlib.sha256(this.read_bytes()).hexdigest()[:16],
        "result": result,
        "context": payload["context"],
    }
    try:
        witness["scriptCommitSha"] = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", str(this)],
            cwd=this.parent, text=True).strip() or "uncommitted"
    except Exception:
        witness["scriptCommitSha"] = "uncommitted"
    out = HERE / "mu3-target-frame-robustness.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. This producer DOES read q0 (from the
    # jet-filtration witness), so the anchor is resolved and stamped, not suppressed.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    # q0_anchor was `False`, i.e. "this witness carries no q0-dependent field".
    # Untrue: q0 is read from the jet-filtration witness at module scope and
    # every quantity below is a function of it. The false declaration DELETED
    # the anchor stamp on every run, converting a visible Q0_FLIP into a silent
    # Q0_ANCHOR_MISSING (bean qou-1c4y).
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None)
    out.write_text(json.dumps(witness, indent=2, default=str) + "\n")

    # ---- console report ----
    print("=== μ₃ (A=3 magnitude) target frame-robustness ===")
    print(f"q0 = {mp.nstr(Q0, 30)}  (resolved pin)     c₃ cluster = {mp.nstr(C3_CLUSTER,4)} MeV")
    print(f"μ₃ = ρ_strong(3) − ρ_grad(3): SMALL residual = difference of two O(3.5) numbers")
    print()
    print("baseline (corrected ρ_strong)      ρ_grad(3)   μ₃        gap c₃/μ₃   amp ρ_grad3/μ₃")
    for k, (_, desc) in BASELINES.items():
        r = corr["per_baseline"][k]
        print(f"  {k:24s} {r['rho_grad3']:>9s}  {r['mu3']:>9s}  {r['gap_ratio_c3_over_mu3']:>8s}   "
              f"{r['amplification_rhograd3_over_mu3']:>8s}")
    print()
    print(f"μ₃ baseline-class SPREAD FACTOR = {corr['mu3_spread_factor']}× "
          f"(min {corr['mu3_min']} … max {corr['mu3_max']})")
    print(f"the '1.6× gap' factor (corpus G) = {mp.nstr(gap_factor_corpus,5)}×")
    print(f"ρ_strong correction knob = {rho_strong_knob_pct}% of μ₃ (small)")
    print(f"signs robust (μ₃>0, μ₄<0 all baselines): {corr['signs_robust_mu3pos_mu4neg']}")
    print()
    print("FRAME-INDEPENDENT statement (physical ratio B(³H)/B(²H)):")
    print(f"  model = ρ_grad_G(3)+c₃ = {frame_independent['model_prediction_rho_grad_plus_c3']}"
          f"  vs  ρ_strong(3) = {frame_independent['rho_strong3']}")
    print(f"  same miss Δ={frame_independent['absolute_miss_delta']}: "
          f"{frame_independent['miss_pct_of_physical_ratio']}% of the physical ratio  "
          f"=  {frame_independent['miss_pct_of_residual_mu3']}% of the residual μ₃  "
          f"(framing amplification {frame_independent['framing_amplification_rho3_over_mu3']}×)")
    print()
    print(f"VERDICT: baseline-class spread ({corr['mu3_spread_factor']}×) "
          f"{'≳' if spread_exceeds_gap else '<'} the 1.6× gap "
          f"⇒ the A=3 magnitude gap is baseline-class-RELATIVE (scope-a caveat), "
          f"signs robust. No fit; nothing wired.")
    print(f"witness -> {out.name}")

    # ---- self-checks (none inverts a target) ----
    assert corr["signs_robust_mu3pos_mu4neg"], "μ₃>0, μ₄<0 must be robust across baselines"
    for k in BASELINES:
        assert corr["per_baseline"][k]["mu2_is_zero"], f"μ₂ must be 0 (deuteron) for {k}"
    assert mp.mpf(corr["per_baseline"]["G_graded_coinvariant"]["mu3"]) > mp.mpf("0.47") and \
           mp.mpf(corr["per_baseline"]["G_graded_coinvariant"]["mu3"]) < mp.mpf("0.472"), \
           "corpus μ₃ must reproduce 0.4708"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
