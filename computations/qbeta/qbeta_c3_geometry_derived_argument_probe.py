#!/usr/bin/env python3
"""qbeta_c3_geometry_derived_argument_probe.py

One disciplined shot at the c₃ bar-odd S from the GEOMETRY side, complementing
the merged 60-argument Φ_b *analysis* scan (qbeta_c3_phib_argument_scan.py).

HONEST SCOPE OF THE READOUT (addressing review):
  * The figure-eight REAL volume Vol(m) is computed EXACTLY by the validated
    gluing-equation Newton solver (qbeta_c3_barodd_gluing_newton_solve.vol_of_m):
    solve z(z−1)w(w−1)=1 (w=m²z), then Vol = D(z)+D(w) (Bloch–Wigner). This is
    the genuine solver output and is reported as `Vol_exact`.
  * The bar-odd S candidate is Im 𝔙 (the Chern–Simons companion). The EXACT CS
    from the two tetrahedron shapes needs Neumann's extended-Bloch flattening,
    which is NOT implemented here; we use the LEADING NZ form
    Im 𝔙 ≈ (√3/2)|u|²·sin(2 arg u) (cusp shape √−3, derived, parameter-free).
    This is reported as `ImV_leading` and is explicitly leading-order — NOT the
    full solver output. (Implementing the exact flattening is the noted extension.)

TARGETS (scope-(a); C14; no c_k wired; no fit):
  S(muon)=+0.00968298, S(proton)=−0.03945936, and the un-levered residual
  r = S·u³ with u = ln q₀ (as computed here): r(muon)≈+1.10e-5, r(proton)≈−4.48e-5.
  (These ~1e-5 values are for u=ln q₀; the sibling scan's ~1e-9 figures used a
  different u convention — not reused here to avoid the mismatch.)

READOUT SET: a small NAMED set of principled complex substrate meridian
holonomies m (substrate quantity × the pinned b-map phase e^{iπ/4}, from
phi_b_substrate_regime.py: b²=i·t/(2π), t=ln q₀). Real m give Im 𝔙 = 0
(arg u = 0), so only complex m carry signal — the honest reason the
real-substrate readout is silent.

GATE (zero-parameter): CANDIDATE iff, at BOTH anchors, |ImV_leading/S − 1| < 1e-3
AND sign(ImV_leading) = sign(S). Otherwise the honest geometry-side data point
(expected negative: the same q₀→m map is the open volume-conjecture link, so the
anchor-dependent sign-flip cannot appear in a smooth readout).
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from qbeta_c3_barodd_gluing_newton_solve import vol_of_m  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# Match the qou_substrate serialization precision the witness metadata records,
# so compute_dps and the witness agree (review: no silent 40-vs-70 mismatch).
mp.mp.dps = 70

Q = {"muon": mp.mpf("1.10997859555733471"),
     "proton": mp.mpf("1.1099785827513808075916690956107688798744991218736")}
S_TARGET = {"muon": mp.mpf("0.00968298"), "proton": mp.mpf("-0.03945936")}
PHASE = mp.e ** (mp.mpc(0, 1) * mp.pi / 4)   # the pinned b-map phase


def cs_leading(u):
    """Leading NZ Im 𝔙 = (√3/2)|u|² sin(2 arg u) — leading-order, NOT exact CS."""
    return (mp.sqrt(3) / 2) * mp.fabs(u) ** 2 * mp.sin(2 * mp.arg(u))


def m_candidates(q0):
    """Named principled complex meridian holonomies (substrate qty × b-map phase)."""
    t = mp.log(q0)
    hbar_q = 1 - 1 / q0
    return {
        "u=t·e^{iπ/4}": t * PHASE,
        "u=2t·e^{iπ/4}": 2 * t * PHASE,
        "u=ℏ_q²·e^{iπ/4}": hbar_q ** 2 * PHASE,
        "u=b² (=i·t/2π)": mp.mpc(0, 1) * t / (2 * mp.pi),
        "u=2πb²·e^{iπ/4}": t * mp.mpc(0, 1) * PHASE,
    }


def main() -> int:
    print("=" * 78)
    print(" c₃ bar-odd S — GEOMETRY-side one-shot (exact Vol via solver; Im 𝔙 leading)")
    print("=" * 78)

    r_target = {a: S_TARGET[a] * (mp.log(Q[a])) ** 3 for a in Q}
    print("\n targets (u = ln q₀):")
    for a in ("muon", "proton"):
        print(f"   {a:7s}: S={mp.nstr(S_TARGET[a],6):>12}   r=S·u³={mp.nstr(r_target[a],6)}")

    rows, any_candidate = [], False
    print("\n readouts (Vol_exact = gluing solver; ImV_leading = (√3/2)|u|²sin2φ):")
    for name in m_candidates(Q["muon"]):
        imV, volx = {}, {}
        for a in ("muon", "proton"):
            uc = m_candidates(Q[a])[name]
            m = mp.e ** (uc / 2)
            try:
                vol, z, w = vol_of_m(m)          # genuine solver output (real Vol)
                volx[a] = mp.re(vol)
            except Exception:
                volx[a] = mp.mpf("nan")
            imV[a] = cs_leading(uc)              # leading-order Im 𝔙 (labeled)

        def match(a):
            t = S_TARGET[a]
            if t == 0:
                return False
            same_sign = (mp.sign(mp.re(imV[a])) == mp.sign(t))
            return same_sign and float(mp.fabs(imV[a] / t - 1)) < 1e-3
        cand = all(match(a) for a in ("muon", "proton"))
        any_candidate = any_candidate or cand
        eS = max(float(mp.fabs(imV[a] / S_TARGET[a] - 1)) for a in ("muon", "proton"))
        print(f"   {name:22s}: ImV_lead(μ)={mp.nstr(imV['muon'],5):>11} "
              f"(p)={mp.nstr(imV['proton'],5):>11}  Vol_exact(μ)={mp.nstr(volx['muon'],7)}  "
              f"|ΔS|max={eS:.2e} {'CANDIDATE' if cand else '—'}")
        rows.append({"argument": name,
                     "ImV_leading_muon": mp.nstr(imV["muon"], 12),
                     "ImV_leading_proton": mp.nstr(imV["proton"], 12),
                     "Vol_exact_muon": mp.nstr(volx["muon"], 12),
                     "Vol_exact_proton": mp.nstr(volx["proton"], 12),
                     "relerr_S_max": eS, "candidate": cand})

    print("\n VERDICT:", "CANDIDATE (near-match tier — verify)" if any_candidate
          else "clean geometry-side NEGATIVE — no principled complex m reproduces S.")
    print(" ImV_leading is anchor-smooth (anchors differ ~1e-8) ⇒ cannot produce the")
    print(" S(muon)>0>S(proton) sign-flip; the near-singular q₀→m map (open volume")
    print(" conjecture) is required. u=t·e^{iπ/4} matches S magnitude (~3%) but not sign.")

    wb = WitnessBuilder("qbeta-c3-geometry-derived-argument", engine="mpmath")
    wb.set_description(
        "Geometry-side one-shot for c₃ bar-odd S. Vol_exact from the validated "
        "gluing Newton solver (vol_of_m); Im 𝔙 candidate = LEADING NZ form "
        "(√3/2)|u|²sin(2 arg u) (exact CS via Neumann flattening not implemented — "
        "noted extension). Scored vs S at both anchors over a small named set of "
        "principled complex meridian holonomies (substrate qty × b-map phase "
        "e^{iπ/4}). Gate requires magnitude AND sign at both anchors. Clean "
        "negative: magnitude reproducible, sign-flip needs the open q₀→m map. "
        "Scope-(a); C14; no c_k wired; no fit; dps=70 matches witness metadata."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")
    wb.add_data("targets", {"S": {a: mp.nstr(S_TARGET[a], 8) for a in Q},
                            "r_S_u3_u_is_ln_q0": {a: mp.nstr(r_target[a], 8) for a in Q}})
    wb.add_data("readouts", rows)
    wb.add_data("verdict", "candidate" if any_candidate else "clean_negative")
    # Assert the actual outcome: this one-shot records a clean negative.
    wb.add_assertion("no_candidate_found",
                     computed=0.0 if any_candidate else 1.0, expected=1.0, tolerance=0.5,
                     source="geometry-side gate (magnitude+sign at both anchors) yields no candidate")
    wb.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
