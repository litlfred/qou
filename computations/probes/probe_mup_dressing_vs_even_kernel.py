#!/usr/bin/env python3
"""
probe_mup_dressing_vs_even_kernel.py — does the exactly-measured Q_β
bar-even kernel E(ũ) account for the μ–p dressing? (derive-or-refute)

Context. The μ–p tension (11.5 ppb in q₀; ~242 ppb on m_p at the
muon-pinned canonical q₀) is the shadow of the missing higher-order
dressing on the low-order mass identities (2026-05-28 floor audit; PR
#3264 decision package). The freshest exact object in the corpus is the
bar-even channel of the Q_β net-route ladder: ORD-17 proved
log R |_even = E(ũ) with 8 EXACT rungs e₁..e₈ in ℚ(√3), ũ =
q·(√(q⁴+q²+1)/(q²+1))·ℏ_q² (witness `qbeta-bar-split-ord17`, bean 08ds).

Question. Transported as-is to the mass channel — i.e. evaluated at the
substrate ũ₀ and read as a multiplicative dressing candidate — does any
natural object built from E (full kernel, single rung e_k·ũ^k, or tail
Σ_{k≥j}) reproduce the required mass dressing

    δ_p := m_p_CODATA / m_p_pred(q₀_muon) − 1        (≈ +2.4e-7), or
    δ_μ := m_μ_CODATA / m_μ_pred(q₀_proton) − 1      (≈ −2.1e-7, the
           tension worn on the muon leg instead)?

No fit: the rungs are loaded from the committed ORD-17 witness verbatim;
the only evaluation freedom is which documented variable (ũ, or the
mis-normalized legacy u) and which truncation — all combinations are
reported with sign and ratio.

Output: probe-mup-dressing-vs-even-kernel.witness.json
"""
from __future__ import annotations

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

HERE = Path(__file__).parent

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from knot_volumes import VOL_4_1_MPF  # noqa: E402
from m_p_substrate_identity_50dps import F_Bor  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

M_P_CODATA = mp.mpf("938.27208816")
M_MU_CODATA = mp.mpf("105.6583755")
ORD17_WITNESS = HERE.parent / "qbeta" / "qbeta-bar-split-ord17.witness.json"


def m_p_pure_q(q, m_e):
    hbar_q_sq = ((q - 1) / q) ** 2
    return 2 * (m_e * VOL_4_1_MPF / hbar_q_sq * F_Bor(q) - 6 * m_e)


def m_mu_pred(q, m_e):
    return m_e * VOL_4_1_MPF / (((q - 1) / q) ** 2)


def _q_muon_explicit():
    """Muon pin, solved explicitly from m_mu/m_e = Vol(4_1)/hbar_q^2 —
    self-contained so this probe is INDEPENDENT of which pin the package
    constant carries (the towered-constant incident, 592eade9, showed
    Q_50_DIGIT_STR's pin can drift; owner ruling 2026-07-03 restored the
    raw proton pin there)."""
    r = mp.mpf("206.7682830")            # CODATA m_mu/m_e
    hbar = mp.sqrt(VOL_4_1_MPF / r)
    return 1 / (1 - hbar)


def main() -> int:
    # Q_50_DIGIT_STR provenance (verified): package proton solve WITH
    # the fitted Habiro tower inside => numerically the MUON-pin value
    # to sub-ppb (m_mu fingerprint 1.36 ppb). See the attribution probe.
    q0 = _q_muon_explicit()              # muon pin, explicit
    m_e = mp.mpf(M_E_MEV)

    # Required dressings, both attributions of the tension.
    delta_p = M_P_CODATA / m_p_pure_q(q0, m_e) - 1
    q0_proton = mp.findroot(
        lambda q: m_p_pure_q(q, m_e) - M_P_CODATA, q0)
    delta_mu = M_MU_CODATA / m_mu_pred(q0_proton, m_e) - 1

    # Exact rungs from the committed ORD-17 witness (verbatim).
    with open(ORD17_WITNESS, "r", encoding="utf-8") as f:
        w = json.load(f)
    rungs = {int(k): sp.sympify(v)
             for k, v in w["data"]["E_rungs_exact"].items()}
    e_num = {k: mp.mpf(str(sp.N(v, mp.mp.dps))) for k, v in rungs.items()}

    # The two documented ladder variables at substrate.
    hbar2 = ((q0 - 1) / q0) ** 2
    b = mp.sqrt(q0**4 + q0**2 + 1) / (q0**2 + 1)
    u_tilde = q0 * b * hbar2             # the bar-even variable (ai81/08ds)
    u_legacy = b * hbar2                 # the mis-normalized corpus u

    candidates = {}
    for name, uv in (("utilde", u_tilde), ("ulegacy", u_legacy)):
        terms = {k: e_num[k] * uv**k for k in sorted(e_num)}
        candidates[f"E_full_{name}"] = mp.fsum(terms.values())
        for k, tval in terms.items():
            candidates[f"rung{k}_{name}"] = tval
        for j in (4, 5, 6):
            candidates[f"tail_ge{j}_{name}"] = mp.fsum(
                v for k, v in terms.items() if k >= j)

    print(f"delta_p (dressing on proton leg, muon q0)  = {mp.nstr(delta_p, 8)}")
    print(f"delta_mu (dressing on muon leg, proton q0) = {mp.nstr(delta_mu, 8)}")
    print(f"u_tilde(q0) = {mp.nstr(u_tilde, 10)}   u_legacy = {mp.nstr(u_legacy, 10)}")
    best = {}
    for target_name, target in (("delta_p", delta_p), ("delta_mu", delta_mu)):
        print(f"--- candidates vs {target_name} = {mp.nstr(target, 6)} ---")
        for cname, cval in candidates.items():
            ratio = cval / target
            flag = " <== match" if abs(ratio - 1) < mp.mpf("0.01") else ""
            if abs(ratio) < 50:  # only print same-ballpark candidates
                print(f"  {cname:22s} = {mp.nstr(cval, 6):>14s}  ratio {mp.nstr(ratio, 5):>10s}{flag}")
            key = f"best_{target_name}"
            if key not in best or abs(abs(candidates[best[key]] / target) - 1) > abs(abs(ratio) - 1):
                best[key] = cname
    any_match = any(
        abs(candidates[c] / t - 1) < mp.mpf("0.01")
        for c in candidates for t in (delta_p, delta_mu))

    wb = WitnessBuilder("probe-mup-dressing-vs-even-kernel",
                        engine="mpmath+sympy", output_dir=HERE)
    wb.add_upstream(ORD17_WITNESS)
    wb.set_description(
        "Derive-or-refute: transport the ORD-17 exact bar-even Q_beta "
        "kernel E(u~) (8 exact rungs, witness-loaded verbatim) to the "
        "mass channel and test whether any natural object (full kernel, "
        "single rung, tail) reproduces the mu-p dressing delta_p "
        "(+~242 ppb) or delta_mu (-~210 ppb). No fit; all documented "
        "variables and truncations reported with sign and ratio.")
    wb.add_data("delta_p_needed", mp.nstr(delta_p, 15))
    wb.add_data("delta_mu_needed", mp.nstr(delta_mu, 15))
    wb.add_data("u_tilde_at_q0", mp.nstr(u_tilde, 30))
    wb.add_data("candidates_ratio_to_delta_p",
                {c: mp.nstr(v / delta_p, 10) for c, v in candidates.items()})
    wb.add_data("candidates_ratio_to_delta_mu",
                {c: mp.nstr(v / delta_mu, 10) for c, v in candidates.items()})
    wb.add_data("best_candidate_delta_p", best.get("best_delta_p"))
    wb.add_data("best_candidate_delta_mu", best.get("best_delta_mu"))
    wb.add_data("verdict",
                "REFUTED-as-is (scope (a)): no witness-exact object built "
                "from the Q_beta bar-even kernel E(u~) — full kernel, "
                "single rung, or tail, in either documented ladder "
                "variable — reproduces the mu-p dressing within 1%. The "
                "mass-channel dressing is NOT the Q_beta even kernel "
                "evaluated at the same substrate argument; nearest "
                "candidates recorded with sign/ratio as the sharpener."
                if not any_match else
                "MATCH FOUND — see best_candidate fields (near-match "
                "tier; NOT wired).")
    wb.add_assertion("no_silent_match_within_1pct", str(bool(any_match)),
                     "False",
                     source="refutation gate: a future rung/variable change "
                            "producing a 1% match must FAIL this witness "
                            "so the near-match gets re-adjudicated")
    path = wb.save()
    print(f"witness: {path}")
    print("VERDICT:", "match found (near-match tier)" if any_match
          else "REFUTED-as-is, scope (a)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
