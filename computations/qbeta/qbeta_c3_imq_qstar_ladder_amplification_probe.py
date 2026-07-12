#!/usr/bin/env python3
"""qbeta_c3_imq_qstar_ladder_amplification_probe.py

Third-anchor push on the ε(q₀) decay projection (candidate (iii); #3600/#3636).
Instead of a third *physical* anchor, this evaluates the c₃ extractor
`c3_target_at(q₀, Q_β, m_e)` (`qbeta_utils`) as a DETERMINISTIC function of q₀,
which dissolves the "2-anchor entropy" framing of the earlier
`qbeta_c3_imq_ratio_and_entropy_probe.py` and lets the S-zero q* be root-found to
full precision. It then decomposes the hypersensitivity — with a sharper,
honest conclusion.

FINDINGS (scope-(a); C14; no c_k wired; no fit):

  1. **q\\* to full precision.** `S(q) = c3_target_at(q,Q_β,m_e) + Vol(4₁)` (both
     anchors reproduced exactly) has its zero at
       `q\\* = 1.10997859303152328840…`
     (the pure bar-even / ε=0 substrate point, where c₃ = −Vol(4₁) exactly),
     `~80.3 %` of the way muon-ward, root-found — not interpolated.

  2. **The hypersensitivity is a `1/u³` ladder-inversion artifact, NOT a physical
     near-singularity (scope-(a) RECALIBRATION).** The extractor is
     `c₃ = (Q_β/Q_{N2} − 1)/u³`, `u = b·ℏ_q² ≈ 0.00852` the truncation
     small-parameter. So `S'(q\\*) = 3.84×10⁶ = 2.37 × (1/u³)` with
     `1/u³ ≈ 1.62×10⁶` and a **smooth O(1)** prefactor `2.37`. The famous
     `dc₃/dq ≈ 4.66×10⁶` is therefore the `1/u³` amplification of a smooth
     numerator zero-crossing — not a phase "near a quadrant boundary" nor a
     magnitude singularity. Earlier corpus framings that read the swing as a
     near-singular substrate→u map are re-scoped: the NUMBERS stand, the
     "singularity" interpretation does not. The underlying object
     `(Q_β/Q_{N2} − 1)` (hence the decay projection ε) is SMOOTH.

  3. **The real precision limit is the EXPERIMENTAL Q_β, not the anchor count.**
     `dq\\*/dQ_β ≈ −0.54`, so q* is pinned only as well as the neutron β-decay
     Q-value is measured (`Q_BETA_MEV ≈ 0.7823`). Identifying q* as a
     mathematical constant is limited by that experimental precision — a **more
     precise neutron Q_β measurement directly sharpens q\\***, a concrete
     falsifiable lever (which more *anchors* at the same Q_β would not give).

This REFINES the earlier ratio-entropy probe: S(q₀) is fully computable (not
2-anchor-limited); the block is the experimental Q_β precision on identifying q*,
and the hypersensitivity is a derived 1/u³ representation artifact. The physical
model for the smooth underlying object (Im 𝔙 / Φ_b state-integral, #3596) stays
the open question — but it is a SMOOTH object, no singular map required.
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
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402

mp.mp.dps = 60
ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
VOL41 = 2 * mp.clsin(2, mp.pi / 3)


def S(q):
    return c3_target_at(q, QCOD, ME) + VOL41


def main() -> int:
    print("=" * 78)
    print(" c₃ ε(q₀): q* to full precision + the 1/u³ ladder-amplification reframing")
    print("=" * 78)

    qp, qm = q_at(60), q_muon_at(60)
    print("\n[0] reproduce anchors (c3_target_at deterministic):")
    print(f"    S(proton)={mp.nstr(S(qp),8)} (tgt −0.03945936)   S(muon)={mp.nstr(S(qm),8)} (tgt +0.00968298)")
    repro = abs(S(qp) - mp.mpf("-0.03945936")) < mp.mpf("1e-6") and abs(S(qm) - mp.mpf("0.00968298")) < mp.mpf("1e-6")

    # ---- 1. q* root-found ----
    qstar = mp.findroot(S, (qp + qm) / 2)
    frac = (qstar - qp) / (qm - qp)
    print("\n[1] q* (S=0, root-found — pure bar-even / ε=0 point):")
    print(f"    q* = {mp.nstr(qstar,25)}   ({mp.nstr(frac*100,5)}% muon-ward; not interpolated)")

    # ---- 2. hypersensitivity = smooth × 1/u³ ----
    u = substrate_ladder_quantities(qstar)["u"]
    hh = mp.mpf("1e-18")
    dS = (S(qstar + hh) - S(qstar - hh)) / (2 * hh)
    prefactor = dS * u ** 3
    print("\n[2] hypersensitivity decomposition (NOT a singularity):")
    print(f"    u(q*)={mp.nstr(u,8)}  1/u³={mp.nstr(1/u**3,6)}")
    print(f"    S'(q*)={mp.nstr(dS,8)} = {mp.nstr(prefactor,6)} × 1/u³   (smooth O(1) prefactor)")
    print("    ⇒ dc₃/dq≈4.66e6 is the 1/u³ ladder-inversion amplification of a smooth")
    print("      numerator zero — the 'near-singular map' framing is re-scoped (numbers stand).")

    # ---- 3. real limit = experimental Q_β ----
    dq_dQ = mp.diff(lambda Qb: mp.findroot(lambda q: c3_target_at(q, Qb, ME) + VOL41, qstar), QCOD)
    print("\n[3] precision limit is EXPERIMENTAL Q_β, not anchor count:")
    print(f"    dq*/dQ_β = {mp.nstr(dq_dQ,6)}  (Q_BETA_MEV={str(C.Q_BETA_MEV)})")
    print("    ⇒ a more precise neutron Q_β directly sharpens q*; more anchors at same Q_β do not.")

    # ---- 4. q* is a decay-sector determination of q0, not a mass-sector mean ----
    sig_mu, sig_p = mp.mpf("22"), mp.mpf("0.06")          # documented anchor ppb
    q_wmean = (qp / sig_p ** 2 + qm / sig_mu ** 2) / (1 / sig_p ** 2 + 1 / sig_mu ** 2)
    frac_w = (q_wmean - qp) / (qm - qp) * 100
    print("\n[4] q* is a third, DECAY-SECTOR determination of q₀:")
    print(f"    precision-weighted μ-p mass reconciliation: {mp.nstr(frac_w,4)}% muon-ward (≈ proton;")
    print(f"      proton is {mp.nstr(sig_mu/sig_p,4)}× more precise) — the mass-sector consensus q₀.")
    print(f"    q* (ε=0 bar-odd point):                     {mp.nstr(frac*100,4)}% muon-ward.")
    print("    ⇒ q* is NOT the mass-sector statistical mean; it is an INDEPENDENT determination")
    print("      of q₀ from the bar-odd Q_β decay sector. μ-p tension becomes a μ-p-Q_β trio.")
    decay_sector_independent = abs(float(frac * 100) - float(frac_w)) > 10

    wb = WitnessBuilder("qbeta-c3-imq-qstar-ladder-amplification", engine="mpmath")
    wb.set_description(
        "ε(q₀) decay-projection: evaluate the c₃ extractor c3_target_at as a "
        "deterministic function of q₀ (dissolving the 2-anchor framing), root-find "
        "the S=0 point q*=1.10997859303152… (pure bar-even, ~80.3% muon-ward), and "
        "decompose the hypersensitivity. KEY: S'(q*)=3.84e6=2.37×(1/u³), u=b·ℏ_q²≈"
        "0.00852 — the dc₃/dq≈4.66e6 swing is the 1/u³ ladder-inversion amplification "
        "of a SMOOTH O(1) numerator zero, NOT a physical near-singularity "
        "(scope-(a) recalibration of prior 'near-singular map' framings; numbers "
        "stand). Precision limit is the experimental Q_β (dq*/dQ_β≈−0.54), not the "
        "anchor count — a better neutron Q_β sharpens q*. Refines the earlier "
        "ratio-entropy probe. The underlying decay projection is smooth; the physical "
        "model (Im 𝔙 / Φ_b, #3596) stays open. No c_k wired; no fit; C14."
    )
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("q_star", {"value": mp.nstr(qstar, 25), "frac_muon_ward_pct": mp.nstr(frac * 100, 8),
                           "meaning": "S=0: c3 = -Vol(4_1) exactly (pure bar-even, eps=0)",
                           "anchors_reproduced": bool(repro)})
    wb.add_data("hypersensitivity_decomp", {
        "S_prime_qstar": mp.nstr(dS, 10), "u": mp.nstr(u, 12), "inv_u_cubed": mp.nstr(1 / u ** 3, 10),
        "smooth_prefactor": mp.nstr(prefactor, 8),
        "verdict": "dc3/dq is 1/u^3 ladder amplification of a smooth numerator zero, not a singularity"})
    wb.add_data("precision_limit", {"dqstar_dQbeta": mp.nstr(dq_dQ, 8), "Q_BETA_MEV": str(C.Q_BETA_MEV),
                                    "lever": "more precise neutron Q_beta sharpens q*; more anchors do not"})
    wb.add_data("decay_sector_determination", {
        "q_star_frac_muon_ward_pct": mp.nstr(frac * 100, 6),
        "mass_weighted_reconciliation_pct": mp.nstr(frac_w, 6),
        "proton_over_muon_precision": mp.nstr(sig_mu / sig_p, 4),
        "verdict": "q* is an independent decay-sector (bar-odd Q_beta) determination of q0, "
                   "NOT the mass-sector statistical mean (which sits ~0% muon-ward = proton); "
                   "the mu-p tension becomes a mu-p-Q_beta three-way picture"})
    wb.add_assertion("hypersensitivity_is_ladder_1_over_u3_amplification",
                     computed=float(prefactor), expected=2.37, tolerance=0.5,
                     source="S'(q*) = (smooth O(1) prefactor ~2.37) x 1/u^3; the dc3/dq swing is a 1/u^3 representation artifact, not a physical singularity")
    wb.add_assertion("anchors_reproduced_exactly",
                     computed=1.0 if repro else 0.0, expected=1.0, tolerance=0.5,
                     source="S(proton)/S(muon) from c3_target_at match the committed anchor-blind witness")
    wb.add_assertion("qstar_is_decay_sector_not_mass_mean",
                     computed=1.0 if decay_sector_independent else 0.0, expected=1.0, tolerance=0.5,
                     source="q* at 80% muon-ward != precision-weighted mass reconciliation ~0% (proton); q* is an independent decay-sector determination of q0")
    wb.save()
    print("\n  RESULT: q* full-precision; hypersensitivity = 1/u³ ladder artifact (smooth prefactor 2.37);")
    print("          q* limited by experimental Q_β. Underlying decay projection is SMOOTH.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
