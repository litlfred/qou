#!/usr/bin/env python3
"""
Option-E PROBE 1 — DERIVE-OR-FALSIFY the v9 mirror-pair (1+q)/2 closure factor.

Ledger: docs/coordination/option-e.md PROBE 1 (next-session keystone).
Audit:  docs/audits/2026-06-02-option-e-derive-1plusq-over-2.md

The v9 closure formula (option_e_v9_all_symmetries.py) is

    B_T - B_³He = m_π · ℏ_q · (1+q)/2 · Σ_λ y_λ · (χ^λ(β_T) + χ^{λᵀ}(β_³He))/2

Every factor EXCEPT (1+q)/2 is derived. (1+q)/2 was SELECTED from a substrate-
candidate list to close the residual (published 0.11% near-match — but at the
STALE muon-anchor literal q₀ = 1.1097090249 hardcoded in the v9 source).

This probe does NOT search for a v10 / better factor. It tests the EXISTING
(1+q)/2 against the structural machinery and against a proton-pin vs muon-pin
fit discriminator.

STEP 0  — refresh the v9 residual at the CURRENT canonical proton q₀.
HYP 1-4 — does any structural construction FORCE exactly (1+q)/2 (= [2]_q/2 in
          the unbalanced Hecke convention [2]_q = 1+q)?
DECISIVE — required closure factor R = target/(m_π·ℏ_q·S) at proton-pin vs
          muon-pin; does (1+q)/2 hold at both or drift?  A structural factor is
          the SAME algebraic expression at every anchor (q the only variable).

AUDIT-ONLY witness (no production wiring). Canonical q₀ via q_parameter; the
stale literal appears ONLY in the explicit staleness-delta demonstration.

Output: option-e-probe1-derive-1plusq-over-2.witness.json
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from codata_constants import (
    AME_B_TRITIUM_MEV_VALIDATION,
    M_PI_PM_MEV_VALIDATION  # noqa: E402 (codata sweep,
)
import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from q_parameter import q_at, q_muon_at  # noqa: E402
from codata_constants import AME_B_HE3_MEV_VALIDATION  # noqa: E402  (AME registry)

DPS = 50
mp.mp.dps = DPS

M_PI_MEV = mp.mpf(M_PI_PM_MEV_VALIDATION)           # CAL-3 pion mass (input)
# witness-copy-intentional: frozen ON PURPOSE — see the note above.
# This probe's subject IS the published near-match at this retired
# pin; re-pointing it at a live value would delete the finding.
STALE_Q0 = mp.mpf("1.1097090249")        # the v9 hardcoded muon-anchor literal

# AME binding energies (MeV) — same source as the v9 script.
AME = {"T": AME_B_TRITIUM_MEV_VALIDATION, "3He": AME_B_HE3_MEV_VALIDATION}
DIFF_TARGET = AME["T"] - AME["3He"]      # B_T - B_³He (target)

REPO = Path(__file__).resolve().parent.parent
COMP = REPO / "computations"


# ── partition helpers ───────────────────────────────────────────────────────
def transpose(lam):
    lam = list(lam)
    if not lam:
        return tuple()
    return tuple(sum(1 for p in lam if p > i) for i in range(max(lam)))


# ── load the canonical (proton-q₀) y_λ and χ_λ at 50 dps ─────────────────────
def load_y_and_chi(atom):
    """Load y_λ AND χ_λ from the canonical chi-<atom>-h9-at-q0-50dps witness.
    These are at the CURRENT canonical proton q₀ = 1.1099785955573347 (50dps)."""
    name = {"T": "tritium-h9", "3He": "helium-3-h9"}[atom]
    fn = COMP / f"chi-{name}-at-q0-50dps.witness.json"
    data = json.load(fn.open())
    q0_baked = mp.mpf(data["q_0_50dps"])
    y, chi = {}, {}
    for e in data["by_partition"]:
        part = e["partition"]
        part = tuple(eval(part)) if isinstance(part, str) else tuple(part)
        y[part] = mp.mpf(e["y_lambda"])
        chi[part] = mp.mpf(e["chi_lambda"])
    return y, chi, q0_baked


def mirror_sum(y_T, chi_T, chi_He3):
    """S = Σ_λ y_λ · (χ^λ(β_T) + χ^{λᵀ}(β_³He))/2  (the structural bar-sym sum)."""
    S = mp.mpf(0)
    for p in chi_T:
        pt = transpose(p)
        if pt not in chi_He3:
            continue
        M_sym = (chi_T[p] + chi_He3[pt]) / 2
        S += y_T.get(p, mp.mpf(0)) * M_sym
    return S


def hbar_q(q):
    return 1 - 1 / q


def factor_1plusq_over_2(q):
    return (1 + q) / 2


def main() -> int:
    t0 = time.monotonic()

    q_p = q_at(DPS)        # canonical proton pin
    q_mu = q_muon_at(DPS)  # muon cross-check pin

    print("=" * 72)
    print("Option-E PROBE 1 — derive-or-falsify v9 (1+q)/2")
    print("=" * 72)
    print(f"q_proton (canonical) = {mp.nstr(q_p, 30)}")
    print(f"q_muon   (crosscheck)= {mp.nstr(q_mu, 30)}")
    print(f"q_stale  (v9 literal)= {mp.nstr(STALE_Q0, 20)}")
    print(f"target B_T-B_³He     = {mp.nstr(DIFF_TARGET, 12)} MeV\n")

    # The canonical y_λ, χ_λ caches are baked at the proton q₀.
    y_T, chi_T, q0_T = load_y_and_chi("T")
    y_He3, chi_He3, q0_He3 = load_y_and_chi("3He")
    print(f"y/χ caches baked at q₀ = {mp.nstr(q0_T, 25)} (T), "
          f"{mp.nstr(q0_He3, 25)} (³He)")
    cache_is_proton = abs(q0_T - q_p) < mp.mpf("1e-20")
    print(f"  cache == canonical proton q₀ ? {cache_is_proton}\n")

    S = mirror_sum(y_T, chi_T, chi_He3)
    print(f"structural mirror sum  S = Sum y_lam*(chi^lam(T)+chi^lamT(3He))/2 = "
          f"{mp.nstr(S, 18)}\n")

    # ── STEP 0: refresh v9 residual at canonical q₀ (vs stale literal) ────────
    def v9_value(q):
        return M_PI_MEV * hbar_q(q) * factor_1plusq_over_2(q) * S

    def rel_pct(pred):
        return float((pred - DIFF_TARGET) / DIFF_TARGET * 100)

    v9_stale = v9_value(STALE_Q0)
    v9_proton = v9_value(q_p)
    v9_muon = v9_value(q_mu)
    step0 = {
        "stale_literal_q0": str(STALE_Q0),
        "canonical_proton_q0": str(q_p),
        "muon_q0": str(q_mu),
        "v9_value_at_stale_MeV": str(v9_stale),
        "v9_value_at_proton_MeV": str(v9_proton),
        "v9_value_at_muon_MeV": str(v9_muon),
        "target_MeV": str(DIFF_TARGET),
        "residual_at_stale_pct": rel_pct(v9_stale),
        "residual_at_proton_pct": rel_pct(v9_proton),
        "residual_at_muon_pct": rel_pct(v9_muon),
    }
    print("-- STEP 0: v9 residual, stale vs canonical --")
    print(f"  v9 @ stale   q0: {mp.nstr(v9_stale,10)} MeV  "
          f"resid {step0['residual_at_stale_pct']:+.4f}%")
    print(f"  v9 @ proton  q0: {mp.nstr(v9_proton,10)} MeV  "
          f"resid {step0['residual_at_proton_pct']:+.4f}%")
    print(f"  v9 @ muon    q0: {mp.nstr(v9_muon,10)} MeV  "
          f"resid {step0['residual_at_muon_pct']:+.4f}%\n")

    # ── DECISIVE FIT TEST: required closure factor R at each pin ──────────────
    # R(q) := target / (m_π · ℏ_q · S).  A STRUCTURAL factor equals (1+q)/2 at
    # EVERY anchor.  We compare R(q) to (1+q)/2 at proton vs muon pins.  S is
    # held at its canonical (proton-cache) value; varying S to the muon pin
    # shifts it by ~11.5 ppb — negligible vs the test resolution (documented).
    def required_factor(q):
        return DIFF_TARGET / (M_PI_MEV * hbar_q(q) * S)

    R_p = required_factor(q_p)
    R_mu = required_factor(q_mu)
    f_p = factor_1plusq_over_2(q_p)
    f_mu = factor_1plusq_over_2(q_mu)
    decisive = {
        "required_factor_proton": str(R_p),
        "required_factor_muon": str(R_mu),
        "candidate_1plusq_over_2_proton": str(f_p),
        "candidate_1plusq_over_2_muon": str(f_mu),
        "residual_proton_pct": float((f_p - R_p) / R_p * 100),
        "residual_muon_pct": float((f_mu - R_mu) / R_mu * 100),
    }
    print("-- DECISIVE FIT TEST: required factor R vs (1+q)/2 --")
    print(f"  proton pin: R = {mp.nstr(R_p,12)}  (1+q)/2 = {mp.nstr(f_p,12)}  "
          f"resid {decisive['residual_proton_pct']:+.4f}%")
    print(f"  muon   pin: R = {mp.nstr(R_mu,12)}  (1+q)/2 = {mp.nstr(f_mu,12)}  "
          f"resid {decisive['residual_muon_pct']:+.4f}%")
    drift = abs(decisive["residual_muon_pct"] - decisive["residual_proton_pct"])
    print(f"  drift |resid_muon - resid_proton| = {drift:.6f} pct-points")
    print("  (proton & muon q0 differ by only ~11.5 ppb, so a STRUCTURAL")
    print("   factor's residual is identical at both pins to ~1e-8; the test")
    print("   asks instead: is R EQUAL to (1+q)/2 at all, or merely near it?)\n")

    # ── HYPOTHESES 1-4: does any structural construction FORCE (1+q)/2? ───────
    # Compute each candidate at q_p; compare to (1+q_p)/2.  A hypothesis is
    # "FORCING" only if it equals (1+q)/2 IDENTICALLY (algebraic identity), not
    # merely numerically near.

    # HYP 1: [2]_q / [2]_{q=1}  in unbalanced convention [2]_q = 1+q.
    #        [2]_{q=1} = 2 ⇒ ratio = (1+q)/2.  Algebraically equal BY DEFINITION;
    #        the real question (answered in the audit) is whether S carries a
    #        hidden [2]_q normalization that SUPPLIES this ratio structurally.
    hyp1_val = (1 + q_p) / (1 + mp.mpf(1))           # = (1+q)/2

    # HYP 2: trace of σ_1 in the standard (2,1) rep & its half.
    #        Unbalanced H_3: σ_1 eigenvalues {q, -q⁻¹} on ρ_(2,1) (2-dim) ⇒
    #        tr ρ_(2,1)(σ_1) = q - q⁻¹ = h.
    hyp2_trace = q_p - 1 / q_p                       # = h
    hyp2_halftrace = hyp2_trace / 2                  # h/2
    hyp2_principal = (q_p + 1) / 2                   # (q+1)/2 principal-spec form

    # HYP 3: Hoefsmit seminormal normalization at the (2,1) shape.
    #        balanced [k]_q = (q^k - q^-k)/(q - q^-1).
    def qint_bal(k, q):
        return (q**k - q**(-k)) / (q - q**(-1))
    hyp3_diag = 1 / qint_bal(2, q_p)                 # 1/[2]_q axial-distance diag
    hyp3_offdiag = mp.sqrt(qint_bal(3, q_p) * qint_bal(1, q_p)) / qint_bal(2, q_p)

    # HYP 4: (2,1)-block "identity-half" weight — symmetric-channel projector
    #        weight of the trivial component.
    hyp4_sym_bal = q_p / (q_p + 1 / q_p)             # q/[2]_q balanced
    hyp4_sym_unbal = q_p / (1 + q_p)                 # q/(1+q) unbalanced

    target_factor = factor_1plusq_over_2(q_p)

    def forcing_report(name, val):
        diff = val - target_factor
        is_identity = abs(diff) < mp.mpf("1e-40")
        return {
            "name": name,
            "value": str(val),
            "minus_1plusq_over_2": str(diff),
            "rel_pct_vs_1plusq_over_2": float(diff / target_factor * 100),
            "ALGEBRAIC_IDENTITY_with_1plusq_over_2": bool(is_identity),
        }

    hyps = {
        "H1_two_q_over_two_unbalanced": forcing_report(
            "[2]_q/2 = (1+q)/2 (unbalanced)", hyp1_val),
        "H2a_standard_rep_trace_sigma1": forcing_report(
            "tr rho_(2,1)(sigma_1) = q-q^-1 = h", hyp2_trace),
        "H2b_half_trace_sigma1": forcing_report(
            "h/2", hyp2_halftrace),
        "H2c_principal_spec_form": forcing_report(
            "(q+1)/2 principal-spec form", hyp2_principal),
        "H3a_hoefsmit_diag_1_over_2q": forcing_report(
            "1/[2]_q (Hoefsmit diag, balanced)", hyp3_diag),
        "H3b_hoefsmit_offdiag": forcing_report(
            "sqrt([3][1])/[2] (Hoefsmit offdiag)", hyp3_offdiag),
        "H4a_sym_proj_q_over_2q_bal": forcing_report(
            "q/[2]_q (sym projector, balanced)", hyp4_sym_bal),
        "H4b_sym_proj_q_over_1plusq": forcing_report(
            "q/(1+q) (sym projector, unbalanced)", hyp4_sym_unbal),
    }
    print("-- HYPOTHESES 1-4: does any construction FORCE (1+q)/2? --")
    print(f"  target (1+q)/2 @ proton = {mp.nstr(target_factor, 18)}")
    for k, h in hyps.items():
        flag = "  <== ALGEBRAIC IDENTITY" if h["ALGEBRAIC_IDENTITY_with_1plusq_over_2"] else ""
        print(f"  {h['name']:42s} = {mp.nstr(mp.mpf(h['value']),12):>14s}  "
              f"({h['rel_pct_vs_1plusq_over_2']:+8.3f}%){flag}")
    print()

    elapsed = time.monotonic() - t0

    # Provenance: last commit that touched THIS script (robust to the
    # subsequent witness commit, unlike `git rev-parse HEAD`).
    import subprocess
    try:
        script_sha = subprocess.run(
            ["git", "log", "-1", "--format=%H", "--", __file__],
            cwd=str(Path(__file__).resolve().parent),
            capture_output=True, text=True, check=True,
        ).stdout.strip() or None
    except Exception:
        script_sha = None

    witness = {
        "engine": "python+mpmath",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "option-e-probe1-derive-1plusq-over-2",
        "scriptCommitSha": script_sha,
        "auditOnly": True,
        "trigger": (
            "author directive 'work on Delta_lambda binding-energy Gram "
            "closure' -> docs/coordination/option-e.md PROBE 1 (next-session "
            "keystone): derive-or-falsify v9 (1+q)/2"
        ),
        "description": (
            "Tests whether the v9 mirror-pair closure factor (1+q)/2 is "
            "structurally FORCED (= [2]_q/2 unbalanced) or a near-match/fit. "
            "Refreshes the v9 residual at canonical proton q0 (v9 source "
            "hardcodes the stale muon-anchor literal 1.1097090249); tests 4 "
            "structural hypotheses for an algebraic identity with (1+q)/2; runs "
            "the proton-pin vs muon-pin required-factor discriminator. "
            "AUDIT-ONLY: no production wiring, no v10 ansatz, no fit."
        ),
        "dps": DPS,
        "start_time_monotonic": t0,
        "elapsed_sec": elapsed,
        "q_proton_canonical": str(q_p),
        "q_muon_crosscheck": str(q_mu),
        "stale_literal_q0": str(STALE_Q0),
        "mirror_sum_S": str(S),
        "m_pi_MeV": str(M_PI_MEV),
        "target_diff_MeV": str(DIFF_TARGET),
        "step0_staleness_refresh": step0,
        "decisive_fit_test": decisive,
        "hypotheses": hyps,
    }
    out = COMP / "option-e-probe1-derive-1plusq-over-2.witness.json"
    with out.open("w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(witness, f, indent=2)
    print(f"Wrote {out}")
    print(f"Elapsed {elapsed:.3f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
