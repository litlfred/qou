#!/usr/bin/env python3
"""qbeta_c3_geometry_derived_argument_probe.py

CORRECTION (2026-07-26)
=======================
This is the THIRD probe that carried the WRONG figure-eight NZ leading Im form
  WRONG:  Im 𝔙 ≈ (√3/2)|u|²·sin(2 arg u) = √3·Re(u)·Im(u)   (implies a REAL a₂)
(the other two — qbeta_udeform_map_constraint_probe.py and
qbeta_c3_barodd_gluing_newton_solve.py — were fixed in PR #4372). The figure-
eight cusp modulus is τ = −i√3 (CCGLS A-polynomial, ℚ(√−3)), so the leading
complex-volume coefficient a₂ = 𝔙″(0)/2 is PURELY IMAGINARY, a₂ = i·√3/4, hence
  RIGHT:  Im 𝔙₄₁(u) = (√3/4)(Re²u − Im²u)
proved sorry-free as `imV₄₁` in
  content/quantum-observable-universe/lean/QOU/Knot/FigureEightComplexVolume.lean
Audit: docs/audits/2026-07-26-sdeformed-channel-signflip.md.
Authoritative corrected geometry-side readout (this probe AGREES with it):
  computations/qbeta/qbeta_geometric_boost_udeform_probe.py.

CONSEQUENCE of the correction (the whole "silent" story inverts):
  * Under the WRONG form, a REAL u = ln q₀ (arg u = 0) gave Im 𝔙 = 0 — hence the
    prior claim "real m are silent; only complex m carry signal". That reasoning
    is FALSE. Under the CORRECT form a REAL boost u = ln q₀ gives
      Im 𝔙₄₁(ln q₀) = (√3/4)(ln q₀)² > 0  — NONZERO,
    muon-sign-correct and the right ballpark (~0.49×S(muon), matching the
    sibling probe).
  * It is instead the OLD named complex readout set (substrate qty × the b-map
    phase e^{iπ/4}) that is now near-SILENT: arg u = π/4 is exactly the DIAGONAL
    |Re u| = |Im u| where Im 𝔙₄₁ VANISHES (cos 2·(π/4) = 0). The e^{iπ/4} phase
    that MAXIMISED the wrong sin(2 arg u) sits on the null diagonal of the
    correct cos(2 arg u). So the phase-π/4 candidates carry no signal, and the
    real boost does.

HONEST SCOPE OF THE READOUT (unchanged where correct):
  * The figure-eight REAL volume Vol(m) is computed EXACTLY by the validated
    gluing-equation Newton solver (qbeta_c3_barodd_gluing_newton_solve.vol_of_m):
    solve z(z−1)w(w−1)=1 (w=m²z), then Vol = D(z)+D(w) (Bloch–Wigner). This is
    the genuine solver output and is reported as `Vol_exact` — UNCHANGED by the
    correction (only the Im/CS leading form was wrong).
  * The bar-odd S candidate is Im 𝔙 (the Chern–Simons companion). The EXACT CS
    from the two tetrahedron shapes needs Neumann's extended-Bloch flattening,
    which is NOT implemented here; we use the CORRECTED LEADING NZ form
    Im 𝔙₄₁ = (√3/4)(Re²u − Im²u) (a₂ = i√3/4, cusp modulus, derived,
    parameter-free), reported as `ImV_leading` and explicitly leading-order.

TARGETS (scope-(a); C14; no c_k wired; no fit):
  S(muon)=+0.00968298, S(proton)=−0.03945936, and the un-levered residual
  r = S·u³ with u = ln q₀ (as computed here): r(muon)≈+1.10e-5, r(proton)≈−4.48e-5.

READOUT SETS:
  (A) the REAL geometric boost u = ln q₀ (meridian-holonomy-boost.md: the cusp-
      torus meridian holonomy IS multiplication by q₀, a hyperbolic boost of
      rapidity ln q₀ at real q₀>1). Under the CORRECT form this is NONZERO and
      carries the muon-sign+ballpark signal.
  (B) the OLD named set of principled complex meridian holonomies m (substrate
      quantity × the pinned b-map phase e^{iπ/4}). Kept for continuity — the
      correction shows they land on/near the null DIAGONAL and are silent.

GATE (zero-parameter): CANDIDATE iff, at BOTH anchors, |ImV_leading/S − 1| < 1e-3
AND sign(ImV_leading) = sign(S). Expected honest negative (scope-(a)): the real
boost hits the muon sign+ballpark but is NEARLY CONSTANT across the ~1e-8-apart
anchor q₀'s (real boost cannot sign-flip), and the complex phase-π/4 set is on
the null diagonal; the anchor-dependent sign-flip needs the boost→spin
transition (a complex/spin part crossing the diagonal), which is the open
u(q₀) — NOT fitted here.
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

# The MUON leg read BY NAME (bean qou-9ugp, 2026-09-04). It was the literal
# 1.1099785955573347..., the RETIRED self-certified pin A -- retired 2026-08-22
# when the muon anchor was re-derived to the CODATA-2022 lepton ratio. This is a
# DELIBERATE two-pin comparison, so the fix is the live MUON value, not proton:
# swapping in the proton pin would delete the comparison this probe exists for.
# The stale leg understated the mu-p separation by 0.67% (11.5371 vs 11.6141
# ppb) -- the fourth instance of that class found in this drain.
import sys as _sys_qm  # noqa: E402
from pathlib import Path as _Path_qm  # noqa: E402
for _p_qm in (_Path_qm(__file__).resolve().parent,
              _Path_qm(__file__).resolve().parent.parent,
              _Path_qm(__file__).resolve().parent.parent / 'substrate'):
    if str(_p_qm) not in _sys_qm.path:
        _sys_qm.path.insert(0, str(_p_qm))
from q_parameter import q_muon_at as _q_muon_at  # noqa: E402
Q_MUON_LIVE_STR = str(_q_muon_at(50))

# Match the qou_substrate serialization precision the witness metadata records,
# so compute_dps and the witness agree (review: no silent 40-vs-70 mismatch).
mp.mp.dps = 70

Q = {"muon": mp.mpf(Q_MUON_LIVE_STR),
     "proton": mp.mpf("1.1099785827513808075916690956107688798744991218736")}
S_TARGET = {"muon": mp.mpf("0.00968298"), "proton": mp.mpf("-0.03945936")}
PHASE = mp.e ** (mp.mpc(0, 1) * mp.pi / 4)   # the pinned b-map phase
KAPPA = mp.sqrt(3) / 4   # |a₂|, the (purely imaginary) NZ leading coeff magnitude


def cs_leading(u):
    """CORRECTED leading NZ Im 𝔙₄₁ = (√3/4)(Re²u − Im²u) — a₂ = i√3/4 purely
    imaginary (cusp modulus τ=−i√3). Leading-order, NOT exact CS.
    Ref: QOU.Knot.FigureEightComplexVolume.imV₄₁ (#4372). Supersedes the WRONG
    (√3/2)|u|²·sin(2 arg u) = √3·Re·Im form (which corresponds to a REAL a₂)."""
    u = mp.mpc(u)
    return KAPPA * (mp.re(u) ** 2 - mp.im(u) ** 2)


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
    print(" c₃ bar-odd S — GEOMETRY-side one-shot (exact Vol via solver; Im 𝔙 CORRECTED)")
    print(" CORRECTED form Im 𝔙₄₁ = (√3/4)(Re²u − Im²u)  (imV₄₁, #4372) — supersedes")
    print(" the wrong √3·Re·Im. Real boost u=ln q₀ now NONZERO; phase-π/4 set silent.")
    print("=" * 78)

    r_target = {a: S_TARGET[a] * (mp.log(Q[a])) ** 3 for a in Q}
    print("\n targets (u = ln q₀):")
    for a in ("muon", "proton"):
        print(f"   {a:7s}: S={mp.nstr(S_TARGET[a],6):>12}   r=S·u³={mp.nstr(r_target[a],6)}")

    # ---- (A) REAL geometric boost u = ln q₀ (the corrected, non-silent readout) ----
    print("\n (A) REAL geometric boost u = ln q₀ (meridian-holonomy-boost.md);"
          " corrected Im 𝔙₄₁ = (√3/4)(ln q₀)²:")
    real_readout = {}
    for a in ("muon", "proton"):
        u_real = mp.mpc(mp.log(Q[a]), 0)
        imV = cs_leading(u_real)
        ratio = imV / S_TARGET[a]
        real_readout[a] = {"u_ln_q0": u_real, "imV": imV, "ratio_imV_over_S": ratio}
        print(f"   {a:7s}: u=ln q₀={mp.nstr(mp.re(u_real),8)}  Im 𝔙₄₁=+{mp.nstr(imV,7)}"
              f"  S={mp.nstr(S_TARGET[a],7)}  Im 𝔙/S={mp.nstr(ratio,5)}"
              f"  sign-match={bool(mp.sign(imV) == mp.sign(S_TARGET[a]))}")
    d_imV = real_readout["proton"]["imV"] - real_readout["muon"]["imV"]
    s_gap = S_TARGET["muon"] - S_TARGET["proton"]
    print(f"   Δ Im 𝔙₄₁(real, muon→proton) = {mp.nstr(d_imV,4)}  ≪  |S gap| ="
          f" {mp.nstr(mp.fabs(s_gap),4)}  ⇒ nearly CONSTANT across anchors.")
    # corrected findings on the REAL boost
    g_muon_sign = (real_readout["muon"]["imV"] > 0 and S_TARGET["muon"] > 0)
    g_muon_ballpark = mp.mpf("0.2") < real_readout["muon"]["ratio_imV_over_S"] < mp.mpf("5")
    g_proton_wrong_sign = not (real_readout["proton"]["imV"] * S_TARGET["proton"] > 0)
    g_nearly_const = mp.fabs(d_imV) < mp.fabs(s_gap) / 100

    # ---- (B) OLD named complex set: now on/near the null diagonal (silent) ----
    rows, any_candidate = [], False
    print("\n (B) named complex m (substrate qty × e^{iπ/4}): arg u=π/4 is the null")
    print("     DIAGONAL of the corrected form (cos 2·π/4 = 0) ⇒ Im 𝔙₄₁ ≈ 0:")
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
            imV[a] = cs_leading(uc)              # CORRECTED leading-order Im 𝔙 (labeled)

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
          else "clean geometry-side NEGATIVE — no readout reproduces S at BOTH anchors.")
    print(" Corrected reading: the REAL boost u=ln q₀ hits the muon SIGN + ballpark")
    print(f" (Im 𝔙₄₁/S(muon) = {mp.nstr(real_readout['muon']['ratio_imV_over_S'],4)}), but is")
    print(" REFUTED as the full map (scope-(a)): nearly constant across the ~1e-8-apart")
    print(" anchors, so it cannot give S(proton)<0. The phase-π/4 complex set sits on the")
    print(" null diagonal (Im 𝔙₄₁≈0). The S(muon)>0>S(proton) sign-flip needs the")
    print(" boost→spin transition — a complex/spin part crossing the diagonal |Re u|=|Im u|")
    print(" — which is the OPEN u(q₀), NOT fitted here (agrees with the sibling probe).")

    wb = WitnessBuilder("qbeta-c3-geometry-derived-argument", engine="mpmath")
    wb.set_description(
        "Geometry-side one-shot for c₃ bar-odd S, CORRECTED to the figure-eight NZ "
        "leading form Im 𝔙₄₁ = (√3/4)(Re²u − Im²u) (a₂ = i√3/4, cusp modulus τ=−i√3; "
        "QOU.Knot.FigureEightComplexVolume.imV₄₁, #4372) — supersedes the WRONG "
        "√3·Re·Im form this probe previously carried (third such probe; the other two "
        "fixed in #4372). Vol_exact from the validated gluing Newton solver (vol_of_m), "
        "UNCHANGED. Corrected consequence: the REAL boost u=ln q₀ gives Im 𝔙₄₁=(√3/4)"
        "(ln q₀)²>0 (NONZERO; ~0.49×S(muon), muon-sign-correct) — the prior 'real m are "
        "silent' reasoning was a wrong-form artefact. The named complex phase-e^{iπ/4} "
        "set now lands on the null DIAGONAL (Im 𝔙₄₁≈0). Clean scope-(a) negative on the "
        "zero-parameter both-anchor gate: real boost is muon-sign+ballpark but nearly "
        "constant across anchors (cannot sign-flip); the flip needs the boost→spin "
        "complex part crossing the diagonal — the OPEN u(q₀). Agrees with the sibling "
        "qbeta_geometric_boost_udeform_probe.py. Scope-(a); C14; no c_k wired; no "
        "SDeformedVolumeChannel instance; u(q₀) open; no fit; dps=70 matches witness meta."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")
    wb.add_data("targets", {"S": {a: mp.nstr(S_TARGET[a], 8) for a in Q},
                            "r_S_u3_u_is_ln_q0": {a: mp.nstr(r_target[a], 8) for a in Q}})
    wb.add_data("real_boost_readout", {
        a: {"u_ln_q0": mp.nstr(mp.re(real_readout[a]["u_ln_q0"]), 12),
            "imV41": mp.nstr(real_readout[a]["imV"], 12),
            "S": mp.nstr(S_TARGET[a], 12),
            "imV41_over_S": mp.nstr(real_readout[a]["ratio_imV_over_S"], 8)}
        for a in ("muon", "proton")})
    wb.add_data("delta_imV41_across_anchors_real_boost", mp.nstr(d_imV, 8))
    wb.add_data("complex_phase_pi4_readouts", rows)
    wb.add_data("verdict", "candidate" if any_candidate else "clean_negative")
    # ---- assertions: the CORRECTED outcome (no assertion encodes the old wrong claim) ----
    # Corrected: real boost is NONZERO (kills the old "real gives zero / silent" claim).
    wb.add_assertion("real_boost_imV_nonzero_positive",
                     computed=1.0 if real_readout["muon"]["imV"] > 0 else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="Im 𝔙₄₁(ln q₀) = (√3/4)(ln q₀)² > 0 under the corrected form "
                            "(imV₄₁) — supersedes the wrong-form 'real m silent' claim")
    wb.add_assertion("real_boost_muon_sign_correct",
                     computed=1.0 if g_muon_sign else 0.0, expected=1.0, tolerance=0.5,
                     source="sign(Im 𝔙₄₁(ln q_muon)) = sign(S(muon)) > 0")
    wb.add_assertion("real_boost_muon_ballpark",
                     computed=1.0 if g_muon_ballpark else 0.0, expected=1.0, tolerance=0.5,
                     source="Im 𝔙₄₁/S(muon) = "
                            + mp.nstr(real_readout["muon"]["ratio_imV_over_S"], 5))
    wb.add_assertion("real_boost_wrong_sign_at_proton",
                     computed=1.0 if g_proton_wrong_sign else 0.0, expected=1.0, tolerance=0.5,
                     source="real boost gives Im 𝔙₄₁>0 at proton but S(proton)<0")
    wb.add_assertion("real_boost_nearly_constant_refuted_as_full_map",
                     computed=1.0 if g_nearly_const else 0.0, expected=1.0, tolerance=0.5,
                     source="Δ Im 𝔙₄₁(real) = " + mp.nstr(d_imV, 4)
                            + " ≪ |S gap| = " + mp.nstr(mp.fabs(s_gap), 4))
    # The zero-parameter both-anchor gate still yields no candidate (clean negative).
    wb.add_assertion("no_candidate_found",
                     computed=0.0 if any_candidate else 1.0, expected=1.0, tolerance=0.5,
                     source="zero-parameter gate (magnitude+sign at both anchors) yields no "
                            "candidate; sign-flip needs the open diagonal-crossing u(q₀)")
    wb.save()
    ok = all([g_muon_sign, g_muon_ballpark, g_proton_wrong_sign, g_nearly_const,
              real_readout["muon"]["imV"] > 0, not any_candidate])
    print("\nwitness → qbeta-c3-geometry-derived-argument.witness.json")
    print("ALL ASSERTIONS PASS" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
