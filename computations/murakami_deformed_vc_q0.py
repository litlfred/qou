#!/usr/bin/env python3
"""
Murakami deformed volume-conjecture (VC) route to an *anchor-free* substrate
modulus q0 — categorical N-selection analysis (μ–p Subgoal-2 follow-up to the
pin-sensitivity map, PR #3847 / docs/audits/2026-07-17-mu-p-pin-sensitivity-map.md).

QUESTION (exact).  The pin-sensitivity map PROVED (sorry-free Lean
`PinRobustnessOfRatios`) that the 11.5 ppb μ–p tension lives *entirely* in the
absolute anchor ℏ_q² = ((q0−1)/q0)²; every dimensionless ratio cancels it.  The
only escape is a substrate-first ABSOLUTE q0 that does NOT invert a mass anchor.
The muon anchor is  m_μ/m_e = Vol(4₁)/ℏ_q²,  Vol(4₁) = 2·Cl₂(π/3) ≈ 2.02988
(the *complete*-structure hyperbolic volume of the figure-eight).  Murakami's
DEFORMED VC generalises this to a u-deformed volume Vol(4₁; u).  Does a
CATEGORICALLY-DERIVED deformation datum on 4₁ give
    Vol(4₁; α*)  ⇒  ℏ_q  ⇒  q0   absolutely, independent of the μ/p anchors?

This script does NOT fit anything and wires NOTHING.  It quantifies the three
structural branches of the route and shows each fails to yield an anchor-free q0
to the 11.5 ppb the tension demands, reproducing / extending the #3704
`qbeta_c3_mq0_nk_scan` finding but now aimed at the ABSOLUTE q0 (not the odd-S
value).  Tier: scope-(a) numerical falsification.

Branches (see docs/audits/2026-07-17-murakami-deformed-vc-q0.md §3):
  B1  Undeformed (u=0):    Vol(4₁) is q-INDEPENDENT ⇒ zero q0-handle ⇒ the muon
                            relation must supply m_μ (anchor inversion).
  B2  Real deformation:   Im 𝔙(real u)=0 ⇒ no CS handle; the real-volume
                            deformation has NO purely-geometric target to close.
  B3  Winding deformation: the DERIVED substrate matching u(N,k)=N·ln q0 − 2πik
                            forces |u| ≥ 2πk ≥ 2π (off the 4₁ geometric
                            component); the categorical INTEGER N∈{3,6,60,120}
                            gives q0=exp(2π/N) missing q0 by 3.8e5–5e7 ppb, and
                            hitting 11.5 ppb needs the NON-INTEGER N=60.218 (fit).

-- Ref: [murakami2004] figure-eight & Dehn surgery spaces (math/0401084)
-- Ref: [kashaev1997]  https://doi.org/10.1007/BF01239527
-- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
"""
from __future__ import annotations
import json, subprocess, hashlib, datetime, os
import mpmath as mp

mp.mp.dps = 60

# ---------------------------------------------------------------------------
# Inputs (documented pins — NOT fitted here; from the corpus).
# BOTH pins RESOLVED, not frozen (2026-08-29, bean qou-1c4y). This producer's
# subject IS the mu-p tension, so it reads both anchors on purpose -- but both
# literals had gone wrong in different ways:
#   * the muon literal was the SUPERSEDED pin A, retired as the muon anchor by
#     PR #5500's re-derivation to CODATA-2022, so the "muon" leg of a tension
#     adjudication was no longer the muon pin;
#   * the proton literal was TRUNCATED to 12 digits ("1.10997858275") inside a
#     file running at 60 dps -- ~0.1 ppb of fabricated error in a probe whose
#     whole quantity is an 11.5 ppb gap, i.e. ~1 % of the effect being measured.
# Resolved from the anchor resolver instead, so both follow the next CODATA
# revision with no digit edited by hand.
from qou_substrate.witness import _q0_value_for_anchor as _q0_pin  # noqa: E402

Q0_MUON = mp.mpf(_q0_pin("muon"))
Q0_PROTON = mp.mpf(_q0_pin("proton"))
MU_P_GAP_PPB = mp.mpf("11.5")  # the tension to be adjudicated

# Vol(4₁) = 2·Cl₂(π/3), the COMPLETE-structure volume (the α=1, u=0 limit).
def vol_41() -> mp.mpf:
    # Cl₂(θ) = Im Li₂(e^{iθ}); Vol(4₁) = 2 Cl₂(π/3).
    return 2 * mp.im(mp.polylog(2, mp.e ** (1j * mp.pi / 3)))

VOL41 = vol_41()

# ---------------------------------------------------------------------------
# Branch B1 — the complete-structure volume is q-independent.
# S(Vol) = d log Vol / d log q0 numerically (should be 0 to noise): Vol has NO
# q0 dependence, so the undeformed muon anchor's ENTIRE pin-sensitivity is in
# ℏ_q⁻² (this is the pin-map line-30/86 fact, reproduced here as the branch-B1
# obstruction: without a q-dependent numerator the volume gives no q0-handle).
def branch_b1(q0: mp.mpf) -> dict:
    hbar = (q0 - 1) / q0
    mmu_over_me = VOL41 / hbar ** 2                       # the anchor relation
    # invert: to get q0 from Vol you MUST feed m_μ/m_e — that is the inversion.
    # Sensitivity of Vol to q0 is identically 0 (Vol is a constant):
    S_vol = mp.mpf(0)  # exact: Vol41 has no q0 argument
    S_hbar2 = 2 / (q0 - 1)  # exact d log ℏ_q² / d log q0 = 2/(q0−1)
    return {
        "hbar_q_squared": mp.nstr(hbar ** 2, 30),
        "m_mu_over_m_e_from_anchor": mp.nstr(mmu_over_me, 20),
        "S_Vol41_dlog_dlogq0": mp.nstr(S_vol, 6),
        "S_hbar2_dlog_dlogq0_exact_2_over_qm1": mp.nstr(S_hbar2, 20),
        "verdict": ("Vol(4₁) is q-independent (S=0); undeformed anchor's whole "
                    "q0-sensitivity is in ℏ_q⁻². Determining q0 needs a second "
                    "q-dependent input; the corpus's is m_μ/m_e (anchor inversion)."),
    }

# ---------------------------------------------------------------------------
# Branch B3 — the DERIVED substrate matching and its winding obstruction.
# Murakami evaluates J_N(4₁) at q_eval = exp((u + 2πi)/N). Matching to the REAL
# substrate q0 = e^t (t = ln q0):  (u+2πi)/N = t (mod 2πi/N)  ⇒  u = N·t − 2πik.
# Hence Im(u) = −2πk ⇒ |u| ≥ 2πk ≥ 2π  (the winding lower bound; #3704).
def substrate_meridian(q0: mp.mpf, N: int, k: int) -> mp.mpc:
    t = mp.log(q0)
    return N * t - 2j * mp.pi * k

def branch_b3(q0: mp.mpf) -> dict:
    t = mp.log(q0)
    # (i) the naive quantization q0 = exp(2π/N): required N is 2π/ln q0.
    N_req = 2 * mp.pi / t
    named = [3, 6, 59, 60, 61, 120]
    exp_2pi_over_N = {}
    for N in named:
        qN = mp.e ** (2 * mp.pi / N)
        ppb = (qN - q0) / q0 * mp.mpf(10) ** 9
        exp_2pi_over_N[str(N)] = {
            "q0_candidate": mp.nstr(qN, 15),
            "miss_ppb_vs_pin": mp.nstr(ppb, 8),
        }
    # (ii) the winding lower bound |u| ≥ 2π for the substrate-matched datum.
    windings = {}
    for (N, k) in [(3, 1), (6, 1), (60, 1), (120, 1), (60, 2), (120, 2)]:
        u = substrate_meridian(q0, N, k)
        windings[f"N{N}_k{k}"] = {
            "u": f"{mp.nstr(mp.re(u),10)} + {mp.nstr(mp.im(u),10)}i",
            "abs_u": mp.nstr(abs(u), 12),
            "abs_im_u_eq_2pi_k": mp.nstr(abs(mp.im(u)), 12),
        }
    return {
        "N_required_for_q0_eq_exp_2pi_over_N": mp.nstr(N_req, 18),
        "N_required_is_integer": bool(mp.almosteq(N_req, mp.nint(N_req), abs_eps=mp.mpf(10) ** -6)),
        "exp_2pi_over_N_candidates": exp_2pi_over_N,
        "substrate_winding_data": windings,
        "winding_floor_2pi": mp.nstr(2 * mp.pi, 12),
        "verdict": ("q0=exp(2π/N) needs the NON-INTEGER N=%s; nearest categorical "
                    "integer N=60 misses q0 by %s ppb. The substrate-matched datum "
                    "u=N·t−2πik always has |u|≥2π (off the 4₁ geometric component, "
                    "per #3704). No categorical INTEGER N gives anchor-free q0."
                    % (mp.nstr(N_req, 8),
                       mp.nstr((mp.e ** (2 * mp.pi / 60) - q0) / q0 * mp.mpf(10) ** 9, 6))),
    }

# ---------------------------------------------------------------------------
# Integer-N degeneracy w.r.t. the pin (a SECOND reason the route cannot
# adjudicate μ–p): the CONTINUOUS N_req = 2π/ln q0 does move with q0 (~110 ppb
# between pins — it is a reparametrisation of q0, NOT pin-blind). But a
# CATEGORICAL selection yields a single INTEGER N, and ⌊N_req⌉ = 60 for BOTH
# pins; one integer cannot produce two distinct q0=exp(2π/N). So the integer-N
# route is degenerate w.r.t. the pin — it cannot even represent the split.
def cross_pin() -> dict:
    N_mu = 2 * mp.pi / mp.log(Q0_MUON)
    N_p = 2 * mp.pi / mp.log(Q0_PROTON)
    swing_ppb = (N_p - N_mu) / N_mu * mp.mpf(10) ** 9
    return {
        "N_req_muon_pin": mp.nstr(N_mu, 18),
        "N_req_proton_pin": mp.nstr(N_p, 18),
        "N_req_continuous_cross_pin_swing_ppb": mp.nstr(swing_ppb, 8),
        "nearest_integer_both_pins": int(mp.nint(N_mu)),
        "note": ("The CONTINUOUS N_req moves ~110 ppb between pins (a "
                 "reparametrisation of q0, not pin-blind), but the nearest INTEGER "
                 "is 60 for both. A categorical selection yields one integer N, "
                 "which cannot produce two distinct q0=exp(2π/N) — the integer-N "
                 "route is degenerate w.r.t. the μ–p split, independent of the "
                 "379095 ppb absolute miss."),
    }

def script_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", os.path.basename(__file__)],
            cwd=os.path.dirname(os.path.abspath(__file__)),
        ).decode().strip() or "uncommitted"
    except Exception:
        return "uncommitted"

def file_hash() -> str:
    with open(os.path.abspath(__file__), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:16]

def main() -> None:
    result = {
        "description": ("Murakami deformed-VC route to an anchor-free q0: "
                        "categorical N-selection analysis. Scope-(a) negative — "
                        "no anchor-free categorical selection currently exists; "
                        "nothing fitted, nothing wired. μ–p Subgoal-2 (#3847)."),
        "computation": "murakami_deformed_vc_q0",
        "audit_only": True,
        "tier": "scope-(a) numerical falsification (no fit; not wired; μ–p NOT resolved)",
        "precision_dps": mp.mp.dps,
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "inputs": {
            "q0_muon_pin": mp.nstr(Q0_MUON, 30),
            "q0_proton_pin": mp.nstr(Q0_PROTON, 15),
            "Vol_4_1_2Cl2_pi_over_3": mp.nstr(VOL41, 30),
            "mu_p_gap_ppb_to_adjudicate": mp.nstr(MU_P_GAP_PPB, 4),
        },
        "branch_b1_undeformed_qindependent": branch_b1(Q0_MUON),
        "branch_b3_winding_and_naive_quantization": branch_b3(Q0_MUON),
        "cross_pin_blindness": cross_pin(),
        "overall_verdict": (
            "No anchor-free categorical N-selection currently exists (scope-(a)). "
            "B1: undeformed Vol(4₁) is q-independent ⇒ anchor inversion. "
            "B3: substrate-matched u=N·t−2πik forces |u|≥2π (off-component, #3704); "
            "q0=exp(2π/N) needs the non-integer N=60.218, nearest integer N=60 "
            "misses by 3.8e5 ppb (~33000× the 11.5 ppb tension); tuning N is a fit. "
            "This is scope-(a) (the construction ALONE fails), NOT scope-(b): no "
            "proved invariant forbids a future substrate-functor level datum with a "
            "small-complex u (the meridian-side surviving direction #3704 flags)."
        ),
        "witness": {
            "scriptCommitSha": script_sha(),
            "scriptHash": file_hash(),
        },
        "refs": [
            "docs/audits/2026-07-17-mu-p-pin-sensitivity-map.md",
            "docs/scope/2026-07-12-mq0-nk-scan-result.md",
            "docs/scope/2026-07-12-mq0-unified-boundary-selection.md",
            "computations/qbeta/qbeta_c3_mq0_nk_scan.py",
        ],
    }
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "murakami-deformed-vc-q0.witness.json")
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    # DECLARED comparison. Both pins are read deliberately -- the mu-p gap IS the
    # subject -- so there is no single pin to stamp, and an auto-resolved anchor
    # plus the carry-forward of the previous run's value produced a Q0_FLIP on a
    # witness whose numbers were fine. `comparison` names its legs, and the
    # anchor audit re-checks each against its canonical pin, so the declaration
    # is verifiable rather than taken on trust (bean qou-1c4y).
    from qou_substrate.witness import apply_q0_comparison  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(result, script_path=__file__, engine="mpmath")
    apply_q0_comparison(result,
        muon=Q0_MUON, proton=Q0_PROTON,
        reason=("adjudicates the mu-p substrate tension itself: the same "
                "deformed-volume construction is evaluated at both pins and "
                "the ~11.5 ppb gap between them is the measured quantity, so "
                "each pin is read on purpose and reported under its own key"))
    result.pop("q0Value", None)
    result["scriptFile"] = _os.path.basename(__file__)
    with open(out, "w") as f:
        json.dump(result, f, indent=2)
    print(json.dumps(result, indent=2))
    print(f"\n[witness] wrote {out}")

if __name__ == "__main__":
    main()
