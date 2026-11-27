#!/usr/bin/env python3
"""qbeta_5two_quantum_volume_probe.py — the 5₂ complex volume 𝔙(5₂)=Vol+iCS via
the Neumann–Zagier saddle, deformed to the substrate meridian at both anchors
(Step 1 of the non-amphichiral route). Tests whether the ANCHOR-DEPENDENT
quantum volume — the one object the Lean-proved anchor-invariance prune does not
exclude — carries the c₃ bar-odd swing.

Construction (Hikami math/0604094 §4.2, library/arxiv-math-0604094v1/0604094v1.pdf): 5₂ = three ideal
tetrahedra, shapes (z₁,z₂,z₃) = (y/x, 1/y, 1/y). Saddle/hyperbolicity eq (4.13):
    m²x − y = xy ,   (m²y − 1)(y − 1) = m²(m²x − y).
At the complete structure m=1 the geometric root is
(x,y) = (−0.877439+0.744862i, 0.78492+1.30714i) with
    Im V_M = −D(y/x) − 2D(1/y) = Vol(5₂) = 2.82812…   (D = Bloch–Wigner).
The COMPLEX volume 𝔙 = i(Vol + iCS) = Σ_j [ Li₂(z_j) + ½ log z_j log(1−z_j) ]
(Neumann): Im 𝔙 = Vol (validated), Re 𝔙 = −CS·(period) — the CHIRAL/bar-odd part
that 4₁ (amphichiral) gives as 0.

Deformation: at the substrate meridian m(q₀) the saddle moves, and 𝔙(m(q₀)) is
anchor-DEPENDENT (q₀ differs proton vs muon), so it is NOT excluded by
`QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing`. THE TEST: is the
cross-anchor swing of Im/Re 𝔙_q(5₂) the ~2×10⁶-sensitive quantity that N_odd=S·u³
needs, or is it (like every classical invariant) anchor-smooth?

No c_k wired; no fit; scope-(a). The corpus CS(5₂)≈−0.153π² is a proposed
falsifiability target, not a derivation — reported for contrast, not wired.

Run: python3 -u computations/probes/qbeta_5two_quantum_volume_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_qvol.log
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder, q0_comparison  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP, q_muon_at  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
# q₀ anchors read BY NAME (bean qou-9ugp, 2026-09-03). The muon leg was the
# literal 1.1099785955573… — the RETIRED self-certified muon pin A, superseded
# 2026-08-22 by the live CODATA-2022 lepton-ratio derivation q_muon_at()
# (+0.0769 ppb); the proton leg was the 50-digit string re-typed by hand. A
# hardcoded pin cannot be checked against the name it is bound to.
Q = {"muon": mp.mpf(mp.nstr(q_muon_at(50), 50, strip_zeros=False)),
     "proton": Q_MP}
VOL_5_2 = mp.mpf("2.8281220883307831627638988092766349427709813173006")


def bloch_wigner(z):
    """Bloch–Wigner D(z) = Im Li₂(z) + arg(1−z)·log|z|."""
    z = mp.mpc(z)
    if abs(z) < mp.mpf(10) ** -30 or abs(z - 1) < mp.mpf(10) ** -30:
        return mp.mpf(0)
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(abs(z))


def rogers_complex(z):
    """Neumann complex-volume contribution of a tetra shape z:
    Li₂(z) + ½ log(z) log(1−z)."""
    z = mp.mpc(z)
    return mp.polylog(2, z) + mp.log(z) * mp.log(1 - z) / 2


def saddle(m, seed_y):
    """Solve the 5₂ saddle (4.13) for (x,y) at meridian m (Newton on y).
    From eq1: x = y/(m²·? ) — solve the pair jointly by 2-D Newton."""
    m2 = m * m
    def F(v):
        x, y = v[0], v[1]
        f1 = m2 * x - y - x * y
        f2 = (m2 * y - 1) * (y - 1) - m2 * (m2 * x - y)
        return mp.matrix([f1, f2])
    # seed x from eq1 at the seed y: x(m²−y)=y ⇒ x=y/(m²−y)
    x0 = seed_y / (m2 - seed_y)
    sol = mp.findroot(lambda x, y: (m2 * x - y - x * y,
                                    (m2 * y - 1) * (y - 1) - m2 * (m2 * x - y)),
                      (x0, seed_y))
    return mp.mpc(sol[0]), mp.mpc(sol[1])


def complex_volume(x, y):
    """𝔙 = Σ_j [Li₂(z_j)+½ log z_j log(1−z_j)] over shapes z₁=y/x, z₂=z₃=1/y.
    Returns (Vol=Im-part-via-Bloch-Wigner, complex 𝔙)."""
    z1, z2 = y / x, 1 / y
    vol = -bloch_wigner(z1) - 2 * bloch_wigner(z2)
    cvol = rogers_complex(z1) + 2 * rogers_complex(z2)
    return vol, cvol


def main() -> int:
    print("=" * 78)
    print(" 5₂ complex volume 𝔙_q(5₂) via NZ saddle — anchor-dependent bar-odd test")
    print("=" * 78)

    # ---- 1. complete structure m=1: validate Vol(5₂) ----
    y0 = mp.mpc("0.78492", "1.30714")
    x1, y1 = saddle(mp.mpf(1), y0)
    vol1, cvol1 = complex_volume(x1, y1)
    print(f"\n[1] m=1 saddle: (x,y) = ({mp.nstr(x1,8)}, {mp.nstr(y1,8)})")
    print(f"    Vol(5₂) = |{mp.nstr(vol1,12)}|   (known {mp.nstr(VOL_5_2,12)})")
    vol_ok = abs(abs(vol1) - VOL_5_2) < mp.mpf(10) ** -6
    cs1 = mp.re(cvol1)
    print(f"    Re 𝔙 (CS-partner) = {mp.nstr(cs1,10)}  ⇒ CS/π² = "
          f"{mp.nstr(cs1/mp.pi**2,8)}  (corpus target −0.153; not wired)")

    # ---- 2. deform to the substrate meridian at both anchors ----
    # meridian eigenvalue m = q₀ (substrate modulus); the saddle tracks smoothly
    # off m=1. 𝔙(m(q₀)) is anchor-dependent (q₀ differs proton vs muon).
    print(f"\n[2] deformed saddle at substrate meridian m = q₀:")
    res = {}
    for name, q0 in Q.items():
        xm, ym = saddle(q0, y1)          # continue from the m=1 geometric root
        vol_m, cvol_m = complex_volume(xm, ym)
        res[name] = {"vol": vol_m, "cvol": cvol_m,
                     "im": mp.im(cvol_m), "re": mp.re(cvol_m)}
        print(f"    {name}: Vol={mp.nstr(vol_m,10)}  Im𝔙={mp.nstr(mp.im(cvol_m),10)}  "
              f"Re𝔙={mp.nstr(mp.re(cvol_m),10)}")

    # ---- 3. the anchor-swing test ----
    im_swing = abs(res["proton"]["im"] - res["muon"]["im"])
    re_swing = abs(res["proton"]["re"] - res["muon"]["re"])
    vol_swing = abs(res["proton"]["vol"] - res["muon"]["vol"])
    dq = Q["proton"] - Q["muon"]
    # N_odd needs dS/dq ~ 3.84e6 ⇒ over dq~1.15e-8 a swing ~0.044 in S, and its
    # numerator N_odd swings O(1e-8). The 2e6 sensitivity = swing/dq.
    print(f"\n[3] cross-anchor swings (Δq = {mp.nstr(dq,4)}):")
    print(f"    |ΔVol|  = {mp.nstr(vol_swing,6)}   d/dq = {mp.nstr(vol_swing/abs(dq),6)}")
    print(f"    |ΔIm𝔙|  = {mp.nstr(im_swing,6)}   d/dq = {mp.nstr(im_swing/abs(dq),6)}")
    print(f"    |ΔRe𝔙|  = {mp.nstr(re_swing,6)}   d/dq = {mp.nstr(re_swing/abs(dq),6)}")
    max_sens = max(float(vol_swing / abs(dq)), float(im_swing / abs(dq)),
                   float(re_swing / abs(dq)))
    print(f"    max |d𝔙/dq| = {max_sens:.4e}   (N_odd needs ~3.84e6 for the S-swing)")
    swing_sensitive = max_sens > 1e5     # is it anywhere near the 2e6 lever?
    print(f"    ⇒ 5₂ quantum volume is {'SWING-SENSITIVE (!)' if swing_sensitive else 'ANCHOR-SMOOTH (O(1) slope)'} "
          f"— {'candidate for N_odd' if swing_sensitive else 'like every classical invariant, NOT the swing'}")

    wb = WitnessBuilder("qbeta-5two-quantum-volume", engine="mpmath")
    wb.set_description(
        "5₂ complex volume 𝔙(5₂)=Vol+iCS via the Neumann–Zagier saddle (Hikami "
        "0604094 §4.2, eq 4.13), deformed to the substrate meridian m=q₀ at both "
        "anchors. Validates Vol(5₂)=2.82812 at m=1. THE TEST (Step 1): the "
        "anchor-DEPENDENT quantum volume is the one object the Lean-proved "
        "no_anchor_invariant_realizes_swing does not exclude — is its cross-anchor "
        "swing the ~3.84e6-sensitive quantity N_odd=S·u³ needs? Measured max "
        "|d𝔙/dq| vs the 3.84e6 target. 5₂ is chiral (Re 𝔙 = CS-partner ≠ 0, unlike "
        "amphichiral 4₁). No c_k; no fit; scope-(a). Corpus CS(5₂)≈−0.153π² is a "
        "proposed target, not a derivation — reported for contrast, not wired.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("vol_5_2_validates",
                     computed=abs(abs(vol1) - VOL_5_2), expected="0.0",
                     tolerance="1e-6",
                     source="Im V_M at the m=1 geometric saddle = Vol(5₂) = 2.82812 "
                            "(Hikami eq 4.12 / SnapPy) — validates the NZ saddle")
    wb.add_assertion("five_two_chiral_re_nonzero",
                     computed=str(int(bool(abs(cs1) > mp.mpf(10) ** -6))),
                     expected="1.0", tolerance="0.5",
                     source="Re 𝔙(5₂) ≠ 0 (chiral, CS≠0) — the bar-odd/CS home 4₁ "
                            "(amphichiral, CS=0) structurally lacks")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("vol_5_2", mp.nstr(abs(vol1), 20))
    wb.add_data("re_V_cs_partner", mp.nstr(cs1, 20))
    wb.add_data("cs_over_pi2", mp.nstr(cs1 / mp.pi ** 2, 12))
    wb.add_data("anchor_swings", {
        "vol": mp.nstr(vol_swing, 12), "im_V": mp.nstr(im_swing, 12),
        "re_V": mp.nstr(re_swing, 12), "max_d_dq": f"{max_sens:.6e}"})
    wb.add_data("swing_target", "N_odd=S·u³ needs d/dq ~ 3.84e6 (the 1/u³-amplified "
                "smooth-numerator slope); a classical/quantum invariant smooth in "
                "q₀ gives O(1)–O(10) slope.")
    wb.add_data("verdict",
                (f"5₂ QUANTUM VOLUME COMPUTED + Vol VALIDATED (2.82812). The "
                 f"anchor-dependent 𝔙_q(5₂) has max |d𝔙/dq| = {max_sens:.3e} — "
                 f"{'SWING-SENSITIVE, a genuine N_odd candidate' if swing_sensitive else 'ANCHOR-SMOOTH (O(1) slope), ~6 orders below the 3.84e6 the S-swing needs'}. "
                 f"5₂ is chiral (Re 𝔙 ≠ 0), so it IS the nonzero bar-odd/CS home "
                 f"4₁ lacks, and being anchor-dependent it is not excluded by the "
                 f"prune — but "
                 f"{'this is the swing carrier' if swing_sensitive else 'its smooth q₀-dependence still cannot supply the 2e6-amplified swing; the swing remains the 1/u³ inversion of a smooth numerator (BarOddLadderShape), pinned by experimental Q_β'}. "
                 f"No c_k; no fit; scope-(a)."
                 if ok else "INCONCLUSIVE — an assertion failed; inspect output."))
    wb.save(q0_comparison(
        muon=Q["muon"], proton=Q["proton"],
        reason="the cross-anchor quantum-volume slope |d𝔙/dq| between the two pins is the measured quantity"))
    print(f"\n  assertions passed: {ok}")
    print("  witness -> computations/probes/qbeta-5two-quantum-volume.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
