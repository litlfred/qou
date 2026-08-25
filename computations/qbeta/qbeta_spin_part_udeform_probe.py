#!/usr/bin/env python3
"""qbeta_spin_part_udeform_probe.py — SP1: is the SPIN part of u(q₀) the fibre
meridian holonomy? Derive-then-check under the corrected Im 𝔙₄₁.

Continuation of #4391 (docs/coordination/udeform-spin-part-derivation.md). The
real-boost part of the open S-channel map is geometrically fixed: `Re u = ln q₀`
(meridian-holonomy-boost.md). The sign-flip S(muon)>0>S(proton) needs
`Im 𝔙₄₁ = (√3/4)(Re²u−Im²u) < 0` at the proton anchor, i.e. `Im²u > Re²u` — the
meridian holonomy crossing the diagonal into the SPIN-dominated regime.

DERIVE (not fitted) the spin candidate. `PhiBSArgumentIdentification` fixes the
physical regime as the fibre branch (real b ⇒ |q_b|=1), with
`q_b = e^{i·ln q₀/2}` (fibreQParam_fibreB, proved). So the fibre log meridian
holonomy is `log q_b = i·(ln q₀/2)` — a pure spin (imaginary), the |q|=1 compact
regime. Full geometric candidate: `u = ln q₀ + i·(ln q₀/2)` (boost + fibre spin).

CHECK (assertions):
  [SP1a] the fibre spin angle ln q₀/2 is SMALLER than the boost ln q₀
         (Im u/Re u = 1/2 < 1), so u stays boost-dominated (Re²u > Im²u).
  [SP1b] hence Im 𝔙₄₁(u) > 0 at BOTH anchors — the smooth boost+fibre-spin
         candidate CANNOT reach S(proton) < 0. REFUTED as the full map (scope-(a)).
  [SP1c] reaching the diagonal (Im²u > Re²u, needed for S<0) requires
         Im u > Re u = ln q₀ ≈ 0.104 — the spin must EXCEED the boost. No smooth
         geometric holonomy from q₀≈1.11 supplies that (even the full fibre
         angle ln q₀ only reaches the diagonal, Im 𝔙 = 0, not past it).

CONCLUSION (SP2, the open crux): the sign-flip source cannot be a smooth
geometric meridian holonomy — it must be a NON-smooth / resonance / near-
degeneracy spin part with Im u > Re u AND hypersensitive to q₀ at the ~1e-8
anchor gap (slope k≈2.2e6, #3773 witness). Identifying (or excluding) such a
geometric object is the remaining open frontier. No u wired; no c_k; no
SDeformedVolumeChannel instance fabricated; nothing fitted.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import c3_target_at  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
with mp.workdps(50):
    VOL41 = +(2 * mp.clsin(2, mp.pi / 3))
KAPPA = mp.sqrt(3) / 4


def S(q):
    return c3_target_at(q, QCOD, ME) + VOL41


def imV41(u: mp.mpc) -> mp.mpf:
    return KAPPA * (mp.re(u) ** 2 - mp.im(u) ** 2)


def main() -> int:
    print("=" * 78)
    print(" SP1: spin part of u(q₀) = fibre holonomy? (boost ln q₀ + i·ln q₀/2)")
    print("=" * 78)
    q_pr, q_mu = q_at(50), q_muon_at(50)
    S_mu, S_pr = S(q_mu), S(q_pr)
    print(f"\n anchors: S(muon)={mp.nstr(S_mu,7)} (+)  S(proton)={mp.nstr(S_pr,7)} (−)")

    results = {}
    for name, q, Sv in [("muon", q_mu, S_mu), ("proton", q_pr, S_pr)]:
        L = mp.log(q)
        u = mp.mpc(L, L / 2)  # boost + fibre spin
        v = imV41(u)
        ratio = mp.im(u) / mp.re(u)
        boost_dom = mp.re(u) ** 2 > mp.im(u) ** 2
        print(f"  {name}: u = ln q₀ + i·(ln q₀/2), Im u/Re u = {mp.nstr(ratio,4)}, "
              f"Im 𝔙₄₁ = {mp.nstr(v,7)}  [{'boost-dom, Im 𝔙>0' if boost_dom else 'spin-dom'}]  "
              f"sign-match S={v*Sv>0}")
        results[name] = (float(v), bool(boost_dom), bool(v * Sv > 0))

    # SP1a: fibre spin < boost (ratio 1/2)
    sp1a = abs(mp.im(mp.mpc(mp.log(q_mu), mp.log(q_mu) / 2)) /
               mp.re(mp.mpc(mp.log(q_mu), mp.log(q_mu) / 2)) - mp.mpf("0.5")) < mp.mpf("1e-30")
    # SP1b: Im V > 0 both anchors ⇒ can't reach proton S<0 ⇒ refuted
    sp1b_both_pos = results["muon"][0] > 0 and results["proton"][0] > 0
    sp1b_proton_wrong = not results["proton"][2]
    # SP1c: full fibre angle only reaches the diagonal (Im V = 0), not past
    u_full = mp.mpc(mp.log(q_mu), mp.log(q_mu))
    sp1c_diag = abs(imV41(u_full)) < mp.mpf("1e-30")

    print("\n ⇒ smooth boost+fibre-spin candidate REFUTED (scope-(a)): Im u ≤ Re u ⇒ Im 𝔙₄₁ ≥ 0")
    print("   at both anchors, cannot reach S(proton)<0. Diagonal-crossing needs Im u > Re u = ln q₀,")
    print("   which no smooth geometric holonomy from q₀≈1.11 supplies. SP2 (non-smooth/resonance")
    print("   hypersensitive spin part) is the open crux.")

    wb = WitnessBuilder("qbeta-spin-part-udeform", engine="mpmath")
    wb.set_description(
        "SP1 of the u(q₀) spin-part derivation (#4401 continuation of #4391). Tests the "
        "geometric fibre-spin candidate u = ln q₀ + i·(ln q₀/2) (fibre holonomy "
        "q_b=e^{i·ln q₀/2}, |q_b|=1) under Im 𝔙₄₁=(√3/4)(Re²u−Im²u). Fibre spin angle "
        "ln q₀/2 < boost ln q₀ ⇒ Im u<Re u ⇒ Im 𝔙₄₁>0 at both anchors ⇒ cannot reach "
        "S(proton)<0: smooth boost+fibre-spin REFUTED (scope-(a)). Diagonal-crossing needs "
        "Im u>Re u=ln q₀ (even full fibre angle only reaches the diagonal, Im 𝔙=0). ⇒ the "
        "sign-flip spin part must be NON-smooth/resonance + hypersensitive (SP2, open). No "
        "fit, no c_k, no instance.")
    wb.set_content_block("conj:binding-qbeta-complex-volume")
    wb.add_data("fibre_spin_readout", {
        "imV41_muon_boost_plus_fibrespin": mp.nstr(mp.mpf(results["muon"][0]), 10),
        "imV41_proton_boost_plus_fibrespin": mp.nstr(mp.mpf(results["proton"][0]), 10),
        "Im_over_Re_ratio": "0.5",
        "diagonal_needs_Im_over_Re_gt": "1.0 (Im u > Re u = ln q₀)",
        "verdict": ("smooth boost+fibre-spin refuted scope-(a): Im 𝔙₄₁>0 both anchors; "
                    "sign-flip needs non-smooth/resonance hypersensitive spin part (SP2 open)")})
    wb.add_assertion("fibre_spin_ratio_half", str(bool(sp1a)), "True")
    wb.add_assertion("imV_positive_both_anchors_refutes_smooth", str(bool(sp1b_both_pos)), "True")
    wb.add_assertion("proton_sign_unreachable_by_smooth_spin", str(bool(sp1b_proton_wrong)), "True")
    wb.add_assertion("full_fibre_angle_only_reaches_diagonal", str(bool(sp1c_diag)), "True")
    wb.save()
    print("\nwitness → qbeta-spin-part-udeform.witness.json")
    ok = all([sp1a, sp1b_both_pos, sp1b_proton_wrong, sp1c_diag])
    print("ALL ASSERTIONS PASS" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
