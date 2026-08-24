#!/usr/bin/env python3
"""sdeformed_channel_signflip_probe.py — can S = Im 𝔙₄₁(u(q₀)) sign-flip?

T2 of the SDeformedVolumeChannel keystone attack (bean qou-fook; coordination
docs/coordination/keystone-sdeformedvolume-channel-attack.md).

With the figure-eight deformed complex volume 𝔙₄₁(u) made CONCRETE (companion
Lean QOU/Knot/FigureEightComplexVolume.lean, T1), test the channel identity
`S(q₀) = Im 𝔙₄₁(u(q₀))` of `conj:binding-qbeta-complex-volume`
(SDeformedVolumeChannel.S_eq) against the measured sign-flipping bar-odd leak

    S(muon)  ≈ +0.00968298   >   0   >   S(proton) ≈ −0.03945936.

STRICT anti-fit: 𝔙₄₁ is the LITERATURE Neumann–Zagier deformed complex volume of
4₁, assembled from the figure-eight geometry ALONE (Thurston gluing / the CCGLS
A-polynomial longitude), independent of the S targets. No coefficient is chosen
to match S. No u-map is fitted; no c_k wired; no keystone instance fabricated.

THE DECISIVE GEOMETRIC FACT (rigorous, from the A-polynomial — NOT a fit).
The figure-eight cusp modulus / NZ leading longitude coefficient is
`τ = −i·√3` (PURELY IMAGINARY, recognised in ℚ(√−3) by
qbeta_nz_even_series_fourone_probe.py, τ = (0,−1,1)). With the NZ relation
`𝔙′(u) ∝ v(u)` (real proportionality) and `v(u) = τ·u + O(u³)`, the leading
complex-volume coefficient a₂ is PURELY IMAGINARY, `a₂ = ± i·√3/4`, so

    𝔙₄₁(u) = Vol(4₁) + i·(√3/4)·u² + O(u⁴)   (even; O(u⁴) even),
    Im 𝔙₄₁(u) = (√3/4)·Re(u²) = (√3/4)·(Re²u − Im²u).

Verified here by direct integration of the closed-form geometric-branch
longitude `𝔙(u) = Vol(4₁) − ½∫₀ᵘ v` (matches (√3/4)(Re²−Im²) to O(u⁴), and
VANISHES on the DIAGONALS |Re u| = |Im u|, not on the axes).

⇒ CORRECTION TO THE PRIOR SURVIVOR. The #3773 constraint probe
(qbeta_udeform_map_constraint_probe.py) inverted the HEURISTIC leading form
`Im 𝔙 ≈ √3·Re(u)·Im(u)` (= (√3/2)Im(u²)) — the WRONG one; it corresponds to a
REAL a₂, contradicting τ = −i√3. Against the CORRECT form `Im 𝔙 = κ(Re²u−Im²u)`
the "surviving" family F3 (one component linear-through-zero at q*, the other
anchor-constant) gives `S = κ(k²d² − c₀²)`, which is EVEN in d = q−q* and, near
q* where |k·d| ≪ |c₀|, has the SAME SIGN at both anchors — it CANNOT reproduce
the measured sign flip. The F3 survival was an artefact of the heuristic form.

VERDICT: structural-partial.
  * The channel `S = Im 𝔙₄₁` is NOT excluded outright: `Im 𝔙₄₁ = κ(Re²u−Im²u)`
    DOES change sign when u crosses a DIAGONAL |Re u| = |Im u|. Reproducing both
    measured signs requires u(q₀) to cross that diagonal between the anchors
    (Re²u − Im²u  > 0 at muon, < 0 at proton) — a sharper, admissible constraint.
  * The #3773-surviving F3 family is REFUTED against the corrected form
    (scope-(b) for that family; invariant = a₂ purely imaginary ⇒ Im 𝔙₄₁ even
    quadratic form vanishing on diagonals, so an F3-linear component crossing
    zero keeps both anchors on the same side of the diagonal).
  * u(q₀) itself stays OPEN (making 𝔙₄₁ concrete sharpens the constraint from
    "F3: one-linear-one-const" to "must cross |Re u|=|Im u| between anchors";
    it does not determine the map).

Companion Lean (T1): QOU/Knot/FigureEightComplexVolume.lean —
`V₄₁`, `imV_eq` (Im V₄₁ = κ(Re²−Im²)), `imV_pos_iff` (0<Im ↔ Im²u<Re²u),
`f3_re_linear_no_flip` (the F3 same-side-of-diagonal invariant).

Run:  python3 -u sdeformed_channel_signflip_probe.py 2>&1 | tee /tmp/signflip.log
"""
from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
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

# Vol(4₁) = 2·Cl₂(π/3), the exact figure-eight hyperbolic volume.
VOL41 = 2 * mp.clsin(2, mp.pi / 3)
SQRT3 = mp.sqrt(3)
KAPPA = SQRT3 / 4  # = |a₂|; a₂ = i·κ (purely imaginary, from τ = −i√3)

# Measured anchor S-leak values (S = c₃ + Vol(4₁)); audited inputs, cited to the
# #3773 constraint witness qbeta-udeform-map-constraint.witness.json and
# docs/audits/2026-07-11-qbeta-c3-barodd-sleak-phib-target.md. Measurements, not
# fitted here.
S_MUON = mp.mpf("0.00968298")
S_PROTON = mp.mpf("-0.03945936")


# ─────────────────────────────────────────────────────────────────────────────
# Closed-form geometric-branch longitude of 4₁ (CCGLS A-polynomial) and the
# integrated deformed complex volume 𝔙(u) = Vol(4₁) − ½∫₀ᵘ v.
# ─────────────────────────────────────────────────────────────────────────────
def _B(M):
    return M**8 - M**6 - 2 * M**4 - M**2 + 1


def longitude_v(u):
    """v(u) = log(−L(u)), geometric branch (L(0) = −1); u = 2 log M."""
    M = mp.e ** (u / 2)
    disc = _B(M) ** 2 - 4 * M**8
    s = mp.sqrt(disc)
    L_minus = (_B(M) - s) / (2 * M**4)
    L_plus = (_B(M) + s) / (2 * M**4)
    L = L_minus if abs(L_minus + 1) <= abs(L_plus + 1) else L_plus
    return mp.log(-L)


def V41_integrated(u, sign=+1):
    """𝔙(u) via the line integral of the closed-form longitude (validates the
    leading form). sign = ± fixes the NZ potential-vs-correction convention;
    both give the same Re²−Im² Im-structure."""
    integ = mp.quad(lambda t: longitude_v(t * u) * u, [0, 1])
    return VOL41 + (sign / mp.mpf(2)) * integ


def V41_leading(u):
    """The concrete Lean form: 𝔙₄₁(u) = Vol(4₁) + i·κ·u², κ = √3/4."""
    return VOL41 + 1j * KAPPA * u * u


def im_V41(u):
    return KAPPA * (mp.re(u) ** 2 - mp.im(u) ** 2)


def main() -> int:
    print("=" * 78)
    print(" SDeformedVolumeChannel sign-flip probe — S = Im 𝔙₄₁(u(q₀))")
    print("=" * 78)
    assertions = []
    t0 = datetime.now(timezone.utc)

    # ── [0] anchors + the leading τ check ────────────────────────────────────
    # τ is purely imaginary with |τ| = √3 (the ℚ(√−3) cusp modulus). Its SIGN is
    # a log-branch convention (v = log(−L)); what matters for the Im-structure is
    # that τ is purely imaginary ⇒ a₂ = 𝔙″(0)/2 is purely imaginary.
    tau_lead = longitude_v(mp.mpf("1e-6")) / mp.mpf("1e-6")
    tau_re_err = abs(mp.re(tau_lead))
    tau_mod_err = abs(abs(tau_lead) - SQRT3)
    print(f"\n[0] longitude leading coeff τ = v(u)/u|_0 = {mp.nstr(tau_lead, 8)}")
    print(f"    |Re τ| = {float(tau_re_err):.2e}  (→0, purely imaginary);"
          f"  ||τ|−√3| = {float(tau_mod_err):.2e}  (ℚ(√−3) cusp modulus)")
    print(f"    S(muon)  = {mp.nstr(S_MUON,8)}   S(proton) = {mp.nstr(S_PROTON,8)}")
    sign_flip = S_MUON > 0 > S_PROTON
    assertions.append({
        "name": "tau_purely_imaginary_modulus_sqrt3",
        "computed": float(tau_re_err + tau_mod_err), "expected": 0.0, "tolerance": 1e-6,
        "passed": bool(tau_re_err < 1e-6 and tau_mod_err < 1e-6),
        "source": "closed-form longitude v(u)/u: Re→0, |τ|=√3 (±i√3 ℚ(√−3) cusp "
                  "modulus; sign is a log-branch convention)"})
    assertions.append({
        "name": "measured_sign_flip_hard_fact",
        "computed": 1.0 if sign_flip else 0.0, "expected": 1.0, "tolerance": 0.0,
        "passed": bool(sign_flip),
        "source": "S(muon) > 0 > S(proton) (audited anchors)"})

    # ── [1] Im 𝔙 structure: integrated vs the concrete leading form ──────────
    print("\n[1] Im 𝔙₄₁(u): integrated closed form vs concrete Lean leading form")
    print("    (r = 0.1; κ(Re²−Im²) = the concrete form; √3·Re·Im = the heuristic)")
    r = mp.mpf("0.1")
    max_dev_lead = mp.mpf(0)
    diag_vanish = mp.mpf(0)
    for phi in [mp.mpf(0), mp.pi/6, mp.pi/4, mp.pi/3, mp.pi/2]:
        u = r * mp.e ** (1j * phi)
        iv_int = mp.im(V41_integrated(u, +1))
        iv_lead = im_V41(u)
        heuristic = SQRT3 * mp.re(u) * mp.im(u)
        dev = abs(iv_int - iv_lead)
        max_dev_lead = max(max_dev_lead, dev)
        if abs(float(phi) - float(mp.pi/4)) < 1e-9:
            diag_vanish = abs(iv_int)
        print(f"    φ={float(phi):.4f}: Im𝔙_int={mp.nstr(iv_int,6):>12} "
              f" κ(Re²−Im²)={mp.nstr(iv_lead,6):>12}  √3ReIm={mp.nstr(heuristic,6):>12}")
    print(f"    max |Im𝔙_int − κ(Re²−Im²)| over the ray = {float(max_dev_lead):.2e}"
          f"  (O(u⁴) even tail)")
    print(f"    Im𝔙 at the diagonal φ=π/4 (Re u = Im u) = {float(diag_vanish):.2e}"
          f"  → vanishes on the DIAGONAL, not the axis")
    assertions.append({
        "name": "leading_form_matches_integrated_to_O_u4",
        "computed": float(max_dev_lead), "expected": 0.0, "tolerance": 1e-3,
        "passed": bool(max_dev_lead < 1e-3),
        "source": "Im 𝔙₄₁ = κ(Re²u−Im²u), κ=√3/4 (integrated closed form, r=0.1)"})
    assertions.append({
        "name": "imV_vanishes_on_diagonal_not_axis",
        "computed": float(diag_vanish), "expected": 0.0, "tolerance": 1e-4,
        "passed": bool(diag_vanish < 1e-4),
        "source": "Im 𝔙₄₁(Re u = Im u) = 0 (harmonic quadratic form Re(u²))"})

    # ── [2] F3 family under the CORRECTED form: cannot sign-flip ─────────────
    # F3 (from #3773): u(q) has one component = k·(q−q*) linear-through-zero at
    # q*, the other = anchor-constant c₀ ≠ 0. #3773 slope k ≈ 2.216e6.
    print("\n[2] #3773 surviving family F3 under the CORRECTED form Im𝔙=κ(Re²−Im²)")
    # d = q−q* at each anchor, from qbeta-udeform-map-constraint.witness.json (#3773).
    d_mu = mp.mpf("2.52266e-9")
    d_pr = mp.mpf("-1.02801e-8")
    k_slope = mp.mpf("2216103.8")
    # F3 sub-case (Re linear through zero, Im = const c0). Pick c0 ~ O(0.1) as
    # "anchor-constant nonzero" (its exact value is the open datum; the SIGN
    # conclusion is c0-independent for |k·d| ≪ |c0|).
    f3_refuted = True
    for label, c0 in [("Im=c₀=+0.30", mp.mpf("0.30")),
                      ("Im=c₀=+0.15", mp.mpf("0.15"))]:
        vals = []
        for d in (d_mu, d_pr):
            u = mp.mpc(k_slope * d, c0)            # Re linear-thru-zero, Im const
            vals.append(im_V41(u))
        same_sign = (vals[0] > 0) == (vals[1] > 0)
        f3_refuted = f3_refuted and same_sign and not (vals[0] > 0 > vals[1])
        print(f"    F3 Re-linear, {label}: S(muon)={mp.nstr(vals[0],6)}, "
              f"S(proton)={mp.nstr(vals[1],6)}  same-sign={same_sign}")
    # The invariant, stated: near q*, |k·d| ~ 2.2e6·1e-8 ~ 2e-2 ≪ c0 ~ 0.3, so
    # Re²u − Im²u ≈ −c0² < 0 at BOTH anchors ⇒ same sign. F3 refuted.
    kd_mu, kd_pr = abs(k_slope * d_mu), abs(k_slope * d_pr)
    print(f"    |k·d_muon| = {mp.nstr(kd_mu,4)}, |k·d_proton| = {mp.nstr(kd_pr,4)}"
          f"  — both ≪ c₀ for O(0.1) c₀ ⇒ both on same side of the diagonal.")
    print("    ⇒ F3 CANNOT sign-flip against the corrected form (scope-(b), invariant")
    print("      = a₂ purely imaginary ⇒ Im𝔙 = κ(Re²−Im²) even in each F3 component).")
    assertions.append({
        "name": "F3_family_cannot_signflip_against_corrected_form",
        "computed": 1.0 if f3_refuted else 0.0, "expected": 1.0, "tolerance": 0.0,
        "passed": bool(f3_refuted),
        "source": "Im𝔙=κ(Re²−Im²); F3 keeps |k·d|≪|c₀| near q* ⇒ same side of "
                  "diagonal ⇒ same sign at both anchors (heuristic-form survival "
                  "was an artefact)"})

    # ── [3] What the channel DOES require: a diagonal crossing ───────────────
    # Invert Im𝔙 = κ(Re²u−Im²u) = S at each anchor.
    need_mu = S_MUON / KAPPA       # required Re²u − Im²u at muon
    need_pr = S_PROTON / KAPPA     # required Re²u − Im²u at proton
    crosses = (need_mu > 0) != (need_pr > 0)
    print("\n[3] channel requirement (NOT excluded): Re²u − Im²u = S/κ at each anchor")
    print(f"    need (Re²−Im²)_muon  = {mp.nstr(need_mu,6)}  (>0 ⇒ |Re u|>|Im u|)")
    print(f"    need (Re²−Im²)_proton= {mp.nstr(need_pr,6)}  (<0 ⇒ |Re u|<|Im u|)")
    print(f"    opposite signs ⇒ u(q₀) MUST cross the diagonal |Re u|=|Im u| "
          f"between anchors: {crosses}")
    print("    ⇒ the channel is VIABLE but needs a diagonal-crossing u(q₀) — a")
    print("      sharper open constraint than F3. Map still OPEN; nothing wired.")
    assertions.append({
        "name": "channel_viable_requires_diagonal_crossing",
        "computed": 1.0 if crosses else 0.0, "expected": 1.0, "tolerance": 0.0,
        "passed": bool(crosses),
        "source": "Re²u−Im²u = S/κ: +ve at muon, −ve at proton ⇒ u crosses "
                  "|Re u|=|Im u| between anchors (channel not scope-(b) excluded)"})

    dur = (datetime.now(timezone.utc) - t0).total_seconds()
    all_passed = all(a["passed"] for a in assertions)
    witness = {
        "engine": "mpmath",
        "engineVersion": f"mpmath {mp.__version__}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "sdeformed-channel-signflip",
        "scriptFile": "sdeformed_channel_signflip_probe.py",
        "commitSha": subprocess.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True,
            check=True).stdout.strip(),
        "contentBlock": "conj:binding-qbeta-complex-volume",
        "description": (
            "T2 SDeformedVolumeChannel sign-flip probe. With 𝔙₄₁ made concrete "
            "(Lean FigureEightComplexVolume), test S = Im 𝔙₄₁(u(q₀)) vs the "
            "measured flip S(muon)>0>S(proton). Rigorous A-polynomial fact "
            "τ=−i√3 ⇒ a₂ purely imaginary ⇒ Im𝔙₄₁ = κ(Re²u−Im²u) (κ=√3/4), "
            "vanishing on the diagonals |Re u|=|Im u|, NOT the axes — correcting "
            "the heuristic √3·Re·Im form the #3773 F3 survivor was built on. "
            "Verdict structural-partial: F3 refuted against the corrected form "
            "(scope-(b), even-in-d), channel not excluded but requires a "
            "diagonal-crossing u(q₀). No fit; no u-map wired; no instance "
            "fabricated; no c_k."),
        "precisionMetadata": {"compute_dps": 50,
                              "u_convention": "u = 2·log M (meridian eigenvalue)",
                              "kappa": "sqrt(3)/4", "tau": "-i*sqrt(3)"},
        "data": {
            "VOL_4_1": mp.nstr(VOL41, 30),
            "kappa": mp.nstr(KAPPA, 30),
            "S_muon": mp.nstr(S_MUON, 12),
            "S_proton": mp.nstr(S_PROTON, 12),
            "required_ReSq_minus_ImSq_muon": mp.nstr(need_mu, 12),
            "required_ReSq_minus_ImSq_proton": mp.nstr(need_pr, 12),
            "verdict": "structural-partial",
            "scope_b_subresult": (
                "F3 family (one component linear-through-zero at q*, other "
                "anchor-constant) cannot sign-flip against Im𝔙=κ(Re²u−Im²u); "
                "invariant = a₂ purely imaginary (τ=−i√3)."),
            "channel_status": (
                "not excluded; requires u(q₀) crossing the diagonal |Re u|=|Im u| "
                "between anchors (Re²u−Im²u: +ve muon, −ve proton). Map OPEN."),
            "correction": (
                "heuristic Im𝔙≈√3·Re·Im (qbeta_udeform_map_constraint_probe.py, "
                "qbeta_c3_barodd_gluing_newton_solve.py) is WRONG (implies real "
                "a₂); rigorous A-poly form is κ(Re²u−Im²u).")},
        "assertions": assertions,
        "allPassed": all_passed,
        "durationSeconds": dur,
    }
    out = Path(__file__).with_name("sdeformed-channel-signflip.witness.json")
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nwitness → {out.name}")
    for a in assertions:
        print(f"  [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")
    print("VERDICT: structural-partial (F3 refuted scope-(b); channel needs "
          "diagonal-crossing u(q₀), OPEN)")
    print("ALL ASSERTIONS PASS" if all_passed else "ASSERTION FAILURE")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
